def make_album(artist, title, tracks = ''):
    album = { 'author': artist.title(), 'title': title.title()}

    if tracks:
        album['tracks'] = tracks
    
    return album

led_zeppelin = make_album('Led Zeppelin', 'I', 12)
van_hallen = make_album('Van Hallen', 'Diver Down')
def_leppard = make_album('Def Leppard', 'Pyromania')

print(led_zeppelin)
print(van_hallen)
print(def_leppard)