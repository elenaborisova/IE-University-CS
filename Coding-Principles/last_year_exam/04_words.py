def make_words_uppercase(words):
    for i in range(len(words)):
        words[i] = words[i].upper()
    return words


def main():
    words = []

    i = 1
    while len(words) < 3:
        word = input(f'Please enter word {i}: ')
        if not word.isalpha():
            print('The word should not contain numbers!')
            continue
        words.append(word)
        i += 1

    words_upper = make_words_uppercase(words)
    print(words_upper)


main()
