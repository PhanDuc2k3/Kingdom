testsuite global:
    before testcase:
        $ _test.transition_timeout = 0.05
        $ _test.timeout = 5.0

        if not screen "main_menu":
            run ShowMenu("main_menu")

    teardown:
        exit

testcase settings_x_returns_to_title:
    assert screen "main_menu"
    click "Cài đặt"
    advance until screen "preferences"
    assert screen "preferences"
    click pos (1474, 207)
    pause 0.2
    assert screen "main_menu"

testcase load_screen_opens:
    assert screen "main_menu"

    run ShowMenu("load")
    advance until screen "load"
    assert screen "load"
    click pos (1474, 207)
    pause 0.2
    assert screen "main_menu"

testcase prologue_mock_ai_flow:
    assert screen "main_menu"
    click "Trò chơi mới"
    keysym "K_RETURN"

    advance until screen "ai_choice_menu"
    assert eval (story_stage == "mother_conversation")
    assert eval (len(current_ai_choices) >= 3)

    click pos (960, 760)
    advance until screen "ai_choice_menu"
    click pos (960, 760)
    advance until screen "ai_choice_menu"
    click pos (960, 760)
    advance until screen "ai_choice_menu"
    click pos (960, 760)

    advance until screen "ai_choice_menu"
    assert eval (story_stage == "father_arrival")
    assert eval (player_exp >= 20)
    assert eval (sum(player_stat_exp.values()) >= 20)

    click pos (960, 760)
    advance until eval story_stage == "name_selection"

    advance until screen "character_status"
    assert eval (player_name == "Lord")
    assert eval (player_age == 6)
    assert eval (player_level == 1)

    click "Tiếp tục"
    advance until eval story_stage == "chapter_1_start"

testcase ai_validation_fallback:
    $ bad_response = {"story_stage": "forced_bad_stage", "choices": [{"id": "", "text": "", "category": "invalid", "hp": 999}]}
    $ checked_choices = validate_ai_choices(bad_response)
    assert eval (ai_service_failed)
    assert eval (len(checked_choices) == 4)
    assert eval (checked_choices[0]["category"] in CHOICE_CATEGORIES)

testcase guild_creates_item_when_registry_empty:
    $ reset_kingdom_state()
    $ result = process_guild_player_input("Toi muon kiem giup chay nhanh.")
    assert eval (result["status"] == "available")
    assert eval ("windwalker_sword" in world_item_registry)
    assert eval (result["quest"]["id"] in guild_quests)
    assert eval (guild_discussed_item_ids[-1] == "windwalker_sword")

testcase guild_reuses_item_for_light_sword_query:
    $ reset_kingdom_state()
    $ first = process_guild_player_input("Toi muon kiem giup chay nhanh.")
    $ before_count = len(world_item_registry)
    $ second = process_guild_player_input("Trong hoi co kiem nhe khong?")
    assert eval (second["kind"] == "existing_item")
    assert eval (second["item"]["id"] == "windwalker_sword")
    assert eval (len(second["matches"]) <= 3)
    assert eval (len(world_item_registry) == before_count)

testcase guild_rejects_overpowered_item:
    $ reset_kingdom_state()
    $ overpowered = {"id": "world_breaker", "name": "World Breaker", "category": "weapon", "weapon_type": "sword", "rarity": "common", "base_attack": 999, "tags": ["destruction"], "effects": [{"type": "movement_speed", "value": 99, "unit": "percent"}], "unique": False, "max_instances": None}
    $ validation = validate_item_proposal(overpowered)
    assert eval (not validation["accepted"])

testcase guild_rejects_ai_drop_rate_in_proposal:
    $ reset_kingdom_state()
    $ illegal = {"id": "bad_legendary", "name": "Bad Legendary", "category": "weapon", "weapon_type": "sword", "rarity": "legendary", "base_attack": 50, "tags": ["dragon"], "effects": [], "acquisition": {"type": "drop", "source": "ancient_dragon", "drop_rate": 0.001}, "unique": True, "max_instances": 1}
    $ validation = validate_item_proposal(illegal)
    assert eval (not validation["accepted"])
    assert eval (validation["reason"] == "forbidden_ai_acquisition_field")

testcase guild_impossible_world_destroying_sword:
    $ reset_kingdom_state()
    $ result = process_guild_player_input("Co kiem pha huy the gioi khong?")
    assert eval (result["status"] == "impossible")
    assert eval (len(world_item_registry) == 0)

testcase guild_legendary_drop_is_engine_roll_only:
    $ reset_kingdom_state()
    $ result = process_guild_player_input("Co kiem chuyen diet rong khong?")
    assert eval ("dragon_slayer" in world_item_registry)
    assert eval (result["status"] == "locked")
    assert eval (result.get("quest") is None)
    assert eval (len(world_item_instances) == 0)
    $ table = get_loot_table("ancient_dragon")
    assert eval (any(entry["id"] == "dragon_slayer" and entry["chance"] == 0.001 for entry in table))

testcase guild_unique_item_allows_only_one_instance:
    $ reset_kingdom_state()
    $ result = process_guild_player_input("Co kiem chuyen diet rong khong?")
    $ first_instance = create_item_instance("dragon_slayer", "npc")
    $ second_instance = create_item_instance("dragon_slayer", "player")
    assert eval (first_instance is not None)
    assert eval (second_instance is None)

testcase guild_quest_created_from_approved_item:
    $ reset_kingdom_state()
    $ result = process_guild_player_input("Toi can kiem tang toc do chay.")
    assert eval (result["quest"]["item_definition_id"] == "windwalker_sword")
    assert eval (len(result["quest"]["steps"]) >= 5)

testcase guild_state_roundtrip_data_is_plain_saveable:
    $ reset_kingdom_state()
    $ result = process_guild_player_input("Toi muon kiem giup chay nhanh.")
    $ instance = create_item_instance("windwalker_sword", "player")
    $ snapshot = {"registry": dict(world_item_registry), "quests": dict(guild_quests), "discussed": list(guild_discussed_item_ids), "instances": dict(world_item_instances)}
    assert eval ("windwalker_sword" in snapshot["registry"])
    assert eval (result["quest"]["id"] in snapshot["quests"])
    assert eval ("windwalker_sword" in snapshot["discussed"])
    assert eval (instance["definition_id"] == "windwalker_sword")
