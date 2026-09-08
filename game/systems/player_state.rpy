default player_name = "Lord"
default player_age = 6

default player_level = 1
default player_exp = 0

default player_hp = 100
default player_max_hp = 100

default player_stamina = 100
default player_max_stamina = 100

default player_strength = 5
default player_agility = 5
default player_constitution = 5
default player_intelligence = 10
default player_perception = 8
default player_charisma = 6

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

init python:
    def reset_player_state():
        store.player_name = "Lord"
        store.player_age = 6
        store.player_level = 1
        store.player_exp = 0
        store.player_hp = 100
        store.player_max_hp = 100
        store.player_stamina = 100
        store.player_max_stamina = 100
        store.player_strength = 5
        store.player_agility = 5
        store.player_constitution = 5
        store.player_intelligence = 10
        store.player_perception = 8
        store.player_charisma = 6
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
