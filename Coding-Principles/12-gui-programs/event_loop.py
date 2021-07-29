from graphics import *


def main():
    win = GraphWin('Color Window', 500, 500)

    while True:
        key = win.getKey()
        if key == 'q':
            break

        if key == 'r':
            win.setBackground('pink')
        elif key == 'w':
            win.setBackground('white')
        elif key == 'b':
            win.setBackground('lightblue')
        elif key == 'g':
            win.setBackground('lightgray')

    win.close()


main()
