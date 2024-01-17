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
        self.button1.clicked.connect(self.convert)

        self.comboBox1 = qtw.QComboBox()
        self.comboBox1.addItems(["Feet", "Metres", "Inches", "Yards"])

        self.comboBox2 = qtw.QComboBox()
        self.comboBox2.addItems(["Feet", "Metres", "Inches", "Yards"])


        layout.addRow(self.comboBox1, self.lineEdit)
        layout.addRow(self.comboBox2, self.label)
        layout.addRow(self.button1)

        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

    def convert(self):
        dlg = qtw.QMessageBox.warning(self, "Convert?", "Are you sure you want to convert this number?", qtw.QMessageBox.StandardButton.Ok | qtw.QMessageBox.StandardButton.Cancel)
        if dlg == qtw.QMessageBox.StandardButton.Ok:
            
            units = {
                "Metres" : 1, "Feet" : 3.28084, "Inches" : 39.3701, "Yards" : 1.09361
            }

            #divide lineEdit.text() by units[comboBox1.currentText()], times by units[comboBox2.currentText()] ??
            #e.g. 2 inches in yards: 2 / 39.37 * 1.094 = ~0.0556

            calculatedDistance = int(self.lineEdit.text()) / units[self.comboBox1.currentText()] * units[self.comboBox2.currentText()]

            self.label.setText(str(round(calculatedDistance, 3)))
    


app = qtw.QApplication([])

window = MainWindow()
window.show()

app.exec()