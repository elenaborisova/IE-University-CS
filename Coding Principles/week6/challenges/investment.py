def main():
    interest_rate = float(input('Enter annualized interest rate: '))
    initial_investment = float(input('What is your initial investment? '))

    years = 0
    investment = initial_investment

    while investment < initial_investment * 2:
        investment += investment * interest_rate / 100
        years += 1

    print('It will take', years, 'to double your investment of', initial_investment)


main()
