default player_name = "Lord"
default player_age = 6
default player_month = 1

default player_level = 1
default player_exp = 0

default player_hp = 100
default player_max_hp = 100

default player_stamina = 100
default player_max_stamina = 100

default player_strength = 5
default player_dexterity = 5
default player_agility = 5
default player_constitution = 5
default player_intelligence = 10
default player_wisdom = 8
default player_perception = 8
default player_charisma = 6
default player_leadership = 4
default player_knowledge = 4

default player_gold = 0

default player_stat_exp = {
    "strength": 0,
    "agility": 0,
    "constitution": 0,
    "intelligence": 0,
    "perception": 0,
    "charisma": 0,
    "deception": 0,
    "combat": 0,
    "survival": 0,
}

default player_mastery = {
    "sword_mastery": 0,
    "magic_mastery": 0,
    "archery_mastery": 0,
    "healing_mastery": 0,
    "martial_mastery": 0,
    "politics_mastery": 0,
    "territory_management": 0,
    "exploration": 0,
}

init python:
    def reset_player_state():
        store.player_name = "Lord"
        store.player_age = 6
        store.player_month = 1
        store.player_level = 1
        store.player_exp = 0
        store.player_hp = 100
        store.player_max_hp = 100
        store.player_stamina = 100
        store.player_max_stamina = 100
        store.player_strength = 5
        store.player_dexterity = 5
        store.player_agility = 5
        store.player_constitution = 5
        store.player_intelligence = 10
        store.player_wisdom = 8
        store.player_perception = 8
        store.player_charisma = 6
        store.player_leadership = 4
        store.player_knowledge = 4
        store.player_gold = 0
        store.player_stat_exp = {
            "strength": 0,
            "agility": 0,
            "constitution": 0,
            "intelligence": 0,
            "perception": 0,
            "charisma": 0,
            "deception": 0,
            "combat": 0,
            "survival": 0,
        }
        store.player_mastery = {
            "sword_mastery": 0,
            "magic_mastery": 0,
            "archery_mastery": 0,
            "healing_mastery": 0,
            "martial_mastery": 0,
            "politics_mastery": 0,
            "territory_management": 0,
            "exploration": 0,
        }

    def get_player_stat(stat_id):
        return getattr(store, "player_%s" % stat_id, 0)

    def add_player_stat(stat_id, amount):
        attr = "player_%s" % stat_id
        current = getattr(store, attr, 0)
        setattr(store, attr, round(current + amount, 2))
        return getattr(store, attr)

    def add_player_mastery(mastery_id, amount):
        store.player_mastery[mastery_id] = round(store.player_mastery.get(mastery_id, 0) + amount, 2)
        return store.player_mastery[mastery_id]

    def add_mastery(mastery_id, amount):
        if not mastery_id.endswith("_mastery") and mastery_id in ("sword", "magic", "archery", "healing", "martial", "politics"):
            mastery_id = "%s_mastery" % mastery_id
        return add_player_mastery(mastery_id, amount)
