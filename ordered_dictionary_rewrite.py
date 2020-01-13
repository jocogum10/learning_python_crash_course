#Glossary




glossary = {}

glossary['for'] = 'loop statement'
glossary['if'] = 'conditional statement'
glossary['list'] = 'stores series of items like an array'
glossary['tuples'] = 'unchangable list'
glossary['dictionary'] = 'stores information/characteristics of an object'

for key,value in glossary.items():
	print(key + " - " + value)



from collections import OrderedDict

glossary = OrderedDict()

glossary['for'] = 'loop statement'
glossary['if'] = 'conditional statement'
glossary['list'] = 'stores series of items like an array'
glossary['tuples'] = 'unchangable list'
glossary['dictionary'] = 'stores information/characteristics of an object'

for key,value in glossary.items():
	print(key + " - " + value)



