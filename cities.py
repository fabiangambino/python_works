cities = {
	'brooklyn': {"country": "united states", "population": 4000000, "fact": "considered part of new york city"},
	'pflugerville': {"country": "united states", "population": 100000, "fact": "founded by a german settler"},
	'rome': {"country": "italy", "population": 1000000, "fact": "capital of the roman empire"},
}

for city, fact_sets in cities.items():
	print(city.title())
	for fact_set in fact_sets.items():
		print(f"\t{fact_set}")
