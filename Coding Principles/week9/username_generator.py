def main():
    print('This program generates computer usernames.\n')

    first_name = input('Please enter your first name (all lowercase): ')
    last_name = input('Please enter your last name (all lowercase): ')

    username = first_name[0] + last_name[:7]

    print('Your username is:', username)


main()
