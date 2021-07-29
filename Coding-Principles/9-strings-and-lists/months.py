def get_month_abbrev_from_string():
    n = int(input('Enter a month number (1-12): '))
    months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    pos = (n - 1) * 3
    month_abbrev = months[pos:pos + 3]

    print('The month abbreviation is:', month_abbrev)


def get_month_abbrev_from_lists():
    n = int(input('Enter a month number (1-12): '))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    print('The month abbreviation is:', months[n-1])


