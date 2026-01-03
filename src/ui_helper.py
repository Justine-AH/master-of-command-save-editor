

from PySide6.QtWidgets import QSpinBox, QComboBox

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
    
    def refresh_ui(self):
        self.reset_spinboxes()
        self.reset_comboboxes()
    
    def reset_spinboxes(self):
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
    
    def reset_comboboxes(self):
        comboboxes = [
            *self.regiment_combos,
            *self.reserve_combos,
        ]
        for w in comboboxes:
            w.blockSignals(True)
            w.setCurrentIndex(0)
            w.setProperty("originalValue", "")
            w.blockSignals(False)
    