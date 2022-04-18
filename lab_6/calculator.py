import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)
        self.b_dot = QPushButton(".", self)
        self.hbox_first.addWidget(self.b_dot)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        self.b_minus = QPushButton("-", self)
        self.hbox_result.addWidget(self.b_minus)
        self.b_div = QPushButton("/", self)
        self.hbox_result.addWidget(self.b_div)
        self.b_multiple = QPushButton("*", self)
        self.hbox_result.addWidget(self.b_multiple)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_div.clicked.connect(lambda: self._operation("/"))
        self.b_multiple.clicked.connect(lambda: self._operation("*"))
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_dot.clicked.connect(lambda: self._button("."))

    def _button(self, param):
        line = self.input.text()
        if param == '.' and ('.' in line or not line):
            return

        self.input.setText(line + param)

    def _value_validate(self, value):
        value = value.replace('.', '')
        return bool(value and value.isnumeric())

    def _operation(self, op):
        value = self.input.text()
        if not self._value_validate(value):
            return

        self.num_1 = float(value)

        self.op = op
        self.input.setText("")

    def _result(self):
        value = self.input.text()
        if not self._value_validate(value):
            return

        self.num_2 = float(value)

        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        elif self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        elif self.op == "/":
            self.input.setText(str(self.num_1 / self.num_2))
        elif self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
