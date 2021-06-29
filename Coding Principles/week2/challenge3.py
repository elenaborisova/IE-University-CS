def main():
    def convert_usd_to_euro(dollars):
        return dollars * 0.82

    print('This program converts dollars to euros.')

    dollars = eval(input("Enter dollar amount: "))
    euros = convert_usd_to_euro(dollars)

    print("Euros:", euros)


main()
