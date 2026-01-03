from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Optional, Protocol, TypeGuard
from constants import LOC_UNITS_NAME_PREFIX, TEMPLATES_DIR

class LoadedTemplateStore(Protocol):
    unit_template: dict[str, dict[str, Any]]
    upgrade_template: dict[str, Any]
    flag_template: dict[str, Any]
    bust_template: dict[str, Any]
    loc_dict: dict[str, str]
@dataclass
class TemplateStore():
    
    unit_template: Optional[dict[str, dict[str, Any]]] = None
    upgrade_template: Optional[dict[str, Any]] = None
    flag_template: Optional[dict[str, Any]] = None
    bust_template: Optional[dict[str, Any]] = None
    loc_dict: Optional[dict[str, str]] = None
        
    def load_templates(self):
        # Loading Unit Templates
        with open(TEMPLATES_DIR / "Template_Units.json", "r", encoding="utf-8") as f:
            unit_template_list = json.load(f)
        
        self.unit_template = {unit["ID"]: unit for unit in unit_template_list}
        
        # Loading Upgrade Templates
        with open(TEMPLATES_DIR / "UpgradeTrees.json", "r", encoding="utf-8") as f:
            upgrade_template_list = json.load(f)
        
        self.upgrade_template = upgrade_template_list
        
        # Loading Flag Templates
        with open(TEMPLATES_DIR / "FlagTemplates.json", "r", encoding="utf-8") as f:
            flag_template_list = json.load(f)
        
        self.flag_template = flag_template_list["FlagTemplates"]
            
        # Loading Bust Templates
        bust_templates = {}
        folder_path = Path(TEMPLATES_DIR / "Busts")
        for file in folder_path.glob("*.json"):
            with file.open("r", encoding="utf-8") as f:
                bust_templates[file.stem] = json.load(f)
        
        self.bust_template = bust_templates
        
        # Loading Localization Templates
        with open(TEMPLATES_DIR / "English.json", "r", encoding="utf-8") as f:
            loc = json.load(f)["Terms"]
        
        self.loc_dict = {
            item["Key"].split("/")[-1]: item["Translation"]
            for item in loc
            if LOC_UNITS_NAME_PREFIX in item["Key"]
        }

    def missing_templates(self) -> list[str]:
        missing: list[str] = []
        if self.unit_template is None:
            missing.append("unit_template")
        if self.upgrade_template is None:
            missing.append("upgrade_template")
        if self.flag_template is None:
            missing.append("flag_template")
        if self.bust_template is None:
            missing.append("bust_template")
        if self.loc_dict is None:
            missing.append("loc_dict")
        return missing

    def is_loaded(self) -> bool:
        return not self.missing_templates()
    
    def templates_ready(self, store: TemplateStore) -> TypeGuard[LoadedTemplateStore]:
        return (
            store.unit_template is not None
            and store.upgrade_template is not None
            and store.flag_template is not None
            and store.bust_template is not None
            and store.loc_dict is not None
        )