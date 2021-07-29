def main():
    print('This is a program that calculates total weekly wage.')

    hours_worked = float(input('Enter the amount of hours worked: '))
    hourly_rate = float(input('Enter the hourly rate: '))

    if hours_worked <= 40:
        total_weekly_wage = hours_worked * hourly_rate
    else:
        total_weekly_wage = 40 * hourly_rate
        hours_left = hours_worked - 40
        total_weekly_wage += hours_left * (1.5 * hourly_rate)

    print('Total wage for the week is:', total_weekly_wage)


main()
