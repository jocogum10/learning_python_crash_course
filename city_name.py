def city_country_name(city, country, population=''):
	"""Neatly formatted city and country name."""
	if population:
		name = city + ', ' + country + ' - ' + str(population)
	else:
		name = city + ', ' + country
	return name.title()
