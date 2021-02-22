#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import functions as f
import datetime
import gc


# In[ ]:





# In[ ]:


#Tradable Symbols
def get_symbols(sym):
    
    switcher = {
        
        #List of Desired Instruments
        0: 'EUR_CHF',
        1: 'EUR_GBP',
        2: 'EUR_USD',
        3: 'USD_CHF',
        4: 'GBP_USD',
        5: 'EUR_AUD',
        6: 'AUD_CHF',
        7: 'CHF_JPY',
        8: 'EUR_JPY',
        9: 'GBP_JPY',
        
        10: 'USD_CAD',
        11: 'AUD_USD',
        12: 'NZD_USD',
        13: 'USD_JPY',
        14: 'USD_SGD',
        15: 'AUD_CAD',
        16: 'CAD_JPY',
        17: 'AUD_NZD',
        18: 'AUD_JPY',
        19: 'NZD_JPY',
        
        20: 'GBP_AUD',
        21: 'EUR_NZD',
        22: 'GBP_CAD',
        23: 'CAD_CHF',
        24: 'GBP_NZD',
        25: 'EUR_CAD',
        26: 'GBP_CHF',
        27: 'AUD_SGD',
        28: 'NZD_CHF',
        29: 'SGD_JPY',
        30: 'NZD_CAD',
        
    }
    
    return switcher.get(sym, 'ERR')


# In[ ]:





# In[ ]:





# In[ ]:


def main():
    
    ts = round(datetime.datetime.now().timestamp(), 0)
    print(" ")
    print("OFDC: Activated at " +  str(ts))
    print(" ")
    
    #Update all Tradeable Symbols
    for i in range(31):

        try:
            sym = get_symbols(i) 
            df1 = f.get_data(sym)
            f.update_db(df1, sym)
        except:
            print("ERR. Get and Update - " + sym)
            continue
    
    #Post DB
    f.post_db() 
    ts2 = round(datetime.datetime.now().timestamp(), 0)
    tim = round(((ts2 - ts)/60), 2)    
    msg = f"OFDC: Done, Deactivated in {tim} Minutes." 
    print(" ")
    print(msg)
    
    return None


# In[ ]:





# In[ ]:





# In[ ]:


if __name__ == "__main__":
    main()
    gc.collect()    
    quit()


# In[ ]:





# In[ ]:





# In[ ]:




