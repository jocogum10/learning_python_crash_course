from restaurant_01 import Restaurant

#class for an ice cream stand that inherits the restaurant class
class IceCreamStand(Restaurant):
	"""Represents a restaurant that is an ice cream stand."""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize the attributes of the restaurant
		Add a flavors attribute"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'vanilla', 'ube']
		
	def display_flavors(self):
		"""Displays the flavors of the ice cream."""
		for flavor in self.flavors:
			print(flavor)
		
		
my_ice_cream = IceCreamStand('selecta', 'deserts')
print(my_ice_cream.flavors)
my_ice_cream.display_flavors()

