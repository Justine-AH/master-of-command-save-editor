from dataclasses import dataclass, field
import json
from typing import Any
from constants import NEW_LEADER_TEMPLATE

# have to do it like this or we get problems with dict reference
def generate_template() -> dict[str, Any]:
    return json.loads(NEW_LEADER_TEMPLATE)

@dataclass
class Leader():
    data: dict[str, Any] = field(default_factory=generate_template)

    def set_level(self, level: int) -> None:
        self.data["Level"] = level

    def set_skill_points(self, points: int) -> None:
        self.data["SkillPointsAvailable"] = points

    def set_skills(self, skills: list[str]) -> None:
        self.data["SkillSaves"] = skills
        