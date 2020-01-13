for value in range(1,5):
	print(value)
	
for value in range(1,6):
	print(value)
	
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

#square values
squares = []				#create empty list
for value in range(1,11):	#loop from 1 to 10 using range function
	square = value**2		#store in square variable the current loop value raised to the 2nd power
	squares.append(square)	#add to the list the value of square
	
print(squares)

#better square values
squaresb = []
for value in range(1,11):
	squaresb.append(value**2)
print("\n\n")
print(squaresb)


#list comprehensions
print("\n\n")
print("\n\n")
squares = [value**2 for value in range(1,11)]
print(squares)
add_one = [integer+1 for integer in range(1,6)]
print(add_one)

#try it yourself
print("#########################")
#counting to twenty
for number_to_twenty in range(1,21):
	print(number_to_twenty)
	
#one million pero up to hundred lang kay dugay
hundred = []
for count_to_hundred in range(1,101):
	hundred.append(count_to_hundred)
print(hundred)
#summing a million pero hundred lang kay dugay
print(min(hundred))
print(max(hundred))
print(sum(hundred))

#odd numbers
odd_numbers = []
for odd in range(1,20,2):
	odd_numbers.append(odd)
	
print(odd_numbers)

#cubes
cubes = []
for first_10_cubes in range(1,11):
	cubes.append(first_10_cubes**3)
	
print(cubes)

#cube comprehension
cubes_comprehension = [first_10_cubes_b**3 for first_10_cubes_b in range(1,11)]
print(cubes_comprehension)
