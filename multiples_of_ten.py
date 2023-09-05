number = input("Please select a number: ")

if int(number) % 10  == 0:
	print(f"\n{number} is a multiple of 10.")
else:
	print(f"\n{number} is not a multiple of 10.")