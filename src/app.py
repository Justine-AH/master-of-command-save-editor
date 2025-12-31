import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)
from PySide6.QtCore import Qt
from save_editor_ui import Ui_MainWindow

class SaveEditor(QMainWindow, Ui_MainWindow):
    def __init__(self, q_app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.q_app = q_app

        self.setWindowTitle("Master of Command - Save Editor")
        self.resize(1200, 800)
        self.statusBar().showMessage("Ready")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = SaveEditor(app)
    main_window.show()

    sys.exit(app.exec())
