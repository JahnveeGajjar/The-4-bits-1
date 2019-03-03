import pytesseract
from PIL import Image
import os
import re
from fuzzywuzzy import process


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img= Image.open('Screenshot (192).png')
text = pytesseract.image_to_string(img)
print(text)


g = open("invoice.txt","w+")
for i in text:
     g.write(text)
g.close()

#print('final', final_amount)
with open('invoice.txt','r') as f:
     comps= f.read().split("\n")
len(comps)
def get_matches(query,choices,limit=1):
     results = process.extract(query,choices,limit=limit)
     print(results)

get_matches('Limited ', comps)











































##all= re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}",str)
#all= re.findall(r"[\d]{1,2}\s(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s[\d]{4}",str)

##for s in all:
##    print('Date found',s)
##
##
##
'''
for line in str:
    line= line.strip()
    y = re.findall('( [0-9]+)',line)
#print(y)
if len(y)>0:
    print(sum(map(int,y)))

##m= max(y)
##print(m)

'''
##def extractMax(input): 
##  
##     # get a list of all numbers separated by  
##     # lower case characters  
##     # \d+ is a regular expression which means 
##     # one or more digit 
##     # output will be like ['100','564','365'] 
##     numbers = re.findall('\d+',input) 
##  
##     # now we need to convert each number into integer 
##     # int(string) converts string into integer 
##     # we will map int() function onto all elements  
##     # of numbers list 
##     numbers = map(int,numbers)
##     print( max(numbers))
##
##
##p = extractMax(str)
##print(p)

