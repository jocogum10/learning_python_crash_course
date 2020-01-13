import json

filename = 'favorite_number.json'

with open(filename) as file_object:
	message = json.load(file_object)
	
print("I know your favorite number! It's " + message + "!")
