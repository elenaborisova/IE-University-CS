def add_contact(name, number, email, address, contact_book):
    contact_book[name] = {}
    contact_book[name]['number'] = number
    contact_book[name]['email'] = email
    contact_book[name]['address'] = address

    print(f'You successfully added {name} to the contact book!\n')
    return contact_book


def search_by_name(name, contact_book):
    if name not in contact_book:
        print('Sorry, the name you are searching for is not in the contact book!\n')

    number = contact_book[name]['number']
    email = contact_book[name]['email']
    address = contact_book[name]['address']

    print(f'Contact information:\n'
          f'Name: {name}\n'
          f'Telephone number: {number}\n'
          f'Email address: {email}\n'
          f'Home address: {address}\n')


def search_by_phone(number, contact_book):
    for name, info in contact_book.items():
        if info['number'] == number:
            return name

    print('Sorry, the number you are searching for is not in the contact book!\n')
    return


def delete_contact(name, contact_book):
    if name not in contact_book:
        print('Sorry, the contact you are trying to delete is not in the contact book!\n')
    else:
        contact_book.pop(name)
        print(f'{name} deleted successfully!\n')
    return contact_book


def show_all(contact_book):
    if not contact_book:
        print('Sorry, there are no contacts in your contact book!\n')
        return

    result = 'Contacts in the contact book:\n'

    for contact in contact_book:
        result += f'{contact}\n'

    print(result)


def main():
    contact_book = {}

    while True:
        command = input('What do you want to do?\n'
                        '[add, search by name, delete, show all, search by phone]\n'
                        '[ENTER to quit]\n'
                        '>>> ')

        if not command:
            break
        elif command == 'add':
            name = input('Please enter the name of the contact you want to add: ')
            number = input('Please enter their telephone number: ')
            email = input('Please enter their email address: ')
            address = input('Please enter their home address: ')
            contact_book = add_contact(name, number, email, address, contact_book)
        elif command == 'search by name':
            name = input('Please enter the name of the contact you are searching for: ')
            search_by_name(name, contact_book)
        elif command == 'search by phone':
            number = input('Please enter the telephone number you are searching for: ')
            name = search_by_phone(number, contact_book)
            search_by_name(name, contact_book)
        elif command == 'delete':
            name = input('Please enter the name of the contact you want to delete: ')
            contact_book = delete_contact(name, contact_book)
        elif command == 'show all':
            show_all(contact_book)


main()
