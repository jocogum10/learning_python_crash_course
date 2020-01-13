from random import randint

class Die():
	"""A class that simulates a die"""
	def __init__(self, sides=6):
		"""Initialize the attributes"""
		self.sides = sides
		
	def roll_die(self):
		"""method to roll a die"""
		x = randint(1, self.sides)
		print(x)
		
dice = Die()
dice.roll_die()
