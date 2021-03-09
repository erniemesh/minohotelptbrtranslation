######################################################################
#                        CHARACTER DEFINITIONS
######################################################################

define asterion = Character("Astério",
                            window_background= "textBoxAsterion")
define luke = Character("Luke",
                            color="#ebeff2",
                            window_background= "textBoxLuke")

define you = Character("Você")

define old = Character ("Velho")

define thing = Character("???",
                            window_background= "textBoxAsterion")

define argos = Character("Argos",
                            color="#8e9b9e",
                            window_background= "textBoxArgos")
define kota = Character("Kota",
                            color="#5058bc",
                            window_background= "textBoxKota")

define contract = Character(
                            what_color="#1c1d29",
                            window_background= "textBoxContract")

define cobalts = Character("Cobaltos",
                            color="#7a2718",
                            window_background= "textBoxCobalts")

define cobaltq = Character("???",
                            color="#7a2718",
                            window_background= "textBoxCobalts")

define gruggy = Character("Gruggy",
                            color="#7a2718",
                            window_background= "textBoxCobalts")

define p = Character("P",
                            color="#2e933a",
                            window_background= "textBoxP")

define pq = Character("???",
                            color="#2e933a",
                            window_background= "textBoxP")

define robert = Character("Roberto",
                            color="#806bba",
                            window_background= "textBoxRobert")

define storm = Character("Tempestade",
                            color="#525252",
                            window_background= "textBoxStorm")

define stormq = Character("???",
                            color="#525252",
                            window_background= "textBoxStorm")

define wolfdad = Character("Lobo",
                            color="#525252",
                            window_background= "textBoxStorm")

define khenbish = Character("Khenbish",
                            color="#72414F",
                            window_background= "textBoxKhenbish")

define androgeos = Character("Androgeu",
                            color="#8DDCBC",
                            window_background= "textBoxAndrogeos")


######################################################################
#                           CUSTOM TEXTBOXES
######################################################################

image textBoxAsterion:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Asterion.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Asterion.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxLuke:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Luke.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Luke.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxArgos:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Argos.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Argos.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxKota:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Kota.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Kota.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxOnsen:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Onsen.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Onsen.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxCobalts:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Cobalts.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Cobalts.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxRobert:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Robert.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Robert.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxKhenbish:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Khenbish.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Khenbish.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxStorm:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Storm.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Storm.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxP:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_P.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_P.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxAndrogeos:
    contains:
        "gui/customtextboxes/textBox.png"
        xpos 0.0
        ypos -15
    contains:
        "gui/customtextboxes/scroll_Androgeos.png"
        xpos 0.0
        ypos -9
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/customtextboxes/scroll_Androgeos.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 157
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image textBoxContract:
    contains:
        "gui/customtextboxes/contract.png"
        xalign 0.5
        yalign 1.0
