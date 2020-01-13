filename = 'programming_poll.txt'

with open(filename, 'a') as file_object:
	active = True
	print("Why do you like programming? ")
	print("Enter 'q' to quit.")
	while active:
		poll = input("")
		if poll == 'q':
			active = False
		else:
			file_object.write(poll + "\n")
