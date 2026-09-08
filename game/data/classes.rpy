init python:
    CLASS_DEFINITIONS = {
        "swordsman": {
            "id": "swordsman",
            "name": "Kiếm sĩ",
            "requirements": {"sword_mastery": 8},
            "hidden": False,
            "discovery_event_id": "event_first_class_swordsman",
        },
        "mage": {
            "id": "mage",
            "name": "Pháp sư",
            "requirements": {"magic_mastery": 8},
            "hidden": False,
            "discovery_event_id": "event_first_class_mage",
        },
        "magic_swordsman": {
            "id": "magic_swordsman",
            "name": "Ma kiếm sĩ",
            "requirements": {"sword_mastery": 10, "magic_mastery": 10},
            "required_traits": ["mana_affinity"],
            "hidden": True,
            "discovery_event_id": "event_magic_swordsman_discovery",
        },
    }
