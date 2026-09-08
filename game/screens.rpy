style kingdom_menu_button is button:
    xsize 360
    ysize 62
    background "#19150fcc"
    hover_background "#7f6833dd"
    insensitive_background "#14110dcc"
    padding (28, 10)

style kingdom_menu_button_text is text:
    font gui.interface_text_font
    size 34
    color "#e8dfcf"
    hover_color "#ffffff"
    insensitive_color "#7e766a"
    xalign 0.5


style kingdom_panel is frame:
    background "#17120cd9"
    padding (40, 34)


style kingdom_label_text is text:
    font gui.interface_text_font
    size 46
    color "#f0e3c8"


style kingdom_body_text is text:
    font gui.interface_text_font
    size 28
    color "#e8dfcf"

style kingdom_pref_group is frame:
    background "#241c12cc"
    padding (24, 20)

style kingdom_pref_group_title is text:
    font gui.interface_text_font
    size 26
    color "#f0e3c8"

style kingdom_pref_button is button:
    xsize 250
    ysize 52
    idle_background "#15110bcc"
    hover_background "#806832dd"
    selected_idle_background "#9a7d3bdd"
    selected_hover_background "#b89443ee"
    padding (18, 7)

style kingdom_pref_button_text is text:
    font gui.interface_text_font
    size 24
    color "#e8dfcf"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5

style kingdom_pref_row is frame:
    background "#21190fcc"
    padding (24, 16)
    xfill True

style kingdom_pref_bar is bar:
    xsize 620
    ysize 26
    left_bar Solid("#c8a75d")
    right_bar Solid("#3a3020")
    thumb Solid("#f5e4ad")
    thumb_offset 10


style kingdom_close_button is button:
    xsize 72
    ysize 72
    background "#15120dcc"
    hover_background "#826a34dd"
    padding (0, 0)


style kingdom_close_button_text is text:
    font gui.interface_text_font
    size 34
    color "#e8dfcf"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5

style kingdom_say_window is frame:
    background "#000000a8"
    padding (90, 28)

style kingdom_say_namebox is frame:
    background "#806832ee"
    padding (26, 8)

style kingdom_say_name_text is text:
    font gui.name_text_font
    size 32
    color "#ffffff"

style kingdom_say_dialogue_text is text:
    font gui.text_font
    size 32
    color "#efe9dd"
    line_spacing 6

style kingdom_name_input_panel is frame:
    background "#0b0805e8"
    padding (48, 38)

style kingdom_name_input_title is text:
    font gui.interface_text_font
    size 40
    color "#f0e3c8"

style kingdom_name_input_field is input:
    font gui.interface_text_font
    size 34
    color "#ffffff"
    xalign 0.5

style kingdom_name_input_box is frame:
    background "#1b150dcc"
    padding (24, 14)

style kingdom_name_input_button is button:
    xsize 260
    ysize 58
    idle_background "#806832dd"
    hover_background "#b89443ee"
    padding (22, 8)

style kingdom_name_input_button_text is text:
    font gui.interface_text_font
    size 28
    color "#ffffff"
    xalign 0.5

style kingdom_file_slot is button:
    xsize 330
    ysize 245
    idle_background "#17120ce8"
    hover_background "#2d2315ee"
    selected_idle_background "#7f6833dd"
    selected_hover_background "#9f813eee"
    padding (14, 14)

style kingdom_file_slot_text is text:
    font gui.interface_text_font
    size 21
    color "#efe9dd"
    hover_color "#ffffff"

style kingdom_file_slot_label is text:
    font gui.interface_text_font
    size 24
    color "#f1dfad"
    hover_color "#ffffff"

style kingdom_file_thumb is frame:
    background "#090705cc"
    padding (0, 0)

style kingdom_file_page_button is button:
    xminimum 74
    ysize 48
    idle_background "#15110bcc"
    hover_background "#806832dd"
    selected_idle_background "#9a7d3bdd"
    selected_hover_background "#b89443ee"
    padding (16, 6)

style kingdom_file_page_button_text is text:
    font gui.interface_text_font
    size 22
    color "#e8dfcf"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5

style kingdom_file_delete_button is button:
    xsize 82
    ysize 38
    idle_background "#2a1713cc"
    hover_background "#7f2f25ee"
    padding (12, 4)

style kingdom_file_delete_button_text is text:
    font gui.interface_text_font
    size 19
    color "#e8dfcf"
    hover_color "#ffffff"
    xalign 0.5

style kingdom_file_page_text is text:
    font gui.interface_text_font
    size 25
    color "#f0e3c8"
    xalign 0.5


screen main_menu():

    tag menu

    add "images/title/title.png" xysize (config.screen_width, config.screen_height)

    add Solid("#00000066")

    frame:
        background None
        xalign 0.5
        yalign 0.72
        xsize 420

        vbox:
            spacing 14
            xalign 0.5

            textbutton _("Trò chơi mới"):
                style "kingdom_menu_button"
                action Start()

            textbutton _("Tiếp tục"):
                style "kingdom_menu_button"
                action ShowMenu("load")

            textbutton _("Cài đặt"):
                style "kingdom_menu_button"
                action ShowMenu("preferences")

            textbutton _("Thoát"):
                style "kingdom_menu_button"
                action Quit(confirm=True)

    text "v[config.version]":
        xalign 0.985
        yalign 0.975
        size 22
        color "#d4c5a8"


screen game_menu(title, scroll=None, yinitial=0.0):

    tag menu

    add "images/kingdom/kingdom_sang.png" xysize (config.screen_width, config.screen_height)

    add Solid("#00000088")

    frame:
        style "kingdom_panel"
        xalign 0.5
        yalign 0.5
        xsize 1180
        ysize 790

        vbox:
            spacing 24

            fixed:
                xfill True
                ysize 60

                text title:
                    style "kingdom_label_text"
                    yalign 0.5

            transclude

    button:
        style "kingdom_close_button"
        xpos 1438
        ypos 171
        action Function(renpy.full_restart, transition=False)

        text "X":
            style "kingdom_close_button_text"
            xalign 0.5
            yalign 0.5


screen save():

    use game_menu(_("Lưu game")):
        use file_slots(_("Lưu"))


screen load():

    use game_menu(_("Tải game")):
        use file_slots(_("Tải"))


screen file_slots(mode_text):

    vbox:
        spacing 20
        xfill True

        grid 3 2:
            spacing 20
            xalign 0.5

            for i in range(1, 7):

                button:
                    style "kingdom_file_slot"
                    action FileAction(i)

                    vbox:
                        spacing 10

                        fixed:
                            xsize 302
                            ysize 150

                            frame:
                                style "kingdom_file_thumb"
                                xysize (302, 150)
                                add FileScreenshot(i) xysize (302, 150)

                        text "[mode_text] ô [i]":
                            style "kingdom_file_slot_label"
                            xpos 12
                            ypos 10

                        text FileTime(i, format=_("%d/%m/%Y  %H:%M"), empty=_("Ô trống")):
                            style "kingdom_file_slot_text"
                            xalign 0.5

                        text FileSaveName(i):
                            style "kingdom_file_slot_text"
                            xalign 0.5
                            size 19

                    textbutton _("Xóa"):
                        style "kingdom_file_delete_button"
                        xalign 1.0
                        yalign 1.0
                        action FileDelete(i)

        vbox:
            spacing 14
            xalign 0.5

            text _("Trang lưu hiện tại"):
                style "kingdom_file_page_text"

            hbox:
                spacing 10
                xalign 0.5

                textbutton _("Trước") style "kingdom_file_page_button" action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("Tự động") style "kingdom_file_page_button" action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("Nhanh") style "kingdom_file_page_button" action FilePage("quick")

                for page in range(1, 6):
                    textbutton "[page]" style "kingdom_file_page_button" action FilePage(page)

                textbutton _("Sau") style "kingdom_file_page_button" action FilePageNext()


screen preferences():

    use game_menu(_("Cài đặt")):

        vbox:
            spacing 18
            xfill True

            hbox:
                spacing 22
                xalign 0.5

                frame:
                    style "kingdom_pref_group"
                    xsize 520

                    vbox:
                        spacing 12
                        text _("Hiển thị") style "kingdom_pref_group_title"

                        hbox:
                            spacing 12
                            textbutton _("Cửa sổ") style "kingdom_pref_button" action Preference("display", "window")
                            textbutton _("Toàn màn hình") style "kingdom_pref_button" action Preference("display", "fullscreen")

                frame:
                    style "kingdom_pref_group"
                    xsize 520

                    vbox:
                        spacing 12
                        text _("Bỏ qua") style "kingdom_pref_group_title"

                        hbox:
                            spacing 12
                            textbutton _("Đoạn chưa đọc") style "kingdom_pref_button" action Preference("skip", "toggle")
                            textbutton _("Sau lựa chọn") style "kingdom_pref_button" action Preference("after choices", "toggle")

            vbox:
                spacing 12
                xfill True

                frame:
                    style "kingdom_pref_row"
                    hbox:
                        yalign 0.5
                        spacing 28
                        text _("Tốc độ chữ") style "kingdom_body_text" xsize 330
                        bar value Preference("text speed") style "kingdom_pref_bar"

                frame:
                    style "kingdom_pref_row"
                    hbox:
                        yalign 0.5
                        spacing 28
                        text _("Tự động đọc") style "kingdom_body_text" xsize 330
                        bar value Preference("auto-forward time") style "kingdom_pref_bar"

                if config.has_music:
                    frame:
                        style "kingdom_pref_row"
                        hbox:
                            yalign 0.5
                            spacing 28
                            text _("Âm lượng nhạc") style "kingdom_body_text" xsize 330
                            bar value Preference("music volume") style "kingdom_pref_bar"

                if config.has_sound:
                    frame:
                        style "kingdom_pref_row"
                        hbox:
                            yalign 0.5
                            spacing 28
                            text _("Âm lượng hiệu ứng") style "kingdom_body_text" xsize 330
                            bar value Preference("sound volume") style "kingdom_pref_bar"

                if config.has_voice:
                    frame:
                        style "kingdom_pref_row"
                        hbox:
                            yalign 0.5
                            spacing 28
                            text _("Âm lượng giọng") style "kingdom_body_text" xsize 330
                            bar value Preference("voice volume") style "kingdom_pref_bar"


screen confirm(message, yes_action, no_action):

    modal True
    zorder 200

    add Solid("#000000aa")

    frame:
        style "kingdom_panel"

        xalign 0.5
        yalign 0.5
        xsize 720

        vbox:
            spacing 28

            text message:
                style "kingdom_body_text"
                xalign 0.5
                text_align 0.5

            hbox:
                spacing 18
                xalign 0.5

                textbutton _("Có"):
                    style "kingdom_menu_button"
                    xsize 180
                    action yes_action

                textbutton _("Không"):
                    style "kingdom_menu_button"
                    xsize 180
                    action no_action


screen say(who, what):

    frame:
        style "kingdom_say_window"
        xalign 0.5
        yalign 1.0
        xsize 1920
        ysize 250

        vbox:
            spacing 14

            if who:
                frame:
                    style "kingdom_say_namebox"

                    text who style "kingdom_say_name_text"

            text what:
                id "what"
                style "kingdom_say_dialogue_text"


screen player_name_input(default_name="Lord"):
    modal True

    default typed_name = default_name

    add Solid("#00000088")

    frame:
        style "kingdom_name_input_panel"
        xalign 0.5
        yalign 0.5
        xsize 680

        vbox:
            spacing 26
            xalign 0.5

            text "Tên của bạn là gì?" style "kingdom_name_input_title" xalign 0.5

            frame:
                style "kingdom_name_input_box"
                xsize 480
                xalign 0.5

                input:
                    style "kingdom_name_input_field"
                    value ScreenVariableInputValue("typed_name")
                    length 24
                    allow " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"

            textbutton _("Xác nhận"):
                style "kingdom_name_input_button"
                xalign 0.5
                action Return(typed_name.strip() or default_name)

    key "K_RETURN" action Return(typed_name.strip() or default_name)
