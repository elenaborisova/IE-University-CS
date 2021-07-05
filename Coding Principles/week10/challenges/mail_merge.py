def main():
    names = open('names.txt', 'r')

    for name in names:
        letter = open('letter.txt', 'r')
        print(f'Dear {name[:-1]},')
        print(letter.read())
        print()


main()
