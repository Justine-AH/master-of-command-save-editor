from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Optional, Protocol, TypeGuard
from constants import BUST_DIR, FLAG_DIR, LOC_DIR, QUESTS_DIR, SKILLS_DIR, UNITS_DIR, UPGRADE_DIR

class LoadedTemplateStore(Protocol):
    unit_template: dict[str, dict[str, Any]]
    upgrade_template: dict[str, Any]
    flag_template: dict[str, Any]
    bust_template: dict[str, Any]
    loc_dict: dict[str, str]
    skill_template: dict[str, Any]
    
@dataclass
class TemplateStore():
    
    unit_template: Optional[dict[str, dict[str, Any]]] = None
    upgrade_template: Optional[dict[str, Any]] = None
    flag_template: Optional[dict[str, Any]] = None
    bust_template: Optional[dict[str, Any]] = None
    loc_dict: Optional[dict[str, str]] = None
    skill_template: Optional[dict[str, Any]] = None
        
    def load_templates(self, game_path):
        # if game path invalid
        path = Path(game_path)
        
        try:
            # Loading Unit Templates
            with open(path / UNITS_DIR, "r", encoding="utf-8") as f:
                unit_template_list = json.load(f)
            
            self.unit_template = {unit["ID"]: unit for unit in unit_template_list}
            
            # Loading Upgrade Templates
            with open(path / UPGRADE_DIR, "r", encoding="utf-8") as f:
                upgrade_template_list = json.load(f)
            
            self.upgrade_template = upgrade_template_list
            
            # Loading Flag Templates
            with open(path / FLAG_DIR, "r", encoding="utf-8") as f:
                flag_template_list = json.load(f)
            
            self.flag_template = flag_template_list["FlagTemplates"]
                
            # Loading Bust Templates
            bust_templates = {}
            folder_path = Path(path / BUST_DIR)
            for file in folder_path.glob("*.json"):
                with file.open("r", encoding="utf-8") as f:
                    bust_templates[file.stem] = json.load(f)
            
            self.bust_template = bust_templates
            
            # Loading Skills Templates
            # the skill system of the game is convoluted, their definition are under Quests along other stuff like stratagems, etc.
            quests_templates = {}
            folder_path = Path(path / QUESTS_DIR)
            for file in folder_path.glob("*.json"):
                with file.open("r", encoding="utf-8") as f:
                    quests_templates[file.stem] = json.load(f)
                    
            skills_templates = {}
            folder_path = Path(path / SKILLS_DIR)
            for file in folder_path.glob("*.json"):
                with file.open("r", encoding="utf-8") as f:
                    skills_templates[file.stem] = json.load(f)
                    
            self.skill_template = {
                quest.get("ID"): quest.get("TooltipNodes")[0]["HeaderKey"] 
                for quest in quests_templates.values() 
                if quest.get("ID") in skills_templates.keys()
                and quest.get("TooltipNodes")
            }
            
            # Loading Localization Templates
            with open(path / LOC_DIR, "r", encoding="utf-8") as f:
                loc = json.load(f)["Terms"]
        
            self.setup_loc(loc)
            
        except FileNotFoundError as e:
            raise TemplateLoadError(f"Missing file: {path}") from e
        except json.JSONDecodeError as e:
            raise TemplateLoadError(f"Invalid JSON: {path}\n{e}") from e
        except OSError as e:
            raise TemplateLoadError(f"Could not read: {path}\n{e}") from e
        except TemplateLoadError:
            self.unit_template = None
            self.upgrade_template = None
            self.flag_template = None
            self.bust_template = None
            self.skill_template = None
            self.loc_dict = None
            raise
        
    def setup_loc(self, loc):
        if self.unit_template is None:
            return
        if self.skill_template is None:
            return
            
        self.loc_dict = {
            item["Key"]: item["Translation"]
            for item in loc
        }
        for key, value in self.unit_template.items():
            self.unit_template[key]["Name"] = self.loc_dict.get(str(value.get("Name")))
        for key, value in self.skill_template.items():
            self.skill_template[key] = self.loc_dict.get(value)

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
        if self.skill_template is None:
            missing.append("skill_template")
        return missing

    def is_loaded(self) -> bool:
        return not self.missing_templates()
    
class TemplateLoadError(Exception):
    """Raised when game templates fail to load."""
    pass
    
def templates_ready(store: TemplateStore) -> TypeGuard[LoadedTemplateStore]:
    return (
        store.unit_template is not None
        and store.upgrade_template is not None
        and store.flag_template is not None
        and store.bust_template is not None
        and store.loc_dict is not None
        and store.skill_template is not None
    )