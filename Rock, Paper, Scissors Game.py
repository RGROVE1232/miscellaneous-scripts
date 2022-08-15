#!/usr/bin/env python
# coding: utf-8

# In[8]:


###___author___: ryleighjgrove
###___twitter__: Ryleigh_Grove1
###___Code created using Jupyter Notebook, Mon Aug 15 2022

#Import library
import random

#Starting choices for user and computer
start = input('Choose rock, paper, or scissors: ')
possible_choices = ['rock', 'paper', 'scissors']
computer = random.choice(possible_choices)

print('You chose' + start + \n + 'computer chose' + computer)

#Determining a winner
if start == computer:
    print('Both chose {start}. Tie!')
          
elif start == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
          
    else:
        print("Paper covers rock! You lose.")
elif start == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
          
    else:
        print("Scissors cuts paper! You lose.")
elif start == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
          
    else:
        print("Rock smashes scissors! You lose.")


# In[ ]:



