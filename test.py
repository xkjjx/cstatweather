import sys
from instagramBot import cstatPlaceID,cstatTime,renewToken
from postGenerator import makeImage,createPostText
from instagramKeys import *
import time

print(createPostText(cstatPlaceID,cstatTime(),False))
