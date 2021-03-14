###################################################################
#                        REWARD SCENES
###################################################################

#The following scenes are triggered by obtaining a team reward

label teamRewards:

    #"End of day, checking team rewards"
    if UI_permissions['rd']:
        scene Bedrock
        $show_team(rd_team_names())
        $pose_team(rd_team_names(), 'neutral')
        with Dissolve(1.0)
        "Vamos verificar a equipe de P&D."
        if len(rd_team_names())==0:
            "Ah? Parece que ninguém está aqui.
            Sua equipe de P&D não fez nenhum progresso."
        else:
            $reward=determine_rd_reward(rewards, inventory, guests, relationships)
            $accumulate_rd_stats()
            if reward == 'none':
                "Sua equipe de P&D fez algum progresso, mas nenhum projeto foi concluído."
            else:
                if build < 4 or is_essential(reward):
                    $pose_team(rd_team_names(), 'victory')
                    "Ah? Parece que você concluiu um projeto!"
                    $ renpy.jump('RDReward_' + reward)
                else:
                    $pose_team(rd_team_names(), 'victory')
                    "Sua equipe atual pode concluir um projeto!
                    Você quer concluir sua pesquisa ou continuar trabalhando na direção de outra coisa?"
                    $myChoices = rewards.get_reward_choices(inventory.accumulated_stats['RD'] + calculate_rd_team_stats(), inventory.raw_materials)
                    $narrator("Gastar sua pesquisa?", interact=False)
                    $result = renpy.display_menu(myChoices)
                    if result == 'none':
                        $pose_team(rd_team_names(), 'neutral')
                        "A equipe manterá seu progresso e trabalhar em outros projetos."
                    else:
                        $ renpy.jump('RDReward_' + result)

    #we return here after the scene with the reward we just claimed
    label RDrewardcheck:

    if UI_permissions['exploration']:
        scene bg valley
        $show_team(exploration_team_names())
        $pose_team(exploration_team_names(), 'neutral')
        with Dissolve(1.0)
        "Vamos verificar a equipe de exploração."
        if len(exploration_team_names())==0:
            "Bem... ninguém foi enviado para o labirinto."
        else:
            if team_in_danger():
                jump danger
            else:
                label EXreward:
                if calculate_exploration_team_stats().get_value("Surveying") >=1:
                    $survey_label = survey()
                    if survey_label !='none':
                        $ renpy.jump("survey_" + survey_label)
                label returnEX:
                $reward=determine_exploration_reward(rewards, inventory, guests, relationships)
                $accumulate_exploration_stats()
                if reward == 'none':
                    $pose_team(exploration_team_names(), 'neutral')
                    if calculate_exploration_team_stats().get_value("Surveying") >=1:
                        "Fora isto, sua equipe de exploração não fez nenhuma grande descoberta."
                    else:
                        "Sua equipe de exploração não encontrou nada."
                else:
                    $pose_team(exploration_team_names(), 'victory')
                    if calculate_exploration_team_stats().get_value("Surveying") >=1:
                        "Ah? Parece que você encontrou alguma outra coisa!"
                    else:
                        "Parece que sua equipe encontrou alguma coisa!"
                    $ renpy.jump('EXReward_' + reward)
        #we return here after the scene with the reward we just claimed
    label EXrewardcheck:
    $hide_team(rd_team_names())
    #both teams are done. we return to the day the team processing was called from.
    $ renpy.jump(nextLabel)


label danger:
    #Your team fucked up and is in danger.
    $pose_team(exploration_team_names(), 'defeat')
    "A equipe de exploração relata suas descobertas.\n
    Eles foram atacados por uma criatura nas profundezas do Labirinto."
    $RNJesus = renpy.random.randint(1, 100)
    if player_background == "speedrunner" and RNJesus <= 40:
        $loot = calculate_exploration_team_stats().get_value("Surveying")
        $pose_team(exploration_team_names(), 'victory')
        "No entanto... de alguma forma, sua equipe conseguiu sair ilesa.
        Não apenas isto, eles conseguiram saquear [loot] matérias-primas da criatura!"
        "Algumas pessoas atribuiriam isto a pura sorte ou intervenção divina.
        Na sua cabeça, seus anos gastos aperfeiçoando gerenciamento de recursos e
        suas habilidades épicas e instintos de gamer foram a verdadeira chave para o sucesso."
        $inventory.raw_materials +=loot
    else:
        if danger_attack():
            #if you got attacked but avoided it successfully you can still claim a reward
            #if someone got injured you jump straight to the end
            jump EXrewardcheck
    jump EXreward

#survey extra rewards
label survey_Cool:
    "Isto é um exemplo de uma cena extra que acontece quando você acaba sendo muito sortudo durante inspeções."
    jump returnEX


label RDReward_WiFi:

    scene Bedrock
    show Greta:
        xalign 0.5 yalign 1.1 zoom 1.0 xzoom 1
    with Dissolve(1.0)

    #You are accosted by Greta.

    show Greta:
        ease 0.3 yalign 1.0
        ease 0.3 yalign 1.1

    "Greta" "[player_name]!{w=0.2} [player_name]! É maravilhoso, todo mundo está se divertindo!"

    you "Ah, oi Greta. O que está acontecendo, a Internet está funcionando?"

    pause 1.0

    show Greta:
        ease 1.0 xalign 0.45

    "Greta" "...Internet?"

    pause 1.0
    show Greta:
        ease 0.5 xalign 0.5

    "Greta" "Ah, sim!{w=0.2} A Internet, que boba, como eu podia esquecer.{w=0.2}
    Está funcionando, conseguimos, mas isso nem é o melhor."

    "Greta" "Toda essa experiência aqui me deu tantas ideias incríveis,
    tantas visões maravilhosas para pesquisa!{w=0.2} Eu escrevi um documento destacando algumas
    delas e mostrei a todo mundo!"

    show Greta:
        ease 0.3 yalign 1.0
        ease 0.3 yalign 1.1
    "Greta" "Eles estão todos tão maravilhados com isso,{w=0.2} não conseguem nem captar mais de uma
    ou duas ideias antes de precisar de uma pausa!"

    "Greta" "Ah, é lindo, [player_name]!{w=0.2} Todo mundo lá no
    departamento de engenharia vai ficar com tanta inveja!"

    you "Isso...{w=0.3} isso é ótimo, Greta.{w=0.2} Fico feliz em ouvir isso.{w}
    I'm sure everyone will love your...{w=0.3} ideas."

    you "Então, presumo que tudo esteja no lugar e funcionando?"

    show Greta:
        ease 0.3 yalign 1.0
        ease 0.3 yalign 1.1
    "Greta" "Sim, absolutamente!{w=0.5}... Mais ou menos."

    "Greta" "Nós... nós conseguimos fazer o wi-fi funcionar,{w=0.2} mas teve uma grande confusão sobre
    como conseguir um provedor de serviços de internet e..."

    show Greta:
        xzoom -1
        ease 1.0 xalign 0.4

    "Greta" "Podemos estar...{w=0.5}ha ha...{w=0.5} podemos estar usando o provedor de internet
    para o qual os uruguaios trabalham, ok?"

    show Greta:
        xzoom 1
        ease 1.0 xalign 0.5
    "Greta" "Então, as coisas são bem improvisadas nesse sentido, sabe.{w=0.2}
    A banda larga é muito limitada.{w} Mas funciona!{w=0.2} Está tudo em ordem."

    "Greta" "...Mas se algo der errado, receio não ter a menor ideia de como consertar, haha."

    "Greta" "Eu não sou uma engenheira de redes. Dá um tempo, ok?"

    "Greta" "Você pode querer enviar um e-mail à central de vez em quando,{w=0.2}
    e também vai ter que pagar as contas.{w} Mas tenho certeza que vai ser fácil para você,{w=0.2}
    com um hotel mágico e tudo."

    "Greta" "Me dá um minuto,{w=0.2} estamos fazendo um teste de estresse aqui,{w=0.2} já volto com você."

    show Greta:
        xzoom -1
        ease 2.0 xalign -1.3
    pause 2.0

    $show_team(rd_team_names())
    $pose_team(rd_team_names(), 'victory')
    with Dissolve(1.0)


    $throwaway1 = list_into_text(rd_team_names())

    "You approach [throwaway1]."

    if 'Luke' in rd_team_names():
        $Luke.change("emotion", "laughing")
        $Luke.change("arm", "pointing")
        luke "É isso aí!{w=0.2} Olha essa merda, [player_name]!"

        $Luke.change("emotion", "cocky")
        show Luke:
            ease 1.0

        "Luke quase enfia o telefone na sua cara. Já viu dias melhores: as laterais estão
        amassadas e a tela está rachada e toda arranhada, dificultando sua leitura."

        "Na verdade, agora mesmo as garras de Luke estão adicionando novos arranhões apenas por segurá-lo."

        "No entanto, você consegue distinguir {i}um monte{/i} de nofiticações na parte superior da tela,
        e uma conversa toda em letras maiúsculas que Luke está tendo com um contato apelidado de \"Mainha\", seguido
        por uma dose saudável de emojis de coração."

        $Luke.change("arm", "hip")
        show Luke:
            ease 1.0

    if 'Kota' in rd_team_names():
        $Kota.change("emotion", "happy")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "relaxed")

        kota "Não é uma notícia empolgante, senhor [player_name]?"

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        if 'Kota' == first_guest:
            kota "Eu não uso muito meu celular, mas ser capaz de procurar receitas para atender aos clientes
            do mundo todo é definitivamente uma dádiva para qualquer restaurante."
        else:
            kota "Eu não uso muito meu celular, mas tenho certeza que isto fará a estadia dos
            hóspedes ser mais agradável."

    if 'Asterion' in rd_team_names():
        $ global_affection += 1
        $Asterion.change("emotion", "laughing")

        asterion "Conseguimos, Mestre."

        $Asterion.change("emotion", "contemplative")
        asterion "Bem... eu não fiz muito além de explicar como escrever contratos e me
        certificar de que tudo estava em ordem, os outros fizeram o trabalho pesado.{w=0.2}
        Mas estou feliz por ter sido capaz de ajudar."

    #Since we have a contingency scene to give the player the WiFi reward anyway, it would be
    #unfair if they wasted time getting wifi the way they were intended to, so let's throw them a bone.

    python:
        myList = list()
        for member in rd_team_names():
            myList.append((member, guests.get_guest_stats(member).get_value('Tech')))
        myList.sort(key=lambda x: x[1])
        myList = myList[0][0]

    if myList == 'Asterion':
        $Asterion.change("emotion", "smiling")
        asterion "Greta foi muito útil explicando-me estes conceitos ao longo
        das sessões.{w=0.2} Sinto que me atualizei com alguns dos avanços que perdi
        nessas últimas décadas."
        $Asterion.change("emotion", "contemplative")
        asterion "Eu... ainda sinto que precisarei de sua ajuda para aprender mais, Mestre,
        mas já me sinto mais confiante em minha habilidade."

    elif myList == 'Kota':
        $Kota.change("emotion", "happy")
        kota "Ah, e é claro, dona Greta tem sido muito atenciosa."

        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        $Kota.change("emotion", "neutral")
        kota "Eu insisti que não era necessário, mas como eu era a pessoa menos informada
        no cômodo, ela me pôs a par de muitos desses assuntos."

        $Kota.change("rightarm", "relaxed")
        kota "Tenho esperança de que serei mais útil no futuro."

    elif myList == 'Luke':
        $Luke.change("emotion", "laughing")
        luke "Também,{w=0.2} rapaz,{w=0.2} retiro tudo o que eu disse sobre os
        alemães. Greta foi uma mão na roda a tarde inteira explicando toda essa baboseira
        pra mim,{w=0.2} {i}quase{/i} faz sentido agora."

        $Luke.change("emotion", "wink")
        luke "Se você precisar de uma mão pra mexer nessas coisas no futuro,
        acho que posso ajudar um pouco aqui e ali."

    play sound "sfx/asterionchord.mp3"
    $guests.increase_guest_stat(myList, "Tech", 1)
    "O atributo de {color=[UIColorTech]}Tecnologia{/color} de [myList] aumentou em 1!"

    you "Isso é uma ótima notícia.{w=0.2} Então, devo tentar fazer login?"

    #one of the team at random shows you how to log in
    $throwaway2 = rd_team_names()[renpy.random.randint(1, len(rd_team_names()))-1]

    if throwaway2 == 'Asterion':
        $Asterion.change("emotion", "smiling")
        asterion "Sim,{w=0.2} hã,{w=0.2} deixe-me ver se consigo lembrar das instruções..."

        asterion "A \"rede\" é {i}’Hotel Minotauro’{/i}."
        $Asterion.change("emotion", "tired")
        asterion "E a senha é..."

        "Astério pensa por alguns segundos com uma expressão tensa,
        mas então apenas aponta na direção de uma tira de papel sobre a mesa."

        "Você a pega e nela está contido:"

        contract "Senha: Netzwerkdurchsetzungsgesetz"

        you "Ok,{w=0.2} vamos ter que mudar isso."

        asterion "Seria bom.{w=0.2} Ela detalhou cuidadosamente como fazer isto
        em um destes documentos."

    elif throwaway2 == 'Luke':
        $Luke.change("emotion", "annoyed")
        luke "Bem, você pode tentar.{w=0.2} A rede é {i}\"Hotel Minotauro\"{/i},{w=0.2}
        mas a senha é uma desgraça de palavra alemã doida que é impossível de se lembrar."

        $Luke.change("arm", "pointing")
        "Luke mostra a senha para você em uma nota em seu celular.{w=0.2} Você consegue ler,
        apesar das marcas de garras e rachaduras na tela que tornam quase impossível fazer isso."

        contract "Senha: Netzwerkdurchsetzungsgesetz"

        you "Ok,{w=0.2} vamos ter que mudar isso."

        $Luke.change("arm", "hip")
        $Luke.change("emotion", "neutral")
        luke "Né?{w=0.2} Ela deixou algumas instruções de como fazer isso, felizmente."

    elif throwaway2 == 'Kota':
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        $Kota.change("emotion", "happy")
        kota "Pois bem. Você não terá problema algum para encontrar a rede, uma vez que é a única.
        Chama-se {i}\"Hotel Minotauro\"{/i}."

        $Kota.change("rightarm", "relaxed")
        kota "Quanto à senha, bem, é...{w=0.3} Espero estar dizendo isso direito...
        {w=0.3} Netzwerkdurchsetzungsgesetz."

        you "Desculpa,{w=0.2} é o que?"

        $Kota.change("emotion", "sad")
        "Kota suspira e lhe entrega um pedaço de papel. Está escrito em tinta roxa brilhante,
        com o que você supõe ser a caligrafia de Greta."

        contract "Senha: Netzwerkdurchsetzungsgesetz"

        you "Ok,{w=0.2} vamos ter que mudar isso."

        $Kota.change("emotion", "neutral")
        kota "Sim, parece prudente fazer isto.{w=0.2} Ela foi gentil o suficiente para
        deixar instruções sobre como fazer."

    you "Então, Hotel Minotauro.{w} Ok, é memorável e direto ao ponto, suponho."
    play sound "sfx/vibratephone.mp3"
    "Você faz o login e, pela primeira vez em muito tempo, seu ícone de wi-fi acende."
    stop sound
    $obtain_reward('WiFi', 'RD')
    $add_file('Tech', "WiFi")

    play sound "sfx/asterionchord.mp3"
    "Você conseguiu estabelecer {color=[UIColorOrange]}acesso à internet{/color} no hotel.
    Você pode ver seus projetos de tecnologia concluídos na guia de tecnologia
    na tela {color=[UIColorOrange]}Arquivos{/color} no menu de pausa."

    if len(exploration_team_names()) > 0:
        "A animação no cômodo é palpável, mas você tem outras responsabilidades a cumprir.
        Você parabeniza a equipe pelo trabalho bem feito e vai verificar a equipe de exploração."
    else:
        "A animação no cômodo é palpável. Você parabeniza a equipe pelo trabalho bem feito
        e fica com eles por um tempo para comemorar."

    jump RDrewardcheck


label RDReward_Contract1:
    "This is the scene that plays when the first contract is crafted.
    This is super optional, but if you want to come up with a first contract i'm all for it."
    $obtain_reward('Contract1', 'RD')
    jump RDrewardcheck


label RDReward_Contract2:
    "This is the scene that plays when the second contract is crafted."
    $obtain_reward('Contract2', 'RD')
    jump RDrewardcheck


label RDReward_Satellite:
    "This is the scene that plays when the sattelite is assembled."
    jump RDrewardcheck

label EXReward_Tablet1:
    $add_file('Memento', "Tablet1")
    "Você encontrou uma tábua de argila narrando a jornada de um filho devoto a Creta.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet1', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet2:
    $add_file('Memento', "Tablet2")
    "Você encontrou uma tábua de argila.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet2', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet3:
    $add_file('Memento', "Tablet3")
    "You obtained a clay tablet narrating a rare audience with an ancient king.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet3', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet4:
    $add_file('Memento', "Tablet4")
    "You obtained a clay tablet narrating an intervention from a concerned youth.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet4', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet5:
    $add_file('Memento', "Tablet5")
    "You obtained a clay tablet narrating a man's encounter with one of divine nature.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet5', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet6:
    $add_file('Memento', "Tablet6")
    "You obtained a clay tablet revealing a child's hospitality.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet6', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet7:
    $add_file('Memento', "Tablet7")
    "You obtained a clay tablet narrating a small tragedy of human folly.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet7', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet8:
    $add_file('Memento', "Tablet8")
    "You obtained a clay tablet depicting a scene of treachery.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet8', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet9:
    $add_file('Memento', "Tablet9")
    "You obtained a clay tablet narrating a small tragedy of human folly.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet9', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet10:
    $add_file('Memento', "Tablet10")
    "You obtained a clay tablet revealing a bastard tempting a pious youth away from his duty.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet10', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet11:
    $add_file('Memento', "Tablet11")
    "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet11', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet12:
    $add_file('Memento', "Tablet12")
    "You obtained a clay tablet revealing a hybrid's foul nature.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet12', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet13:
    $add_file('Memento', "Tablet13")
    "You obtained a clay tablet revealing the hybrid's despondency.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet13', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet14:
    $add_file('Memento', "Tablet14")
    "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet14', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet15:
    $add_file('Memento', "Tablet15")
    "You obtained a clay tablet revealing a prisoner's last shred of hope.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet15', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet16:
    $add_file('Memento', "Tablet16")
    "You obtained a clay tablet depicting a crime against divine order.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet16', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet17:
    $add_file('Memento', "Tablet17")
    "You obtained a clay tablet revealing a prisoner's liberation.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet17', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet18:
    $add_file('Memento', "Tablet18")
    "You obtained a clay tablet revealing an ominous fate.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet18', 'Exploration')
    jump EXrewardcheck

label EXReward_TypewriterScrap:
    $add_file('Memento', "TypewriterScrap")
    "You encountered a very old crumpled piece of paper: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('TypewriterScrap', 'Exploration')
    jump EXrewardcheck

label EXReward_PoemNotebook:
    $add_file('Memento', "PoemNotebook")
    "You encountered a tiny, goatskin-bound notebook, containing handwritten poetry.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('PoemNotebook', 'Exploration')
    jump EXrewardcheck

label EXReward_RockCarving:
    $add_file('Memento', "RockCarving")
    "You found a petroglyph: writing engraved into a slab of rock.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('RockCarving', 'Exploration')
    jump EXrewardcheck

label EXReward_Agape:
    $add_file('Memento', "Agape")
    "You found a poem written in very old parchment: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Agape', 'Exploration')
    jump EXrewardcheck

label EXReward_FieldWork:
    $add_file('Memento', "FieldWork")
    "You found an old page torn off a book: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('FieldWork', 'Exploration')
    jump EXrewardcheck

label EXReward_FoldedNote:
    $add_file('Memento', "FoldedNote")
    "You found an old page torn off a book: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('FoldedNote', 'Exploration')
    jump EXrewardcheck

label EXReward_Selene:
    $add_file('Memento', "Selene")
    "You found a handwritten poem: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Selene', 'Exploration')
    jump EXrewardcheck





label EXReward_Wine:
    $inventory.remove_item('Bundle')
    you "So... how’d that go?"

    if 'Luke' in exploration_team_names() and 'Kota' not in exploration_team_names():
        $throwaway1 = 'we' if 'Asterion' in exploration_team_names() else 'I'
        luke "[player_name],{w=0.2} [throwaway1] fucking did it.{w=0.2} Mission accomplished, pardner!"

        you "Really?{w} You sure you did it right?"

        $Luke.change("arm", "pointing")

        luke "Oh, you can bet the farm on it.{w=0.2} Just followed the instructions:
        walked south and saw the plateau with a couple statues on top. It was impossible to miss, really!"

        $Luke.change("arm", "hip")
        $Luke.change("emotion", "neutral")

        if 'Asterion' in exploration_team_names():
            $Asterion.change("emotion", "sad")
            luke "Now, when we got to the top, there were two statues:{w=0.2} a buff dude on a throne
            and a chick with a spear, shield and funny helmet on it."

            luke "Y’see I was gonna go with the spear lady,{w=0.2} because she looked like those old
            timey propaganda posters with the chick draped in the flag and shit.{w} Very vintage, you know?"

            $Luke.change("emotion", "annoyed")
            luke "But Asterion convinced me otherwise and,{w=0.2} hey,{w=0.2} I’ll trust what he says
            on these matters.{w} Besides, I had to throw the guy a bone, boss,{w=0.2}
            he looked fucking miserable the entire way there."
            $BundleSacrifice = 'Zeus'

            $Asterion.change("emotion", "tired")
            luke "Not to mention the legless crawling lady things didn’t leave him alone."

            you "You mean like the one that jumped at me?"
            $Luke.change("arm", "pointing")

            $Asterion.change("emotion", "sad")
            luke "Bingo.{w=0.2} Now, I was doing fine, you know,{w=0.2} half bird and all.{w}
            I’m light on my feet{w=0.2} — but, man, Asterion just had the worst fucking time.{w=0.2}
            Those things went ballistic whenever they saw him. "

            $Luke.change("arm", "hip")
            luke "I know we’re kinda tight on time for that bottle thing, but please,{w=0.2}
            next time spare the guy."

        else:
            luke "Now, when I got to the top, there were two statues:{w=0.2} a buff dude on a throne
            and a chick with a spear, shield and funny helmet on it."

            luke "The dude on the throne looked {i}good{/i},{w=0.2} let me tell you,{w=0.2} so I was
            gonna burn the thingy at his feet like a good boy."

            $Luke.change("emotion", "horny")
            luke "But...{w=0.2} I don’t know,{w=0.2} call me a softy, but the chick got me nostalgic,
            you know?{w} She looked like those old timey propaganda posters with the lady draped in
            the flag and shit."

            $Luke.change("arm", "salute")
            luke "It’s cheesy, I know, but I...{w=0.2} well, I put the bundle in front of her, lit it on fire,
            and did a little salute."
            $BundleSacrifice = 'Athena'

            $Luke.change("emotion", "surprise")
            luke "It was fucking scary, though.{w=0.2} On my way back the place was crawling with these weird
            legless lady things."

            you "You mean like the one that jumped at me?"

            $Luke.change("arm", "pointing")
            $Luke.change("emotion", "neutral")
            luke "Bingo.{w=0.2} Thankfully I’m light on my feet — you know,{w=0.2} half bird and all,{w=0.2}
            so I’m here in one piece."

        $Luke.change("arm", "pointing")
        $Luke.change("emotion", "cocky")
        luke "But what’s important is, go show that snake who’s boss, will ya?"

    elif 'Luke' not in exploration_team_names() and 'Kota' in exploration_team_names():
        $throwaway1 = 'We' if 'Asterion' in exploration_team_names() else 'I'

        kota "Mister [player_name], I’ll have you know that the task at hand is complete."

        you "That’s fantastic! Did you burn it in the right place?"
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        kota "Well, there wasn’t much of a margin for error.{w=0.2} The instructions were very clear."

        $Kota.change("rightarm", "relaxed")
        $Asterion.change("emotion", "sad")
        kota "[throwaway1] walked south until we saw a small plateau with some large statues
        on top of it,{w=0.2} then followed the path to the top."

        if 'Asterion' in exploration_team_names():
            kota "So, atop the plateau there were two statues.
            According to Asterion they represent Zeus and Athena."

            $Kota.change("emotion", "puzzled")
            $Kota.change("leftarm", "raised")
            kota "Now, I have heard quite a lot of outrageous stories about Zeus,{w=0.2} so I first
            thought about doing a sacrifice to Athena.{w} But Asterion convinced me we should go
            with Zeus instead,{w=0.2} and I will trust his judgement before mine in these matters."
            $BundleSacrifice = 'Zeus'
            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "tired")
            kota "Sadly,{w=0.2} our return was more complicated than our arrival.{w} These...{w=0.3}
            legless,{w=0.2} wailing,{w=0.2} crawling creatures started approaching us."

            $Kota.change("leftarm", "relaxed")
            you "Oh right, one of those jumped at me yesterday."

            $Kota.change("emotion", "puzzled")
            kota "Yes, very unpleasant things.{w=0.2} Thankfully they didn’t come at me all at once."

            kota "Although I should say...{w=0.2} I may not look like it, but I can handle myself in
            a physical altercation, so regardless I wasn't under any peril.{w}
            But I don’t think I can say the same about Mister Asterion."

            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "sad")
            kota "[player_name]...{w=0.2} I must implore you, please refrain from sending
            Asterion to the valley again.{w} It felt like everything there — and I do not just
            refer to just the creatures — was out to get him."

            $Kota.change("emotion", "neutral")
            kota "Thankfully we are both here in one piece and the sacrifice to the Gods is fulfilled.{w=0.2}
            That is what matters."

        else:
            kota "So, atop the plateau there were two statues which...{w=0.2} based on my knowledge on Greek
            deities should represent Zeus and Athena."

            $Kota.change("emotion", "puzzled")
            $Kota.change("leftarm", "raised")
            kota "Now, I have heard quite a lot of outrageous stories about Zeus, so I
            put the bundle at Athena’s feet.{w=0.2} I burned it, recited a small prayer,
            and went on my merry way."
            $BundleSacrifice = 'Athena'
            $Kota.change("emotion", "sad")
            kota "...Which is what I would like to say but there was nothing merry about my return at all.{w}
            On my way back these...{w=0.2} legless,{w=0.2} wailing,{w=0.2}
            crawling creatures started approaching me."

            $Kota.change("leftarm", "relaxed")
            you "Oh right, one of those jumped at me yesterday."

            $Kota.change("emotion", "happy")
            kota "Thankfully they didn’t come at me all at once.{w=0.2} I may not look like it,
            but I can handle myself in a physical altercation — still, avoiding conflict is always good."

            kota "Regardless, what matters is: I am here in one piece,
            and the sacrifice to the Gods is fulfilled."

        you "Thank you,{w=0.2} Kota."

        $Kota.change("emotion", "laughing")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        kota "Please, it was the least I could do.{w=0.2} Now, enough chit-chat,
        I believe you have a reward to claim with a certain snake, do you not?"

    elif 'Luke' in exploration_team_names() and 'Kota' in exploration_team_names():
        luke "Actually, boss, not bad. Not bad at all."
        kota "Yes. I… we are happy to inform that the task is done."

        you "That’s great! Did you guys run into any issues?"

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")
        $Asterion.change("emotion", "sad")
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "relaxed")
        kota "Well, not at first."
        $Kota.change("leftarm", "relaxed")
        luke "See, getting to the plateau was the easy part. All we did was walk south and after
        a while we did see the plateau in the distance, you couldn’t miss it."
        $Luke.change("emotion", "annoyed")
        luke "I was expecting the snake to be lying and sending us on a wild goose chase
        but we had no problem getting there."

        if 'Asterion' not in exploration_team_names():
            $Luke.change("emotion", "neutral")
            kota "Atop the plateau there were two statues, which based on my knowledge of Greek
            deities represented Zeus and Athena."
            $Kota.change("emotion", "happy")
            $Luke.change("emotion", "horny")
            luke "It was funny, we just stopped for a second, looked at each other and decided to
            go with the big dude in the throne."
            $BundleSacrifice = 'Zeus'
            you "Well, I’m happy to see you’re both getting along better."
            $Luke.change("emotion", "annoyed")
            $Kota.change("emotion", "sad")
            kota "Well, I would say cooperation became a necessity, because of what happened next."
            $Luke.change("arm", "pointing")
            luke "Yeah, I think that fucking asshole sent us to an ambush, because when we started
            walking back these legless screaming things started crawling toward us."
            you "Oh, yes, I think one of those jumped at me yesterday."
            luke "Yeah, it was spooky shit."
            $Luke.change("arm", "hip")
            kota "Well, thankfully, they didn’t come at us all at once. I am… let’s just say, not
            a good runner, so we had to kick some of those out of our way."
            $Luke.change("emotion", "cocky")
            luke "I’ll be honest, I’m impressed with dragon boy here. Wouldn’t mind going a round
            or two with him."
            pause 1.0
            $Kota.change("emotion", "angry")
            kota "I {i}hope{/i} you mean a fight."
            $Luke.change("emotion", "horny")
            $Luke.change("arm", "pointing")
            luke "Whatever you want to call it."
            $Luke.change("arm", "hip")
            pause 1.0

        else:
            $Luke.change("emotion", "neutral")
            kota "Atop the plateau there were two statues, which Asterion explained represent Zeus
            and Athena. He suggested burning the bundle at the bottom of Zeus’ throne and we all agreed.
            It was a simple task."
            $BundleSacrifice = 'Zeus'
            $Luke.change("emotion", "annoyed")
            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "tired")
            luke "Now the hard part was getting back, because let me tell you, I think that fucking
            asshole sent us to an ambush, because when we started walking back these legless
            screaming things started crawling toward us."
            you "Oh, yes, I think one of those jumped at me yesterday."
            $Luke.change("arm", "pointing")
            luke "Yeah it was spooky shit."
            $Luke.change("arm", "hip")
            $Kota.change("rightarm", "raised")
            kota "Alas, they all went straight for Asterion. Mister [player_name], I know it was
            imperative to get all the help we could get this one time, but please,
            unless it is absolutely necessary, refrain from doing it in the future."

            $Kota.change("rightarm", "relaxed")
            $Asterion.change("emotion", "sad")
            luke "It wasn’t just the creatures, boss. The soil, the grass, the roots, the insects;
            everything was out to get him. He had a miserable time."
            $Luke.change("emotion", "neutral")

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        kota "We’re back in one piece, which is what’s important."
        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "pointing")
        luke "Yeah, now go show that snake who’s boss, will ya?"

    else:
        $Asterion.change("emotion", "sad")
        $Asterion.change("leftarm", "loose")
        $Asterion.change("rightarm", "loose")
        show Asterion:
            ease 0.05 xalign 0.503
            ease 0.05 xalign 0.5
            repeat
        pause 2.0
        asterion "I- I…"
        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")
        asterion "I completed the task, Master."
        pause 1.0
        show Asterion:
            ease 0.05 xalign 0.5
        you "I’m sorry for sending you out. It was the only way to get the bottle."
        $Asterion.change("leftarm", "loose")
        pause 3.0
        $Asterion.change("emotion", "sad")
        "Asterion doesn’t respond. He has a hard time maintaining eye contact with you."
        pause 1.0
        you "I’m sorry."
        pause 2.0
        "After a while, Asterion regains his composure, and slowly bows to you."
        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")
        asterion "Please, Master, don’t be. What matters is that the sacrifice is complete.
        I put the bundle next to a statue of Zeus at the shrine and set it on fire,
        and made it back. That is what matters."
        $BundleSacrifice = 'Zeus'
        pause 1.0
        $Asterion.change("emotion", "tired")
        $Asterion.change("leftarm", "loose")
        asterion "I-I do believe Argos is waiting for you, Master."
        you "Yes, I’ll go meet him right away."

    $obtain_reward('Wine', 'Exploration')
    #$add_file('Artifact', "Wine")
    jump EXrewardcheck

label RandomTabletReward:
    #receive a random tablet reward, can be handed out for completing optional objectives.
    $throwaway2 = ['Tablet1', 'Tablet2', 'Tablet3', 'Tablet4', 'Tablet5', 'Tablet6', 'Tablet7',
                   'Tablet8', 'Tablet9', 'Tablet10', 'Tablet11', 'Tablet12', 'Tablet13',
                   'Tablet14', 'Tablet15', 'Tablet16', 'Tablet17', 'Tablet18']
    $throwaway3 = throwaway2[renpy.random.randint(1, len(throwaway2))-1]
    while rewards.is_obtained(throwaway3):
        $throwaway3 = throwaway2[renpy.random.randint(1, len(throwaway2))-1]
    play sound "sfx/asterionchord.mp3"
    if throwaway3 == 'Tablet1':
        $add_file('Memento', "Tablet1")
        "You obtained a clay tablet narrating a dutiful son's journey to Crete.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet1', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet2':
        $add_file('Memento', "Tablet2")
        "You obtained a clay tablet narrating a cursed family's arrival to Crete.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet2', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet3':
        $add_file('Memento', "Tablet3")
        "You obtained a clay tablet narrating a rare audience with an ancient king.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet3', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet4':
        $add_file('Memento', "Tablet4")
        "You obtained a clay tablet narrating an intervention from a concerned youth.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet4', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet5':
        $add_file('Memento', "Tablet5")
        "You obtained a clay tablet narrating a man's encounter with one of divine nature.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet5', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet6':
        $add_file('Memento', "Tablet6")
        "You obtained a clay tablet revealing a child's hospitality.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet6', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet7':
        $add_file('Memento', "Tablet7")
        "You obtained a clay tablet narrating a small tragedy of human folly.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet7', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet8':
        $add_file('Memento', "Tablet8")
        "You obtained a clay tablet depicting a scene of treachery.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet8', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet9':
        $add_file('Memento', "Tablet9")
        "You obtained a clay tablet narrating a small tragedy of human folly.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet9', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet10':
        $add_file('Memento', "Tablet10")
        "You obtained a clay tablet revealing a bastard tempting a pious youth away from his duty.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet10', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet11':
        $add_file('Memento', "Tablet11")
        "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet11', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet12':
        $add_file('Memento', "Tablet12")
        "You obtained a clay tablet revealing a hybrid's foul nature.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet12', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet13':
        $add_file('Memento', "Tablet13")
        "You obtained a clay tablet revealing the hybrid's despondency.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet13', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet14':
        $add_file('Memento', "Tablet14")
        "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet14', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet15':
        $add_file('Memento', "Tablet15")
        "You obtained a clay tablet revealing a prisoner's last shred of hope.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet15', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet16':
        $add_file('Memento', "Tablet16")
        "You obtained a clay tablet depicting a crime against divine order.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet16', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet17':
        $add_file('Memento', "Tablet17")
        "You obtained a clay tablet revealing a prisoner's liberation.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet17', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet18':
        $add_file('Memento', "Tablet18")
        "You obtained a clay tablet revealing an ominous fate.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet18', 'Exploration', subtract=False)
    $ renpy.jump(nextLabel)


label RDReward_Diary1:
    "This is the scene that plays when the first Argos diary is translated."
    $obtain_reward('Diary1', 'RD')
    jump RDrewardcheck

label RDReward_Diary2:
    "This is the scene that plays when the second Argos diary is translated."
    $obtain_reward('Diary2', 'RD')
    jump RDrewardcheck

label RDReward_Gym:
    "This is the scene that plays when the gym is unlocked. This will give
    Asterion new clothing options."
    $obtain_reward('Gym', 'RD')
    $wardrobe.add("underwear", "gymshorts_blue")
    $wardrobe.add("underwear", "gymshorts_red")
    $wardrobe.add("armwear", "leathergloves")
    $wardrobe.add("clothes", "workout")
    jump RDrewardcheck
