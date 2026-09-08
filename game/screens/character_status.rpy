style kingdom_status_panel is frame:
    background "#12100ce8"
    padding (46, 38)

style kingdom_status_title_text is text:
    font gui.interface_text_font
    size 48
    color "#f0e3c8"

style kingdom_status_text is text:
    font gui.interface_text_font
    size 27
    color "#efe9dd"

style kingdom_status_button is button:
    xsize 260
    ysize 58
    idle_background "#17120ce8"
    hover_background "#806832ee"
    padding (22, 8)

style kingdom_status_button_text is text:
    font gui.interface_text_font
    size 28
    color "#efe9dd"
    hover_color "#ffffff"
    xalign 0.5

init python:
    def format_status_core_name():
        core = get_divine_core()
        return core.get("name") if core else "Chưa có"

    def format_status_class_names():
        return ", ".join([get_class_name(class_id) for class_id in store.unlocked_classes]) or "Chưa có"

    def format_status_combat_mastery():
        return "Kiếm %s   Ma pháp %s   Cung %s   Chữa trị %s" % (
            store.player_mastery.get("sword_mastery", 0),
            store.player_mastery.get("magic_mastery", 0),
            store.player_mastery.get("archery_mastery", 0),
            store.player_mastery.get("healing_mastery", 0),
        )

    def format_status_life_mastery():
        return "Chính trị %s   Lãnh địa %s   Khám phá %s" % (
            store.player_mastery.get("politics_mastery", 0),
            store.player_mastery.get("territory_management", 0),
            store.player_mastery.get("exploration", 0),
        )

screen character_status(close_action=Return()):
    modal True

    add Solid("#00000099")

    frame:
        style "kingdom_status_panel"
        xalign 0.5
        yalign 0.5
        xsize 820

        vbox:
            spacing 14

            text "[player_name]" style "kingdom_status_title_text" xalign 0.5

            text "Tuổi: [player_age]    Tháng: [player_month]" style "kingdom_status_text"
            text "Cấp: [player_level]    Kinh nghiệm: [player_exp]" style "kingdom_status_text"
            text "Sinh lực: [player_hp]/[player_max_hp]    Thể lực: [player_stamina]/[player_max_stamina]" style "kingdom_status_text"

            null height 6

            text "Sức mạnh [player_strength]   Khéo léo [player_dexterity]   Thể chất [player_constitution]" style "kingdom_status_text"
            text "Trí tuệ [player_intelligence]   Minh triết [player_wisdom]   Sức hút [player_charisma]" style "kingdom_status_text"
            text "Nhận thức [player_perception]   Lãnh đạo [player_leadership]   Tri thức [player_knowledge]" style "kingdom_status_text"

            null height 6

            text "Thần Tâm: [format_status_core_name()]" style "kingdom_status_text"
            text "Chức nghiệp: [format_status_class_names()]" style "kingdom_status_text"
            text format_status_combat_mastery() style "kingdom_status_text"
            text format_status_life_mastery() style "kingdom_status_text"

            null height 8

            textbutton _("Tiếp tục"):
                style "kingdom_status_button"
                xalign 0.5
                action close_action
