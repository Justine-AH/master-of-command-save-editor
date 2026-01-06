import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS = BASE_DIR / "settings.ini"
VERSION = "1.0.0"

GAME_DIR = Path("Master Of Command_Data/StreamingAssets/GameData")
QUESTS_DIR = GAME_DIR / "Quests"
SKILLS_DIR = GAME_DIR / "Skills"
UNITS_DIR = GAME_DIR / "Units/Template_Units.json"
LOC_DIR = GAME_DIR / "Languages/English.json"
FLAG_DIR = GAME_DIR / "General/FlagTemplates.json"
BUST_DIR = GAME_DIR / "Busts"
UPGRADE_DIR = GAME_DIR / "Campaign/UpgradeTrees.json"

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

NEW_DIVISION_TEMPLATE = """
{
    "OfficerSave": null,
    "Regiments": [
        null,
        null,
        null,
        null
    ],
    "Name": "2nd Brigade"
}
"""
NEW_LEADER_TEMPLATE = """
{
    "Name": "John",
    "LastName": "Befehlmeister",
    "Level": 1,
    "Experience": 0,
    "SkillPointsAvailable": 0,
    "SkillSaves": [],
    "Uniform": "OFFICER_UNIFORM_AUS_06",
    "Head": "OFFICER_HEAD_06",
    "Hat": "OFFICER_HAT_00",
    "Hair": "OFFICER_HAIR_04",
    "StatsTracker": {
        "Kills": 0,
        "Losses": 0,
        "RecentKills": 0,
        "RecentLosses": 0,
        "BattlesWon": 0,
        "BattlesLoss": 0
    }
}
"""
NEW_UNIT_TEMPLATE = """
{
    "$type": "GameData.Save.PlayerRegimentSaveData, GameCore",
    "TargetManpower": 500,
    "CurrentExperience": 0,
    "CurrentLevel": 0,
    "MeleeAttribute": 25,
    "AccuracyAttribute": 10,
    "ReloadAttribute": 15,
    "MoraleAttribute": 60,
    "FatigueAttribute": 75,
    "ChargeBonusAttribute": 45,
    "WalkSpeed": 55,
    "RunSpeed": 85,
    "PreviousUnlockedUnits": [],
    "HasPlayerModifiedOutift": false,
    "RegimentStatsTracker": {
        "Kills": 0,
        "Losses": 0,
        "BattlesWon": 0,
        "BattlesLoss": 0,
        "RecentKills": 0,
        "RecentLosses": 0
    },
    "InventorySave": {
        "BackpackSlot": {
            "ItemSave": null
        },
        "BackpackSlots": [],
        "OffhandSlots": [
            {
            "ItemSave": null
            },
            {
            "ItemSave": null
            },
            {
            "ItemSave": null
            },
            {
            "ItemSave": null
            },
            {
            "ItemSave": null
            },
            {
            "ItemSave": null
            },
            {
            "ItemSave": null
            },
            {
            "ItemSave": null
            }
        ],
        "LockedOffHandSlots": [
            false,
            false,
            false,
            true,
            true,
            true,
            true,
            true
        ],
        "RangedWeaponSlot": {
            "ItemSave": null
        },
        "MeleeWeaponSlot": {
            "ItemSave": null
        }
    },
    "BustData": {
        "ID": "PRU_Deaths_Heads_Hussars",
        "Boots": {
        "BootsColorData": {
            "PrimaryColors": [
            {
                "r": 45,
                "g": 45,
                "b": 45,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false
        },
        "Items": [
            "BOOTS_BLACK_KNEE_BOOT"
        ]
        },
        "Hat": {
        "HatColorData": {
            "PrimaryColors": [
            {
                "r": 32,
                "g": 50,
                "b": 61,
                "a": 255
            }
            ],
            "SecondaryColors": [
            {
                "r": 239,
                "g": 239,
                "b": 239,
                "a": 255
            }
            ],
            "TertiaryColors": [
            {
                "r": 239,
                "g": 239,
                "b": 239,
                "a": 255
            }
            ],
            "QuaternaryColors": [
            {
                "r": 0,
                "g": 255,
                "b": 0,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false,
            "IsSecondaryFlagEditable": false,
            "IsTertiaryFlagEditable": false,
            "IsQuaternaryFlagEditable": false
        },
        "Items": [
            "HAT_HUSSAR_08"
        ]
        },
        "Pants": {
        "PantsColorData": {
            "PrimaryColors": [
            {
                "r": 45,
                "g": 45,
                "b": 45,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false
        }
        },
        "Shirt": {
        "ShirtColorData": {
            "PrimaryColors": [
            {
                "r": 45,
                "g": 45,
                "b": 45,
                "a": 255
            }
            ],
            "SecondaryColors": [
            {
                "r": 239,
                "g": 239,
                "b": 239,
                "a": 255
            }
            ],
            "TertiaryColors": [
            {
                "r": 43,
                "g": 43,
                "b": 43,
                "a": 255
            }
            ],
            "QuaternaryColors": [
            {
                "r": 229,
                "g": 229,
                "b": 229,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false,
            "IsSecondaryFlagEditable": false,
            "IsTertiaryFlagEditable": false,
            "IsQuaternaryFlagEditable": false
        },
        "Items": [
            "SHIRT_PELISSE"
        ]
        },
        "Skin": {
        "SkinColorData": {
            "PrimaryColors": [
            {
                "r": 203,
                "g": 164,
                "b": 144,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false
        },
        "Items": [
            "HEAD_4"
        ]
        },
        "Hair": {
        "HairColorData": {
            "PrimaryColors": [
            {
                "r": 212,
                "g": 212,
                "b": 212,
                "a": 255
            }
            ],
            "SecondaryColors": [
            {
                "r": 45,
                "g": 45,
                "b": 45,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false,
            "IsSecondaryFlagEditable": false
        },
        "Items": [
            "HAIR_1"
        ]
        },
        "Collar": {
        "CollarColorData": {
            "PrimaryColors": [
            {
                "r": 45,
                "g": 45,
                "b": 45,
                "a": 255
            }
            ],
            "SecondaryColors": [
            {
                "r": 32,
                "g": 50,
                "b": 61,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false,
            "IsSecondaryFlagEditable": false
        },
        "Items": [
            "COLLAR_03_HUSSAR"
        ]
        },
        "Straps": {
        "StrapsColorData": {
            "PrimaryColors": [
            {
                "r": 0,
                "g": 255,
                "b": 0,
                "a": 255
            }
            ],
            "SecondaryColors": [
            {
                "r": 0,
                "g": 255,
                "b": 0,
                "a": 255
            }
            ],
            "IsPrimaryFlagEditable": false
        },
        "Items": []
        },
        "Moustache": {
        "Items": [
            "FACIAL_HAIR_3"
        ]
        },
        "PlayerDirty": false,
        "UsePrimaryAsFallback": false
    },
    "FlagSave": {
        "EmblemKey": "Emblem_GEN_05",
        "PrimaryColor": "333333",
        "Patternkey": "GENERIC_PATTERN10",
        "SecondaryColor": "f5f6e6",
        "SecondaryDyeColor": "00FFFF",
        "PrimaryDyeColor": "333333"
    },
    "Name": "The Death's Head Hussars",
    "UnitID": "PRU_Deaths_Heads_Hussars",
    "Manpower": 500,
    "MaxManpower": 500,
    "DivisionPosition": 1,
    "UpgradeTreeID": null,
    "Supply": 140
}
"""