user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'}
	
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
		
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	language.title() + ".")

for name in favorite_languages.keys():
	print(name.title())

###
print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")
		
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")
	
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
	
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
	
#rivers
rivers = {'nile': 'egypt',
	'mississipi': 'United States of America',
	'pasig': 'philippines',
	}
	
for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title() + ".")
for river in rivers.keys():
	print(river.title())
for country in rivers.values():
	print(country.title())


#Polling
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
people = ['carlos', 'jen', 'sarah', 'xander', 'carlito', 'edward', 'phil']

for name in people:
	print(name.title())
	
	if name in favorite_languages.keys():
		print("Hi " + name.title() + ", thank you for taking the poll!")


