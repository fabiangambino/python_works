cities = {
	'brooklyn': {"country": "united states", "population": 4000000, "fact": "it is considered part of New York City"},
	'pflugerville': {"country": "united states", "population": 100000, "fact": "it was founded by a German settler"},
	'rome': {"country": "italy", "population": 1000000, "fact": "it was the capital of the Roman Empire"},
}

for city, fact_sets in cities.items():
	print(city.title())
	print(f"\t{city.title()} is located in the {fact_sets['country'].title()}.")
	print(f"\t{city.title()} has a population of {fact_sets['population']}.")
	print(f"\tA fun fact about {city.title()} is that {fact_sets['fact']}.\n")
	
