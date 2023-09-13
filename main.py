from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Faris Calculator")
        MainWindow.resize(392, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 70, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 70, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 70, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 110, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 110, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 110, 89, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 150, 89, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 150, 89, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 150, 89, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 190, 89, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 190, 89, 25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(250, 190, 91, 25))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 67, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(52, 40, 291, 25))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # prop - read only
        self.lineEdit.setReadOnly(True)

        # connection widget
        self.pushButton_12.clicked.connect(self.clearDisplay)
        self.pushButton.clicked.connect(self.action7)
        self.pushButton_2.clicked.connect(self.action8)
        self.pushButton_3.clicked.connect(self.action9)
        self.pushButton_4.clicked.connect(self.action4)
        self.pushButton_5.clicked.connect(self.action5)
        self.pushButton_6.clicked.connect(self.action6)
        self.pushButton_7.clicked.connect(self.action1)
        self.pushButton_8.clicked.connect(self.action2)
        self.pushButton_9.clicked.connect(self.action3)
        self.pushButton_11.clicked.connect(self.action0)

        # comboBox
        operator = ['+','-','/','*','%','=']
        self.comboBox.addItems(operator)
        self.comboBox.activated.connect(self.comboClicker)

    # comboClicker - event trigger when combobox being clicked
    def comboClicker(self):
        curr = self.displayText()
        if self.comboBox.currentText() == "=": 
            self.compute()
            return 
        self.setDisplayText(curr + self.comboBox.currentText())
    
    # compute - calculate equation
    def compute(self):
        equation = self.displayText()
        try:
            ans = eval(equation)
            self.setDisplayText(str(ans))
        except ZeroDivisionError:
            self.setDisplayText("Cannot divide by zero.")
        except:
            self.setDisplayText("Wrong Input")

    def action7(self):
        curr = self.displayText()
        self.setDisplayText(curr + "7")
    
    def action8(self):
        curr = self.displayText()
        self.setDisplayText(curr + "8")

    def action9(self):
        curr = self.displayText()
        self.setDisplayText(curr + "9")

    def action4(self):
        curr = self.displayText()
        self.setDisplayText(curr + "4")

    def action5(self):
        curr = self.displayText()
        self.setDisplayText(curr + "5")

    def action0(self):
        curr = self.displayText()
        self.setDisplayText(curr + "0")

    def action6(self):
        curr = self.displayText()
        self.setDisplayText(curr + "6")

    def action1(self):
        curr = self.displayText()
        self.setDisplayText(curr + "1")

    def action2(self):
        curr = self.displayText()
        self.setDisplayText(curr + "2")

    def action3(self):
        curr = self.displayText()
        self.setDisplayText(curr + "3")

    # displayText - get current value display
    def displayText(self):
        return self.lineEdit.text()
    
    # setDisplayText - updates display value
    def setDisplayText(self, text):
        self.lineEdit.setText(text)
        self.lineEdit.setFocus()

    # clearDisplay - clear display value
    def clearDisplay(self):
        self.setDisplayText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Faris Calculator"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "8"))
        self.pushButton_3.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "1"))
        self.pushButton_8.setText(_translate("MainWindow", "2"))
        self.pushButton_9.setText(_translate("MainWindow", "3"))
        self.pushButton_11.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "clear"))

#  main program
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
