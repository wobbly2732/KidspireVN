#!/bin/python3
# -*- coding: utf-8 -*-

#using a function to ensure a valid selection is made

#Player1 function
def Player1():
	choice = input('Select Kéo (ke), Búa (bu), Bao (ba): ')

	if choice == 'ke':
		print('You chose Kéo')
	elif choice == 'bu':
		print('You chose Búa')
	elif choice == 'ba':
		print('You chose Bao')
	else:
		print('Make another choice')
		Player1() #creates a loop for invalid entries

#Calls Player1 function with no inputs
Player1()