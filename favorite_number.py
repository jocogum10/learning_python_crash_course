import json

filename = 'favorite_number.json'

try:
	with open(filename) as file_object:
		message = json.load(file_object)
except FileNotFoundError:
	with open(filename, 'w') as file_object:
		message = input("What is your favorite number? ")
		json.dump(message, file_object)
else:
	print("I know your favorite number! It's " + message + "!")
	
