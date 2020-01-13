class User():
	"""A class that defines a user."""
	
	def __init__(self, first_name, last_name, gender, age):
		"""Initialize the first name, last name, age, and gender attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.age = age
		self.login_attempt = 0
		
	def describe_user(self):
		"""A method that prints the a summary of the user's information."""
		print("User Information: ")
		print("Fist Name: " + self.first_name.title())
		print("Last Name: " + self.last_name.title())
		print("Gender: " + self.gender.title())
		print("Gender: " + str(self.age))
		
	def greet_user(self):
		"""A method that prints a personalized greeting to the user."""
		print("Hello, " + self.first_name.title() + "!")
		
	def increment_login_attempt(self):
		"""Increments the value of login_attempts by 1."""
		self.login_attempt += 1
		
	def reset_login_attempts(self):
		"""Resets the value of login_attempts to 0."""
		self.login_attempt = 0
