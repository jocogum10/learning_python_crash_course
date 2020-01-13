import user_01

my_admin = user_01.Admin('carlos', 'gumanay', 'male', 26)
print("Admin name: " + my_admin.first_name.title())
my_admin.privilege.show_privileges()
