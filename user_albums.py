def make_album(artist_name, album_title, tracks = None):
	music_album = {'artist_name': artist_name, 'album_title': album_title, 'tracks': tracks}
	return music_album

while True:
	artist_name = input("Please name the artist: ")
	album_title = input("Please name the album: ")
	tracks = input("Please name the number of songs on the album: ")
	print(make_album(artist_name, album_title, tracks))
	quit = input("\nWould you like to add more entries? (yes/no): ")
	if quit == 'no':
		break
		
