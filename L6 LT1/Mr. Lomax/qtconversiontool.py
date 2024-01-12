import PyQt6.QtWidgets as qtw
#import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Feet to metres")

        layout = qtw.QFormLayout()

        validator = qtg.QIntValidator()
        self.lineEdit = qtw.QLineEdit("")
        self.lineEdit.setValidator(validator)

        self.label = qtw.QLabel("0")

        self.button1 = qtw.QPushButton("Go")
        self.button1.clicked.connect(self.button_click)

        layout.addRow("Feet", self.lineEdit)
        layout.addRow("Metres", self.label)
        layout.addRow(self.button1)

        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

    def button_click(self):
        self.label.setText(str(int(self.lineEdit.text()) / 3.281))


app = qtw.QApplication([])

window = MainWindow()
window.show()

app.exec()