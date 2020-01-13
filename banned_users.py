banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")


#conditional test

car = 'subaru'
print("is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi' ? I predict False.")
print(car == 'audi')

car_2 = 'bmw'
print("is car == 'bmw'? I predict True.")
print(car == 'bmw')

print("\nIs car == 'mercedes' ? I predict False.")
print(car == 'mercedes')

#more conditional tests
#equality and inequality of strings
equal_s = 'Cat'
if equal_s == 'dog':
	print("\nThe string is not equal to dog.")
else:
	print("\nThe string is equal to dog.")
	
#using lower() function
if(equal_s.lower() == 'cat'):
	print("\nThe string is equal to cat.")
else:
	print("\nThe string is not equal to cat.")
#using test involving equality and inequality, greater than, and less than, greater than or equal to, and less than or equal to

number_y = 3
number_x = 4

if (number_y == number_x):
	print("number_y is equal to number_x")
	
if (number_y != number_x):
	print("number_y  is not equal to number_x")
	
if (number_y > number_x):
	print("number_y is greater than number_x")
	
if (number_y < number_x):
	print("number_y is lesser than number_x")
	
if (number_y >= number_x):
	print("number_y is greater than or equal to number_x")

if (number_y <= number_x):
	print("number_y is lesser than or equal to number_x")

#test using the and keyword and the or keyword

if ((number_x < 5) and (number_y < number_x)):
	print("number_x is lesser than 5 and the number_x is lesser than number_y.")
if ((number_x != 5) or (number_y != 5)):
	print("neither of the number_x or number_y is equal to 5.")
	
#item in a list
my_favorites = ['pizza', 'donut', 'siomai', 'siopao']
food = 'sisig'

if food in my_favorites:
	print("the food is in my list of favorites.")
if food not in my_favorites:
	print("the food is not in my list of favorites.")
