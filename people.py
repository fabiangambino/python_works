people = []

person_1 = {
	'first_name': 'robert',
	'last_name': 'blafford',
	'age': 33,
	'city': "staten island",	
}

#print(people['first_name'].title())
#print(people['last_name'].title())
#print(people['age'])
#print(people['city'].title())

person_2 = {
	'first_name': 'fabian',
	'last_name': 'gambino',
	'age': 33,
	'city': 'pflugerville',
}

person_3 = {
	'first_name': 'rose',
	'last_name': 'gambino',
	'age': 64,
	'city': 'brooklyn',
}

people.append(person_1)
people.append(person_2)
people.append(person_3)

for person in people:
	print(person['first_name'].title())
	print(person['last_name'].title())
	print(person['age'])
	print(f"{person['city'].title()}\n")