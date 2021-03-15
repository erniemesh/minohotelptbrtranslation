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
    "Você obteve uma tábua de argila narrando a jornada de um filho devoto a Creta.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet1', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet2:
    $add_file('Memento', "Tablet2")
    "Você obteve uma tábua de argila narrando a chegada de uma familia amaldiçoada em Creta.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet2', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet3:
    $add_file('Memento', "Tablet3")
    "Você obteve uma tábua de argila narrando uma rara audiência com um rei antigo.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet3', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet4:
    $add_file('Memento', "Tablet4")
    "Você obteve uma tábua de argila narrando uma intervenção de uma jovem preocupada.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet4', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet5:
    $add_file('Memento', "Tablet5")
    "Você obteve uma tábua de argila narrando o encontro de um homem com outro de natureza divina.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet5', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet6:
    $add_file('Memento', "Tablet6")
    "Você obteve uma tábua de argila revelando a hospitalidade de uma criança.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet6', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet7:
    $add_file('Memento', "Tablet7")
    "Você obteve uma tábua de argila narrando uma pequena tragédia da loucura humana.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet7', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet8:
    $add_file('Memento', "Tablet8")
    "Você obteve uma tábua de argila retratando uma cena de traição.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet8', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet9:
    $add_file('Memento', "Tablet9")
    "Você obteve uma tábua de argila narrando uma pequena tragédia da loucura humana.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet9', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet10:
    $add_file('Memento', "Tablet10")
    "Você obteve uma tábua de argila revelando um bastardo tentando um jovem devoto a se afastar para longe de seu dever.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet10', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet11:
    $add_file('Memento', "Tablet11")
    "Você obteve uma tábua de argila revelando uma das muitas tragédias que levaram à morte de um menino.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet11', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet12:
    $add_file('Memento', "Tablet12")
    "Você obteve uma tábua de argila revelando a natureza suja de um híbrido.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet12', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet13:
    $add_file('Memento', "Tablet13")
    "Você obteve uma tábua de argila revelando o desânimo do híbrido.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet13', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet14:
    $add_file('Memento', "Tablet14")
    "Você obteve uma tábua de argila revelando uma das muitas tragédias que levaram à morte de um menino.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet14', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet15:
    $add_file('Memento', "Tablet15")
    "Você obteve uma tábua de argila revelando o último resquício de esperança de um prisioneiro.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet15', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet16:
    $add_file('Memento', "Tablet16")
    "Você obteve uma tábua de argila retratando um crime contra a ordem divina.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet16', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet17:
    $add_file('Memento', "Tablet17")
    "Você obteve uma tábua de argila revelando a libertação de um prisioneiro.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet17', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet18:
    $add_file('Memento', "Tablet18")
    "Você obteve uma tábua de argila revelando um destino sinistro.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Tablet18', 'Exploration')
    jump EXrewardcheck

label EXReward_TypewriterScrap:
    $add_file('Memento', "TypewriterScrap")
    "Você encontrou um pedaço de papel amassado muito antigo: uma pequena lembrança do passado de Astério.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('TypewriterScrap', 'Exploration')
    jump EXrewardcheck

label EXReward_PoemNotebook:
    $add_file('Memento', "PoemNotebook")
    "Você encontrou um pequeno caderno encadernado em pele de cabra, contendo poesia escrita à mão.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('PoemNotebook', 'Exploration')
    jump EXrewardcheck

label EXReward_RockCarving:
    $add_file('Memento', "RockCarving")
    "Você encontrou um petróglifo: escrita gravada em uma placa de rocha.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('RockCarving', 'Exploration')
    jump EXrewardcheck

label EXReward_Agape:
    $add_file('Memento', "Agape")
    "Você encontrou um poema escrito em um pergaminho muito antigo.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Agape', 'Exploration')
    jump EXrewardcheck

label EXReward_FieldWork:
    $add_file('Memento', "FieldWork")
    "Você encontrou uma página velha arrancada de um livro: uma pequena lembrança do passado de Astério.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('FieldWork', 'Exploration')
    jump EXrewardcheck

label EXReward_FoldedNote:
    $add_file('Memento', "FoldedNote")
    "Você encontrou uma nota dobrada: uma pequena lembrança do passado de Astério.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('FoldedNote', 'Exploration')
    jump EXrewardcheck

label EXReward_Selene:
    $add_file('Memento', "Selene")
    "Você encontrou um poema escrito à mão: uma pequena lembrança do passado de Astério.\n
    Você pode ler abrindo os Arquivos no menu."
    $obtain_reward('Selene', 'Exploration')
    jump EXrewardcheck





label EXReward_Wine:
    $inventory.remove_item('Bundle')
    you "Então... como foi?"

    if 'Luke' in exploration_team_names() and 'Kota' not in exploration_team_names():
        $throwaway1 = 'nós conseguimos' if 'Asterion' in exploration_team_names() else 'eu consegui'
        luke "[player_name],{w=0.2} [throwaway1].{w=0.2} Missão cumprida, parceiro!"

        if throwaway1 == 'nós conseguimos':
            you "Sério?{w} Tem certeza que fizeram direito?"

            $Luke.change("arm", "pointing")

            luke "Ah, pode apostar.{w=0.2} Simplesmente seguimos as instruções:
            andamos na direção sul e vimos o planalto com algumas estátuas no topo. Era impossível errar, sério!"

        else:
            you "Sério?{w} Tem certeza que fez direito?"

            $Luke.change("arm", "pointing")

            luke "Ah, pode apostar.{w=0.2} Simplesmente segui as instruções:
            andei na direção sul e vi o planalto com algumas estátuas no topo. Era impossível errar, sério!"

        $Luke.change("arm", "hip")
        $Luke.change("emotion", "neutral")

        if 'Asterion' in exploration_team_names():
            $Asterion.change("emotion", "sad")
            luke "Agora, quando a gente chegou no topo, tinha duas estátuas:{w=0.2} um cara bombado em um trono
            e uma mulher com uma lança, escudo e usando um capacete engraçado."

            luke "Olha, eu ia na moça com a lança,{w=0.2} porque a pose dela parecia com aqueles pôsteres de propaganda
            antigos com uma mulher atraente enrolada na bandeira e essas merdas.{w} Bem vintage, sabe?"

            $Luke.change("emotion", "annoyed")
            luke "Mas Astério me convenceu do contrário e,{w=0.2} ei,{w=0.2} vou confiar no que ele diz
            se tratando desses assuntos.{w} Além disso, eu tive que dar uma animada no cara, chefe,{w=0.2}
            ele parecia péssimo pra caramba o caminho inteiro até aqui."
            $BundleSacrifice = 'Zeus'

            $Asterion.change("emotion", "tired")
            luke "Sem falar nas mulheres rastejantes sem pernas, elas não deixavam ele em paz."

            you "Você quer dizer como aquela que pulou em mim?"
            $Luke.change("arm", "pointing")

            $Asterion.change("emotion", "sad")
            luke "Bingo.{w=0.2} Olha, eu indo bem, sabe,{w=0.2} metade pássaro e tudo.{w}
            Eu sou ligeiro{w=0.2} — mas, cara, Astério acabou de passar o pior momento.{w=0.2}
            Aquelas coisas ficavam doidas sempre que viam ele. "

            $Luke.change("arm", "hip")
            luke "Eu sei que a gente tá meio sem tempo com aquela coisa de garrafa mas, por favor,{w=0.2}
            na próxima vez, poupa o cara de ter que ir lá."

        else:
            luke "Agora, quando eu cheguei no topo, tinha duas estátuas:{w=0.2} um cara bombado em um trono
            e uma mulher com uma lança, escudo e usando um capacete engraçado."

            luke "O cara no trono parecia {i}bem{/i},{w=0.2} deixa eu te contar,{w=0.2} então eu ia
            queimar o negocinho nos pés dele como um bom menino."

            $Luke.change("emotion", "horny")
            luke "Mas...{w=0.2} eu não sei,{w=0.2} me chama de frangote, mas a mulher me deixou nostálgico,
            sabe?{w} A pose dela parecia com aqueles pôsteres de propaganda
            antigos com uma mulher atraente enrolada na bandeira e essas merdas."

            $Luke.change("arm", "salute")
            luke "É cafona, eu sei, mas eu...{w=0.2} bem, eu coloquei o pacote na frente dela, queimei
            e fiz uma pequena saudação."
            $BundleSacrifice = 'Athena'

            $Luke.change("emotion", "surprise")
            luke "Mas foi assustador pra caralho.{w=0.2} Na volta, o lugar tava cheio daquelas mulheres sem perna
            rastejando."

            you "Você quer dizer como aquela que pulou em cima de mim?"

            $Luke.change("arm", "pointing")
            $Luke.change("emotion", "neutral")
            luke "Bingo.{w=0.2} Felizmente, eu sou ligeiro — sabe,{w=0.2} metade pássaro e tudo,{w=0.2}
            então cheguei aqui inteirinho."

        $Luke.change("arm", "pointing")
        $Luke.change("emotion", "cocky")
        luke "Mas, o importante é, vá mostrar pra aquela cobra quem é que manda, beleza?"

    elif 'Luke' not in exploration_team_names() and 'Kota' in exploration_team_names():
        $throwaway1 = 'Nós' if 'Asterion' in exploration_team_names() else 'Eu'

        kota "Mestre [player_name], devo informar que a tarefa em mãos está completa."

        you "Isso é fantástico! Você queimou no lugar certo?"
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        kota "Bem, não havia lá muita margem para erro.{w=0.2} As instruções foram muito claras."

        $Kota.change("rightarm", "relaxed")
        $Asterion.change("emotion", "sad")

        if throwaway1 == 'Nós':
            kota "[throwaway1] caminhamos para o sul até que vimos um pequeno planalto com algumas grandes estátuas
            no topo,{w=0.2} então seguimos o caminho até lá."
        else:
            kota "[throwaway1] caminhei para o sul até que vi um pequeno planalto com algumas grandes estátuas
            no topo,{w=0.2} então segui o caminho até lá."

        if 'Asterion' in exploration_team_names():
            kota "Então, no topo do planalto havia duas estátuas.
            De acordo com Astério, elas representam Zeus e Atenas."

            $Kota.change("emotion", "puzzled")
            $Kota.change("leftarm", "raised")
            kota "Bem, eu ouvi muitas histórias ultrajantes sobre Zeus,{w=0.2} então, primeiramente,
            pensei em fazer um sacrifício a Atenas.{w} Mas Astério me convenceu de que deveríamos fazer
            para Zeus,{w=0.2} e eu darei prioridade ao julgamento dele antes do meu nestes assuntos."
            $BundleSacrifice = 'Zeus'
            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "tired")
            kota "Infelizmente,{w=0.2} nosso retorno foi mais complicado que nossa chegada.{w} Aquelas...{w=0.3}
            criaturas sem pernas,{w=0.2} uivantes{w=0.2} e rastejantes começaram a se aproximar de nós."

            $Kota.change("leftarm", "relaxed")
            you "Ah sim, uma delas pulou em mim ontem."

            $Kota.change("emotion", "puzzled")
            kota "Sim, coisas bastante desagradáveis.{w=0.2} Felizmente, elas não vieram até mim todas de uma vez."

            kota "Embora eu deva dizer...{w=0.2} Pode não parecer, mas posso me virar em
            uma altercação física, então, independentemente, eu não estava sob nenhum perigo.{w}
            Mas não acho que posso dizer o mesmo sobre o senhor Astério."

            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "sad")
            kota "[player_name]...{w=0.2} Eu devo implorá-lo, por favor, evite enviar Astério para
            o vale novamente.{w} Parecia que tudo lá — e eu não me refiro
            apenas às criaturas — queria pegá-lo."

            $Kota.change("emotion", "neutral")
            kota "Felizmente, nós dois estamos aqui inteiros e o sacrifício aos Deuses foi cumprido.{w=0.2}
            Isto é o que importa."

        else:
            kota "Então, no topo do planalto havia duas estátuas que...{w=0.2} baseado em meu conhecimento sobre divindades
            gregas, deveriam representar Zeus e Atenas."

            $Kota.change("emotion", "puzzled")
            $Kota.change("leftarm", "raised")
            kota "Já ouvi muitas histórias ultrajantes sobre Zeus, então coloquei
            o pacote aos pés de Atenas.{w=0.2} O queimei, recitei uma pequena prece,
            e segui meu caminho alegre."
            $BundleSacrifice = 'Athena'
            $Kota.change("emotion", "sad")
            kota "...Que é o que eu gostaria de dizer, mas não havia nada de alegre sobre o meu retorno.{w}
            No meu caminho de volta, aquelas...{w=0.2} criaturas sem pernas,{w=0.2} uivantes{w=0.2}
            e rastejantes começaram a se aproximar de mim."

            $Kota.change("leftarm", "relaxed")
            you "Ah, sim, uma delas pulou em mim ontem."

            $Kota.change("emotion", "happy")
            kota "Felizmente, elas não vieram até mim de uma só vez.{w=0.2} Pode não parecer,
            mas posso me virar em uma altercação física — ainda assim, evitar conflito é sempre bom."

            kota "De qualquer forma, o que importa é: estou aqui inteiro e
            o sacrifício aos Deuses foi cumprido."

        you "Obrigado,{w=0.2} Kota."

        $Kota.change("emotion", "laughing")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        kota "Por favor, era o mínimo que eu podia fazer.{w=0.2} Agora, chega de bate-papo,
        acredito que você tem uma recompensa para reindivicar com uma certa cobra, não?"

    elif 'Luke' in exploration_team_names() and 'Kota' in exploration_team_names():
        luke "Na verdade, chefe, nada mal. Nem um pouco."
        kota "Sim. Eu… nós ficamos felizes em informar que a tarefa está concluída"

        you "Isso é ótimo! Vocês tiveram algum problema?"

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")
        $Asterion.change("emotion", "sad")
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "relaxed")
        kota "Bem, não no começo."
        $Kota.change("leftarm", "relaxed")
        luke "Sabe, chegar no planalto foi a parte fácil. Tudo o que fizemos foi andar na direção sul
        e depois de um tempo vimos o planalto de longe, não dava pra perder."
        $Luke.change("emotion", "annoyed")
        luke "Eu achei que a cobra tava mentindo e mandando a gente pra uma busca com pouca chance de
        encontrar o que se procura, mas a gente não teve problema pra chegar lá."

        if 'Asterion' not in exploration_team_names():
            $Luke.change("emotion", "neutral")
            kota "No topo do planalto havia duas estátuas que, com base no meu conhecimento das divindades
            gregas, representavam Zeus e Atenas."
            $Kota.change("emotion", "happy")
            $Luke.change("emotion", "horny")
            luke "Foi engraçado, a gente parou por um segundo, olhou um pro outro e decidiu
            ir com o cara grandão no trono."
            $BundleSacrifice = 'Zeus'
            you "Bem, fico feliz em ver que vocês dois estão se dando melhor."
            $Luke.change("emotion", "annoyed")
            $Kota.change("emotion", "sad")
            kota "Bem, eu diria que a cooperação tornou-se uma necessidade, por causa do que aconteceu depois."
            $Luke.change("arm", "pointing")
            luke "Sim, acho que aquele cuzão de merda nos mandou pra uma emboscada, porque quando a gente
            começou a andar de volta, aquelas coisas sem pernas gritando começaram a rastejar na nossa direção."
            you "Ah, sim, acho que uma dessas pulou em mim ontem."
            luke "Sim, foi uma merda sinistra."
            $Luke.change("arm", "hip")
            kota "Bem, felizmente, elas não vieram até nos de uma só fez. Eu não sou… digamos, um
            bom corredor, então tivemos que chutar algumas delas para fora do nosso caminho."
            $Luke.change("emotion", "cocky")
            luke "Vou ser honesto, eu tô impressionado com o menino dragão aqui. Não me importaria de ir uma
            ou duas rodadas com ele."
            pause 1.0
            $Kota.change("emotion", "angry")
            kota "Eu {i}espero{/i} que você esteja falando de uma luta."
            $Luke.change("emotion", "horny")
            $Luke.change("arm", "pointing")
            luke "O que você quiser chamar."
            $Luke.change("arm", "hip")
            pause 1.0

        else:
            $Luke.change("emotion", "neutral")
            kota "No topo do planalto havia duas estátuas, que Astério explicou representarem Zeus
            e Atenas. Ele sugeriu queimar o pacote na base do trono de Zeus e todos concordamos.
            Foi uma tarefa simples."
            $BundleSacrifice = 'Zeus'
            $Luke.change("emotion", "annoyed")
            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "tired")
            luke "Agora a parte difícil foi voltar, porque, deixa eu te contar, acho que aquele
            cuzão mandou a gente pra uma emboscada, porque quando a gente começou a andar de volta,
            aquelas coisas sem pernas gritando começaram a rastejar na nossa direção."
            you "Ah, sim, acho que uma dessas pulou em mim ontem."
            $Luke.change("arm", "pointing")
            luke "Sim, foi uma merda sinistra."
            $Luke.change("arm", "hip")
            $Kota.change("rightarm", "raised")
            kota "Infelizmente, todas elas foram direto para Astério. Mestre [player_name], sei que era
            imperativo obter toda a ajuda que pudéssemos desta vez, mas, por favor,
            a não ser que seja absolutamente necessário, evite enviá-lo no futuro."

            $Kota.change("rightarm", "relaxed")
            $Asterion.change("emotion", "sad")
            luke "Não foram só as criaturas, chefe. O solo, a grama, as raízes, os insetos;
            tudo queria pegar ele. Ele teve uma péssima experiência."
            $Luke.change("emotion", "neutral")

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        kota "Estamos de volta inteiros, o que é importante."
        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "pointing")
        luke "Sim, agora mostra àquela cobra quem é o chefe, beleza?"

    else:
        $Asterion.change("emotion", "sad")
        $Asterion.change("leftarm", "loose")
        $Asterion.change("rightarm", "loose")
        show Asterion:
            ease 0.05 xalign 0.503
            ease 0.05 xalign 0.5
            repeat
        pause 2.0
        asterion "Eu- Eu…"
        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")
        asterion "Eu completei a tarefa, Mestre."
        pause 1.0
        show Asterion:
            ease 0.05 xalign 0.5
        you "Sinto muito por mandar você para fora. Era o único jeito de conseguir a garrafa."
        $Asterion.change("leftarm", "loose")
        pause 3.0
        $Asterion.change("emotion", "sad")
        "Astério não responde. Ele tem dificuldade em manter contato visual com você."
        pause 1.0
        you "Sinto muito."
        pause 2.0
        "Depois de um tempo, Astério recupera a compostura e lentamente se curva para você."
        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")
        asterion "Por favor, Mestre, não sinta. O que importa é que o sacrifício está completo.
        Eu coloquei o pacote ao lado de uma estátua de Zeus no santuário e o queimei,
        e consegui voltar. Isto é o que importa."
        $BundleSacrifice = 'Zeus'
        pause 1.0
        $Asterion.change("emotion", "tired")
        $Asterion.change("leftarm", "loose")
        asterion "Eu-eu acredito que Argos esteja esperando por você, Mestre."
        you "Sim, vou me encontrar com ele agora mesmo."

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
        "Você obteve uma tábua de argila narrando a jornada de um filho devoto a Creta.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet1', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet2':
        $add_file('Memento', "Tablet2")
        "Você obteve uma tábua de argila narrando a chegada de uma família amaldiçoada em Creta.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet2', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet3':
        $add_file('Memento', "Tablet3")
        "Você obteve uma tábua de argila narrando uma rara audiência com um rei antigo.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet3', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet4':
        $add_file('Memento', "Tablet4")
        "Você obteve uma tábua de argila narrando uma intervenção de uma jovem preocupada.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet4', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet5':
        $add_file('Memento', "Tablet5")
        "Você obteve uma tábua de argila narrando o encontro de um homem com outro de natureza divina.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet5', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet6':
        $add_file('Memento', "Tablet6")
        "Você obteve uma tábua de argila revelando a hospitalidade de uma criança.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet6', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet7':
        $add_file('Memento', "Tablet7")
        "Você obteve uma tábua de argila narrando uma pequena tragédia da loucura humana.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet7', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet8':
        $add_file('Memento', "Tablet8")
        "Você obteve uma tábia de argila retratando uma cena de traição.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet8', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet9':
        $add_file('Memento', "Tablet9")
        "Você obteve uma tábua de argila uma pequena tragédia da loucura humana.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet9', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet10':
        $add_file('Memento', "Tablet10")
        "Você obteve uma tábua de argila revelando um bastardo tentando um jovem devoto a se afastar para longe de seu dever.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet10', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet11':
        $add_file('Memento', "Tablet11")
        "Você obteve uma tábua de argila revelando uma das muitas tragédias que levaram à morte de um menino.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet11', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet12':
        $add_file('Memento', "Tablet12")
        "Você obteve uma tábua de argila revelando a natureza suja de um híbrido.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet12', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet13':
        $add_file('Memento', "Tablet13")
        "Você obteve uma tábua de argila revelando o desânimo do híbrido.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet13', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet14':
        $add_file('Memento', "Tablet14")
        "Você obteve uma tábua de argila revelando uma das muitas tragédias que levaram à morte de um menino.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet14', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet15':
        $add_file('Memento', "Tablet15")
        "Você obteve uma tábua de argila revelando o último resquício de esperança de um prisioneiro.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet15', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet16':
        $add_file('Memento', "Tablet16")
        "Você obteve uma tábua de argila retratando um crime contra a vontade divina.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet16', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet17':
        $add_file('Memento', "Tablet17")
        "Você obteve uma tábua de argila revelando a libertação de um prisioneiro.\n
        Você pode ler abrindo os Arquivos no menu."
        $obtain_reward('Tablet17', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet18':
        $add_file('Memento', "Tablet18")
        "Você obteve uma tábua de argila revelando um destino sinistro.\n
        Você pode ler abrindo os Arquivos no menu."
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
