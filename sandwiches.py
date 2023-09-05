#ingredients = ['turkey', 'swiss cheese', 'lettuce', 'tomato', 'mayo']

def sandwich_order(*choices):
	print("\nSandwich Order:")
	for ingredient in choices:	
		print(f" - {ingredient}")

sandwich_order('turkey')
sandwich_order('turkey', 'swiss')
sandwich_order('turkey', 'swiss cheese', 'lettuce', 'tomato', 'mayo')

