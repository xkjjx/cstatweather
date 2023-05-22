from instagramKeys import *
from postGenerator import createPostText
import time
import requests

cstatPlaceID = 4682464

def IGImageURL(ctime):
    year, month, day, hour, minute, sec, wday, tday, dst = ctime
    if day < 9:
        day = "0" + str(day)
    else:
        day = str(day)

    if month < 9:
        month = "0" + str(month)
    else:
        month = str(month)

    return "https://res.cloudinary.com/dzygv07en/image/upload/" + str(3600*hour + 60*minute + sec) + month + "/" + day + "/" + str(year)

def cstatTime():
    return time.localtime()


def renewToken(accessToken):
    url = graphURL + "oauth/access_token"
    param = {"grant_type":"fb_exchange_token","client_id":appID,"client_secret":appSecret,"fb_exchange_token":accessToken}
    response = requests.get(url=url,params=param).json()
    print(response)
    outP = response["access_token"]
    return outP


def uploadImage(imageURL,caption):
    url = graphURL + igAccountID + "/media"
    param = {"access_token":longAccessToken,"caption":caption,"image_url":imageURL}
    response = requests.post(url,params=param)
    response = response.json()
    return response


def postOnIG():
    ctime = cstatTime()
    caption,imageSaved = createPostText(cstatPlaceID,ctime,False)
    if imageSaved:
        picURL = IGImageURL(ctime)
        response = uploadImage(picURL,caption)
        print(response)
        print("Instagram Image URL:\n" + picURL)
        print("Instagram Post Text:\n" + caption)
        containerID = response['id']
        url = graphURL + igAccountID + "/media_publish"
        param = {"access_token":longAccessToken,"creation_id":containerID}
        requests.post(url,params=param)
        print("Succesfully posted on Instagram\n")
    else:
        print("No image found - Instagram post not completed\n")

