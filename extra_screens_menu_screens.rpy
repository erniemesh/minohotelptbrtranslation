##############################################################################
#                                 ALLIGNMENT
##############################################################################

init python:
    if renpy.variant("android"):
        ButtonBarHeight = 127
        SaveScrollY = 610
    else:
        ButtonBarHeight = 90
        SaveScrollY = 585


############################################################################
#                        CUSTOM MENU SCREENS
############################################################################

screen mobileGuestsMenu():
    $PlatAlign = 0.28 if renpy.variant("android") else 0.265
    $PlatClick = 'Toque' if renpy.variant("android") else 'Clique'

    tag menu

    #display BG
    add "images/backtitle.png"

    use navigation

    #add scrolls
    add "scrollsMobileGuest"

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Hóspedes{/size}" yalign 0.5

    #Guest Icons
    hbox xpos 92 yalign PlatAlign spacing 20:
        for guest_name in preset_guest_names:
            $icon_filename = get_guest_inventory_filename(guest_name, size = 'big')
            $tooltip_info = get_guest_tooltip(guests, persistent.known_guests, guest_name, preset_guest_descriptions)
            $guest_stats = guests.get_guest_stats(guest_name)
            imagebutton idle icon_filename:
                action Show("mobileGuestDescription", guest_name=tooltip_info['title'], description=tooltip_info['description'], stats=guest_stats)
                hovered Show("mobileGuestDescription", guest_name=tooltip_info['title'], description=tooltip_info['description'], stats=guest_stats)

    frame xpos 140 ypos 476 xminimum 1000 yminimum 200:
        text "{size=+10}[PlatClick] em um hóspede para aprender mais.{/size}" xalign 0.5 yalign 0.5


screen mobileTeamsMenu():
    $PlatAlign = 0.15 if renpy.variant("android") else 0.006
    $PlatTeam = -0.05 if renpy.variant("android") else 0.006
    $PlatSpace = 4 if renpy.variant("android") else 20

    tag menu

    #display BG
    add "images/backtitle.png"

    use navigation

    #add scrolls
    add "scrollsMobileTeams"

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Equipes{/size}" yalign 0.5

    vbox yalign 0.6+PlatAlign xalign 0.1 spacing PlatSpace:
        if UI_permissions['rd']:
            text "{size=+10}P&D{/size}" xalign 0.5
        else:
            text "{size=+10}???{/size}" xalign 0.5
        frame xminimum 500 yminimum 450:
            if UI_permissions['rd']:
                vbox xalign 0.5 yalign 0.7 spacing 20:
                    $rd_stats = calculate_rd_team_stats()
                    $relationship_bonus = relationships.get_relationships_with_guests(guests.get_rd_team().names()).sum_bonus()
                    $stat_list = ['Contract', 'Tech', 'Fragment'] if UI_permissions['fragments'] else ['Contract', 'Tech']
                    for stat in stat_list:
                        $stat_color = UIColorPink if relationship_bonus.get_value(stat) != 0 else UIColorOrange
                        $stat_value = rd_stats.get_value(stat)
                        text "{size=+6}{color=[stat_color]}[stat]:{/color} [stat_value]{/size}"


    vbox yalign 0.6+PlatAlign xalign 0.9 spacing PlatSpace:
        if UI_permissions['exploration']:
            text "{size=+10}Exploração{/size}" xalign 0.5
        else:
            text "{size=+10}???{/size}" xalign 0.5
        frame xminimum 500 yminimum 450:
            if UI_permissions['exploration']:
                vbox xalign 0.5 yalign 0.8:
                    $ex_stats = calculate_exploration_team_stats()
                    $relationship_bonus = relationships.get_relationships_with_guests(guests.get_exploration_team().names()).sum_bonus()
                    $stat_list = ['Memento', 'Artifact', 'Surveying', 'Fragment', 'Danger'] if UI_permissions['fragments'] else ['Memento', 'Artifact', 'Surveying', 'Danger']
                    for stat in stat_list:
                        $stat_color = UIColorPink if relationship_bonus.get_value(stat) != 0 else UIColorOrange
                        if stat == 'Danger':
                            $stat_color = UIColorDanger
                        $stat_value = ex_stats.get_value(stat)
                        text "{size=+6}{color=[stat_color]}[stat]:{/color} [stat_value]{/size}"

                    text "{size=+6}{color=[UIColorOrange]}Raw materials: {/color}[inventory.raw_materials]{/size}"

    #RD guest icons
    if UI_permissions['rd']:
        vbox xalign 0.1 yalign 0.36-PlatTeam xminimum 500:
            hbox xalign 0.5 spacing 50:
                for guest_name in guests.get_rd_team().names():
                    $icon_filename = get_guest_inventory_filename(guest_name, size = 'big')
                    $tooltip_info = get_guest_tooltip(guests, persistent.known_guests, guest_name, preset_guest_descriptions)
                    imagebutton idle icon_filename:
                        action Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        hovered Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        unhovered Hide("menu_tooltip")


   #Exploration guest icons
    if UI_permissions['exploration']:
        vbox xalign 0.9 yalign 0.36-PlatTeam xminimum 500:
            hbox xalign 0.5 spacing 50:
                for guest_name in guests.get_exploration_team().names():
                    $icon_filename = get_guest_inventory_filename(guest_name, size = 'big')
                    $tooltip_info = get_guest_tooltip(guests, persistent.known_guests, guest_name, preset_guest_descriptions)
                    imagebutton idle icon_filename:
                        action Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        hovered Show("menu_tooltip", title=tooltip_info['title'], description=tooltip_info['description'])
                        unhovered Hide("menu_tooltip")


screen mobileHistoryMenu():
    $PlatAlign = 170 if renpy.variant("android") else 155
    tag menu
    #display BG
    add "images/backtitle.png"
    use navigation

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Histórico{/size}" yalign 0.5

    if _history_list:
        side "c r":
            area (100, PlatAlign, 1080, 500)

            viewport id "vp":
                yinitial 1.0
                draggable True
                mousewheel True

                vbox spacing 10:
                    for h in _history_list:

                        if h.who:
                            hbox spacing 30:
                                hbox xminimum 150:
                                    if "color" in h.who_args:
                                        $myCol = h.who_args["color"]
                                    else:
                                        $myCol = UIColorOrange
                                    text "{color=[myCol]}[h.who]" xalign 1.0
                                text "{size=-1}{i}[h.what]":
                                    size gui.text_size + persistent.text_font_size
                                    if persistent.dyslexic_mode:
                                        font "fonts/OpenDyslexic.otf"
                        else:
                            text "{size=-1}{i}[h.what]":
                                size gui.text_size + persistent.text_font_size
                                if persistent.dyslexic_mode:
                                    font "fonts/OpenDyslexic.otf"

            vbar value YScrollValue("vp")
    else:
        text "O histórico de diálogo está vazio." xalign 0.5 yalign 0.55


screen mobilePreferencesMenu():
    $PlatAlign = 0.05 if renpy.variant("android") else 0
    $PlatSpace = -70 if renpy.variant("android") else 30
    $PlatXpos = 72 if renpy.variant("android") else 85

    tag menu
    #display BG
    add "images/backtitle.png"
    use navigation
    #add scrolls
    add "scrollsMobileTeams"

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Configurações{/size}" yalign 0.5

    hbox xpos PlatXpos yalign 0.3+PlatAlign spacing PlatSpace:
        if renpy.variant("pc"):
            vbox:
                style_prefix "radio"
                label _("{size=+6}Tela")
                textbutton _("{size=+4}Janela") action Preference("display", "window")
                textbutton _("{size=+4}Tela Cheia") action Preference("display", "fullscreen")

        vbox:
            style_prefix "radio"
            label _("{size=+6}Toque Lateral")
            textbutton _("{size=+4}Desativar") action Preference("rollback side", "disable")
            textbutton _("{size=+4}Esquerda") action Preference("rollback side", "left")
            textbutton _("{size=+4}Direita") action Preference("rollback side", "right")

        vbox:
            style_prefix "check"
            label _("{size=+6}Pular")
            textbutton _("{size=+4}Texto não visto") action Preference("skip", "toggle")
            textbutton _("{size=+4}Depois de escolhas") action Preference("after choices", "toggle")
            textbutton _("{size=+4}Transições") action InvertSelected(Preference("transitions", "toggle"))

        vbox:
            style_prefix "radio"
            label _("{size=+6}Rolagem")
            textbutton _("{size=+4}Desligada") action SetField(persistent, "scroll_speed", 0)
            textbutton _("{size=+4}Lenta") action SetField(persistent, "scroll_speed", 1)
            textbutton _("{size=+4}Rápida") action SetField(persistent, "scroll_speed", 2)

        vbox:
            style_prefix "radio"
            label _("{size=+6}Tamanho da Fonte")
            textbutton _("{size=+4}Pequeno") action SetField(persistent, "text_font_size", -2)
            textbutton _("{size=+4}Normal") action SetField(persistent, "text_font_size", 0)
            textbutton _("{size=+4}Grande") action SetField(persistent, "text_font_size", 2)

    hbox xalign 0.5 yalign 0.8+PlatAlign:
        style_prefix "slider"
        box_wrap True
        vbox:
            label _("{size=+4}Velocidade do Texto")
            bar value Preference("text speed")
            label _("{size=+4}Tempo de Avanço Automático")
            bar value Preference("auto-forward time")
            text ""
            vbox xalign 0.5 spacing 20:
                if not permaSFW:
                    hbox spacing 30:
                        imagebutton:
                            if not persistent.sfwMode:
                                idle "gui/checkbox_idle.png"
                                action SetField(persistent, "sfwMode", True)
                            else:
                                idle "gui/checkbox_hover.png"
                                action SetField(persistent, "sfwMode", False)
                        text "{i}Modo SFW (Sem Nudez)" yalign 0.5
                hbox spacing 30:
                    imagebutton:
                        if not persistent.dyslexic_mode:
                            idle "gui/checkbox_idle.png"
                            action SetField(persistent, "dyslexic_mode", True)
                        else:
                            idle "gui/checkbox_hover.png"
                            action SetField(persistent, "dyslexic_mode", False)
                    text "{i}Fonte amigável para dislexia" yalign 0.5

        vbox:
            if config.has_music:
                label _("{size=+4}Volume da Música")
                hbox:
                    bar value Preference("music volume")
            if config.has_sound:
                label _("{size=+4}Volume do Som")
                hbox:
                    bar value Preference("sound volume")
                    if config.sample_sound:
                        textbutton _("{size=+4}Testar") action Play("sound", config.sample_sound)
            if config.has_voice:
                label _("{size=+4}Volume da Voz")
                hbox:
                    bar value Preference("voice volume")
                    if config.sample_voice:
                        textbutton _("{size=+4}Testar") action Play("voice", config.sample_voice)
            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing
                textbutton _("{size=+4}Silenciar Tudo"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"


screen save():
    tag menu
    #display BG
    add "images/backtitle.png"
    use navigation

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Salvar{/size}" yalign 0.5
    use mobileFileSlots(_("Load"), 'save')
    use saveSideInfo()


screen mobileLoadMenu():
    tag menu
    #display BG
    add "images/backtitle.png"
    use navigation

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Carregar{/size}" yalign 0.5
    use mobileFileSlots(_("Load"), 'load')
    if not main_menu:
        use saveSideInfo()
    else:
        add "scrollsMobileSave"


screen mobileItemsMenu():
    $PlatAlign = 0.33 if renpy.variant("android") else 0.3

    tag menu
    #display BG
    add "images/backtitle.png"
    use navigation
    #add scrolls
    add "scrollsMobileGuest"

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Itens{/size}" yalign 0.5

    #Item icons
    hbox yalign PlatAlign xalign 0.5 spacing 40:
        for item in inventory.items:
            imagebutton idle "gui/inventory/icons/big/item_" + item + ".png":
                action Show("mobileItemsDescription", title=item, description=preset_item_descriptions[item])
                hovered Show("mobileItemsDescription", title=item, description=preset_item_descriptions[item])

    frame xpos 140 ypos 476 xminimum 1000 yminimum 200:
        $message = "Coloque o mouse"
        if renpy.variant("android"):
            $message = "Toque"
        text "{size=+10}[message] em um item para aprender mais.{/size}" xalign 0.5 yalign 0.5


screen mobileHelpMenu():
    $PlatAlign = 155 if renpy.variant("android") else 140
    $PlatAlign2= 0.565 if renpy.variant("android") else 0.55
    default device = "keyboard"
    default myOption = 'none'
    tag menu
    #display BG
    add "images/backtitle.png"
    use navigation
    #add scrolls
    add "scrollsMobileTeams"

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{i}{/i}{size=+10}Ajuda{/size}" yalign 0.5

    vbox spacing 20 yalign PlatAlign2 xalign 0.05:
        if renpy.variant("pc"):
            frame xalign 0.5 xminimum 190 ypadding 10 xpadding 10:
                textbutton "{size=+6}Controles" action SetLocalVariable("myOption", "controls") xalign 0.5
        if not main_menu:
            frame xalign 0.5 xminimum 190 ypadding 10 xpadding 10:
                if player_background != "":
                    textbutton "{size=+6}Meu repertório" action SetLocalVariable("myOption", "background") xalign 0.5
                else:
                    text "{size=+2}{i}{color=[UIColorDisabled]}Meu repertório" xalign 0.5
            frame xalign 0.5 xminimum 190 ypadding 10 xpadding 10:
                if UI_permissions['rd'] or UI_permissions['exploration']:
                    textbutton "{size=+6}Sessões de equipe" action SetLocalVariable("myOption", "teams") xalign 0.5
                else:
                    text "{size=+2}{i}{color=[UIColorDisabled]}Sessões de equipe" xalign 0.5
            frame xalign 0.5 xminimum 190 ypadding 10 xpadding 10:
                if UI_permissions['rd'] or UI_permissions['exploration']:
                    textbutton "{size=+6}Explicação de atributo" action SetLocalVariable("myOption", "stats") xalign 0.5
                else:
                    text "{size=+2}{i}{color=[UIColorDisabled]}Explicação de atributo" xalign 0.5
            frame xalign 0.5 xminimum 190 ypadding 10 xpadding 10:
                if build >=4:
                    textbutton "{size=+6}Rotas de hóspedes" action SetLocalVariable("myOption", "routes") xalign 0.5
                else:
                    text "{size=+2}{i}{color=[UIColorDisabled]}Rotas de hóspedes" xalign 0.5


    if myOption == 'controls':
        vbox spacing 20 yalign 0.7 xalign 0.7 yminimum 460 xminimum 540 xmaximum 540:
            hbox spacing 10:
                textbutton "{size=+6}Teclado" action SetLocalVariable("device", "keyboard")
                textbutton "{size=+6}Mouse" action SetLocalVariable("device", "mouse")
                if GamepadExists():
                    textbutton "{size=+6}Gamepad" action SetLocalVariable("device", "gamepad")
            if device == "keyboard":
                grid 2 11:
                    text "{color=[UIColorOrange]}Enter"
                    text "{size=-2}{i}Avança o diálogo e ativa a interface."

                    text "{color=[UIColorOrange]}Espaço"
                    text "{size=-2}{i}Avança o diálogo sem fazer escolhas."

                    text "{color=[UIColorOrange]}Setas"
                    text "{size=-2}{i}Navega a interface."

                    text "{color=[UIColorOrange]}Esc"
                    text "{size=-2}{i}Acessa o menu do jogo."

                    text "{color=[UIColorOrange]}Ctrl"
                    text "{size=-2}{i}Pula o diálogo enquanto pressionado."

                    text "{color=[UIColorOrange]}Tab"
                    text "{size=-2}{i}Ativa/Desativa o pulo de diálogo."

                    text "{color=[UIColorOrange]}Page Up"
                    text "{size=-2}{i}Volta para o diálogo anterior."

                    text "{color=[UIColorOrange]}Page Down"
                    text "{size=-2}{i}Avança para o diálogo posterior."

                    text "{color=[UIColorOrange]}H"
                    text "{size=-2}{i}Esconde a interface de usuário."

                    text "{color=[UIColorOrange]}S"
                    text "{size=-2}{i}Tira uma captura de tela."

                    text "{color=[UIColorOrange]}V"
                    text "{size=-2}{i}Ativa/Desativa o {a=https://www.renpy.org/l/voicing}assistente de voz{/a}."

            if device == "mouse":
                grid 2 5:
                    text "{color=[UIColorOrange]}Clique Esquerdo"
                    text "{size=-2}{i}Avança o diálogo e ativa a interface."

                    text "{color=[UIColorOrange]}Clique Médio"
                    text "{size=-2}{i}Esconde a interface de usuário."

                    text "{color=[UIColorOrange]}Clique Direito"
                    text "{size=-2}{i}Acessa o menu do jogo."

                    text "{color=[UIColorOrange]}Roda do Mouse para cima\nClique Lateral"
                    text "{size=-2}{i}Volta para o diálogo anterior."

                    text "{color=[UIColorOrange]}Roda do Mouse para baixo"
                    text "{size=-2}{i}Avança para o diálogo posterior."

            if device == "gamepad":
                vbox spacing 0:
                    grid 2 6:
                        text "{color=[UIColorOrange]}RT\nA/Botão Inferior"
                        text "{size=-2}{i}Avança o diálogo e ativa a interface."

                        text "{color=[UIColorOrange]}LT\nLS"
                        text "{size=-2}{i}Volta para o diálogo anterior."

                        text "{color=[UIColorOrange]}RS"
                        text "{size=-2}{i}Avança para o diálogo posterior."

                        text "{color=[UIColorOrange]}Botões de Direção, Sticks"
                        text "{size=-2}{i}Navega a interface."

                        text "{color=[UIColorOrange]}Start, Guia"
                        text "{size=-2}{i}Acessa o menu do jogo."

                        text "{color=[UIColorOrange]}Y/Botão Superior"
                        text "{size=-2}{i}Esconde a interface de usuário."
                    textbutton _("Calibrar") action GamepadCalibrate()

    if myOption == 'background':
        side "c r":
            area (360, PlatAlign, 820, 500)
            viewport id "vp":
                draggable True
                mousewheel True
                vbox spacing 10:
                    if player_background == 'tech':
                        text "Seu repertório é {color=[UIColorTech]}Tecnologia{/color}."
                        text "Você tem conhecimento sobre sistemas de computação e engenharia."
                        text "Como resultado, você tem um bônus passivo para para pontos de tecnologia em projetos de P&D."
                        text "Isso permite que suas equipes concluam projetos relacionados a tecnologia com mais rapidez."

                    if player_background == 'arts':
                        text "Seu repertório é {color=[UIColorArts]}Artes{/color}."
                        text "Com seu repertório, você tem um vasto conhecimento de literatura, artes e arquitetura."
                        text "Em certos momentos, você poderá fazer reformas adicionais no hotel."
                        text "Estas reformas trarão novos hóspedes, aumentando seu limite máximo de hóspedes disponíveis para além dos outros repertórios."

                    if player_background == 'humanities':
                        text "Seu repertório é {color=[UIColorHumanities]}Humanas{/color}."
                        text "Isto o torna melhor na elaboração de contratos que nos outros repertórios possíveis, dando-lhe um bônus passivo para pontos de contrato em projetos de P&D."
                        text "Além disso, quando suas equipes criam contratos, você pode obter opções adicionais para modificar seus termos."
                        text "Você também é bom em lidar com situações burocráticas e trabalhar sob pressão."

                    if player_background == 'math':
                        text "Seu repertório é {color=[UIColorMath]}Matemática{/color}."
                        text "Você é analítico e meticuloso e acha mais fácil detectar contradições nas declarações das pessoas."
                        text "Durante os segmentos de gerenciamento de equipe, você terá acesso a informações adicionais:"
                        text "• Os pontos de progresso acumulados por ambas equipes." xpos 30
                        text "• A quantidade de recompensas possíveis que sua atual composição de equipe pode obter." xpos 30
                        text "Eles permitem que você tome melhores decisões sobre as composições de sua equipe."
                        if build > 4:
                            text "Você também obtém uma melhor estimativa de quanto tempo precisa passar com um hóspede para concluir suas rotas ou relacionamentos no menu de Hóspedes."

                    if player_background == 'leader':
                        text "Seu repertório é {color=[UIColorLeader]}Líder{/color}."
                        text "Você é muito confiante e carismático."
                        text "Isso o torna um bom mediador de conflitos e permite que você escape de situações difíceis por meio do diálogo."
                        text "Algumas opções são fixas para os outros repertórios, mas você pode escolher outras."

                    if player_background == 'speedrunner':
                        text "Seu repertório é {color=[UIColorSpeedrunner]}Speedrunner{/color}."
                        text "Você é meio bobo e às vezes não será levado a sério. Algumas escolhas serão feitas por você."
                        text "Você tem seus momentos de brilho, no entanto. É mais provável que você obtenha itens adicionais com a exploração do que nos outros repertórios."
                        text "Além disso, se sua equipe encontrar uma situação de Perigo ao explorar o labirinto, há uma chance de resolverem o problema e obterem recompensas adicionais."

            vbar value YScrollValue("vp")

    if myOption == 'stats':
        side "c r":
            area (360, PlatAlign, 820, 500)
            viewport id "vp":
                draggable True
                mousewheel True
                vbox spacing 10:
                    text "Cada hóspede jogável possui um conjunto de atributos que afetam seu desempenho nas sessões de equipe."
                    if UI_permissions['rd']:
                        text ""
                        text "{i}{color=[UIColorOrange]}Atributos de P&D" xalign 0.5
                        text "{i}{color=[UIColorOrange]}•  Tecnologia{/color}{/i}: Indica a capacidade do hóspede de contribuir com projetos de tecnologia na equipe de P&D."
                        text "{i}{color=[UIColorOrange]}•  Contratos{/color}{/i}: A capacidade do hóspede de elaborar contratos na equipe de P&D."
                    if UI_permissions['exploration']:
                        text ""
                        text "{i}{color=[UIColorOrange]}Exploration Stats" xalign 0.5
                        text "{i}{color=[UIColorOrange]}•  Lembranças{/color}{/i}: Torna o hóspede mais propenso a encontrar lembranças do passado de Asterion no labirinto."
                        text "{i}{color=[UIColorOrange]}•  Artefatos{/color}{/i}: Indica a probabilidade do hóspede de encontrar artefatos antigos no labirinto que podem aumentar as estatísticas de seus hóspedes."
                        text "{i}{color=[UIColorOrange]}•  Inspeção{/color}{/i}: Determina a quantidade de materiais que o hóspede provavelmente encontrará. Quanto maior for o total, maiores serão as chances de dobrar suas recompensas ou obter bônus adicionais, e menores serão as chances de não encontrar nada."
                        text "{i}{color=[UIColorDanger]}•  Perigo{/color}{/i}: A probabilidade do hóspede de correr riscos, ser atacado ou colocar a equipe em perigo."
                        text "Se Perigo for o atributo total mais alto em sua equipe de exploração, sua equipe pode entrar em uma situação perigosa no labirinto e correr o risco de deixar seus hóspedes temporariamente incapacitados."
                    if UI_permissions['fragments']:
                        text "{i}{color=[UIColorOrange]}•  Fragmentos{/color}{/i}: Indica a probabilidade de seu hóspede encontrar Fragmentos Divinos no labirinto e sua capacidade de pesquisá-los na equipe de P&D."

            vbar value YScrollValue("vp")

    if myOption == 'teams':
        side "c r":
            area (360, PlatAlign, 820, 500)
            viewport id "vp":
                draggable True
                mousewheel True
                vbox spacing 10:
                    text "{color=[UIColorOrange]}•  {/color}At the start of every in-game day, you will be given the chance to assign some of your guests to a team and perform tasks to improve the hotel."
                    if UI_permissions['rd']:
                        text "{color=[UIColorOrange]}•  {/color}The {i}{color=[UIColorOrange]}R&D Team{/color}{/i} will research technological projects to expand the hotel's capabilites, or work out new contracts that modify the rules of the hotel."
                    if UI_permissions['exploration']:
                        text "{color=[UIColorOrange]}•  {/color}The {i}{color=[UIColorOrange]}Exploration Team{/color}{/i} will head out to the labyrinth and explore it, acquiring goods such as mementos from hotel's past, artifacts that might help your guests, and materials that the hotel can't replenish upon request."

                    add "gui/teamexplanation.jpg" xalign 0.5

                    text "{color=[UIColorOrange]}•  {/color}To assign a guest to a team in the guest management screen, click/tap on their icon (1), and then select the appropriate option (2)."
                    text "Similarly, you can dismiss a guest already assigned to a team by clicking/tapping their icon in the team and selecting the 'dismiss' option."
                    text "{i}(Keep in mind that each team has a maximum of 3 guests, and some guests may be temporarily unavailable for selection.){/i}"
                    text ""
                    if UI_permissions['rd']:
                        if UI_permissions['exploration']:
                            text "{color=[UIColorOrange]}•  {/color}Every session, your team's stat total will be spent working towards a reward, such as completing a tech project or crafting a contract, or finding a memento or artifact."
                        else:
                            text "{color=[UIColorOrange]}•  {/color}Every session, your team's stat total will be spent working towards a reward, such as completing a tech project or crafting a contract."
                    else:
                        text "{color=[UIColorOrange]}•  {/color}Every session, your team's stat total will be spent working towards a reward, such as finding a memento or artifact."
                    text "{color=[UIColorOrange]}•  {/color}Every reward has a stat requirement that must be met for you to obtain it. If your team can't reach that total, don't worry! Your progress towards obtaining a reward will carry on to future sessions."
                    text "{color=[UIColorOrange]}•  {/color}Each team can only obtain one reward per session. If more than one reward is possible, you will unlock the one with the higher stat requirement, and the one that matches your team's highest overall stat."

                    if UI_permissions['exploration']:
                        text "{color=[UIColorOrange]}•  {/color}Additionally, your exploration team will obtain random rewards based on your total surveying stat. These include raw materials and maybe more, if you're lucky."
                        text ""
                        text "{color=[UIColorOrange]}•  {/color}Keep an eye out on your Exploration team's {color=[UIColorDanger]}Danger{/color} stat. If it gets too high, you might get attacked while exploring the labyrinth!"

            vbar value YScrollValue("vp")


    if myOption == 'routes':
        side "c r":
            area (360, PlatAlign, 820, 500)
            viewport id "vp":
                draggable True
                mousewheel True
                vbox spacing 10:
                    text "{color=[UIColorOrange]}•  {/color}You can now choose to spend time with your guests."
                    text "{color=[UIColorOrange]}•  {/color}If, immediately after a team session, any of your guests are available but don't have an assigned task, you can choose to spend time with one of them."
                    text "{color=[UIColorOrange]}•  {/color}Spending time with that guest will help him work through his issues or get more insight on him."
                    text "{color=[UIColorOrange]}•  {/color}As a result, the guest's stats can improve."
                    text "{color=[UIColorOrange]}•  {/color}It's up to you to balance a guest's personal development with his contributions to R&D and exploration."
                    if player_background == "math":
                        text "{color=[UIColorOrange]}•  {/color}As a result of your {color=[UIColorMath]}Math{/color} background, you can see the detailed progress of your guests' routes in the {i}{color=[UIColorOrange]}Guests{/color}{/i} menu."
                    else:
                        text "{color=[UIColorOrange]}•  {/color}You can see each guest's progress in the {i}{color=[UIColorOrange]}Guests{/color}{/i} menu."
                    text ""
                    text "{color=[UIColorOrange]}•  As of this build, every guest route is a work in progress. You may get a message on the guest select screen informing you that you can't currently advance a certain character's route past that point."
            vbar value YScrollValue("vp")



################################################################################
#                                EXTRA SCREENS
################################################################################

screen mobileFileSlots(title, saveLoad):
    $PlatAlign = 0.54 if renpy.variant("android") else 0.44
    $PageY= 637 if renpy.variant("android") else 627
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The grid of file slots.
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign PlatAlign

            spacing gui.slot_spacing
            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1
                button:
                    #action FileAction(slot)
                    if saveLoad == 'load':
                        action FileLoad(slot)
                    else:
                        action FileSave(slot)
                    has vbox
                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{size=+6}{#file_time}%A, %B %d %Y, %H:%M"), empty=_("{size=+12}Empty slot")):
                        style "slot_time_text"

                    if FileSaveName(slot)=="":
                        text FileSaveName(slot):
                            style "slot_name_text"
                    else:
                        if FileSaveName(slot)=="math":
                            text "{color=[UIColorMath]}Matemática{/color}" xalign 0.5 size 24
                        elif FileSaveName(slot)=="tech":
                            text "{color=[UIColorTech]}Tecnologia{/color}" xalign 0.5 size 24
                        elif FileSaveName(slot)=="leader":
                            text "{color=[UIColorLeader]}Líder{/color}" xalign 0.5 size 24
                        elif FileSaveName(slot)=="speedrunner":
                            text "{color=[UIColorSpeedrunner]}Speedrunner{/color}" xalign 0.5 size 24
                        elif FileSaveName(slot)=="humanities":
                            text "{color=[UIColorHumanities]}Humanas{/color}" xalign 0.5 size 24
                        elif FileSaveName(slot)=="arts":
                            text "{color=[UIColorArts]}Artes{/color}" xalign 0.5 size 24
                        else:
                            text FileSaveName(slot) xalign 0.5 size 24

                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            style_prefix "page"

            xalign 0.5
            ypos PageY

            spacing 10
            textbutton _("{size=+10}<{/size}") action FilePagePrevious()
            if config.has_autosave:
                textbutton _("{size=+10}{#auto_page}A{/size}") action FilePage("auto")
            if config.has_quicksave:
                textbutton _("{size=+10}{#quick_page}R{/size}") action FilePage("quick")
            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "{size=+10}[page]{/size}" action FilePage(page)
            textbutton _("{size=+10}>{/size}") action FilePageNext()


screen saveSideInfo():
    $InfoAlign = 0.54 if renpy.variant("android") else 0.47
    add "scrollsMobileSave"

    #background on the left
    vbox spacing 40 xalign 0.975 yalign InfoAlign:
        vbox xalign 0.5 spacing 10:
            if player_background != "":
                text "Your background:" xalign 0.5
                $fn="gui/inventory/icons/MC_" + player_background + ".png"
                image "[fn]" xalign 0.5
                if player_background == "arts":
                    text "{size=+2}{color=[UIColorArts]}Artes{/color}{/size}" xalign 0.5
                if player_background == "math":
                    text "{size=+2}{color=[UIColorMath]}Matemática{/color}{/size}" xalign 0.5
                if player_background == "tech":
                    text "{size=+2}{color=[UIColorTech]}Tecnologia{/color}{/size}" xalign 0.5
                if player_background == "leader":
                    text "{size=+2}{color=[UIColorLeader]}Líder{/color}{/size}" xalign 0.5
                if player_background == "humanities":
                    text "{size=+2}{color=[UIColorHumanities]}Humanas{/color}{/size}" xalign 0.5
                if player_background == "speedrunner":
                    text "{size=+2}{color=[UIColorSpeedrunner]}Speedrunner{/color}{/size}" xalign 0.5

    vbox xalign 0.04 yalign InfoAlign spacing 30:
        if player_name is not '':
            vbox xalign 0.5 spacing 5:
                text "Jogador:" xalign 0.5
                text "[player_name]" xalign 0.5
        #chapter
        text "[chapter]" xalign 0.5


screen mobileGuestDescription(guest_name, description, stats=None):
    #recieves a tuple with title and description. If description is "none", it won't be displayed

    frame xalign 0.5 ypos 475 xminimum 1100 yminimum 200:
        vbox yalign 0.5 xalign 0.5 spacing 20:
            hbox spacing 50 xalign 0.5:
                text "{size=+10}[guest_name]{/size}"
                if description != "none":
                    text "{size=+4}{color=[UIColorOrange]}{i}[description]{/i}{/color}" yalign 1.0
            if stats is not None:
                hbox xalign 0.5 spacing 100:
                    hbox spacing 30:
                        if UI_permissions['rd']:
                            vbox:
                                $contract = stats.get_value('Contract')
                                text "{size=+4}{color=[UIColorOrange]}Contratos:{/color} [contract]"
                                $tech = stats.get_value('Tech')
                                text "{size=+4}{color=[UIColorOrange]}Tecnologia:{/color} [tech]"
                        if UI_permissions['exploration']:
                            vbox:
                                $mementos = stats.get_value('Memento')
                                text "{size=+4}{color=[UIColorOrange]}Lembranças:{/color} [mementos]"
                                $artifact = stats.get_value('Artifact')
                                text "{size=+4}{color=[UIColorOrange]}Artefatos:{/color} [artifact]"
                            vbox:
                                $surveying = stats.get_value('Surveying')
                                text "{size=+4}{color=[UIColorOrange]}Inspeção:{/color} [surveying]"
                                $danger = stats.get_value('Danger')
                                text "{size=+4}{color=[UIColorDanger]}Perigo:{/color} [danger]"
                        if UI_permissions['fragments']:
                            vbox:
                                $fragment = stats.get_value('Fragment')
                                text "{size=+4}{color=[UIColorOrange]}Fragmentos:{/color} [fragment]" yalign 0.5
                    if build >=4:
                        vbox yalign 0.5:
                            hbox spacing 10 xalign 0.5:
                                $progress = guests.guests[guest_name].route_progress
                                $max_route = preset_guest_route_length[guest_name]
                                text 'Crescimento:' yalign 0.5
                                bar value progress range max_route xmaximum 120 left_bar Frame("/gui/orangebar.png", 12, 12)  right_bar Frame("/gui/orangebarback.png", 12, 12) yalign 0.5
                                if player_background == "math":
                                    $prog= str(progress)
                                    $top = str(max_route)
                                    text "{color=[UIColorMath]}[prog]/[top]" yalign 0.5
                            if guests.guests[guest_name].romance_status == 'single':
                                hbox xalign 0.5 yminimum 70:
                                    text 'Relacionamento: Solteiro' yalign 0.5
                            else:
                                $couple = guests.guests[guest_name].romance_partner
                                hbox xalign 0.5 spacing 10 yminimum 70:
                                    $progress = relationships.get_relationship_progress(guest_name)
                                    $max_route = get_relationship_maximum_length(guest_name, couple)
                                    #$max_route = preset_maximum_relationship_length[guest_name+','+couple]
                                    text 'Relacionamento:' yalign 0.5
                                    image get_guest_inventory_filename(couple) yalign 0.5
                                    bar value progress range max_route xmaximum 120 left_bar Frame("/gui/pinkbar.png", 12, 12)  right_bar Frame("/gui/pinkbarback.png", 12, 12) yalign 0.5
                                    if player_background == "math":
                                        $prog= str(progress)
                                        $top = str(max_route)
                                        text "{color=[UIColorMath]}[prog]/[top]" yalign 0.5


screen mobileItemsDescription(title, description):
    frame xpos 140 ypos 476 xminimum 1000 yminimum 200:
        vbox yalign 0.5 xalign 0.5 spacing 40:
            text "{size=+10}[title]{/size}" xalign 0.5
            if description != "none":
                text "{size=+4}{color=[UIColorOrange]}{i}[description]{/i}{/color}" xalign 0.5


################################################################################
#                                   SCROLLS
################################################################################

image scrollsButtonBar:
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos ButtonBarHeight
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image scrollsMobileGuest:
    contains:
        "gui/inventory/scroll.png"
        xpos 0.0 ypos 440
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 685
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image scrollsMobileSave:
    contains:
        "gui/inventory/scroll.png"
        xpos 0.0 ypos SaveScrollY
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos -1.0*scroll_speed_1(persistent.scroll_speed)
        repeat
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 685
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

image scrollsMobileTeams:
    contains:
        "gui/inventory/scroll.png"
        xpos -1*scroll_speed_1(persistent.scroll_speed)
        ypos 688
        linear 60.0*scroll_speed_2(persistent.scroll_speed) xpos 0.0
        repeat

#Function that hides the additional screens when toggling between menus
init python:
    def hideExtraMenuScreens(pressedButton):
        if pressedButton != 'guests':
            renpy.hide_screen("mobileGuestDescription")
        if pressedButton != 'items':
            renpy.hide_screen("mobileItemsDescription")

############################################################################
#                          THE ABOUT SCREEN
############################################################################

screen mobileAboutMenu():
    $PlatAlign = 170 if renpy.variant("android") else 155

    tag menu

    #display BG
    add "images/backtitle.png"

    use navigation

    #add scrolls
    add "scrollsMobileTeams"

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Sobre{/size}" yalign 0.5

    side "c r":
        area (100, PlatAlign, 1080, 500)

        viewport id "vp":
            draggable True
            mousewheel True

            #add "washington.jpg"

            vbox spacing 10:
                text "{size=+10}{color=[UIColorOrange]}Créditos" xalign 0.5 line_spacing 40
                text "{size=+5}{color=[UIColorOrange]}Escrita e Edição" xalign 0.5 line_spacing 20
                text "Escrito por Awoo, Kangarube, MinoAnon e {a=https://nemo0690.sofurry.com/}Nemo0690{/a}."
                text "Escrita adicional por {a=https://www.furaffinity.net/user/meestline/}mystline{/a} e nanoff."
                text "{size=+5}{color=[UIColorOrange]}Programação e Arte" xalign 0.5 line_spacing 20
                text "{a=https://twitter.com/nanoff94}Nanoff{/a}"
                text "{size=+5}{color=[UIColorOrange]}Agradecimentos" xalign 0.5 line_spacing 20
                text "{a=https://twitter.com/alephinexile}Aleph (@alephdraws){/a}"
                text "{a=https://eddio.itch.io/killigans-treasure}Eddio (@gleeksunstroke and @killigansdev){/a}"
                text "{a=https://twitter.com/erniemesh}Erniemesh (@erniemesh){/a}"
                text "{a=https://gigasaddle.itch.io/pervader}GigaSaddle (@GigaSaddle){/a}"
                text "{a=https://harmoyena.itch.io/beyond-the-harbor}Harmonious (@Harmoyena){/a}"
                text "{a=https://roddorod.itch.io/nerus}Roddorod (@nerusvn){/a}"
                text "{a=https://squawks.itch.io/revenir}Squawks (@squawksdev){/a}"
                text "{a=https://stormsingerstudios.itch.io/santa-lucia}ZanderWolfie (@stormsingerdev){/a}"
                text "Orikson"
                text "Dacu"
                text "Kopten"
                text "AWthor"
                text "arSyx"
                text "Wattson"
                text "{size=+5}{color=[UIColorOrange]}Agradecimentos Especiais" xalign 0.5 line_spacing 20
                text "Em particular, gostaríamos de oferecer nossa sincera gratidão a:"
                text "{a=https://www.youtube.com/channel/UCTjX0_ahxJwbZqEbrtTrnQA}Lina Palera{/a}, que tão caridosamente licenciou sua performance do Epitáfio de Sícilo sob a Creative Commons, {a=https://luthieros.com/}Luthieros{/a} por seu trabalho na reconstrução da lira antiga e {a=https://lyreacademy.com/}LyreAcademy{/a} por seus recursos educacionais sobre o assunto."
                text "Suas contribuições para a preservação da cultura antiga são uma inspiração para todos nós. Se jogar Hotel Minotauro deu a você uma apreciação ao som da lira, considere apoiar o trabalho inestimável deles."
                text "{size=+10}{color=[UIColorOrange]}Licenciamento" xalign 0.5 line_spacing 40
                text "Direitos Autorais© 2021 por Minoh Workshop. Todos os direitos reservados sob Convenções Internacionais de Direitos Autorais."
                text "{size=+5}{color=[UIColorOrange]}Música" xalign 0.5 line_spacing 20
                text "Salvo mediante especificação, todas as músicas foram editadas no Audacity para equalizar o volume para a melhor experiência do usuário."
                text "{a=https://freemusicarchive.org/music/Lina_Palera_Lyre_20_Project_player/An_Appreciation/01_Seikilos_Epitaph_with_the_Lyre_of_Apollo}\"Seikilos Epitaph with the Lyre of Apollo\"{/a}, por {a=https://freemusicarchive.org/music/Lina_Palera_Lyre_20_Project_player}Lina Palera (Lyre 2.0 Project Player){/a}, Álbum {a=https://freemusicarchive.org/music/The_Music_of_Ancient_Greece/An_Appreciation}\"An Appreciation\"{/a}, {a=https://creativecommons.org/licenses/by-nc-sa/3.0/}disponível sobre Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0){/a}."
                text "Este trabalho foi modificado para ter um comprimento menor."
                text "\"Ariadne's Thread\" e \"Asterion\" foram compostas e performadas por {a=https://stormsingerstudios.itch.io/}Stormsinger Studios{/a}, que graciosamente nos permitiu utilizá-las em Hotel Minotauro."
                text "Confira o jogo mais recente deles, {a=https://stormsingerstudios.itch.io/santa-lucia}Santa Lucia, disponível de graça no Itch.io{/a}."
                text "O autor possui todos os direitos sobre as músicas Ariadne's Thread e Asterion. Não estão sob uma licença Creative Commons. Ariadne's Thread e Asterion não foram modificados."
                text "{a=http://ilicensemusic.com/sku/berkman-heartstrings}\"Lullaby\"{/a} por Daniel Berkman do álbum \"Heartstrings\"."
                text "{a=http://ilicensemusic.com/sku/dgilden-ancestral}\"Crossing The Astral Bridge\", \"Island Journey\" e \"Kora Duet\"{/a} por David Gilden do álbum \"Ancestral Voices\"."
                text "{a=http://ilicensemusic.com/sku/dgilden-diststrings}\"Greek Folk Song\"{/a} por David Gilden do álbum \"Distant Strings\"."
                text "{a=http://ilicensemusic.com/sku/dgilden-jato}\"Jato (The Lion)\"{/a} por David Gilden do álbum \"Jato the Lion\"."
                text "{a=http://ilicensemusic.com/sku/jilin-lastdayofsummer}\"The Sorrow\"{/a} por Andrew Jilin do álbum \"Last Day of Summer\"."
                text "{a=http://ilicensemusic.com/sku/rayborn-qadim}\"Calliopeia - kithara (Ancient Greek)\"{/a} por Tim Rayborn do álbum \"Qadim\"."
                text "{a=http://ilicensemusic.com/sku/raymontford-fragile}\"When Darkness Takes Flight\"{/a} por Ray Montford do álbum \"A Fragile Balance\"."
                text "{a=http://ilicensemusic.com/sku/bbunkertrio-bbunkertrio}\"Solidarity\", \"Aberdeen Done It\" e \"Vindaloo Blues\"{/a} por Brian Bunker Trio do álbum \"Brian Bunker Trio\"."
                text "{a=http://ilicensemusic.com/sku/jilin-lastdayofsummer}\"Eagle's Song\"{/a} por Andrew Jilin do álbum \"Last Day of Summer\"."
                text "{a=http://ilicensemusic.com/sku/joesmith-highfidelity}\"Obviously\"{/a} por Joe Smith e os Spicy Pickles do álbum \"High-Fidelity\"."
                text "{a=http://ilicensemusic.com/sku/noisehifi-distortion}\"Red Distortion\"{/a} por Noise HiFi do álbum \"Red Distortion\"."
                text "{a=http://ilicensemusic.com/sku/raymontford-earlysessions}\"May It Begin (acoustic)\"{/a} por Ray Montford do álbum \"The Early Sessions\"."
                text "{a=http://ilicensemusic.com/sku/raymontford-shedyour}\"One Witness\" e \"May It Begin\"{/a} por Ray Montford do álbum \"Shed Your Skin\"."
                text "{a=http://ilicensemusic.com/sku/oliostere-circonflexe}\"2 Virgule 4\"{/a} por Oliostere do álbum \"Circonflexe\"."
                text "Salvo mediante especificação, as músicas foram salvas em qualidade média no formato .mp3 ou .ogg por motivos de armazenamento."
                text "{size=+5}{color=[UIColorOrange]}Considerações de Streaming" xalign 0.5 line_spacing 40
                text "Você está livre para fazer streams, gravar vídeos de Hotel Minotauro e publicá-los em plataformas como Youtube e Twitch. Tenha em mente, entretanto, que Hotel Minotauro usa músicas licenciadas por meio do iLicenseMusic, que podem acionar sistemas automatizados de identificação de direitos autorais."
                text "Não podemos garantir que os detentores dos direitos autorais das músicas autorizarão a monetização de vídeos contendo suas obras. Caso você tenha problemas se tratando disso, recomendamos que você grave o jogo com o volume da música no zero."
                text "{size=+5}{color=[UIColorOrange]}Fontes" xalign 0.5 line_spacing 20
                text "Hotel Minotauro utiliza a fonte Junicode, disponibilizada sob a SIL Open Font License, Version 1.1, de acordo com as especificações da licença."
                text "Além disso, utiliza {a=https://opendyslexic.org/}OpenDyslexic{/a}, disponibilizada sob a SIL Open Font License (OFL)."
                text "{size=+5}{color=[UIColorOrange]}Imagens" xalign 0.5 line_spacing 20
                text "Salvo mediante especificação, as imagens de fundo utilizadas em Hotel Minotauro vêm de {a=https://pixabay.com/}Pixabay{/a}."
                text "{a=https://commons.wikimedia.org/wiki/File:Staircase_of_the_abandoned_Central_Hotel_in_Annan,_Scotland_(DSCF8956).jpg}Staircase of the abandoned Central Hotel in Annan, Scotland{/a}, tirada por {a=https://commons.wikimedia.org/wiki/User:Trougnouf}Trougnouf (Benoit Brummer){/a}, {a=https://creativecommons.org/licenses/by-sa/4.0/deed.en}disponível sob Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).{/a}"
                text "{a=https://commons.wikimedia.org/wiki/File:Tarnow_hotel_Tarnovia.jpg}Tarnów - Tarnovia hotel{/a}, por {a=https://commons.wikimedia.org/wiki/User:Andrzej_O}Andrzej Otrębski{/a}, {a=https://creativecommons.org/licenses/by-sa/3.0/deed.en}disponível sob Attribution-ShareAlike 2.0 Unported License (CC BY-NC-SA 2.0).{/a}"
                text "{a=https://ccsearch.creativecommons.org/photos/e2e57bd9-dba7-4291-b66f-6a85527106eb}SoCal5{/a}, por {a=https://www.flickr.com/photos/48929940@N00}Rich Aten{/a}, {a=https://creativecommons.org/licenses/by-nc-sa/2.0/}disponível sob Attribution-ShareAlike 3.0 Unported License (CC BY-SA 3.0).{/a}"
                text "{size=+5}{color=[UIColorOrange]}Efeitos Sonoros" xalign 0.5 line_spacing 20
                text "{a=https://freesound.org/people/JuliusMabe/sounds/445196/}Creature Moan.wav{/a}, por {a=https://freesound.org/people/JuliusMabe/}JuliusMabe{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 3.0 Unported License (CC BY 3.0).{/a}"
                text "{a=https://freesound.org/people/franskedelight/sounds/94639/}Phone 093 - Silly phone call.wav{/a}, por {a=https://freesound.org/people/franskedelight/}franskedelight{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 3.0 Unported License (CC BY 3.0).{/a}"
                text "{a=https://freesound.org/people/Cabeeno%20Rossley/sounds/175039/}Cellphone, phone vibrate.wav{/a}, por {a=https://freesound.org/people/Cabeeno%20Rossley/}Cabeeno Rossley{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 3.0 Unported License (CC BY 3.0).{/a}"
                text "{a=https://freesound.org/people/klankbeeld/sounds/248148/}reverberating wood-metal sound.wav{/a}, por {a=https://freesound.org/people/klankbeeld/}klankbeeld{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 3.0 Unported License (CC BY 3.0).{/a}"
                text "{a=https://freesound.org/people/jodybruchon/sounds/459460/}Beeps - cell phone answer chirp.wav{/a}, por {a=https://freesound.org/people/jodybruchon/}judybruchon{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 1.0 Universal License (CC0 1.0).{/a}"
                text "{a=https://freesound.org/people/MilanKovanda/sounds/377053/}Displacement Chair{/a}, por {a=https://freesound.org/people/MilanKovanda/}MilanKovanda{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 1.0 Universal License (CC0 1.0).{/a}"
                text "{a=https://freesound.org/people/hellska/sounds/328727/}flute_note_tremolo.wav{/a}, por {a=https://freesound.org/people/hellska/sounds/328727/}hellska{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 1.0 Universal License (CC0 1.0).{/a}"
                text "{a=https://freesound.org/people/rebeat/sounds/128262/}Dish Rustling_2.aif{/a}, por {a=https://freesound.org/people/rebeat/}rebeat{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 1.0 Universal License (CC0 1.0).{/a}"
                text "{a=https://freesound.org/people/Jerimee/sounds/434784/}ominous.wav{/a}, por {a=https://freesound.org/people/Jerimee/}Jerimee{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 1.0 Universal License (CC0 1.0).{/a}"
                text "{a=https://freesound.org/people/16FPanskaLipovska_Katerina/sounds/497945/}Glass clinking.WAV{/a}, por {a=https://freesound.org/people/16FPanskaLipovska_Katerina/}16FPanskaLipovska_Katerina{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 1.0 Universal License (CC0 1.0).{/a}"
                text "{a=https://freesound.org/people/InspectorJ/sounds/416179/}Book, Flipping Through Pages, A.wav{/a}, por {a=https://freesound.org/people/InspectorJ/}InspectorJ{/a}, via {a=https://freesound.org/}Freesound.org{/a}, {a=https://creativecommons.org/licenses/by/3.0/}disponível sob Attribution 3.0 Unported License (CC BY 3.0).{/a}"
                text "{a=https://stormsingerstudios.itch.io/}Asterion's Chord, por Stormsinger Studios{/a}. Todos os direitos reservados."
                text "{size=+10}{color=[UIColorOrange]}Software" xalign 0.5 line_spacing 20
                text "Feito com {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"


        vbar value YScrollValue("vp")
