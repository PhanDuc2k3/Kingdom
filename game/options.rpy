define config.name = _("Kingdom")
define config.version = "0.1.0"

define config.window_title = _("Kingdom")
define config.save_directory = "Kingdom-1700000000"

define config.screen_width = 1920
define config.screen_height = 1080

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = None

define config.has_autosave = False
define config.autosave_on_choice = False
define config.autosave_on_input = False
define config.autosave_on_quit = False
define config.save_on_mobile_background = False
define config.has_quicksave = False

define build.name = "Kingdom"
define build.directory_name = "Kingdom"
define build.executable_name = "Kingdom"

init python:
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("game/**.rpy", "archive")
    build.classify("game/**.png", "archive")
