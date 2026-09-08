default mother_affection = 70
default father_affection = 55
default butler_trust = 50

default mother_suspicion = 0
default father_suspicion = 0

default relationship_state = {
    "mother": {
        "affection": 70,
        "suspicion": 0,
    },
    "father": {
        "affection": 55,
        "suspicion": 0,
    },
        "butler": {
            "trust": 50,
        },
        "sword_instructor": {
            "respect": 35,
        },
        "magic_instructor": {
            "respect": 35,
        },
        "maid": {
            "trust": 40,
        },
    }

init python:
    def reset_relationship_state():
        store.mother_affection = 70
        store.father_affection = 55
        store.butler_trust = 50
        store.mother_suspicion = 0
        store.father_suspicion = 0
        store.relationship_state = {
            "mother": {
                "affection": 70,
                "suspicion": 0,
            },
            "father": {
                "affection": 55,
                "suspicion": 0,
            },
            "butler": {
                "trust": 50,
            },
            "sword_instructor": {
                "respect": 35,
            },
            "magic_instructor": {
                "respect": 35,
            },
            "maid": {
                "trust": 40,
            },
        }

    def adjust_relationship(npc_id, key, amount):
        if npc_id not in store.relationship_state:
            store.relationship_state[npc_id] = {}
        current = store.relationship_state[npc_id].get(key, 0)
        store.relationship_state[npc_id][key] = current + amount

        if npc_id == "mother" and key == "affection":
            store.mother_affection = store.relationship_state[npc_id][key]
        elif npc_id == "father" and key == "affection":
            store.father_affection = store.relationship_state[npc_id][key]
        elif npc_id == "butler" and key == "trust":
            store.butler_trust = store.relationship_state[npc_id][key]

        return store.relationship_state[npc_id][key]
