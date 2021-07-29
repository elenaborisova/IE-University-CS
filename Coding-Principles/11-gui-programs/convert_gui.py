from graphics import *


def main():
    win = GraphWin('Celsius Converter', 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1, 3), 'Celsius Temperature:').draw(win)
    Text(Point(1, 1), 'Fahrenheit Temperature:').draw(win)

    input_text = Entry(Point(2.25, 3), 5)
    input_text.setText('0.0')
    input_text.draw(win)

    output_text = Text(Point(2.25, 1), '')
    output_text.draw(win)

    button = Text(Point(1.5, 2.0), 'Convert It')
    button.draw(win)

    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    win.getMouse()

    celsius = float(input_text.getText())
    fahrenheit = 9/5 * celsius + 32

    output_text.setText(round(fahrenheit, 2))
    button.setText('Quit')

    win.getMouse()
    win.close()


main()
