import cloudinary
from cloudinary.uploader import upload
from cloudinaryKeys import *

def cloudinaryUpload(name,localName="portraitpic.jpeg"):
    cloudinary.config(cloud_name = cloudName, api_key = key, api_secret = keySecret, secure = True)
    url = upload(localName, public_id=name)["url"]

