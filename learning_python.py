filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

my_string = ''
for line in lines:
	my_string += line
	print(line.strip())

print(my_string)
print("\n" + my_string.replace('python', 'c'))

