
from user_02 import User


class Privileges():
	"""Class of the privileges."""
	def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
		"""Initiliaze the privilege attributes"""
		self.privileges = privileges
		
	def show_privileges(self):
		"""lists the administrator's set of privileges."""
		print("Administrator's Privileges: ")
		for privilege in self.privileges:
			print("- " + privilege)


class Admin(User):
	"""Represent users that are administrators."""
	def __init__(self, first_name, last_name, gender, age):
		"""Initialize the attributes of the parent class.
		Initialize a privilege attribute"""
		super().__init__(first_name, last_name, gender, age)
		self.privilege = Privileges()

			

