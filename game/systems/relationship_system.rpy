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
        }
