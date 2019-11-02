import tweepy
import time
import random

consumer_key = ''
consumer_secret = ''
access_token =''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#takes in text file and numerates the text file lines
#returns line with text at random
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line

file = open('quotes.txt', 'r')
while (True):
    tweet = random_line(file)
    api.update_status(tweet) #comment this line out if you do not want the tweets updating to the bot account
    tweet_flag = 1
    #print (tweet) #uncomment to print tweet on command line
    if(tweet_flag==1):
        time.sleep(86400) #sleep for the next 86400 seconds (24 hours)
        tweet_flag = 0
    file.seek(0)