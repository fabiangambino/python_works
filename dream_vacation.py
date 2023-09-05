responses = {}

active = True 
while active:
	name = input("\nWhat is your name? ")
	place = input("If you could visit one place in the world, where would you go? ")

	responses[name] = place

	continue_polling = input("\nWould you like to continue polling? (yes/no) ")
	if continue_polling == 'no':
		active = False

print("\n--- Polling Results ---\n")
for name, place in responses.items():
	print(f"{name} would visit {place}.")


