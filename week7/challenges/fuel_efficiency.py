def main():
    initial_odometer = float(input('Please add initial odometer reading: '))
    total_odometer = initial_odometer
    total_gas_used = 0

    while True:
        curr_odometer = input('Please add current odometer reading: ')
        if not curr_odometer:
            break

        curr_odometer = float(curr_odometer)
        gas_used = float(input('Please add current gas used: '))

        average_miles_per_gallon = (curr_odometer - total_odometer) / gas_used
        total_odometer += curr_odometer
        total_gas_used += gas_used
        print('Average miles per gallon for current leg: ', average_miles_per_gallon)

    print('Total miles per gallon for the trip:', total_odometer / total_gas_used)


main()
