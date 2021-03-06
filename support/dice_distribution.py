# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:24:40 2017

@author: fredrik
"""
import matplotlib.pyplot as plt

# Manual testing throwing the dice
#~ throws = [3, 4, 1, 6, 6, 3, 2, 5, 4, 3,\
          #~ 1, 4, 1, 5, 3, 2, 1, 3, 1, 6,\
          #~ 2, 1, 1, 2, 5, 3, 6, 3, 6, 1,\
          #~ 5, 1, 5, 5, 1, 1, 3, 2, 5, 6,\
          #~ 5, 3, 4, 5, 2, 6, 6, 3, 2, 5,\
          #~ 4, 5, 2, 5, 3, 6, 6, 2, 4, 2,\
          #~ 5, 4, 3, 6, 3, 1, 2, 3, 2, 5,\
          #~ 3, 3, 3, 2, 6, 5, 5, 5, 6, 1,\
          #~ 1, 6, 6, 4, 1, 2, 5, 2, 1, 1,\
          #~ 5, 1, 1, 5, 5, 6, 4, 5, 6, 5]

# "Automated" testing using the Uno and serial port          
throws = [  1,6,2,1,6,6,6,4,4,5,2,5,6,5,3,1,2,4,2,3,\
            6,1,6,1,6,2,5,3,1,1,3,5,5,6,4,2,6,2,5,4,\
            6,3,4,3,4,1,6,2,1,4,4,5,4,6,1,4,1,2,4,6,\
            6,6,1,6,1,4,4,5,5,1,1,2,5,2,1,4,2,4,6,2,\
            2,3,1,6,3,1,4,3,2,6,6,5,4,2,5,6,2,2,2,1,\
            4,3,1,5,3,1,6,6,5,2,2,5,3,5,3,2,6,2,1,1,\
            5,6,6,1,2,3,4,3,4,6,1,4,4,3,1,1,2,6,1,6,\
            6,2,2,5,3,4,2,4,4,6,5,6,3,2,5,1,2,4,4,6,\
            5,5,6,6,2,1,2,2,6,3,6,2,5,5,2,4,3,5,3,2,\
            5,4,4,6,4,1,4,4,4,6,2,5,1,6,2,5,4,6,3,3,\
            6,1,1,3,4,6,4,1,6,2,5,5,3,1,2,1,1,5,2,5,\
            1,3,5,4,2,6,3,3,2,1,4,6,1,3,4,6,1,6,1,1,\
            3,3,3,5,4,3,2,3,1,1,1,1,1,2,5,6,3,4,5,4,\
            4,1,4,3,5,1,2,2,3,6,4,6,6,2,5,2,5,2,4,3,\
            4,3,5,3,1,5,4,2,1,5,2,1,1,1,5,1,5,5,3,4,\
            3,3,2,5,2,2,2,6,2,6,5,3,3,1,1,6,1,6,2,6,\
            2,2,3,1,5,2,3,6,6,1,1,2,4,6,6,1,4,5,2,3,\
            1,5,2,1,5,1,6,3,4,6,6,6,1,5,1,4,2,1,2,4,\
            1,1,6,1,6,6,4,2,6,1,4,2,6,4,6,5,4,4,3,4,\
            5,3,4,3,2,6,3,4,5,6,3,6,4,5,2,6,3,1,6,1,\
            1,2,1,4,3,4,1,1,1,3,4,6,5,6,5,2,2,6,4,3,\
            4,5,1,5,6,4,1,5,3,5,3,6,1,1,2,1,2,1,5,6,\
            6,3,4,4,5,4,1,6,4,2,4,3,3,3,2,3,6,1,4,3,\
            2,2,1,6,4,4,5,4,1,3,2,6,5,6,2,6,3,1,6,4,\
            4,1,1,4,4,2,5,4,6,2,2,5,1,3,2,4,1,4,5,3,\
            1,1,3,5,3,4,1,6,5,5,3,5,2,5,2,6,4,4,3,3,\
            2,5,1,4,2,5,3,1,6,1,5,2,1,3,4,2,2,3,2,6,\
            6,5,2,3,3,2,2,5,1,1,4,2,6,5,5,5,3,2,1,3,\
            3,4,1,6,5,1,1,2,3,5,1,3,5,3,3,6,6,3,5,6,\
            4,4,3,1,5,5,3,6,2,5,5,6,5,3,3,5,2,1,1,6,\
            6,2,3,3,6,5,1,5,6,6,2,5,4,6,3,5,1,6,4,2,\
            6,5,1,5,4,6,3,5,4,1,6,4,1,6,1,3,4,3,3,5,\
            3,3,3,6,5,1,2,1,1,6,5,2,2,1,3,3,6,4,6,2,\
            6,6,4,2,4,5,2,6,4,2,5,4,4,1,3,2,5,5,2,5,\
            6,3,1,1,5,6,5,1,3,5,5,6,6,6,1,6,2,3,3,5,\
            3,3,4,1,6,2,4,1,6,6,4,4,5,5,1,4,3,4,3,3,\
            5,1,2,1,4,3,4,1,4,3,5,5,5,4,6,1,3,5,2,3,\
            3,5,3,5,2,1,1,2,4,4,5,4,6,1,4,3,5,4,1,6,\
            4,4,4,2,2,1,3,1,3,1,2,1,2,6,1,6,4,5,3,5,\
            5,6,1,5,3,4,2,3,2,4,4,6,1,2,5,1,2,2,1,6,\
            6,4,6,5,2,1,6,3,3,3,5,4,5,4,4,6,1,6,4,1,\
            3,4,1,6,6,6,3,6,5,2,5,2,5,3,5,1,2,5,3,1,\
            4,5,1,5,4,4,5,6,1,3,4,5,1,4,1,1,2,2,4,2,\
            2,6,1,6,3,4,1,4,3,5,5,2,1,3,3,6,3,2,6,3,\
            3,1,1,5,2,3,2,6,5,5,4,6,3,4,3,6,1,2,5,1,\
            6,5,4,1,5,3,3,1,1,1,5,5,3,1,1,5,5,5,3,5,\
            5,1,5,2,2,4,3,4,6,6,1,5,1,5,2,6,4,1,4,6,\
            6,4,6,4,3,4,3,1,5,6,3,5,2,1,5,4,1,3,5,5,\
            6,6,4,5,3,1,3,6,4,4,3,4,4,5,6,4,5,6,1,1,\
            5,5,5,4,2,2,6,5,4,6,1,4,5,6,3,4,6,1,5,1]

numbers = [1,2,3,4,5,6]   
freq = [throws.count(num) for num in numbers]       
#plt.hist(throws, bins=6)
fig = plt.bar(numbers, freq, align='center')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Distribution of %d dice throws' % (len(throws)))
plt.show()