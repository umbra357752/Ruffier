from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit

app = QApplication([])

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.widgets()

        self.setLayout(self.lyt)

    def ui_init(self):
        self.setWindowTitle("Informacion App")     
        self.setFixedWidth(640)
        self.setFixedHeight(480)

    def widgets(self):
        self.lyt = QVBoxLayout()

        self.lbl_info = QLabel("Aplicacion Ruffier")
        self.btn = QPushButton("Iniciar")

        self.lyt.addWidget(self.lbl_info)
        self.lyt.addWidget(self.btn)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
        self.widgets()

        self.setLayout(self.lyt)

    def ui_init(self):
        self.setWindowTitle("Ruffier Test")     
        self.setFixedWidth(640)
        self.setFixedHeight(480)

    def widgets(self):
        self.lyt = QVBoxLayout()

        self.lbl_name = QLabel("Nombre")
        self.input_name = QLineEdit()

        self.lyt.addWidget(self.lbl_name)
        self.lyt.addWidget(self.input_name)

window = App()
window.show()

app.exec()