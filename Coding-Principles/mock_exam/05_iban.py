def get_iban():
    while True:
        iban = input('Enter IBAN: ')
        if len(iban) == 22:
            return iban


def main():
    iban = get_iban()
    
    country_code = iban[:2]
    check_number = iban[2:4]
    bank_identifier = iban[4:8]
    sort_code = iban[8:14]
    account_number = iban[14:22]

    print('The country code is:', country_code)
    print('The check number is:', check_number)
    print('The bank identifier is:', bank_identifier)
    print('The sort code is:', sort_code)
    print('The account number:', account_number)


main()
