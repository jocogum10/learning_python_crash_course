"""def build_profile(first, last, **user_info):
	#Build a dictionary containing everything we know about a user.
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
"""

print("\n\n")
#sandwiches
def my_sandwiches(*sandwiches):
	"""Displays the sandwiches that the user enters."""
	print("\nThis is my chosen sandwiches: ")
	for sandwich in sandwiches:
		print("- " + sandwich)

my_sandwiches('ham')
my_sandwiches('ham', 'cheese', 'mayo')
my_sandwiches('ham', 'egg', 'mayo', 'cheese', 'lettuce')


print("\n\n")
#user profile
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('carlos joco', 'gumanay', location = 'cebu', field = 'engineering', position = 'pilot development engineer')
print(user_profile)


print("\n\n")
#cars
def make_car(manufacturer, model_name, **car_info):
	"""Displays the car details entered by the user."""
	profile = {}
	profile['manufacturer'] = manufacturer
	profile['model'] = model_name
	for key,value in car_info.items():
		profile[key] = value
		
	return profile
	
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)
