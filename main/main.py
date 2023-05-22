from twitterBot import postOnTwitter
from instagramBot import postOnIG


def postAll():
    postOnTwitter()
    postOnIG()


postAll()
