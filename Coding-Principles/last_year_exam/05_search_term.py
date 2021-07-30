def is_term_present(text, term):
    if term not in text:
        return False
    return True


def get_text():
    while True:
        text = input('What is the text: ')
        if not text.isalpha():
            print('Please enter a valid text!')
        else:
            return text


def get_search_term():
    while True:
        search_term = input('What do you want to search for: ')
        if not search_term.isalpha():
            print('Please enter a valid search term!!')
        else:
            return search_term


def main():
    text = get_text()
    search_term = get_search_term()

    if is_term_present(text, search_term):
        print(f'True. The search term {search_term} is present in the text you entered.')
    else:
        print(f'False. The search term {search_term} is not present in the text you entered.')


main()
