requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
	
print("\nFinished making your pizza!")


print("\n")

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_toppings + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")



print("\n")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
		
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")


#hello admin
print("\n")
users = ['anton', 'bea', 'cris', 'admin', 'dennis']

for user in users:
	if user == 'admin':
		print("Hello " + user.lower() + ", would you like to see a status report?")
	else:
		print("Hello " + user.title() + ", thank you for logging in again.")

#add an if statement to make sure list is not empty
print("\n")
#users = ['anton', 'bea', 'cris', 'admin', 'dennis']
users = []

if users:
	for user in users:
		if user == 'admin':
			print("Hello " + user.lower() + ", would you like to see a status report?")
		else:
			print("Hello " + user.title() + ", thank you for logging in again.")
else:
	print("We need to find some users!")


#checking usernames
current_users = ['anton', 'bea', 'cris', 'admin', 'dennis']
new_users = ['ANTON', 'beatrice', 'cristian', 'admin1', 'dennis']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Please enter a new user name. Name is existing.")
	else:
		print("Username is available.")


#ordinal numbers
ordinal_numbers = list(range(1,10))

for ordinal_number in ordinal_numbers:
	if (ordinal_number == 1):
		print(str(ordinal_number) + "st")
	elif (ordinal_number == 2):
		print(str(ordinal_number) + "nd")
	elif (ordinal_number == 3):
		print(str(ordinal_number) + "rd")
	else:
		print(str(ordinal_number) + "th")
