def main():
    print('This program creates a file of usernames from a file of names.')

    infile_name = input('What file are the names in? ')
    outfile_name = input('What file should the usernames go to? ')

    infile = open(infile_name, 'r')
    outfile = open(outfile_name, 'w')

    for line in infile:
        first, last = line.split()
        uname = (first[0] + last[:7]).lower()
        print(uname, file=outfile)

    infile.close()
    outfile.close()

    print('Usernames have been written to:', outfile_name)


main()
