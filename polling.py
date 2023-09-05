favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")

take_poll = ['jen', 'fabian', 'edward', 'robert']

for person in take_poll:
	if person in favorite_languages.keys():
		print(f"Thank you for taking the poll, {person.title()}.")
	else:
		print(f"You should take the poll, {person.title()}.")