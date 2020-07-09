#!/usr/bin/python3
import os
from PIL import Image
path=os.getcwd()+"/image"
destination=path #path to directory where new converted 'JPEG' file is to be stored
for filename in os.listdir(path):
  try: #Loop to iterate through source directory file contents
    im=Image.open(path+"/"+filename) #Open image using PIL Library
    im.save(destination+"/"+"new_"+filename,'JPEG') #Saving converted file to destination
  except:
    print("Cannot convert {}".format(filename))
    continue
