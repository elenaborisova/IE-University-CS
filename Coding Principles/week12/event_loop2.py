from graphics import *


def handle_key(key, win):
    if key == 'r':
        win.setBackground('pink')
    elif key == 'w':
        win.setBackground('white')
    elif key == 'b':
        win.setBackground('lightblue')
    elif key == 'g':
        win.setBackground('lightgray')


def handle_click(pt, win):
    entry = Entry(pt, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == 'Return':
            break

    entry.undraw()
    Text(pt, entry.getText()).draw(win)

    # clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()


def main():
    win = GraphWin('Color Window', 500, 500)

    while True:
        key = win.checkKey()
        if key == 'q':
            break

        if key:
            handle_key(key, win)

        pt = win.checkMouse()
        if pt:
            handle_click(pt, win)

    win.close()


main()
