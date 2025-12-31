import json
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)
from PySide6.QtCore import Qt
from save_editor_ui import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog

class SaveEditor(QMainWindow, Ui_MainWindow):
    def __init__(self, q_app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.save = None
        
        self.q_app = q_app

        self.setWindowTitle("Master of Command - Save Editor")
        self.resize(1200, 800)
        self.statusBar().showMessage("Ready")
        
        self.actionLoad_File.triggered.connect(self.on_load_button_trigger)
    
    def on_load_button_trigger(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Save Files (*.fcs *.json)"
        )

        if not path:
            return

        with open(path, "r", encoding="utf-8") as f:
            self.save = json.load(f)
            
        self.load_data()

    def load_data(self):
        if self.save is not None:
            self.statusBar().showMessage("Save file loaded")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = SaveEditor(app)
    main_window.show()

    sys.exit(app.exec())
