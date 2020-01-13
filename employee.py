class Employee():
	"""A profile of an employee."""
	def __init__(self, first_name, last_name, annual_salary):
		"""Initialize the first name, last name, and annual salary attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary
		
	def give_raise(self, amount=5000):
		"""Gives raise to the employee of 5000 by default"""
		self.annual_salary += amount

"""employee = Employee('carlos', 'gumanay', 400000)
print(employee.first_name)
print(employee.annual_salary)
employee.give_raise()
print(employee.annual_salary)
"""
