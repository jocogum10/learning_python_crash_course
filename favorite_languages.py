favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() 
	+ ".")

print("Jen's favorite language is " +
	favorite_languages['jen'].title()
	+ ".")


#Person
person = {'first_name':'carlos',
		'last_name':'gumanay',
		'age':'26',
		'city':'cebu'}

print("Name: " + person['first_name'].title() 
	+ " " +person['last_name'].title())
print("Age: " + person['age'])
print("Lives in: " + person['city'].title() + " City")

#favorite numbers
favorite_numbers = {'juan':1,
	'bea': 5, 
	'cris': 8, 
	'rod': 7, 
	'greg': 4}

print("Juan's favorite number is " + str(favorite_numbers['juan']))
print("Bea's favorite number is " + str(favorite_numbers['bea']))
print("Cris' favorite number is " + str(favorite_numbers['cris']))
print("Rod's favorite number is " + str(favorite_numbers['rod']))
print("Greg's favorite number is " + str(favorite_numbers['greg']))

#Glossary
glossary = {'for': 'loop statement',
	'if': 'conditional statement',
	'list': 'stores series of items like an array',
	'tuples': 'unchangable list',
	'dictionary': 'stores information/characteristics of an object'}

print("A For is: " + glossary['for'])
print("An If is: " + glossary['if'])
print("A list is: " + glossary['list'])
print("A tuples is: " + glossary['tuples'])
print("A dictionary is: " + glossary['dictionary'])

#glossary 2

for name in favorite_numbers.keys():
	print(name.title() + "'s favorite number is " + str(favorite_numbers[name]))

for item in glossary.keys():
	print("A " + item.title() + " is: " + glossary[item] + ".")
