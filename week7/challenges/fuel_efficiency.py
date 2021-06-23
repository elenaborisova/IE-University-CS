starting_odometer = float(input())

total_odometer = starting_odometer
total_miles_per_gallon = 0
total_gas_used = 0


while True:
    curr_odometer = float(input())

    if not curr_odometer:
        break

    gas_used = float(input())
    miles_per_hour = float(input())

    total_odometer += curr_odometer
