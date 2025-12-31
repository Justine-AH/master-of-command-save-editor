import json
import os
import sys
import tempfile
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFileDialog, QComboBox, QSpinBox, QCheckBox)
from save_editor_ui import Ui_MainWindow
from constants import UNITS

DEV_FEATURES = os.getenv("DEV_FEATURES", "").lower() == "true"

# TODO: Yeesh, the unit stats are separate from unit type... might need to read game files
class SaveEditor(QMainWindow, Ui_MainWindow):
    def __init__(self, q_app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.populate_comboboxes(UNITS)
        
        self.data = None
        
        self.q_app = q_app

        self.setWindowTitle("Master of Command - Save Editor")
        self.resize(1200, 800)
        self.statusBar().showMessage("Ready")
        
        self.actionSave_File.setEnabled(False)
        self.actionLoad_File.triggered.connect(self.on_load_button_trigger)
        self.actionSave_File.triggered.connect(self.on_save_button_trigger)
        
        if DEV_FEATURES:
            with open("./save_folder/test.fcs", "r", encoding="utf-8") as f:
                self.data = json.load(f)
                
            self.load_data()
            self.actionSave_File.setEnabled(True)
    
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
        army_data = player_data["ArmySaveData"]
        divisions_data = army_data["Divisions"]
        reserve_regiments_data = army_data["ReserveRegiments"]
        reserve_officers_data = army_data["ReserveOfficers"]
        
        self.goldSpinBox.setValue(player_data["Cash"])
        self.supplySpinBox.setValue(player_data["Food"])
        self.ammoSpinBox.setValue(player_data["Ammo"])
        self.manpowerSpinBox.setValue(player_data["Manpower"])
    
        self.goldSpinBox.setValue(player_data["Cash"])
        self.supplySpinBox.setValue(player_data["Food"])
        self.ammoSpinBox.setValue(player_data["Ammo"])
        self.manpowerSpinBox.setValue(player_data["Manpower"])
        
        for i, item in enumerate(reserve_regiments_data):
            if item is None:
                continue
            combo = getattr(self, f"reserveTypeComboBox_{i+1}", None)
            spinbox = getattr(self, f"reserveVeterancySpinBox_{i+1}", None)
            if not isinstance(combo, QComboBox):
                continue
            if not isinstance(spinbox, QSpinBox):
                continue
            combo.setCurrentText(UNITS[item["UnitID"]])
            spinbox.setValue(item["CurrentLevel"])
        
        for i, item in enumerate(reserve_officers_data):
            pass
        
        for i in range(len(divisions_data)):
            for j in range(4):
                combo = getattr(self, f"regimentTypeComboBox_{i+1}_{j+1}", None)
                spinbox = getattr(self, f"veterancySpinBox_{i+1}_{j+1}", None)
                if not isinstance(combo, QComboBox):
                    continue
                if not isinstance(spinbox, QSpinBox):
                    continue
                regiment = divisions_data[i]["Regiments"][j]
                if regiment is None:
                    # no unit here
                    continue
                combo.setCurrentText(UNITS[regiment["UnitID"]])
                spinbox.setValue(regiment["CurrentLevel"])
        
    def save_data(self):
        if self.data is None:
            return
        
        player_data = self.data["PlayerSaveData"]
        army_data = player_data["ArmySaveData"]
        
        player_data["Cash"] = self.goldSpinBox.value()
        player_data["Food"] = self.supplySpinBox.value()
        player_data["Ammo"] = self.ammoSpinBox.value()
        player_data["Manpower"] = self.manpowerSpinBox.value()
        
        self.data["PlayerSaveData"] = player_data
    
    def populate_comboboxes(self, unit_list):
        for i in range(5):
            combo = getattr(self, f"reserveTypeComboBox_{i+1}", None)
            if not isinstance(combo, QComboBox):
                continue
                    
            combo.blockSignals(True)
            combo.clear()

            combo.addItem(" ", None)

            for key, value in unit_list.items():
                combo.addItem(value, key)

            combo.blockSignals(False)

            
        for i in range(5):
            for j in range(4):
                name = f"regimentTypeComboBox_{i+1}_{j+1}"
                combo = getattr(self, name, None)

                if not isinstance(combo, QComboBox):
                    continue
                    
                combo.blockSignals(True)
                combo.clear()

                combo.addItem(" ", None)

                for key, value in unit_list.items():
                    combo.addItem(value, key)

                combo.blockSignals(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = SaveEditor(app)
    main_window.show()

    sys.exit(app.exec())
