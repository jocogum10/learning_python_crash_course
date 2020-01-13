import json

filename = 'username.json'

def get_stored_username():
	"""Get stored username if available."""
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Stores another username to the file."""
	new_user = input("What is your name? ")
	with open(filename, 'w') as file_object:
		json.dump(new_user, file_object)
		print("We'll remember you when you come back, " + new_user.title() + "!")
	

def greet_user():
	"""Greets the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username.title() + "!")
	else:
		get_new_username()
		
			
get_stored_username()
user = get_stored_username()

print("Are you " + user.title() + "?")
answer = input("Enter 'yes' if you are. ")

if answer == 'yes':
	greet_user()
else:
	get_new_username()
		
