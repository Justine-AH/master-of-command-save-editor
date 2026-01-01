import json
import os
from pathlib import Path
import pprint
import random
import sys
import tempfile
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFileDialog, QComboBox, QSpinBox, QTreeWidgetItem, QTableWidgetItem)
from save_editor_ui import Ui_MainWindow

DEV_FEATURES = os.getenv("DEV_FEATURES", "").lower() == "true"

# TODO: setting to remember paths?
# TODO: fix bust data, need to pick random and generate random when empty

class SaveEditor(QMainWindow, Ui_MainWindow):
    def __init__(self, q_app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.data = None
        self.unit_template = None
        self.flag_template = None
        self.bust_template = None
        self.upgrade_template = None
        self.loc_dict = None
        
        # Templates are needed for changing unit types or adding new units
        # unit stats, bust and flag are not attached to unit_types and must be manually changed
        # we need the templates for reference to generate or change units
        self.load_templates()
        self.populate_comboboxes(self.unit_template)
        
        self.q_app = q_app

        self.setWindowTitle("Master of Command - Save Editor")
        self.resize(1200, 800)
        self.statusBar().showMessage("Ready")
        
        self.actionSave_File.setEnabled(False)
        self.actionLoad_File.triggered.connect(self.on_load_button_trigger)
        self.actionSave_File.triggered.connect(self.on_save_button_trigger)
        
        
        index = self.tabWidget.indexOf(self.devTab)
        self.tabWidget.setTabVisible(index, False)
        
        if DEV_FEATURES:
            self.tabWidget.setTabVisible(index, True)
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
                json.dump(self.data, f, indent=2, ensure_ascii=False)

            os.replace(temp_path, path)
        except Exception:
            os.remove(temp_path)
            raise

    def load_data(self):
        if self.data is None or self.loc_dict is None:
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
            combo.setCurrentText(self.loc_dict[item["UnitID"]])
            combo.setProperty("originalValue", combo.currentData())
            spinbox.setValue(item["CurrentLevel"])
            spinbox.setProperty("originalValue", spinbox.value())
        
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
                combo.setCurrentText(self.loc_dict[regiment["UnitID"]])
                combo.setProperty("originalValue", combo.currentData())
                spinbox.setValue(regiment["CurrentLevel"])
                spinbox.setProperty("originalValue", spinbox.value())
        
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
        
        player_data = self.data["PlayerSaveData"]
        army_data = player_data["ArmySaveData"]
        divisions_data = army_data["Divisions"]
        reserve_divisions_data = army_data["ReserveRegiments"]
        
        # checks for unit type change
        for i in range(len(divisions_data)):
            for j in range(4):
                combo = getattr(self, f"regimentTypeComboBox_{i+1}_{j+1}", None)
                spinbox = getattr(self, f"veterancySpinBox_{i+1}_{j+1}", None)
                if not isinstance(combo, QComboBox):
                    continue
                if not isinstance(spinbox, QSpinBox):
                    continue
                
                combo_original = None if combo.property("originalValue") == "" else combo.property("originalValue")
                combo_current = combo.currentData()

                if combo_original != combo_current:
                    new_regiment = self.handle_unit_type_change(divisions_data[i]["Regiments"][j], combo_current)
                    divisions_data[i]["Regiments"][j] = new_regiment
                
                spin_original = spinbox.property("originalValue") or 0
                spin_current = spinbox.value()

                if spin_original != spin_current:
                    new_regiment = divisions_data[i]["Regiments"][j]
                    if new_regiment is not None:
                        new_regiment["CurrentLevel"] = spinbox.value()
                
        for i in range(len(reserve_divisions_data)):
            if reserve_divisions_data[i] is None:
                return
            
            combo = getattr(self, f"reserveTypeComboBox_{i+1}", None)
            spinbox = getattr(self, f"reserveVeterancySpinBox_{i+1}", None)
            if not isinstance(combo, QComboBox):
                continue
            if not isinstance(spinbox, QSpinBox):
                continue
            
            combo_original = None if combo.property("originalValue") == "" else combo.property("originalValue")
            combo_current = combo.currentData()

            if combo_original != combo_current:
                new_regiment = self.handle_unit_type_change(reserve_divisions_data[i], combo_current)
                reserve_divisions_data[i] = new_regiment

            spin_original = spinbox.property("originalValue") or 0
            spin_current = spinbox.value()

            if spin_original != spin_current:
                new_regiment = reserve_divisions_data[i]
                if new_regiment is not None:
                    new_regiment["CurrentLevel"] = spinbox.value()
    
    def handle_unit_type_change(self, regiment, new_unit_type):
        
        if self.unit_template is None:
            return
        if self.upgrade_template is None:
            return
        if self.flag_template is None:
            return
        if self.bust_template is None:
            return
        if self.loc_dict is None:
            return
        
        # TODO: handle adding and deleting units
        unit = self.unit_template[new_unit_type]
        flag_list = self.flag_template[unit["FlagTemplate"]]
        bust_list = self.bust_template[unit["ID"]]
        
        primary_color = random.choice(flag_list["PrimaryColors"])
        secondary_color = random.choice(flag_list["SecondaryColors"])
        pattern = random.choice(flag_list["Patterns"])
        emblem = random.choice(flag_list["Emblems"])
        
        flag = {
            "EmblemKey": emblem,
            "PrimaryColor": primary_color,
            "Patternkey": pattern,
            "SecondaryColor": secondary_color,
            "SecondaryDyeColor": "00FFFF",
            "PrimaryDyeColor": primary_color
        }
        
        tree_id, prereq = self.find_tree_and_prereq_by_unit_id(self.upgrade_template, new_unit_type)
        new_bust = self.validate_bust_data(bust_list)
        
        regiment["TargetManpower"] = unit["MaxManpower"]
        regiment["Manpower"] = unit["MaxManpower"]
        regiment["MaxManpower"] = unit["MaxManpower"]
        regiment["MeleeAttribute"] = unit["BaseStats"]["MeleeSkill"]
        regiment["AccuracyAttribute"] = unit["BaseStats"]["RangedSkill"]
        regiment["ReloadAttribute"] = unit["BaseStats"]["ReloadSkill"]
        regiment["MoraleAttribute"] = unit["BaseStats"]["Morale"]
        regiment["FatigueAttribute"] = unit["BaseStats"]["FatigueSkill"]
        regiment["ChargeBonusAttribute"] = int(unit["BaseStats"]["ChargeBonus"])
        regiment["WalkSpeed"] = int(unit["BaseStats"]["WalkSpeed"])
        regiment["RunSpeed"] = int(unit["BaseStats"]["SprintSpeed"])
        regiment["PreviousUnlockedUnits"] = prereq
        regiment["BustData"] = new_bust
        regiment["FlagSave"] = flag
        regiment["Name"] = self.loc_dict[unit["Name"].split("/")[-1]]
        regiment["UnitID"] = new_unit_type
        regiment["UpgradeTreeID"] = tree_id
                
        # "InfantryMaxSupply": 10,
        # "CavalryMaxSupply": 15,
        # "ArtilleryMaxSupply": 80,
        # regiment["Supply"] #??? dunno where this is based on, maybe by unit types?
        
        return regiment
    
    def find_tree_and_prereq_by_unit_id(self, data, unit_id):
        for tree_name, tree in data.items():
            items = tree["Items"]
            if unit_id in items:
                return tree_name, items[unit_id]["Prerequisite"] or []
        return None, []
    
    def validate_bust_data(self, data):
        COLOR_KEYS = {
            "PrimaryColors",
            "SecondaryColors",
            "TertiaryColors",
            "QuaternaryColors",
        }

        def make_placeholder():
            return [{
                "r": 45,
                "g": 45,
                "b": 45,
                "a": 255,
            }]

        # maybe recursive isnt optimal but it works...
        def walk(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    k_lower = key.lower()
                    if k_lower.endswith("colordata") and isinstance(value, dict):
                        for ck in COLOR_KEYS:
                            if ck in value and isinstance(value[ck], list):
                                if value[ck] == []:
                                    # empty lists causes color issues (ugly cyan)
                                    value[ck] = make_placeholder()
                                else:
                                    # game chooses only 1 color or it messes up customization
                                    value[ck] = [random.choice(value[ck])]
                    if k_lower == "items" and isinstance(value, list):
                        # game chooses only 1 item
                        if len(value) > 1:
                            obj[key] = [random.choice(value)]
                    walk(value)

            elif isinstance(obj, list):
                for item in obj:
                    walk(item)

        walk(data)
        return data

    def populate_comboboxes(self, unit_list):
        if self.loc_dict is None:
            return
        
        for i in range(5):
            combo = getattr(self, f"reserveTypeComboBox_{i+1}", None)
            if not isinstance(combo, QComboBox):
                continue
                    
            combo.blockSignals(True)
            combo.clear()

            combo.addItem(" ", None)

            for key, value in unit_list.items():
                if "test" in key.lower() or value["RawUnitType"] == "SUPPLY_CARAVAN":
                    continue
                # "Name": "Units/Name/RUS_Möller_Sakomelsky_Jägers"
                name_key = value["Name"].split("/")[-1]
                combo.addItem(self.loc_dict[name_key], key)

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
                    if "test" in key.lower() or value["RawUnitType"] == "SUPPLY_CARAVAN":
                        continue
                    name_key = value["Name"].split("/")[-1]
                    combo.addItem(self.loc_dict[name_key], key)

                combo.blockSignals(False)

    def load_templates(self):
        # Loading Unit Templates
        with open("./templates/Template_Units.json", "r", encoding="utf-8") as f:
            unit_template_list = json.load(f)
        
        self.unit_template = {unit["ID"]: unit for unit in unit_template_list}
        
        # Loading Upgrade Templates
        with open("./templates/UpgradeTrees.json", "r", encoding="utf-8") as f:
            upgrade_template_list = json.load(f)
        
        self.upgrade_template = upgrade_template_list
        
        # Loading Flag Templates
        with open("./templates/FlagTemplates.json", "r", encoding="utf-8") as f:
            flag_template_list = json.load(f)
        
        self.flag_template = flag_template_list["FlagTemplates"]
            
        # Loading Bust Templates
        bust_templates = {}
        folder_path = Path("./templates/Busts")
        for file in folder_path.glob("*.json"):
            with file.open("r", encoding="utf-8") as f:
                bust_templates[file.stem] = json.load(f)
        
        self.bust_template = bust_templates
        
        with open("./templates/English.json", "r", encoding="utf-8") as f:
            loc = json.load(f)["Terms"]
        
        self.loc_dict = {
            item["Key"].split("/")[-1]: item["Translation"]
            for item in loc
            if "Units/Name/" in item["Key"]
        }
        
        self.unitTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.unitTemplateTreeWidget.invisibleRootItem(), self.unit_template)
        self.flagTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.flagTemplateTreeWidget.invisibleRootItem(), self.flag_template)
        self.bustTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.bustTemplateTreeWidget.invisibleRootItem(), self.bust_template)
        self.upgradeTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.upgradeTemplateTreeWidget.invisibleRootItem(), self.upgrade_template)
        
        for row, (key, value) in enumerate(self.loc_dict.items()):
            self.locTableWidget.setRowCount(len(self.loc_dict))
            self.locTableWidget.setItem(row, 0, QTableWidgetItem(str(key)))
            self.locTableWidget.setItem(row, 1, QTableWidgetItem(str(value)))

        self.locTableWidget.resizeColumnsToContents()
    
    def add_dict_to_tree(self, parent, data):
        for k, v in data.items():
            item = QTreeWidgetItem([str(k)])

            if isinstance(v, dict):
                self.add_dict_to_tree(item, v)
            elif isinstance(v, list):
                for i, val in enumerate(v):
                    self.add_dict_to_tree(item, {f"[{i}]": val})
            else:
                item.setText(1, str(v))

            parent.addChild(item)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = SaveEditor(app)
    main_window.show()

    sys.exit(app.exec())
