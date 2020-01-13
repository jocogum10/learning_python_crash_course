"""#start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left.
#move each design to completed_models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	#simulate creating a 3d print from the design.
	print("Printing model: " + current_design)
	completed_models.append(current_design)
	
#display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
	print(completed_model)
"""
"""
#using functions
def print_models(unprinted_designs, completed_models):
	#simulate printing each design, until none are left
	#move each design to completed_models after printing.
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		#simulate creating a 3d print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	#Show all the models that were printed.
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
		
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
"""
#magicians
def show_magicians(magicians_names):
	for magician in magicians:
		print(magician)
	
magicians = ['hudini', 'blane', 'johnson']	
show_magicians(magicians)

print("\n")
#great magicians
def make_great(magicians):
	for magician in magicians:
		magician = 'the great ' + magician
		print(magician)
		
make_great(magicians)

print("\n\n")
#unchanged magicians
copied_magicians = []
def make_great_copy(magicians, copy_of_magicians):
	for magician in magicians:
		magician = 'the great ' + magician
		copy_of_magicians.append(magician)
		

make_great_copy(magicians, copied_magicians)
print(copied_magicians)
print(magicians)

