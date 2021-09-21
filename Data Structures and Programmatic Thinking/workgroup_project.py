def string_to_list_of_words(s):
    return s.split()


def calculate_frequencies(words):
    words_frequencies = {}

    for word in words:
        if word not in words_frequencies:
            words_frequencies[word] = 0
        words_frequencies[word] += 1

    return words_frequencies


def display_frequencies(words_frequencies):
    pattern = ''

    for word, frequency in words_frequencies.items():
        pattern += word + ' | ' + frequency * '*' + '\n'

    return pattern


print(display_frequencies({
    "hello": 2,
    "goodbye": 3,
    "you": 1,
    "I": 1,
}))
