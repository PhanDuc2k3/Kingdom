default class_states = {}
default discovered_classes = []
default unlocked_classes = []
default pending_class_event_ids = []

init python:
    def reset_class_state():
        store.class_states = {}
        store.discovered_classes = []
        store.unlocked_classes = []
        store.pending_class_event_ids = []
        for class_id, definition in CLASS_DEFINITIONS.items():
            store.class_states[class_id] = {
                "state": "locked",
                "hidden": definition.get("hidden", False),
            }

    def class_requirements_met(class_def):
        for mastery_id, required in class_def.get("requirements", {}).items():
            if store.player_mastery.get(mastery_id, 0) < required:
                return False
        for trait in class_def.get("required_traits", []):
            if trait not in store.divine_core_traits:
                return False
        return True

    def discover_class(class_id):
        if class_id not in CLASS_DEFINITIONS:
            return False
        if class_id not in store.discovered_classes:
            store.discovered_classes.append(class_id)
        store.class_states[class_id] = {
            "state": "discovered",
            "hidden": CLASS_DEFINITIONS[class_id].get("hidden", False),
        }
        return True

    def unlock_class(class_id):
        if class_id not in CLASS_DEFINITIONS:
            return False
        discover_class(class_id)
        if class_id not in store.unlocked_classes:
            store.unlocked_classes.append(class_id)
        store.class_states[class_id]["state"] = "unlocked"
        return True

    def check_class_discovery():
        new_events = []
        for class_id, class_def in CLASS_DEFINITIONS.items():
            if class_id in store.unlocked_classes:
                continue
            if not class_requirements_met(class_def):
                continue
            event_id = class_def.get("discovery_event_id")
            if event_id and event_id not in store.completed_event_ids and event_id not in store.pending_class_event_ids:
                store.pending_class_event_ids.append(event_id)
                new_events.append(event_id)
        return new_events

    def get_class_name(class_id):
        return CLASS_DEFINITIONS.get(class_id, {}).get("name", class_id)
