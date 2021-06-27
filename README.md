# candle_retrieval_oanda
Get Candles from Oanda V20 API (CRON)<br/><br/><br/>

## Overview

The tool retrieves price information from OANDA and appends it onto a local sqllite database ("db"). The tool then uploads the appended db file to a S3 or S3-like server using boto3. This is done on a daliy basis using cron.<br/><br/><br/>

## Instructions for the use of a release
Python 3.8.5 was the python version used.<br/>
Ubuntu Server 20.04.2 LTS on Raspberry Pi 4 2GB was the testing environment.<br/>
MINIO on Raspberry Pi 4 4GB was the S3-like backup server used.
<br/><br/>

In the Linux Terminal navigate to the base folder:<br/>

1. To first install required dependencies, TYPE: pip install -r requirements.txt<br/>
2. To run the CRON JOB on a daliy basis, crontab setup.cron<br/>
3. Make Executable shell script (i.e., run.sh) and python files (i.e., main.py and functions.py) using chmod +x 
<br/><br/>

To configure this, navigate to the config subfolder and edit the config.yml file - Instructions Within.<br/><br/><br/>


## Contributing
Superceeded
<br/><br/><br/>

