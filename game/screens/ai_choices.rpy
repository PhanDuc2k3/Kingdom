style kingdom_choice_button is button:
    xsize 1180
    background "#17120ce8"
    hover_background "#806832ee"
    padding (24, 18)

style kingdom_choice_button_text is text:
    font gui.interface_text_font
    size 28
    color "#efe9dd"
    hover_color "#ffffff"

style kingdom_choice_category_text is text:
    font gui.interface_text_font
    size 22
    color "#c8a75d"

screen ai_choice_menu(choices):
    modal True

    frame:
        background "#080604cc"
        xalign 0.5
        yalign 0.78
        padding (28, 24)

        vbox:
            spacing 12

            for choice in choices:
                button:
                    style "kingdom_choice_button"
                    action Return(choice["id"])

                    vbox:
                        spacing 4
                        text "[get_choice_category_label(choice['category'])]" style "kingdom_choice_category_text"
                        text choice["text"] style "kingdom_choice_button_text"
