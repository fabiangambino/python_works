pets = []

pet_1 = {
	'name': 'lily',
	'type': 'dog',
	'owner': 'kimberlee',
}

pet_2 = {
	'name': 'chester',
	'type': 'cat',
	'owner': 'reese',
}

pet_3 = {
	'name': 'quincy',
	'type': 'bird',
	'owner': 'sue',
}

pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)

for pet in pets:
	print(pet['name'].title())
	print(pet['type'].title())
	print(f"{pet['owner'].title()}\n")

