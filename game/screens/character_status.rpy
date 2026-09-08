style kingdom_status_panel is frame:
    background "#12100ce8"
    padding (46, 38)

style kingdom_status_title_text is text:
    font gui.interface_text_font
    size 48
    color "#f0e3c8"

style kingdom_status_text is text:
    font gui.interface_text_font
    size 28
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

screen character_status():
    modal True

    add Solid("#00000099")

    frame:
        style "kingdom_status_panel"
        xalign 0.5
        yalign 0.5
        xsize 720

        vbox:
            spacing 18

            text "[player_name]" style "kingdom_status_title_text" xalign 0.5

            text "Tuổi: [player_age]" style "kingdom_status_text"
            text "Cấp: [player_level]    Kinh nghiệm: [player_exp]" style "kingdom_status_text"
            text "Sinh lực: [player_hp]/[player_max_hp]" style "kingdom_status_text"
            text "Thể lực: [player_stamina]/[player_max_stamina]" style "kingdom_status_text"

            null height 8

            text "Sức mạnh        [player_strength]" style "kingdom_status_text"
            text "Nhanh nhẹn      [player_agility]" style "kingdom_status_text"
            text "Thể chất        [player_constitution]" style "kingdom_status_text"
            text "Trí tuệ         [player_intelligence]" style "kingdom_status_text"
            text "Nhận thức       [player_perception]" style "kingdom_status_text"
            text "Sức hút         [player_charisma]" style "kingdom_status_text"

            null height 8

            textbutton _("Tiếp tục"):
                style "kingdom_status_button"
                xalign 0.5
                action Return()
