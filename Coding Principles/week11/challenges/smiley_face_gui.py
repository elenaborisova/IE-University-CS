from graphics import *


def main():
    win = GraphWin('Smiley')

    face = Circle(Point(100, 100), 50)
    face.setFill('yellow')
    face.draw(win)

    left_eye = Circle(Point(80, 90), 7)
    left_eye.setFill('green')
    left_eye.draw(win)

    right_eye = Circle(Point(120, 90), 7)
    right_eye.setFill('green')
    right_eye.draw(win)

    nose = Line(Point(100, 105), Point(100, 115))
    nose.draw(win)

    smile = Line(Point(90, 130), Point(110, 130))
    smile.setFill('red')
    smile.draw(win)

    smile_left_side = Line(Point(90, 130), Point(80, 120))
    smile_left_side.setFill('red')
    smile_left_side.draw(win)
    smile_right_side = Line(Point(110, 130), Point(120, 120))
    smile_right_side.setFill('red')
    smile_right_side.draw(win)

    input('Press <enter> to quit')
    win.close()


main()
