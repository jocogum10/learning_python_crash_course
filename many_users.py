users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		}
	}

for username,user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())

print("\n\n")
#people
person_1 = {
	'name': 'carlos',
	'age': 26,
	'location': 'cebu',
	}
person_2 = {
	'name': 'bantot',
	'age': 25,
	'location': 'cebu',
	}
person_3 = {
	'name': 'myu',
	'age': 8,
	'location': 'cebu',
	}
	
people = [person_1, person_2, person_3]

for pipz in people:
	print("\n")
	for details in pipz.values():
		print(details)


#pets
lycan = {
	'kind': 'dog',
	'owner': 'mama',
	}
kylakay = {
	'kind': 'cat',
	'owner': 'papa',
	}
kafka = {
	'kind': 'mouse',
	'owner': 'fam',
	}

pets = [lycan, kylakay, kafka]

for pet in pets:
	print("\nOur pets and owners: ")
	for details in pet.values():
		print(details)

print("\n\n")
#favorite places
favorite_places = {
	'me': ['cebu', 'lapu lapu', 'north'],
	'you': ['mactan', 'basak', 'south'],
	'us': ['pardo', 'lahug', 'hipodromo'],
	}

for name, places in favorite_places.items():
	print(name)
	for place in places:
		print("\t" + place)

print("\n\n")
#favorite_numbers
favorite_number = {
	'me': [1, 3, 5],
	'you': [2, 4, 6],
	'us': [34, 61, 52],
	}

for name, numbers in favorite_number.items():
	print(name + ":")
	for number in numbers:
		print("\t" + str(number))


print("\n\n")
#cities
cities = {
	'cebu': {'population': 123, 'region': 'region 7', 'fact' : 'I dont',},
	'lapu lapu': {'population': 456, 'region': 'region 3', 'fact' : 'know',},
	'bohol': {'population': 789, 'region': 'region 8', 'fact' : 'yet',},
	}

for name,details in cities.items():
	print("\n" + name + ":")
	for keys, values in details.items():
		print(keys + " : " + str(values) + ".")

print("\n\n")
#extensions
