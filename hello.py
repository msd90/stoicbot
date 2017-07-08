import tweepy
import time


consumer_key = '55I6fdWEFalD20kJW7lIQ9ScK'
consumer_secret = 'ExyQtnjeoBSpYmLMr020qe9VyKHh4GQ57dxygUEROd1J6kZNkj'
access_token ='139634825-q4Pjzglzg5LxUkjVxdC5tZHhTUCFPsNiUJOoVNij'
access_token_secret ='6WpAC7WBKgMACagXmsI3zYb5y2adgq7W8f4zjdhVh4d6j'

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
    time.sleep(30)
    i+=1
    if i == 10:
        #file.seek(0)
        #i = 0
        print "done"
        break


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
