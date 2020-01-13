#list of bicycles
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())

print(bicycles[-1].title())
print(bicycles[-2].title())
print(bicycles[-3].title())
print(bicycles[-4].title())

print("\n")
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)

print("\n\n")

names = ['xander', 'carlito', 'pat']
print(names[0].title())
print(names[1].title())
print(names[2].title())

print("\n\n")

message1 = "Hello, " + names[0].title() + "!"
message2 = "Hello, " + names[1].title() + "!"
message3 = "Hello, " + names[2].title() + "!"
print(message1)
print(message2)
print(message3)

print("\n\n")

goal_list = ['mini copper', 'minimalist-style house', 'free time', 'passive income']
goal_message = "My goal in life is to have " + goal_list[2] + ", buy a " + goal_list[0] + ", and have a " + goal_list[1] + " using my " + goal_list[3] + "."

print(goal_message)
