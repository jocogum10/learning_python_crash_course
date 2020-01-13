import unittest
from city_name import city_country_name

class CityCountryTestCase(unittest.TestCase):
	"""Test the city country name."""
	def test_city_country_name(self):
		"""function that test the city_name module"""
		name = city_country_name('santiago', 'chile', 5000000)
		self.assertEqual(name, 'Santiago, Chile - 5000000')
		
unittest.main()
