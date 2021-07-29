from graphics import *


def main():
    print('This program plots the growth of a 10-year investment.')

    win = GraphWin('Investment Growth Chart', 320, 240)
    win.setBackground('white')

    input_text1 = Entry(Point(100, 100), 10)
    input_text1.setText('0.0')
    input_text1.draw(win)

    input_text2 = Entry(Point(100, 200), 10)
    input_text2.setText('0.0')
    input_text2.draw(win)

    win.getMouse()

    principal = float(input_text1.getText())
    apr = float(input_text2.getText())

    input_text1.undraw()
    input_text2.undraw()

    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1, 11):
        principal *= 1 + apr
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

    input('Press <ENTER> to quit')
    win.close()


main()
