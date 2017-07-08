import os
import re
import time

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
			time.sleep(0.5)
			print ("\nOrder Received: #" + str(userInput))
			time.sleep(0.5)
			
			for letter in str(userInput):
				time.sleep(0.25)
				print (str(*menu[int(letter)]))	
				order.append(str(*menu[int(letter)]))
				
			orderSum = re.findall("\d+\.\d+", str(order))
			orderAggregate = []
			
			for item in orderSum:
				orderAggregate.append(float(item))
				
			orderAggregate = sum(orderAggregate)
			time.sleep(0.75)
			print ("\nOrder Total: $" + str("%.2f" % orderAggregate) + "\n")
			time.sleep(1)
				
		else:
			print("\nSorry, that won't work, enter an integer")
		
# Keep the program running, 
while True:
	order = []
	start()