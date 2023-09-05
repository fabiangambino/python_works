prompt = "What topping would you like on your pizza?"
prompt += "\nIf you are done adding toppings, enter 'quit': "

active = True
while active:
	topping = input(prompt)
	if topping != 'quit':
		print(f"\nWe will add {topping} to your pizza.\n")
	else:
		active = False


