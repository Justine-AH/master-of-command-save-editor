import json
import os
import sys
import tempfile
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
        
        self.data = None
        
        self.q_app = q_app

        self.setWindowTitle("Master of Command - Save Editor")
        self.resize(1200, 800)
        self.statusBar().showMessage("Ready")
        
        self.actionSave_File.setEnabled(False)
        self.actionLoad_File.triggered.connect(self.on_load_button_trigger)
        self.actionSave_File.triggered.connect(self.on_save_button_trigger)
    
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
            self.data = json.load(f)
            
        self.load_data()
        self.actionSave_File.setEnabled(True)
        
    def on_save_button_trigger(self):
        self.save_data()
        
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Save Files (*.fcs)"
        )

        if not path:
            return
        
        dir_name = os.path.dirname(path)
        fd, temp_path = tempfile.mkstemp(dir=dir_name)

        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2)

            os.replace(temp_path, path)
        except Exception:
            os.remove(temp_path)
            raise

    def load_data(self):
        if self.data is None:
            return
        
        self.statusBar().showMessage("Save file loaded")
        
        player_data = self.data["PlayerSaveData"]
        
        self.goldSpinBox.setValue(player_data["Cash"])
        self.supplySpinBox.setValue(player_data["Food"])
        self.ammoSpinBox.setValue(player_data["Ammo"])
        self.manpowerSpinBox.setValue(player_data["Manpower"])
    
    def save_data(self):
        if self.data is None:
            return
        
        player_data = self.data["PlayerSaveData"]
        
        player_data["Cash"] = self.goldSpinBox.value()
        player_data["Food"] = self.supplySpinBox.value()
        player_data["Ammo"] = self.ammoSpinBox.value()
        player_data["Manpower"] = self.manpowerSpinBox.value()
        
        self.data["PlayerSaveData"] = player_data

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = SaveEditor(app)
    main_window.show()

    sys.exit(app.exec())
