from graphics import *


def main():
    win = GraphWin('Quiz Grade')

    win.setCoords(0.0, 0.0, 4.0, 4.0)

    title = Text(Point(2, 3.5), 'Quiz Calculator')
    title.setTextColor('blue')
    title.draw(win)

    prompt = Text(Point(2, 3), 'Enter a grade from 1-5:')
    prompt.setTextColor('black')
    prompt.draw(win)

    input_text = Entry(Point(2, 2.5), 5)
    input_text.setText('')
    input_text.draw(win)

    converted_grade = Text(Point(2, 1), '')
    converted_grade.setSize(20)
    converted_grade.setTextColor('red')
    converted_grade.draw(win)

    win.getMouse()

    if input_text.getText() == '5':
        converted_grade.setText('A')
    elif input_text.getText() == '4':
        converted_grade.setText('B')
    elif input_text.getText() == '3':
        converted_grade.setText('C')
    elif input_text.getText() == '2':
        converted_grade.setText('D')
    elif input_text.getText() == '1' or input_text.getText() == '0':
        converted_grade.setText('F')
    else:
        converted_grade.setText('Invalid quiz score!')

    win.getMouse()
    win.close()


main()
