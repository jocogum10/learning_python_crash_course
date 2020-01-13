def read_file(f):
	"""Reads a text file."""
	try:
		with open(f) as file_object:
			files = file_object.read()
	except FileNotFoundError:
		#print("The file '" + f + "' was not found on the directory. \nPlease check the file name.")
		pass
	else:
		print(files)

filename = 'cats.txt'
read_file(filename)
print("\n")
filename2 = 'dogs.txt'
read_file(filename2)
