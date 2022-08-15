#!/usr/bin/env python
# coding: utf-8

# In[20]:


###___author___: ryleighjgrove
###___twitter__: Ryleigh_Grove1
###___Code created using Jupyter Notebook, Sun Aug 14 2022

#Import libraries
import pytube
from time import time

start = time() #To view execution time, leave this open

def repeat():
    
    #Asking user for input
    link = input('What is the link to the video? ')
    path = input('What is the path you would like to save under? \n ***Example on MacOS: /Users/ryleighjgrove/Downloads \n ***Example on Windows: C:\\Users\\rgrove\\Downloads')

    #Pulling video from link inputted by user
    pytube.YouTube(link).streams.get_highest_resolution().download(path)
    print('Video Downloaded!')

    #Asking user if they would like to continue downloading video
    cont = input('Would you like to download more videos? Y or N ')

    if cont == 'Y':
        repeat()
        
    if cont == 'N':
        print('Thank you!')

repeat()

#To view execution time, leave the following open
end = time()
execution_time = end - start
print('Execution Time: ', execution_time)


# In[ ]:




