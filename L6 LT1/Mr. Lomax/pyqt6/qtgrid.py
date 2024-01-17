import PyQt6.QtWidgets as qtw
#import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")
        self.setFixedSize(300,130)

        layout = qtw.QGridLayout()
        self.label = qtw.QLabel("Widget Demo")

        self.formLayout = qtw.QFormLayout()
        lineEdit1 = qtw.QLineEdit()
        lineEdit2 = qtw.QLineEdit()
        self.formLayout.addRow("Name:", lineEdit1)
        self.formLayout.addRow("Location:", lineEdit2)

        self.comboBox = qtw.QComboBox()
        self.comboBox.addItems(["One", "Two", "Three", "Four"])

        self.checkBox = qtw.QCheckBox("On or Off")

        self.pushButton1 = qtw.QPushButton("Ok")
        self.pushButton2 = qtw.QPushButton("Cancel")


        layout.addLayout(self.formLayout, 0, 0, 1, 3)
        layout.addWidget(self.comboBox, 1, 0, 1, 2)
        layout.addWidget(self.checkBox, 1, 2, 1, 1)
        layout.addWidget(self.pushButton1, 2, 1, 1, 1)
        layout.addWidget(self.pushButton2, 2, 2, 1, 1)



        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)


app = qtw.QApplication([])

window = MainWindow()
window.show()

app.exec()