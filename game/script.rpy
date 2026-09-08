define narrator = Character(None)
define mother = Character("Mẹ")
define father = Character("Cha")
define butler = Character("Quản gia")
define protagonist = Character("[player_name]", dynamic=True)

image mother neutral = "images/char/mother/mother.png"
image father neutral = "images/char/father/father.png"
image butler neutral = "images/char/generate/generate.png"
image bg main_bedroom_day = Transform("images/room/main_bedroom.png", xysize=(1920, 1080))
image bg mansion_main_hall = Transform("images/room/mansion_main_hall.png", xysize=(1920, 1080))
image bg mansion_corridor = Transform("images/room/mansion_corridor.png", xysize=(1920, 1080))
image bg mansion_library = Transform("images/room/mansion_library.png", xysize=(1920, 1080))
image bg training_courtyard = Transform("images/room/training_courtyard.png", xysize=(1920, 1080))
image bg magic_study_room = Transform("images/room/magic_study_room.png", xysize=(1920, 1080))
image bg archery_range = Transform("images/room/archery_range.png", xysize=(1920, 1080))
image bg father_study = Transform("images/room/father_study.png", xysize=(1920, 1080))
image bg mother_room = Transform("images/room/mother_room.png", xysize=(1920, 1080))
image bg mansion_garden = Transform("images/room/mansion_garden  .png", xysize=(1920, 1080))
image bg family_dining_room = Transform("images/room/family_dining_room.png", xysize=(1920, 1080))
image bg mansion_exterior_day = Transform("images/room/mansion_exterior_day.png", xysize=(1920, 1080))
image bg divine_ceremony_hall = Transform("images/room/divine_ceremony_hall.png", xysize=(1920, 1080))
image bg divine_realm = Transform("images/room/divine_realm.png", xysize=(1920, 1080))
image bg mansion_back_gate_night = Transform("images/room/mansion_back_gate_night.png", xysize=(1920, 1080))
image bg border_town_street = Transform("images/room/border_town_street.png", xysize=(1920, 1080))
image bg border_town_market = Transform("images/room/border_town_market.png", xysize=(1920, 1080))
image bg war_room = Transform("images/room/war_room.png", xysize=(1920, 1080))
image bg noble_bedroom = Transform("images/room/main_bedroom.png", xysize=(1920, 1080))
image bg border_day = Transform("images/room/mansion_exterior_day.png", xysize=(1920, 1080))

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
