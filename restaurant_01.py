class Restaurant():
	"""A simple class called restaurant."""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant name and cuisine type attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		"""A method that describes the restaurant."""
		print("The name of the restaurant is " + 
				self.restaurant_name.title() + ".")
		print("The types of cuisines that the restaurant offers are " 
				+ self.cuisine_type.title() + ".")
				
	def open_restaurant(self):
		"""A method which indicates that the restaurant is open."""
		print("The restaurant is now open!")
		
	def set_number_served(self, numbers_served):
		"""Sets the number of customers that have been served."""
		self.number_served = numbers_served
		
	def increment_number_served(self, served):
		"""Increments the number of customers served."""
		self.number_served = self.number_served + served
		
