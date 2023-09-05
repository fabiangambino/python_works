favorite_numbers = {
	'kimberlee': [12, 21, 27],
	'fabian': [17, 16, 19],
	'rose': [26, 4],
	'stacy': [3, 25],
	'reese': [8, 10, 37],	
}

for person, numbers in favorite_numbers.items():
	print(f"\n{person.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")

