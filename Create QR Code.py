#!/usr/bin/env python
# coding: utf-8

# In[1]:


###___author___: ryleighjgrove
###___twitter__: Ryleigh_Grove1
###___Code created using Jupyter Notebook, Sun Aug 14 2022
    
#Import libraries
import os
import pyqrcode
from time import time

start = time() #To view execution time, leave this open

linkForQR = input('What is the link you would like a QR for? ')
link = linkForQR

qr_code = pyqrcode.create(link)

#Saving the QR code
directoryPath = input("What is the directory path you would like the QR saved? \n ***Example on MacOS: /Users/ryleighjgrove/Downloads \n ***Example on Windows: C:\\Users\\rgrove\\Downloads ")
nameOfImage = input("What would you like to save the QR code as? ")
qr_code.png(directoryPath + '/' + nameOfImage, scale = 5)
print("QR Created!")

#To view execution time, leave the following open
end = time()
execution_time = end - start
print('Execution Time: ', execution_time)

