total = 0.0
count = 0

data = input('Enter a number (enter to quit) >> ')
while data:
    total += float(data)
    count += 1

    data = input('Enter a number (enter to quit) >> ')

average = total / count
print(average)
