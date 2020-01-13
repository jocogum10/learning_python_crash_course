motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)
motorcycles.append('ktm')
motorcycles.append('mazda')
motorcycles.append('hyundai')
print(motorcycles)

motorcycles.insert(1,'bmw')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

del motorcycles[-1]
del motorcycles[-1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

print("\n\n")
motorcycles.remove('yamaha')
print(motorcycles)

print("\n\n")
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


#guest list
print("\n\n")
invite = ['steve', 'joe', 'guthrie']
message = "I invite you " + invite[0].title() + ", " + invite[1].title() + ", and " + invite[2].title() + " to have dinner with me."
print(message)

#changing guest list
print("\n\n")
cant_make_it = invite.pop()
invite.append('slash')
message = "I invite you " + invite[0].title() + ", " + invite[1].title() + ", and " + invite[2].title() + " to have dinner with me. Because " + cant_make_it.title() + " can't make it."
print(message)

#more guest
print ("I just found a bigger table.")
invite.insert(0,'yngwie')
invite.insert(2,'jimi')
invite.append('buckethead')
add_message = "Inviting you " + invite[0].title() + ", " + invite[2].title() + ", and " + invite[-1].title() + " to also join us."
print(add_message)


#shrinking guest list
print("Fake news. There will be only two guest that I can be invited.")
print(invite)
invite.pop(-1)
invite.pop(0)
invite.pop()
invite.pop(1)
print(invite)
final_message = "I invite you " + invite[0].title() + ", and " + invite[1].title() + " to dinner."
print(final_message)
