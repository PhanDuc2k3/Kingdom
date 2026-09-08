default world_flags = {}
default completed_event_ids = []
default recent_event_ids = []
default pending_event_id = None
default last_event_result = {}
default used_activity_dialogue = {}

init python:
    EVENT_PRIORITY_ORDER = {
        "main": 500,
        "conditional": 400,
        "class_discovery": 350,
        "relationship": 250,
        "random": 100,
    }

    def reset_event_state():
        store.world_flags = {}
        store.completed_event_ids = []
        store.recent_event_ids = []
        store.pending_event_id = None
        store.last_event_result = {}
        store.used_activity_dialogue = {}

    def set_world_flag(flag_id, value=True):
        store.world_flags[flag_id] = value
        return value

    def has_world_flag(flag_id):
        return bool(store.world_flags.get(flag_id, False))

    def event_completed(event_id):
        return event_id in store.completed_event_ids

    def complete_event(event_id):
        if event_id and event_id not in store.completed_event_ids:
            store.completed_event_ids.append(event_id)
        if event_id:
            store.recent_event_ids.append(event_id)
            store.recent_event_ids = store.recent_event_ids[-8:]
        if store.pending_event_id == event_id:
            store.pending_event_id = None
        if event_id in store.pending_class_event_ids:
            store.pending_class_event_ids.remove(event_id)

    def _requirement_value(requirement_id):
        if requirement_id in store.player_mastery:
            return store.player_mastery.get(requirement_id, 0)
        return get_player_stat(requirement_id)

    def event_requirements_met(event_def, activity_id=None):
        if event_def.get("once_only") and event_completed(event_def["id"]):
            return False
        if event_def.get("activity") and event_def.get("activity") != activity_id:
            return False
        if store.player_age < event_def.get("age_min", 0):
            return False
        if "age_max" in event_def and store.player_age > event_def.get("age_max"):
            return False
        for flag_id in event_def.get("required_flags", []):
            if not has_world_flag(flag_id):
                return False
        for flag_id in event_def.get("blocked_flags", []):
            if has_world_flag(flag_id):
                return False
        for req_id, req_value in event_def.get("requirements", {}).items():
            if _requirement_value(req_id) < req_value:
                return False
        return True

    def choose_next_event(activity_id=None):
        candidates = []

        for event_id in list(store.pending_class_event_ids):
            event_def = EVENT_DEFINITIONS.get(event_id)
            if event_def and event_requirements_met(event_def, activity_id):
                candidates.append(event_def)

        for event_id, event_def in EVENT_DEFINITIONS.items():
            if event_id in store.pending_class_event_ids:
                continue
            if event_def.get("type") == "class_discovery":
                continue
            if event_requirements_met(event_def, activity_id):
                if event_def.get("type") == "random" and event_def.get("weight", 0) < 20:
                    continue
                candidates.append(event_def)

        if not candidates:
            store.pending_event_id = None
            return None

        candidates.sort(key=lambda event_def: (
            EVENT_PRIORITY_ORDER.get(event_def.get("type"), 0),
            event_def.get("priority", 0),
            event_def.get("weight", 0),
        ), reverse=True)

        selected = candidates[0]
        store.pending_event_id = selected["id"]
        return selected

    def trigger_event(event_id):
        event_def = EVENT_DEFINITIONS.get(event_id)
        if not event_def:
            return None
        store.pending_event_id = event_id
        return event_def
