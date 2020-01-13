"""def get_formatted_name(first_name, last_name):
	#Return a full name, neatly formatted.
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
#this is an infinite loop!
while True:
	print("\nPlease tell me you name: ")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
"""

#city names
def city_country(city, country):
	info = ('"' + city.title() + ', ' + country.title() + '"')
	return info

country = city_country('cebu', 'philippines')
print(country)
country = city_country(city = 'santiago', country = 'chile')
print(country)
country = city_country(country = 'hong kong', city = 'hong kong')
print(country)


#album
def make_album(artist_name, album_title, number_of_tracks = ''):
	"""This will make an album dictionary"""
	if number_of_tracks:
		album = {'artist': artist_name, 'title': album_title, 'number of tracks': number_of_tracks}
	else:
		album = {'artist': artist_name, 'title': album_title}
	return album
	
alb = make_album('satriani', 'surfing with the aliens')
print(alb)
alb = make_album('vai', 'aliens love secrets')
print(alb)
alb = make_album('govan', 'erotic cakes')
print(alb)
alb = make_album('malmsteem', 'concerto', 9)
print(alb)


print("\n\n")
#user albums
def make_album_loop(artist_name, album_title):
	"""This will make an album dictionary that the user will enter the info"""
	album = {'artist': artist_name, 'title': album_title, 'number of tracks': number_of_tracks}
	return album
	
#loop
while True:
	print("Enter the details of the album: ")
	print("(enter 'q' to quit)")
	
	artist = input("Enter the name of the artist: ")
	if artist == 'q':
		break
	
	title = input("Enter the title of the album: ")
	if title == 'q':
		break
		
	print("\nThis is album details: ")
	alb = make_album(artist, title)
	print(alb)
