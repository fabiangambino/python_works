def make_album(artist_name, album_title, tracks = None):
	music_album = {'artist_name': artist_name, 'album_title': album_title, 'tracks': tracks}
	return music_album

print(make_album('The Beatles', 'One'))
print(make_album('Metallica', 'Master of Puppets'))
print(make_album('System of a Down', 'Toxicity'))
print(make_album('Jimi Hendrix', 'Rock Legends', '13'))


def city_country(city_name, country):
	return f"{city_name}, {country}"

print(city_country('Santiago', 'Chile'))
print(city_country('Milan', 'Italy'))
print(city_country('Berlin', 'Germany'))

def make_shirt(size = 'large', message = 'I love Python.'):
	print(f'The {size} shirt has a quote that says {message}')

make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', message = "Python is the best!")