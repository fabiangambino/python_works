age = ""
while age == "":
	age = input("How old are you?: ")
	if int(age) < 3:
		print("Your ticket is free.")
	elif int(age) > 2 and int(age) < 13:
		print("Your ticket is $10.")
	else:
		print("Your ticket is $15.")
