from PyQt5.uic import loadUiType

Ui_MainWindow, QMainWindow = loadUiType('calculadora.ui')

class FormMain(QMainWindow, Ui_MainWindow):

    firstNumber = None

    def __init__(self, parent=None):
        super(FormMain, self).__init__()
        self.setupUi(self)

        #chamando os botões
        self.button0.clicked.connect(self.digit_pressed)
        self.button1.clicked.connect(self.digit_pressed)
        self.button2.clicked.connect(self.digit_pressed)
        self.button3.clicked.connect(self.digit_pressed)
        self.button4.clicked.connect(self.digit_pressed)
        self.button5.clicked.connect(self.digit_pressed)
        self.button6.clicked.connect(self.digit_pressed)
        self.button7.clicked.connect(self.digit_pressed)
        self.button8.clicked.connect(self.digit_pressed)
        self.button9.clicked.connect(self.digit_pressed)

        self.decimalButton.clicked.connect(self.decimal_pressed)

        self.plusMinusButton.clicked.connect(self.plusMinus_pressed)
        self.percentButton.clicked.connect(self.percent_pressed)

        self.divideButton.clicked.connect(self.divide_pressed)
        self.multiplyButton.clicked.connect(self.multiply_pressed)
        self.minusButton.clicked.connect(self.minus_pressed)
        self.plusButton.clicked.connect(self.plus_pressed)

        self.equalButton.clicked.connect(self.equal_pressed)

        self.clearButton.clicked.connect(self.clear_pressed)

        self.op = None
        self.novoNumero = False

    #números
    def digit_pressed(self):
        button = self.sender()

        if self.novoNumero:
            newResultDisplay = format(float(button.text()), '.12g')
            self.novoNumero = False
        else:
            if(('.' in self.resultDisplay.text()) and (button.text() == "0")):
                if len(self.resultDisplay.text()) < 12:
                    newResultDisplay = self.resultDisplay.text() + button.text()
                else:
                    newResultDisplay = self.resultDisplay.text()
            else:
                newResultDisplay = format(float(self.resultDisplay.text() + button.text()), '.12g')

        self.resultDisplay.setText(newResultDisplay)

    #botão .
    def decimal_pressed(self):
        if "." not in self.resultDisplay.text():
            self.resultDisplay.setText(self.resultDisplay.text() + '.')

    #botão +/-
    def plusMinus_pressed(self):
        button = self.sender()
        labelNumber = float(self.resultDisplay.text())
        labelNumber = labelNumber * -1

        newLabel = format(labelNumber, '.12g')
        self.resultDisplay.setText(newLabel)

    #botão %
    def percent_pressed(self):
        button = self.sender()
        labelNumber = float(self.resultDisplay.text())
        labelNumber = labelNumber * 0.01
        newLabel = format(labelNumber, '.12g')
        self.resultDisplay.setText(newLabel)

    #botão ÷
    def divide_pressed(self):
        self.firstNumber = float(self.resultDisplay.text())
        self.op = '/'
        self.novoNumero = True

    #botão x
    def multiply_pressed(self):
        self.firstNumber = float(self.resultDisplay.text())
        self.op = 'x'
        self.novoNumero = True

    #botão -
    def minus_pressed(self):
        self.firstNumber = float(self.resultDisplay.text())
        self.op = '-'
        self.novoNumero = True

    #botão +
    def plus_pressed(self):
        self.firstNumber = float(self.resultDisplay.text())
        self.op = '+'
        self.novoNumero = True

    #botão =
    def equal_pressed(self):
        secondNumber = float(self.resultDisplay.text())

        if self.op == '/':
            if secondNumber == 0:
                str(self.resultDisplay.setText("Error!"))
            else:
                labelNumber = self.firstNumber / secondNumber
                newLabel = format(labelNumber, '.12g')
                self.resultDisplay.setText(newLabel)

        elif self.op == 'x':
            labelNumber = self.firstNumber * secondNumber
            newLabel = format(labelNumber, '.12g')
            self.resultDisplay.setText(newLabel)

        elif self.op == '-':
            labelNumber = self.firstNumber - secondNumber
            newLabel = format(labelNumber, '.12g')
            self.resultDisplay.setText(newLabel)

        elif self.op == '+':
            labelNumber = self.firstNumber + secondNumber
            newLabel = format(labelNumber, '.12g')
            self.resultDisplay.setText(newLabel)

        self.op = None

    def clear_pressed(self):
        self.resultDisplay.setText("0")

if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    main = FormMain()
    main.show()
    sys.exit(app.exec_())
# --------------------------
