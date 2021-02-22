#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[ ]:





# In[2]:

import json
import yaml
import boto3
import ntplib
import sqlite3
import requests
import datetime
import numpy as np
import pandas as pd

from dateutil import parser
from botocore.client import Config
from datetime import date, timedelta


# In[ ]:





# In[ ]:





# In[3]:


def get_data(sym):
    
    #Configurations
    with open('./config/config.yaml') as file:
        config = yaml.safe_load(file)
        
    authorization = config['configuration']['authorization'] 
    url = config['configuration']['oanda']
    granuality = config['configuration']['granuality']
    data_start = config['configuration']['data_start']
    data_end = config['configuration']['data_end']
    price = config['configuration']['price']
    
    
    #Get Time
    x = ntplib.NTPClient()
    
    try:
        now = datetime.datetime.utcfromtimestamp(x.request('uk.pool.ntp.org').tx_time)
    except:
        try:
            now = datetime.datetime.utcfromtimestamp(x.request('europe.pool.ntp.org').tx_time)
        except:
            now = datetime.datetime.now()
            
            
    def check_weekday(date):
        # Mon-Fri (0-4)
        while date.weekday() > 4: 
            date -= timedelta(days=1)
        return date
    
    
    #Time to Epoch
    start = now.replace(hour=data_start, minute=0, second=0, microsecond=0)
    end = now.replace(hour=data_end, minute=0, second=0, microsecond=0)
    weekday_start = check_weekday(start)
    weekday_end = check_weekday(end)
    start_epoch = weekday_start.timestamp()
    end_epoch = weekday_end.timestamp()
    

    #Headers and Parameters
    payload_1 = {'from': start_epoch, 'to': end_epoch, 'price': price, 'granularity': granuality}
    auth = {"Authorization": "Bearer " + authorization}
    url = url + sym + "/candles" 
    
    
    #Request 1
    response = requests.get(url, params=payload_1, headers=auth)     
    raw = response.json()
    data = json.dumps(raw, indent=2)
    dataset = pd.read_json(data)
    df = pd.json_normalize(dataset['candles'])
    del df['complete']

    df['time'] = pd.to_datetime(df['time']).dt.tz_localize(None)
    df.columns = ['vol','time', 'open','high','low', 'close']
    df1 = df[['time','vol','high','low','open', 'close']]
    
    return df1


# In[ ]:





# In[ ]:





# In[4]:


def update_db(df_one, symbol):
    
    #Configurations
    with open('./config/config.yaml') as file:
        config = yaml.safe_load(file)
        
    db_path = config['locations']['db_path']
    granuality = config['configuration']['granuality']
    
    table_one_name = symbol + "_" + granuality
    conn = sqlite3.connect(db_path)
    
    try:
        
        #Check if Data Exists
        query = "SELECT * FROM [" + table_one_name + "]"
        temp_date = pd.read_sql_query(query, conn)
    
        last_r_time = parser.parse(temp_date.at[(len(temp_date.index) - 1), 'time'])
        current_r_time = parser.parse(str(df_one.at[(len(df_one.index) - 1), 'time']))
    
        if(last_r_time >= current_r_time):
            print("Record Exists in Local DB - " + symbol)   
        else:
            #Update
            df_one.to_sql(name=table_one_name, con=conn, if_exists='append')
            print("Local DB Updated - " + symbol)
        
    except:
        #Insert
        df_one.to_sql(name=table_one_name, con=conn, if_exists='replace')
        print("Local DB inserted - " + symbol)
    
    conn.close()
        
    return None


# In[ ]:





# In[ ]:





# In[5]:


def post_db():

    #Configurations
    with open('./config/config.yaml') as file:
        config = yaml.safe_load(file)
        
    minio_key = config['settings']['minio_key']
    minio_access = config['settings']['minio_access']
    
    db_path = config['locations']['db_path']
    server_path = config['locations']['server_path']
    server_bucket = config['locations']['server_bucket']

    
    #Get Time
    x = ntplib.NTPClient()
    
    try:
        now = datetime.datetime.utcfromtimestamp(x.request('uk.pool.ntp.org').tx_time)
    except:
        try:
            now = datetime.datetime.utcfromtimestamp(x.request('europe.pool.ntp.org').tx_time)
        except:
            now = datetime.datetime.now()
    

    #Upload
    try:
        s3 = boto3.resource('s3', endpoint_url=server_path, aws_access_key_id=minio_key, 
                            aws_secret_access_key=minio_access,
                            config=Config(signature_version='s3v4'), 
                            region_name='us-east-1' )
        
        posting_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        file = str(posting_date.weekday()) + "-OANDA.db"
        
        s3.Bucket(server_bucket).upload_file(db_path, file)       
        print("Upload Successful.")
     
    except:
        print("Upload Failed.")

    return None


# In[ ]:





# In[ ]:





# In[ ]:




