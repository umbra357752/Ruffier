from PySide6.QtWidgets import QApplication, QWidget

app = QApplication([])

class Home(QWidget):
    def __init__(self):
        super().__init__()

window = Home()
window.show()

app.exec()