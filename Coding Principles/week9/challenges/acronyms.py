def main():
    phrase_words = input('Please enter a phrase: ').upper().split()
    first_letters = []

    for word in phrase_words:
        first_letters.append(word[0])

    print('The acronym is:', ''.join(first_letters))


main()
