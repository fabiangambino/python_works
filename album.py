def make_album(artist_name, album_title, tracks = None):
	music_album = {'artist_name': artist_name, 'album_title': album_title, 'tracks': tracks}
	return music_album

print(make_album('The Beatles', 'One'))
print(make_album('Metallica', 'Master of Puppets'))
print(make_album('System of a Down', 'Toxicity'))
print(make_album('Jimi Hendrix', 'Rock Legends', '13'))
