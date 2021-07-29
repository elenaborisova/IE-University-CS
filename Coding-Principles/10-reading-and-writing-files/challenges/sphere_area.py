import math
from tkinter.filedialog import askopenfilename, asksaveasfilename


def main():
    print('This is a program that calculate the volume '
          'and surface area of a sphere from its radius.')

    infile_name = askopenfilename()
    infile = open(infile_name, 'r')

    radius = float(infile.readline())

    outfile_name = asksaveasfilename()
    outfile = open(outfile_name, 'w')

    volume = 4 / 3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2

    print('The volume is:', volume, 'and the area is:', area, file=outfile)

    infile.close()
    outfile.close()


main()
