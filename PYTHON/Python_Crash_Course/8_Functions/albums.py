#!../bin/python3

def make_album(artist_name, album_title, songs=None):
    """Return ALbum Dictionary."""
    album = {'Artist':artist_name, 'Album':album_title}
    if songs:
        album['songs'] = songs
    return album

keep_going = True
while keep_going:
    message = "ENTER THE ALBUM'S ARTIST AND TITLE"
    msg_len = len(message)
    print(f'{message}\n(enter "q" to quit!)')
    print(msg_len * '=')
    artist = input("Enter Artist's Name: ")
    if artist == 'q':
        break
    album = input("Enter Album's Title: ")
    if album == 'q':
        break
    song = input("Number of songs(optional): ")
    if song == 'q':
        break

    import time
    
    album1 = make_album(artist.title(), album.title(), song)
    time.sleep(1)
    print(f'{album1}\n')
    keep_going = False

# album1 = make_album('Young Thug', 'Red Slime')
# album2 = make_album('Bon Jovi', 'Wanted Dead or Alive')
# album3 = make_album('Crown The Empire', 'Retrograde')
# album4 = make_album('Erigga', 'The Lost Boy', 15)
# albums = [album1, album2, album3, album4]
# for i, album in enumerate(albums, start=1):
#     print(i, album)
