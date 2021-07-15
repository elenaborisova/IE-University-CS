def main():
    nums = []
    x = float(input('Enter a number: '))

    while x >= 0:
        nums.append(x)
        x = float(input('Enter a number: '))

    print(nums)


main()
