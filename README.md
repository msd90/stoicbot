# stoicbot
Uses the twitter API (tweepy) to print out text from quotes.txt running on Heroku.

To see this in action see https://twitter.com/StoicQuoteBot


# How to run this locally:

1. Download the file contents in a single folder
2. Make sure you have ```pip``` installed and inside the downloaded folder run ```pip install -r requirements.txt```
3. Inside ```start.py``` you will need your own set of token and access keys from https://developer.twitter.com/ 
4. Once those keys are generated you can copy and paste them in the ```start.py``` file:

`consumer_key =    '(insert key here from https://developer.twitter.com/  )`\
`consumer_secret = '(insert key here from https://developer.twitter.com/) '`\
`ccess_token =     '(insert key here from https://developer.twitter.com/)'`\
`access_token_secret = '(insert key here from https://developer.twitter.com/)'`

5. Inside `start.py`, change the `time.sleep(86400)` to `time.sleep(3)'` to see the tweets updated from the script
6. Run `python start.py` 





