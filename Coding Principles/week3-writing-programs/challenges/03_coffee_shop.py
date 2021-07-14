def main():
    pounds = int(input('Enter the amount of pounds: '))

    price_per_pound = 10.5
    shipping_cost_per_pound = 0.86
    fixed_cost = 1.5

    total_cost = (price_per_pound + shipping_cost_per_pound) * pounds + fixed_cost

    print('Total cost:', total_cost)


main()
