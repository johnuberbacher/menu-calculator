import os
	
# Configure and load menuArray items into memory
menuArray = []
with open('menu.txt') as inputfile:
	for line in inputfile:
		menuArray.append(line.strip().split(','))

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
				print ("Your item: " + str(*menuArray[int(letter)]))	
		else:
			print("\nSorry, that won't work, enter an integer")
		
# Keep the program running, 
while True:
	start()