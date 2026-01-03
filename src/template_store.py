

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Optional
from constants import LOC_UNITS_NAME_PREFIX, TEMPLATES_DIR

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
    