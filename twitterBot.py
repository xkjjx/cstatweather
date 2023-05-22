import time
import tweepy
from twitterKeys import *
from postGenerator import createPostText
cstatPlaceID = 4682464


def postOnTwitter():
    cstatTime = time.localtime()
    postText,imageSaved = createPostText(cstatPlaceID,cstatTime,True)
    print("Twitter Post Text: \n" + postText)

    client = tweepy.Client(bearerToken,key,keySecret,accessToken,accessTokenSecret)
    auth = tweepy.OAuthHandler(key,keySecret)
    auth.set_access_token(accessToken,accessTokenSecret)
    api = tweepy.API(auth)

    if imageSaved:
        media = api.media_upload("landscapepic.jpeg")
        client.create_tweet(text=postText,media_ids=[media.media_id])
        "Succesfully posted with image landscapepic.jpeg\n"
        pass
    else:
        client.create_tweet(text=postText)
        "Succesfully posted without image\n"
        pass
