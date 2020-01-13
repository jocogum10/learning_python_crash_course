#importing entire module
import pizza_01

pizza_01.make_pizza(16, 'pepperoni')
pizza_01.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n\n")
#importing specific functions
from pizza_01 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n\n")
#using as to give a function an alias
from pizza_01 import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


print("\n\n")
#using as to give a module an alias
import pizza_01 as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print("\n\n")
#importing all functions in a module
from pizza_01 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


