sandwich_orders = ['pastrami on rye', "turkey club on multigrain", 'pastrami on rye', 'mortadella and mozzarella on ciabatta', 'pastrami on rye']
finished_sandwiches = []

print("The Deli has run out of Pastrami.\n")

while "pastrami on rye" in sandwich_orders:
	sandwich_orders.remove("pastrami on rye")

for sandwich in sandwich_orders:
	print(f"I made your {sandwich}.")
	finished_sandwiches.append(sandwich)

print("\nFinished Sandwiches:\n")

for sandwich in finished_sandwiches:
	print(sandwich.title())

