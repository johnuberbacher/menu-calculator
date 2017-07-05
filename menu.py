import os
import re

# Configure and load menu items into memory
menu = []
with open('menu.txt') as inputfile:
	for line in inputfile:
		menu.append(line.strip().split(','))

def start():
	# Prompt user for orders
	# TODO exit command(s)
	userInput = input("Enter a string of numbers: ")
	try:
		userInput = int(userInput)
	except ValueError:
		print("\nSorry, enter an integer")
	else:
		if userInput >= 0:
			print ("\nOrder Received: #" + str(userInput))
			for letter in str(userInput):
				print (str(*menu[int(letter)]))	
				order.append(str(*menu[int(letter)]))
			
			print(*order)
			orderSum = re.findall("\d+\.\d+", str(order))
			print(*orderSum)
			
		else:
			print("\nSorry, that won't work, enter an integer")
		
# Keep the program running, 
while True:
	order = []
	start()