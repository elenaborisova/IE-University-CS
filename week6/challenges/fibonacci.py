def main():
    n = int(input('Please enter a number: '))

    prev_num1 = 0
    prev_num2 = 0
    curr_num = 0

    for i in range(n):
        if i == 0:
            curr_num = 1
            prev_num1 = curr_num
        else:
            curr_num = prev_num1 + prev_num2
            prev_num2 = prev_num1
            prev_num1 = curr_num

    print('The n-th fibonacci number is:', curr_num)


main()
