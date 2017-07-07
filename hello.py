import tweepy
import urllib


consumer_key = '55I6fdWEFalD20kJW7lIQ9ScK'
consumer_secret = 'ExyQtnjeoBSpYmLMr020qe9VyKHh4GQ57dxygUEROd1J6kZNkj'
access_token ='139634825-q4Pjzglzg5LxUkjVxdC5tZHhTUCFPsNiUJOoVNij'
access_token_secret ='6WpAC7WBKgMACagXmsI3zYb5y2adgq7W8f4zjdhVh4d6j'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#api.update_status('Testing my first tweet using an API!')

file = open('quotes.txt', 'r')
print file.read()
