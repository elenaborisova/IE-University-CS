total = 0.0
count = 0
more_data = 'yes'

while more_data == 'yes':
    x = float(input('Enter a number: '))
    total += x
    count += 1

    more_data = input('Do you have more numbers (yes or no)? ')

average = total / count
print(average)
