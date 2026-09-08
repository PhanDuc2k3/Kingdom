default story_chapter = 0
default story_stage = "awakening"
default current_location = "bedroom"
default current_location_bg = "bg main_bedroom_day"

default ai_turn_count = 0
default ai_turn_limit = 0

default recent_dialogue = []
default last_choice_result = ""

init python:
    def reset_story_state():
        store.story_chapter = 0
        store.story_stage = "awakening"
        store.current_location = "bedroom"
        store.current_location_bg = "bg main_bedroom_day"
        store.ai_turn_count = 0
        store.ai_turn_limit = 0
        store.recent_dialogue = []
        store.last_choice_result = ""

    def reset_kingdom_state():
        reset_player_state()
        reset_relationship_state()
        reset_story_state()
        reset_time_state()
        reset_event_state()
        reset_divine_core_state()
        reset_class_state()
        reset_activity_state()
        reset_adventure_guild_state()

    def set_story_stage(stage, location=None, turn_limit=0):
        store.story_stage = stage
        if location is not None:
            store.current_location = location
        store.ai_turn_count = 0
        store.ai_turn_limit = turn_limit

    def set_location_bg(bg_name):
        store.current_location_bg = bg_name or "bg mansion_main_hall"
        return store.current_location_bg

    def advance_ai_turn():
        store.ai_turn_count += 1
        return store.ai_turn_count >= store.ai_turn_limit

    def remember_dialogue(speaker, text):
        store.recent_dialogue.append({
            "speaker": speaker,
            "text": text,
            "stage": store.story_stage,
        })
        store.recent_dialogue = store.recent_dialogue[-8:]
