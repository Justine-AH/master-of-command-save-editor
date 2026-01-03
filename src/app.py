import json
import os
import random
import sys
import tempfile
from typing import TypeGuard
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)
from PySide6.QtCore import (QSettings, Slot)
from PySide6.QtWidgets import (QFileDialog, QComboBox, QSpinBox, QTreeWidgetItem, QTableWidgetItem)
from constants import *
from main_window import Ui_MainWindow
from template_store import TemplateStore
from ui_helper import UIHelperMixin

# TODO: maybe find directory of game files for template instead
# TODO: weapon and equipment contraints...

DEV_FEATURES = os.getenv("DEV_FEATURES", "").lower() == "true"

class SaveEditor(UIHelperMixin, QMainWindow, Ui_MainWindow):
    def __init__(self, q_app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_widget_lists()
        
        self.data = None
        
        self.settings = QSettings(str(SETTINGS), QSettings.Format.IniFormat)

        # Templates are needed for changing unit types or adding new units
        # unit stats, bust and flag are not attached to unit_types and must be manually changed
        # we need the templates for reference to generate or change units
        self.templates = TemplateStore()
        self.templates.load_templates()
        self.populate_comboboxes()
        self.populate_dev_tabs()
        
        self.q_app = q_app

        self.setWindowTitle("Master of Command - Save Editor")
        self.resize(1200, 800)
        self.statusBar().showMessage("Ready")
        
        self.actionSave_File.setEnabled(False)
        self.actionLoad_File.triggered.connect(self.load_button_triggered)
        self.actionSave_File.triggered.connect(self.save_button_triggered)
        
        index = self.tabWidget.indexOf(self.devTab)
        self.tabWidget.setTabVisible(index, False)
        
        if DEV_FEATURES:
            self.tabWidget.setTabVisible(index, True)
            with open("./save_folder/test.fcs", "r", encoding="utf-8") as f:
                self.data = json.load(f)
                
            self.load_data()
            self.actionSave_File.setEnabled(True)
    
    @Slot()
    def load_button_triggered(self):
        last = self.settings.value("paths/last_open_dir", "", str)
        if last is None:
            last = ""
            
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            str(last),
            "Save Files (*.fcs *.json)"
        )

        if path:
            self.settings.setValue("paths/last_open_dir", path)

        if not path:
            return

        with open(path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
            
        self.load_data()
        self.actionSave_File.setEnabled(True)
    
    @Slot()
    def save_button_triggered(self):
        
        self.save_data()
        
        last = self.settings.value("paths/last_open_dir", "", str)
        if last is None:
            last = ""
        
        
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            str(last),
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
        if self.data is None or self.templates.loc_dict is None:
            return
        
        self.refresh_ui()
        self.statusBar().showMessage("Save file loaded")
        
        player_data = self.data["PlayerSaveData"]
        army_data = player_data["ArmySaveData"]
        divisions_data = army_data["Divisions"]
        reserve_regiments_data = army_data["ReserveRegiments"]
        # reserve_officers_data = army_data["ReserveOfficers"]
        
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
            combo.setCurrentText(self.templates.loc_dict[item["UnitID"]])
            combo.setProperty("originalValue", combo.currentData())
            spinbox.setValue(item["CurrentLevel"])
            spinbox.setProperty("originalValue", spinbox.value())
        
        # for i, item in enumerate(reserve_officers_data):
        #     pass
        
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
                combo.setCurrentText(self.templates.loc_dict[regiment["UnitID"]])
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
                    if combo_current is None:
                        new_regiment = None
                    else:
                        new_regiment = self.handle_unit_type_change(divisions_data[i]["Regiments"][j], combo_current, j)
                    divisions_data[i]["Regiments"][j] = new_regiment
                
                spin_original = spinbox.property("originalValue") or 0
                spin_current = spinbox.value()

                if spin_original != spin_current:
                    new_regiment = divisions_data[i]["Regiments"][j]
                    if new_regiment is not None:
                        new_regiment["CurrentLevel"] = spinbox.value()
                
        for i in range(len(reserve_divisions_data)):
            if reserve_divisions_data[i] is None:
                continue
            
            combo = getattr(self, f"reserveTypeComboBox_{i+1}", None)
            spinbox = getattr(self, f"reserveVeterancySpinBox_{i+1}", None)
            if not isinstance(combo, QComboBox):
                continue
            if not isinstance(spinbox, QSpinBox):
                continue
            
            combo_original = None if combo.property("originalValue") == "" else combo.property("originalValue")
            combo_current = combo.currentData()

            if combo_original != combo_current:
                if combo_current is None:
                    new_regiment = None
                else:
                    new_regiment = self.handle_unit_type_change(reserve_divisions_data[i], combo_current, i)
                reserve_divisions_data[i] = new_regiment

            spin_original = spinbox.property("originalValue") or 0
            spin_current = spinbox.value()

            if spin_original != spin_current:
                new_regiment = reserve_divisions_data[i]
                if new_regiment is not None:
                    new_regiment["CurrentLevel"] = spinbox.value()

    def handle_unit_type_change(self, regiment, new_unit_type, position):
        
        def find_tree_and_prereq_by_unit_id(data, unit_id):
            for tree_name, tree in data.items():
                items = tree["Items"]
                if unit_id in items:
                    return tree_name, items[unit_id]["Prerequisite"] or []
            return None, []
        
        def validate_bust_data(data):
            def make_placeholder():
                return [PLACEHOLDER_COLOR]

            # ? this now mutates the template with randoms but maybe that better
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
        
        if not self.templates.templates_ready(self.templates):
            # ? might need to add logging in future
            print("Templates missing:", self.templates.missing_templates())
            return
        
        if regiment is None:
            regiment = json.loads(NEW_UNIT_TEMPLATE)
        
        unit = self.templates.unit_template[new_unit_type]
        flag_list = self.templates.flag_template[unit["FlagTemplate"]]
        bust_list = self.templates.bust_template[unit["ID"]]
        
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
        
        category = TYPE_MAP[unit["RawUnitType"]]
        supply = SUPPLY_MULT[category]

        tree_id, prereq = find_tree_and_prereq_by_unit_id(self.templates.upgrade_template, new_unit_type)
        new_bust = validate_bust_data(bust_list)
        
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
        regiment["Name"] = self.templates.loc_dict[unit["Name"].split("/")[-1]]
        regiment["UnitID"] = new_unit_type
        regiment["UpgradeTreeID"] = tree_id
        regiment["Supply"] = int((unit["MaxManpower"] // 100) * supply)
        regiment["DivisionPosition"] = position
        
        return regiment
    
    def populate_comboboxes(self):
                
        for i in range(5):
            combo = getattr(self, f"reserveTypeComboBox_{i+1}", None)
            if not isinstance(combo, QComboBox):
                continue
                
            self._populate_unit_combo(combo)

            
        for i in range(5):
            for j in range(4):
                name = f"regimentTypeComboBox_{i+1}_{j+1}"
                combo = getattr(self, name, None)

                if not isinstance(combo, QComboBox):
                    continue
                
                self._populate_unit_combo(combo)
    
    def _populate_unit_combo(self, combo: QComboBox):
        if self.templates.loc_dict is None:
            return
        if self.templates.unit_template is None:
            return
        
        combo.blockSignals(True)
        combo.clear()
        combo.addItem(" ", None)

        for key, value in self.templates.unit_template.items():
            if self._is_excluded(key.lower()) or value["RawUnitType"] in EXCLUDED_RAW_TYPES:
                continue
            # ex. "Name": "Units/Name/RUS_Möller_Sakomelsky_Jägers"
            name_key = value["Name"].split("/")[-1]
            combo.addItem(self.templates.loc_dict[name_key], key)

        combo.blockSignals(False)
    
    def populate_dev_tabs(self):
        self.unitTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.unitTemplateTreeWidget.invisibleRootItem(), self.templates.unit_template)
        self.flagTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.flagTemplateTreeWidget.invisibleRootItem(), self.templates.flag_template)
        self.bustTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.bustTemplateTreeWidget.invisibleRootItem(), self.templates.bust_template)
        self.upgradeTemplateTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.upgradeTemplateTreeWidget.invisibleRootItem(), self.templates.upgrade_template)
        
        if self.templates.loc_dict is None:
            return
        
        for row, (key, value) in enumerate(self.templates.loc_dict.items()):
            self.locTableWidget.setRowCount(len(self.templates.loc_dict))
            self.locTableWidget.setItem(row, 0, QTableWidgetItem(str(key)))
            self.locTableWidget.setItem(row, 1, QTableWidgetItem(str(value)))

        self.locTableWidget.resizeColumnsToContents()
        
    def _is_excluded(self, unit_id):
        uid = unit_id.lower()
        return any(sub in uid for sub in EXCLUDED_ID_SUBSTRINGS)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = SaveEditor(app)
    main_window.show()

    sys.exit(app.exec())
