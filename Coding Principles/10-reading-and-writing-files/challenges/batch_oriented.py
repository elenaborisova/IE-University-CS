def main():
    nums = []
    infile = open('numbers_input.txt', 'r')
    outfile = open('numbers_output.txt', 'w')

    x = float(infile.readline())

    while x >= 0:
        nums.append(x)
        x = float(infile.readline())

    print(nums, file=outfile)


main()
