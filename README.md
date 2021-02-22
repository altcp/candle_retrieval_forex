# candle_retrieval_oanda
Get Candles from Oanda V20 API (CRON)<br/><br/><br/>

## Overview

The tool retrieves price information from OANDA and appends it into a local sqllite database ("db") on a daily basis. It then uploads the appended db file to a S3 or S3-like server using boto3.<br/><br/><br/>

## Instructions for the use of a release
Python 3.8.5 was the python version used in testing prior to containerization.<br/>
Ubuntu Server 20.04.2 LTS on Raspberry Pi 4 2GB was the testing environment.
You may need to create a log folder in the base folder to store error logs.
<br/><br/>

In the Linux Terminal navigate to the base folder:<br/>

1. To first install required dependencies, TYPE: pip install -r requirements.txt<br/>
2. To run the CRON JOB on a daliy basis, crontab setup.cron<br/>
3. Make Executable shell scripts (i.e., run.sh) and python files (i.e., main.py and functions.py) using chmod +x 
<br/><br/>

To configure this, navigate to the config subfolder and edit the config.yml file - Instructions Within.<br/><br/><br/>

## Discussion

I aim to write clear, simple and clean code so that others can inspect, maintain or append with ease. Sponsoring me helps others navigate better (e.g., with speed, simplicity and etc.) as it allows me to focus on delivering a better product or thing than on paying the bills.<br/><br/>

You can do this thru GitHub Sponsors if and when it is made available to me.<br/><br/><br/>

## Disclaimer

I bear no responsibilty for any loss or financial loss incurred by you or by anyone as a result of providing this automation.<br/><br/><br/>

## Contributing

You can contribute by informing me of typos, bugs, errors, omissions, improvements and general feedback. Further, please see CONTRIBUTING.md<br/><br/><br/>

