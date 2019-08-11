#!/bin/python3
# -*- coding: utf-8 -*-

#import modules
from random import randint #imports the random integer module

count = 0 # we set the count variable to 0
while count != 10: #the loop will run while count isn't equal to 10

	chosen = randint(1,3) #use the random integer module to pick a number between 1 & 3
	print('Count = ',count , ' Chosen = ',chosen) #display the values of count & chosen
	count += 1 #increase the value of count by 1
