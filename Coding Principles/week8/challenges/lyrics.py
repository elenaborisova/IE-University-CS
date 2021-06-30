def print_lyrics(animal, sound):
    lyrics = f'Old MacDonalds had a farm, Ee-igh, Oh!\n' \
             f'And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh!\n' \
             f'With a {sound}, {sound} here and a {sound}, {sound} there.\n' \
             f'Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.\n' \
             f'Old MacDonalds had a farm, Ee-igh, Ee-igh, Oh!\n'

    print(lyrics)


def main():
    animals_info = {
        'cow': 'moo',
        'cat': 'meow',
        'dog': 'whoof',
        'donkey': 'hihan',
        'bird': 'pu-pu',
    }

    for animal, sound in animals_info.items():
        print_lyrics(animal, sound)


main()
