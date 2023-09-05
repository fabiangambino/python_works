sandwich_orders = ['pastrami on rye', "turkey club on multigrain", 'mortadella and mozzarella on ciabatta']
finished_sandwiches = []

for sandwich in sandwich_orders:
	print(f"I made your {sandwich}.")
	finished_sandwiches.append(sandwich)

print("\nFinished Sandwiches:\n")

for sandwich in finished_sandwiches:
	print(sandwich.title())