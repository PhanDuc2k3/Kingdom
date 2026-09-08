default divine_core_id = None
default divine_core_traits = []

init python:
    def reset_divine_core_state():
        store.divine_core_id = None
        store.divine_core_traits = []

    def get_divine_core():
        if not store.divine_core_id:
            return None
        return DIVINE_CORE_DEFINITIONS.get(store.divine_core_id)

    def give_divine_core(core_id):
        core = DIVINE_CORE_DEFINITIONS.get(core_id)
        if not core:
            return False
        store.divine_core_id = core_id
        store.divine_core_traits = list(core.get("traits", []))
        set_world_flag("divine_core_chosen")
        return True

    def get_reward_multiplier(reward_id):
        core = get_divine_core()
        if not core:
            return 1.0
        return core.get("bonuses", {}).get(reward_id, 1.0)
