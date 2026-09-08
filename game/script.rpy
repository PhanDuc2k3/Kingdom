define narrator = Character(None)
define mother = Character("Mẹ")
define father = Character("Cha")
define butler = Character("Quản gia")
define protagonist = Character("[player_name]", dynamic=True)

image mother neutral = "images/char/mother/mother.png"
image father neutral = "images/char/father/father.png"
image butler neutral = "images/char/generate/generate.png"
image bg noble_bedroom = Transform("images/room/bedroom.png", xysize=(1920, 1080))
image bg border_day = "images/kingdom/kingdom_sang.png"

transform vn_center:
    zoom 0.32
    xalign 0.05
    yanchor 1.0
    ypos 830

transform vn_left:
    zoom 0.32
    xalign 0.0
    yanchor 1.0
    ypos 830

transform vn_right:
    zoom 0.32
    xalign 0.19
    yanchor 1.0
    ypos 830

label start:
    call prologue_start
    return
