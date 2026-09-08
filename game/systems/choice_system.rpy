init python:
    CATEGORY_EXP_MAP = {
        "intelligence": "intelligence",
        "observation": "perception",
        "social": "charisma",
        "deception": "deception",
        "kindness": "charisma",
        "bold": "strength",
        "noble": "charisma",
        "combat": "combat",
        "survival": "survival",
    }

    def get_choice_by_id(choice_id):
        for choice in store.current_ai_choices:
            if choice.get("id") == choice_id:
                return choice
        return None

    def apply_choice_effect(choice):
        if not choice:
            store.last_choice_result = "Lựa chọn không hợp lệ. Câu chuyện tiếp tục theo hướng an toàn."
            return store.last_choice_result

        category = choice.get("category")
        stat_key = CATEGORY_EXP_MAP.get(category)

        if stat_key:
            store.player_stat_exp[stat_key] = store.player_stat_exp.get(stat_key, 0) + 5
            store.player_exp += 5

        if store.story_stage == "mother_conversation":
            if category == "kindness":
                store.mother_affection += 2
                store.relationship_state["mother"]["affection"] = store.mother_affection
                result = "Sự dịu dàng trong giọng nói khiến mẹ cậu yên lòng hơn."
            elif category == "deception":
                store.mother_suspicion += 2
                store.relationship_state["mother"]["suspicion"] = store.mother_suspicion
                result = "Mẹ cậu thoáng khựng lại, như thể có điều gì đó không khớp."
            elif category == "intelligence":
                result = "Cậu giữ giọng bình tĩnh, cố gom từng mảnh thông tin rời rạc."
            elif category == "observation":
                result = "Cậu im lặng ghi nhớ từng chi tiết trong căn phòng xa lạ."
            else:
                result = "Mẹ cậu nhìn cậu thêm một lúc, rồi nhẹ nhàng gật đầu."

        elif store.story_stage == "father_arrival":
            if category == "noble":
                store.father_affection += 1
                store.relationship_state["father"]["affection"] = store.father_affection
                result = "Cha cậu khẽ gật đầu trước vẻ bình tĩnh hiếm thấy ấy."
            elif category == "observation":
                result = "Cậu nhận ra nỗi lo bị giấu sau vẻ nghiêm nghị của ông."
            elif category == "intelligence":
                result = "Cha cậu trả lời ngắn gọn, nhưng ánh mắt nghiêm túc hơn."
            else:
                result = "Cha cậu quan sát cậu trong im lặng."

        else:
            result = "Lựa chọn được ghi nhận."

        store.last_choice_result = result
        return result

    def select_ai_choice(choice_id):
        choice = get_choice_by_id(choice_id)
        result = apply_choice_effect(choice)
        limit_reached = advance_ai_turn()
        return {
            "choice": choice,
            "result": result,
            "limit_reached": limit_reached,
        }
