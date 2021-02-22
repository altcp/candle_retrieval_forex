# candle_retrieval_oanda
Get Candles from Oanda V20 API (CRON)<br/><br/><br/>

## Overview

The tool retrieves price information from OANDA and appends it into a local sqllite database on a daily basis. It then uploads the appended db file to a S3 or S3 like server using Boto3.<br/><br/><br/>

## Instructions for the use of a release
Python 3.8.5 was the python version used in testing prior to containerization.<br/>
Ubuntu Server 20.04.2 LTS on Raspberry Pi 4 2GB was the testing environment.
You may need to create a log folder in the base folder to store error logs.
<br/><br/>

In the Linux Terminal navigate to the base folder:<br/>

1.To first install required dependencies, TYPE: pip install -r requirements.txt<br/>
2.To run the CRON JOB on a daliy basis, crontab setup.cron<br/><br/>

To configure this, navigate to the config subfolder and edit the config.yml file - Instructions Within.<br/><br/><br/>

## Discussion

I aim to write clear, simple and clean code so that others can inspect, maintain or append with ease. Sponsoring me helps others navigate better (e.g., with speed, simplicity and etc.) as it allows me to focus on delivering a better product or thing than on paying the bills.<br/><br/>

You can do this thru GitHub Sponsors if and when it is made available to me.<br/><br/><br/>

## Disclaimer

Ideal Condition(s) are a set of assumptions taken in some model(s) used in Fundamental Analysis. Despite such formal methods, the world we live in is seldom or never ideal. Making considered or control assumptions simplify the complex world we live in and such is often or can be the manner in which the scientific community communicates.<br/><br/> 

While I can or may over time code out such formal methods, it cannot with or without relevant alternative data sources truly ignore, avoid or be absent of the standard provided by the attestation process or the additional due diligence conducted on the buy-side. It is the sum of these that approximates Idea Conditions.<br/><br/>

The techniques being automated here are not immune to such assumptions or assumptions in general. The outlook provided by the automation with regards to price action is therefore not definitive in nature, but indicative with varying degree(s) of error. This is the general case or the case for all types of financial analysis.
<br/><br/>

Without proven Artificial Intelligence and despite a provision for alternative data sources thru a function implementing the use of that, it is up to the user to make the necessary inference using acumen and to exercise prudence in execution.<br/><br/>

Nonetheless, everyone should exercise caution when reviewing the output of the automation and should seek independent financial advice when unsure before making any type of financial decision(s).<br/><br/>

I bear no responsibilty for any loss or financial loss incurred by you or by anyone as a result of providing this automation.<br/><br/><br/>

## Contributing

You can contribute by informing me of typos, bugs, errors, omissions, improvements and general feedback. Further, please see CONTRIBUTING.md<br/><br/><br/>

