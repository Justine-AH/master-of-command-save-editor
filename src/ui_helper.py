

from PySide6.QtWidgets import QSpinBox, QComboBox, QTreeWidgetItem, QLabel, QPushButton

class UIHelperMixin:
    
    # for typehints
    goldSpinBox: QSpinBox
    supplySpinBox: QSpinBox
    ammoSpinBox: QSpinBox
    manpowerSpinBox: QSpinBox
    
    def init_widget_lists(self):
        self.resource_spinboxes: list[QSpinBox] = [
            self.goldSpinBox,
            self.supplySpinBox,
            self.ammoSpinBox,
            self.manpowerSpinBox
        ]

        self.regiment_combos: list[QComboBox] = [
            getattr(self, f"regimentTypeComboBox_{i}_{j}")
            for i in range(1, 6)
            for j in range(1, 5)
        ]

        self.regiment_spinboxes: list[QSpinBox] = [
            getattr(self, f"veterancySpinBox_{i}_{j}")
            for i in range(1, 6)
            for j in range(1, 5)
        ]

        self.reserve_combos: list[QComboBox] = [
            getattr(self, f"reserveTypeComboBox_{i}")
            for i in range(1, 6)
        ]

        self.reserve_spinboxes: list[QSpinBox] = [
            getattr(self, f"reserveVeterancySpinBox_{i}")
            for i in range(1, 6)
        ]
        
        self.create_leader_buttons: list[QPushButton] = [
            getattr(self, f"createLeaderButton_{i}")
            for i in range(1, 6)
        ]
        
        self.delete_leader_buttons: list[QPushButton] = [
            getattr(self, f"deleteLeaderButton_{i}")
            for i in range(1, 6)
        ]
        
        self.leader_label: list[QLabel] = [
            getattr(self, f'leaderNameLabel_{i}')
            for i in range(1, 6)
        ]
        
        self.leader_skill_combos: list[QComboBox] = [
            getattr(self, f'leaderComboBox_{i}_{j}')
            for i in range(1, 6)
            for j in range(1, 6)
        ]
        
        self.leader_level_spinbox: list[QSpinBox] = [
            getattr(self, f'leaderLevelSpinBox_{i}')
            for i in range(1, 6)
        ]
        
        self.leader_skillpoints_spinbox: list[QSpinBox] = [
            getattr(self, f'leaderSkillPointSpinBox_{i}')
            for i in range(1, 6)
        ]
        
        self.create_reserve_leader_buttons: list[QPushButton] = [
            getattr(self, f"reserveCreateLeaderButton_{i}")
            for i in range(1, 6)
        ]
        
        self.delete_reserve_leader_buttons: list[QPushButton] = [
            getattr(self, f"reserveDeleteLeaderButton_{i}")
            for i in range(1, 6)
        ]
        
        self.reserve_leader_label: list[QLabel] = [
            getattr(self, f'reserveLeaderNameLabel_{i}')
            for i in range(1, 6)
        ]
        
        self.reserve_leader_skill_combos: list[QComboBox] = [
            getattr(self, f'reserveLeaderComboBox_{i}_{j}')
            for i in range(1, 6)
            for j in range(1, 6)
        ]
        
        self.reserve_leader_level_spinbox: list[QSpinBox] = [
            getattr(self, f'reserveLeaderLevelSpinBox_{i}')
            for i in range(1, 6)
        ]
        
        self.reserve_leader_skillpoints_spinbox: list[QSpinBox] = [
            getattr(self, f'reserveLeaderSkillPointSpinBox_{i}')
            for i in range(1, 6)
        ]
    
    def refresh_ui(self):
        self.reset_army_spinboxes()
        self.reset_army_comboboxes()
        self.reset_leader_spinboxes()
        self.reset_leader_comboboxes()
        self.reset_leader_labels()
    
    def reset_army_spinboxes(self):
        spinboxes = [
            *self.resource_spinboxes,
            *self.regiment_spinboxes,
            *self.reserve_spinboxes,
        ]
        for w in spinboxes:
            w.blockSignals(True)
            w.setValue(0)
            w.setProperty("originalValue", 0)
            w.blockSignals(False)
    
    def reset_army_comboboxes(self):
        comboboxes = [
            *self.regiment_combos,
            *self.reserve_combos,
        ]
        for w in comboboxes:
            w.blockSignals(True)
            w.setCurrentIndex(0)
            w.setProperty("originalValue", "")
            w.blockSignals(False)
    
    def reset_leader_spinboxes(self):
        spinboxes = [
            *self.leader_level_spinbox,
            *self.leader_skillpoints_spinbox,
            *self.reserve_leader_level_spinbox,
            *self.reserve_leader_skillpoints_spinbox,
        ]
        for w in spinboxes:
            w.blockSignals(True)
            w.setValue(0)
            w.setProperty("originalValue", 0)
            w.blockSignals(False)
    
    def reset_leader_comboboxes(self):
        comboboxes = [
            *self.leader_skill_combos,
            *self.reserve_leader_skill_combos,
        ]
        for w in comboboxes:
            w.blockSignals(True)
            w.setCurrentIndex(0)
            w.setProperty("originalValue", "")
            w.blockSignals(False)
            
    def reset_leader_labels(self):
        comboboxes = [
            *self.leader_label,
            *self.reserve_leader_label
        ]
        for w in comboboxes:
            w.blockSignals(True)
            w.setText("")
            w.setProperty("originalValue", "")
            w.blockSignals(False)
    
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
    
    def on_load_file_UI_handler(self, divisions_enabled: int, reserve_leaders: int):
        # Maybe define proper division ui in future
        for i in range(divisions_enabled):
            self.enable_widgets([self.leader_label[i]])
            
            reg_start = i * 4
            self.enable_widgets(self.regiment_combos[reg_start: reg_start + 4])
            self.enable_widgets(self.regiment_spinboxes[reg_start: reg_start + 4])
            
            skill_start = i * 5
            if (self.leader_label[i].text()):
                self.enable_widgets([self.leader_level_spinbox[i]])
                self.enable_widgets([self.leader_skillpoints_spinbox[i]])
                self.enable_widgets(self.leader_skill_combos[skill_start: skill_start + 5])
                
                self.enable_widgets([self.delete_leader_buttons[i]])
            else:
                self.enable_widgets([self.create_leader_buttons[i]])
        
        for i in range(reserve_leaders):
            skill_start = i * 5
            if (self.reserve_leader_label[i].text()):
                self.enable_widgets([self.reserve_leader_level_spinbox[i]])
                self.enable_widgets([self.reserve_leader_skillpoints_spinbox[i]])
                self.enable_widgets(self.reserve_leader_skill_combos[skill_start: skill_start + 5])
                
                self.enable_widgets([self.delete_reserve_leader_buttons[i]])
            else:
                self.enable_widgets([self.create_reserve_leader_buttons[i]])
        
        self.enable_widgets([
            *self.resource_spinboxes,
            # reserve regiments
            *self.reserve_spinboxes,
            *self.reserve_combos,
        ])
    
    def enable_widgets(self, widgets: list):
        for w in widgets:
            w.blockSignals(True)
            w.setEnabled(True)
            w.blockSignals(False)
        
    def disable_all_widgets(self):
        widgets = [
            # regiments
            *self.regiment_spinboxes,
            *self.regiment_combos,
            # leaders
            *self.leader_label,
            *self.leader_level_spinbox,
            *self.leader_skillpoints_spinbox,
            *self.leader_skill_combos,
            *self.resource_spinboxes,
            # reserve regiments
            *self.reserve_spinboxes,
            *self.reserve_combos,
            # reserve leader
            *self.reserve_leader_label,
            *self.reserve_leader_level_spinbox,
            *self.reserve_leader_skillpoints_spinbox,
            *self.reserve_leader_skill_combos,
            # leader buttons
            *self.delete_leader_buttons,
            *self.create_leader_buttons,
            *self.delete_reserve_leader_buttons,
            *self.create_reserve_leader_buttons,
        ]
        for w in widgets:
            w.blockSignals(True)
            w.setEnabled(False)
            w.blockSignals(False)