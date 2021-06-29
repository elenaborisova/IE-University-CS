def main():
    ans = input('What flavour do you want [vanilla]: ')
    if ans:
        flavour = ans
    else:
        flavour = 'vanilla'

    print('The flavour you entered was', flavour)


main()
