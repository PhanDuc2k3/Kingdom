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
