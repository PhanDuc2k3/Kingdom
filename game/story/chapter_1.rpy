label chapter_1_intro:
    $ story_chapter = 1
    $ set_story_stage("chapter_1_start", "bedroom", 0)

    scene black
    with fade

    centered "{size=64}CHƯƠNG I{/size}\n\n{size=42}NGƯỜI THỪA KẾ VÙNG BIÊN{/size}"

    scene bg border_day
    with fade

    narrator "Bên ngoài cửa sổ là vùng biên mà bạn vẫn chưa thật sự hiểu rõ."
    narrator "Núi, rừng, làng mạc và những con đường dài đều nằm sau bức tường dinh thự."
    narrator "Hiện tại, thế giới của bạn chỉ là dinh thự này: bài học, gia đình, những lời thì thầm, và quá trình chậm rãi để trở thành một con người mới."

    jump chapter_1_start


label chapter_1_start:
    $ set_story_stage("childhood_monthly_gameplay", "earls_mansion", 0)

    if not divine_core_id:
        call chapter_1_divine_core_ceremony

    jump chapter_1_monthly_loop


label chapter_1_divine_core_ceremony:
    scene bg divine_ceremony_hall
    with fade

    narrator "Vào tháng đầu tiên sau khi bạn tỉnh lại, nhà nguyện của dinh thự được chuẩn bị từ trước bình minh."
    narrator "Cha mẹ gọi đây là Nghi lễ Thần ban. Với mọi người, bạn chỉ là một đứa trẻ đang chờ nhận phước lành."

    scene bg divine_realm
    with dissolve
    $ set_location_bg("bg divine_realm")

    call screen divine_core_selection
    $ selected_core_id = _return
    $ give_divine_core(selected_core_id)

    narrator "Ánh sáng tan đi, nhưng có thứ gì đó vẫn còn lại dưới lồng ngực: nhỏ bé, ổn định, và thuộc về bạn."
    narrator "[get_divine_core().get('name')] đã thức tỉnh."
    $ set_location("mansion_main_hall")
    return


label chapter_1_monthly_loop:
    while not childhood_complete:
        call screen monthly_activity_screen
        $ selected_activity_id = _return

        if selected_activity_id == "__repeat_last_3" and last_activity_id:
            $ repeat_count = 0
            while repeat_count < 3 and not childhood_complete:
                $ activity_result = perform_monthly_activity(last_activity_id)
                if activity_result.get("ok"):
                    $ show_activity_background(activity_result)
                    narrator "[activity_result['summary']]"
                    narrator "[activity_result['short_line']]"
                    if activity_result.get("event_label"):
                        call expression activity_result["event_label"]
                $ repeat_count += 1
            jump chapter_1_monthly_loop

        $ activity_result = perform_monthly_activity(selected_activity_id)

        if activity_result.get("ok"):
            $ show_activity_background(activity_result)
            narrator "[activity_result['summary']]"
            narrator "[activity_result['short_line']]"
            if activity_result.get("event_label"):
                call expression activity_result["event_label"]
        else:
            narrator "[activity_result.get('message', 'Không có gì xảy ra.')]"

    jump chapter_1_age_11_final_event
