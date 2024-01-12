import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")
        self.setFixedSize(200,300)

        layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel("Widget Demo")

        self.comboBox = qtw.QComboBox()
        self.comboBox.addItem("One")
        self.comboBox.addItem("Two")
        self.comboBox.addItem("Three")
        self.comboBox.addItem("Four")
        
        self.checkBox1 = qtw.QCheckBox("Choose this")
        self.checkBox2 = qtw.QCheckBox("and this?")

        self.lineEdit = qtw.QLineEdit("Type here")
        
        self.radioButton1 = qtw.QRadioButton("This one?")
        self.radioButton2 = qtw.QRadioButton("Or this one?")
        
        self.slider = qtw.QSlider(qtc.Qt.Orientation.Horizontal)
        
        self.button1 = qtw.QPushButton("Ok")
        self.button2 = qtw.QPushButton("Cancel")


        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.RadioButton1)
        layout.addWidget(self.RadioButton2)
        layout.addWidget(self.slider)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)


app = qtw.QApplication([])

window = MainWindow()
window.show()

app.exec()