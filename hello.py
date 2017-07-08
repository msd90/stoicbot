import tweepy
import time


consumer_key = 'insert here'
consumer_secret = 'insert here'
access_token ='insert here'
access_token_secret = 'insert here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#count=0
#while True:
#    api.update_status(count)
#    count = count + 1
#    time.sleep(60)

file = open('quotes.txt', 'r')
i=0
while (True):
    tweet = file.readline()
    api.update_status(tweet)
    #print tweet
    time.sleep(86400)
    i+=1
    if i == 75:
        file.seek(0)
        i = 0
        #print "done"



#chars = words = lines = 0
#file = 'quotes_test.txt'
#with open(file, 'r') as in_file:
#    for line in in_file:
#        lines += 1
#        chars += len(line)
        #print lines, chars
#        if (chars <= 140):
#            print line
#        time.sleep(2)
#        chars = 0
