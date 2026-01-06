from functools import partial
import json
import os
import random
import sys
import tempfile
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow
)
from PySide6.QtCore import (QSettings, QTimer)
from PySide6.QtWidgets import (QFileDialog, QComboBox, QSpinBox, QMessageBox, QTableWidgetItem, QPushButton, QCheckBox)
from constants import *
from leader_dataclass import Leader
from main_window import Ui_MainWindow
from template_store import TemplateLoadError, TemplateStore, templates_ready
from ui_helper import UIHelperMixin

# TODO: maybe find directory of game files for template instead
# TODO: weapon and equipment contraints...
# TODO: skill desc
# TODO: isolate original value saving
DEV_FEATURES = os.getenv("DEV_FEATURES", "").lower() == "true"

class SaveEditor(UIHelperMixin, QMainWindow, Ui_MainWindow):
    def __init__(self, q_app, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_widget_lists()
        
        self.enable_widgets([self.actionLoad_File], False)
        self.enable_widgets([self.actionSave_File], False)
        
        self.data = None
        
        self.settings = QSettings(str(SETTINGS), QSettings.Format.IniFormat)

        # Templates are needed for changing unit types or adding new units
        # unit stats, bust and flag are not attached to unit_types and must be manually changed
        # we need the templates for reference to generate or change units
        self.templates = TemplateStore()
        
        saved_game_dir = self.settings.value("paths/game_dir", "", str)
        QTimer.singleShot(0, lambda: self.on_game_path_button_triggered(saved_game_dir))
        
        self.q_app = q_app

        self.setWindowTitle("Master of Command - Save Editor")
        self.resize(1200, 800)
        self.statusBar().showMessage("Ready")
        
        self.setup_connections()
        
        dev_index = self.tabWidget.indexOf(self.devTab)
        self.tabWidget.setTabVisible(dev_index, False)
        
        # not yet
        index2 = self.tabWidget.indexOf(self.inventoryTab)
        self.tabWidget.setTabVisible(index2, False)
        
        if DEV_FEATURES:
            self.tabWidget.setTabVisible(dev_index, True)
            with open("./save_folder/test.fcs", "r", encoding="utf-8") as f:
                self.data = json.load(f)
            
            self.refresh_ui()
            QTimer.singleShot(
                0, 
                lambda: self.load_data()
            )
            QTimer.singleShot(
                0, 
                lambda: self.set_original_values()
            )
            self.actionSave_File.setEnabled(True)
    
    def pick_game_folder(self) -> Path | None:
        folder = QFileDialog.getExistingDirectory(self, "Select game folder")
        return Path(folder) if folder else None

    def load_data(self):
        self.disable_all_widgets()
        self.refresh_ui()
        if self.data is None:
            return
        
        player_data = self.data["PlayerSaveData"]
        army_data = player_data["ArmySaveData"]
        divisions_data = army_data["Divisions"]
        reserve_regiments_data = army_data["ReserveRegiments"]
        reserve_leaders_data = army_data["ReserveOfficers"]
        
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
            combo.setCurrentText(self.get_unit_loc(item["UnitID"]))
            spinbox.setValue(item["CurrentLevel"])
        
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
                combo.setCurrentText(self.get_unit_loc(regiment["UnitID"]))
                spinbox.setValue(regiment["CurrentLevel"])
                
        for i, item in enumerate(reserve_leaders_data):
            if item is None:
                continue
            self.reserve_leader_label[i].setText(f"{item["Name"]} {item["LastName"]}")
            self.reserve_leader_level_spinbox[i].setValue(item["Level"])
            self.reserve_leader_skillpoints_spinbox[i].setValue(item["SkillPointsAvailable"])
            for j in range(len(item["SkillSaves"])):
                index = (i*5)+j
                combo = self.reserve_leader_skill_combos[index]
                combo.setCurrentText(self.get_skill_loc(item["SkillSaves"][j]))
        
        for i, item in enumerate(divisions_data):
            leader = item["OfficerSave"]
            if leader is None:
                continue
            self.leader_label[i].setText(f"{leader["Name"]} {leader["LastName"]}")
            self.leader_level_spinbox[i].setValue(leader["Level"])
            self.leader_skillpoints_spinbox[i].setValue(leader["SkillPointsAvailable"])
            for j in range(len(leader["SkillSaves"])):
                index = (i*5)+j
                combo = self.leader_skill_combos[index]
                combo.setCurrentText(self.get_skill_loc(leader["SkillSaves"][j]))

        self.on_load_file_UI_handler(len(divisions_data), len(reserve_leaders_data))
        
    def save_data(self):
        if self.data is None:
            return
        
        player_data = self.data["PlayerSaveData"]
        army_data = player_data["ArmySaveData"]
        divisions_data = army_data["Divisions"]
        reserve_regiments_data = army_data["ReserveRegiments"]
        reserve_officers_data = army_data["ReserveOfficers"]
        
        # resources
        player_data["Cash"] = self.goldSpinBox.value()
        player_data["Food"] = self.supplySpinBox.value()
        player_data["Ammo"] = self.ammoSpinBox.value()
        player_data["Manpower"] = self.manpowerSpinBox.value()
        
        # detect any change for future logging
        for i, item in enumerate(divisions_data):
            if item is not None:
                
                leader = item["OfficerSave"]
                
                if leader is not None:
                
                    leader_obj = Leader(leader)
                    
                    skill_set = []
                    for j in range(5):
                        index = ( i * 5 ) + j
                        combo = self.leader_skill_combos[index]
                        combo_current = combo.currentData()
                        
                        if combo_current:
                            skill_set.append(combo_current)
                    
                    
                    print(f"{leader_obj.data.get("Level")} != {self.leader_level_spinbox[i].value()}")
                    leader_obj.set_level(self.leader_level_spinbox[i].value())
                    leader_obj.set_skill_points(self.leader_skillpoints_spinbox[i].value())
                    leader_obj.set_skills(skill_set)
                    
                    item["OfficerSave"] = leader_obj.data
            
            ###############################################
            
            for j in range(4):
                combo = getattr(self, f"regimentTypeComboBox_{i+1}_{j+1}", None)
                spinbox = getattr(self, f"veterancySpinBox_{i+1}_{j+1}", None)
                if not isinstance(combo, QComboBox):
                    continue
                if not isinstance(spinbox, QSpinBox):
                    continue
                
                combo_current = combo.currentData()

                if self._detect_changed_value(combo, combo_current):
                    if combo_current is None:
                        new_regiment = None
                    else:
                        new_regiment = self.handle_unit_type_change(item["Regiments"][j], combo_current, j)
                    item["Regiments"][j] = new_regiment
                
                spin_current = spinbox.value()

                if self._detect_changed_value(spinbox, spin_current):
                    new_regiment = item["Regiments"][j]
                    if new_regiment is not None:
                        new_regiment["CurrentLevel"] = spinbox.value()
                
        for i, item in enumerate(reserve_officers_data):
            if item is None:
                continue
            
            leader_obj = Leader(item)
                    
            skill_set = []
            for j in range(5):
                index = ( i * 5 ) + j
                combo = self.reserve_leader_skill_combos[index]
                current_data = combo.currentData()
                
                if current_data:
                    skill_set.append(current_data)
            
            leader_obj.set_level(self.reserve_leader_level_spinbox[i].value())
            leader_obj.set_skill_points(self.reserve_leader_skillpoints_spinbox[i].value())
            leader_obj.set_skills(skill_set)
            
            item = leader_obj.data
            
        for i, item in enumerate(reserve_regiments_data):
            
            combo = getattr(self, f"reserveTypeComboBox_{i+1}", None)
            spinbox = getattr(self, f"reserveVeterancySpinBox_{i+1}", None)
            if not isinstance(combo, QComboBox):
                continue
            if not isinstance(spinbox, QSpinBox):
                continue
            
            combo_current = combo.currentData()

            if self._detect_changed_value(combo, combo_current):
                if combo_current is None:
                    new_regiment = None
                else:
                    new_regiment = self.handle_unit_type_change(item, combo_current, i)
                reserve_regiments_data[i] = new_regiment

            spin_current = spinbox.value()

            if self._detect_changed_value(spinbox, spin_current):
                new_regiment = item
                if new_regiment is not None:
                    new_regiment["CurrentLevel"] = spinbox.value()

    def handle_unit_type_change(self, regiment, new_unit_type, position):
        
        def find_tree_and_prereq_by_unit_id(data, unit_id):
            prereq_list = None
            tree = None
            for tree_name, tree in data.items():
                items = tree["Items"]
                if unit_id in items:
                    prereq_list = get_prereq(unit_id, tree["Items"])
                    return tree_name, prereq_list
            
            return None, []
        
        def get_prereq(unit_id, tree) -> list:
            prereq_list = tree.get(unit_id)["Prerequisite"]
            result = []
            
            if prereq_list is None:
                return []
            
            for item in prereq_list:
                res = get_prereq(item, tree)
                if res is None:
                    return []
                else:
                    result.append(item)
                    result.extend(res)
            
            return result
        
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
        
        if not templates_ready(self.templates):
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
        regiment["Name"] = unit["Name"]
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
            
        all_leader_skill_combos = [
            *self.leader_skill_combos,
            *self.reserve_leader_skill_combos,
        ]
        for combo in all_leader_skill_combos:
            self._populate_skill_combo(combo)
    
    def _populate_unit_combo(self, combo: QComboBox):
        if self.templates.unit_template is None:
            return
        
        combo.blockSignals(True)
        combo.clear()
        combo.addItem(" ", None)

        for key, value in self.templates.unit_template.items():
            if self._is_excluded(key.lower()) or value["RawUnitType"] in EXCLUDED_RAW_TYPES:
                continue
            combo.addItem(value["Name"], key)

        combo.blockSignals(False)
    
    def _populate_skill_combo(self, combo: QComboBox):
        if self.templates.skill_template is None:
            return
        
        combo.blockSignals(True)
        combo.clear()
        combo.addItem(" ", None)

        for key, value in self.templates.skill_template.items():
            combo.addItem(value, key)

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
        self.skillsTreeWidget.setHeaderLabels(["Key", "Value"])
        self.add_dict_to_tree(self.skillsTreeWidget.invisibleRootItem(), self.templates.skill_template)
        
        if self.templates.loc_dict is None:
            return
        
        for row, (key, value) in enumerate(self.templates.loc_dict.items()):
            self.locTableWidget.setRowCount(len(self.templates.loc_dict))
            self.locTableWidget.setItem(row, 0, QTableWidgetItem(str(key)))
            self.locTableWidget.setItem(row, 1, QTableWidgetItem(str(value)))

        self.locTableWidget.resizeColumnsToContents()
        
    def setup_connections(self):
        self.actionLoad_File.triggered.connect(self.on_load_button_triggered)
        self.actionSave_File.triggered.connect(self.on_save_button_triggered)
        self.actionSelect_Game_Folder.triggered.connect(self.on_game_path_button_triggered)
        
        create_buttons = [
            *self.create_reserve_leader_buttons,
            *self.create_leader_buttons,
        ]
        delete_buttons = [
            *self.delete_reserve_leader_buttons,
            *self.delete_leader_buttons
        ]
        for button in create_buttons:
            button.clicked.connect(
                partial(self.on_create_leader_button_triggered, button)
            )

        for button in delete_buttons:
            button.clicked.connect(
                partial(self.on_delete_leader_button_triggered, button)
            )
            
        for checkbox in self.division_checkboxes:
            checkbox.clicked.connect(
                partial(self.on_division_checkbox_triggered, checkbox)
            )
    
    def on_create_leader_button_triggered(self, widget: QPushButton):
        reserve: bool = widget.property("reserveLeader")
        index = int(widget.property("index"))
        
        if self.data is None:
            return
        
        leader_template = Leader()
        if reserve:
            self.data["PlayerSaveData"]["ArmySaveData"]["ReserveOfficers"][index] = leader_template.data
        else:
            divisions_data = self.data["PlayerSaveData"]["ArmySaveData"]["Divisions"]
            divisions_data[index]["OfficerSave"] = leader_template.data
        
        self.save_data()
        self.load_data()
    
    def on_delete_leader_button_triggered(self, widget: QPushButton):
        reserve: bool = widget.property("reserveLeader")
        index = int(widget.property("index"))
        
        if self.data is None:
            return
        
        if reserve:
            self.data["PlayerSaveData"]["ArmySaveData"]["ReserveOfficers"][index] = None
        else:
            divisions_data = self.data["PlayerSaveData"]["ArmySaveData"]["Divisions"]
            divisions_data[index]["OfficerSave"] = None
            
        self.save_data()
        self.load_data()
    
    def on_division_checkbox_triggered(self, widget: QCheckBox):
        index = int(widget.property("index"))
        checked: bool = widget.isChecked()
        
        end = index + 1 if checked else 5
        
        self.enable_divisions(index, end, checked)
        
        if checked:
            if index < 4:
                self.enable_widgets([self.division_checkboxes[index + 1]], True)
        else:
            self.enable_widgets(self.division_checkboxes[index + 1:], False)
        
        amount = index + 1 if checked else index
        self.modify_division_count(amount, checked)
        self.save_data()
        self.load_data()
    
    def modify_division_count(self, new_division_count, add: bool):
        if self.data is None:
            return
        
        divisions_data: list = self.data["PlayerSaveData"]["ArmySaveData"]["Divisions"]
        
        if add:
            while len(divisions_data) < new_division_count:
                divisions_data.append(json.loads(NEW_DIVISION_TEMPLATE))
        else:
            while len(divisions_data) > new_division_count:
                divisions_data.pop()
    
    def on_load_button_triggered(self):
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
            
        self.refresh_ui()
        self.load_data()
        self.set_original_values()
        self.actionSave_File.setEnabled(True)
    
    def on_save_button_triggered(self):
        
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
        
        self.load_data()

    def on_game_path_button_triggered(self, saved_path = None):
        if saved_path:
            game_path = Path(saved_path)
        else:
            game_path = self.pick_game_folder()
        
        if game_path is None:
            self.enable_widgets([self.actionLoad_File], False)
            return
        
        try:
            self.templates.load_templates(game_path)
        except TemplateLoadError as e:
            QMessageBox.critical(
                self, 
                "Templates not found",
                f"Couldn't find templates under the selected folder: {self.templates.missing_templates()}"
            )
            self.enable_widgets([self.actionLoad_File], False)
            return
        
        if templates_ready(self.templates):
            self.populate_comboboxes()
            self.populate_dev_tabs()
            self.settings.setValue("paths/game_dir", game_path.as_posix())
        
        self.enable_widgets([self.actionLoad_File], True)

    def _is_excluded(self, unit_id):
        uid = unit_id.lower()
        return any(sub in uid for sub in EXCLUDED_ID_SUBSTRINGS)
    
    def get_unit_loc(self, key, fallback = ""):
        if self.templates.unit_template is None:
            return fallback
        if not isinstance(key, str):
            return fallback
        
        unit = self.templates.unit_template.get(key)
        if unit is not None:
            return unit["Name"]
        return fallback
    
    def get_skill_loc(self, key, fallback = ""):
        if self.templates.skill_template is None:
            return fallback
        if not isinstance(key, str):
            return fallback
        
        skill = self.templates.skill_template.get(key)
        if skill is not None:
            return skill 
        else:
            return fallback

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = SaveEditor(app)
    main_window.show()

    sys.exit(app.exec())
