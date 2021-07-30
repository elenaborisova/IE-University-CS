def are_credentials_valid(user_id, password, correct_id, correct_password):
    if user_id == correct_id and password == correct_password:
        return True
    return False


def main():
    correct_id = 'elena.borisova@gmail.com'
    correct_password = 'elena'

    while True:
        user_id = input('Please enter user ID: ')
        if '@' not in user_id:
            print('User ID should be a valid email!')
            continue

        password = input('Please enter password: ')
        for char in password:
            if not char.isalpha():
                print('Password should contain only letters!')
                continue

        if are_credentials_valid(user_id, password, correct_id, correct_password):
            break
        else:
            print('Wrong!')


main()
