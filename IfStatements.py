#!/bin/python3
# -*- coding: utf-8 -*-

#Sample if statements

from random import randint
  
count = randint(1,3)

if count == 1:
	print('The computer picked Kéo')

else:
	if  count == 2:
		print('The computer picked Búa')
	else:
		print('The computer picked Bao')

#We can use elif to reduce the amount of code needed

if count == 1:
	print('The computer picked Kéo')

elif count == 2:
	print('The computer picked Búa')
else:
	print('The computer picked Bao')

#We can use a loop with an if statement to prove the selection is random

loop = 0
while loop != 10:

	count2 = randint(1,3)
	
	if count2 == 1:
		print('The computer has now picked Kéo')
		loop += 1
	elif count2 == 2:
		print('The computer has now picked Búa')
		loop += 1
	else:
		print('The computer has now picked Bao')
		loop += 1
