vocabulary = {
	'variable': "a keyword used to access a value",
	'float': "an integer expressed with a decimal place",
	'string': "a series of characters used to form a sentence",
	'list': "a grouping of varies pieces of data",
	'dictionary': "a list of keys and values",
	'key': 'the key is used to access the value in a key value pair',
	'value': 'the value is the data stored by a key in a key value pair',
	'loop': 'the method of moving through a series of data',
	'method': 'a function that performs a particular task on a specifc type of data',
}

#print(f"Variable: {vocabulary['variable']}")
#print(f"Float: {vocabulary['float']}")
#print(f"String: {vocabulary['string']}")
#print(f"List: {vocabulary['list']}")
#print(f"Dictionary: {vocabulary['dictionary']}")

for key, value in vocabulary.items():
	print(f"{key.title()}: {value}")


