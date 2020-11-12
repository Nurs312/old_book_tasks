def make_album(performer, album):
    dictionary = {'performer': performer, 'album': album}
    return dictionary


while True:
    print("\nTell me your fav performer:")
    print('(Enter "q" when you want to quit)')

    singer = input('Enter name of the performer: ').lower()
    if singer == 'q':
        break
    albom = input('Enter name of the album: ').lower()
    if albom == 'q':
        break
    formatted_msg = make_album(singer, albom)
    for k, v in formatted_msg.items():
        print(f'{k.title()}: {v.title()}')

