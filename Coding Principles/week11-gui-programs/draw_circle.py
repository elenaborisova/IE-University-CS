from graphics import *


def main():
    win = GraphWin('Circle')

    body = Circle(Point(100, 100), 50)
    body.setFill('red')
    body.draw(win)

    input('Press <enter> to quit')
    win.close()


main()
