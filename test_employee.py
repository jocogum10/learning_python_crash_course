import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test for class Employee"""
	
	def setUp(self):
		"""Create an employee and setup"""
		self.employee = Employee('carlos', 'joco', 400000)
	
	def test_give_default_raise(self):
		"""Test by giving default value raise."""
		self.employee.give_raise()
		
		self.assertEqual(self.employee.annual_salary, 405000)
		
	def test_give_custom_raise(self):
		"""Test by giving default value raise."""
		self.employee.give_raise(1000)
		
		self.assertEqual(self.employee.annual_salary, 401000)

unittest.main()
