style childhood_panel is frame:
    background "#14100be8"
    padding (30, 24)

style childhood_title_text is text:
    font gui.interface_text_font
    size 42
    color "#f0e3c8"

style childhood_body_text is text:
    font gui.interface_text_font
    size 24
    color "#efe9dd"
    line_spacing 4

style childhood_small_text is text:
    font gui.interface_text_font
    size 20
    color "#c8a75d"

style childhood_activity_button is button:
    xsize 390
    ysize 82
    idle_background "#17120ce8"
    hover_background "#806832ee"
    padding (18, 10)

style childhood_activity_button_text is text:
    font gui.interface_text_font
    size 23
    color "#efe9dd"
    hover_color "#ffffff"

style childhood_command_button is button:
    xsize 210
    ysize 52
    idle_background "#17120ce8"
    hover_background "#806832ee"
    padding (18, 6)

style childhood_command_button_text is text:
    font gui.interface_text_font
    size 22
    color "#efe9dd"
    hover_color "#ffffff"
    xalign 0.5

init python:
    def format_rewards(rewards):
        if not rewards:
            return ""
        parts = []
        for key, value in rewards.items():
            parts.append("%s +%s" % (key, value))
        return ", ".join(parts)

    def format_summary_mastery():
        return "Kiếm %s | Ma pháp %s | Cung %s | Chữa trị %s | Tri thức %s" % (
            store.player_mastery.get("sword_mastery", 0),
            store.player_mastery.get("magic_mastery", 0),
            store.player_mastery.get("archery_mastery", 0),
            store.player_mastery.get("healing_mastery", 0),
            store.player_knowledge,
        )

    def format_current_core_name():
        core = get_divine_core()
        return core.get("name") if core else "Chưa có"

    def format_unlocked_class_names():
        return ", ".join([get_class_name(class_id) for class_id in store.unlocked_classes]) or "Chưa có"

    def format_discoveries(discoveries):
        return ", ".join(discoveries or []) or "Chưa có"

    def format_summary_classes():
        return ", ".join(store.childhood_summary.get("classes", [])) or "Chưa có"

    def format_summary_mastery_line():
        mastery = store.childhood_summary.get("mastery", {})
        return "Kiếm %s | Ma pháp %s | Cung %s | Chữa trị %s" % (
            mastery.get("sword_mastery", 0),
            mastery.get("magic_mastery", 0),
            mastery.get("archery_mastery", 0),
            mastery.get("healing_mastery", 0),
        )

    def format_summary_stats_line():
        stats = store.childhood_summary.get("stats", {})
        return "Tri thức %s | Lãnh đạo %s" % (
            stats.get("knowledge", 0),
            stats.get("leadership", 0),
        )

screen divine_core_selection():
    modal True

    add current_location_bg xysize (config.screen_width, config.screen_height)
    add Solid("#00000099")

    frame:
        style "childhood_panel"
        xalign 0.5
        yalign 0.5
        xsize 1240

        vbox:
            spacing 18
            text "Nghi lễ Thần ban" style "childhood_title_text" xalign 0.5
            text "Trong khoảnh khắc tĩnh lặng, một lời cầu nguyện đáp lại linh hồn của bạn." style "childhood_body_text" xalign 0.5

            grid 3 2:
                spacing 14
                xalign 0.5
                for core_id, core in DIVINE_CORE_DEFINITIONS.items():
                    button:
                        style "childhood_activity_button"
                        action Return(core_id)
                        vbox:
                            spacing 4
                            text core["name"] style "childhood_activity_button_text"
                            text core["description"] style "childhood_small_text"

screen monthly_activity_screen():
    modal True

    add current_location_bg xysize (config.screen_width, config.screen_height)
    add Solid("#00000088")

    frame:
        style "childhood_panel"
        xalign 0.5
        yalign 0.5
        xsize 1420
        ysize 830

        vbox:
            spacing 16

            hbox:
                spacing 22
                xfill True
                vbox:
                    spacing 4
                    text "[get_time_label()]" style "childhood_title_text"
                    text "[current_location]" style "childhood_body_text"
                    if divine_core_id:
                        text "Thần Tâm: [format_current_core_name()]" style "childhood_small_text"
                    text format_summary_mastery() style "childhood_small_text"

                hbox:
                    spacing 10
                    xalign 1.0
                    if last_activity_id:
                        textbutton "Lặp x3":
                            style "childhood_command_button"
                            action Return("__repeat_last_3")
                    textbutton "Trạng thái":
                        style "childhood_command_button"
                        action Show("character_status", close_action=Hide("character_status"))
                    textbutton "Lưu":
                        style "childhood_command_button"
                        action ShowMenu("save")

            if last_activity_result:
                frame:
                    background "#0e0b08cc"
                    padding (16, 12)
                    xfill True
                    ysize 118
                    vbox:
                        spacing 5
                        text last_activity_result.get("summary", "") style "childhood_body_text"
                        text last_activity_result.get("short_line", "") style "childhood_small_text"
                        text format_rewards(last_activity_result.get("rewards", {})) style "childhood_small_text"

            grid 2 5:
                spacing 14
                xalign 0.5
                for activity in get_available_activities():
                    button:
                        style "childhood_activity_button"
                        action Return(activity["id"])
                        vbox:
                            spacing 4
                            text activity["name"] style "childhood_activity_button_text"
                            text activity["description"] style "childhood_small_text"

screen childhood_summary_screen():
    modal True

    add "images/kingdom/kingdom_chieu.png" xysize (config.screen_width, config.screen_height)
    add Solid("#00000099")

    frame:
        style "childhood_panel"
        xalign 0.5
        yalign 0.5
        xsize 1120

        vbox:
            spacing 14
            text "Tuổi 12" style "childhood_title_text" xalign 0.5
            text "Thần Tâm: [childhood_summary.get('divine_core')]" style "childhood_body_text"
            text "Chức nghiệp: [format_summary_classes()]" style "childhood_body_text"
            text format_summary_mastery_line() style "childhood_body_text"
            text format_summary_stats_line() style "childhood_body_text"
            text "Khám phá quan trọng: [format_discoveries(childhood_summary.get('discoveries', []))]" style "childhood_body_text"

            textbutton "Tiếp tục":
                style "childhood_command_button"
                xalign 0.5
                action Return()
