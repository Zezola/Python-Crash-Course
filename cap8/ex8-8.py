def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'title': title}

    if tracks:
        album['tracks'] = tracks
    return album 

while True:
    print("Enter the artist's name and the album title\n")
    print("Enter 'q' at anytime to quit")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break
    
    album = make_album(artist, title)
    print(album)
    

