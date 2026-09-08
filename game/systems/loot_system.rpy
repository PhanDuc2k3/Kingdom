init python:
    LOOT_TABLES = {
        "ancient_dragon": [
            {"kind": "material", "id": "dragon_scale", "chance": 0.45},
            {"kind": "material", "id": "dragon_fang", "chance": 0.20},
            {"kind": "material", "id": "dragon_heart", "chance": 0.05},
            {"kind": "material", "id": "dragon_core", "chance": 0.01},
            {"kind": "item", "id": "dragon_slayer", "chance": 0.001},
        ],
    }

    def get_loot_table(source_id):
        return list(LOOT_TABLES.get(source_id, []))

    def roll_loot(source_id, rng=None):
        rng = rng or renpy.random.random
        drops = []
        for entry in get_loot_table(source_id):
            if rng() <= entry.get("chance", 0):
                drops.append({
                    "kind": entry.get("kind"),
                    "id": entry.get("id"),
                })
        return drops
