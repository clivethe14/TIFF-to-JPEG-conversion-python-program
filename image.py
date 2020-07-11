#!/usr/bin/python3
import os
from PIL import Image

path=input("Enter absolute path to imagess directory:")  #path to source folder conatining .tif images
destination=input("Enter absolute path to directory the converted files need to be stored in:") #path to directory where new converted 'JPEG' file is to be stored

for filename in os.listdir(path):  #Loop to iterate through source directory file contents
  try: 
    nfilename=filename.split(".")
    im=Image.open(path+"/"+filename) #Open image using PIL Library
    im.save(destination+"/"+"new_"+nfilename[0]+".jpeg",'JPEG') #Saving converted file to destination
  except:
    print("Cannot convert {}".format(filename))
    continue
