while True:
	first_number = input("\nFirst Number: ")
	if first_number == 'q':
		break
	second_number = input("Second Number: ")
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Please input a number.")
	else:
		print(answer)

