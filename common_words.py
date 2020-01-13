filename = 'alice.txt'

with open(filename) as file_object:
	files = file_object.read()

print(files)
print(len(files.split()))
print(len(files))
print(files.lower().count('the'))
