default guild_rank = "D"
default guild_unlocked_regions = ["gale_forest"]
default guild_known_dungeons = ["wind_wolf_den"]
default guild_known_bosses = ["wind_wolf_king", "ancient_dragon"]
default guild_known_blacksmiths = ["border_blacksmith"]

default world_item_registry = {}
default world_item_instances = {}
default guild_quests = {}
default active_guild_quest_ids = []

default guild_recent_messages = []
default guild_discussed_item_ids = []
default guild_discussed_quest_ids = []
default guild_last_intent = {}
default guild_last_search_results = []
default guild_pending_quest_id = None
default guild_pending_item_id = None
default guild_last_result = {}

init python:
    GUILD_MESSAGE_LIMIT = 12
    GUILD_MEMORY_LIMIT = 12

    def reset_adventure_guild_state():
        store.guild_rank = "D"
        store.guild_unlocked_regions = ["gale_forest"]
        store.guild_known_dungeons = ["wind_wolf_den"]
        store.guild_known_bosses = ["wind_wolf_king", "ancient_dragon"]
        store.guild_known_blacksmiths = ["border_blacksmith"]
        store.world_item_registry = {}
        store.world_item_instances = {}
        store.guild_quests = {}
        store.active_guild_quest_ids = []
        store.guild_recent_messages = []
        store.guild_discussed_item_ids = []
        store.guild_discussed_quest_ids = []
        store.guild_last_intent = {}
        store.guild_last_search_results = []
        store.guild_pending_quest_id = None
        store.guild_pending_item_id = None
        store.guild_last_result = {}

    def guild_remember_message(speaker, text):
        store.guild_recent_messages.append({
            "speaker": speaker,
            "text": text,
        })
        store.guild_recent_messages = store.guild_recent_messages[-GUILD_MESSAGE_LIMIT:]

    def guild_remember_item(item_id):
        if item_id and item_id not in store.guild_discussed_item_ids:
            store.guild_discussed_item_ids.append(item_id)
            store.guild_discussed_item_ids = store.guild_discussed_item_ids[-GUILD_MEMORY_LIMIT:]

    def guild_remember_quest(quest_id):
        if quest_id and quest_id not in store.guild_discussed_quest_ids:
            store.guild_discussed_quest_ids.append(quest_id)
            store.guild_discussed_quest_ids = store.guild_discussed_quest_ids[-GUILD_MEMORY_LIMIT:]
