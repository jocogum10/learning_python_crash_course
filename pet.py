"""def describe_pet(animal_type, pet_name):
	#Display information about a pet.
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(animal_type = 'rat', pet_name = 'richie')
describe_pet(pet_name = 'ralph', animal_type = 'rabbit')
"""

def describe_pet(pet_name, animal_type = 'dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'willie')
describe_pet('willie')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')

#a dog named willie
describe_pet('willie')
describe_pet(pet_name='willie')

#a hamster named harry
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')


print("\n\n")
#t-shirt
def make_shirt(size, message):
	"""displays the size of the shirt and the message"""
	print("The size of the shirt is " + size + ".")
	print("Message: " + message.title())
	
make_shirt('extra large', 'I am inevitable')
make_shirt(size = 'medium', message = 'i am iron man')

print("\n\n")
#large shirts
def make_shirt(size = 'large', message = 'I love Python'):
	"""displays the size of the shirt and the message"""
	print("The size of the shirt is " + size + ".")
	print("Message: " + message.title())
	
make_shirt()
make_shirt('medium')
make_shirt('small', 'I love cobras')

print("\n\n")
#cities
def describe_city(city, country = 'Philippines'):
	"""writes a simple message"""
	print(city.title() + " is in " + country.title() + ".")


describe_city('cebu')
describe_city('lapu-lapu')
describe_city('ang mo kio', 'singapore')
