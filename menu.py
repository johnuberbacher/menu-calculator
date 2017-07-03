import os

menu = []
textFile = open("menu.txt")
lines = textFile.readlines()
for line in lines:
	menu.append(line.split(" "))

data = input("Enter a string of numbers: ")
try:
	data = int(data)
except ValueError:
	print("\nSorry, enter an integer")
else:
	if data > 0:
		for letter in data:
			print (str(letter))
	else:
		print("\nSorry, that won't work, enter an integer")
			

