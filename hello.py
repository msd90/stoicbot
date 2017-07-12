import tweepy
import time
import random


consumer_key = 'insert here'
consumer_secret = 'insert here'
access_token ='insert here'
access_token_secret = 'insert here'

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
    api.update_status(tweet)
    #print tweet
    time.sleep(43200)
    file.seek(0)
