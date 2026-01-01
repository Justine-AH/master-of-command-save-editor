from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

TYPE_MAP = {
    "RECRUIT_INFANTRY": "INFANTRY",
    "RECRUIT_LIGHT_CAVALRY": "CAVALRY",
    "SUPPLY_CARAVAN": "SUPPLY",
    "HEAVY_CAVALRY": "CAVALRY",
    "LINE_INFANTRY": "INFANTRY",
    "LIGHT_INFANTRY": "INFANTRY",
    "HEAVY_LINE_INFANTRY": "INFANTRY",
    "LIGHT_CAVALRY": "CAVALRY",
    "ARTILLERY": "ARTILLERY",
    "LIGHT_ARTILLERY": "ARTILLERY",
    "RECRUIT_ARTILLERY": "ARTILLERY",
}

SUPPLY_MULT = {
    "INFANTRY": 10,
    "CAVALRY": 15,
    "ARTILLERY": 80,
}

EXCLUDED_RAW_TYPES = {"SUPPLY_CARAVAN"}
LOC_UNITS_NAME_PREFIX = "Units/Name/"
EXCLUDED_ID_SUBSTRINGS = (
    "test",
    "debug",
    "dummy",
)

COLOR_KEYS = {
    "PrimaryColors",
    "SecondaryColors",
    "TertiaryColors",
    "QuaternaryColors",
}

PLACEHOLDER_COLOR = {"r": 45, "g": 45, "b": 45, "a": 255}