import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg

import qdarktheme
import re

class FindDialog(qtw.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Find')
        self.layout = qtw.QVBoxLayout()
        self.text_to_find = qtw.QLineEdit()
        self.next_button = qtw.QPushButton('Next')
        self.prev_button = qtw.QPushButton('Previous')
        self.layout.addWidget(self.text_to_find)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.prev_button)
        self.setLayout(self.layout)

        self.next_button.clicked.connect(self.on_next_clicked)
        self.prev_button.clicked.connect(self.on_prev_clicked)

    def on_next_clicked(self):
        text = self.text_to_find.text()
        self.parent().find_text(text, forward=True)

    def on_prev_clicked(self):
        text = self.text_to_find.text()
        self.parent().find_text(text, forward=False)

class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()

        #Setup
        self.setWindowTitle("Bonchrstianote")
        self.opened = False
        self.layout = qtw.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.resize(960,540)

        self.not_opened_label = qtw.QLabel("No file open\nPress Ctrl+O to choose/create a file.")
        self.layout.addWidget(self.not_opened_label)
        self.not_opened_label.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
        self.not_opened_label.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        #Create textEdit widget --> added to layout when file is opened in open_button()
        self.textEdit = qtw.QTextEdit()
        self.textEdit.setStyleSheet("QTextEdit:focus { border: none; }")
        self.textEdit.setFont(qtg.QFont('Arial', 11))

        #Menus init
        menubar = self.menuBar()
        self.file_menu = menubar.addMenu("&File")
        self.edit_menu = menubar.addMenu("&Edit")
        self.file_menu.setIcon(qtg.QIcon(r"L6 LT1\Mr. Lomax\pyqt6\texteditor\media\fileicon.png"))
        self.edit_menu.setIcon(qtg.QIcon(r"L6 LT1\Mr. Lomax\pyqt6\texteditor\media\editicon.png"))

        #Open + save button
        open_action = qtg.QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_button)
        self.save_action = qtg.QAction('Save', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.save_button)

        #File menu
        self.file_menu.addAction(open_action)
        self.file_menu.addAction(self.save_action)
        self.save_action.setVisible(False)
        self.file_menu.addSeparator()
        self.file_menu.addAction("&Exit", self.exit_button)

        #Edit menu
        copy_action = qtg.QAction('Copy', self)
        copy_action.setShortcut('Ctrl+C')
        copy_action.triggered.connect(self.copy_button)  
        self.edit_menu.addAction(copy_action)

        paste_action = qtg.QAction('Paste', self)
        paste_action.setShortcut('Ctrl+V')
        paste_action.triggered.connect(self.paste_button)  
        self.edit_menu.addAction(paste_action)

        cut_action = qtg.QAction('Cut', self)
        cut_action.setShortcut('Ctrl+X')
        cut_action.triggered.connect(self.cut_button)  
        self.edit_menu.addAction(cut_action)

        self.edit_menu.addSeparator()

        undo_action = qtg.QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.textEdit.undo)
        self.edit_menu.addAction(undo_action)

        redo_action = qtg.QAction('Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.textEdit.redo)
        self.edit_menu.addAction(redo_action)

        self.edit_menu.addSeparator()

        find_action = qtg.QAction('Find', self)
        find_action.setShortcut('Ctrl+F')
        find_action.triggered.connect(self.open_find_dialog)
        self.edit_menu.addAction(find_action)

        #Toolbar
        self.toolbar = qtw.QToolBar("self.toolbar")
        self.addToolBar(self.toolbar)
        self.toolbar.setVisible(False)

        #Styles
        font_action = qtg.QAction('Font', self)
        font_action.triggered.connect(self.change_font)
        font_action.setIcon(qtg.QIcon(r"L6 LT1\Mr. Lomax\pyqt6\texteditor\media\fonticon.png"))
        self.toolbar.addAction(font_action)

        bullet_action = qtg.QAction('Bullet Points', self)
        bullet_action.triggered.connect(self.apply_bullet_points)
        bullet_action.setIcon(qtg.QIcon(r"L6 LT1\Mr. Lomax\pyqt6\texteditor\media\bulletpointsicon.png"))
        self.toolbar.addAction(bullet_action)

        image_action = qtg.QAction('Insert Image', self)
        image_action.triggered.connect(self.insert_image)
        image_action.setIcon(qtg.QIcon(r"L6 LT1\Mr. Lomax\pyqt6\texteditor\media\imageicon.png"))
        self.toolbar.addAction(image_action)

        #Setup
        widget = qtw.QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def open_button(self):
        self.opened = True
        self.filename, _ = qtw.QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.md)")
        
        if self.filename:

            self.setWindowTitle(self.filename)

            self.not_opened_label.setVisible(False)
            self.save_action.setVisible(True)
            self.layout.addWidget(self.textEdit)
            self.toolbar.setVisible(True)
            
            with open(self.filename, 'r') as file:
                text = file.read()
            self.textEdit.setHtml(text)

    def save_button(self):
        with open(self.filename, 'w') as file:
            file.write(self.textEdit.toHtml())

    def exit_button(self):
        saved = False
        if self.opened:
            with open(self.filename, 'r') as file:
                file_text = file.read()
                editor_text = self.textEdit.toHtml()
                if file_text == editor_text:
                    saved = True

            if saved == False: 
                dlg = qtw.QMessageBox.warning(self, "Exit", "Close editor?\nAny unsaved changes will be lost", qtw.QMessageBox.StandardButton.Ok | qtw.QMessageBox.StandardButton.Cancel)
                if dlg == qtw.QMessageBox.StandardButton.Ok:
                    qtw.QApplication.quit()
            else:
                qtw.QApplication.quit()
        else:
            qtw.QApplication.quit()

    def copy_button(self):
        clipboard = qtw.QApplication.clipboard()
        selected_text = self.textEdit.textCursor().selectedText()
        clipboard.setText(selected_text)

    def paste_button(self):
        clipboard = qtw.QApplication.clipboard()
        clipboard_text = clipboard.text()
        self.textEdit.insertPlainText(clipboard_text)

    def cut_button(self):
        clipboard = qtw.QApplication.clipboard()
        selected_text = self.textEdit.textCursor().selectedText()
        clipboard.setText(selected_text)
        self.textEdit.insertPlainText('')

    def change_font(self):
        current_font = self.textEdit.currentFont()
        font, ok = qtw.QFontDialog.getFont(current_font, self)
        if ok:
            self.textEdit.setFont(font)

    def apply_bullet_points(self):
        cursor = self.textEdit.textCursor()

        #Start a new block (paragraph) with bullet list format
        cursor.insertBlock()
        list_format = qtg.QTextListFormat()
        list_format.setStyle(qtg.QTextListFormat.Style.ListDisc)#Style for bullet points
    
        #Apply the list format to the current block
        cursor.createList(list_format)

    def insert_image(self):
        imagename, _ = qtw.QFileDialog.getOpenFileName(self, "Open Image File", ".", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")

        if imagename:
            size, ok = qtw.QInputDialog.getText(self, "Image Size", "Enter image size (width x height):\ne.g., 100x100")
            if ok and size:
                if re.search("\d+\s*[xX]\s*\d+", size):
                    width, height = re.split("[Xx]", size)
                    html_img = f'<img src="{imagename}" width="{width}" height="{height}" />'
                    cursor = self.textEdit.textCursor()
                    cursor.insertHtml(html_img)

    def open_find_dialog(self):
        self.find_dialog = FindDialog(self)
        self.find_dialog.show()

    def find_text(self, text, forward=True):
        options = qtg.QTextDocument.FindFlag(0)
        if not forward:
            options |= qtg.QTextDocument.FindFlag.FindBackward
        
        self.textEdit.find(text, options)
                    


app = qtw.QApplication([])
qdarktheme.setup_theme()

app.setWindowIcon(qtg.QIcon(r'L6 LT1\Mr. Lomax\pyqt6\texteditor\media\mainicon.png'))

window = MainWindow()
window.show()

app.exec()