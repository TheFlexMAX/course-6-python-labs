import sys

from PyQt5.QtWidgets import QApplication

from calculator import Calculator


def main():
    app = QApplication(sys.argv)

    win = Calculator()
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
