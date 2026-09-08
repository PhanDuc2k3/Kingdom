style guild_panel is frame:
    background "#14100be8"
    padding (30, 24)

style guild_title_text is text:
    font gui.interface_text_font
    size 42
    color "#f0e3c8"

style guild_body_text is text:
    font gui.interface_text_font
    size 24
    color "#efe9dd"
    line_spacing 4

style guild_small_text is text:
    font gui.interface_text_font
    size 20
    color "#c8a75d"

style guild_input_box is frame:
    background "#0b0805dd"
    padding (18, 10)

style guild_text_input is input:
    font gui.interface_text_font
    size 24
    color "#ffffff"

style guild_button is button:
    xsize 210
    ysize 50
    idle_background "#17120ce8"
    hover_background "#806832ee"
    insensitive_background "#100d09aa"
    padding (18, 6)

style guild_button_text is text:
    font gui.interface_text_font
    size 22
    color "#efe9dd"
    hover_color "#ffffff"
    insensitive_color "#766e63"
    xalign 0.5

init python:
    GUILD_DISPLAY_NAMES = {
        "common": "Thường",
        "uncommon": "Không thường",
        "rare": "Hiếm",
        "epic": "Sử thi",
        "legendary": "Huyền thoại",
        "movement_speed": "Tốc độ di chuyển",
        "attack_speed": "Tốc độ đánh",
        "dragon_damage": "Sát thương lên rồng",
        "silver_wind_stone": "Ngân Phong Thạch",
        "wind_wolf_king": "Phong Lang Vương",
        "ancient_dragon": "Cổ Long",
        "gale_forest": "Rừng Gió Xoáy",
        "border_blacksmith": "Thợ rèn vùng biên",
        "travel": "Di chuyển",
        "investigate": "Điều tra",
        "defeat_boss": "Đánh bại boss",
        "loot_material": "Thu thập nguyên liệu",
        "craft": "Chế tạo",
    }

    def guild_display_name(value):
        return GUILD_DISPLAY_NAMES.get(value, value)

    def submit_guild_chat(text):
        clean = (text or "").strip()
        if clean:
            process_guild_player_input(clean)

    def format_guild_item_line(item):
        if not item:
            return ""
        effects = []
        for effect in item.get("effects", []):
            effects.append("%s +%s%s" % (
                guild_display_name(effect.get("type", "hiệu ứng")),
                effect.get("value", ""),
                "%" if effect.get("unit") == "percent" else "",
            ))
        return "%s | %s | Công %s | %s" % (
            item.get("name", item.get("id", "")),
            guild_display_name(item.get("rarity", "common")),
            item.get("base_attack", 0),
            ", ".join(effects) or "không có hiệu ứng",
        )

    def format_guild_quest_details(quest):
        if not quest:
            return "Chưa chọn nhiệm vụ."
        lines = [quest.get("title", quest.get("id", "")), quest.get("description", "")]
        for index, step in enumerate(quest.get("steps", []), 1):
            lines.append("%d. %s: %s" % (index, guild_display_name(step.get("type")), guild_display_name(step.get("target"))))
        return "\n".join(lines)

    def format_guild_match_names(matches):
        names = []
        for match in matches or []:
            item = match.get("item", {})
            names.append(item.get("name", item.get("id", "")))
        return ", ".join(names)

screen adventure_guild():
    modal True
    default guild_input = ""
    default show_details = False

    add "images/kingdom/kingdom_sang.png" xysize (config.screen_width, config.screen_height)
    add Solid("#00000099")

    frame:
        style "guild_panel"
        xalign 0.5
        yalign 0.5
        xsize 1360
        ysize 820

        vbox:
            spacing 16

            hbox:
                spacing 18
                xfill True

                vbox:
                    spacing 6
                    xsize 310
                    text "Hội Mạo Hiểm Giả" style "guild_title_text"
                    text "Lễ tân: Mira" style "guild_body_text"
                    text "Hạng hội: [guild_rank]" style "guild_small_text"
                    null height 10
                    text "Kho vật phẩm: [len(world_item_registry)] định nghĩa" style "guild_small_text"
                    text "Nhiệm vụ đang nhận: [len(active_guild_quest_ids)]" style "guild_small_text"

                viewport:
                    xsize 970
                    ysize 485
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 10
                        for message in guild_recent_messages:
                            frame:
                                background "#21190fcc"
                                padding (14, 10)
                                xfill True
                                vbox:
                                    spacing 3
                                    text message["speaker"].title() style "guild_small_text"
                                    text message["text"] style "guild_body_text"

                        if not guild_recent_messages:
                            text "Mira đang chờ câu hỏi của ngài." style "guild_body_text"

            frame:
                style "guild_input_box"
                xfill True
                hbox:
                    spacing 14
                    input:
                        style "guild_text_input"
                        value ScreenVariableInputValue("guild_input")
                        length 160
                        xsize 1010

                    textbutton "Gửi":
                        style "guild_button"
                        action [Function(submit_guild_chat, guild_input), SetScreenVariable("guild_input", ""), SetScreenVariable("show_details", False)]

            if guild_last_result:
                $ item = guild_last_result.get("item")
                $ quest = guild_last_result.get("quest")
                $ matches = guild_last_result.get("matches", [])

                frame:
                    background "#0e0b08cc"
                    padding (18, 14)
                    xfill True
                    ysize 175

                    vbox:
                        spacing 8
                        text "Kết quả: [guild_last_result.get('status', '').upper()]" style "guild_small_text"
                        if item:
                            text format_guild_item_line(item) style "guild_body_text"
                        if quest:
                            text "Nhiệm vụ đề xuất: [quest.get('title')]" style "guild_body_text"
                        if len(matches) > 1:
                            text "Vật phẩm gần đúng: [format_guild_match_names(matches)]" style "guild_small_text"

                        hbox:
                            spacing 12
                            if quest:
                                textbutton "Nhận nhiệm vụ":
                                    style "guild_button"
                                    action Function(accept_guild_quest, quest["id"])
                                textbutton "Từ chối":
                                    style "guild_button"
                                    action Function(decline_guild_quest, quest["id"])
                                textbutton "Xem chi tiết":
                                    style "guild_button"
                                    action ToggleScreenVariable("show_details")

                if show_details and quest:
                    frame:
                        background "#21190fcc"
                        padding (18, 14)
                        xfill True
                        ysize 135
                        viewport:
                            mousewheel True
                            draggable True
                            text format_guild_quest_details(quest) style "guild_body_text"

            hbox:
                spacing 12
                xalign 1.0
                textbutton "Đóng":
                    style "guild_button"
                    action Return()

    key "K_RETURN" action [Function(submit_guild_chat, guild_input), SetScreenVariable("guild_input", ""), SetScreenVariable("show_details", False)]

label adventure_guild_demo:
    call screen adventure_guild
    return
