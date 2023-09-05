group_size = input("How many people are in your dinner group?: ")

if int(group_size) > 8:
	print("\nYou will have to wait for a table.")
else:
	print("\nYour table is ready.")