#!/bin/python3
# -*- coding: utf-8 -*-

#Sample if statements

from random import randint

loop = 0
while loop != 10:

	count = randint(1,3)
	
	if count == 1:
		print('The computer has now picked Kéo')
		loop += 1
	elif count == 2:
		print('The computer has now picked Búa')
		loop += 1
	else:
		print('The computer has now picked Bao')
		loop += 1
