favorite_places = {
	'john': ['brooklyn', 'florida', 'las vegas'],
	'bob': ['milan', 'london', 'germany'],
	'fabian': ['toretta', 'salerno', 'firenza'],
}

for person, places in favorite_places.items():
	print(f"\n{person.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")