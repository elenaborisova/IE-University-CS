from graphics import *


def main():
    win = GraphWin('Winter Scene')

    win.setCoords(0.0, 0.0, 4.0, 4.0)

    tree_base = Rectangle(Point(0.75, 1), Point(1.5, 2))
    tree_base.setFill('brown')
    tree_base.draw(win)

    tree_top = Polygon(Point(0.2, 2), Point(1.2, 3), Point(2, 2))
    tree_top.setFill('green')
    tree_top.draw(win)

    snowman_c1 = Circle(Point(2.75, 1.3), 0.5)
    snowman_c1.setFill('gray')
    snowman_c1.setOutline('black')
    snowman_c1.draw(win)

    snowman_c2 = Circle(Point(2.75, 2.2), 0.4)
    snowman_c2.setFill('gray')
    snowman_c2.setOutline('black')
    snowman_c2.draw(win)

    snowman_c3 = Circle(Point(2.75, 2.9), 0.3)
    snowman_c3.setFill('gray')
    snowman_c3.setOutline('black')
    snowman_c3.draw(win)

    snowman_nose = Polygon(Point(2.75, 2.8), Point(2.75, 2.9), Point(2.95, 2.9))
    snowman_nose.setFill('orange')
    snowman_nose.draw(win)

    win.getMouse()
    win.close()


main()
