def happy():
    return 'Happy birthday to you!\n'


def verse_for(person):
    lyrics = happy() * 2 + f'Happy birthday dear {person}.\n' + happy()
    return lyrics


def main():
    for person in ['Fred', 'Lucy', 'Elmer']:
        print(verse_for(person))


main()
