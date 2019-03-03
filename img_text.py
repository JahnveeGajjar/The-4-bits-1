# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:20:15 2019

@author: admin
"""
import cv2
import pytesseract
from PIL import Image
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import numpy as np
#from google.cloud import storage
from google.cloud.storage import Blob
import datetime
import urllib.request as request
import io
import requests


src_path = "C:/Users/admin/Desktop/Hackathon/"


cred = credentials.Certificate("C:/Users/admin/Desktop/Hackathon/cred_file.json")

# Initialize the app with a service account, granting admin privileges
#app = firebase_admin.initialize_app(cred, {'storageBucket': 'https://gs://ocrfirebaseproject-a3ad3.appspot.com/uploads',}, name='test_storage7')
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'ocrfirebaseproject-a3ad3.appspot.com',
}, name='storage802')
bucket = storage.bucket(app=app)

blobs = bucket.list_blobs()

files_img = []
files_img_url = []

for blob in blobs:
    files_img.append(blob.name)
    files_img_url.append((blob.name.split('/')[1], blob.public_url))
    #import pdb;pdb.set_trace()
    print(blob.name)



for filename, url in files_img_url:
    im = requests.get(url)
    img_f = io.BytesIO(fd._content)
    imgs = Image.open(img_f)
    text = pytesseract.image_to_string(imgs, lang = 'eng')
    text = text.replace('\n', '')
    text_file = open("C:/Users/admin/Desktop/Hackathon/%s" %(filename.split('.')[0] + '.txt'), "w")
    with open('C:/Users/admin/Desktop/Hackathon/%s' %(filename.split('.')[0] + '.txt'), 'w') as f:
        f.write("text %s" % text.encode("utf-8"))
    
    text_file.close()
    '''
    
fd = requests.get("https://firebasestorage.googleapis.com/v0/b/ocrfirebaseproject-a3ad3.appspot.com/o/uploads%2Fimg3.jpeg?alt=media&token=be94488d-712a-49d5-b643-4a2cbb82ae42")
image_file = io.BytesIO(fd._content)
im = Image.open(image_file)'''
#im = Image.open("https://firebasestorage.googleapis.com/v0/b/ocrfirebaseproject-a3ad3.appspot.com/o/uploads%2Fimg4.jpeg?alt=media&token=50bf1b4c-2efc-49ab-824c-e78c3ab08e5e")
text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
text = text.replace('\n', '')

text_file = open("C:/Users/admin/Desktop/Hackathon/some_file.txt", "w")
#text_file.write("Purchase Amount: %s" % TotalAmount)


with open('C:/Users/admin/Desktop/Hackathon/some_file_1.txt', 'w') as f:
    f.write("text %s" % text.encode("utf-8"))
    
text_file.close()

###############