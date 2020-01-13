filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
	active = True
	while active:
		message = input("\nWhat is your name? ")
		
		if message == 'q':
			active = False
		else:
			file_object.write(message + "\n")
			print("\nHello, " + message.title() + ".")
