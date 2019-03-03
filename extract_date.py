# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:18:45 2019

@author: admin
"""

import pytesseract
from PIL import Image
import os
import re
from fuzzywuzzy import process


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img= Image.open('Screenshot (192).png')
text = pytesseract.image_to_string(img)
#print(text)
str=text




all= re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}",str)
#all= re.findall(r"[\d]{1,2}\s(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s[\d]{4}",str)

for s in all:
    print('Date found',s)

