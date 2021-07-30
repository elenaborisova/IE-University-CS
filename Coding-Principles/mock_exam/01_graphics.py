from graphics import *
import random


def draw_circles(win):
    for i in range(1, 6):
        p = win.getMouse()
        circle = Circle(p, random.randrange(20, 100))
        circle.setFill('blue')
        circle.draw(win)
        Text(p, i).draw(win)


def main():
    win = GraphWin('Circles', 400, 400)
    message = Text(Point(200, 50), 'click to draw a circle').draw(win)

    draw_circles(win)

    message.setText('click to quit')

    win.getMouse()
    win.close()


main()
