default activities_performed = {}
default last_activity_id = None
default last_activity_result = {}
default childhood_summary = {}

init python:
    MASTERY_KEYS = {
        "sword_mastery",
        "magic_mastery",
        "archery_mastery",
        "healing_mastery",
        "martial_mastery",
        "politics_mastery",
        "territory_management",
        "exploration",
    }

    def reset_activity_state():
        store.activities_performed = {}
        store.last_activity_id = None
        store.last_activity_result = {}
        store.childhood_summary = {}

    def get_available_activities():
        result = []
        for activity_id, activity in ACTIVITY_DEFINITIONS.items():
            requirements = activity.get("requirements", {})
            locked = False
            for req_id, req_value in requirements.items():
                if _requirement_value(req_id) < req_value:
                    locked = True
            if not locked:
                result.append(activity)
        return result

    def choose_activity_dialogue(activity_id):
        activity = ACTIVITY_DEFINITIONS.get(activity_id, {})
        pool = activity.get("dialogue_pool", [])
        used = store.used_activity_dialogue.get(activity_id, [])
        for line in pool:
            if line not in used:
                used.append(line)
                store.used_activity_dialogue[activity_id] = used[-len(pool):]
                return line
        if pool:
            line = pool[len(used) % len(pool)]
            used.append(line)
            store.used_activity_dialogue[activity_id] = used[-len(pool):]
            return line
        return "Tháng này trôi qua yên tĩnh."

    def apply_activity_rewards(activity):
        applied = {}
        for reward_id, amount in activity.get("rewards", {}).items():
            amount = round(amount * get_reward_multiplier(reward_id), 2)
            if reward_id in MASTERY_KEYS:
                add_player_mastery(reward_id, amount)
            else:
                add_player_stat(reward_id, amount)
            applied[reward_id] = amount

        for npc_id, rewards in activity.get("relationship_rewards", {}).items():
            for key, amount in rewards.items():
                adjust_relationship(npc_id, key, amount)
                applied["relationship:%s:%s" % (npc_id, key)] = amount

        return applied

    def find_activity_milestone_event(activity_id, before_rewards):
        activity = ACTIVITY_DEFINITIONS.get(activity_id, {})
        for threshold, event_id in sorted(activity.get("milestones", {}).items()):
            if event_completed(event_id):
                continue
            for mastery_id in MASTERY_KEYS:
                before = before_rewards.get(mastery_id, store.player_mastery.get(mastery_id, 0))
                after = store.player_mastery.get(mastery_id, 0)
                if before < threshold and after >= threshold:
                    return event_id
        return None

    def perform_monthly_activity(activity_id):
        activity = ACTIVITY_DEFINITIONS.get(activity_id)
        if not activity:
            return {
                "ok": False,
                "message": "Hoạt động không tồn tại.",
            }

        store.last_activity_id = activity_id
        store.current_location = activity.get("location", "Earl's Mansion")
        set_location_bg(activity.get("bg", "bg mansion_main_hall"))
        before_mastery = dict(store.player_mastery)
        before_count = store.activities_performed.get(activity_id, 0)
        store.activities_performed[activity_id] = before_count + 1

        rewards = apply_activity_rewards(activity)
        check_class_discovery()

        event_id = None
        if before_count == 0 and activity.get("first_time_event") and not event_completed(activity.get("first_time_event")):
            event_id = activity.get("first_time_event")

        if not event_id:
            event_id = find_activity_milestone_event(activity_id, before_mastery)

        if event_id:
            event_def = trigger_event(event_id)
        else:
            event_def = choose_next_event(activity_id)

        time_after = advance_month()

        result = {
            "ok": True,
            "activity_id": activity_id,
            "activity_name": activity.get("name", activity_id),
            "location": activity.get("location", "Dinh thự Bá tước"),
            "bg": activity.get("bg", "bg mansion_main_hall"),
            "summary": "Bạn dành tháng này để %s." % activity.get("name", activity_id).lower(),
            "short_line": choose_activity_dialogue(activity_id),
            "rewards": rewards,
            "event_id": event_def.get("id") if event_def else None,
            "event_label": event_def.get("label") if event_def else None,
            "time_after": time_after,
        }
        store.last_activity_result = result
        return result

    def build_childhood_summary():
        discoveries = []
        if has_world_flag("knows_adventurer_guild"):
            discoveries.append("Đã biết tới Hội Mạo Hiểm Giả")
        if has_world_flag("secret_hallway_found"):
            discoveries.append("Đã phát hiện hành lang bí mật")
        if has_world_flag("old_border_history_read"):
            discoveries.append("Đã đọc biên niên sử vùng biên")
        if has_world_flag("first_clean_archery_mark"):
            discoveries.append("Đã bắn trúng tâm bia đầu tiên")
        if has_world_flag("helped_injured_servant"):
            discoveries.append("Đã giúp người hầu bị thương")
        if has_world_flag("mother_shared_old_letter"):
            discoveries.append("Đã biết một phần quá khứ của mẹ")
        if has_world_flag("noticed_border_route"):
            discoveries.append("Đã nhận ra tuyến đường vùng biên")
        if has_world_flag("noticed_tax_shortage"):
            discoveries.append("Đã phát hiện khoản hụt trong sổ thuế")
        if has_world_flag("saw_refugees_rumor"):
            discoveries.append("Đã nghe tin về người tị nạn")
        if has_world_flag("found_locked_library_shelf"):
            discoveries.append("Đã tìm thấy kệ sách bị khóa")
        if has_world_flag("saw_adventurer_badge"):
            discoveries.append("Đã thấy huy hiệu mạo hiểm giả")

        store.childhood_summary = {
            "age": store.player_age,
            "month": store.player_month,
            "divine_core": get_divine_core().get("name") if get_divine_core() else "Chưa có",
            "classes": [get_class_name(class_id) for class_id in store.unlocked_classes],
            "mastery": dict(store.player_mastery),
            "stats": {
                "strength": store.player_strength,
                "dexterity": store.player_dexterity,
                "intelligence": store.player_intelligence,
                "wisdom": store.player_wisdom,
                "constitution": store.player_constitution,
                "charisma": store.player_charisma,
                "leadership": store.player_leadership,
                "knowledge": store.player_knowledge,
            },
            "relationships": dict(store.relationship_state),
            "discoveries": discoveries,
            "flags": dict(store.world_flags),
        }
        return store.childhood_summary

    def show_activity_background(activity_result):
        renpy.scene()
        renpy.show(activity_result.get("bg", "bg mansion_main_hall"))
        renpy.with_statement(dissolve)
