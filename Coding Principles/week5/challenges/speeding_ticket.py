def main():
    speed_limit = int(input('Enter speed limit: '))
    clocked_speed = int(input('Enter clocked speed: '))

    fine = 50

    if clocked_speed > speed_limit:
        mph_over_limit = clocked_speed - speed_limit
        fine += mph_over_limit * 5
        if clocked_speed > 90:
            fine += 200
        print('The speed is illegal! Your fine is:', fine)
    else:
        print('The speed is legal.')


main()
