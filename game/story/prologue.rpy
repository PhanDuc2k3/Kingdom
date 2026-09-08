label prologue_start:
    $ reset_kingdom_state()
    call screen player_name_input("Lord")
    $ player_name = _return

    scene black
    with fade

    narrator "Ta nhớ rằng mình đã chết."
    pause

    narrator "Không có ánh sáng."
    narrator "Không có tiếng nói của thần linh."
    narrator "Không có bất kỳ lời giải thích nào."
    pause

    narrator "Và rồi..."
    narrator "Ta mở mắt."

    $ set_story_stage("awakening", "bedroom", 0)

    scene bg noble_bedroom
    with fade

    narrator "Trần nhà lạ lẫm hiện ra trong tầm mắt."
    narrator "Cơ thể nặng trĩu. Bàn tay nhỏ bé. Hơi thở yếu ớt như của một đứa trẻ vừa qua cơn sốt."
    narrator "Không có điện thoại. Không có tiếng xe. Không có mùi khói bụi của thành phố."
    narrator "Chỉ có rèm nhung, mùi thuốc thảo mộc, và căn phòng rộng đến lạnh người."
    narrator "Mình... khoảng sáu tuổi."

    $ set_story_stage("mother_conversation", "bedroom", 4)

    show mother neutral at vn_center
    with dissolve

    mother "[player_name]...?"
    $ remember_dialogue("mother", player_name + "...?")

    mother "Con tỉnh rồi sao?"
    $ remember_dialogue("mother", "Con tỉnh rồi sao?")

    call mother_ai_interaction

    jump father_arrival


label mother_ai_interaction:
    while ai_turn_count < ai_turn_limit:
        $ prepare_ai_choices("mother")

        if last_ai_response.get("narration"):
            narrator "[last_ai_response['narration']]"

        if last_ai_response.get("dialogue"):
            mother "[last_ai_response['dialogue']]"
            $ remember_dialogue("mother", last_ai_response["dialogue"])

        call screen ai_choice_menu(current_ai_choices)
        $ selected_choice_id = _return
        $ choice_result = select_ai_choice(selected_choice_id)

        narrator "[choice_result['result']]"

    return


label father_arrival:
    $ set_story_stage("father_arrival", "bedroom", 1)

    show mother neutral at vn_left
    show father neutral at vn_right
    with dissolve

    father "Tình trạng của thằng bé thế nào?"
    $ remember_dialogue("father", "Tình trạng của thằng bé thế nào?")

    mother "Sốt đã hạ. Nhưng con có vẻ... khác mọi ngày."
    $ remember_dialogue("mother", "Sốt đã hạ. Nhưng con có vẻ khác mọi ngày.")

    father "[player_name]."
    father "Con còn đau ở đâu không?"
    $ remember_dialogue("father", "Con còn đau ở đâu không?")

    call father_ai_interaction

    hide mother
    hide father
    with dissolve

    jump butler_report


label father_ai_interaction:
    while ai_turn_count < ai_turn_limit:
        $ prepare_ai_choices("father")

        if last_ai_response.get("narration"):
            narrator "[last_ai_response['narration']]"

        if last_ai_response.get("dialogue"):
            father "[last_ai_response['dialogue']]"
            $ remember_dialogue("father", last_ai_response["dialogue"])

        call screen ai_choice_menu(current_ai_choices)
        $ selected_choice_id = _return
        $ choice_result = select_ai_choice(selected_choice_id)

        narrator "[choice_result['result']]"

    return


label butler_report:
    $ set_story_stage("butler_report", "bedroom", 0)

    scene bg noble_bedroom
    show butler neutral at vn_center
    with dissolve

    butler "Thưa ngài, báo cáo từ biên giới vừa được đưa tới."
    butler "Mùa đông năm nay khắc nghiệt hơn dự đoán."
    butler "Một vài ngôi làng đã bắt đầu thiếu lương thực."
    butler "Ở phía bắc, có tin về cướp đường và quái vật xuất hiện gần tuyến vận chuyển."
    butler "Ngân khố hiện không đủ dư dả để xử lý mọi việc cùng lúc."

    narrator "Những câu nói ấy không giống một cuộc trò chuyện bên giường bệnh."
    narrator "Chúng giống tiếng gõ đầu tiên của một cơn bão đang đến."

    hide butler
    with dissolve

    jump reincarnation_realization


label reincarnation_realization:
    $ set_story_stage("reincarnation_realization", "bedroom", 0)

    scene black
    with fade

    narrator "Sau khi mọi người rời đi, căn phòng cuối cùng cũng yên tĩnh."
    narrator "Mình đã chuyển sinh."
    narrator "Mình khoảng sáu tuổi."
    narrator "Mình là con trai của một Bá tước cai quản vùng biên."
    narrator "Và lãnh địa này đang gặp khó khăn."

    protagonist "Nếu đây thực sự là cuộc đời thứ hai..."
    protagonist "...thì lần này, ta sẽ tự quyết định mình sẽ sống như thế nào."

    jump name_selection


label name_selection:
    $ set_story_stage("name_selection", "bedroom", 0)

    protagonist "Tên mình là [player_name]."

    call screen character_status

    jump chapter_1_intro
