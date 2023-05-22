import tweepy
import time
from twitterKeys import *

client = tweepy.Client(bearerToken,key,keySecret,accessToken,accessTokenSecret)
auth = tweepy.OAuthHandler(key,keySecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

tag = client.get_me()[0]["id"]
print(tag)
print(client.get_user(id=tag))
#print(api.get_user(id=tag))
