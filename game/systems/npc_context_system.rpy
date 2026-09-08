init python:
    def build_npc_context(npc_id):
        context = {
            "age": store.player_age,
            "month": store.player_month,
            "location": store.current_location,
            "divine_core": store.divine_core_id,
            "classes": list(store.unlocked_classes),
            "major_flags": {},
            "relationship": store.relationship_state.get(npc_id, {}),
            "recent_events": list(store.recent_event_ids[-5:]),
        }

        for flag_id in (
            "sneaked_out_once",
            "caught_sneaking_out",
            "mother_knows_sneaking",
            "knows_adventurer_guild",
            "heard_noble_rebellion",
        ):
            if flag_id in store.world_flags:
                context["major_flags"][flag_id] = store.world_flags[flag_id]

        return context
