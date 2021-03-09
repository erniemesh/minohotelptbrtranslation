##############################################################################
#                                 UI COLORS
##############################################################################

init python:
    UIColorOrange =     '#e55921'
    if renpy.variant("android"):
        UIColorDisabled =   '#2d559c'
    else:
        UIColorDisabled =   '#203a68'
    UIColorPink =       '#c74c9e'
    UIColorDanger =     '#a12525'
    UIColorContract ='#1c1b24'
    UIColorArts =       '#ec4f37'
    UIColorMath =       '#a737ec'
    UIColorTech =       '#3776ec'
    UIColorLeader =     '#eccb37'
    UIColorHumanities = '#61ec37'
    UIColorSpeedrunner ='#919191'

    style.vagene = Style(style.button_text)
    style.vagene.color = UIColorOrange
    style.vagene.hover_color = UIColorOrange
    style.vagene.selected_color = UIColorOrange


##############################################################################
#                               INVENTORY SCREEN
##############################################################################

image scrollsInventory:
    contains:
        "gui/inventory/scroll.png"
        xpos 0.0  ypos 10
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 240
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos 0.0 ypos 570
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 688
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image scrollsTeam:
    contains:
        "gui/inventory/scroll.png"
        xpos 0.0 ypos 10
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 155
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos 0.0 ypos 325
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 688
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

#Displays a small description of the selected character

default mX=0
default mY=0

screen menu_tooltip(title, description=''):
    #recieves a tuple with title and description. If description is "none", it won't be displayed
    $ mX,mY = renpy.get_mouse_pos()

    frame:
        xpadding 10 ypadding 5 xmaximum 400
        if mY>500:
            ypos mY-60
        else:
            ypos mY+40
        if mX>880:
            xpos 880
        else:
            xpos mX
        vbox:
            text "[title]"
            if description != '':
                text "{size=-2}{color=[UIColorOrange]}[description]"


screen inventory():
    tag menu
    #display BG
    add "gui/inventory/inventory_background.png"

    #background icon
    vbox xminimum 150 yalign 0.92 xalign 0.0:
        if player_background != "":
            hbox xalign 0.5 spacing 5 yalign 0.5:
                image "gui/inventory/icons/MC_" + player_background + ".png" xalign 0.2 yalign 0.5
                if player_background == "arts":
                    $myText = "{size=-1}{color=[UIColorArts]}Artes{/color}{/size}"
                if player_background == "math":
                    $myText = "{size=-1}{color=[UIColorMath]}Matemática{/color}{/size}"
                if player_background == "tech":
                    $myText = "{size=-1}{color=[UIColorTech]}Tecnologia{/color}{/size}"
                if player_background == "leader":
                    $myText = "{size=-2}{color=[UIColorLeader]}Líder{/color}{/size}"
                if player_background == "humanities":
                    $myText = "{size=-3}{color=[UIColorHumanities]}Humanas{/color}{/size}"
                if player_background == "speedrunner":
                    $myText = "{size=-3}{color=[UIColorSpeedrunner]}Speedrunner{/color}{/size}"
                text myText xalign 0.6 yalign 0.5

    add "scrollsInventory"

    #RD statbox
    if UI_permissions['rd']:
        vbox xpos 70 ypos 400 xminimum 300 yminimum 120 spacing 4:
            $rd_stats = calculate_rd_team_stats()
            $relationship_bonus = relationships.get_relationships_with_guests(guests.get_rd_team().names()).sum_bonus()
            $stat_list = ['Contract', 'Tech', 'Fragment'] if UI_permissions['fragments'] else ['Contract', 'Tech']
            for stat in stat_list:
                hbox spacing 8:
                    $stat_color = UIColorPink if relationship_bonus.get_value(stat) != 0 else UIColorOrange
                    $stat_value = rd_stats.get_value(stat)
                    textbutton "{color=[stat_color]}[stat]:{/color}":
                        style "vagene"
                        action Show("menu_tooltip", title=stat, description=preset_stat_descriptions[stat])
                        hovered Show("menu_tooltip", title=stat, description=preset_stat_descriptions[stat])
                        unhovered Hide("menu_tooltip")
                    text str(stat_value)


    #EX statbox
    if UI_permissions['exploration']:
        $exspace = [1,382] if UI_permissions['fragments'] else [4,400]
        vbox xpos 490 ypos exspace[1] xminimum 300 yminimum 120 spacing exspace[0]:
            $ex_stats = calculate_exploration_team_stats()
            $relationship_bonus = relationships.get_relationships_with_guests(guests.get_exploration_team().names()).sum_bonus()
            $stat_list = ['Memento', 'Artifact', 'Surveying', 'Danger', 'Fragment'] if UI_permissions['fragments'] else ['Memento', 'Artifact', 'Surveying', 'Danger']
            for stat in stat_list:
                hbox spacing 8:
                    $stat_color = UIColorPink if relationship_bonus.get_value(stat) != 0 else UIColorOrange
                    $stat_value = ex_stats.get_value(stat)
                    textbutton "{color=[stat_color]}[stat]:{/color}":
                        style "vagene"
                        action Show("menu_tooltip", title=stat, description=preset_stat_descriptions[stat])
                        hovered Show("menu_tooltip", title=stat, description=preset_stat_descriptions[stat])
                        unhovered Hide("menu_tooltip")
                    text str(stat_value)


    #Raw materials display
        hbox xpos 645 ypos 435:
            textbutton "{color=[UIColorOrange]}Matérias Primas: {/color}":
                style "vagene"
                action Show("menu_tooltip", title="Matérias Primas", description="Materiais valiosos que o hotel não consegue gerar.")
                hovered Show("menu_tooltip", title="Matérias Primas", description="Materiais valiosos que o hotel não consegue gerar.")
                unhovered Hide("menu_tooltip")
            text str(inventory.raw_materials)

    #Text displaying subscreen titles
    vbox xpos 50 ypos 35:
        if UI_permissions['guests']:
            text "{color=[UIColorOrange]}Hóspedes{/color}"
        else:
            text "{color=[UIColorOrange]}   ???{/color}"

    vbox xpos 170 ypos 270:
        if UI_permissions['rd']:
            text "{color=[UIColorOrange]}Equipe de P&D{/color}"
        else:
            text "{color=[UIColorOrange]}       ???{/color}"

    vbox xpos 580 ypos 270:
        if UI_permissions['exploration']:
            text "{color=[UIColorOrange]}Exploração{/color}"
        else:
            text "{color=[UIColorOrange]}       ???{/color}"

    vbox xpos 1030 ypos 270:
        if UI_permissions['items']:
            text "{color=[UIColorOrange]}Itens{/color}"
        else:
            text "{color=[UIColorOrange]}  ???{/color}"

    vbox xpos 170 ypos 590:
        if UI_permissions['fragments']:
            text "{color=[UIColorOrange]}Fragmentos Divinos{/color}"
        else:
            text "{color=[UIColorOrange]}            ???{/color}"

    #Guest Icons
    if UI_permissions['guests']:
        vbox xpos 70 ypos 70:
            hbox spacing 30:
                for guest_name in preset_guest_names:
                    $icon_filename = get_guest_inventory_filename(guest_name, size = 'normal')
                    $tooltip_info = get_guest_tooltip(guests, persistent.known_guests, guest_name, preset_guest_descriptions)
                    imagebutton idle icon_filename:
                        action Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        hovered Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        unhovered Hide("menu_tooltip")

    #RD icons
    if UI_permissions['rd']:
        vbox xpos 70 ypos 310 xminimum 310:
            hbox xalign 0.5 spacing 50:
                for member in guests.get_rd_team().names():
                    $icon_filename = get_guest_inventory_filename(member, size = 'normal')
                    $tooltip_info = get_guest_tooltip(guests, persistent.known_guests, member, preset_guest_descriptions)
                    imagebutton idle icon_filename:
                        action Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        hovered Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        unhovered Hide("menu_tooltip")

    #Exploration icons
    if UI_permissions['exploration']:
        vbox xpos 490 ypos 310 xminimum 310:
            hbox xalign 0.5 spacing 50:
                for member in guests.get_exploration_team().names():
                    $icon_filename = get_guest_inventory_filename(member, size = 'normal')
                    $tooltip_info = get_guest_tooltip(guests, persistent.known_guests, member, preset_guest_descriptions)
                    imagebutton idle icon_filename:
                        action Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        hovered Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        unhovered Hide("menu_tooltip")

    #Item icons
    if UI_permissions['items']:
        vbox xpos 900 ypos 320 xminimum 310:
            hbox xalign 0.5 spacing 40:
                for item in inventory.items:
                    imagebutton idle "gui/inventory/icons/item_" + item + ".png":
                        action Show("menu_tooltip", title=item, description=preset_item_descriptions[item])
                        hovered Show("menu_tooltip", title=item, description=preset_item_descriptions[item])
                        unhovered Hide("menu_tooltip")

    #FRAGMENT ICONS
    if UI_permissions['fragments']:
        vbox ypos 615 xpos 220:
            hbox spacing 20:
                for i in inventory.fragList:
                    imagebutton idle inventory.getFragmentFilename(i.name, size = 'normal'):
                        action Show("invDescription", myTup=inventory.makeDesc("fragment",fragDict[i.name]))
                        hovered Show("invDescription", myTup=inventory.makeDesc("fragment",fragDict[i.name]))
                        unhovered Hide("invDescription")

    #return button
    hbox xminimum 150 xalign 1.0 yalign 1.0 yminimum 120:
        vbox yminimum 80 xalign 0.5:
            frame xpadding 10 ypadding 10 yalign 0.5:
                textbutton "{size=+4}Voltar" action Return()


##############################################################################
#                               TITLE SCREEN
##############################################################################

image LtoRscroll1:
    "scroll3"
    xpos 0.0
    ypos -480
    linear 60.0 xpos -1.0
    repeat

image LtoRscroll2:
    "scroll1"
    xpos 0.0
    ypos -160
    linear 60.0 xpos -1.0
    repeat

image RtoLscroll1:
    "scroll2"
    xpos -1
    ypos -320
    linear 60.0 xpos 0.0
    repeat

image RtoLscroll2:
    "scroll4"
    xpos -1
    ypos 0
    linear 60.0 xpos 0.0
    repeat

##############################################################################
#                             CHAPTER TRANSITION
##############################################################################

image scrollsChapter:
    contains:
        "scroll1.png"
        xpos 0.0 ypos 100
        linear 30.0 xpos -1.0
        repeat
    contains:
        "scroll2.png"
        xpos -1 ypos 500
        linear 30.0 xpos 0.0
        repeat

image scrollsDark:
    contains:
        "scroll5dark.png"
        xpos 0.0 ypos 100
        linear 30.0 xpos -1.0
        repeat
    contains:
        "scroll2dark.png"
        xpos -1 ypos 500
        linear 30.0 xpos 0.0
        repeat

image scrollsHinterlands:
    contains:
        "scrollStorm.png"
        #"scrollStorm"
        xpos 0.0 ypos 100
        linear 30.0 xpos -1.0
        repeat
    contains:
        "scrollP.png"
        xpos -1 ypos 500
        linear 30.0 xpos 0.0
        repeat

transform my_fading:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen ChapterTransition(title, subtitle, altTitle='No'):

    add "bg black"

    if altTitle == 'Hades':
        add "scrollsDark":
            at my_fading
    elif altTitle == 'Hinterlands':
        add "scrollsHinterlands":
            at my_fading
    else:
        add "scrollsChapter":
            at my_fading

    text "[title]" xalign 0.5 yalign 0.40 size 48:
        at my_fading

    $titleColor= UIColorOrange
    if altTitle == 'Hades':
        $titleColor = UIColorDisabled
    elif altTitle == 'Hinterlands':
        $titleColor = "#2e933a"

    text "{i}{color=[titleColor]}[subtitle]{/color}{/i}" xalign 0.5 yalign 0.58 size 35:
        at my_fading

    imagebutton:
        idle "null.png"
        action Return()

    if renpy.get_skipping()!=None:
        timer 0.4 action Return()
    timer 5.0 action Return()


##############################################################################
#                                   POEM READER
##############################################################################


screen Poem(Stanzas):
    default stanza_progress = 0
    default line_progress = 0
    vbox xalign 0.5 yalign 1.0 xminimum 700:
        vbox yminimum 550 yalign 0.0:
            vbox:
                for line in Stanzas[stanza_progress][0:line_progress+1]:
                    text line:
                        #size gui.text_size + persistent.text_font_size
                        if persistent.dyslexic_mode:
                            font "fonts/OpenDyslexic.otf"
                            size gui.text_size -2
                    text ""
    imagebutton:
        idle "null.png"
        if stanza_progress == len(Stanzas)-1 and line_progress == len(Stanzas[stanza_progress])-1:
            action Return()
        elif line_progress == len(Stanzas[stanza_progress])-1:
            action [SetLocalVariable("stanza_progress", stanza_progress+1), SetLocalVariable("line_progress", 0)]
        else:
            action SetLocalVariable("line_progress", line_progress+1)

    if renpy.get_skipping()!=None:
        timer 0.4 action Return()

##############################################################################
#                                SKIP BUTTON
##############################################################################

screen SkipButton(labelToJump, skipText="Pular"):
    frame xalign 0.97 yalign 0.68 xpadding 5 ypadding 5 :
        if renpy.variant("android"):
            textbutton "{size=+10}[skipText]" action Confirm("Pular esta cena?", Jump(labelToJump))
        else:
            textbutton "{size=+4}[skipText]" action Confirm("Pular esta cena?", Jump(labelToJump))


##############################################################################
#                              CE PRESS BUTTON
##############################################################################

#The press button used in cross examinations

screen CEPressScreen(failLabel, pressText="Pressione!"):
    $Wide = 1 if renpy.variant("android") else 5
    image "gui/CEQuestions.png" xalign 0.05 yalign 0.35 alpha 0.8
    vbox xalign 0.05 xminimum 340 yminimum 400 yalign 0.35:
        vbox xalign 0.5 yalign 0.5 spacing Wide*4:
            vbox xalign 0.2 yalign 0.5 spacing Wide:
                for i, j in enumerate(PressQuestions):
                    $i = i+1
                    hbox spacing 20:
                        if j == 'c':
                            text "{color=[UIColorOrange]}Afirmação [i]:" yalign 0.5
                        else:
                            text "{color=[UIColorContract]}Afirmação [i]:" yalign 0.5
                        if j == 'q':
                            image "gui/D_ContractBlock_q.png"
                        elif j == 'y':
                            image "gui/D_ContractBlock_hover.png"
                        else:
                            image "gui/D_ContractBlock_idle.png"
            text "{color=[UIColorContract]}Perguntas Restantes: [PressTries]" yalign 0.9
    if showCEButton:
        frame xalign 0.97 yalign 0.65 xpadding 5 ypadding 5 :
            if PressTries == 0:
                if renpy.variant("android"):
                    textbutton "{size=+10}[pressText]" action Jump(failLabel)
                else:
                    textbutton "{size=+4}[pressText]" action Jump(failLabel)
            else:
                if renpy.variant("android"):
                    textbutton "{size=+10}[pressText]" action Jump(PressLabel)
                else:
                    textbutton "{size=+4}[pressText]" action Jump(PressLabel)


##############################################################################
#                              GUEST PICKER
##############################################################################

screen GuestPicker(guestList, cancel = False):
    $colmax = 3
    $platAction = 'Toque' if renpy.variant("android") else 'Clique'
    hbox xalign 0.5 yalign 0.9 spacing 50:
        frame xpadding 10 ypadding 10:
            text "{size=+4}[platAction] em um hóspede para selecioná-lo."
        if cancel:
            frame xpadding 10 ypadding 10:
                textbutton "{size=+4}Cancelar" action Return('cancel') yalign 0.5
    hbox xalign 0.5 yalign 0.35 spacing 10:
        for i in range(int(len(guestList)/colmax)):
            vbox spacing 10:
                for j in range(i*colmax, i*colmax+colmax):
                    $name = guestList[j]
                    frame xpadding 10 ypadding 10 xalign 0.5:
                        hbox spacing 10:
                            imagebutton idle "gui/inventory/icons/big/char_" + name + "_color.png":
                                action Return(name)
                            textbutton "{size=+10}[name]" action Return(name) yalign 0.5
        vbox spacing 10 yalign 0.5:
            for j in range (int(len(guestList)/colmax)*colmax,int(len(guestList))):
                $name = guestList[j]
                frame xpadding 10 ypadding 10 xalign 0.5:
                    hbox spacing 10:
                        imagebutton idle "gui/inventory/icons/big/char_" + name + "_color.png":
                            action Return(name)
                        textbutton "{size=+10}[name]" action Return(name) yalign 0.5


##############################################################################
#                             COUPLE PICKER
##############################################################################

screen CouplePicker(coupleList, cancel = False):
    $colmax = 3
    $platAction = 'Tap' if renpy.variant("android") else 'Click'
    hbox xalign 0.5 yalign 0.9 spacing 50:
        frame xpadding 10 ypadding 10:
            text "{size=+4}[platAction] on a couple to select them."
        if cancel:
            frame xpadding 10 ypadding 10:
                textbutton "{size=+4}Cancel" action Return('cancel') yalign 0.5
    hbox xalign 0.5 yalign 0.35 spacing 10:
        for i in range(int(len(coupleList)/colmax)):
            vbox spacing 10:
                for j in range(i*colmax, i*colmax+colmax):
                    $guest1 = coupleList[j][0]
                    $guest2 = coupleList[j][1]
                    $routeLabel = guest1 + "_" + guest2
                    frame xpadding 10 ypadding 10 xalign 0.5:
                        hbox spacing 10:
                            imagebutton idle "gui/inventory/icons/big/char_" + guest1 + "_color.png":
                                action Return(routeLabel)
                            textbutton "{size=+10}[guest1] and [guest2]" action Return(routeLabel) yalign 0.5
                            imagebutton idle "gui/inventory/icons/big/char_" + guest2 + "_color.png":
                                action Return(routeLabel)
        vbox spacing 10 yalign 0.5:
            for j in range (int(len(coupleList)/colmax)*colmax,int(len(coupleList))):
                $guest1 = coupleList[j][0]
                $guest2 = coupleList[j][1]
                $routeLabel = guest1 + "_" + guest2
                frame xpadding 10 ypadding 10 xalign 0.5:
                    hbox spacing 10:
                        imagebutton idle "gui/inventory/icons/big/char_" + guest1 + "_color.png":
                            action Return(routeLabel)
                        textbutton "{size=+10}[guest1] and [guest2]" action Return(routeLabel) yalign 0.5
                        imagebutton idle "gui/inventory/icons/big/char_" + guest2 + "_color.png":
                            action Return(routeLabel)


##############################################################################
#                             BACKGROUND PICKER
##############################################################################

#This is the screen where you pick your background.
#Displays more information than a simple 6 choice option.

screen BackgroundPicker():
    $PlatSize = 6 if renpy.variant("android") else 2
    vbox xalign 0.5 yalign 0.5 spacing 40:

        frame xalign 0.5 xpadding 10 ypadding 10:
            text "Escolha seu repertório."

        hbox spacing 40:

            frame xminimum 350 xmaximum 350 yminimum 280 xpadding 10:
                vbox xalign 0.5 yalign 0.5 spacing 20:
                    hbox xalign 0.5 spacing 30:
                        image "gui/inventory/icons/MC_humanities.png"
                        text "{size=+4}{color=[UIColorHumanities]}Humanas" yalign 0.5
                    text "{size=-[PlatSize]}Você é melhor na elaboração de contratos e pode conseguir opções adicionais deles. Também é bom em lidar com situações burocráticas."
                    frame xalign 0.5:
                        textbutton "\"Gosto das ciências sociais e humanas.\"" action Return("humanities")

            frame xminimum 350 xmaximum 350 yminimum 280 xpadding 10:
                vbox xalign 0.5 yalign 0.5 spacing 20:
                    hbox xalign 0.5 spacing 30:
                        image "gui/inventory/icons/MC_leader.png"
                        text "{size=+4}{color=[UIColorLeader]}Líder" yalign 0.5
                    text "{size=-[PlatSize]}Você é carismático e um bom mediador de conflitos. Pode fazer algumas escolhas que são fixas para outros repertórios."
                    frame xalign 0.5:
                        textbutton "\"Todo mundo sempre me achou um líder.\"" action Return("leader")

            frame xminimum 350 xmaximum 350 yminimum 280 xpadding 10:
                vbox xalign 0.5 yalign 0.5 spacing 20:
                    hbox xalign 0.5 spacing 30:
                        image "gui/inventory/icons/MC_arts.png"
                        text "{size=+4}{color=[UIColorArts]}Artes" yalign 0.5
                    text "{size=-[PlatSize]}Você possui um vasto conhecimento de literatura, artes e arquitetura. Pode fazer reformas no hotel que trazem hóspedes adicionais."
                    frame xalign 0.5:
                        textbutton "\"Encontrei minha vocação nas artes.\"" action Return("arts")

        hbox spacing 40:

            frame xminimum 350 xmaximum 350 yminimum 280 xpadding 10:
                vbox xalign 0.5 yalign 0.5 spacing 20:
                    hbox xalign 0.5 spacing 30:
                        image "gui/inventory/icons/MC_tech.png"
                        text "{size=+4}{color=[UIColorTech]}Tecnologia" yalign 0.5
                    text "{size=-[PlatSize]}Você tem conhecimento sobre sistemas de computador, programação e engenharia. Pode fornecer ajuda adicional em projetos de P&D de tecnologia."
                    frame xalign 0.5:
                        textbutton "\"Eu tenho uma afinidade com tecnologia.\"" action Return("tech")

            frame xminimum 350 xmaximum 350 yminimum 280 xpadding 10:
                vbox xalign 0.5 yalign 0.5 spacing 20:
                    hbox xalign 0.5 spacing 30:
                        image "gui/inventory/icons/MC_math.png"
                        text "{size=+4}{color=[UIColorMath]}Matemática" yalign 0.5
                    text "{size=-[PlatSize]}Você é analítico e meticuloso. Possui acesso a informações adicionais que levam a uma melhor gestão e otimização da equipe."
                    frame xalign 0.5:
                        textbutton "\"Sou muito talentoso com matemática.\"" action Return("math")

            frame xminimum 350 xmaximum 350 yminimum 280 xpadding 10:
                vbox xalign 0.5 yalign 0.5 spacing 20:
                    hbox xalign 0.5 spacing 30:
                        image "gui/inventory/icons/MC_speedrunner.png"
                        text "{size=+4}{color=[UIColorSpeedrunner]}Speedrunner" yalign 0.5
                    text "{size=-[PlatSize]}Você obtém itens adicionais de exploração e pode tomar vantagem sob um evento perigoso. Bom para uma segunda jogatina."
                    frame xalign 0.5:
                        textbutton "\"Eu faço speedruns para sobreviver.\"" action Return("speedrunner")


##############################################################################
#                               RANK
##############################################################################

#screen that shows your rank at the end of a build

screen RankBar(affection):
    default boton = False
    default myTime = 0
    if boton:
        vbox xalign 0.5 yalign 0.2:
            text "{size=+8}Sua classificação é:" xalign 0.5
            if int(affection) %4 == 0:
                $col = "#7e4317"
            elif int(affection) %4 == 1:
                $col = "#949494"
            elif int(affection) %4 == 2:
                $col = "#d6a335"
            elif int(affection) %4 == 3:
                $col = "#97b3d3"
            $rank = encrypt_rank(affection)
            text "{size=+16}{color=[col]}[rank]" xalign 0.5
    hbox xalign 0.5 yalign 0.4:
        for i in range (0, int(abs(affection)/4)+1):
            if affection >0:
                image "gui/rankbar/meandrosOrange.png"
            else:
                image "gui/rankbar/meandrosBlue.png"
    hbox xalign 0.5 yalign 0.4 xminimum (int(abs(affection)/4)+1)*64:
        hbox xalign 0.0:
            for i in range (0,int(myTime)+1):
                $j = i%4
                image "gui/rankbar/bar" + str(j) + ".png"
    hbox xalign 0.5 yalign 0.4:
        for i in range (0, int(abs(affection)/4)+1):
            image "gui/rankbar/frame.png"
    hbox xalign 0.5 yalign 0.5:
        for i in range (0, int(abs(affection)/4)+1):
            $j = i if i<3 else 3
            $medcol = "gold" if myTime > i*4-1 else "gray"
            image "gui/rankbar/medal_[medcol]_[j].png"

    if myTime < int(abs(affection)):
        $i = 0.02 + 0.02* int(5*myTime/abs(affection))
        timer i repeat True action [SetLocalVariable("myTime", myTime+0.5), Play('sound', "sfx/click.ogg")]

    if int(abs(affection)) == int(myTime):
        timer 1.0 action SetLocalVariable("boton", True)
    if boton:
        frame yalign 0.7 xalign 0.5:
            textbutton "{size=+14}Continuar" action Return()


        vbox xalign 0.95 yalign 0.9 xmaximum 330 spacing 20:
            if player_background == "arts":
                $max = 14.5
                $myText = "{color=[UIColorArts]}Artes{/color}"
            if player_background == "math":
                $max = 14.0
                $myText = "{color=[UIColorMath]}Matemática{/color}"
            if player_background == "tech":
                $max = 14.0
                $myText = "{color=[UIColorTech]}Tecnologia{/color}"
            if player_background == "leader":
                $max = 14.0
                $myText = "{color=[UIColorLeader]}Líder{/color}"
            if player_background == "humanities":
                $max = 14.0
                $myText = "{color=[UIColorHumanities]}Humanas{/color}"
            if player_background == "speedrunner":
                $max = 14.5
                $myText = "{color=[UIColorSpeedrunner]}Speedrunner{/color}"
            text "A classificação máxima desta build para o repertório de " + myText + " é:" xalign 0.5
            if int(max) %4 == 0:
                $col = "#7e4317"
            elif int(max) %4 == 1:
                $col = "#949494"
            elif int(max) %4 == 2:
                $col = "#d6a335"
            elif int(max) %4 == 3:
                $col = "#97b3d3"
            $rankmax = encrypt_rank(max)
            text "{size=+3}{color=[col]}[rankmax]" xalign 0.5


transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script



image bar1:
    contains:
        "gui/rankbar/meandros.png"
    contains:
        "gui/rankbar/frame.png"


##############################################################################
#                               SFW CONFIRMATION
##############################################################################

screen SFWConfirmation:
    modal True
    add "images/blackback.png" alpha 0.5
    frame xminimum 600 yminimum 300 xalign 0.5 yalign 0.5:
        vbox xalign 0.5 yalign 0.5 spacing 40:
            vbox:
                text "{i}Ativar o modo SFW?" xalign 0.5
                text "{i}Isto censurará a nudez e pulará as cenas de sexo." xalign 0.5
            hbox xalign 0.5 spacing 30:
                imagebutton:
                    if not persistent.sfwMode:
                        idle "gui/checkbox_idle.png"
                        action SetField(persistent, "sfwMode", True)
                    else:
                        idle "gui/checkbox_hover.png"
                        action SetField(persistent, "sfwMode", False)
                text "{i}Modo SFW" yalign 0.5
            hbox xminimum 300 xalign 0.5:
                textbutton "{size=+4}Começar jogo" action [Function(hideExtraMenuScreens, 'start'), Start(), Hide("SFWConfirmation")]
                textbutton "{size=+4}Cancelar" action Hide("SFWConfirmation") xalign 1.0

##############################################################################
#                                  OTHER
##############################################################################

transform xalcenter:
    xalign 0.5
    yalign 1.0

transform xalleft:
    xalign 0.1
    yalign 1.0

transform xalright:
    xalign 0.9
    yalign 1.0

transform xallefter:
    xalign -0.1
    yalign 1.0

transform xalrighter:
    xalign 1.1
    yalign 1.0
