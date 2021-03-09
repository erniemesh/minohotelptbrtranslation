##############################################################################
#                      CHAPTER 6: THE SECOND NIGHT
##############################################################################
#6_0: Asterion and MC talking.

label chapter6:
    $new_build_update()
    $build=2
    $check_in_guest('Asterion')

    $abuse_act1 = 0
    $abuse_act2 = 0
    $abuse_act3 = 0
    if Chapter4_Terrorized_Asterion == "True":
        $abuse_act1 +=3


    play music "music/JatoTheLion.ogg" fadeout 1.0 fadein 1.0
    scene bg lounge
    with Dissolve (1)
    show Asterion
    with Dissolve (1)

    "Você acena com a cabeça e conta a Astério sobre suas bebidas favoritas."

    if Chapter4_Terrorized_Asterion == "True":
        $Asterion.change ("emotion","neutral")

        "O minotauro se ocupa com seu pedido. A carranca na testa dele desaparece
        pouco tempo depois."

    else:
        "Os detalhes do que você diz parecem banhar Astério. Ele não acena
        ou reage enquanto você descreve a bebida — em vez disso, o rosto dele é tomado por uma lânguida alegria."

    $Asterion.change ("emotion","contemplative")

    "Astério vai para trás do novo balcão do salão. Suas mãos acariciam a madeira,
    sentindo a textura macia, quase sensual. Ele acena com a cabeça sem olhar para você."

    asterion "Agora eu posso lhe assegurar — farei algo bastante extraordinário."

    if Chapter4_Terrorized_Asterion == "True":
        "Ele diz enquanto acaricia seu Hotel, com um olhar cheio de orgulho e
        amor.{w} Por um momento, até parece que você não existe."

        asterion "Ah, que momentos maravilhosos nós teremos."

        asterion "Exatamente como costumava ser.{w} Pessoas por toda parte outra vez, não
        estaremos tão sozinhos."

    else:
        "Ele diz enquanto acaricia seu amado Hotel."

    "O minotauro olha para as garrafas na parede. Você não reconhece nenhum
    dos rótulos, mesmo que consiga adivinhar o conteúdo; parece que são
    todas produções locais."

    "Astério, no entanto, parece acomodado. Seu olhar vagueia apenas por um momento
    antes de ganhar um tom de reconhecimento. Ele seleciona as garrafas necessárias e
    começa a preparar sua bebida."

    "Ele começa lavando um copo. Já estava brilhando quando o minotauro o retirou da
    bancada, como se tivesse acabado de ser polido para o primeiro uso, mas ele
    insiste em lavar."

    "A torneira está ligada e há até uma barra de sabão nova perto da pia. É
    como se todo o lugar tivesse acabado de ser arrumado por uma equipe de limpeza disciplinada."

    "O minotauro mantém o sorriso, seus olhos entreabertos enquanto ele passa os dedos no
    jogo de taças e em todo o equipamento que utilizará."

    "Ele saboreia seu doce tempo para se familiarizar com o novo ambiente e, em seguida,
    serve sua bebida. Às vezes ele desmonstra um pouco de falta de destreza, sem dúvida
    uma consequência de beber uma garrafa inteira de vinho."

    "Astério cuidadosamente desliza o copo para você em cima de um guardanapo. Ele finalmente
    olha de volta para seus olhos, reconhecendo sua existência. A voz dele sai com a
    mais leve inflexão de um sorriso."

    asterion "Ainda não cheguei lá. Vou melhorar, só preciso de um pouco
    de prática para voltar ao meu antigo eu."

    asterion "Eu raramente administrava o salão. Estou familiarizado com ele, é
    claro, mas sempre houve melhores bartenders por perto."

    asterion "Mas eu gosto. É tão calmante, a precisão que acompanha a mistura
    de bebidas."

    $Asterion.change ("leftarm","raised")

    "Astério coloca o antebraço em cima do balcão, apoiando o próprio peso.
    Sua cauda balança preguiçosamente atrás dele."

    $Asterion.change ("emotion","smiling")

    asterion "Eu também nunca fui o melhor cozinheiro. Cozinho bem o suficiente para
    agradar ao Mestre, você vai ver, mas trabalhar na cozinha exige agilidade."

    asterion "Eu poderia gastar dez minutos cortando um tomate, me certificando de
    que todos os pedaços estivessem do mesmo tamanho. O Mestre Jean-Marie me fez fazer exatamente isto
    algumas vezes."

    asterion "Cozinhar é uma coisa bastante querida, Mestre."

    asterion "Na época em que o Mestre Jean-Marie estava vivo, meus turnos ajudando os
    funcionários da cozinha se resumiam a, no máximo, ficar em um canto cortando algumas cebolas
    por hora."

    asterion "Trabalhar com as mãos é muito relaxante, mesmo que eu não seja
    terrivelmente hábil."

    asterion "Pode ser uma surpresa para você, mas eu só aprendi a cozinhar — como
    medir ingredientes, ler receitas, temperar comida — há apenas alguns séculos."

    asterion "Ninguém me ensinou como fazer isso em Creta. E, quando eu estava no
    labirinto, não havia muito com o que cozinhar."

    asterion "Meu pai enviava remessas de comida..."

    $Asterion.change ("emotion", "tired")

    asterion "..."

    $Asterion.change ("emotion", "neutral")

    asterion "Não importa. É impróprio de minha parte descarregar algo assim em
    alguém, muito menos no Mestre."

    asterion "Há assuntos mais felizes em abundância."

    $Asterion.change ("emotion","contemplative")
    $Asterion.change ("leftarm", "loose")

    "O minotauro se vira e pega uma garrafa de vinho. É diferente das garrafas
    anteriores que você encontrou; possui uma etiqueta minimalista e
    um formato mais moderno."

    if global_affection < 2:
        "Astério serve uma taça para si mesmo."

    if global_affection >= 2:
        "Astério dá uma olhada rápida e pensativa em você antes de abrir a garrafa
        e tomar um longo gole."

    "Sobre o que vocês falam a seguir?"

##############################################################################
#                      CHAPTER 6.1: ASKING QUESTIONS
##############################################################################

    $myChoices = [ ("O que você fazia para se divertir?", "id1"), ("Como era a vida em Creta?", "id2"),
    ("Quais são as suas comidas favoritas?", "id3"), ("Qual é a sua memória favorita?", "id4")]
    label chapter6_0:
        $narrator("Sobre o que vocês falam a seguir?", interact=False)
        $result = renpy.display_menu(myChoices)


    if result == "id1":

        you "Então, eu estou curioso. Antes do Mestre Clément aparecer, o que
        você fazia para se divertir aqui?"

        $Asterion.change ("emotion", "smiling")

        asterion "Para me divertir?"
        asterion "Suponho que tive um número de atividades de lazer ao longo dos
        séculos... desde que o Hotel foi construído, pelo menos."
        asterion "Nem sempre tive os meios, mas... fui um ávido leitor
        por um tempo."

        $Asterion.change ("emotion", "contemplative")

        asterion "Tenha em mente que eu venho de uma época muito, muito antes da invenção
        da prensa móvel. Eu aprendi a ler a língua cretense com meus irmãos, lendo e
        escrevendo letras na areia."

        asterion "Não havia papel naquela época e as histórias eram recitadas
        de memória."

        asterion "Ainda hoje, o Hotel não pode manifestar livros. Ainda dependemos
        em receber remessas do mundo exterior."

        $Asterion.change ("emotion", "smiling")

        asterion "Mas quando os Mestres achavam por bem me presentear alguns... eu sempre
        gostei de adquirir material de leitura."

        asterion "Poesia, principalmente, mas... como posso dizer..."

        $Asterion.change ("emotion", "contemplative")

        asterion "Estou curioso para saber como está o mundo lá fora. Eu
        nunca pude ver por conta própria, mas quando leio as histórias...
        posso imaginar."

        asterion "Muitas vezes me perguntei quão diferente a realidade é do que
        imaginei e o quanto ela mudou."

        asterion "Mestre Jean-Marie insistiu que eu lesse {i}O Corcunda de
        Notre-Dame.{/i} Ele até me mostrou alguns desenhos da Catedral
        que ele mesmo desenhou de memória."

        $Asterion.change ("emotion", "smiling")

        asterion "Mas eu me pergunto... como deve ser a sensação de estar lá?
        Quão assustador deve ser?"

        $Asterion.change ("emotion", "contemplative")

        asterion "Eu nunca estive em uma igreja — morri muito antes de Cristo.
        Mas os hóspedes me contaram tudo sobre elas."

        asterion "Vitrais. Pilares altos e poderosos. Os arcos...
        A voz de uma pessoa ecoando todo o caminho até a entrada. E os
        bancos de madeira."

        asterion "Eu me pergunto como a {i}Notre-Dame de Paris{/i} deve estar
        hoje em dia. Qual deve ser a sensação de caminhar sozinho por ela,
        observando todas as estátuas dos apóstolos."

        if player_background == "arts":
            "Você se lembra de alguns detalhes sobre {i}Notre-Dame de Paris{/i}
            de seus estudos de arte."

            menu:
                "{color=[UIColorArts]}(ARTES) Discutir Notre-Dame em profundidade.{/color}":

                    you "Sim, deve ser uma ótima atmosfera. A Catedral tem
                    muita reverberação, como costumavam ter os anfiteatros da Grécia Antiga."
                    $Asterion.change ("emotion","contemplative")

                    you "Se você falar, vai ouvir o que disse pelos próximos quatro segundos.
                    Tenho certeza de que é assustador se você ouvir presencialmente, mas em uma
                    gravação seria apenas um eco."
                    you "As composições de música feitas para aquele espaço eram deliberadamente simples e flutuantes,
                    e levou um bom tempo para adotarem uma outra abordagem. Acredito
                    que a música antiga também era assim."
                    you "Os acordes completos soaram estranhos para você quando ouviu pela
                    primeira vez? Presumo que a música com a qual você cresceu era principalmente monofônica."

                    asterion "Bem, sim. Eu passei bastante tempo sem escutar músicas e,
                    quando me familiarizei com elas novamente, tudo soava muito estranho
                    para mim."

                    you "Se o Mestre Jean-Marie falou bem da Catedral, posso pensar em
                    algumas canções que poderia mostrar a você. Elas estão entre
                    monofonia e polifonia."

                    you "Você gostaria disso? Não é a mesma coisa que estar
                    na {i}Notre-Dame de Paris{/i} mas você pode gostar."
                    $Asterion.change ("emotion","smiling")

                    asterion "Sim, com certeza! Eu adoraria, Mestre."

                    you "Vou tentar me lembrar de conseguir mais livros para você, também,
                    já que você é um leitor tão ávido."
                    $Asterion.change ("emotion","contemplative")

                    asterion "Eu gostaria muito disso também. Livros são
                    minha... minha escapatória, eu suponho. Desta realidade."
                    $ global_affection += 0.5
                "Deixá-lo continuar":
                    "Você terá muitas oportunidades para falar sobre Notre Dame.\n
                    Então decide não interromper Astério."


        if player_background == "speedrunner":
            menu:
                "{color=[UIColorSpeedrunner]}(SPEEDRUNNER) Ah! Ah! Eu conheço Notre Dame!{/color}":

                    you "Não é aquela igreja que pegou fogo?"

                    $Asterion.change ("emotion","surprise")

                    asterion "Como?"

                    you "É, ela pegou fogo. Foi por causa de alguma fiação defeituosa ou algo assim."

                    $Asterion.change ("emotion","sad")

                    asterion "...Ah."

                    asterion "..."

                    asterion "..."

                    you "Não fique triste, existem alguns videogames ambientados na França que têm recriações
                    muito precisas dela."

                    asterion "Me desculpe, mas o que é um videogame?"

                    you "...Deixa para lá."
                "Permanecer em silêncio." if global_affection >=3:
                    "Em um raro momento de autocontrole, você decide mudar de assunto
                    e poupar Astério de algumas más notícias sobre a catedral de
                    Notre-Dame."

        else:

            asterion "Às vezes, eu até sonhava com o que estava lendo.
            Era uma satisfação como nenhuma outra."

            asterion "Existem poucas coisas melhores do que um bom livro."

            asterion "Isso dificilmente conta como meu passatempo principal, porém,
            já que livros sempre foram tão escassos. Minha lira tem sido minha querida
            amiga há séculos."

            $Asterion.change ("emotion", "tired")

            asterion "...O Mestre pode pressupor que devo estar terrivelmente
            enferrujado depois de todos esses anos trancado."
            $Asterion.change ("emotion", "smiling")

            if global_affection >= 2:
                asterion "Porém, assim que aperfeiçoar minhas habilidades e afiná-la...
                seria um prazer tocá-la para meu Mestre."

            asterion "Como disse, eu também gostava de passar tempo com os hóspedes.
            Quem não gosta de estar entre amigos?"

            asterion "Mas suponho que, para mim, seja diferente... faz com que eu me sinta
            normal. Tão normal quanto um minotauro pode ser, o que não é muito."

            $Asterion.change ("emotion", "neutral")

            asterion "Nem sempre contava para eles sobre meu passado. O Mestre tem
            o direito de saber, é claro. E alguns deles foram informados,
            mas apenas aqueles que eu escolhi."

            asterion "Na maioria das vezes, eu não queria que eles soubessem."

            $Asterion.change ("emotion", "tired")

            asterion "Isso apenas atrapalhava. Já era suficientemente difícil fazer
            amigos. E abria caminho para uma série de questões que eu prefiro não responder todos os dias."

            "Astério morde o lábio e suspira."

            asterion "Há uma coisa que eu gostava muito... mas dificilmente conta como uma atividade
            de lazer e eu não gostaria de incomodar o Mestre divagando sobre isso."

            menu:
                "Deixar para lá.":
                    if len(myChoices)>1:
                        asterion "Algo mais que o Mestre gostaria de saber?"

                "Pedir para continuar.":

                    $Asterion.change ("emotion", "neutral")

                    you "Continue. O que era?"
                    if Chapter4_Terrorized_Asterion == "True":
                        $Asterion.change ("emotion", "tired")
                        pause 1.0
                        asterion "Não...{w} era nada realmente, meu senhor. Nada com o que
                        você deveria se preocupar.{w} Perdoe-me."

                        you "Sério? Não tem problema, você pode confiar em mim."

                        $Asterion.change ("emotion", "sad")

                        asterion "Ah, eu sei.{w} Apenas prefiro não incomodar meu senhor com meus
                        comentários fúteis sobre um assunto tão frívolo."

                        asterion "Há mais alguma coisa que gostaria de saber?"

                    else:
                        $Asterion.change ("emotion", "contemplative")
                        asterion "Bem, se o Mestre realmente deseja saber..."

                        asterion "Alguns mestres que herdaram o Hotel
                        tiveram seus próprios filhos. Na maioria das vezes, eles mesmos eram
                        hóspedes antes de adquirirem a escritura, então me conheciam
                        bem o suficiente."

                        asterion "Eu ajudei a cuidar dos filhos. Eles eram uma alegria, cada
                        um deles."

                        $Asterion.change ("emotion", "smiling")

                        asterion "Mesmo os indisciplinados, devo acrescentar."

                        asterion "Normalmente, demorava um pouco para que eles gostassem de mim.
                        Eu sei que posso ser assustador até para um adulto, quanto mais para uma criança."

                        if global_affection >= 2:

                            $Asterion.change ("emotion", "tired")

                            asterion "Posso apenas imaginar o que deve ter passado por sua
                            mente quando você me viu na câmara fria..."

                            $Asterion.change ("emotion", "contemplative")

                            asterion "Suponho que eu deveria ser grato por você não ter
                            me abandonado lá mesmo."

                            asterion "Enfim..."

                        $Asterion.change ("emotion", "contemplative")

                        asterion "Os mais novos, se por acaso chegassem ao Hotel
                        cedo o suficiente... habituavam-se a mim mais
                        rápido."

                        $Asterion.change ("emotion", "smiling")

                        asterion "Alguns até diziam que eu era fofo!"

                        asterion "Eles achavam divertido ter um amigo minotauro.
                        Brincar com meus chifres, me acariciar. Eu até carregava eles nas
                        minhas costas. Eu era o babá divertido, pode-se dizer."

                        asterion "Uma boa parte deles até cresceram para se tornar mestres
                        eles mesmos, herdando a escritura de seus pais. Era uma
                        alegria, servir às crianças que ajudei a criar."

                        $Asterion.change ("emotion", "contemplative")

                        asterion "Eu era bastante orgulhoso deles, de quem eles se tornaram. O
                        Hotel detinha um significado especial para eles, era uma casa como
                        nenhum outro lugar poderia ser."

                        asterion "...O Hotel atrai aqueles que estão perdidos. Muitas daquelas
                        crianças não tinham um lugar para onde voltar. Algumas perderam
                        seus países completamente."

                        asterion "..."

                        $Asterion.change ("emotion", "tired")

                        asterion "Isso foi há muito tempo. Me pergunto se alguns de seus
                        descendentes ainda vivem."

                        asterion "A vida dura apenas por um curto período de tempo."

                        $Asterion.change ("rightarm", "loose")

                        asterion "Conheci um deus uma vez. Ele me disse que a vida humana é como
                        um piscar de olhos para eles. Somos equivalentes a animais de estimação."

                        asterion "Meu pai costumava me dizer para não me apegar a cães,
                        pois eles tinham vidas curtas. É assim que eles enxergam os mortais."

                        $Asterion.change ("rightarm", "hips")
                        $Asterion.change ("emotion", "smiling")

                        asterion "Não é a mesma coisa para mim. Posso já ter morrido,
                        mas vivencio o tempo como qualquer outra pessoa."

                        asterion "De fato, a vida dura apenas um curto período de tempo, mas é longa
                        o suficiente para ser aproveitada."

                        asterion "É melhor não pensar demais sobre esses assuntos."

                        $Asterion.change ("emotion", "neutral")

                        asterion "O que mais... eu gosto de exercícios."

                        $Asterion.change ("emotion", "smiling")

                        asterion "Eu não era um grande lutador por natureza, mas fui treinado
                        para tal. Fui ensinado a permanecer sempre atento."

                        asterion "Francamente, mal posso esperar para fazer algum exercício.
                        Possivelmente não esta noite. Ainda é muito cedo, mas... o dia chegará."

                        asterion "O que mais... O que mais eu gostava..."

                        asterion "Música! Eu tocava a lira, sim, mas o rádio...
                        Ah, era ótimo. O Mestre Jean-Marie fazia questão que eu ouvisse
                        todos os cantores franceses."

                        $Asterion.change ("emotion", "contemplative")

                        asterion "A humanidade é de fato maravilhosa. Os deuses e as criaturas
                        míticas, eles são gravados em pedra e dificilmente mudam algum dia.
                        Foram feitos para ser eternos."

                        asterion "Mas os humanos mudam tanto! E eu sou grato por pelo menos
                        ser meio-humano, gosto muito das invenções que a humanidade confeccionou ao
                        longo dos séculos!"

                        asterion "Mal posso esperar para aprender sobre tudo o que mudou."

                        asterion "Há mais alguma coisa que o Mestre gostaria de saber?"

        $ myChoices.remove(("O que você fazia para se divertir?", "id1"))

    if result == "id2":
        $Asterion.change ("emotion", "neutral")
        asterion "A vida em Creta?"

        $Asterion.change ("emotion", "tired")

        asterion "Agora isso... minha memória está nebulosa, para dizer o mínimo.
        Já faz tanto tempo que nem tenho certeza se o que lembro está correto."

        asterion "Mas..."

        $Asterion.change ("emotion", "smiling")

        asterion "Creta era uma grande potência naquela época. Isto foi antes de
        Atenas ganhar força."

        asterion "Eu fui criado no Palácio de Cnossos. Era um edifício amplo e
        imenso, possivelmente o maior que o mundo já tinha visto na época."

        $Asterion.change ("emotion", "contemplative")

        asterion "Eu tinha muitos irmãos. Nós brincávamos, quando me era permitido.
        Eu não podia deixar o palácio com frequência, mas costumava fugir com meus irmãos
        para caçar cabras selvagens."

        asterion "Eu era ligeiro, meus cascos me ajudavam a cruzar o solo duro e vulcânico
        de Creta."

        $Asterion.change ("emotion", "smiling")

        asterion "Eu tinha uma mãe e um pai, como qualquer outra criança."

        $Asterion.change ("emotion", "neutral")

        asterion "..."

        if global_affection >= 2:

            asterion "O nome da minha mãe era Pasífae. Ela... em retrospecto,
            percebo que ela não era muito presente. Mentalmente, quero dizer."

            asterion "Eu não entendia muito bem na época, mas acho que ela não
            gostava de me ver. Eu a lembrava do que ela tinha feito
            e de sua reputação."

            asterion "Meu pai adotivo era o Rei Minos. Contanto que eu não estivesse
            me comportando mal, ele me tratava bem na maior parte do tempo.
            Pois eu era sagrado."

            asterion "..."

        if global_affection >= 3:

            $Asterion.change ("emotion", "tired")

            asterion "E então eu fui enviado para o labirinto."

            asterion "Não me lembro qual era minha idade naquela época. Talvez doze anos ou
            mais. Minha irmã, Ariadne, convenceu o pai."

            $Asterion.change ("emotion", "neutral")

            asterion "Ela disse que eu me tornaria perigoso. Demorou um pouco, mas
            ele foi influenciado."

            $Asterion.change ("emotion", "tired")

            asterion "Eu fui transportado e largado lá apenas com um machado para me
            defender. Naquele labirinto construído pelo artesão Dédalo."

            asterion "Assim que era a vida para mim em Creta."

            $Asterion.change ("emotion", "neutral")

            asterion "Não é curioso como guardamos memórias da infância?
            Eu já existo há milhares de anos."

            asterion "Eu morri jovem, antes do meu vigésimo aniversário. Ainda assim, muito
            de quem eu sou vem dessas duas décadas."

            asterion "Me pergunto com frequência como teria sido a vida se eu não fosse
            um monstro híbrido. Para começar, a mãe não teria perdido a cabeça."

            asterion "Minha irmã não teria tentado convencer o pai a me mandar
            embora. Eu teria tido uma infância normal."

            asterion "Não se engane, a vida naquela época não era fácil e morrer
            jovem não era algo fora do comum. Uma terra como Creta também
            precisava se manter armada."

            asterion "Se eu tivesse nascido completamente humano, poderia ter morrido jovem
            de alguma doença, ou no início da idade adulta em combate."

            asterion "Ainda assim, isso teria sido preferível ao que precisei
            passar. Se eu não tivesse sido enviado para o labirinto, os deuses não teriam
            me sentenciado por minha covardia."

            asterion "Eu ainda estaria em Hades, no Campo de Asfódelos,
            onde eu deveria estar."

            $Asterion.change ("emotion", "smiling")

            asterion "Hades... Pode ser que o Mestre tenha desejado que eu contasse sobre
            boas memórias de Creta. Eu tenho algumas, bastante, na verdade, mas tenho
            mais de Hades."

            asterion "Eu era bem-vindo lá, assim como todas as almas. É claro, eu não era um herói
            e jamais veria os Campos Elísios — é para onde iam os heróis."

            asterion "Mas o Campo de Asfódelos, para onde as almas comuns eram
            sentenciadas, era bastante agradável."

            asterion "Eu até tinha um emprego lá! O deus do submundo me escolheu para
            fazer parte da patrulha da fronteira. Era um dever simples o
            bastante, patrulhar a fronteira para pegar almas tentando
            escapar."

            $Asterion.change ("emotion", "contemplative")

            asterion "Eu dividia a casa com um primo. Eu nem mesmo
            sabia que {i}tinha{/} um primo até então."

            asterion "Seu nome era Gerião, e tínhamos muito em comum."

            asterion "O deus do submundo, o próprio senhor Hades, gostou
            de mim. Treinávamos juntos com frequência e ele me ensinou o estilo
            de luta do submundo."

            "Astério olha para o balcão e tamborila os dedos sobre ele,
            perdido em pensamentos."

            asterion "Eu era um bom patrulheiro. Não teria me importado
            em permanecer lá."

        $Asterion.change ("emotion", "smiling")

        asterion "Isso é tudo, eu suponho."

        if len(myChoices)>1:
            asterion "O Mestre tem alguma outra pergunta?"

        $ myChoices.remove(("Como era a vida em Creta?", "id2"))


#What's your favorite food?
    if result == "id3":
        $Asterion.change ("emotion","neutral")

        asterion "Minha comida favorita?"

        $Asterion.change ("emotion","smiling")

        asterion "O Mestre não deve se preocupar com isso. Eu como as
        sobras, qualquer coisa serve para mim."

        asterion "E não é como se eu pudesse morrer de fome.
        Em última análise, isso realmente não importa."

        you "Mas certamente existem coisas que você prefere... ou comidas
        que você não comeria. Alguma alergia?"

        $Asterion.change ("emotion","neutral")

        asterion "Bem, se o Mestre realmente deseja saber... Eu não..."

        $Asterion.change ("emotion","bowing")
        $Asterion.change ("leftarm","raised")

        asterion "Eu prefiro não comer carne bovina e já não faço isto há
        milhares de anos. Seria canibalismo."

        $Asterion.change ("emotion","neutral")

        asterion "Então, geralmente prefiro aves e peixes, ou..."

        $Asterion.change ("emotion","contemplative")

        asterion "Bem, eu caçava cabras selvagens com meus irmãos em Creta.
        Gosto bastante... É de longe uma de minhas comidas favoritas."

        $Asterion.change ("leftarm","loose")

        $Asterion.change ("emotion","neutral")

        asterion "Eu não comia carne com frequência quando era criança.
        Era uma espécie de luxo... e as remessas para o labirinto raramente
        tinham alguma. Teria apodrecido no caminho, então eles nem tentavam."

        $Asterion.change ("emotion","contemplative")

        asterion "Cabras à parte... por muito tempo aveia era o melhor que eu podia
        conseguir. Ainda hoje tenho um bom paladar para mingau."

        if global_affection >= 2:
            $Asterion.change ("emotion","smiling")

            asterion "E... tenho um gosto por doces. Sempre gostei de frutas e mel,
            desde criança, mas em 1940 havia tantas opções."

            asterion "Mestre Jean-Marie insistiu desde o início de seu mandato que precisávamos de
            doces franceses diariamente."

            asterion "Tradicionais baguetes, croissants e {i}pain au chocolat{/i}
            para o café da manhã, com geleia. Macarons todo domingo e tortas depois do almoço."

            $Asterion.change ("emotion","contemplative")

            asterion "Fazer uma baguete tradicional não é tarefa simples. Passei
            muitos meses tentando fazer uma única que agradasse seu paladar."

            asterion "Ele me permitia comer as sobras de vez em quando."

            $Asterion.change ("emotion","smiling")

            asterion "Só pensar nisso me faz salivar. Sou tão grato..."

            "Ele não termina o pensamento. Astério mantém seus olhos fixos
            em você, suas orelhas e cauda sacudindo preguiçosamente."

        if len(myChoices)>1:
            asterion "Há mais alguma coisa que deseja saber, Mestre?
            Você só precisa perguntar."

        $ myChoices.remove(("Quais são as suas comidas favoritas?", "id3"))

#Favorite memory?

    if result == "id4":
        $Asterion.change ("emotion","contemplative")
        $Asterion.change ("rightarm","hips")
        $Asterion.change ("lefttarm","loose")

        asterion "Minha... minha memória favorita?"

        asterion "Esta é uma pergunta difícil..."

        "Astério bebe mais de seu vinho, então esfrega a mão contra
        o balcão. Ele suspira, olha para você, depois volta a
        olhar para baixo algumas vezes."

        asterion "Pergunta muito difícil. Mas acho que sei..."

        $Asterion.change ("emotion","smiling")

        asterion "Houve um Mestre, Seu Bernardo. Ele foi o senhor do Labirinto
        por algumas décadas e depois passou para o filho, Seu Roberto."

        $Asterion.change ("emotion","contemplative")

        asterion "Quando Seu Bernardo estava no leito de morte, seu filho transferiu
        a posse do Hotel de volta para ele por um dia."

        asterion "Como Mestre reincidente do Hotel, Seu Bernardo escreveu e assinou
        um... um \"contrato.\" Exceto que era apenas uma... uma carta para mim.
        Me agradecendo por tudo."

        asterion "Seu Roberto assumiu novamente, é claro, e ele me
        preparou algo também."

        $Asterion.change ("emotion","smiling")

        asterion "Eu ajudei a criá-lo, sabe, e ele reuniu todos os desenhos
        de infância que fez de mim e os assinou como um contrato
        também."

        asterion "Contratos são eternos, a menos que sejam revogados
        explicitamente. Então os \"contratos\" deles durariam para sempre. Eles não podem
        ser queimados ou rasgados — nada irá destruí-los."

        asterion "Esta é minha memória mais querida. Os presentes de Roberto e Bernardo para mim."

        $Asterion.change ("emotion","neutral")

        asterion "...Os contratos, eles duram para sempre, mas eu sei que Clément rasgou
        o livro de registros onde os guardávamos."

        asterion "Eles devem estar escondidos em algum lugar. Vou encontrá-los outra vez,
        eventualmente, mesmo que demore anos."

        $Asterion.change ("emotion","contemplative")

        asterion "Afinal, eu tenho todo o tempo do mundo, não tenho?"

        "O minotauro toma mais um gole de vinho. Ele balança
        para a esquerda e para a direita, os olhos entreabertos."

        asterion "...Eu tenho outra memória tão doce quanto."

        asterion "Quando eu estava no submundo, fiz amigos.
        Um deles me presenteou com a estátua de um boi vermelho."

        asterion "Ele foi um pastor em vida. Combinava, é claro.
        Eu a trouxe comigo para este lugar... a única coisa que consegui trazer."

        $Asterion.change ("emotion","neutral")

        asterion "Deveria estar no meu quarto, mas... novamente, Clément."

        $Asterion.change ("emotion","contemplative")

        asterion "...Eu era amado. As cartas e a estátua,
        eu as valorizava muito."

        $Asterion.change ("emotion","smiling")

        asterion "Mas o amor não precisa de presentes para ser lembrado."

        "Astério olha para baixo novamente. Ele segura a garrafa de vinho contra o peito."

        if len(myChoices)>1:
            asterion "Há mais alguma coisa que o Mestre gostaria de saber?"

        $ myChoices.remove(("Qual é a sua memória favorita?", "id4"))

    $ long = len(myChoices)
    if long > 0:
        jump chapter6_0


##############################################################################
#                      CHAPTER 6.2: ENDING THE NIGHT
##############################################################################

    "Quando a conversa se esgota naturalmente, vocês dois se
    deixam levar pela inércia para um silêncio confortável."

    "O burburinho caloroso do álcool em seu sistema ajuda muito a aliviar o trabalho
    penoso do dia, assim como o crepitar amigável da lareira
    reacendida recentemente."

    "Os assentos suportam seu peso admiravelmente, apesar da idade, e o
    rústico aroma de fumaça de madeira e fino estofamento de couro tornam o
    relaxamento tão fácil quanto respirar."

    "Embora você e Astério sejam os únicos ocupantes atuais do
    salão, as coisas parecem um pouco mais animadas do que a fileira de bancos vazios
    poderia sugerir."

    "Com a melhoria das condições do Hotel, cada objeto
    transborda com potencial para servir a futuros clientes."

    "Há algo na capacidade da luz do fogo de cativar o coração que remonta
    a tempos imemoriais."

    "Como se gravadas em seus ossos pelos esforços de seus ancestrais,
    as sombras dançantes despertam um impulso que sua mente pode apenas
    vagamente direcionar."

    "Por um momento a presença de Astério é tão insubstancial que você
    se sente sozinho com seus pensamentos."

    "No canto do olho, você enxerga a sobrancelha bovina dele vincar,
    os olhos movendo-se lentamente de um lado para o outro entre você e a lareira."

    "A boca dele abre silenciosamente por um momento, mas fecha com a mesma rapidez,
    como se a mais sutil perturbação do ar fosse suficiente para estilhaçar a idílica
    cena."

    "Na suave luz, o semblante de Astério fica cheio de vida e, em seguida, frio e lúcido."

    "Talvez como uma peculiaridade de seu corpo imortal, ele parece ficar sóbrio mais rápido
    do que você esperava; seu olhar finalmente fixa-se no fogo com o rígido foco
    de um guarda treinado — alerta, mas sem denunciar qualquer sinal de seus
    sentimentos."

    "Você não consegue dizer quantas horas vocês dois passaram diante da lareira,
    observando com atenção, simples e extasiada, para a chama. Sem consciência da passagem
    de tempo, o insaciável momento se estende enquanto as compulsões de sua biologia
    permitirem."

    "A sensação do queixo batendo em seu peito eventualmente o tira do devaneio
    silencioso — você nem percebeu que estava começando a cochilar."

    "Com os olhos turvos, seja por embriaguez ou fadiga, você verifica o celular;
    é quase meia-noite."

    "Astério furtivamente rouba uma olhada no relógio da tela de seu smartphone,
    mas não faz nenhum comentário sobre ele. Curiosidade emboscada pelo dever,
    ele fala, enfim."

    asterion "Já está bem tarde, Mestre. Seria de seu agrado se eu preparasse o
    jantar antes de você ir dormir?"

    if global_affection >= 2:
        asterion  "...Desta vez eu posso cozinhar uma refeição apropriada para você."

    hide Asterion
    with Dissolve(1.0)
    pause 1.0
    scene bg staircase
    with Dissolve(1.0)

    "Você não consegue enxergar razão para recusar a oferta de Astério."

    scene bg oldquarters
    with Dissolve(1.0)

    "A caminhada de volta aos seus aposentos é abençoadamente breve e
    você rapidamente se senta no sofá e se acomoda
    para o jantar."

    "Enquanto seu servo minotauro prepara o jantar, há pouco a fazer,
    exceto relaxar no sofá e saborear os cheiros que emanam de sua
    cozinha particular."

    "Você continua a intercalar entre consciência e inconsciência volta e meia,
    dividido entre a fome torturante em sua barriga e o peso repentino de suas
    pálpebras."

    $Asterion.change ("emotion","bowing")
    $Asterion.change ("leftarm","raised")
    $Asterion.change ("rightarm","loose")
    show Asterion
    with Dissolve(1.0)

    "Astério o presenteia com sua comida em pouco tempo, trazendo uma bandeja
    de bife de presunto e purê de batata para o sofá para poupá-lo de ter que andar
    até a mesa."

    $Asterion.change ("emotion","neutral")

    "Para o seu cérebro embriagado e nublado pelo sono, parece um verdadeiro banquete.
    Você avança na comida com o prazer de um homem faminto."

    $Asterion.change ("emotion","contemplative")

    "Quando você se senta e começa a comer, Astério parece vagamente contente em vê-lo
    saboreando sua comida."

    $Asterion.change ("emotion","bowing")

    "Velhos hábitos são difíceis de morrer, de qualquer maneira; o minotauro se curva obedientemente
    antes de galopar para fora, de forma a permitir que você desfrute de sua refeição em solidão."

    hide Asterion
    with Dissolve(1.0)

    "Ele se vai antes que você possa pensar em pedi-lo para se juntar a você e, embora saiba que ele está
    a apenas um grito de distância, você acha melhor não pedir mais nada para ele."

    "Assim que sua fome é saciada, o sono cai sobre você em pouco tempo.
    Você coloca a bandeja ao lado do sofá e fecha os olhos."

    scene bg black
    with Dissolve (2)

    "Os últimos sons que você ouve são o leve clique dos cascos de Astério contra o
    chão e o tilintar dos talheres enquanto ele carrega suas sobras de volta para
    a cozinha."

    if global_affection >= 3:
        "Um passo lento e furtivo atinge seu cérebro semiconsciente através
        da névoa do sono agitado, seguido por uma repentina sensação de calor e
        uma pressão suave por todo o seu corpo."

        "Você logo cai em um sono fácil e profundo."

    $Asterion.change ("leftarm","loose")
    $Asterion.change ("rightarm","loose")
    $Asterion.change ("emotion", "contemplative")
    stop music fadeout 3.0
    pause 2
    scene bg asterionbed
    with Dissolve (1)


##############################################################################
#                      CHAPTER 6.3: ASTERION IS ALONE
##############################################################################

    $chapter = "Hades"
    call screen ChapterTransition("Hades", "Arrival", 'Hades')
    pause 0.5
    $save_name=output_save_name("Hades")


    play sound "sfx/clink.ogg"

    show Asterion:
        xalign 0.1 yalign 1.0
        ease 2.0 xalign 0.5
    show blackback:
        alpha 0.5
    with Dissolve(2)


    "A maçaneta clica atrás de Astério. Seu sorriso persiste à medida que
    ele aprecia o calor desta noite."

    "As bochechas do minotauro começam a doer por causa dos sorrisos, uma sensação estranha depois
    de décadas trancado."

    "Sua garganta também está dolorida por falar. Tudo o que ele tenta dizer
    agora sai apenas como um murmúrio rouco."

    "Seu corpo em recuperação o surpreende às vezes. O fato de se mover não doer
    mais, quão rápido ele está mesmo em um ritmo lento."

    "Esta força renovada o surpreende. Ele teve uma experiência difícil manuseando
    as frágeis taças e ferramentas pequenas e delicadas no salão."

    "Similarmente, fechar a porta sem bater
    agora mesmo foi complicado."

    $Asterion.change ("emotion", "neutral")

    "No entanto, agora ele está sozinho em seu quarto."

    "Está silencioso."

    "E um silêncio como este, depois de qualquer noite em que as bochechas acabam doendo
    de tanto sorrir, é tão opressivo quanto ser levado embora do paraíso."

    "O silêncio pode ser imperdoável."

    "A voz e a respiração do Mestre, a sutil mudança na mobília enquanto
    ele se movia pelo quarto, o som de seus próprios passos... tudo se foi."

    show Asterion:
        ease 1.0 xalign 0.6 yalign 2.0

    "Não há olhos o observando,
    não há nada para dizer ou fazer neste quarto deserto."

    "Ele deita em sua cama, olhando para o teto.
    O quarto não possui janelas, apenas uma única lâmpada brilhando no alto."

    "Astério balança a cauda — o tufo de cabelo no final o presenteia
    com um único som."

    $Asterion.change ("emotion", "tired")
    "Ele agarra o travesseiro sob sua cabeça.
    Seus dedos se contorcem em punhos trêmulos e a luz imprime uma mancha em seus olhos."

    "Os cantos de sua boca curada doem. Já se passaram décadas desde a última vez que ele sorriu tanto."

    "Largado sozinho, não há distrações para evitar os pensamentos sombrios."

    "Sobre aquele Mestre e todos os humanos envolvidos."

    "\"A humanidade é uma sentença por si só,\" ele pensa. \"Ser apenas
    meio-humano e governado por aqueles que nunca serei parecido.\""

    "O minotauro se pergunta quão grande é a lacuna que impede os homens de enlouquecerem.
    É fácil mostrar bondade no começo, como Clément fez, mas, eventualmente,
    eles ficam entediados."

    "E homens entediados são realmente perigosos."

    "Quanto tempo vai demorar para este Mestre aprender, o minotauro se pergunta.
    Geralmente começa bem simples — no início ele se torna o brinquedo deles.
    Um boneco."

    "Mas não vai parar por aí. Os humanos frequentemente anseiam por novas emoções."

    "Clément foi um caso especial, um homem que começou bom, mas enlouqueceu como nenhum
    antes. Mas sim, havia muitos mestres que tinham esta mesma semente neles,
    apenas com a diferença de que germinava mais devagar."

    "Até mesmo o Mestre Jean-Marie a tinha, até certo ponto. Aquela vez..."

    show Asterion:
        ease 0.6 yalign 1.6

    "Astério se joga para cima, impedindo-se de prosseguir nesta estrada.
    Pensamentos muito sombrios para uma hora tão tardia. E, de que importa
    agora, pensar sobre os mortos muito bem enterrados?"

    "Sua mente volta ao Mestre atual."

    "Uma única boa noite não compensa um passado terrível e um
    futuro assustador."

    "Astério pensa de volta sobre Argos e seu contrato, e como o Mestre
    lidou com isto."

    python:
        try:
            myVar = ArgosContract
        except:
            ArgosContract = "Signed"

    if ArgosContract == "Signed":
        "O Mestre [player_name] o assinou."

        "Havia uma pegadinha? É bem possível, com base em experiências passadas."

        "Mas seja qual for o risco, Astério sente um alívio fluindo através de si mesmo.
        Um Mestre é mais perigoso quanto mais inteligente for."

        "É uma benção que, em todos esses anos, nenhum humano tentou usar o poder do Hotel
        para fazer mal àqueles do lado de fora. Até mesmo os piores senhores contentavam-se
        em usá-lo para seu próprio hedonismo."


    elif ArgosContract == "Contested":
        "O Mestre [player_name] discutiu com a cobra, tentou contestar seus termos."

        "O minotauro conhece bem o delicado equilíbrio que vem com os Mestres.
        Alguém muito inocente pode ser enganado pela cobra, mas um senhor muito espirituoso
        é perigoso por si só."

        "O Hotel possui um grande poder, e é um milagre que até mesmo os mais cruéis
        dos mestres o tenham usado para seu próprio hedonismo ao invés de causar
        danos ao mundo exterior."


    elif ArgosContract == "Tricked":
        "O Mestre [player_name] conseguiu enganar a cobra."

        "Talvez isto deva trazer algum alívio para o minotauro — que os monstros do vale
        podem não ser um problema com um Mestre astuto — mas ele sabe que um líder
        espirituoso pode trazer perigos próprios."

        "Quanto mais inteligente o Mestre, mais perigoso ele pode se tornar. E pior serão
        os tormentos se o minotauro alguma vez o desagradar."


    if Chapter4_Terrorized_Asterion == "True":
        "Apesar dos desejos do minotauro, [player_name] o enviou para o vale."

        "Arrepios correm a partir da parte de trás de seu crânio até a espinha.
        Talvez tenha sido apenas um engano, ele não sabia o que ia acontecer. Pode não ter
        sido malícia. Mas as memórias de Clément continuam o atacando."

        "Ele sabe que deve ser cauteloso. Gostaria que não fosse este o caso,
        mas ele repetiu esse cenário em sua cabeça de novo e de novo nas décadas
        em que esteve trancado na câmara fria."

        "Não há muito que ele possa fazer contra os comandos de um Mestre,
        mas há contingências."


    if player_background == "speedrunner":
        "Mestre [player_name]... é um Mestre incomum, Astério pensa.
        Ele não para de falar sobre assuntos tão peculiares."

        "Video games isso, estratégias aquilo, otimização, seguidores...
        Conceitos estranhos não dados o tempo ou atenção necessários para serem assimilados."

        "Os tempos com certeza mudaram. É comum para as pessoas realizarem essas mesmas tarefas inúteis e
        repetitivas de novo e de novo sem nenhum propósito além de conquista pessoal?"

        "Astério já serviu a pessoas muito excêntricas antes. Boêmios, aristocratas confinados,
        párias e exilados que encontraram caminho até o hotel."

        "Tão distantes da sociedade como eram, eles estavam cientes disto.
        Mas o Mestre [player_name] discute tudo de uma forma tão pragmática."

    show Asterion:
        ease 2.0 yalign 2.2

    "O minotauro continua pensando até a exaustão, analisando cada
    possibilidade em relação a este novo Mestre."

    "Ele não percebe a sonolência vindo, nem o misericordioso abraço
    dos sonhos."
    scene bg black
    with Dissolve (4)
    pause 2.0
    play music "music/ariadne.ogg" fadeout 3.0 fadein 3.0
    "{i}O minotauro sonha."

    "{i}Um campo de flores brancas balançava sob uma fria brisa.
    Ele estava deitado de bruços no solo e os caules e folhas das flores
    faziam cócegas em suas costas como se estivessem tentando tirá-lo do sono."

    "{i}O solo estava úmido e cheirava a petricor e densa vegetação.
    Astério acariciou, arranhou, sentiu a água da areia se
    infiltrando em seus pelos."

    "{i}Tudo doía — a cada batida do coração, sua cabeça e olhos eram
    martelados. Seu corpo inteiro queimava em exaustão, tonto e nauseado."

    "{i}Mas, acima de tudo, seu pescoço — queimava como se um fio quente de metal
    o estrangulasse."

    "{i}O minotauro tentou respirar, mas era como se seus pulmões não conseguissem
    puxar o ar. Isto o teria deixado desesperado, não fosse pela dor avassaladora
    o distraindo."

    "{i}O tempo passou — quanto tempo ele não podia dizer. Astério tinha apenas o
    solo, úmido e aromático, e as flores balançando em cima dele."

    "{i}Ele cavou no solo argiloso. A textura áspera escorregando entre seus dedos
    tornava a dor suportável."

    "{i}E então — um calafrio correu de seu crânio através de sua espinha até a ponta
    de sua cauda."

    "{i}Ele respirou fundo e pôde ouvir seus próprios grunhidos irregulares de alívio.
    O minotauro sacudiu as orelhas enquanto seus plenos sentidos voltavam."

    "{i}O vento oscilante, ele podia ouvi-lo novamente, agora acompanhado ao
    farfalhar das folhas. Ele apoiou o peito para cima, sustentando-se em seus
    braços ardentes, e o paladar voltou para ele."

    "{i}Ferro. Ele tossiu e sangue frio e escuro escorreu de sua boca.
    Caiu no pelo branco de sua mão."

    "{i}Sua lingua permaneceu coberta com o óleo preto. Era amargo como o cheiro
    esfumaçado de uma forja. Ele conhecia bem este cheiro."

    "{i}Enquanto tentava se recompor, o sangue pingou
    no solo. Seu pelo permanecia manchado de vermelho enquanto o óleo escuro
    pingava."

    "{i}\"Sangue amaldiçoado,\" ele pensou. Mas outra coisa também veio à
    mente — o calafrio que o trouxe de volta."

    "{i}Estava sob sua língua; um caroço duro e gelado. Ele tentou cuspir fora,
    mas sem sucesso."

    "{i}Suas entranhas chacoalharam e ele perdeu o controle. Ele abriu a boca para vomitar,
    mas nada saiu."

    "{i}Passou-se mais uma hora antes que ele conseguisse levantar e observar o horizonte."

    "{i}Não havia céu acima, apenas pedras de pontas afiadas apontando para baixo como
    facas. O próprio horizonte estava pintado com rios serpentinos, suas águas
    batendo nos arredores e deixando rastros de espuma."

    "{i}A terra estava escura e, ainda assim, a luz parecia vazar de todas as superfícies.
    As estalactites do teto brilhavam turquesa, o campo de flores cintilava
    com luzes brancas quando a brisa soprava."

    "{i}O próprio solo brilhava com um subjugado tom quase púrpura tíria. E a brisa
    detinha um certo frescor. As águas turbulentas dos rios encheram o ar
    com pequenas gotas."

    "{i}Água pingava do teto aqui e ali, com uma graça quase
    preguiçosa; como um deus soltando presentes de cima para as pessoas abaixo."

    "{i}Um homem esperava na margem do rio, olhando para o minotauro.
    Ele acenou e, ali mesmo, a mente de Astério se acalmou."

    "{i}Esta linda terra era sua benção. O nó em sua garganta e o caroço sob
    sua língua seriam as últimas dores que ele sentiria, para sempre."

    "{i}Ele havia sido libertado."

    $chapter = "Capítulo 5"
    call screen ChapterTransition("Capítulo 5", "Leve inauguração")
    pause 0.5
    $save_name=output_save_name("Capítulo 5")

    $Asterion_UN = False
    stop music fadeout 3.0
    pause 4.0
    #Add some kitchen noises.

    "Você acorda com o som dos cascos de Astério clicando no chão de madeira
    bem atrás de você."

    play music "music/IslandJourney.ogg" fadeout 1.0 fadein 1.0
    scene bg oldquarters
    with Dissolve(1.0)

    $Asterion.change ("emotion","neutral")
    $Asterion.change ("leftarm","loose")
    $Asterion.change ("rightarm","loose")
    show Asterion
    with Dissolve(1.0)

    $Asterion.change ("emotion","bowing")
    $Asterion.change ("leftarm","raised")

    asterion "Bom dia, Mestre. Sinto muito pelo barulho,
    não tive a intenção de acordá-lo."

    if global_affection >= 3:
        "É fácil ignorar as palavras do minotauro enquanto você está
        aconchegado no sofá envolto por um cobertor."

        "Não fosse a luz do sol brilhando diretamente em seus olhos e o cheiro de café da manhã,
        teria voltado a dormir. Você se desprende do
        calor de seu cobertor."

        "Você dá a Astério um sorriso atordoado enquanto se levanta e ordenadamente dobra o cobertor
        antes de deixá-lo no sofá."

        you "Eu dormi muito bem. Obrigado, Astério."

        $Asterion.change ("emotion","smiling")

    else:
        you "Não se preocupe com isso, eu dormi o suficiente."

    asterion "Ah, isto é um alívio. Bem, eu fui em frente e fiz um café da manhã para você."

    "Às vezes é fácil esquecer quão excepcionais são as circustâncias em que você
    se encontra. Esperar pelo café da manhã é uma coisa tão mundana, mas basta
    um vislumbre de Astério para que a fachada de normalidade desabe."

    "É fácil achar chocante a cura rápida de Astério, mais até que o próprio
    Hotel. Ele já estica as roupas que ontem pareciam grandes demais."

    $Asterion.change ("emotion","neutral")
    $Asterion.change ("rightarm","hips")
    $Asterion.change ("leftarm","loose")

    if Asterion.favoriteClothes == "40s":
        "Falando das roupas, ele está vestindo aquele mesmo traje antigo de ontem."

        "Pode-se dizer que há quase um toque de nostalgia na forma como ele se veste,
        como se quisesse se ligar ao passado."

        "Ou pode ser por uma questão mais prática — que este seja o
        traje que você o pediu para vestir."

        you "Diga, Astério."

        asterion "Sim, Mestre?"

        you "Sobre suas roupas, isso é tudo o que você tem para vestir?"

        $Asterion.change ("emotion","sad")

        asterion "Sim, é tudo o que pude encontrar. Acredito que Clément jogou fora a maior parte de minhas roupas,
        assim como ele se desfez do vinho. Tudo o que resta é minha roupa atual."

        asterion "E, hm, uma perizoma velha."

    else:
        you "Vejo que a camisa está cabendo melhor em você. Gostou dela?"

        $Asterion.change ("emotion","smiling")
        asterion "Sim, agradeço muito o gesto, Mestre.
        Não sobrou muito no meu guarda-roupa, exceto minhas roupas antigas de quando
        Jean-Marie era meu Mestre e uma perizoma velha."

    if player_background == "arts":
        "Você se lembra do que é uma perizoma de seus estudos de arte clássica.
        Não é surpresa que Astério seja um cara antiquado e esteja usando
        uma tanga no estilo dos anos 1500 A.C por baixo das calças."
    else:
        you "Perizoma?"
        $Asterion.change ("emotion","surprise")
        asterion "...Devo ter pulado esta parte. Sinto muito."
        $Asterion.change ("emotion","tired")
        asterion "É-é um antigo estilo de tanga. É o que vestíamos em Creta."

    if Asterion.favoriteClothes == "40s":
        you "Bem, você não pode simplesmente usar as mesmas roupas todos os dias.
        E roupas de 70 anos, ainda por cima. Talvez você possa tentar algo mais moderno?"

        you "Nós podemos simplesmente invocar água e comida aqui, não é?
        Com certeza eu posso conseguir algumas roupas para você também."

        $Asterion.change ("emotion","neutral")
        $Asterion.change ("leftarm","raised")
        asterion "É claro, Mestre. Simplesmente comande e o Hotel se submeterá à sua vontade."

        scene bg black
        with Dissolve (0.5)
        "O Hotel pisca ao seu redor enquanto a realidade se reescreve."
        "Você imagina uma camisa que poderia se ver vestindo. É uma tarefa simples."

        if player_background == "humanities":
            "Algo clássico e minimalista..."
        if player_background == "tech":
            "Algo consciente de si e fascinante..."
        if player_background == "math":
            "Algo eterno e poderoso..."
        if player_background == "arts":
            "Algo estiloso e adequado para um minotauro..."
        if player_background == "leader":
            "Algo ousado, corajoso e que exale confiança..."
        if player_background == "speedrunner":
            "Algo {i}minimalista, fascinante, poderoso, estiloso e corajoso...{/i}
            Mas, acima de tudo: {i}clássico.{/i}"

        scene bg oldquarters
        with Dissolve(0.5)
        show Asterion
        "Do nada, um pacote aparece em suas mãos.
        É um exemplar de calça jeans e uma camisa com decote V que você criou.
        Astério observa, visivelmente curioso."

        $Asterion.change ("emotion","smiling")
    else:

        you "Não precisa ficar envergonhado.
        Fico feliz que você gostou da camisa o suficiente para vestir de novo."
        $Asterion.change ("emotion","smiling")
        $Asterion.change ("leftarm","raised")

    asterion "Talvez seja apropriado que eu tenha mais roupas modernas para vestir.
    Hoje pode ser um dia especial."
    $Asterion.change ("emotion","contemplative")
    asterion "Agora que a lareira está acesa, os hóspedes podem encontrar o
    caminho para o hotel novamente."
    $Asterion.change ("emotion","neutral")
    asterion "Eu quero causar uma boa impressão.
    Talvez as roupas que escolhi sejam inapropriadas, eu não saberia.
    Afinal, já faz muito tempo."

    if player_background == "leader":
        $Asterion.change ("emotion","smiling")
        asterion "Algo sobre a maneira como você se comporta, Mestre..."
        asterion "Você me parece bastante seguro em sua atitude e tomada
        de decisão. Uma pessoa firme. Estou inclinado a acreditar que seu
        julgamento sobre o que é apropriado deve ser confiável."

    if player_background == "speedrunner":
        $Asterion.change ("emotion","sad")
        asterion "Eu... Seu estilo é... incomum, Mestre.
        Talvez realmente tenha se passado muito tempo.
        Não posso fazer nada a não ser confiar em seu julgamento."

    $Asterion.change ("emotion","neutral")
    $Asterion.change ("rightarm","hips")
    $Asterion.change ("leftarm","loose")
    $Asterion.change ("underwear","loincloth")

    asterion "O que devo vestir hoje, então?"

    contract "Para vestir Astério, selecione uma das categorias no lado esquerdo da
    tela e, em seguida, selecione as roupas que deseja que Astério use na direita.\n
    Quando terminar, clique no botão \"Concluído\"."
    $chapter6nude = False
    $reroll=False
    $chapter6LieAboutUndies = 0
label chapter6_wardrobe:
    call screen dayManager("wardrobe")
    if "vneck" in Asterion.clothes:
        $Asterion.change ("emotion","smiling")
        "Astério parece curioso sobre suas novas roupas. Ele observa o padrão da camisa,
        percorre a mão através do tecido da calça jeans e ajusta a cauda para
        passar por um buraco abaixo do cinto."

        asterion "Já vi este tecido antes. Deixe-me pensar..."

        asterion "Acredito ter visto em um minerador americano. Ele havia perdido sua casa
        após a quebra da bolsa de valores de Wall Street. As calças dele pareciam mais...
        resistentes, apesar de desgastadas por causa do trabalho."

        asterion "Este tecido é comum hoje em dia, Mestre?"

        you "Sim, muito. Basicamente todo mundo tem pelo menos um exemplar de calça jeans hoje em dia."

        $Asterion.change ("emotion", "contemplative")

        asterion "Engraçado como as coisas tomaram este rumo. Me lembro que esse tipo de roupa
        era mal visto naquela época. É sempre fascinante quando as roupas da classe trabalhadora tornam-se
        moda mesmo entre aristocratas. Já vi isso acontecer."
        $Asterion.change ("emotion","neutral")

        if player_background == "humanities":
            "Astério observa a camisa."
            $Asterion.change ("emotion","sad")
            asterion "Uma guirlanda de folhas de louro?"
            asterion "Lamento terrivelmente questionar o julgamento de meu senhor,
            mas... por que? Receio que não entendi muito bem."
            $Asterion.change ("emotion","tired")
            you "Parece suntuoso para mim. Eu já vi algumas enfeitando a minha universidade.
            Representa a realização acadêmica. Além disso, é comum em
            símbolos atléticos. Simboliza vitória, não?"
            you "Acho que é bastante adequado, para ser honesto. Você é muito
            culto e, com o benefício de ver você como está hoje, eu diria que o atletismo
            também combina com você."

            if global_affection >=3:
                $Asterion.change ("emotion","contemplative")
                you "Ontem mesmo você estava me contando sobre {i}Notre Dame
                de Paris{/i} e os livros do Victor Hugo. Isso diz coisas sobre
                você."

                you "Além disso, também tem o tom de azul que eu escolhi."

                $Asterion.change ("emotion","tired")

                asterion "Perdão?"

                you "Esse tom de azul é usado pela Organização das Nações Unidas.
                É um orgão internacional com várias missões humanitárias e de
                manutenção da paz."

                you "Acredito que tenha a ver com o que você me contou sobre a missão do Hotel,
                não? Nós estamos dando um lar para aqueles que estão perdidos e não têm
                a quem recorrer."

                you "É um esforço humanitário. Se qualquer um merece vestir isso,
                esse alguém é você."

                pause 2
                "O minotauro olha para seus olhos, como se esperasse uma reviravolta ou piada.
                Seu olhar permanece fixo, ligeiramente mudando ao perceber que você
                está sendo honesto."

                $Asterion.change ("emotion","contemplative")

                asterion "Eu...eu não sei o que dizer. Isto é —"

                pause 1

                $Asterion.change ("emotion","tired")
                "Ele engasga no meio da frase. Por mais que tente esconder,
                os olhos do minotauro o denunciam. Eles ficam nebulosos —
                ele os estreita e olha para o chão."

                "Ele inspira e expira, inspira e expira. Mas, assim que fala, sua
                voz falha, saindo rouca e desafinada."

                asterion "Obrigado. Isso é muito gentil de sua parte."
                pause 2

                $Asterion.change ("emotion","bowing")
                "E então, como se percebesse o baixar de sua guarda, seu eu
                profissional retorna."

                asterion "Fico grato por seu elogio, meu senhor, e
                cuidarei de seu presente."

                asterion "..."

                $Asterion.change ("emotion","contemplative")
                asterion "...Cuidarei, sim."

                $Asterion_UN = True

            else:
                you "É fácil imaginar você até os ombros em uma pilha de livros. Caramba, você daria
                um ótimo acadêmico se isso for algo que você gostaria de fazer algum dia."

                $Asterion.change ("emotion","contemplative")

                asterion "Devo discordar respeitosamente, Mestre. Eu nunca fui
                formalmente ensinado sobre nada, do que eu sei, sequer?"

                you "Muita história, para começar."

                asterion "...Eu não cheguei a testemunhar nada dela. São todos relatos de
                segunda mão. E, ainda assim, eu sei apenas sobre os tempos depois que o Hotel
                foi instaurado."

                asterion "Há mais séculos dos quais nada sei do que aqueles
                que conheço um fragmento."

                asterion "Também não sei muito sobre minha terra natal.
                Eu fui embora tão cedo."

                asterion "Ainda assim, suas palavras são gentis, meu senhor."

                $Asterion.change ("emotion","smiling")
                asterion "Cuidarei desta camisa que você me deu."

        elif player_background == "tech":
            "Astério encara a camisa com a testa franzida."

            asterion "..."

            asterion "Hmm... Mestre, o que isso significa?"

            you "Ah, é uma definição de classe. Pensei que ficaria legal."

            "Sua resposta só serve para deixá-lo ainda mais confuso."

            you "Suponho que você nem saiba o que é um computador."

            asterion "Peço desculpas. Não, eu não sei."

            you "Por onde eu sequer começo...? Digamos apenas que, nos últimos 70 anos,
            desenvolvemos máquinas que fazem cálculos complexos e automáticos a uma taxa e escopo
            que os humanos não são capazes de efetuar."

            you "Eventualmente, os cálculos ficaram cada vez mais complexos e adaptamos as tarefas
            automatizadas que essas máquinas executam para fazer mais que apenas aritmética."

            $Asterion.change ("emotion","surprise")

            asterion "Interessante."

            you "Eu trabalho com essas máquinas. O código na sua camisa é parte de uma instrução que
            colocamos nelas para realizar uma tarefa para nós."
            $Asterion.change ("emotion","neutral")

            asterion "Não tenho certeza se entendi. Você me enviaria instruções
            por meio desta máquina?"

            you "Não, não, esquece. Na verdade é... uma espécie de piada interna.
            Pensei que ficaria legal em você."

            $Asterion.change ("emotion","contemplative")

            asterion "Entendo."

        elif player_background == "math":
            "Astério parece confuso com o padrão de sua camisa.
            Ele franze a testa, examinando-o lentamente, e então um sorriso caloroso
            aparece em seu rosto."
            $Asterion.change ("emotion","contemplative")

            asterion "Eu sei o que é isso. A espiral de Fibonacci."

            you "Sim. Eu sempre gostei desse padrão. Costumava rabiscar o tempo todo nas
            margens dos meus cadernos quando estava em aula."

            asterion "Mais de um matemático esteve no Hotel. Meu
            amigo da cozinha, aquele com quem eu saía à noite,
            ele me contou sobre isso. Como se repete na natureza."

            asterion "Ele era um bom amigo."

        elif player_background == "arts":

            "Astério observa o padrão em sua camisa."

            asterion "Meandros."

            you "Sim. Eu achei apropriado. Faz você parecer um pouco com um
            vaso decorado em um padrão geométrico."

            you "Pensando bem, espero que não traga lembranças ruins de
            ter ficado no labirinto."

            $Asterion.change ("emotion","contemplative")

            asterion "De modo algum. Bem, se tenho qualquer aversão ao símbolo, é
            porque os atenienses o tornaram popular."

            asterion "Mas eu o acho reconfortante. Traz memórias de volta.
            Eu agradeço, Mestre."

        elif player_background == "leader":
            "Astério leva um momento para observar a camisa."

            asterion "Cores fortes estão de volta à moda agora?
            Elas costumavam estar em voga cerca de uma década antes de eu ter sido preso,
            mas a depressão e a guerra os tornaram muito caros para a
            maioria."

            $Asterion.change ("emotion","contemplative")
            asterion "Houve uma jovem que encontrou seu caminho para o Hotel...
            Ela tinha um encanto aristocrata, sabe. O jeito como ela andava, suas maneiras,
            como ela abordava as pessoas ao seu redor."

            asterion "Muito educada. Mas também humilde. A Primeira Guerra Mundial
            destruiu a riqueza de sua família, ela chegou apenas com as roupas do
            corpo."

            asterion "Quando chegou, providenciei roupas adequadas para ela.
            Não era nada demais. Apenas um vestido simples."

            $Asterion.change ("emotion","smiling")

            asterion "Ela pediu que ele fosse amarelo, um tom bastante vivo. Apenas isso."

            asterion "Significava o mundo para ela, aquela pequena lasca de cor.
            Uma coisa tão pequena."

            $Asterion.change ("emotion","contemplative")

            asterion "Acredito que era um pedaço dela que estava faltando. Isto era
            bastante comum naquela época, a Primeira Guerra Mundial cobrou seu preço a tantas pessoas."

            asterion "E um vestido amarelo vivo foi o que a fez se sentir
            ela mesma novamente."

            you "Algumas pessoas chamariam rosa brilhante de brega e chamativo hoje em dia.
            Mas você pode fazer um saco de batatas funcionar como roupa se tiver a confiança."

            $Asterion.change ("emotion","smiling")
            asterion "Concordo."

        elif player_background == "speedrunner":
            "Astério observa sua camisa com a testa franzida — e um
            toque de aversão."

            you "Algo errado?"

            $Asterion.change ("emotion","surprise")

            asterion "N-não, está ótimo."

            $Asterion.change ("emotion","neutral")

            asterion "Não estou acostumado com a moda moderna, apenas isto.
            É comum que uma única peça de roupa tenha três cores,
            como este padrão?"

            asterion "Não me leve a mal, nunca deixo de me impressionar com os avanços no vestuário.
            A revolução têxtil foi algo interessante de se testemunhar."

            asterion "Uma camisa como esta, com cores vívidas e diferentes tecidas de maneira
            tão uniforme teria surpreendido a costureira mais habilidosa de Creta."

            $Asterion.change ("emotion","tired")

            asterion "É que... Espero que você possa perdoar minha grosseria,
            Mestre, mas algo sobre estas cores chamativas e incompatíveis me
            deixam desconfortável."

            "...Ele está zombando de seu senso de moda?"

            $Asterion.change ("emotion","smiling")

            asterion "Tenho certeza que me acostumarei com ela. Não é nada
            em comparação com as perucas empoadas que um velho Mestre
            costumava me fazer usar."

            $Asterion.change ("emotion","tired")

            asterion "Eu me arrepio só de pensar nisto. Deixe-me contá-lo,
            opioides do século 18 não eram motivo de piada."


        $Asterion.change ("emotion","smiling")
        asterion "Se recebermos hóspedes hoje, espero que isto não pareça intimidador para eles.
        Você fez uma boa escolha, Mestre."
        $global_affection += 0.5
    elif Asterion.clothes == "40s":
        $Asterion.change ("emotion","contemplative")
        asterion "Devo usar minhas roupas antigas, então?"
        you "Sim. Camisas brancas provavelmente nunca vão sair de moda.
        As calças são um pouco antigas e as pessoas raramente usam suspensórios fora
        de ocasiões formais, mas acho que você fica bem elegante com eles."

        $Asterion.change ("emotion","smiling")

        if global_affection >=3:
            "Você percebe um tom de rosa na bochecha esquerda dele, onde
            o pelo ainda está crescendo novamente."

        $global_affection += 0.5
        asterion "Agradeço o elogio, Mestre. Estas roupas são muito queridas
        para mim, me agrada saber que ainda são apropriadas nos
        dias de hoje."
    else:
        if reroll:
            if Asterion.underwear =="loincloth":
                asterion "... Muito bem, então."
                $ global_affection -= 0.5
        else:
            if Asterion.underwear =="loincloth":
                $Asterion.change ("emotion","surprise")
                asterion "Ah. Eu não esperava por isso.
                Mestre, as tangas voltaram em grande estilo depois de todos esses anos?"
                if global_affection >=3:
                    $Asterion.change ("emotion","sad")
                    asterion "É comum para os homens exporem seus peitorais novamente?"

                menu:
                    "As tangas estão de volta à moda?"
                    "Sim.":
                        you "Ah, com certeza. Talvez não exatamente as que você está vestindo,
                        mas roupas mais reveladoras estão na moda agora."
                        $Asterion.change ("emotion","smiling")
                        asterion "Ah, entendo. Curioso."
                        $chapter6LieAboutUndies = 1
                    "Na verdade, não.":
                        you "Bem, não exatamente. Homens vestem shorts na praia, por exemplo.
                        Talvez nos dias quentes de verão eles tirem a camisa, mas as pessoas
                        não andam realmente por aí de tanga."
                        $Asterion.change ("emotion","sad")
                        asterion "E eu estou... Mestre, você tem certeza que isto é apropriado para eu usar?"
                        menu:
                            "Talvez você pudesse usar outra coisa.":
                                you "Você está certo. Me desculpe, Astério. Me deixe escolher outra coisa."
                                $Asterion.change ("emotion","neutral")
                                $Asterion.change ("rightarm","hips")
                                $Asterion.change ("leftarm","loose")
                                $reroll=True
                                jump chapter6_wardrobe
                            "Não, você está ótimo.":
                                you "Acho que você fica bem assim. Eu prefiro que você vista apenas a tanga."
                                pause 2.0
                                $Asterion.change ("emotion","bowing")
                                $Asterion.change ("leftarm","raised")
                                asterion "...Como desejar."
                                $ global_affection -= 0.5
            else:
                $ global_affection -= 0.5
                $Asterion.change ("emotion","sad")
                pause 4.0
                asterion "..."
                pause 2.0
                menu:
                    "...":
                        pause 2.0
                        you "..."
                        $ global_affection -= 1
                    "O que tem de errado?":
                        you "O que tem de errado?"
                        pause 2.0
                        $Asterion.change ("emotion","tired")
                        asterion "P-por que eu estou nu?"
                        menu:
                            "Você fica fofo assim.":
                                "Astério parece desconfortável."
                                $ global_affection -= 0.5
                                asterion "É demais pedir para vestir alguma coisa?"
                                menu:
                                    "Você está certo. Foi mal.":
                                        you "Você está certo. Me desculpe, Astério. Me deixe escolher outra coisa."
                                        $Asterion.change ("emotion","neutral")
                                        $Asterion.change ("rightarm","hips")
                                        $Asterion.change ("leftarm","loose")
                                        $reroll=True
                                        jump chapter6_wardrobe
                                    "Você está ótimo.":
                                        you "Eu acho que você parece bem assim."
                                        pause 2.0
                                        $Asterion.change ("emotion","bowing")
                                        $Asterion.change ("leftarm","raised")
                                        asterion "...Entendo."
                                        $ global_affection -= 0.5
                            "Me deixe escolher outra coisa.":
                                you "Deixa para lá. Desculpe, Astério. Me deixe escolher outra coisa."
                                $Asterion.change ("emotion","neutral")
                                $Asterion.change ("rightarm","hips")
                                $Asterion.change ("leftarm","loose")
                                $reroll=True
                                jump chapter6_wardrobe
                            "...":
                                pause 2.0
                                you "..."
                                $ global_affection -= 1

    if Asterion.clothes =="nude" and Asterion.underwear =="none":
        pause 1
        $Asterion.change ("emotion","bowing")

        asterion "Receio não poder cumprir este comando."

        you "Como assim?"

        pause 1

        scene bg black
        with Dissolve(0.2)
        $Asterion.change ("underwear","loincloth")
        scene bg oldquarters
        show Asterion
        with Dissolve(0.2)
        pause 1
        $Asterion.change ("emotion","neutral")

        "As luzes do Hotel piscam. Astério agora está vestido, bem diante de seus olhos."

        asterion "De acordo com os contratos assinados por Mestres anteriores,
        estou proibido de me expor quando estamos esperando por hóspedes."

        asterion "Também não posso estabelecer um relacionamento com um hóspede."

        asterion "Estou submetido a uma variedade de restrições."

        asterion "Infelizmente, não posso cumprir seu comando, Mestre."
        if persistent.sfwMode == False:
            you "Mas você estava nu quando eu te encontrei. Qual é a diferença?"

            asterion "Não estávamos esperando por hóspedes naquele momento."
        $ global_affection -= 1
        $ abuse_act1 += 1
        $chapter6nude = True

#asterion is now wearing his clothes
    $Asterion.change ("emotion","bowing")
    $Asterion.change ("leftarm", "loose")
    $Asterion.change ("rightarm", "loose")
    asterion "Agora que este assunto está resolvido, não mais irei interromper
    seu café da manhã, Mestre."

    $Asterion.change ("emotion","contemplative")

    "Você começa sua refeição. Astério se senta na outra extremidade da mesa,
    ocasionalmente inspecionando a própria aparência. Quando você levanta os olhos do prato, o percebe
    arrumando o pelo aqui e ali."

    $Asterion.change ("emotion","bowing")
    $Asterion.change ("leftarm","raised")
    "Assim que você termina, Astério se curva e pega seu prato."
    hide Asterion
    with Dissolve(1.0)
    "À medida que ele o carrega para a cozinha, você o observa catar alguns
    restos e comê-los."
    pause 3
    "Pouco tempo depois, ele retorna."
    show Asterion
    with Dissolve(1.0)
    asterion "Eu tenho a permissão do Mestre para descer e inspecionar a lareira?
    Quero ter certeza de que tudo no hotel está funcionando corretamente."
    $chapter6StayInRoom = False

    menu:
        "Sim, você pode ir.":
            $chapter6StayInRoom = True
            $Asterion.change ("emotion","neutral")
            asterion "Obrigado, meu senhor."
            hide Asterion
            with Dissolve (1.0)
            "Astério sai. Você permanece em seus aposentos, pensando no que fazer
            pelo resto do dia."

        "Claro, eu posso ir com você.":
            $Asterion.change ("emotion","smiling")
            $Asterion.change ("leftarm","raised")
            asterion "Mesmo?"
            you "Sim. Quer dizer, se vamos receber hóspedes, talvez eu deva ajudar com as inspeções.
            Ver onde tudo está e essas coisas."
            $Asterion.change ("emotion","contemplative")
            asterion "...Muito bem. Por favor, siga-me."
            $global_affection += 0.5
            hide Asterion
            with Dissolve (1.0)

    scene bg black
    with Dissolve (3.0)

##############################################################################
#                      CHAPTER 7: THE FIRST GUEST
##############################################################################

    #First guest scene happens now.
    #If kota was picked first we jump to kota's intro, if not we resume the flow and go to Luke's"
    if first_guest == "Kota":
        jump KotaIntro

label LukeIntro:

    #"This is the scene that introduces luke"

#############################################################################
    #LUKE SCENE 1: CAPE CANAVERAL
#############################################################################
    $chapter = "Luke I"
    call screen ChapterTransition("Luke I", "Observação de estrelas e trauma")
    pause 0.5
    $save_name=output_save_name("Luke I")

    pause 4
    play music "music/Solidarity.ogg"
    queue music "music/AberdeenDoneIt.ogg"
    scene bg canaveral
    with Dissolve (4.0)

    if 'Luke' in persistent.known_guests:
        show screen SkipButton("LukeISkip", "Pular cena de hóspede")

    $Luke.change ("emotion", "neutral")
    $Luke.change ("bandanna", "True")
    $Luke.change ("dogtag", "True")
    $Luke.change ("glasses", "True")
    $Luke.change ("arm", "hip")

    show Luke:
        xalign 0.5 yalign 1.6

    "O grifo encontra-se sentado em uma mesa de piquenique úmida, bebericando sua cerveja
    americana diluída. Ele se curva para frente, apoiando os cotovelos nos joelhos,
    e inala o petricor flutuando do solo escorregadio da chuva."

    "Ele aprecia cada gole de sua Bud Lite morna, deixando-a descansar em seu
    bico até que todo o gosto desapareça antes de engolir."

    "Ele olha para frente em direção ao sítio de lançamento do Cabo Canaveral para evitar
    olhar para as famílias em volta. Ele diz a si mesmo para sorrir."

    $Luke.change ("emotion", "happy")

    "A mesa está revestida por uma fina camada de água salgada, soprada para o continente,
    vinda do mar não muito longe. Esta mesma condensação salgada reveste as penas,
    pele e bico do grifo."

    "Sua mente salta com cada lânguida piscada de seus olhos. A cerveja morna com
    um gosto residual de alumínio. Cheiro de petricor da chuva misturado com grama.
    O zumbido dos insetos."

    "A música pop chiclete tocando em um aparelho de som a alguns metros de distância. Ele bate os pés
    no ritmo da música enquanto coloca a mão sobre o bolso da frente onde
    guarda seu passaporte."

    "O sol poente brilhando em sua direção. Ele levanta a mão para proteger os olhos..."

    $Luke.change ("arm", "salute")
    $Luke.change ("emotion", "horny")

    "...E observa os encantadores homens curtindo com suas famílias,
    dançando ao som da música. Ele sabe que não deveria — eles são casados, afinal —
    mas o grifo não consegue se impedir de fantasiar."

    "Eles são robustos e peludos, molhados depois de um dia úmido sob o sol da Flórida.
    Suas camisas possuem manchas de suor. Alguns deles estão vestindo regatas que sobem até
    o estômago, revelando seus pelos corporais e umbigos."

    $Luke.change ("emotion", "wink")

    "Um deles em particular — um homem na casa dos 30 anos vestindo bermuda cáqui na
    altura do joelho e uma camisa desabotoada adornada com o logotipo da NASA —
    deixa o grifo sedento."

    "Ele é grato por seus óculos escuros. É fácil virar a cabeça enquanto mantém
    os olhos perfurados no prêmio. Pode-se imaginar que ele está apreciando
    os tons de rosa e laranja do sol poente."

    $Luke.change ("emotion", "hornier")

    "Mas não há como conter um desejo como o dele. É um homem encantador, claro,
    mas é a camisa que chama a atenção do grifo. Certamente é apenas um presente
    de uma loja de lembrancinhas, mas {i}talvez ele seja um engenheiro em seu dia de folga.{/i}"

    "Ele sempre teve uma queda por homens inteligentes assim. O que ele não faria para
    prová-lo, senti-lo, ouvi-lo comentar sobre seu último projeto."

    "O grifo abre outra cerveja e bebe. Mesmo com os olhos fechados,
    ele coloca a mão sobre a mesa e reconhece todos os entalhes que datam
    de décadas atrás."

    $Luke.change ("emotion", "horny")

    "Às vezes, este grifo evita pensar em palavras.
    Existe um perigo na eloquência."

    $Luke.change ("emotion", "annoyed")
    $Luke.change ("arm", "hip")

    "Mas ele não pode escapar delas para sempre. Ele verifica seu celular e
    rola as mensagens de sua mãe e irmãos — o contando que
    não poderiam comparecer este ano."

    show Luke:
        ease 2.0 xalign 0.55 yalign 1.8

    "O grifo se senta em sua mesa de piquenique, acariciando os entalhes que deixou
    ao longo dos anos, e é atacado por palavras."

    "Ele se chama Luke. Hoje, ele está sozinho com seus próprios pensamentos, e
    nada mais é tão assustador."

    "Esta é a primeira vez que apenas um deles veio assistir ao lançamento.
    A tradição deles manteve-se cumprida sem interrupção por décadas —
    uma visita anual ao Cabo Canaveral para assistir a um lançamento."

    "Ele sabe que tradições são poderosas —
    enquanto permanecerem intactas."

    "Mas ele está aqui e, com sorte, isto será o suficiente para mantê-la funcionando.
    Ele arrastará todo mundo com ele ano que vem, mesmo que seja a última coisa que ele faça."

    "Mesmo se, como hoje, o lançamento seja cancelado no último minuto.
    A verdade é que ver o foguete subir é uma surpresa feliz, mas não
    é uma parte realmente necessária da tradição."

    "O que importa é reunir a família para recordar."

    $Luke.change ("emotion", "horny")

    "O grifo abre outra lata de cerveja. Ele continuará bebendo até tarde
    da noite, às vezes lançando olhares de soslaio para todos aqueles homens héteros,
    casados e encantadores. Na esperança de que algum deles olhe de volta com os mesmos
    olhos lascivos."
#Added charm here.
    "Se olhassem em sua direção, veriam um humano dolorosamente comum — um
    americano de cabelos castanhos e pele um tanto bronzeada."

    "Luke dá um tapinha no passaporte mais uma vez. Quão frágil é a ilusão que
    impede as pessoas de verem sua verdadeira forma. Um simples livreto é
    seu principal escudo contra a detecção."

    "E este mesmo caderninho é o que impede todos esses homens de
    olharem para o grifo e o notarem.{w} Ele o torna
    imperceptível — caso olhassem em sua direção, ele seria como uma memória distante,
    um semblante humano indescritível, pelo qual suas mentes perderiam o foco."

    "Este é um fardo que todas as criaturas míticas devem carregar, ele sabe."

    "Luke pensa sobre sua infância, cercado por mais de uma dúzia de irmãos.
    Antigamente na velha casa da fazenda a leste de Austin."

    #scene nightfarmhouse

    "Durante o verão, toda a família dormia na varanda para refrescar.
    As crianças tornavam-se uma massa de membros empilhados, respirando em uníssono."

    "Os meninos em um canto, as meninas em outro. Luke e seus irmãos
    olhavam para as estrelas e traçavam constelações."

    "Pedro, o mais velho, contava as histórias por trás de cada uma delas —
    ou as inventava, como Luke percebeu anos depois, quando se alistou para o
    exército e foi ridicularizado por pensar que Órion estava tocando um violão."

    "Esta noite, Luke acalenta suas memórias. Ele dormirá aninhado em sua mesa de piquenique,
    observando as estrelas que nunca tocará."

    "Quando ele fala, possui a voz de um colegial e escuta Pedro,
    contando para ele todas as histórias inventadas."

    "Quase poderia-se esquecer as dificuldades e tentações de ser um
    adulto nessas horas."

    "Quando o dia amanhecer, ele será um homem a caminho de casa novamente."
    hide Luke
    with Dissolve(1)
    scene bg black
    with Dissolve(1)

#############################################################################
    #LUKE SCENE 2: GIVING TRICKY A RIDE
#############################################################################

    play sound "sfx/carstart.ogg"

    scene bg roadluke
    with Dissolve (2.0)

    "Dirigir afugenta as palavras. A mente consciente se desliga e tudo
    o que resta é estar no momento presente. Pura memória mecânica
    acompanhada do cheiro de seus assentos de couro rachados."

    "Longas viagens e milhares de quilômetros nunca assustaram Luke. Desde seus 20 anos,
    dez horas ou mais na estrada eram sempre bem-vindas."

    "Ele tinha uma casa — uma pequena cabana nas montanhas de um estado no interior
    a sessenta e cinco quilômetros da cidade mais próxima."

    "Nem um único vizinho, humano ou não. {w}Não valia a pena se esforçar
    para construir laços quando ele seria simplesmente esquecido."

    "Este era um efeito do passaporte e de todos os amuletos que ele usou —
    disfarçava o grifo como humano, mas também tornava a maioria das pessoas propensas
    a esquecê-lo."

    "Ele nunca conseguia permanecer lá por muito tempo. O isolamento o atingia,
    mas também não ficava muito nas cidades. Ser esquecido era demais."

    "A cabana era apenas um lugar para o qual ele tinha as chaves.{w} Seu carro era uma casa melhor
    — embora com todas as viagens ao longo dos anos ele tenha aprendido a não se apegar
    a nenhum veículo específico, mesmo que cuidasse deles como filhos."

    "O lar era a estrada em todas as suas formas. Normalmente carro, mas também trem, ônibus,
    até mesmo caronas. Quanto à cama, seu tempo no exército lhe ensinou que o chão é tão
    bom quanto qualquer cama."

    "Embora às vezes ele deitasse à noite e começasse a se perguntar: se estivesse em uma
    cama ao invés do chão, haveria alguém ao lado dele?"

    "Ele olha para o porta-copos à sua direita. Lá está seu passaporte, aquele
    livrinho azul. Sua bola com corrente."

    "Ele não pode mentir para si mesmo — não consegue ficar por muito tempo em um único lugar."

    "Mas ele também não consegue falar a verdade. Palavras, ele sabe, são perigosas.
    Para um homem como ele, esses momentos sem palavras, momentos de memória mecânica, parecem o mais próximo
    de paraíso que ele vivenciará por toda sua vida."

    "Apenas faça, seja, não pense muito sobre isso."

    "Um devaneio como este pode durar dias, mas é frágil. Basta uma
    única mudança imprevista e ele se estilhaça — e é isto o que
    acontece."

    "Bem à frente, algo chama a atenção de Luke — um homem caminhando na beira da estrada."

    "Ele não pensa. O impulso de ajudar um estranho simplesmente salta em frente
    à sua mente. Ele quer dá-lo uma carona."

    play sound "sfx/carstop.ogg"

    "O carro para bruscamente. Luke abaixa a janela do passageiro e
    se estica para cumprimentar o viajante."

    $Luke.change ("emotion", "neutral")

    show Luke:
        xalign 0.2 yalign 1.5 xzoom -1
    with Dissolve(1)

    show tricky smug:
        xalign 0.9 yalign 1.0 xzoom -1
    with Dissolve(1)

    "O grifo estica o pescoço para cima e para baixo para dar uma boa olhada no homem,
    mas fala antes mesmo de enxergar seu rosto."

    $Luke.change ("arm", "pointing")

    luke "Ei, você! Quer uma carona?"

    "O grifo ainda está avaliando o homem — bem abertamente, na verdade.
    Já se passaram alguns dias desde que ele viu qualquer ação e a última tarde no
    Cabo Canaveral apenas acelerou seus impulsos."

    "Luke encara descaradamente a virilha do estranho."

    "Ora, esta é uma surpresa feliz, ele pensa. Não é todo dia que um belo
    caronista embala seu próprio almoço — um grosso pedaço de salsicha de arrebentar calças!"

    $Luke.change ("emotion", "horny")

    hide tricky smug
    show tricky neutral:
        xalign 0.9 yalign 1.0 xzoom -1
        ease 1.0 xalign 0.8 yalign 1.5

    "???" "Ora, se não é um bom samaritano. Não se importe se eu quiser."

    "\"Samaritano,\" esta é uma palavra que Luke nunca ouviu antes.
    Ele guarda sua ignorância para si mesmo."

    "O viajante possui um sotaque firme com consoantes agudas e uma voz alegre
    e jovem. Assim que ele entra, Luke fica surpreso com o quão bem cuidado
    ele é — ele cheira a roupa lavada."

    "Esta é uma surpresa ainda melhor. Nunca é sexy quanto o carro acaba cheirando
    como um caminhão de lixo."

    play sound "sfx/carstart.ogg"
    $Luke.change ("arm", "hip")

    hide tricky neutral
    show tricky smug:
        xalign 0.8 yalign 1.5 xzoom -1

    "Os dois partem juntos com o rádio tocando uma doce melodia de jazz.
    Luke olha de soslaio para aquele belo pedaço de homem, mal conseguindo
    conter a necessidade latejante em suas calças."

    hide tricky smug
    show tricky neutral:
        xalign 0.8 yalign 1.5 xzoom -1

    "???" "Poucas pessoas hoje em dia dão carona para qualquer um que veem na
    estrada. É muito gentil de sua parte, senhor...?"

    $Luke.change ("arm", "salute")

    luke "Luke, só Luke. E o que posso dizer, não tenho a frieza de deixar
    alguém pra trás no meio do nada."

    $Luke.change ("arm", "hip")

    luke "Eu viajo bastante, sabe. Já peguei muitas caronas, então sempre
    tento ajudar e retribuir depois. A propósito, senhor, receio não ter captado
    o seu nome também."

    show tricky smug

    "Jean" "Jean, é assim que os meus amigos me chamam."

    $Luke.change ("emotion", "hornier")

    luke "Ah, então nós já somos amigos? Essa foi rápida."

    "Jean" "É claro! Eu estive na estrada há um bom tempo também e
    reconheço alguém que trata bem os viajantes.
    Pessoas como nós devem cuidar das necessidades uns dos outros."

    $Luke.change ("emotion", "horny")

    luke "Ah, claro, eu sei como tratar bem um viajante."

    "Luke lança outro olhar de soslaio para Jean e abre as pernas.
    A protuberância de sua ereção está à mostra para a observação do viajante."

    "Ele com certeza poderia aproveitar um boquete agora mesmo — isto é, dar um."

    $Luke.change ("emotion", "hornier")

    "Não é fácil chupar quando você tem um bico, mas a prática leva à perfeição
    — e Luke teve bastante prática."

    "É preciso um esfoço consciente para evitar parar e cair sobre
    Jean. {w}Ele deve ter um belo pau, Luke pensa.
    Mas pouco importa como parece seu pau, qualquer pau é bom o suficiente."

    "Luke se pergunta como Jean gosta de foder. Talvez ele agarre a cabeça do grifo
    e mande ver. Ele pode acabar com baba escorrendo pelo peito e suas
    penas todas arrepiadas."

    "É assim que uma foda de verdade deveria deixá-lo, ele pensa. Todo desgrenhado com
    o gosto de esperma persistindo em sua boca."

    "Ou talvez Jean seja o tipo de pessoa que tira quando está gozando.
    Isto também seria ótimo, ter porra secando em suas penas.
    Não é como se alguém fosse notar, uma vez que elas já são brancas,
    mas seria excitante se notassem."

    "Luke nunca se preocupou em esconder quão safado ele é.
    É sexy à sua maneira."

    "Ele também não se importaria em ser criticado.
    Curvando-se sobre o capô em chamas do carro, abrindo suas pernas e deixando
    o estranho transformá-lo em uma vadia."

    "E nada se compara a dirigir com porra em suas entranhas."

    "Mas, novamente, o viajante tem feições tão delicadas. É difícil imaginá-lo como um
    transão barra pesada. Talvez ele seja do tipo que faz amor."

    "O grifo sente a tensão aumentando no ar.
    Sua ereção roça contra sua calça. Não vai demorar muito até que
    uma mancha úmida se forme em sua virilha."

    "Seu devaneio, no entanto, matou a conversa. Ele quer mais daquela
    voz exótica — e se certificar de que o viajante está afim."

    $Luke.change ("emotion", "neutral")

    "\"Ele deve ser um daqueles gringos estranhos,\" Luke pensa."

    $Luke.change ("arm", "pointing")

    luke "Você tem um sotaque engraçado, Jean. Se importa de me dizer de onde você é?"

    show tricky neutral
    $Luke.change ("arm", "hip")
    "Jean" "Ah, eu sou da Europa. Mas você provavelmente consegue adivinhar que eu não vivo mais lá.
    Eu trabalho como entregador, então nunca paro por muito tempo em nenhum lugar."

    "Jean" "Na verdade, é por isso que eu estou aqui, para começar. Estou fazendo uma entrega
    em uma parada de caminhões alguns quilômetros adiante. Você só tem que me levar até lá."

    "Jean" "Você é americano, né? Esse aí é um sotaque do Texas que eu percebi?"
    $Luke.change ("arm", "salute")
    $Luke.change ("emotion", "horny")

    luke "Isso mesmo! Nascido e criado no Estado da Estrela Solitária e
    um orgulhoso veterano raiz!"
    $Luke.change ("emotion", "happy")
    $Luke.change ("arm", "hip")
    luke "Eu não moro mais lá, mas deixa eu te contar, não existe nenhum lugar
    como aquele. Os homens são homens, para começar, e nenhuma comida supera a nossa."

    $Luke.change ("emotion", "horny")
    luke "Já ouvi alguns dizerem que a culinária Cajun de Nova Orleans é melhor. E é boa
    mesmo, não me entenda mal, mas nada se compara ao nosso churrasco. {i}Nada.{/i}"
    $Luke.change ("arm", "pointing")
    luke "Eu já tive na Europa, experimentei a comida e o vinho de vocês.
    Não é muito ruim, mas vocês são meio elegantes e arrogantes um pouco demais."

    luke "Na época que eu fui pra lá, preferia comer minha ração militar do que o
    pão amanhecido que os franceses deram pra gente."
    $Luke.change ("emotion", "neutral")
    $Luke.change ("arm", "hip")
    luke "Eu não entendo todo o rebuliço com as baguetes e os croissants,
    naquela época eles não quiseram nem nos dar um pouquinho de manteiga."

    luke "Também nunca entendi o que tem de tão bom nos macarons, quando eu tive em
    Nanci, todos eles tinham gosto de xarope pra tosse. A comida francesa não é tudo isso."

    "A conversa faz Luke esquecer de sua ereção furiosa."

    "Ele está acostumado a ficar em silêncio e evitar palavras. Mas, é claro, ele está quase
    sempre sozinho e em movimento."

    "O prospecto da companhia quebra o gelo e todas as palavras
    saem derramando."

    "Palavras não são tão espinhosas quando você tem companhia."

    "E, embora alguns (senão a maioria) se sentiriam intimidados ou envergonhados com as
    divagações de Luke, o viajante abre um sorriso e acena com a cabeça."

    show tricky smug
    $Luke.change ("arm", "pointing")
    luke "Você já foi no Texas? Você tem que experimentar o pão de milho da gente,
    além de um belo hambúrguer com um Dr.Pepper gelado.{w} Quem bebe Pepsi vai pra forca!"

    luke "O bom e velho churrasco do Texas também, você tem que experimentar.{w} É o melhor em todo
    o maldito mundo e o resto que se foda."

    luke "Mas eu também não sei se um Europeu chique que nem você pode apreciar um hambúrguer de verdade.
    Já vi um de vocês tentando comer um com a porra de um garfo e faca!
    Aliás, não baniram as facas lá na Europa ou algo assim?"
    $Luke.change ("arm", "hip")
    luke "Texas vai fazer de você um homem! E se você for pra Houston algum dia,
    tem tanta coisa pra ver. Controle de Missão e o Centro Espacial, pra começar.
    Eles têm picolés de picles incríveis, você tem que experimentar esses."

    show tricky neutral

    "Jean" "Ah, eu já estive no Texas antes, sim. Mas admito que nunca passei
    por todas essas experiências, foi mal."

    "Jean" "Definitivamente não experimentei o churrasco de lá,
    tenho que resolver isso na próxima vez.
    Não posso cometer essa {i}faux pas{/i} de novo."

    $Luke.change ("emotion", "annoyed")

    "\"Aí está outra daquelas palavras europeias chiques,
    {i}foul pah{/i},\" pensou o grifo."

    "Jean" "Se você não se importa que eu pergunte, o que te trouxe até a Flórida?"

    $Luke.change ("emotion", "horny")

    luke "Ah, foi uma reunião de família. Minha mãe e todos os irmãos se juntam
    uma vez a cada ano pra assistir uma partida de foguete.{w} É a nossa tradição."

    luke "Mas a coisa toda foi pro brejo — todo mundo tava muito ocupado esse ano.
    Eu vim de qualquer jeito, é claro. Não posso deixar uma tradição morrer."

    luke "Mas até o lançamento me deixou na mão! A coisa toda atrasou."

    luke "Fiquei tão chateado que decidi simplesmente ir pra casa mais cedo. Normalmente eu
    paro em Fort Lauderdale pra uma ou duas semanas de diversão, mas percebi que não tava com
    o humor necessário pra isso."

    show tricky neutral

    "Jean" "Ah, sinto muito ouvir isso. E Fort Lauderdale...
    esse é um baita destino se você quiser festejar.{w}
    Talvez umas férias mais relaxantes te façam bem."

    "Jean" "Você já visitou a França. Sinto muito que você teve uma experiência ruim, mas
    talvez você devesse tentar dar outra chance à Europa.{w} Bruges é ótima nessa
    época do ano, é como um conto de fadas."

    "Jean" "Tem algum lugar que você gostaria de visitar?"

    "Luke pensa antes de responder. França está fora de questão, mesma coisa
    com a Alemanha. Itália, talvez. {i}Ou Grécia.{/i}"

    $Luke.change ("emotion", "happy")

    luke "Sim, tem um lugar. Eu sou três vírgula cento e vinte e cinco
    por cento Grego, sabe, é de onde veio minha família de vinte ou
    trinta gerações atrás!"

    $Luke.change ("emotion", "horny")

    luke "Quer dizer, claro, eu tenho muito nativo americano em mim também, por parte
    de mãe."

    luke "Mas eu sempre pensei em mim mesmo como Grego. Tenho que
    fazer uma visita à Nemeia algum dia, ver de onde vieram os meus ancestrais."

    "\"O Leão de Nemeia,\" Luke pensa.{w} Grande é a lacuna entre como um homem se vê
    e como ele é visto pelos outros."

    "O caronista vê um homem, um americano mestiço dolorosamente sem graça, mas,
    pelo espelho retrovisor, Luke enxerga seu verdadeiro semblante.{w} Um passaporte
    encantado é tudo o que mantém sua verdadeira forma escondida."

    $Luke.change ("emotion", "hornier")

    luke "Além disso, não dizem por aí que os gregos gostavam de fazer anal uns
    nos outros? Tenho que ver por conta própria se essa tradição ainda se mantém."

    show tricky smug

    "Luke começa a gargalhar enquanto Jean o observa, em silêncio. Depois que a
    risada do grifo cessa, ele dá ao homem um olhar de soslaio e
    sente a tensão no ar."

    "Pensamentos sombrios, no entanto, se vão rapidamente.{w} Novas necessidades tomam conta
    da mente do grifo."

    "Agora que a conversa foi devidamente encerrada, o tesão de quase uma semana
    sem transar joga toda a sua sutileza pela janela.
    Ele precisa de pau {i}agora{/i}, e ele tem um palpite de que o viajante pode virar nessa direção."

    $Luke.change ("emotion", "cocky")

    luke "Aí, amigo, se importa se a gente fizer uma parada rápida? Eu realmente preciso tirar uma água do joelho."

    show tricky neutral

    "Jean" "O carro é seu, meu caro. Você quem manda.
    Vou aproveitar a chance para fumar, também."

    $Luke.change ("emotion", "horny")

    play sound "sfx/carstop.ogg"

    "Luke freia de repente, denunciando sua ansiedade.
    Ele coloca o passaporte no bolso, verifica se há tráfego — não há
    nenhum — e salta para fora."

    scene bg roadside
    show blackback:
        alpha 0.4
    with Dissolve(1)
    show Luke behind blackback:
        xalign 0.9
        yalign 1.0
    with Dissolve(1)
    show tricky neutral behind blackback:
        xalign 0.1
        yalign 1.0
    with Dissolve(1)

    "O grifo caminha até o lado do carro onde Jean está e, de costas para ele,
    puxa o pau para fora. Ele sorri quando ouve a porta de Jean abrindo
    e fechando, e então o clique de um isqueiro."

    $Luke.change ("emotion", "hornier")

    "Luke abre as pernas e levanta o rabo levemente.
    Ele sente o olhar do viajante o perfurando por trás."

    "Jean caminha até ficar ao lado de Luke e abre o zíper da calça. O grifo
    encara a virilha do homem e faz o possível para ignorar a fumaça."

    $Luke.change ("emotion", "cocky")

    luke "Isso não parece natural? Dois homens mijando ao ar livre?"

    "Jean continua quieto."

    luke "Sabe, eu poderia ajudar você com isso."

    $Luke.change ("emotion", "cocky")
    show tricky smug

    "Jean" "Como é?"

    luke "Você me ouviu. Que tal eu chupar um gozo do seu pau aqui
    e agora?"

    $Luke.change ("emotion", "horny")
    "Jean" "Eu não acho que você tem o que é necessário."

    $Luke.change ("emotion", "cocky")
    luke "É mesmo é? Eu sou um pervertido, consigo aguentar o que você quiser."

    "Jean" "Sério? Você tem certeza disso?"

    $Luke.change ("emotion", "hornier")
    "A expressão de Luke diz tudo para o entregador.
    Jean solta uma gargalhada."

    "Jean" "Tudo bem. Depois não diga que eu não avisei!"

    "Jean" "Eu sou um homem de gostos refinados e requintados.{w}
    Só aceito homens igualmente ousados.{w} Sabe, eu gosto da boa
    e velha tortura de pênis e testículo."

    $Luke.change ("emotion", "surprise")

    "Jean" "Abaixe as calças, putão."

    luke "Espera, o que?"

    "Jean" "Você me ouviu. Abaixe as calças e se prepare."

    luke "Ok, você tá certo, isso não é minha praia."

    "Jean" "Não tão robusto agora, não é, gatinho? Pensei que você
    fosse um homem — não aguenta uma surra?"

    "A gargalhada de Jean ecoa através do matagal."

    $Luke.change ("emotion", "annoyed")
    luke "Só pra você saber, eu {i}consigo{/i} aguentar o que você quiser,
    mas eu não sou {i}tão{/i} estúpido."

    show tricky neutral
    "Jean" "Foi mal, rapaz, só não estou com vontade de receber um boquete.
    Eu não tenho um fetiche em chutar bolas, só queria ver você de cara."

    $Luke.change ("emotion", "surprise")
    luke "Seu filho da puta!"
    $Luke.change ("emotion", "happy")

    "A tensão no ar é difusa de uma só vez.
    Eles fecham o zíper em meio às risadas e voltam para a caminhonete com os braços nos ombros
    um do outro. Há um brilho casto e reconfortante entre os dois."


#############################################################################
    #LUKE SCENE 3: ARRIVING AT THE TRUCKSTOP
#############################################################################

    scene bg truckstop
    show blackback:
        alpha 0.4
    with Dissolve(2)
    play music "music/crickets.mp3" fadeout 1.0 fadein 1.0

    "O rolar da estrada fica mais lento assim que Luke começa a se aproximar da parada de caminhões.
    O lote está rachado até as bordas e as tampas das bombas de gasolina
    estão salpicadas de ferrugem vermelha."

    "A parada de caminhões acumulou seu quinhão de poeira ao longo do tempo. Apesar dos painéis
    azul-claros e das molduras de janela manchadas, manteve-se um centro à beira da estrada
    para os visitantes regulares."

    "Ainda há agitação na parada depois de todos esses anos."

    "Caminhoneiros conversando uns com os outros para cima e para baixo, a parte traseira do lote
    preenchida por caminhões de 18 rodas e a fumaça preta e espessa deixada para trás pelas picapes
    enquanto elas continuam suas jornadas na estrada."

    $Luke.change("emotion", "happy")
    show Luke behind blackback:
        xalign 0.1 yalign 1.0 xzoom -1
    with Dissolve(1)
    show tricky neutral behind blackback:
        xalign 0.9 yalign 1.0 xzoom -1
    with Dissolve(1)
    luke "Não tem nada parecido com isso, eu juro! Abra a janela e dê uma
    fungada nesse ar."

    "À medida que a caminhonete de Luke se move para a entrada do lote, Jean abaixa
    a janela e o cheiro misturado de gasolina e café da manhã 24 horas
    preenche o veículo."

    luke "Isso é o que eu chamo de {i}Americana{/i}."

    "Jean tosse forte, suas palavras se atropelando enquanto ele rapidamente
    rola a janela de volta para cima."

    show tricky neutral
    "Jean" "Isso é, hum, definitivamente outra coisa, posso dizer tranquilo."

    "Jean solta uma risada chiadeira e forçada, já parecendo um pouco mal."

    "Luke gargalha enquanto passa o braço por cima do ombro de Jean,
    entretido com o \"entusiasmo\" do entregador."

    "Logo após estacionar, os dois acabam saindo da caminhonete rindo como
    idiotas, zombando um do outro e falando sacanagem enquanto caminham."

    "Jean" "Sabe, Luke, eu não me importaria em pegar você qualquer dia desses de novo."

    $Luke.change ("emotion", "hornier")
    "A mente de Luke cai na sarjeta novamente."

    "Jean" "Não desse jeito, seu mentecapto. Eu faço entregas nessa rota com frequência,
    sabe. Tem um hotel reabrindo um pouco mais adiante na estrada e
    meu chefe pode enviar algumas remessas para lá em breve."

    "Jean" "Vou ser sincero, você está com cara de que poderia aproveitar um tempo de folga. Nada
    daquela vida de festa em Fort Lauderdale, quero dizer um lugar para relaxar um tempinho."

    "Jean" "Se você realmente ficar lá por um tempo, tenho certeza que a gente vai acabar se vendo
    de novo.{w} E eu ia gostar disso."
    $Luke.change ("emotion", "neutral")
    $Luke.change ("arm", "pointing")
    luke "Ah, mesmo, agora? Vou ter que aceitar isso, então. Não é muito
    comum fazer amigos na estrada. E eu quero dizer amigos que aparecem no mesmo
    restaurante ou parada mais do que uma vez a cada três semanas."
    $Luke.change ("arm", "hip")
    luke "Não é fácil conversar com alguém que você não vê muito,
    especialmente quando metade do tempo eles mal se lembram de você."

    "Jean" "O que, as pessoas têm dificuldade em lembrar de você? Acho isso difícil de
    acreditar, você é bem marcante."

    luke "Ah, é complicado. Você vai ver por conta própria...{w=0.2} é fácil
    se esquecer de pessoas que você conhece na estrada.{w} Não é algo que nós
    controlamos."

    "Jean" "Devo discordar respeitosamente. Eu não tenho nenhum problema
    em lembrar das pessoas que conheci nas minhas viagens."

    "Jean" "Bem, você vai ver. Eu não vou me esquecer de você, gatinho, especialmente se
    você ficar um tempo naquele hotel que eu mencionei. Vou estar bastante por lá,
    alguém precisa entregar caixotes naquele lugar empoeirado."

    "\"Vamos ver,\" Luke pensa, já ciente da tolice humana.{w} O maldito
    passaporte em seu bolso fará com que Jean certamente se esqueça dele."

    "Os dois chegam ao escritório do gerente bem ao lado da lanchonete da parada."

    "Jean" "Eu tenho que deixar esse pacote aqui, mas você devia tentar conseguir um quarto
    lá. Certamente parece que precisa dos hóspedes."
    $Luke.change ("emotion", "wink")
    luke "Vou pensar nisso. Hotéis podem deixar sua carteira mais seca
    que o Deserto de Chihuahua."

    "Jean" "Bem, ele {i}está{/i} reabrindo agora, eu não ficaria surpreso se eles
    estivessem fazendo algum tipo de desconto para os primeiros hóspedes."

    "Jean" "Só me liga ou manda um zap qualquer hora."

    "Os dois trocam números rapidamente antes de Jean estender a mão para
    Luke, oferecendo um aperto de mão cavalheiro."
    $Luke.change ("emotion", "happy")

    show tricky neutral:
        ease 1.0 xalign 0.7

    "Jean" "Foi muito bom te conhecer, Luke. Te vejo por aí, ok?"
    $Luke.change ("arm", "pointing")
    show Luke behind tricky:
        ease 1.0 xalign 0.4


    "Luke afasta a mão de Jean e dá um grande tapa nas costas dele,
    quase derrubando o pobre homem."
    luke "Cara, não é assim que você diz adeus a um amigo.
    Vai pela sombra, parceiro!"

    hide tricky
    with Dissolve(1)
    $Luke.change ("emotion", "neutral")
    $Luke.change ("arm", "hip")
    show Luke:
        ease 2.0 xalign 0.5 yalign 1.0

    "Os dois se separam e acenam enquanto se afastam um do outro."

    "Um homem pode sonhar — em ser lembrado e fazer amigos. A esperança é deleitável
    por si só, especialmente quando é tola. {w}Luke possui um sorriso esticado no rosto
    antes de perceber algo mais insistente: sua fome."

    "Ele pode muito bem se recompensar por ser o bom ‘Samaritano’ que é.
    Ele se afasta de sua caminhonete e se dirige para a lanchonete."
    $Luke.change ("glasses", "False")
    stop music fadeout 1.0

    hide blackback
    with Dissolve(1)
    play sound "sfx/clink.ogg"

    "O tilintar do sino da porta anuncia a entrada de Luke.
    Uma garçonete de rosto enrugado o dá as boas-vindas do balcão e
    pergunta seu pedido, caneta na mão."
    $Luke.change ("arm", "pointing")
    luke "Eu vou querer um café e dois donuts, se você tiver algum."

    "Garçonete" "Claro, querido. Se acomode, tudo bem?"
    $Luke.change ("arm", "hip")
    "Luke olha em volta brevemente e percebe que não há muitos assentos que
    não estão com o preenchimento estofado desgastado. O único assento — uma banqueta manchada,
    mas de veludo —- fica bem entre dois homens. Seus semblantes são largos o
    suficiente para se sobreporem ao assento vazio."

    "Luke pode abrir espaço para si mesmo, também. Ele segue seu caminho até o
    assento e, com um rápido \"perdão\", os dois se afastam para que ele possa se
    sentar. Mesmo assim, o pássaro está quase imprensado entre os dois homens corpulentos."

    "Pouco depois de se sentar, um prato com dois donuts frescos e uma
    xícara de café fumegante são dispostos bem na frente do grifo.
    Luke não perde tempo e começa a bebericar seu café."

    "Forte no sabor e no cheiro, é algo que ele vai amar até que suas
    penas caiam."

    "Assim que ele começa a comer, um bufo abafado vindo do lado chama sua
    atenção."

    $Luke.change ("emotion", "horny")
    show Luke:
        xzoom 1
    pause 1.0
    show Luke:
        ease 2.0 xalign 0.1

    show trucker clothes:
        xalign 2.0 yalign 1.0
        ease 2.0 xalign 0.9
    "Ele lança um olhar para o lado: uma besta corpulenta de homem lendo um jornal.
    Camisa sem mangas, mostrando que ele definitivamente porta alguns músculos."

    "O exército ensinou Luke a utilizar seus periféricos, ele saboreia cada olhar
    que direciona ao homem. Especialmente as espreitadelas na virilha."

    "\"Nada que não me daria um baita orgasmo,\" a águia astuta pensa para si.
    Caminhoneiros sempre acumulam lá em baixo. Com toda a testosterona extra que
    vem com o trabalho, precisa ir para algum lugar."

    $Luke.change ("emotion", "hornier")

    "Outra mordida do donut desce por sua garganta e Luke lança
    um olhar mais uma vez."

    "O grande caminhoneiro coça o rasgo exposto, sem se incomodar
    com o fato de que outras pessoas estão por perto. A visão também atiça
    a coceira de Luke, o excitando ainda mais."

    "Seu donut mergulha no café e Luke olha para o outro lado desta vez:
    um caminhoneiro mais velho que não perde tempo devorando um hambúrguer. Seu uniforme
    de caminhão abraça e aperta sua barriga antes de guiar para o colarinho desabotoado e bagunçado."

    "O grifo dá um puxão em sua própria braguilha, tornando sua ereção mais óbvia."

    show Luke:
        xzoom -1
    pause 1

    show trucker clothes:
        xzoom -1
        pause 1
        xzoom 1

    "Agora, para chamar a atenção de qualquer um dos dois, Luke vira um pouco a cabeça
    e encara o homem corpulento. Não muito tempo depois, o homem olha de volta e
    encontra seu olhar, em seguida resmunga e olha de volta para o papel."

    $Luke.change ("emotion", "horny")

    "Luke olha de volta para sua comida, depois volta a encarar novamente.
    O homem abaixa um pouco o jornal e dá um olhar mais longo na águia.
    Ele sorri pretensiosamente antes de puxar o jornal para cima novamente."

    "Dois minutos se passam antes de Luke dar outra olhada e pegar o homem
    olhando para ele antes de dar uma piscadela."

    show Luke:
        ease 0.5 xalign 0.3
        ease 0.5 xalign 0.2
    show trucker clothes:
        pause 0.2
        xzoom -1

    "Luke chuta levemente o pé do homem e os joelhos do bruto reflexivamente
    abrem mais. Ele encara a ereção escondida abaixo da borda do balcão.
    O grifo já dominou esta arte a essa altura."

    "Luke dá uma baixa risadinha, termina sua refeição e olha para o
    banheiro — um prédio separado do outro lado do estacionamento. Ele olha de volta para o bruto,
    inclina a cabeça na direção do prédio e, em seguida, sai para ir até lá."

    show trucker clothes behind Luke:
        ease 3.0 xalign -1.0

    show Luke:
        pause 1.0
        xzoom 1

    "Discreto e simples. Ele escuta duas vozes profundas murmurando bem
    atrás dele. Olhos de águia e audição aguçada são coisas que ele considera
    úteis mesmo depois de seu tempo no exército."

    show Luke:
        ease 3.0 xalign -1.0

    "Luke espera do lado de fora ao lado da caçamba de lixo até ver o caminhoneiro seguindo
    seu caminho para o banheiro. Depois de um minuto, Luke segue."

    hide Luke
    with Dissolve(1)

#############################################################################
    #LUKE SCENE 4: RESTROOM HOOKUP
#############################################################################

    play music "music/VindalooBlues.ogg" fadeout 1.0 fadein 1.0

    pause 1.0
    menu:
        "Desviar os olhos.":
            scene bg black
            with Dissolve(1)

            "Homens e seus desejos indecorosos."

            "Muitos são os pecados sedutores, atos desenfreados, desejos vergonhosos e prazeres
            passageiros que eles abraçam sob o manto da escuridão."

            "Pode-se imaginar o que tais homens ígneos fazem e que arrependimentos os tomam
            quando a batida de seus corações não é mais a única música trovejando em seus ouvidos."

            "Receio por este, demorará um pouco para essa música terminar,
            para mais homens encontrarem seu caminho até o banheiro e lá vagarem."

            "Quanto a nós, testemunhas, não há nada a se fazer senão girar os
            polegares até bem depois do pôr-do-sol. Muitas vezes, nada pode
            ser feito para impedir um homem de seguir suas escolhas lamentáveis."

            if player_background == "speedrunner":
                "Me perdoe se por acaso você acreditou que algo poderia ser feito para redirecionar esse rapaz a um lugar melhor."
                "Receio que o momento não seja propício para tal gentileza."
                pause 1.5
                "Tem uma fila se formando na porta do banheiro. Isso é completamente ultrajante.
                Eles poderiam pelo menos ser um pouco discretos."
                "E aqui estamos, ainda esperando."
                "Bem. Você é um estimado hóspede. Não temos muito aqui nessa precária parada de caminhões,
                mas, por favor, sinta-se em casa enquanto esperamos que esse deplorável encontro chegue ao fim."

                "Devo dizer que lamento terrivelmente. Isso era para ser uma espécie de chicotada, entende? Algo surpreendente.{w}
                Mas podemos ter ido longe demais em alguns lugares."

                pause 1.5
                "Só alguns."
                "Mas isso nos colocou em uma posição difícil, veja bem. Originalmente, todos os viajantes tinham que testemunhar..."

                pause 1.0

                "Seja lá o que esteja acontecendo lá dentro."
                "Ora, por que fizemos isso?{w} É…{w=0.2} como posso dizer...{w=0.2}
                Acreditamos que existem muitas maneiras de transmitir caracterização."

                "Agora, é claro, estaríamos mentindo se não reconhecêssemos o aspecto estimulante de tudo isso.{w}
                Sim, é estimulante.{w} Para alguns."

                pause 1.5

                "Minha nossa, eles estão tocando jazz agora. Isso não pode ser bom."

                "Voltando ao assunto, tomamos um momento de introspecção e reconhecemos
                que testemunhar o banheiro não era uma coisa boa de se ter como momento obrigatório na história."

                "Não foi nosso melhor momento, vamos apenas concordar nisso.{w}
                O aspecto obrigatório, veja bem, porque a escrita estava bem decente."

                "Mas isso levanta a questão, o que colocar como alternativa?"

                "Essa é difícil, como podemos transmitir toda aquela bagunça sem mostrar a jiripoca piando?"

                "Bem, descrever coisas desagradáveis de uma forma segura para a família é uma habilidade literária por si só."

                "Machado de Assis escreveu toda uma história
                em que o protagonista tinha uma fixação muito peculiar nos braços de uma mulher casada."

                "Isso foi nos anos 1800, escritores tinham que ser muito criativos ao falar de qualquer
                coisa mais picante que uma colherada de açúcar."

                "Para essa variação SFW, queríamos isso. Em outras circunstâncias,
                teríamos dado a Luke um monólogo de fluxo de consciência, mas você sabe
                que ele não gosta muito de toda essa coisa de \"voz interna\"."

                "Que, em retrospecto, é uma pena nessas circunstâncias.
                Lamento dizer que nunca teremos um \"Monólogo de Lucas Walker\" inspirado em James Joyce."

                "Então, tive que ir por outro caminho — vamos de algo minimalista."

                "E é disso que se trata essa cena, na maior parte citando um poema de
                Nag Hammadi chamado Trovão, Mente Perfeita."

                "É um ótimo poema, você deveria dar uma olhada."

                "Enfim. Desculpe por gastar seu tempo, e obrigado por jogar nosso jogo —
                em particular, somos gratos por você ter dado uma chance ao passado de Speedrunner."

                "Vamos apenas fingir que Luke e seus amigos estavam desentupindo um cano.
                Um serviço público em benefício ao pobre proprietário da parada de caminhões, que não pôde contratar um encanador."

                "Agora, vamos voltar para a história."



            else:
                "O silêncio da mente de um indivíduo muitas vezes age como um escudo. Sua mente deve estar quieta,
                focada apenas na pura perfeição mecânica, enquanto a cena se desenrola ao seu redor."

                "Cheiro de detergente. Um desejo maçante e latejante na arcada de suas costas.
                Seus olhos suaves e necessitados, querendo orientação, uma mão reconfortante."

                "Aqui e ali, entre grunhidos, memórias indesejáveis se intrometendo —
                de aventuras semelhantes, mas pior ainda, rostos familiares de pessoas que já partiram."

                "Seu bico com um pequeno corte e sua cauda dobrada na ponta.
                O que ele pensaria ao ver Lucas assim, o rosto contra o chão de ladrilhos?"

                "Ele imaginou algo assim quando ouviu as novidades pela primeira vez?"

                "Talvez sim. Mesmo que Luke não fosse assim quando tudo aconteceu,
                ele poderia ter adivinhado em uma doentia reviravolta do destino."

                "Luke tenta afastar esses pensamentos. Esta não é a hora."
                "Me deixe aproveitar."

            jump lukeChapter1Scene5
        "Arrepender-se do testemunho." if not persistent.sfwMode:
            scene bg truckbathroom
            with Dissolve(1)


    "A partir da porta, um único raio de sol corta a escuridão do banheiro.
    As lâmpadas fluorescentes estão mortas e as poucas janelas ao redor estão cobertas com uma
    poeira espessa e amarelada."

    "É um lugar úmido e mofado, com um forte toque de desinfetante.
    O chão está pegajoso — possivelmente devido aos produtos de limpeza."

    "Há pias à direita e três cabines de banheiro à esquerda, duas das
    quais estão com as portas abertas. Ao lado da porta, à esquerda em frente às
    cabines, ficam os mictórios de porcelana."
    show Luke:
        xalign 1.1
        yalign 1.0
    with Dissolve(1)
    show trucker clothes:
        xalign -0.1
        yalign 1.0
    with Dissolve(1)
    "E lá está o caminhoneiro, pau já para fora. Ele segura o pênis como se estivesse
    urinando, mas não há som de corrente atingindo o metal."

    "O homem está longe de ser um atleta. Ele carrega uma bela barriga, mas possui
    o vasto semblante de alguém que esteve levantando cargas pesadas por anos.
    Seus olhos estão obscurecidos pelo boné de beisebol, mas Luke vê uma barba por fazer
    em seu rosto, acumulada de alguns dias."

    "Sua regata branca está manchada de suor, terra e óleo preto.
    Uma camada de pelos crespos cor de avelã brota de seus ombros e braços
    expostos. A alguns metros de distância, Luke já pode sentir seu cheiro."

    "O forte almíscar de um homem que mal tem tempo ou oportunidade para tomar banho."

    if persistent.sfwMode:
        "Ele se vira de lado para Luke.
        Um sorriso pretensioso abre em seu rosto barbudo."

    else:
        "Ele se vira de lado para Luke e balança o pau em direção ao grifo, que o observa.
        Um sorriso pretensioso abre em seu rosto barbudo."

    show Luke:
        xalign 1.1 yalign 1.0
        ease 1.0 xalign 0.9
    show trucker clothes:
        xalign -0.1 yalign 1.0
        ease 1.0 xalign 0.1
    if persistent.sfwMode:
        "Luke caminha até ficar ao lado dele. O caminhoneiro dá uma olhada rápida para baixo e
        grunhe em aprovação."

    else:
        "Luke caminha até ele e também tira seu pau para fora.
        O caminhoneiro dá uma rápida olhada no equipamento do grifo e
        grunhe em aprovação — mas então ele olha de volta para
        seu próprio membro enrijecido enquanto o acaricia."

    $Luke.change ("emotion", "hornier")
    if persistent.sfwMode:
        "Luke encara o homem. Por completo."

        $Luke.change ("emotion", "horny")

        "Os dois se encaram em um desafio silencioso sobre quem cederá
        primeiro. Luke mantém sua posição por apenas um segundo."

        hide trucker clothes
        hide Luke
        with Dissolve(1)

        "O grifo começa seu ato. Parece certo, como se este fosse seu
        lugar de direito no mundo."
        pause 2
        jump lukesfw1
    else:
        "Luke saliva com a visão. É um belo pau, ele pensa.
        Circuncidado, grosso, uma gorda cabeça de cogumelo com uma gota de pré-semen já
        já pingando, mesmo que ele ainda não esteja completamente duro."
        $Luke.change ("emotion", "horny")
        "A única gota de pré-semen ameaça pingar no mictório."

        "Os dois se olham em um desafio silencioso sobre quem cederá
        primeiro. Luke mantém sua posição por apenas um segundo."

        show Luke:
            xalign 0.9 yalign 1.0
            ease 1.0 xalign 0.7

        "Ele estende a mão e pega a gota de pré-semen exatamente quando está prestes a
        partir. Ele levanta o dedo até a ponta do pênis do caminhoneiro, esfregando sua cabeça.
        E então leva a ponta do dedo à boca."

        "Ele mantém contato visual com o caminhoneiro enquanto lambe o dedo,
        provocando-o para ir em frente."
        $Luke.change ("arm", "pointing")
        $Luke.change ("emotion", "hornier")
        luke "Você tem um gosto bom. Quando tempo faz pra você?"
        $Luke.change ("arm", "hip")

    show trucker clothes:
        xalign 0.1 yalign 1.0
        ease 1.0 xalign 0.2
    "O sorriso dentuço do caminhoneiro é uma
    única faixa de branco na escuridão do banheiro."

    "Caminhoneiro" "Não bato uma faz tempo.
    É melhor você se preparar pra uma baita gozada."
    $Luke.change ("arm", "pointing")
    "Outra gota de pré-semen pinga do pau do caminhoneiro.
    Mais uma vez, Luke a pega com um dedo — e olha diretamente
    nos olhos do homem quando prova."

    "Há um perigo na eloquência, Luke sabe, e há um conforto
    em ter sua voz silenciada. A visão diante de si, o gosto,
    o leva ao limite e ao momento — ele está de volta ao seu devaneio."

    show Luke:
        xalign 0.7 yalign 1.0
        ease 1.0 yalign 3.0
    "O caminhoneiro põe a mão no ombro de Luke e o empurra para baixo
    até ele ficar de joelhos — bem ali, no meio do banheiro."

    "Caminhoneiro" "Manda ver."
    hide trucker clothes
    with Dissolve(1)
    hide Luke
    with Dissolve(1)
    "É pura memória mecânica agora. Luke enterra seu rosto na virilha do homem.
    O cheiro é inebriante, pura masculinidade.
    A mente do grifo fica em branco enquanto ele aprecia o almíscar e esfrega
    o pau do homem em seu rosto."

    "Mas o caminhoneiro não tem paciência para isso.
    Ele agarra o bico de Luke e o abre."
    $Luke.change ("arm", "hip")
    $Luke.change ("emotion", "hornier")
    show Luke:
        xalign 0.65
        yalign 4.0
    with Dissolve(1)
    show trucker naked:
        xalign 0.35
        yalign 1.0
    with Dissolve(1)

    "Caminhoneiro" "É melhor você não arranhar meu pau, ouviu?"

    luke "Não se preocupe com isso.
    Vou te dar o melhor boquete de toda a sua vida."

    "Caminhoneiro" "Você é um putinho convencido, hein?"

    "O caminhoneiro para por um segundo, avaliando a atitude do grifo.
    Então ele ri e alinha seu pau com a boca dele. Luke tenta lamber,
    mas o homem mantém a cabeça dele para trás."

    $Luke.change ("emotion", "surprise")
    "Caminhoneiro" "Eu quero você olhando pra mim, tá me ouvindo?
    Olhe bem nos meus olhos."

    "Luke obedece em silêncio e espera,
    mas o caminhoneiro ainda o segura."

    "Caminhoneiro" "Isso foi uma pergunta. Cadê sua resposta, puto?"

    $Luke.change ("emotion", "horny")

    "Luke mal consegue conter sua frivolidade.
    Ele já foi fodido por muitos homens assim antes.
    Rudes, preocupando-se mais com seu próprio prazer do que qualquer outra coisa, e
    com uma apreciação por deboche."

    $Luke.change ("emotion", "neutral")

    luke "É melhor que você seja durão na foda.
    Eu posso aguentar o que você quiser e fico ansioso por isso."

    luke "Então, sim, senhor. Me foda como se não houvesse amanhã
    e eu vou te olhar direto nos olhos."


    "Caminhoneiro" "Putinho convencido."
    show trucker naked:
        xalign 0.35 yalign 1.0
        ease 1.0 xalign 0.4
    "Ele mergulha e vai até a base. O bico de Luke está esfregando contra seus
    pelos pubianos em menos de um segundo. A barriga do homem repousa na testa do
    grifo, tornando mais difícil para ele manter os olhos no caminhoneiro."

    "É uma foda impiedosa desde o início. Ele usa a boca de Luke sem
    cuidado ou preocupação, alternando impulsos profundos que quase chicoteiam a cabeça do grifo
    e indo até a base pelo tempo que ele conseguir aguentar."

    $Luke.change ("bandanna", "False")

    "Ele não consegue esconder seu prazer em assistir ao esforço do grifo."

    $Luke.change ("emotion", "surprise")

    "A tontura vai e vem enquanto o caminhoneiro usa o grifo da maneira que bem
    entende. Lágrimas escorrem pelo rosto de Luke, mas seu próprio pau está duro
    como uma rocha e seu entusiasmo cresce quanto mais bruto o homem é com ele."

    $Luke.change ("arm", "pointing")

    "Ele agarra a bunda do homem com as duas mãos para puxá-lo para dentro,
    até que novamente seu bico esteja amassando contra a virilha peluda diante dele e
    sua garganta contraindo com o pau dentro dela."

    "Luke certifica-se de que suas roupas estão coletando toda a baba e pré-semen
    pingando de seu bico. Ele olha para o caminhoneiro e escuta os sons molhados
    de sexo que preenchem o banheiro."

    "Luke se pergunta o que o homem está vendo e sentindo. Mesmo durante o sexo,
    o disfarce humano do grifo é mantido."

    "Caminhoneiro" "Caramba, você é um putão mesmo, não é?"

    $Luke.change ("emotion", "neutral")

    "Luke murmura em concordância e o puxa para dentro novamente.
    Desta vez, ele segura as bolas do homem e gentilmente as puxa para baixo."

    "Isso empurra o caminhoneiro além do limite e ele assume um
    desesperado ritmo final."

    $Luke.change ("arm", "hip")

    "O grifo se prepara para a primeira explosão. Ele está ansioso por sua recompensa —
    o gosto amargo de porra de dar água na boca."

    $Luke.change ("emotion", "hornier")

    "Este é seu segundo momento favorito, quando sua boca inunda com
    jorro após jorro e ele pode simplesmente saborear.
    Mantê-lo na boca e então olhar para cima, mostrando a língua para demonstrar
    quão grande foi a gozada."

    show trucker naked:
        xalign 0.4 yalign 1.0
        ease 0.5 xalign 0.3

    $Luke.change ("emotion", "surprise")

    "Mas o caminhoneiro puxa para fora e se masturba por cima da cabeça do grifo,
    explodindo o esperma por todo o rosto de Luke.
    Ele tenta pegar em sua boca aberta com muito pouco sucesso —
    o homem ainda segura sua cabeça em um aperto vicioso."

    show trucker naked:
        xalign 0.3 yalign 1.0
        ease 0.5 xalign 0.4

    "Luke não tem tempo para se sentir desapontado enquanto o caminhoneiro espeta sua
    boca novamente com o pau amolecido. O homem esfrega seu sêmen na cabeça do grifo,
    certificando-se de que penetre em suas penas."
    $Luke.change ("emotion", "annoyed")
    "Caminhoneiro" "Limpe."

    "Luke alicia as últimas gotas de esperma passando a língua na parte inferior
    do pau, da base à ponta.
    Ele as pega e faz questão de mostrar ao caminhoneiro antes de engolir."

label lukesfw1:
    "Está ficando escuro lá fora, mais escuro ainda no banheiro.
    O sorriso desencarnado do homem envia um arrepio de medo na espinha de Luke, mas
    o persistente gosto de esperma o traz de volta."
    if persistent.sfwMode:
        show trucker clothes:
            xalign 0.4 yalign 1.0
    $Luke.change ("emotion", "wink")
    show Luke:
        xalign 0.65 yalign 4.0
        ease 1.0 yalign 3.0
    if persistent.sfwMode:
        luke "E então? Como foi?"
        "Caminhoneiro" "Hm. Talvez eu precise de uma segunda rodada antes de poder dizer com certeza."

    else:
        luke "E então? Foi o melhor boquete da sua vida?"
        "Caminhoneiro" "Quase. Talvez eu precise de uma segunda rodada antes de poder dizer com certeza."

    $Luke.change ("emotion", "happy")

    "Ele segura o queixo do grifo com uma mão.
    Luke inclina a cabeça nela e fecha os olhos.
    Seu rosto está na virilha do homem novamente, mas agora ele está
    transfixado por este gesto curto e afetuoso."

    "Mas acaba muito cedo. O caminhoneiro empurra sua cabeça de volta à
    posição para encará-lo."

    $Luke.change ("emotion", "neutral")

    "Caminho" "Eu tenho alguns amigos que iriam gostar de usar sua boca.
    Que tal você ficar aqui enquanto eu saio e busco eles?"
    if persistent.sfwMode:
        show trucker clothes:
            xalign 0.4 yalign 1.0
            ease 0.5 xalign 0.3
            pause 1
            xzoom -1
        "Caminhoneiro" "Deixe a porta destrancada.
        Eu vou voltar pra usar você de novo e eu não quero esperar pra fazer isso."
        show trucker clothes:
            xalign 0.3 yalign 1.0
            ease 2.0 xalign -0.1
    else:
        show trucker naked:
            xalign 0.4 yalign 1.0
            ease 0.5 xalign 0.3
            pause 1
            xzoom -1
        "Caminhoneiro" "Deixe a porta destrancada.
        Eu vou voltar pra usar você de novo e eu não quero esperar pra fazer isso."
        show trucker naked:
            xalign 0.3 yalign 1.0
            ease 2.0 xalign -0.1
    show Luke:
            xalign 0.65 yalign 3.0
            ease 1.0 xalign 0.8

    "O caminhoneiro move a mão, mas Luke tenta manter o queixo nela.
    Ele quase perde o equilíbrio, tornando mais fácil para o homem
    agarrar a parte de trás de sua camisa e empurrá-lo para dentro da cabine do meio."

    if persistent.sfwMode:
        hide trucker clothes

    else:
        hide trucker naked

    with Dissolve(1)

    $Luke.change ("emotion", "annoyed")
    show Luke:
            xalign 0.8 yalign 3.0
            ease 1.0 yalign 2.0

    "O homem vai embora e, de repente, tudo fica silencioso e vazio — onde está o
    calor daquela mão no bico do grifo?"

    "Luke permanece ajoelhado no chão, sentindo cada segundo passar.
    Ele verifica sua camisa manchada e agora não se sente mais tão seguro sobre isso."

    hide Luke
    with Dissolve (1)

    if not persistent.sfwMode:
        $Luke.change ("clothes", "none")
        $Luke.change ("dogtag", "False")
    show Luke:
        xalign 0.5
        yalign 2.0
    with Dissolve(1)
    "Suas penas estão úmidas de esperma. Ele pensa em ir embora, mas então sente sua
    própria ereção insistente. Assim que se despe e a expõe ao ar livre,
    ele sabe que vai ficar."

    "Passos e gargalhadas turbulentas anunciam a chegada dos amigos do caminhoneiro."

    if persistent.sfwMode:
        $Luke.change ("emotion", "hornier")
        pause 2
        hide Luke
        with Dissolve(2)
        pause 3

        "Os sons do subsequente deboche podem ser ouvidos de fora do banheiro,
        no meio do estacionamento."

        "Um por um, os homens vão embora, enquanto risos e gemidos persistem."
        "À noite, apenas Luke e o primeiro caminhoneiro permanecem."

        $Luke.change ("emotion", "horny")
        jump lukesfw2

    $Luke.change ("emotion", "hornier")
    $Luke.change ("penis", "erect")

    "Luke está acostumado com isso. Não é a primeira vez que ele comanda um glory hole.
    Enquanto acaricia seu pau, ele saliva com o que está por vir e
    volta ao seu devaneio."
    show Luke:
            xalign 0.5 yalign 2.0
            ease 1.0 yalign 3.0
    "Ele olha pelos buracos para suas próximas refeições e é recompensado com outro
    pau grosso, embora mais curto, e um de tamanho bastante médio."

    "Ele não discrimina. Pau é pau."

    "Ele entra em seu ritmo, alternando punhetas e boquetes com os
    dois. Mais passos do lado de fora, seguidos pela voz do primeiro caminhoneiro,
    anunciam o começo de uma fila."

    "A porta abre com força e Luke é puxado para fora da cabine."
    hide Luke
    with Dissolve(1)
    scene cglukebathroom
    with Dissolve(1)
    "Torna-se mecânico, mas não menos agradável. Não há tempo a perder e
    Luke faz seu melhor para fazê-los gozarem o mais rápido possível —
    desta vez, ele se certifica de beber sua recompensa."

    "O tempo passa. Quantos paus ele chupou hoje? Difícil dizer;
    quando ele se vira, é fácil para o caminhoneiro anterior escapar
    despercebido. Conforme fica mais escuro, o grifo para de registrar
    como cada pau se parece."

    "A mistura de saliva, pré-semen e esperma cobre sua camisa. O banheiro cheira
    a sexo, mas o grifo nunca notaria, ele se foi há tanto tempo.
    É pura memória mecânica."

    "O primeiro caminhoneiro aparece.
    Outros homens estão ao seu lado, observando, rindo, mas Luke não se importa em olhar
    para o rosto deles. Ele não para de chupar o pau em sua boca."

    "Caminhoneiro" "Eu soube que você era algo especial no momento em que eu coloquei os olhos em
    você, mas eu nunca pensei que você fosse um caçador de caralhos."

    "Caminhoneiro" "Se vire, é hora de destruir esse seu cu."

    "O grifo demora apenas o tempo de terminar sua refeição atual.
    Em um piscar de olhos, ele está se curvando — porra, seus joelhos queimam de dor —
    e empinando a bunda."

    "Luke se deleita com a devassidão. Ele olha para trás e sabe que é um putão sexy.
    Todos aqueles homens querem um pedaço dele."

    "Ele tenta falar, mas sua voz sai rouca e grave.
    São necessárias algumas tentativas antes que Luke possa ser entendido."

    luke "Isso, entra aí. Manda ver!"

    "Não há lubrificante e o grifo não se incomoda em pedir.
    Tudo o que ele consegue é uma generosa dose de cuspe."

    "Luke sabe como relaxar e receber uma trepada violenta. Ele acaricia seu
    pau e balança os quadris em antecipação.
    Sua cauda está levantada e seu cu está exposto."

    "O caminhoneiro é tão impiedoso quanto antes, colocando tudo de uma vez só.
    Dói como o inferno, tanto pela queimação da invasão quanto pela brusca dor
    de ter suas entranhas empurradas tão rapidamente."

    "Mas o grifo sabe que isso vai passar. Luke se vira para olhar para todos os homens
    e dá um tapa em sua própria bunda forte o suficiente para ser ouvido mesmo do lado de fora do banheiro."

    luke "Vamos, faça o seu pior. Bata em mim, puxe meu rabo, me foda como um homem."

    "O caminhoneiro dobra seu ritmo. O grifo está conseguindo exatamente
    o que queria e grita em resposta. Todos os homens juntam-se ao
    ato, encorajando sua vadia ansiosa e trabalhadora."

    "A dor desaparece em favor de um calor formigante que se espalha até as
    extremidades do grifo. Torna-se uma onda de prazer, batendo
    e recuando, misturada com o calor de toda a cena ao seu redor."

    "Sua boca exala um cheiro de esperma, o mesmo pode ser dito de seu rosto e peito.
    Seu próprio pau vaza; ele não gozou uma única vez em toda essa depravação."

    "Ora, esse é o lugar dele, tudo bem.
    Cheirando a sexo e ansioso para ser cercado por homens excitados."

    "É mecânico, impulso após impulso enquanto o homem atrás dele alterna entre
    bater na bunda do grifo e puxar seu rabo."

    "Novamente, o caminhoneiro puxa para fora, vira Luke de lado e goza na cara dele."

    luke "Seu filho da puta, você gosta de me cobrir de porra, não é?"

    "Caminhoneiro" "Isso mesmo. Eu quero que todos saibam como você é sedento por porra.
    Vamos cobrir você inteiro com isso."

    "Todos eles riem — incluindo Luke. Desta vez, o caminhoneiro não precisa
    espalhar pelo rosto do grifo; Luke faz isso sozinho enquanto se masturba."

    luke "Próximo! Vamos, dessa vez é melhor gozarem dentro."

    "A libertinagem continua até tarde da noite, cada um dos amigos do caminhoneiro tendo
    sua vez no grifo."

    "Homens partem e chegam. A criatividade floresce enquanto eles o colocam na posição
    frango assado no chão do banheiro ou o deixam assumir o comando da foda como passivo dominante."

    "Em pouco tempo, há um fino rio de esperma escorrendo pelas pernas de Luke.
    Quando um termina e o outro homem toma seu lugar, o grifo passa as mãos sobre
    suas coxas para sentir o fio de sêmen."

    scene bg truckbathroom
    with Dissolve(1)
    "Horas se passam. Eventualmente, todos eles voltam para seus carros e caminhões."
    $Luke.change("dogtag", "True")
    $Luke.change("emotion", "horny")
    show Luke:
        xalign 0.7
        yalign 1.0
    with Dissolve(1)
    show trucker hatless:
        xalign 0.3
        yalign 1.0
    with Dissolve(1)

    "No final, é apenas Luke e o primeiro caminhoneiro,
    fodendo ao estilo cachorrinho no chão do banheiro."

    "Quando ele chegou hoje mais cedo, o banheiro cheirava a desinfetante.
    Agora, Luke dificilmente consegue detectar qualquer cheiro além do de sexo."

    "Depois de horas, Luke finalmente se permite derramar sua primeira gozada no chão,
    pouco antes da última ejaculação do dia entrar em suas entranhas."

label lukesfw2:
    if persistent.sfwMode:
        show trucker clothes:
            xalign 0.3 yalign 1.0
        show Luke:
            xalign 0.7 yalign 3.0
        with Dissolve(1)
    else:
        show Luke:
                xalign 0.7 yalign 1.0
                ease 1.0 yalign 3.0

    "O grifo colapsa no chão. Ele só tem a energia para virar
    de costas e olhar para o homem — agora nu, exceto pelas botas."

    $Luke.change("arm", "pointing")
    if persistent.sfwMode:
        show trucker clothes:
                xalign 0.3 yalign 1.0
                ease 1.0 yalign 2.0
    else:
        show trucker hatless:
                xalign 0.3 yalign 1.0
                ease 1.0 yalign 2.0
    "Luke levanta um braço, convidando o homem a se deitar no chão com ele,
    mas o gesto é ignorado. Em vez disso, o caminhoneiro se agacha e verifica as etiquetas militares do grifo."

    "Caminhoneiro" "Seu nome é Lucas, hein? Olha só, se não é um bom patriota,
    servindo aos homens tão bem."
    $Luke.change("emotion", "wink")
    $Luke.change("arm", "salute")
    luke "O que eu posso dizer? Eu gosto de servir ao meu povo."

    "A voz do grifo está rouca. Ainda assim, ele insiste em convidar o homem
    para descansar com ele no chão, mas seu apelo permanece ignorado."
    $Luke.change("arm", "hip")
    if persistent.sfwMode:
        show trucker clothes:
                xalign 0.3 yalign 2.0
                ease 1.0 xalign 0.2 yalign 1.0
        pause 2
        "Caminhoneiro" "Prazer em te conhecer, soldado."
        stop music fadeout 2.0
    else:
        show trucker hatless:
                xalign 0.3 yalign 2.0
                ease 1.0 xalign 0.2 yalign 1.0
        pause 0.5
        hide trucker hatless
        with Dissolve(0.5)
        show trucker naked:
            xalign 0.2 yalign 1.0
        with Dissolve(0.5)
        "Caminhoneiro" "Prazer em te conhecer, soldado."
        stop music fadeout 2.0
        hide trucker naked
        with Dissolve(0.5)
        pause 2
        show trucker clothes:
            xalign 0.2 yalign 1.0
        with Dissolve(0.5)
    "Caminhoneiro" "Se a gente se ver de novo alguma vez, vamos repetir."

    luke "Mas você vai se lembrar de mim?"

    "Caminhoneiro" "É fácil lembrar de um putão que nem você. Pode contar com isso."

    "Ele começa a se vestir. Luke permanece no chão frio —
    e, de repente, seus sentidos voltam."

    hide trucker clothes
    with Dissolve(1)

    $Luke.change("emotion", "annoyed")
    "Houve muitas vezes em que Luke compareceu a concertos de rock.
    Depois disso, seus ouvidos zumbiam por horas, às vezes dias.
    Ele estaria profundamente ciente do silêncio."

    show Luke:
            xalign 0.7 yalign 3.0
            ease 2.0 xalign 0.5 yalign 1.0
    "O mesmo acontece esta noite. O silêncio não é nada além de opressivo."

    "O devaneio chegou ao fim."
    pause 2
    scene bg black
    #with Dissolve(2)

#############################################################################
    #LUKE SCENE 5: AFTER SEX
#############################################################################
    pause 2

    "O grifo e suas roupas cheiram mal. Não há como esconder as manchas
    brancas em sua camisa — vários homens a usaram como pano — ou a trilha molhada
    que desce por suas pernas. Seu rosto está encrostado e descascando porra seca."

    "Às vezes, mostrar a evidência de suas escapadas o fazia se sentir orgulhoso,
    desejável, poderoso. Sair de um apartamento com uma mancha de esperma
    secando em seu peito o fazia se sentir bem."

    "Mas hoje, ele está quebrado e fora de si. As pernas que o conduzem
    em direção à cafeteria não são as dele. Outra pessoa está no volante."

    "Leva um segundo para ele enxergar o que seus olhos estão olhando e
    outro para seu cérebro enviar uma resposta de volta. Sua garganta está rouca por causa
    de toda a ação."

    "Ele foi longe demais novamente. Foi bom no momento, claro, mas ele fica
    estranho quando todos eles o deixam para trás assim.
    Sua mente começa a falar muito alto."

    "Luke precisa de alguém para conversar e abraçar depois que terminam.
    Desta forma, seus próprios pensamentos não correm a cem quilômetros por hora,
    como estão fazendo agora."

    "É sua coisa favorita, aquele resplendor. Como ondas indo e vindo,
    molhando os pés. Luke gosta de deitar a cabeça no peito de alguém —
    o estrondo da voz o faz adormecer como nada neste mundo."

    "E, como muitas vezes antes, isto lhe foi negado."

label lukeChapter1Scene5:
    stop music fadeout 2.0
    scene bg truckstop
    with Dissolve(1)
    $Luke.change("clothes","tankpants")
    $Luke.change("bandanna", "True")
    $Luke.change("emotion", "annoyed")
    show Luke
    with Dissolve(1)
    pause 1

    "Luke chega na cafeteria e pede uma xícara de café.
    A expressão de nojo nos olhos do caixa deixa claro que ele sabe exatamente
    o que Luke estava fazendo e que ele não é bem vindo para pingar esperma no chão deles."

    "O caixa desliza um copo de isopor, mesmo que Luke não tenha pedido para a viagem.
    Ele o pega e sai da cafeteria para sentar ao lado da lixeira e observar as estrelas."

    hide Luke
    with Dissolve(0.5)
    play music "music/crickets.mp3" fadeout 1.0 fadein 1.0
    pause 1
    show blackback:
        alpha 0.4
    show Luke behind blackback
    with Dissolve(1)

    "Suas mãos trêmulas derramam metade do conteúdo do copo.
    O calor pungente nem é percebido."

    "O grifo diz a si mesmo que tudo ficará bem assim que ele traçar as
    constelações. Ele se sentirá como uma criança e será como estar de volta ao
    Cabo Canaveral outra vez."

    $Luke.change("emotion", "surprise")

    "Ele está prestes a virar a esquina quando o fedor de cigarro o atinge."

    $Luke.change("emotion", "annoyed")

    "A ideia de ser visto agora não lhe traz nenhuma faísca de excitação.
    Se estivesse mais sob controle de si mesmo, teria girado os calcanhares
    e se afastado."

    show Luke:
        xalign 0.5 yalign 1.0
        linear 2.0 xalign 0.8
    pause 2.0
    show tricky smug behind blackback:
        xalign 0.2 yalign 1.0
    with Dissolve(1)
    "Mas sua mente está lenta, suas pernas se movem por conta própria e ele esbarra em
    ninguém menos que Jean, aproveitando um cigarro."

    "Está escuro. \"Talvez ele não veja o quanto eu sou uma vergonha,\"
    pensa o grifo. \"E a fumaça pode esconder o cheiro.
    Talvez ele não me reconheça no escuro.\""

    "Mas leva apenas um momento para Jean descobrir quem é."
    show tricky neutral:
        xalign 0.2 yalign 1.0
    "Jean" "Luke, é você? Pensei que você já tivesse ido embora.
    O que você está fazendo aqui?"

    "Luke precisa juntar as peças da reação de Jean e então pensar em uma resposta.
    Palavra por palavra."
    $Luke.change("emotion", "annoyed")
    luke "Eu não tava me sentindo muito bem, então tirei uma soneca no meu carro.
    Acabei de acordar e fui tomar um café."
    show tricky smug:
        xalign 0.2 yalign 1.0
    "Jean" "É mesmo?"

    "A voz do grifo soa áspera e grave.
    Ele não consegue se impedir de tossir seus pulmões para fora."

    "Jean" "Engraçado. Eu percebi o seu carro ainda estacionado.
    Mas não vi você lá quando passei por perto."

    "Ele dá uma longa tragada no cigarro e deixa as palavras demorarem.
    Luke senta no chão e se encolhe enquanto segura seu café."

    "Ele não ousa olhar para Jean. Para aquela silhueta e a ponta
    acesa do cigarro brilhando."

    "Jean" "Parece que você está pegando um resfriado, também.
    Você parece, perdoe minha franqueza, péssimo."

    "Luke toma um gole de seu café,
    esperando que isso lhe dê tempo suficiente para se recompor."

    "Mas o silêncio perdura, o consumindo.
    Jean espera por uma resposta até que se torna demais para o grifo."

    luke "E o que você tá fazendo aqui? Não já devia ter ido embora a essa altura?"
    show tricky neutral:
        xalign 0.2 yalign 1.0
    "Jean" "Ah, minha carona teve alguns problemas. Ele vai demorar mais uma ou duas horas para chegar.
    Então eu estou aqui, esperando, vendo os caminhoneiros irem e virem."
    show tricky smug:
        xalign 0.2 yalign 1.0
    "Jean" "Muita comoção essa noite."

    "A mente do grifo bate e balança como as ondas.
    Ele se lembra o quão agradável foi conversar com Jean antes —
    ele só gostaria de ter aquilo de novo."

    "Como mais cedo no dia, Luke age antes de pensar.
    Enquanto as palavras saem de sua boca, ele já se arrepende delas."
    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "pointing")
    luke "Eu posso te dar uma carona de novo. Você é uma boa companhia,
    Eu gostei da conversa. Que tal isso?"
    $Luke.change("emotion", "annoyed")
    $Luke.change("arm", "hip")
    "O estômago de Luke afunda, no entanto, quando ele percebe que não haverá como esconder
    o quanto ele está fedendo. Jean saberá, se é que já não sabe, o que Luke é."

    "Deixar à mostra suas conquistas sexuais costumavam deixá-lo orgulhoso, mas não esta noite."
    show tricky neutral:
        xalign 0.2 yalign 1.0
    "Jean" "Muito gentil de sua parte, amigo, mas eu vou voltar por onde vim."

    "Jean" "Além disso... parece que você realmente precisa de um descanso."

    "Jean" "Você lembra do que eu te falei? Tem um hotel em frente.
    Está reabrindo, supostamente. Talvez você possa ficar lá um pouco, parece que você precisa."

    "Jean" "Tem alguém esperando por você em casa?"

    luke "Não. Eu moro sozinho."

    "Jean" "E algum motivo para voltar rápido? Um trabalho, família, obrigações?"

    "Luke volta a tomar seu café e Jean entende a dica."
    $Luke.change("emotion", "neutral")
    luke "Talvez eu devesse, é. Eu realmente poderia tirar proveito de um pouco de paz e sossego...
    Uma mudança de cenário."

    "Jean" "Também tem um chuveiro aqui. É para os empregados, mas eu sou
    amigo do dono. Tenho a chave comigo, certeza que ele não
    se importaria com você usando."
    $Luke.change("emotion", "wink")
    luke "É... eu preciso de um banho."

    "Jean entrega a chave para ele."

    "Jean" "Suponho que eu deveria te dar privacidade agora."

    "Jean pisa em seu cigarro."
    $Luke.change("emotion", "happy")
    luke "Na verdade... Se não se importa, você poderia...
    conversar comigo mais um pouco?"

    luke "Sabe sobre as constelações?
    Os nomes e as histórias? Tudo bem se a gente conversar sobre elas?
    Olha, aquela é Orion."

    "É difícil enxergar o rosto de Jean. Mas mesmo que seus olhos estejam cobertos de
    sombras, há um brilho."

    "Jean" "Claro, Luke. Eu sei como ler as estrelas, é útil.
    Vou te contar tudo sobre elas. Mas você me promete que vai fazer uma pausa?"

    $Luke.change("arm", "pointing")
    luke "O que você quiser, contanto que continue falando."

    scene bg black
    with Dissolve(1)

    "Muita coisa mudou desde que Luke era um menino. Chega de dormir na varanda
    em uma pilha com seus irmãos, de ouvir rádio depois que seu pai voltava do
    do trabalho, de ficar observando as estrelas com Pedro."

    "Ele é um homem adulto agora, coberto de sexo e cheio de ódio por si mesmo,
    lutando para não derramar café de seu copo de isopor enquanto se senta
    ao lado de uma lixeira."

    "O chuveiro vai lavar toda a gosma, mas a voz de Jean limpa sua mente.
    Quando Luke fecha os olhos, ele pode fingir que é Pedro, seu irmão.
    O grifo se esforça para não adormecer."

    "Quando a carona de Jean chega, os dois se despedem. É lacônico, até mesmo doloroso."

    "Luke toma seu banho e tira um cochilo no carro, olhando para as estrelas através
    do para-brisa. Ele está muito cansado para dirigir agora."

    "Esta noite, ele se apega à voz de seu irmão como se ainda fosse um menino.
    Quando a manhã chegar, ele será um homem outra vez, a caminho daquele hotel
    em que prometeu se hospedar."

#############################################################################
    #LUKE SCENE 6: ARRIVING AT THE HOTEL
#############################################################################
label LukeISkip:
    hide screen SkipButton
    play music "music/Solidarity.ogg" fadeout 1.0 fadein 1.0
    scene bg desert
    with Dissolve (2)
    $Luke.change("glasses", "True")
    $Luke.change("emotion", "neutral")
    $Luke.change("arms", "hip")
    $Luke.change("clothes", "tankpants")
    $Luke.change("bandanna", "True")
    $Luke.change("dogtag", "True")
    show Luke
    with Dissolve(1)
    "Luke ajusta o espelho retrovisor. Seus olhos brilham por um momento —
    ele não gosta de se ver assim, vindo do nada.
    Espelhos, ele sabe, são perigosos."

    "O motor ruge uma, duas, três vezes para garantir.
    As garras de Luke cravam no couro do volante.
    A luz do sol da manhã passando pelo para-brisa aquece seu peito
    e arranha seu bico."

    "Ele vai embora. Doce memória mecânica. Não leva um minuto sequer
    para o grifo começar a cantarolar uma melodia, um bom hit de Jazz."

    "Lavar toda aquela gosma, uma boa noite de sono no banco de trás
    e a conversa com Jean o fizeram voltar a funcionar."

    "Sim. Ele poderia aproveitar algum tempo em um cenário diferente. Jean estava certo.
    Não é como se ele tivesse qualquer coisa melhor para fazer, ou um trabalho."

    "O cenário muda rapidamente, tão facilmente quanto Luke pula de uma música para
    a outra. Ele acelera até o que o carro esteja tremendo e suas partes individuais
    sacudindo, ameaçando se desfazerem."

    "Mais. Mais deste doce perigo."

    "E ele teria ido mais longe, não fosse pela forma cúbica cerca de um minuto
    à frente — como ele não a percebeu mais cedo neste plano deserto?"

    scene bg hotelexterior
    with Dissolve (2)

    play sound "sfx/carstop.ogg"

    "Ele tira o pé do pedal do acelerador e permite que a inércia o carregue para
    frente. Ele ainda está indo tão rápido que, ao virar à direita para o estacionamento,
    o carro dá uma guinada e o grifo é empurrado contra a porta.
    Ele gargalha com a testa pressionada contra a janela."

    "O carro para precisamente em cima da linha que separa duas filas de vagas
    de estacionamento. Luke quebrou seu recorde usando não um, não dois, não
    três, mas seis espaços simultaneamente."

    "O som de seu carro ainda toca jazz quando ele sai e bate a porta
    no ritmo da música. A melodia não persiste, mas o grifo
    cruza a vasta extensão do estacionamento ainda cantarolando a música, sincronizando seus
    passos com a batida."

    "Ele sobe os degraus, batendo as garras no corrimão.
    As portas se abrem quando ele coloca seu peso sobre elas, em seguida, ele fecha
    o acordo com um empurrão final que as joga contra as paredes atrás."

    scene bg oldlobby
    with Dissolve (2)
    show Luke:
        xalign 2.0 yalign 1.0
        ease 2.0 xalign 0.9
    with Dissolve(1)
    "A chegada de Luke é como um martelo de juiz silenciando o mundo ao redor dele —
    e no vazio subsequente, seu passo ainda segue a batida do Jazz."

    "Desde que partiu no início da manhã, ele adquiriu esta elasticidade contagiante em seus passos.
    A qualquer momento, ele poderia cair na gargalhada ou dançar."

    "Mas agora, conforme seus olhos se adaptam à nova iluminação interna e ele enxerga o homem
    por trás da mesa da recepção, a atitude de Luke muda."

    $Asterion.change("emotion", "neutral")
    show Asterion:
        yalign 1.0 xalign -1.0
        ease 2.0 xalign 0.1 yalign 1.0

    $Luke.change("glasses", "False")
    "Luke tira seus óculos escuros."

    $Luke.change("arm", "pointing")
    $Luke.change("emotion", "cocky")
    luke "Ei, você!"
    $Asterion.change("leftarm", "raised")
    asterion "Sim, senhor?"

    luke "Mas que porra aconteceu com a sua cara? Um cachorro mastigou ela?"

    $Asterion.change("emotion", "surprise")

    "???" "P-perdão?"

    $Luke.change("emotion", "surprise")
    $Luke.change("arm", "salute")
    luke "Você me ouviu, o que aconteceu com a sua cara? E que tipo de coisa chique
    você fez pra conseguir colocar um LED no seu crânio desse jeito?"

    $Asterion.change("leftarm", "loose")
    $Asterion.change("emotion", "tired")

    "O minotauro olha para baixo, gaguejando uma resposta inaudível.
    Ele morde o lábio com força e um fio de suor frio escorre por suas costas."

    $Luke.change("arm", "hip")
    luke "Jesus, se você quer parecer igual a um personagem de desenho animado não
    precisa arrancar metade da sua cara."

    "Os passos largos de Luke cobrem a distância entre eles antes que o minotauro tenha
    a chance de pensar em uma resposta. O grifo coloca as duas mãos na mesa e
    se inclina para frente."

    "Ele mantém o olhar fixo na cavidade ocular vazia do minotauro,
    examinando a chama cintilante de dentro."

    $Luke.change("emotion", "cocky")
    luke "Que coisinha estranha é você. O que você {i}é{/i}, sequer?"

    $Asterion.change("emotion", "tired")
    "O minotauro desvia o olhar e cobre o rosto sem pensar duas vezes.
    Suas costas inteiras estão cobertas de suor frio agora."

    asterion "M-me desculpe. Eu sei que sou —"

    "E em um piscar de olhos, a risada contida de Luke explode como uma represa."

    $Luke.change("emotion", "wink")

    luke "Haha, eu tô só tirando sarro de você, amigo! Você devia ter visto a sua cara!"

    $Asterion.change("emotion", "neutral")
    $Luke.change("arm", "pointing")

    luke "Você deve ter se metido numa briga daquelas.
    Mas eu já vi e passei por coisa pior, sei como é."

    $Luke.change("arm", "hip")

    luke "Não tem como você saber só olhando, já que eu não tenho nenhuma cicatriz pra mostrar, mas
    é. Já passei por maus bocados."

    luke "Até já fui explodido uma ou duas vezes.
    Sabe, com aquelas granadas de graveto antigas. Doem pra caralho!
    E também teve aquela vez que..."

    $Asterion.change("emotion", "neutral")

    luke "Aw, olha pra mim, quase comecei uma das minhas tagarelices.
    Eu poderia ficar o dia todo falando sobre isso com um bife de Angus de primeira
    que nem você."

    if Asterion.clothes == "nude":

        $Luke.change("emotion", "horny")
        luke "De qualquer forma, espero que você perdoe as minhas maneiras. Não entendi direito
        que tipo de estabelecimento emperiquitado era esse, sabe."

        luke "Pensei que era só mais um hotel comum! Mas que naca de carne
        eu achei aqui... esse lugar deve ser melhor que Lauderdale!"

        $Luke.change("arm", "pointing")

        luke "Deixa eu consertar as coisas com você — que tal eu alugar um quarto e levar
        você lá pra gente se divertir um pouco?"

        $Luke.change("emotion", "hornier")

        luke "Sempre quis tentar com um boi, mas eu nunca pensei que a sua laia
        sequer existisse! Aposto que você tem muito leite pra dar, hein?"

        luke "Eu consigo aguentar o que você quiser, amigo. Na verdade,
        eu poderia provavelmente aguentar uma mangueira de incêndio e nem piscar!"

        $Luke.change("arm", "hip")
        $Luke.change("emotion", "cocky")
        if chapter6LieAboutUndies <2:
            asterion "P-perdão, eu não entendo o que está acontecendo."

            luke "Qual é, um baita homem que nem você pelado assim desse jeito?
            Cê tá querendo, não tá?"

            $Asterion.change("emotion", "tired")
            asterion "Senhor, receio que você tenha interpretado mal minhas intenções.
            Este é um estabelecimento de respeito, o que o leva a dizer tais coisas?
            Alguém manchou nossa fachada?"

            luke "Qual é, você é maluco? Você tá quase nu, só pedindo pra ser apalpado
            e virado do avesso. Eu posso ser meio cérebro de passarinho, mas eu não sou {i}tão{/i} idiota assim!"

            if chapter6LieAboutUndies ==0:
                asterion "M-minha perizoma não deve ser apropriada para o período."
            else:
                $Asterion.change("emotion", "sad")
                asterion "M-me foi dito que esta é uma roupa apropriada...
                Que estava de volta à moda..."

                luke "Apropriada? Com certeza é se você for um gogoboy de luxo trabalhando
                pra um sugar daddy na cobertura dele."

                asterion "...O que é um gogoboy?"

                "Luke esfrega as têmporas."

                luke "Angus, meu garoto, você com certeza não é brilhante."

                $global_affection -=0.5
                $chapter6LieAboutUndies =2
        else:
            if chapter6LieAboutUndies ==2:
                asterion "E-eu peço desculpas pelo meu traje. Realmente não foi minha escolha."
            else:
                $Asterion.change("emotion", "sad")
                "Astério parece terrivelmente desapontado. Ele sabe que foi enganado—
                e mais de uma vez."
                $global_affection -=0.5
            $Luke.change("emotion", "annoyed")
            luke "The fuck kind of Eyes-Wide-Shut shit is going on here?"
            $Luke.change("emotion", "wink")
            luke "De qualquer maneira, pode contar comigo."

    pause 1
    $Luke.change("emotion", "neutral")

    luke "Quer saber, não importa. Eu quero reservar um quarto aqui. Esse lugar
    deve ser muito bom, né?"

    "O minotauro tropeça com a menção do hotel.
    Seu olhar mostra um calor desabrochando, apesar da ousadia anterior de Luke."

    $Asterion.change("emotion", "smiling")

    asterion "Sim. É um hotel maravilhoso e garanto que vai melhorar.
    Está bem vazio agora, mas com certeza isto mudará em apenas alguns dias."

    $Luke.change("arm", "pointing")

    luke "Eu vou cobrar isso de você! Então, onde eu assino? Qual é a taxa?"

    $Asterion.change("emotion", "contemplative")

    asterion "Ah, sim. Apenas assine aqui no livro de registros e preencha estes formulários.
    Esta é nossa pré-inauguração — não cobraremos de você, bom senhor."

    luke "Ah, então esse lugar é chique e barato? Qual é a pegadinha?"

    $Asterion.change("emotion", "smiling")

    asterion "Lamento dizer que não há pegadinha.
    Este lugar tem uma missão, veja bem, e... bem, nós nunca cobramos muito."

    $Luke.change("arm", "hip")

    luke "Uma missão? Isso é algum tipo de caridade?"

    asterion "...Suponho que seja uma forma de se descrever, sim, pelo menos foi por
    um bom tempo. Depende do dono."

    $UI_permissions['guests'] = True
    $check_in_guest('Luke')
    play sound "sfx/asterionchord.mp3"
    if renpy.variant("android"):
        "{color=[UIColorOrange]}Luke{/color} foi registrado no hotel.
        \nVocê pode abrir o menu e acessar a tela {color=[UIColorOrange]}hóspedes{/color}
        para ver seus hóspedes atuais."
    else:
        "{color=[UIColorOrange]}Luke{/color} foi registrado no hotel.
        \nVocê pode ver seus hóspedes atuais na tela {color=[UIColorOrange]}hóspedes{/color} no
        menu, ou clicando no ícone do livro de registros."

    "Luke entrega os formulários. O minotauro passa o olho neles."

    asterion "Senhor Lucas Walker. Nascido em Outubro de 1923."

    $Asterion.change("emotion", "neutral")

    asterion "Sua aparência é bastante enganosa. Eu nunca teria adivinhado sua
    idade... Você até teria idade suficiente para..."

    $Luke.change("emotion", "cocky")

    luke "Ah, sabe como é. Grifos não envelhecem igual aos humanos, e eu sou
    de uma ótima linhagem, sabe."

    luke "Sou três vírgula cento e vinte e cinco por cento grego!
    E meu pai era igual a mim nesse aspecto, mal envelheceu."

    $Asterion.change("emotion", "surprise")

    asterion "Ah, entendo. Me desculpe, admito que nunca conheci um grifo antes.
    Eu não \"sei como é\", receio."

    luke "Bem, eu poderia dizer o mesmo! Nunca tinha visto um minotauro, pensei que
    vocês fossem só uma lenda grega antiga."

    $Asterion.change("emotion", "neutral")
    asterion "Cretense."

    $Luke.change("emotion", "neutral")
    luke "Oi?"

    asterion "Uma história cretense, não grega."

    asterion "A Grécia não existia quando tudo aconteceu. Por volta de
    três mil anos antes de Cristo."

    $Asterion.change("emotion", "sad")

    asterion "...Ah, perdoe minha impertinência. Aqui está sua chave, senhor Walker.
    Seu quarto fica logo no final do corredor."

    $Asterion.change("emotion", "bowing")
    $Asterion.change("leftarm", "raised")
    asterion "Espero que você tenha uma estadia agradável aqui conosco."

    luke "Ah, tenho certeza que vou. E eu espero poder provar um pouco de bife de Angus um dia desses!"
    pause 1

    scene bg black
    with Dissolve(1)


    #Now that luke's intro is over we return to the normal flow.
    #If we picked luke first we jump to chapter 6, if not, chapter 7
    if first_guest == "Luke":
        jump chapter6_1
    else:
        jump chapter7_1

label KotaIntro:
############################################################################
    #KOTA SCENE 1: INTRODUCING KOTA
#############################################################################

    $chapter = "Kota I"
    call screen ChapterTransition("Kota I", "Jornada para o oeste")
    pause 0.5
    $save_name=output_save_name("Kota I")

    if 'Kota' in persistent.known_guests:
        show screen SkipButton("KotaISkip", "Skip guest scene")

    play music "music/TheSorrow.ogg" fadeout 1.0 fadein 1.0
    scene bg forestroad
    with Dissolve(3)
    $Kota.change ("emotion","happy")
    $Kota.change ("hair","loose")
    $Kota.change ("fundoshi","True")
    $Kota.change ("clothes","kimono")

    "A luz balança através das folhas verdejantes acima, moldando sombras
    tremeluzentes ao longo do caminho da floresta. Em ambos os lados, árvores balançam na
    leve brisa, sussurrando seus segredos umas às outras e ao viajante que passa sob seus
    ramos poderosos."

    show Kota:
        xalign 0.5
        ease 0.2 yalign 1.0
        pause 0.06
        ease 0.2 yalign 1.3
        pause 1.0
        repeat
    with Dissolve(2)

    "O dragão cantarola uma melodia simples e tranquila para si mesmo, sua profunda e estrondosa voz
    um contraponto com o farfalhar das folhas acima."

    $Kota.change ("emotion","neutral")

    "Ao longo de suas viagens durante esses anos longos e solitários, ele passou a apreciar
    os sons do mundo ao seu redor. Ele aprendeu como ficar em sintonia
    com eles, deixando-os fluirem em sua volta como o rio no qual
    nasceu."

    "Eles são seus companheiros, constantes e confiáveis. Preenchem o silêncio.
    Trazem paz para sua mente e coração durante sua busca longa e aparentemente interminável."

    $Kota.change ("rightarm","raised")

    "Enquanto caminha, seu murmúrio vai diminuindo conforme o vento cessa, ele enfia a mão
    na bolsa pendurada no ombro e tira uma garrafa de plástico cheia d'água."

    "Suas hábeis garras rapidamente desenroscam a tampa e ele inclina a garrafa para
    permitir que a substância revigorante despeje em sua boca expectante."

    $Kota.change ("emotion","laughing")

    "Ele nunca para de se surprender com quantas conveniências como esta surgiram
    ao longo dos anos."

    "Quando começou sua jornada na terra de seu nascimento, água limpa e fresca
    como esta era uma mercadoria quase sagrada. Algo a ser racionado e
    aproveitado até a última gota. Agora ela poderia ser comprada por uma quantia insignificante!"

    $Kota.change ("emotion","happy")
    $Kota.change ("rightarm","relaxed")

    "Seus pensamentos se voltam para o jovem da loja na cidadezinha que ele
    deixou mais cedo naquela manhã, o qual insistiu em encher sua bolsa
    com garrafas d'água e lanches \"para a estrada\"."

    "Ricardo era seu nome e ele era o coproprietário — junto com sua esposa —
    do posto de suprimentos para alpinismo onde o dragão havia passado os últimos dias."

    "Ele trabalhou e eles forneceram comida e abrigo; este era o acordo,
    similar aos que ele fez ao longo da estrada sinuosa."

    "E quando chegou a hora de ir embora, como sempre chegava,
    Ricardo apertou sua mão, deu um tapinha em seu ombro e lhe desejou
    boa viagem como um velho amigo."

    "Um amigo querido.{w} E, no entanto,{w=0.2} Ricardo estava felizmente inconsciente
    do simples fato de que seu hóspede não era humano. O amuleto encantado que ele guardava escondido
    mantinha um disfarce de humanidade."

    "Gretchen, esposa de Ricardo — e a melhor metade, o homem sempre dizia com um
    largo sorriso — preocupou-se com o dragão; um belo par de botas de alpinismo fariam
    melhor o trabalho que as sandálias velhas e gastas em seus pés, ela argumentou."

    $Kota.change ("emotion","laughing")

    "O dragão apenas riu — eles fizeram mais do que o suficiente por ele,
    e tinham tanto sua gratidão como sua bênção — antes de deixar os dois
    acenando da porta da loja."

    "Ele não olhou de volta para eles. Nunca olhava para trás."

    $Kota.change ("emotion","neutral")

    "O dragão se sacode para fora dos pensamentos, fecha sua garrafa de água e
    a joga em sua bolsa. Ele não tem tempo para devaneios. Pelas sombras no
    chão, o horário parece estar em algum lugar por volta do fim da tarde e ele
    tem muito mais chão para caminhar antes que o dia termine."

    "Seu nome é Kota e ele é um andarilho. No entanto, suas viagens estão longe de
    ser sem rumo; o dragão está procurando por algo querido para ele que foi perdido
    há muito tempo."

############################################################################
    #KOTA SCENE 2: THE RIVER
#############################################################################

    "Enquanto Kota vagueia ao longo do caminho, ouvindo os suaves sons da natureza
    em volta, seus ouvidos começam a captar um ruído tranquilo e familiar.
    Tão familiar quanto sua própria respiração."

    pause 1

    $Kota.change ("emotion","happy")

    "Um rio."

    scene bg river
    with Dissolve(2)
    show Kota:
        xalign -1.0 yalign 1.0
        ease 2.0 xalign -0.1

    "Antes que possa detê-los, seus pés o levam à origem do som.
    Ele deixa a trilha para trás, deslizando pela vegetação rasteira e saltando
    sobre troncos caídos com uma sinuosa agilidade que desmente seu tamanho."

    show Kota:
        xalign -0.1 yalign 1.0
        ease 2.0 xalign 0.5

    "Finalmente, as árvores dão lugar à visão de um riacho tortuoso e borbulhante."

    "É fundo, mas Kota não se importa. Ele tira as sandálias e se senta na margem do rio
    para enfiar seus pés cansados na água corrente."
    $Kota.change ("emotion","neutral")
    show Kota:
        xalign 0.5 yalign 1.0
        ease 1.0 yalign 1.5

    "É quentinho. Tão reconfortante."

    "Instintos antigos e meio esquecidos enchem seu peito, fazendo com que o hálito
    do dragão puxe em sua garganta. Faz tanto tempo desde a última vez que ele tomou um
    banho apropriado em um rio morno como este. A necessidade de sentir o abraço da água
    coça em suas escamas e pinica nos cantos longínquos de sua lânguida mente."
    hide Kota
    with Dissolve(0.5)

    $Kota.change ("rightarm","raised")
    $Kota.change ("leftarm","raised")
    $Kota.change ("clothes","none")

    show Kota:
        xalign 0.5 yalign 1.5
    with Dissolve(0.5)

    "Seu yukata, gasto e com um leve cheiro de suor e poeira da estrada,
    sai primeiro. Kota volta à melodia que estava cantarolando antes enquanto
    dobra as roupas em seu colo.
    De novo e de novo em um pacote bonito e organizado, e então cuidadosamente
    deixando de lado na grama macia."

    "O dragão olha em volta por um momento, certificando-se de que está completamente sozinho,
    em seguida, desenrola o fundoshi ao redor de seus quadris com a mesma elegância praticada."
    hide Kota
    with Dissolve(0.5)
    $Kota.change ("fundoshi","False")
    show Kota:
        xalign 0.5 yalign 1.5
    with Dissolve(0.5)

    "Ele sabe bem que não há vergonha em sua nudez, mas séculos de
    perambulação pelo Novo Mundo permitiram que as sensibilidades modernas da modéstia
    passassem para ele."

    "E de nada ajudam as leis desta era.{w} Houve uma época em que criaturas
    como ele eram livres para simplesmente vagar pelo mundo dos homens.{w} Hoje em dia, há
    consequências em quebrar o segredo."

    "Kota não consegue evitar um rápido arrepio de vergonha passando através
    de sua espinha ao se despir, mesmo sem ninguém em volta para vê-lo.{w} Mesmo assim,
    ele mantém suas roupas por perto, de forma que fique ao alcance do amuleto."

    show Kota:
        xalign 0.5 yalign 1.5
        ease 3.0 yalign 7.0
    "Com um leve grunhido e um pulinho, o dragão desliza para as águas mornas e
    correntes do rio."

    $Kota.change ("emotion","happy")
    kota "Ahhh…"

    pause 0.5
    scene CGKotaRiver
    with Dissolve(2)

    "Assim que as águas tocam suas escamas, seus músculos relaxam e ele afunda
    no rio até a cintura. O baixo suspiro escapa de seus lábios em uma
    expiração lenta e preguiçosa e sua cabeça e juba caem para trás para descansar na margem do rio."

    "Ele não tinha percebido o quão profundamente {i}cansado{/i} ficou; mas agora,
    com as águas impetuosas o abraçando e acariciando, a paz acalma sua
    mente pela primeira vez em séculos."

    "As calorosas correntes parecem familiares. Como um velho amigo — um velho amante —
    dando-lhe as boas-vindas a uma casa que ele deixou para trás há muito tempo."

    "Enquanto ele relaxa contra a margem do rio, sentindo as pedras duras e lisas
    abaixo e o turbilhão do rio fluente o envolvendo, Kota se agarra
    a esta familiaridade. Ele permite que sua mente divague,
    junto com suas mãos."

    "Sobre os ombros e encima do peito, suas garras
    dedilhando as saliências entre suas escamas."

    "Descendo até a barriga. Passando pela lateral e quadris. Suas coxas."

    kota "Mm..."

    "Enquanto seus pensamentos ponderantes afundam na névoa calorosa de sua meditação, um
    dedo esfrega os suaves lábios escamados da fenda na virilha do dragão."

    "Conforme desliza para dentro, provocando a sensível carne interior, aquele dedo se torna
    o de outro alguém. Alguém de muito tempo atrás."

    "Ele quase consegue ouvir a respiração dele em seu ouvido.
    Ouvir o baixo estrondo de sua voz ronronante."

    "O coração de Kota palpita em sincronia com suas pálpebras enquanto a ponta do dedo dentro de
    si roça contra um ponto que faz seus dedos dos pés curvarem e sua respiração ficar
    presa em sua garganta."

    "A carícia lenta e gentil das águas do rio de sua casa não é
    a única coisa que o dragão ansiou por todos esses anos."

    "Ele pode sentir a carne interior, o oculto comprimento de sua masculinidade,
    agitando seus pensamentos. O desejo. A necessidade."

    "Com um longo suspiro, Kota relutantemente retira o dedo de dentro de si e
    leva a mão de volta à sua barriga. Ele esfrega seu corpo, do peito
    ao pescoço."

    "Um poema meio lembrado cintila na mente do dragão enquanto suas mãos
    limpam a poeira e o suor de sua jornada."

    $Kota.change ("emotion","neutral")
    kota "  Eu gosto de lavar\n
      a poeira deste mundo\n
      nas gotas de orvalho."

    $Kota.change ("emotion","sad")

    kota "  Com gotas de orvalho pingando,\n
      desejo que de alguma forma eu pudesse lavar\n
      este mundo a perecer."

    "Sua respiração jorra de suas narinas e suas mãos caem para os lados.
    O rio assume a tarefa de acariciar suas escamas e membros com a corrente,
    seu conforto um pálido eco do que o dragão anseia."

    kota "  Não virás e verás a\n
      solidão? Apenas uma folha\n
      da árvore kiri?"

    "???" "Basho, não é?"
    scene bg river
    with Dissolve(0.5)
    show Kota:
        xalign 0.8 yalign 7.0
        ease 1.0 yalign 1.0
    with Dissolve(0.5)
    pause 1
    $Kota.change ("emotion","surprise")
    show Kota:
        xzoom -1 yalign 1.0 xalign 0.8

    "Os olhos de Kota abrem até o limite enquanto sua cabeça vira. Ele não ouviu ninguém se aproximando e,
    ainda assim, lá está um homem de pé, próximo à linha das árvores."

    show tricky smug:
        xalign 0.1 yalign 1.0
    with Dissolve(1)

    pause 2
    show tricky neutral:
            xalign 0.1 yalign 1.0

    "???" "Desculpe por me esgueirar até você assim. Não se importa com a companhia,
    não é? Parece que você poderia aproveitar um pouco."

    $Kota.change ("emotion","neutral")
    pause 1
    $Kota.change ("rightarm","relaxed")

    kota "{i}Ie, ie,{/i} ah… não, de forma alguma. Por favor."

    $Kota.change ("leftarm","relaxed")

    "O dragão transforma seu rosto em um sorriso acolhedor e gesticula para que o homem
    se aproxime com um lânguido aceno."

    $Kota.change ("emotion","puzzled")

    "Por um momento, Kota teme que sua nudez possa
    envergonhar seu convidado repentino,
    mas o homem se acomoda confortavelmente na margem do rio, próximo a ele."

    "O dragão se aproxima de suas roupas descartadas."

    show tricky neutral:
        xalign 0.1 yalign 1.0
        ease 1.0 xalign 0.0 yalign 1.2

    "???" "Desculpe de novo. Eu tenho caminhado o dia todo e meus pés estão me matando."

    $Kota.change ("emotion","neutral")

    "O estranho tira os sapatos com um longo suspiro e depois mergulha os pés
    na água, assim como Kota fez mais cedo;
    vindo da corrente do dragão, o que faz Kota sorrir enquanto acena com a cabeça para o homem."

    kota "Acredite em mim, não o culpo de forma alguma.
    Eu mesmo só parei aqui para ter um momento de descanso."
    show Kota:
        xalign 0.8 yalign 1.0
        ease 1.5 xalign 1.0 yalign 2.0
    "???" "É um ótimo lugar esse que você achou, mesmo que seja só para descansar por um
    momento. Para onde você vai depois daqui, se não se importa que eu pergunte?"

    $Kota.change ("leftarm","raised")
    kota "Ah, aqui e ali. Estou mais para um andarilho, sabe. E você, hã…?"

    "O dragão olha para o estranho com uma expressão educada, porém expectante."

    show tricky smug:
        xalign 0.0 yalign 1.2

    "???" "  Em minhas novas roupas,\n
      me sinto tão diferente, devo\n
      parecer outra pessoa."

    $Kota.change ("emotion","surprise")

    kota "Ah, também um fã das obras de Matsuo-sensei, eu vejo!"
    $Kota.change ("leftarm","relaxed")
    $Kota.change ("emotion","neutral")
    show tricky neutral:
        xalign 0.0 yalign 1.2
    "Jean" "E isso aí. Meus amigos me chamam de Jean. Eu estava fazendo uma entrega, mas...
    me perdi só um pouquinho."

    $Kota.change ("emotion","laughing")

    "O homem esfrega a nuca com uma risada envergonhada e Kota
    solta uma leve risadinha."
    $Kota.change ("rightarm","raised")
    kota "Ah, mas é quando estamos perdidos que somos mais
    facilmente capazes de encontrar a nós mesmos."

    $Kota.change ("emotion","neutral")

    kota "Claro, é mais fácil quando temos alguma ajuda. Eu ficaria feliz em
    guiá-lo de volta para a estrada, Jean-san."

    "Jean" "Obrigado, senhor...?"
    $Kota.change ("rightarm","relaxed")
    kota "Ah, {i}sumimasen{/i}. Eu sou Kota."

    "Jean" "Bem, é um prazer conhecer você, Kota. E
    sua ajuda seria muito apreciada."

    "O homem oferece sua mão com um largo sorriso e Kota se vira para apertar a mão
    de Jean, como ele se acostumou a fazer com todos que conhece.
    Porém, ele não consegue evitar de fazer uma meia reverência para Jean
    de sua posição sentada."

    "Jean" "Hm... me perdoe se eu estou supondo, mas você é do Japão, né?"

    $Kota.change ("emotion","happy")

    kota "{i}Hai{/i}, é isso mesmo. Foi uma longa jornada desde as terras da
    minha casa, mas tenho gostado de vagar por aí. É maravilhoso ver novas
    paisagens, não é? Como este rio."

    "O dragão gesticula para a paisagem idílica que os cerca.
    A água corrente e sorridente e o vento através das árvores cantando uma
    música suave e branda."

    "Os grandes ramos acima da cabeça, fornecendo sombra enquanto permitem que os diamantes da
    luz do sol cintilem na superfície fluente.
    A grama fresca à beira do rio."

    $Kota.change ("emotion","neutral")

    kota "Fiz minha casa em um rio tão preservado quanto este há muito tempo. A natureza
    imaculada carrega significado especial para mim."

    kota "Você e eu podemos ser os únicos a ver este lugar em anos.
    Veja como está intocado. Sinta o frescor do ar."

    "Jean ri."

    $Kota.change ("emotion","neutral")

    "Jean" "Bem, você com certeza é veemente, Kota.
    Isso é sempre bom de se ver em um colega de viagem."

    "Jean" "Eu mesmo sou da Europa. Até lá, lugares assim estão se tornando
    uma raridade, infelizmente. Mas ainda existe tanto para se ver."

    "Jean" "É por isso que eu me tornei um entregador, sabe. Acho que você poderia dizer que a sede
    de viajar está no meu sangue."

    $Kota.change ("emotion","puzzled")

    kota "Parece que você também está muito longe de casa, Jean-san. Tenho certeza de
    que você reuniu muitas histórias em suas jornadas de um lugar para outro."

    show tricky smug:
        xalign 0.0 yalign 1.2

    "Jean" "Ah, sim, mais do que o suficiente para várias vidas. Eu posso contar algumas delas
    para você enquanto andamos, se estiver pronto para ir."

    $Kota.change ("emotion","neutral")
    show Kota:
        xalign 1.0 yalign 2.0
        ease 1.5 yalign 1.0
    "O dragão se levanta e a água escorre de seu corpo como um manto
    de seda. Com um grunhido, Kota se alonga e então sobe
    de volta à margem, completamente seco."

    kota "Permita-me um momento para me vestir e então estarei preparado.
    E, se você quiser, tenho algumas histórias de minhas próprias viagens
    que posso compartilhar com você também."
    hide Kota
    with Dissolve(0.5)
    $Kota.change ("fundoshi","True")
    show Kota:
        xalign 1.0 yalign 1.0 xzoom -1
    with Dissolve(0.5)

    show tricky neutral:
        xalign 0.0 yalign 1.2
        ease 1.5 yalign 1.0
    "Jean" "Claro, eu ia gostar muito disso."
    hide Kota
    with Dissolve(0.5)
    $Kota.change ("clothes","kimono")
    show Kota:
        xalign 1.0 yalign 1.0 xzoom -1
    with Dissolve(0.5)
    "Os dois trocam olhares e acenos. Uma centelha de entendimento e
    aceitação pisca entre Kota e Jean; a compreensão entre dois colegas
    viajantes compartilhando a estrada um com o outro."

    scene bg forestroad
    with Dissolve(1)
    $Kota.change ("emotion","laughing")
    show tricky neutral:
        xalign 0.9 yalign 1.0 xzoom -1
    show Kota:
        xalign 0.1 yalign 1.0
    show Kota:
        ease 0.2 yalign 1.0
        pause 0.06
        ease 0.2 yalign 1.3
        pause 1.02
        repeat
    show tricky neutral:
        pause 0.3
        ease 0.2 yalign 1.0
        pause 0.06
        ease 0.2 yalign 1.1
        pause 0.7
        repeat
    with Dissolve(1)

############################################################################
    #KOTA SCENE 3: TALKING ABOUT THE HOTEL
#############################################################################

    "Enquanto os dois homens caminham lado a lado, sua conversa e risadas
    preenchem o ar. Jean relata a história de uma entrega particularmente difícil na encosta
    de uma montanha — uma viagem que durou quase três dias."

    "Em troca, Kota conta ao homem sobre todos os lugares que esteve e as paisagens
    que viu. Florestas muito parecidas com esta.
    Cidades e vilas antigas e modernas."

    "Mesmo aquela vez com o deslizamento de rochas;
    aquela foi uma grande aventura."

    "Jean ri enquanto dá um tapinha no ombro do dragão."

    "Jean" "Incrível! Você é um viajante muito experiente, né?"

    $Kota.change ("emotion","happy")
    $Kota.change ("leftarm", "raised")
    kota "Bem, eu estou na estrada há tanto tempo que ela quase se tornou minha casa."

    "Jean" "Ah, sei como é isso. Às vezes, quando estou fazendo minhas entregas,
    parece que é a única coisa que eu conheço minha vida toda."

    "Jean" "Espera..."
    $Kota.change ("leftarm", "relaxed")
    "A expressão do homem muda conforme ele olha ao redor.
    Finalmente, seus olhos brilham em reconhecimento."

    "Jean" "Ah, então foi assim que eu dei a volta!"

    "Jean" "Acho que posso encontrar o caminho a partir daqui, Kota. Muito obrigado por sua ajuda."
    $Kota.change ("emotion","laughing")
    kota "Não foi nenhum problema, Jean-san."
    $Kota.change ("emotion","puzzled")
    kota "No entanto, antes de você ir…"

    show tricky smug

    "Jean" "Você quer me perguntar alguma coisa, né."

    $Kota.change ("emotion","laughing")
    $Kota.change ("leftarm", "raised")
    kota "Sou tão fácil assim de se ler?"
    $Kota.change ("leftarm", "relaxed")
    $Kota.change ("emotion","happy")

    kota "Por acaso, alguma vez você já encontrou, bem...{w=0.2} algo que não poderia
    ser explicado?"

    "Jean" "O que você quer dizer com isso?"

    $Kota.change ("emotion","neutral")

    kota "Bem..."

    $Kota.change ("emotion","happy")

    kota "Já faz algum tempo. {w}Lá em Nihon, uma vez encontrei algo muito peculiar
    durante minhas viagens. Estive procurando por isto desde então."

    kota "Pode parecer impossível, mas...{w} de uma fonte de água quente, vi
    algo extraordinário. Era um..."

    "Jean" "Um dragão?"

    $Kota.change ("emotion","surprise")
    pause 1.3
    $Kota.change ("emotion","neutral")
    $Kota.change ("righttarm", "raised")
    "Kota agarra seu amuleto."
    kota "{i}Hai.{/i} Ele tem escamas vermelhas, um tom mais escuro que sangue. Então, você o viu?"

    show tricky neutral

    "O homem pondera por um longo momento, coçando a barba enquanto se
    perde em pensamentos profundos. Kota prende sua respiração, seu olhar
    fixo em Jean, até que o homem finalmente solta um forte suspiro."

    "Jean" "Já me deparei com muitas coisas, digamos, \"únicas\" durante
    as minhas viagens. Poucas coisas podem esperar me surpreender.{w} Mas..."

    "Jean" "Sinto muito. Queria poder ajudar você,
    mas eu nunca me deparei com alguma coisa assim."

    $Kota.change ("leftarm", "relaxed")
    pause 1
    $Kota.change ("emotion", "sad")

    kota "Ah."
    pause 1
    $Kota.change ("righttarm", "neutral")

    kota "Bem, suponho que tenha sido um tiro no escuro. Muito obrigado por sua
    companhia, Jean-san. Boa sorte com sua entrega."

    "O dragão se vira para seguir a estrada, sem olhar para trás na direção de Jean
    — como sempre — até o homem o chamar."

    show tricky smug

    "Jean" "Se bem que..."

    "Quando Kota olha para o homem, Jean está passando os dedos por sua
    barba curta. Ele hesita por um momento, como se estivesse reunindo
    seus pensamentos, e então acena."
    pause 1

    "Jean" "Sim, deve estar por aqui em algum lugar..."
    $Kota.change ("emotion", "puzzled")
    kota "O que?"

    "Jean" "Ah, foi mal, amigo. Tem um hotel por essas bandas que acabou
    de reabrir recentemente, eu estava me perguntando se você não seria capaz de
    encontrar o que está procurando por lá."

    kota "Um... hotel?"

    "Jean" "Sim. Ouvi algumas histórias sobre aquele lugar, supostamente costumava
    ser um ponto de encontro para uma variedade de indivíduos...{w} {i}únicos{/i}
    e essas coisas."

    "Jean" "Tenho certeza de que já existem alguns viajantes por lá.
    Pessoas como você e eu perambulando de um lugar ao outro.
    Eu posso não saber onde está essa coisa que você vem procurando, mas..."

    pause 1
    show tricky neutral

    "Jean" "...talvez um deles saiba?"

    "Kota considera as palavras do homem. Elas soam verdadeiras e seria pelo
    menos um começo; um melhor do que ele teve em pelo menos um século."

    $Kota.change ("emotion", "happy")

    kota "Bem, não saberei até tentar, não é?"

    kota "{i}Arigatou gozaimasu{/i}, Jean-san."

    "O dragão faz uma profunda reverência para Jean e o homem ri, meio que recusando o gesto com a mão."

    "Jean" "É o mínimo que eu posso fazer por um colega de viagem.
    Boa sorte, Kota, e eu espero que você encontre o que está procurando."

    hide tricky neutral
    with Dissolve(1)
    pause 2
    $Kota.change ("emotion", "neutral")
    show Kota:
        xalign 0.1 yalign 1.0
        ease 2 xalign 0.5
    pause 2
    show Kota:
        xalign 0.5
        ease 0.2 yalign 1.0
        pause 0.06
        ease 0.2 yalign 1.3
        pause 1.0
        repeat
    "Os dois se separam, Jean para completar sua entrega e Kota para continuar
    seguindo a estrada onde quer que ela o leve. Seus olhos estão no horizonte,
    o local para onde Jean apontou quando mencionou o \"hotel\"."

    "Talvez haja alguém lá que possa ajudá-lo.
    Alguém que possa fornecer algum tipo de orientação ou apontar na direção
    certa para encontrar o que ele está procurando."
    $Kota.change ("emotion", "sad")

    "Ou talvez, como tantas vezes antes, Kota se encontre decepcionado."

    "Dizem que não é o destino que importa, mas a jornada.
    Em seus longos anos de peregrinação, o dragão acumulou inveja daqueles que são
    capazes de acreditar nestas palavras."

    $Kota.change ("emotion", "happy")

    "No entanto, conforme segue a estrada, Kota encontra uma renovada elasticidade em seus passos.
    Um pequeno sorriso curva seus lábios e, mais uma vez, o estrondo do cantarolar de uma melodia
    junta-se aos sons da natureza, preenchendo o ar ao seu redor."

    "Seu coração parece leve, mais leve do que há séculos; mais leve
    do que jamais esteve desde que sentiu pela primeira vez a dor lancinante de sua perda."

    "Talvez isto seja esperança, ele pensa. Esperança pelo tão esperado fim de sua jornada."
    stop music fadeout 2.0
    scene bg black
    with Dissolve(1)
############################################################################
    #KOTA SCENE 4: ARRIVING AT THE HOTEL
#############################################################################

    #Kota arrives at the Hotel
label KotaISkip:
    stop music fadeout 2.0
    scene bg black
    with Dissolve(1)
    $Kota.change ("clothes", "kimono")
    $Kota.change ("fundoshi", "true")
    $Kota.change ("leftarm", "relaxed")
    $Kota.change ("rightarm", "relaxed")
    hide screen SkipButton

    pause 2
    "Quente."

    "Tão quente."

    "Mas não o calor que ele ansiava. Este é seco. Sem vida."

    "Esta terra é amaldiçoada."

    scene bg desert
    with Dissolve(2)
    pause 1
    $Kota.change("hair", "tied")
    $Kota.change("emotion", "sad")
    show Kota:
        xalign 0.5 yalign 1.0
    show Kota:
        ease 0.2 yalign 1.0
        pause 0.06
        ease 0.2 yalign 1.3
        pause 1.0
        repeat
    with Dissolve(1)

    "O dragão marcha ao longo da beira da estrada, a língua
    pendurada em sua boca aberta como a de um cão ofegante."

    "Seu suprimento de água engarrafada acabou há muito tempo. E agora, o suor secou
    completamente de seu yukata e de sua testa, dando espaço à desolação do
    deserto ao seu redor para infiltrar-se em seus ossos e peito."

    "Parece {i}errado{/i} para o dragão, assim como mergulhar na água corrente do
    riacho antes parecia {i}certo{/i}."

    "Quanto tempo se passou desde que ele deixou Jean para trás? A memória sai nadando, um
    peixe disparando para fora do alcance de seus dedos. Ele estava lá na
    floresta, agora está aqui no deserto."

    "E lá, aparecendo no horizonte, está o hotel de que o homem lhe falou."

    $Kota.change("emotion", "puzzled")

    "Ele se ergue a partir do outro lado de uma colina, quase parecendo inapropriado
    na arenosa extensão que se estende em direção ao horizonte em todas as direções.
    O estilo é um que Kota não via há muito tempo e o mau estado de conservação
    do edifício é claro e aparente, mesmo a esta distância."

    "Não é como se o dragão estivesse esperando um centro movimentado com portas polidas e
    brilhantes nunca tendo a chance de se fechar em torno da maré de viajantes
    entrando e saindo. Mas o lugar parece tão desolado quanto o deserto nos
    arredores."

    "Ainda assim, Kota está aqui. E enquanto a visão diante dele faz seu
    coração afundar um pouco, o dragão ainda segue em frente."

    "Descendo a colina arenosa, tirando uma pedra afiada de sua sandália com os dedos dos pés
    à medida que vai. Ao longo da estrada, sentindo o calor do asfalto contra as escamas de
    suas pernas. Curvando-se ligeiramente enquanto segue a entrada para o estacionamento."

    scene bg hotelexterior
    with Dissolve(1)

    "Frente. Frente. Sempre em frente."

    "Kota luta para subir os degraus da porta da frente do edifício enquanto o
    cansaço de sua jornada começa a se mostrar presente. Ele precisa parar,
    encostando contra a parede para recuperar o fôlego."

    "De perto, o hotel parece pelo menos um pouco melhor. O dragão pode ver
    os lugares onde foi feito esforço para consertar o pior do desgaste.
    Os reparos parecem bastante recentes; alguém tem que estar aqui."

    "Com uma última respiração profunda, Kota empurra a porta."

    scene bg oldlobby

    show Kota:
        xalign 2.0 yalign 1.0 xzoom -1
        ease 2.0 xalign 0.9
    with Dissolve(1)

    kota "Olá?"

    "O dragão mal reconhece sua própria voz, por mais seca e áspera que esteja.
    Ele tosse, pigarreando, arfando e engolindo saliva para molhar sua garganta, e então
    tenta novamente."
    $Kota.change("emotion", "sad")
    kota "Olá?"

    "???" "Senhor, você está bem?"
    show Kota:
        ease 0.5 yalign 3.0
    pause 0.5
    hide Kota
    with Dissolve(0.5)
    "Antes que Kota consiga responder, outro acesso de tosse balança seu corpo cansado.
    Ele sente uma presença correndo para envolver um braço em volta de suas costas e
    o dragão é conduzido para o fresco saguão do hotel."

    play sound "sfx/hum.ogg"
    show backtitle
    with Dissolve(0.25)
    hide backtitle
    with Dissolve(0.25)

    "Seu anfitrião o abaixa em uma cadeira. O mundo pisca por um momento, em seguida um copo d'água
    é empurrado na mão de Kota."

    "Kota se curva desordenadamente em gratidão antes de abrir
    bem a boca para engolir o líquido frio. Não é muito, mas
    este pouco de umidade se instala e revitaliza o dragão."

    "Ele engole, estende o copo para ser segurado por uma mão grande e coberta de pelos
    e ergue os olhos para seu anfitrião."
    play music "music/EaglesSong.ogg" fadeout 1.0 fadein 1.0
    $Asterion.change("emotion", "neutral")
    $Asterion.change("leftarm","loose")
    $Asterion.change("righttarm","loose")
    $Kota.change("emotion", "surprise")
    $Kota.change("leftarm", "raised")
    $Kota.change("rightarm", "raised")
    show Kota:
        xalign 0.9 yalign 1.0 xzoom -1
    show Asterion:
        xalign 0.1 yalign 1.0
    with Dissolve(1)
    kota "Ah. Hm."
    kota "Por favor, desculpe minha intrusão, e perdoe meu estado vergonhoso."

    $Asterion.change ("emotion","bowing")
    $Asterion.change ("leftarm","raised")

    "???" "Não é problema. Fico feliz em oferecer ajuda."
    $Kota.change("leftarm", "relaxed")
    $Kota.change("rightarm", "relaxed")
    kota "Obrigado."
    $Kota.change("emotion", "neutral")
    "O dragão respira lenta e profundamente uma vez, e então outra. E mais uma.
    A sensação dolorida se instala em seus membros cansados, diminuindo ligeiramente
    à medida que se espalha através de seu corpo."

    "Kota aproveita a oportunidade para olhar ao redor no saguão do hotel,
    examinando tanto o cômodo quanto o aparente proprietário."

    $Asterion.change ("emotion","neutral")
    $Asterion.change ("leftarm","loose")

    if Asterion.clothes == "nude":

        "Kota sente seu rosto esquentar ao ver a maneira como o homem está vestido e,
        educadamente, direciona o olhar para baixo."

        "Um dono de hotel vestindo algo tão revelador não é algo que ele
        encontrou em suas viagens; De maneira semelhante, ele também não conheceu
        um meio-homem meio-touro.
        Talvez seja um costume específico de sua espécie?"

        "???" "Algum problema, senhor?"

        $Kota.change("emotion", "surprise")

        kota "Ah, não, não. Perdoe minha grosseria.
        Apenas fui surpreendido por sua maneira de se vestir."

        $Asterion.change ("emotion","smiling")

        if chapter6LieAboutUndies <2:
            $Asterion.change ("emotion","surprise")
            "A criatura olha para baixo por um momento, e então uma expressão de vergonha cruza seu rosto..."
            if chapter6LieAboutUndies ==0:
                "???" "M-minha perizoma não deve ser apropriada para o período.
                Eu peço desculpas!"
            else:
                $Asterion.change ("emotion","smiling")
                "???" "Você gosta? O mestre disse que este era o estilo moderno e
                eu fico feliz que tais roupas estejam de volta à moda. Desejo representar
                nosso Hotel da melhor maneira possível."

                $Kota.change("emotion", "puzzled")
                "Kota tenta manter uma aparência educada, mas não consegue evitar franzir a testa.
                Tangas estão na moda aqui? Deveria ele se despir e ficar apenas com seu fundoshi?
                Como alguém reage a uma situação como esta?"
                pause 2.0
                $Asterion.change("emotion", "sad")
                pause 1.0
                "A criatura reage à expressão involuntária de Kota.
                Ele parece desapontado, mais do que qualquer coisa.
                Kota lamenta não ter sido mais sutil sobre seu dilema."
                "O silêncio começa a ficar desconfortável."
                $global_affection -=0.5
                $chapter6LieAboutUndies =2
        else:
            if chapter6LieAboutUndies ==2:
                $Asterion.change("emotion", "tired")
                asterion "D-Devo me desculpar pelo meu traje. Não foi realmente minha escolha."
            else:
                $Asterion.change("emotion", "sad")
                "A criatura parece terrivelmente desapontada. Ele sabe que foi enganado —
                e mais de uma vez."
                $global_affection -=0.5

        $Kota.change("emotion", "puzzled")
        "Apenas quão longe Kota vagou no deserto?"

    $Asterion.change ("emotion","neutral")

    asterion "Ah, perdão."

    $Kota.change("emotion", "neutral")

    $Asterion.change ("emotion","bowing")
    $Asterion.change ("leftarm","raised")

    show Asterion:
        ease 0.5 yalign 1.5
        ease 0.5 yalign 1.0

    asterion "Seja bem-vindo ao Hotel, senhor. Eu sou Astério, o Zelador deste
    aprazível estabelecimento. O Mestre está ocupado com outra coisa no momento,
    mas eu ficaria feliz em apresentá-lo mais tarde."
    $Asterion.change ("leftarm","loose")

    asterion "Por ora, por favor, me comunique se houver algo que eu possa fazer
    por você, ou quaisquer perguntas que eu possa responder."

    $Kota.change("emotion", "happy")

    kota "Muito obrigado, senhor Astério. Eu ouvi falar sobre a inauguração de seu
    hotel e quis vir para ver com meus próprios olhos.{w} E devo dizer que estou satisfeito..."

    kota "Eu nunca vi um minotauro na minha vida!{w} Viajei por todo o
    globo, vi todos os tipos de seres...{w} mas sempre pensei que os minotauros fossem apenas
    uma lenda.{w}"

    kota "Este lugar realmente deve ser especial, para um espécime tão raro estar aqui."

    kota "Embora..."

    $Asterion.change ("emotion","neutral")

    show Asterion:
        ease 0.5 yalign 1.5
        ease 0.5 yalign 1.0

    "O dragão olha ao redor no saguão vazio. O Zelador meio-homem meio-touro
    parece capaz de ler facilmente a expressão de Kota e o oferece outra profunda reverência."

    $Asterion.change ("emotion","bowing")

    asterion "Sim, o Hotel reabriu recentemente e acabamos de começar
    a aceitar hóspedes."

    $Asterion.change ("emotion","sad")

    asterion "Na verdade, é embaraçoso dizer, mas você está entre os primeiros
    em um bom tempo."

    if first_guest == "Luke":
        $Asterion.change ("emotion","angry")
        asterion "Pelo menos você tem modos melhores que os do último."

    $Asterion.change ("emotion","smiling")
    asterion "Independentemente disso, você está convidado a ficar o tempo que quiser."

    "O dragão cantarola em pensamento, deixando suas garras roçarem através
    e puxarem sua barba."

    "As palavras que Jean proferiu em sua despedida,
    as quais o impulsionaram para a jornada ao longo da estrada deserta do lado de fora,
    provocam no fundo de sua mente mais uma vez. Novamente, ele olha ao redor no saguão vazio e,
    em seguida, para o rosto de Astério."

    "Por trás de sua fachada servil, o meio-homem meio-touro parece ansioso.
    Seus cascos batem levemente contra o ladrilho enquanto ele intercala o peso entre eles e
    uma seriedade quase infantil cintila por trás de seu sorriso educado;
    não menos amigável por causa da metade faltante do rosto de Astério."

    "O hotel parece estar tão degradado quanto seu Zelador.
    Mas há potencial aqui. Esperança."

    $Kota.change("emotion", "laughing")

    kota "Muito obrigado, senhor Astério. Eu ficaria feliz em ficar
    pelo menos um pouco."

    $Kota.change("emotion", "sad")

    kota "Tenho muito pouco dinheiro..."

    $Kota.change("emotion", "happy")

    kota "Mas eu ficaria feliz em realizar qualquer tarefa que você precise que
    me permita ganhar uma cama e uma refeição quente."

    $Asterion.change ("emotion","smiling")

    asterion "Isto não será necessário, senhor. Esta é nossa pré-inauguração,
    então não cobraremos de você. Na verdade, cobramos muito pouco regularmente,
    então dinheiro não é um problema."

    asterion "Contanto que o Hotel seja capaz de cumprir sua missão."

    "Astério se move para pegar o livro de registros e uma caneta da mesa da frente e
    traz para o dragão."

    asterion "Basta assinar aqui e preencher um pouco de informação."

    show Kota:
        ease 0.5 xalign 0.7
        pause 1
        ease 0.5 xalign 0.9

    "Depois de alguns momentos de escrita, o meio-touro meio-homem aceita
    o livro de registros de volta de Kota e examina as informações do novo hóspede."

    $UI_permissions['guests'] = True
    $check_in_guest('Kota')
    play sound "sfx/asterionchord.mp3"
    if renpy.variant("android"):
        "{color=[UIColorOrange]}Kota{/color} foi registrado no hotel.
        \nVocê pode abrir o menu e ir para a tela {color=[UIColorOrange]}hóspedes{/color}
        para ver seus hóspedes atuais."
    else:
        "{color=[UIColorOrange]}Kota{/color} foi registrado no hotel.
        \nVocê pode ver seus hóspedes atuais na tela {color=[UIColorOrange]}hóspedes{/color} no
        menu, ou clicando no ícone do livro de registros."

    asterion "Senhor Kota... sem sobrenome. Nascido em 2 de fevereiro de 1615. Devo dizer
    que você está muito bem para a sua idade, senhor."

    $Kota.change("emotion", "puzzled")

    "Kota pisca. Franze a testa. Estende a mão para o livro de registros."

    kota "Com licença. Posso ver isto um momento?"

    "Ele examina sua escrita. Genna 1, 5º dia do 1º mês.
    Exatamente da forma como ele havia escrito."

    kota "Não me dei conta de que você podia ler japonês, senhor Astério."

    $Asterion.change ("emotion","surprise")

    asterion "Japonês, senhor...?"

    $Kota.change("emotion", "surprise")

    "E é então que atinge Kota. O formato de sua língua à medida que ele falou
    com o minotauro todo esse tempo pareceu estranho, apenas agora ele percebe
    que, depois de seu acesso de tosse, ele mudou para sua língua nativa sem
    perceber."

    "E, ainda assim, Astério foi capaz de entendê-lo. Na verdade, o meio-homem
    meio-touro nem sequer pareceu perceber que Kota estava falando outra língua."

    "Como?"

    $Asterion.change ("emotion","neutral")
    $Asterion.change ("rightarm", "hips")
    asterion "Ah, entendi. Eu compreendo agora."

    asterion "Não se assuste, senhor. É apenas uma peculiaridade do Hotel."

    asterion "Nos permite compreender todos os hóspedes que passam por nossas
    portas, independentemente do país de origem ou da língua que
    escolhem falar."

    $Asterion.change ("emotion","smiling")

    asterion "Eu mesmo sou do Mediterrâneo, muito longe daqui, então você pode
    descansar sabendo que todos os hóspedes são bem-vindos, não importa de onde venham."

    asterion "Devo também acrescentar... {w}Eu posso ver que você é um dragão. Encantamentos
    não funcionam aqui. Mas não se preocupe, isto é permitido aqui. Todos os que estão perdidos
    são bem-vindos."

    "Um lugar para andarilhos, de fato."

    kota "Entendo."

    $Kota.change("emotion", "happy")

    show Kota:
        ease 0.5 yalign 3.0
        ease 0.5 yalign 1.0

    "O dragão se levanta e oferece a Astério uma profunda reverência. Se o que Jean
    e este meio-homem meio-touro disseram for verdade, então talvez seja
    exatamente aqui que Kota precisa estar."

    $Kota.change("rightarm", "raised")
    kota "Muito obrigado, senhor Astério. Você me honra com sua hospitalidade."

    "Astério se move para colocar o livro de registros de volta na mesa da frente e retorna
    para Kota com uma chave. Ele a passa para o dragão enquanto dá a Kota outro sorriso
    de boas-vindas."
    $Kota.change("rightarm", "relaxed")
    asterion "Aqui está sua chave, Sr. Kota. Se quiser,
    Posso mostrá-lo seu quarto."

    $Asterion.change ("emotion","bowing")
    $Asterion.change ("leftarm","raised")
    $Asterion.change ("rightarm", "loose")
    asterion "Espero que tenha uma estadia agradável conosco."

    scene bg black
    with Dissolve(3)

    #Same as luke's, we jump to chapter 6 or 7.
    if first_guest == "Kota":
        jump chapter6_1
    else:
        jump chapter7_1

label chapter6_1:
#First guest to lounge
#Segue from first guest scene to lounge

    $chapter = "Capítulo 6"
    call screen ChapterTransition("Capítulo 6", "Festa de boas vindas")
    pause 0.5
    $save_name=output_save_name("Capítulo 6")

    play music "music/GreekFolkSong.ogg" fadeout 1.0 fadein 1.0
    if chapter6StayInRoom:
        scene bg oldquarters
        with Dissolve(2)

        "Já se passou muito tempo desde que Astério saiu para cuidar da lareira e
        inspecionar o hotel. Enquanto isso, você decidiu permanecer em seus aposentos."

        "O momento de solidão provou-se benéfico. Tanta coisa aconteceu nos últimos dias —
        o encontro com o velho, ter achado o hotel e o minotauro dentro,
        a altercação com Argos."

        "Algumas horas de folga lhe deram a chance de pensar em tudo."

        "O hotel possui energia elétrica agora, pelo menos. Mais cedo esta manhã, você desejou
        uma tomada para conectar seu celular e, após um piscar de olhos, ela se materializou
        para você."

        if player_background == "tech":
            "No entanto, foi uma boa ideia colocar o carregador do celular ali?
            O hotel escolheria a voltagem e frequência corretas?"

            "Pode ter sido imprudente, mas você tentou mesmo assim, se apenas para saciar
            sua curiosidade."

        "Você o verifica depois de passar algumas horas deitado no sofá.
        Ele mal havia carregado dois por cento da bateria.
        Provavelmente não permanecerá ligado por mais de um minuto."

        "Astério entra enquanto você manuseia seu celular."

        $Asterion.change ("emotion","bowing")
        $Asterion.change ("leftarm","raised")
        show Asterion:
            xalign 0.5 yalign 1.0
        with Dissolve(1)
        asterion "Boa tarde, Mestre."
        you "Oi, Astério. Como está a lareira?"

        $Asterion.change ("emotion","smiling")

        asterion "Ah, sim, a lareira. Está indo bem."

        asterion "Eu não quero incomodá-lo,
        mas tenho ótimas notícias."

        $Asterion.change ("leftarm","loose")

        "Astério caminha até você em um passo rápido e animado e lhe entrega o livro de registros.
        Ele fica lá, esperando você abri-lo."

        show Asterion:
            ease 0.2 yalign 1.1 xalign 0.52
            ease 0.2 yalign 1.0 xalign 0.5
            ease 0.2 yalign 1.1 xalign 0.48
            ease 0.2 yalign 1.0 xalign 0.5
            ease 0.2 yalign 1.1 xalign 0.52
            ease 0.2 yalign 1.0 xalign 0.5

        "Ele intercala o peso de casco para casco e sua cauda balança para frente e para trás
        em uníssono com suas orelhas agitadas."

        show Asterion:
            yalign 1.0 xalign 0.5

        if first_guest == "Luke":
            you "Lucas Walker, 1923, hein? O que um sujeito tão velho está fazendo no meio do deserto?
            Você ofereceu uma garrafa d'água para ele pelo menos?"

            $Asterion.change ("emotion","neutral")

            asterion "...As aparências enganam, Mestre.
            A idade é uma das últimas preocupações que tenho sobre ele. Suponho que você verá."
        else:
            you "‘Kota’. Só, ‘Kota’, hum?"
            pause 1
            you "Espere um pouco. 1615?"
            $Asterion.change ("emotion","tired")
            asterion "Eu nasci muitos séculos atrás também, Mestre."
            asterion "Geralmente nossos hóspedes são humanos, mas não todos eles..."
            you "Ainda estou me acostumando com isso, Astério. Bem, vou ter que
            ver isso por conta própria agora."
        $Asterion.change ("emotion","smiling")
        asterion "Gostaria de conhecer nosso hóspede, Mestre? Ele deve estar em seu próprio quarto agora."
        you "Claro. Acho que fiquei deitado no sofá por tempo suficiente."

        scene bg staircase
        with Dissolve(1)

        "Você e Astério deixam o escritório e voltam para a escadaria.
        Ao fazer isso, a parede se fecha atrás de você, escondendo os aposentos do Mestre novamente."
        "Astério guia o caminho. Descendo a escada por dois andares e, em seguida, atravessando um corredor."

        $Asterion.change ("rightarm","hips")
        show Asterion
        "Você está olhando para uma das portas, com Astério ao seu lado.
        Ele morde o próprio lábio para se impedir de sorrir, mas não adianta;
        ele está como uma criança prestes a abrir um presente."
        "No entanto, você não ouve nada vindo do outro lado da porta."

        $Asterion.change ("emotion","neutral")
        "As orelhas grandes e flexíveis de Astério sacodem. Ele instintivamente vira a cabeça
        para tentar capturar qualquer som vindo do quarto, então vira de volta quando lembra
        que sua outra orelha ainda não cresceu completamente."
        $Asterion.change ("rightarm","loose")
        asterion "Ele não está aqui."
        you "Talvez ele esteja perdido. Eu não o culparia."
        hide Asterion
        "Você e Astério voltam para a escadaria e começam a chamar seu
        hóspede. Ao não ouvir uma resposta, vocês voltam para o saguão..."

        scene bg oldlobby
        with Dissolve(1)
        "... Mas ninguém está aqui também, então vocês continuam."
        scene bg lounge
        with Dissolve(1)
        "Vocês dois tentam uma sucessão de quartos sem sucesso,
        até que se encontram no salão."
        show Asterion
        with Dissolve(1)
        asterion "Sem sinal dele aqui."
        $Asterion.change ("emotion","neutral")
        "Você está prestes a desistir e descansar, talvez tomar um ou dois drinques
        antes de retomar sua busca, até ouvir passos se aproximando no salão."

    else:
        scene bg lounge
        with Dissolve(2)

        "Já se passou mais ou menos uma hora desde que Astério deixou o salão."

        "O minotauro o guiou de volta para a lareira do hotel para verificá-la.
        Tudo parecia estar em condições de funcionamento."

        "Vocês dois fizeram as rondas e inspecionaram o hotel. Os quartos, a escadaria,
        o salão, cada lâmpada, interruptor e porta que vocês pudessem encontrar."

        "Algumas paredes ainda estavam rachadas, as janelas estavam quebradas e algumas infiltrações
        de água aqui e ali. A visão desagradou Astério, mas o hotel parecia estar
        se recuperando a um ritmo impressionante."

        "Vocês dois pararam no salão para fazer uma pausa e comemorar um trabalho bem feito.
        Astério serviu sua bebida favorita novamente e —com sua permissão—
        pegou uma taça de vinho para si mesmo."

        "Depois de um breve bate-papo, você verificou a hora apenas para perceber que a bateria de seu celular
        estava descarregada há muito tempo."

        "Mas o Hotel possui energia agora.
        Você desejou uma tomada para conectar seu celular e, após um piscar de olhos,
        ela se materializou diante de você."

        if player_background == "tech":
            "Porém, era uma boa ideia colocar o carregador ali?
            O hotel acertaria a voltagem e frequência corretas?"
            "Pode ter sido imprudente, mas você tentou mesmo assim, se apenas para saciar
            sua curiosidade."

        "Astério estava ansioso para retomar a inspeção. Você estava aproveitando o intervalo,
        então o deixou continuar sem você."

        "O tempo sozinho provou-se benéfico. Tanta coisa aconteceu nos últimos dias —
        o encontro com o velho, ter achado o hotel e o minotauro dentro,
        a altercação com Argos."

        "Depois de um drinque e um pouco de tempo você não se sentiu tão sobrecarregado. Toda a
        loucura parecia estar sob controle."

        "Você verifica seu celular depois de passar duas horas em uma poltrona perto da lareira.
        Ele mal havia carregado três por cento da bateria.
        Provavelmente não permanecerá ligado por mais de um minuto."

        "À medida que volta para o sofá para se sentar, você escuta um som que tornou-se
        familiar para você ao longo dos últimos dias — Os cascos de Astério batendo em sua direção."

        $Asterion.change ("emotion","bowing")
        $Asterion.change ("leftarm","raised")
        show Asterion:
            xalign 0.5 yalign 1.0
        with Dissolve(1)

        asterion "Boa tarde, Mestre."

        you "Oi, Astério. Terminou sua inspeção?"

        $Asterion.change ("emotion","smiling")

        asterion "Bem, tive que terminá-la cedo. Não quero incomodá-lo,
        mas tenho ótimas notícias."

        $Asterion.change ("leftarm","loose")

        "Astério caminha até você em um passo rápido e animado, e lhe entrega o livro de registros.
        Ele fica lá, esperando você abri-lo."

        show Asterion:
            ease 0.2 yalign 1.1 xalign 0.52
            ease 0.2 yalign 1.0 xalign 0.5
            ease 0.2 yalign 1.1 xalign 0.48
            ease 0.2 yalign 1.0 xalign 0.5
            ease 0.2 yalign 1.1 xalign 0.52
            ease 0.2 yalign 1.0 xalign 0.5
        "Ele intercala o peso de casco para casco e sua cauda balança para frente e para trás
        em uníssono com suas orelhas agitadas."
        show Asterion:
            yalign 1.0 xalign 0.5
        if first_guest == "Luke":
            you "Lucas Walker, 1923, hein? O que um sujeito tão velho está fazendo no meio do deserto?
            Você ofereceu a ele uma garrafa d'água pelo menos?"
            $Asterion.change ("emotion","neutral")
            asterion "...As aparências enganam, Mestre.
            A idade é uma das últimas preocupações que tenho sobre ele. Suponho que você verá."
        else:
            you "‘Kota’. Só, ‘Kota’, hum?"
            pause 1
            you "Espere um pouco. 1615?"
            $Asterion.change ("emotion","neutral")
            asterion "Eu nasci muitos séculos atrás também, Mestre."
            asterion "Geralmente nossos hóspedes são humanos, mas não todos eles..."
            you "Ainda estou me acostumando com isso, Astério. Bem, vou ter que ver isso por conta própria agora."

        $Asterion.change ("emotion","smiling")
        you "Você parece uma criança em véspera de Natal, sabia."

        $Asterion.change ("emotion","contemplative")
        asterion "Por favor, me desculpe, Mestre. Eu apenas... não
        recebo hóspedes há muito tempo."

        you "Bem, mal posso esperar para conhecer esse cara. Estou intrigado.
        Você acha que ele está no quarto agora?"

        asterion "Suponho que sim. Eu prefiro não incomodar os hóspedes,
        mas... esta é uma ocasião especial, não é mesmo? Talvez desta vez..."

        $Asterion.change ("emotion","neutral")

        "Você está prestes a seguir caminho para o quarto do novo hóspede quando
        ouve passos se aproximando do salão."

############################################################################
#                          FIRST GUEST TAKES LOUNGE
############################################################################

#regardless of whether you waited in the quarters or not, resume here."
#go to scene where luke or kota change the lounge

    if first_guest == "Kota":

        $Kota.change("emotion", "happy")
        $Kota.change("rightarm", "relaxed")
        $Kota.change("leftarm", "relaxed")

        "Os passos são lentos e regulares, cuidadosamente medidos, como se aquele que
        se aproxima estivesse aproveitando o doce momento para observar os arredores."

        play music "music/TheSorrow.ogg" fadeout 1.0 fadein 1.0

        "São acompanhados por um leve som, seguindo cada passo.
        Uma melodia simples e tranquila, cantarolada em uma voz profunda e retumbante."

        "A melodia é como o fluir de um riacho, firme e constante."

        show Asterion:
            xalign 0.5 yalign 1.0
            ease 1.0 xalign 0.1
        pause 0.5
        show Kota:
            xalign 0.9 yalign 1.0
        with Dissolve(1)

        "Quando o primeiro hóspede chega ao salão, seus olhos já estão vagando
        de cima a baixo para captar a grandeza e decadência persistentes do lugar."

        $Kota.change("emotion", "neutral")

        "Ele parece estar perdido em pensamentos enquanto examina os sofás de couro,
        a lareira, as mesas e cadeiras."

        "É apenas quando Astério limpa a garganta com um educado
        pigarreio que o dragão parece perceber que vocês estão lá."

        show Kota:
            xzoom -1
        $Kota.change("emotion", "surprise")

        pause 1
        $Asterion.change ("emotion","smiling")
        $Asterion.change ("leftarm","raised")

        asterion "Espero que as acomodações sejam de seu agrado, Sr. Kota?"

        $Asterion.change ("leftarm","loose")

        $Kota.change("emotion", "happy")
        $Kota.change("leftarm", "raised")

        kota "Ah, Sr. Astério! Elas são mesmo, obrigado."

        kota "Perdoe-me, eu estava apenas olhando em volta."

        $Kota.change("leftarm", "relaxed")

        you "Está tudo bem. Vá em frente e sinta-se em casa."

        "O dragão, Sr. Kota, olha para você quando você fala.
        Ele o oferece uma profunda reverência e um sorriso educado."

        $Kota.change("emotion", "neutral")

        kota "Muito obrigado pela hospitalidade.
        Presumo que você seja o Mestre que o Sr. Astério mencionou em meu check-in?"

        if player_background == "speedrunner":
            "Você acena com a cabeça, observando o dragão — um dragão japonês de verdade!\n
            E suas roupas — um yukata japonês de verdade!"

            you "Isso mesmo. Estou no comando deste lugar. Meu nome é [player_name].
            Você não precisa me chamar de {i}'-Sama'{/i}, só {i}'-San'{/i} já está bom."

            "Você sorri com a chance de finalmente colocar seu conhecimento da cultura
            japonesa em bom uso. Eles o chamaram de nerd, morador de porão,
            weeb; mas quem está rindo agora?!"

            $Asterion.change ("emotion","tired")
            $Kota.change("emotion", "puzzled")

            "Kota vê o brilho maníaco em seus olhos e seu sorriso educado começa a ficar tenso."

        elif player_background == "leader":
            you "Isso mesmo. Eu estou no comando deste lugar. Meu nome é [player_name]."

            "Você oferece sua mão ao dragão e ele a pega
            depois de um momento de hesitação."

            you "Fico feliz em ter você aqui com a gente e espero que sua estadia seja agradável, Sr. Kota."

            "O dragão lhe concede outra reverência, desta vez mais profunda, enquanto balança sua mão firmemente."

            $Kota.change("righttarm", "raised")

            kota "Obrigado novamente, Mestre [player_name]."

        else:
            you "Sim, sou o dono. Meu nome é [player_name]."
            "O sorriso do dragão se alarga. Ele o concede outra reverência,
            desta vez mais profunda, enquanto balança sua mão firmemente."

            $Kota.change("emotion", "laughing")
            $Kota.change("righttarm", "raised")

            kota "É uma honra, Mestre [player_name]."

            you "Hm, tudo bem."

        $Kota.change("righttarm", "relaxed")
        $Kota.change("emotion", "neutral")
        $Asterion.change("emotion", "neutral")

        "Astério pigarreia novamente, ganhando a atenção do dragão mais uma vez."

        $Asterion.change ("leftarm","raised")

        asterion "Há algo que posso fazer por você no momento, Sr. Kota?
        Uma refeição ou uma bebida, talvez?"

        $Kota.change("emotion", "happy")
        kota "Ah, não, não. Muito obrigado mas, como eu disse, estou apenas olhando em volta agora."
        $Kota.change("emotion", "neutral")
        kota "Talvez mais tarde."

        $Asterion.change("emotion", "bowing")
        asterion "Muito bem."

        $Asterion.change("emotion", "neutral")
        asterion "Então, se me permite a ousadia de perguntar, o que você acha de nosso bom hotel até agora?"
        $Kota.change("emotion", "puzzled")
        kota "É... ótimo. Apenas um pouco mais degradado do que havia imaginado, e
        pensei que já teriam hóspedes a essa altura."
        kota "Mas suponho que é isso o que eu ganho por criar esperanças."
        $Asterion.change("emotion", "sad")
        $Asterion.change ("leftarm","loose")
        asterion "Ah. Eu… eu entendo."
        "O minotauro tenta manter um rosto neutro, mas você pode dizer que as
        palavras de Kota cortaram profundamente. O Hotel é o orgulho e a alegria de Astério,
        e tê-lo criticado pelo primeiro hóspede em anos desta forma deve doer."

        menu:
            "Ficar em silêncio.":
                you "..."
                asterion "Peço sinceras desculpas. Por favor, apenas nos dê um pouco mais de
                tempo para trazer o Hotel de volta aos padrões."
                $Kota.change("emotion", "surprise")
                kota "Não, não, não há necessidade disso.
                Por favor, perdoe-me se minha fala pareceu rude, Sr. Astério."

            "É um trabalho em progresso.":
                you "Bem, ei, é um trabalho em progresso. Você devia ter visto como parecia
                quando eu cheguei aqui."
                asterion "..."
                you "Hm... o que eu quero dizer é… estamos trabalhando nisso e, assim que
                colocarmos tudo em ordem no lugar, acredito que você ficará maravilhado."
                $Kota.change("emotion", "happy")

            "Se você não gosta, pode ir embora.":
                you "Se não está de acordo com seus padrões, você está livre para ir embora a qualquer momento.
                A porta está bem ali, no final daquele corredor."
                $Kota.change("emotion", "surprise")
                you "Tenho bastante certeza de que você não vai encontrar um lugar melhor em quilômetros mas, ei,
                se você quiser voltar para o deserto, a escolha é sua."
                $Kota.change("emotion", "sad")
                pause 2
                kota "Peço sinceras desculpas. Me envergonha ter insultado meus graciosos anfitriões."

        $Asterion.change("emotion", "neutral")
        $Kota.change("emotion", "neutral")

        kota "Apesar de como as coisas parecem agora, posso dizer que este já foi um lugar grandioso.
        Consigo ver sua beleza mesmo sob toda a poeira e decadência."

        $Kota.change("righttarm", "raised")

        kota "Embora, se são apenas vocês dois, então imagino que levará um bom tempo
        para restaurar sua antiga glória. Não há mais funcionários aqui?"

        $Kota.change("righttarm", "relaxed")

        you "Pode supreender você, mas eu e o Astério conseguimos dar conta de muita coisa.
        Ainda assim, é, nós estamos procurando pessoas dispostas a fazer parte da nossa equipe."

        you "Astério, você pode contar ao Sr. Kota como as coisas funcionavam aqui antigamente?"

        $Asterion.change("emotion", "contemplative")
        $Asterion.change("rightarm", "hips")

        asterion "Sim... Antes que surgissem problemas com o gerente anterior,
        era bastante comum os hóspedes escolherem permanecer aqui indefinidamente."

        asterion "A maioria não tinha nenhum outro lugar para onde ir, entende.
        E nós podemos pagar razoavelmente bem. Ou devemos em breve,
        tendo em vista que o hotel não visa gerar lucros."

        $Asterion.change("emotion", "smiling")

        asterion "E os hóspedes que se juntam à nossa equipe podem usufruir de
        todas as facilidades do Hotel pelo tempo que quiserem, gratuitamente."

        $Kota.change("emotion", "puzzled")

        kota "É mesmo? Hm..."

        "O dragão começa a deslizar as garras por sua longa barba,
        olhando de você para Astério e vice-versa. Finalmente, uma faísca de
        esclarecimento brilha em seus olhos."
        $Asterion.change("emotion", "neutral")
        $Kota.change("emotion", "neutral")

        kota "Sr. Astério... quando fiz o check-in, ofereci meus serviços em
        troca de permissão para ficar. Se vocês dois estão precisando de funcionários,
        então ficarei feliz em ajudar de qualquer forma que possa retribuir a hospitalidade dos dois."

        kota "Trabalhei em muitos empregos peculiares ao longo dos meus anos de viagem e ganhei
        uma variedade de habilidades."

        $Kota.change("righttarm", "raised")

        kota "Cozinhar, limpar, alguns anos fazendo trabalho manual — Pode não parecer..."

        $Kota.change("emotion", "laughing")

        "O dragão dá um tapinha na firme e redonda elevação de sua barriga com uma risada."

        kota "Mas meu corpo é sólido."

        $Kota.change("emotion", "happy")
        $Kota.change("righttarm", "relaxed")

        kota "Eu até passei alguns meses como barman há... hmm... vinte anos atrás? Trinta?"

        $Kota.change("emotion", "neutral")

        kota "Falando honestamente, aquele foi meu trabalho preferido.
        As conversas com as pessoas —- contos trocados e segredos divulgados,
        para serem mantidos em sigilo."

        kota "Encontrar a bebida certa para seu cliente...
        Aquela que abrandasse suas preocupações e ajudasse a aliviar o peso de seus fardos,
        ao menos pelo pouco tempo que passavam no balcão..."

        $Asterion.change("emotion", "contemplative")
        "A expressão do dragão fica pensativa e seu olhar distante.
        Quando você olha para Astério, enxerga uma expressão semelhante
        nos olhos do minotauro enquanto ele murmura e pensa."

        "O momento é quebrado quando Kota se sacode para fora de seu devaneio.
        Ele lhe direciona um sorriso pesaroso."

        $Kota.change("emotion", "happy")

        kota "Perdoe-me, às vezes me perco em recordações."

        kota "O que quero dizer é que posso fazer qualquer coisa que precisarem de mim.
        Fico feliz em ajudar."

        $Asterion.change("emotion", "smiling")

        "Você consegue sentir os olhos de Astério em você. Quando você olha para o touro,
        o vê implorando silenciosamente por sua permissão para falar."

        you "Se você tem algo a dizer, vá em frente, Astério."

        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")

        asterion "Muito bem, Mestre [player_name]."

        asterion "O salão poderia aproveitar os serviços de um bom barman.
        Embora eu possa desempenhar o papel bem o suficiente, tenho outros deveres como
        Zelador que vêm primeiro."

        $Asterion.change("emotion", "neutral")

        asterion "A gestão do salão foi muitas vezes delegada a um hóspede
        apropriado no passado."

        $Asterion.change("emotion", "smiling")
        $Asterion.change("leftarm", "loose")

        asterion "Acredito que ele estaria em boas mãos com você
        atrás do balcão, Sr. Kota."

        you "Pois bem, isso encaixa perfeitamente."

        $Kota.change("emotion", "laughing")
        $Kota.change("righttarm", "raised")
        $Kota.change("leftarm", "raised")

        kota "No país em que nasci, costumava-se dizer que a sorte segue o
        rastro dos dragões. Embora eu mesmo não possa me beneficiar dela,
        fico feliz em oferecê-la aos meus graciosos anfitriões."

        you "Acredite, nós podemos aproveitar toda boa sorte que conseguirmos."

        you "Mas antes de nos anteciparmos, queria perguntar uma coisa a você, Sr. Kota.
        Você disse antes que criou esperanças antes de chegar aqui...
        o que você esperava encontrar?"

        $Kota.change("emotion", "surprise")
        pause 2
        $Kota.change("emotion", "happy")
        $Kota.change("righttarm", "relaxed")
        $Kota.change("leftarm", "relaxed")

        kota "Vejo que nada lhe passa despercebido, Mestre [player_name]."

        "Você não diz nada e permite que o dragão organize seus pensamentos."

        $Kota.change("emotion", "sad")

        kota "Por anos —séculos agora— estive procurando por algo.
        Alguém querido para mim, que se perdeu há muito tempo."

        kota "Viajei o mundo inteiro em busca dele,
        mas até agora não tive sorte alguma. Não importa onde eu tenha ido ou para quantas pessoas tenha perguntado."

        kota "Quando soube da inauguração deste Hotel, pensei...
        talvez houvesse alguém aqui que pudesse oferecer uma pista na minha procura.
        Este Hotel é um lugar para viajantes se reunirem, não é?"

        $Kota.change("emotion", "neutral")

        "O dragão se curva e sua expressão fica vazia.
        No entanto, você consegue enxergar desespero brilhando em seus olhos apenas por um momento."

        "O desespero de um homem que chegou tão perto de seu objetivo apenas
        para ter o tapete embaixo de si puxado de novo e de novo."

        kota "Se permitir que eu fique aqui, para falar com os outros hóspedes e
        escutar suas histórias de viagem, talvez eu encontre a pista que estive procurando."

        you "E você planeja ir embora assim que encontrar?"

        $Kota.change("emotion", "sad")

        "Novamente, os olhos do dragão brilham."

        $Kota.change("emotion", "neutral")

        kota "Terei permissão para isso?"

        asterion "É claro. Este Hotel não foi feito para ser uma prisão."

        $Asterion.change ("emotion","tired")

        asterion "Para os hóspedes, pelo menos."

        $Asterion.change ("emotion","neutral")

        asterion "Você estará livre para ir embora assim que encontrar o que
        procura, Sr. Kota.{w} Ou no momento que desejar, naturalmente."

        $Kota.change("emotion", "laughing")

        kota "Eu não planejo desaparecer no meio da noite, se isto os preocupa.
        Me assegurarei de cumprir com o combinado para que minha partida não seja inconveniente para vocês."

        $Kota.change("emotion", "happy")

        kota "Eu não sei quanto tempo vai demorar até que eu encontre o que estou procurando, de qualquer maneira."

        kota "Até chegar a hora, posso muito bem fazer minha parte como seu hóspede, não é mesmo?"

        $Asterion.change("emotion", "contemplative")

        "Novamente, você dá uma olhada em Astério – parece que o minotauro já se
        decidiu sobre aceitar Kota como funcionário."

        asterion "A missão do Hotel é acolher aqueles que estão perdidos. Levando em
        conta o que você nos disse esta noite, parece que você se encaixa."

        $Asterion.change ("emotion","neutral")

        asterion "Você está disposto e pronto para cumprir a missão do Hotel e
        curvar-se à autoridade do proprietário?"

        pause 2
        $Kota.change("emotion", "laughing")

        kota "Que formal! Não ouço um contrato de serviço expressado desta forma
        em séculos. Faz eu me sentir nostálgico."

        $Kota.change("emotion", "happy")

        kota "Contanto que eu seja livre para seguir minha própria agenda, então sim.
        Durante a minha estadia no Hotel, terei todo o gosto em servir de qualquer maneira possível."

        $Asterion.change ("emotion","bowing")
        $Asterion.change("leftarm", "raised")
        $Kota.change("emotion", "neutral")

        asterion "...Bem, senhor [player_name], com o seu comando,
        posso providenciar tudo. O que você diz?"

        $Asterion.change ("emotion","neutral")
        $Asterion.change("leftarm", "loose")

        asterion "Visto que o senhor Kota já fez nosso... \"juramento\",
        tudo o que você precisa dizer é \"Senhor Kota, por meio deste você é aceito
        como funcionário do Hotel para cumprir sua missão e servir como gerente do salão.\""

        pause 2

        you "...Chique, hein?"
        you "Muito bem. Kota, por meio deste você é aceito como funcionário do Hotel
        para cumprir sua missão e servir como gerente do salão."

        "Você oferece seu aperto de mão."

        show Kota:
            ease 0.5 zoom 1.03 yalign 1.4
        pause 0.5
        $Kota.change("emotion", "happy")
        show Kota:
            ease 0.5 zoom 1.0 yalign 1.0
            pause 1
            ease 0.7 yalign 3.0
            ease 1.0 yalign 1.0

        "Kota segura sua mão com as duas dele e, mais uma vez,
        o concede uma profunda reverência. Seu sorriso é plácido, mas seus olhos estão
        brilhando com uma luz de seriedade que você não tinha notado quando conheceu o dragão."

        show Kota:
            zoom 1.0 yalign 1.0

        play sound "sfx/hum.ogg"
        show backtitle
        with Dissolve(0.25)
        hide backtitle
        with Dissolve(0.25)

        "As luzes do hotel piscam por um segundo logo depois que vocês
        soltam as mãos um do outro."

        $Kota.change ("emotion","surprise")

        kota "O que foi isto?"

        $Asterion.change ("emotion","bowing")
        $Asterion.change("leftarm", "raised")

        asterion "Não se preocupe, Sr. Kota. É apenas mais uma peculiaridade do Hotel."
        $Asterion.change ("emotion","neutral")
        $Asterion.change("leftarm", "loose")

        asterion "Já que foi aceito como membro da equipe responsável pelo salão,
        você tem a plena autoridade de moldá-lo como quiser."
        $Asterion.change ("emotion","contemplative")
        $Asterion.change ("rightarm","hips")
        asterion "Tenho boas lembranças do estilo atual deste salão,
        mas o labirinto sempre mudou de aparência ao longo dos anos.
        Talvez seja hora de atualizá-lo."
        you "Bem, poderia parecer mais moderno."

        $Kota.change("emotion", "puzzled")
        kota "Na verdade, posso aproveitar este estilo.
        É uma coisa bela, mesmo como está agora."
        "Ele passa suas garras sobre o balcão.
        Novamente, a melodia suavemente cantarolada ressoa em sua garganta."
        kota "Antigo e novo... algo que apela a uma sensibilidade tradicional e que,
        mesmo assim, é acolhedor para todos os tipos."
        asterion "Sr. Kota?"
        $Kota.change("emotion", "happy")
        kota "Ah, perdoe-me. Estava perdido em recordações novamente. Eu estava...
        pensando sobre o bar no qual costumava trabalhar."
        kota "...Eu ultrapassaria os limites se desse ao salão um toque pessoal?"
        $Asterion.change ("emotion","bowing")
        asterion "Por favor, sinta-se livre."
        kota "Sendo assim, acho que tenho algumas ideias que você pode gostar."
        scene bg black
        with Dissolve(2)
        "Uma por uma, as luzes piscam conforme você aprova os pedidos de Kota.
        Ele olha para você para avaliar sua reação a cada mudança, bem como Astério."
        kota "Vamos adicionar um pouco mais de luz, sim?"
        pause 1
        kota "Ah, mas mantenha a madeira escura. Na verdade, se importam se a deixarmos um pouco mais escura?"
        pause 1
        kota "Hm... um pouco mais de assentos seria bom. Aqui, e aqui.
        Ah, esta área ao redor da lareira seria perfeita!"
        asterion "Por favor, Sr. Kota, meu único pedido é que você não altere demais esta área."
        kota "Certo. Que tal aqui, então?"
        pause 1
        "Kota continua a adicionar seu próprio toque pessoal ao salão.
        Lâmpadas em forma de balões de papel japonês penduradas sobre o balcão do bar.
        Arte tradicional japonesa nas paredes. Guardanapos dobrados de forma complicada em cada mesa."

        scene bg barkota
        with Dissolve(2)

        $Asterion.change("emotion", "contemplative")
        $Kota.change("emotion", "puzzled")
        show Asterion:
            xalign 0.1 yalign 1.0
        show Kota:
            xalign 0.9 yalign 1.0
            pause 2
            xzoom -1
            pause 3
            xzoom 1
        with Dissolve(1)

        "Quando vocês terminam, o antigo salão transformou-se em um restaurante
        bem iluminado que atinge um equilíbrio delicado entre o tradicional e o moderno."
        "Kota continua a examinar cada detalhe; parece que ele não ficará satisfeito até
        que tudo esteja exatamente perfeito. Astério olha em volta,
        uma expressão pensativa no rosto do minotauro."
        asterion "Está..."
        you "Incrível..."
        you "Bom trabalho, Sr. Kota."
        $Asterion.change("emotion", "smiling")
        $Kota.change("emotion", "happy")

        show Kota:
            xzoom -1
        kota "Ah, por favor. Suponho que se vou ficar aqui por um tempo,
        então apenas \"Kota\" está ótimo."
        if player_background == "speedrunner":
            you "Nesse caso, só [player_name] e Astério está ótimo para nós.
            Talvez [player_name]-san e Astério-san, como eu disse antes."

            "Novamente, o sorriso do dragão fica constrangido."

            kota "Muito bem."
        else:
            you "Sendo assim, apenas [player_name] e Astério está ótimo para nós."
            $Kota.change ("emotion","laughing")
            kota "Combinado!"

        kota "Pois bem, acho que este lugar já está parecendo muito melhor. Caloroso, acolhedor..."
        $Kota.change("emotion", "happy")
        kota "Se não se importa que eu diga, já parece um lugar que eu poderia chamar de lar.
        Pelo menos por enquanto."
        if global_affection >=3:
            $Asterion.change ("emotion","tired")
            asterion "...Um lar..."
            $Asterion.change ("emotion","contemplative")
            asterion "...Soa bem para mim."
        $Asterion.change ("emotion","smiling")

        asterion "Que tal tomarmos uma bebida para comemorar? Podemos contar mais sobre
        como as coisas funcionam por aqui e como funcionarão assim que começarmos a receber mais hóspedes."
        hide Kota
        with Dissolve(1)
        pause 1
        "Kota vai até o balcão, pega uma caneca de cerveja e a retorna para você."
        $Kota.change("emotion", "happy")
        $Kota.change("leftarm", "mug")
        show Kota:
            xalign 0.9 yalign 1.0 xzoom -1
        with Dissolve(1)
        kota "Tudo bem. Vou preparar alguma coisa, certo?
        Estou ansioso para trabalhar com vocês dois, Astério, [player_name]."
        $Kota.change ("emotion","laughing")
        kota "Um brinde!"


    else:
        $Luke.change("clothes", "tankpants")
        $Luke.change("bandanna", "False")
        $Luke.change("glasses", "False")
        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")
        "Há um ritmo aderido aos pés conforme eles alternam entre longos passos
        arrastando botas pelo chão e pisando rapidamente."
        play music "music/AberdeenDoneIt.ogg" fadeout 0.5
        "É seguido por uma voz cantarolando, assobios e garras batendo contra metal.
        É como jazz, com batidas sólidas e uma improvisação divertida."

        show Asterion:
            xalign 0.5 yalign 1.0
            ease 1.0 xalign 0.1
        pause 0.5
        show Luke:
            xalign 0.9 yalign 1.0
        with Dissolve(1)

        "Quando o primeiro hóspede chega ao salão, seus olhos já estão
        vagando para cima e para baixo, captando a grandeza e persistente decadência
        do lugar."

        "Ele não nota você e Astério no bar; seus olhos vagam pelos sofás
        de couro, a lareira, as mesas e cadeiras, até que finalmente
        fixam no minotauro."

        $Luke.change("arm", "pointing")
        luke "Olha só se não é o Angus! Eu tava procurando por você agora mesmo, e..."

        $Luke.change("emotion", "cocky")

        "Os olhos do grifo se voltam para você. Apesar de seu sorriso
        amigável, ele o come com os olhos."

        luke "E você deve ser o dono, hein?"

        if player_background == "speedrunner":
            "Você tenta responder, mas o olhar penetrante da águia o paralisa.
            Tudo o que você consegue dizer é uma sequência de grunhidos e gemidos incompreensíveis
            seguidos de seu nome."

            $Luke.change("emotion", "annoyed")
            $Luke.change("arm", "hip")

            "A expressão do grifo muda para uma repulsa
            impossível de se expressar em palavras."

            luke "Meu Deus, você parece o mestre dos weebs. Que tipo de mãe trouxe
            você pra esse mundo e deixou você viver? Tenho certeza que isso
            é alguma espécie de crime."

            $Luke.change("arm", "pointing")
            luke "Você herdou essa joça? Não consigo imaginar alguém igual você
            juntando dinheiro pra conseguir um lugar desses."

        elif player_background == "leader":
            you "Isso mesmo, estou no comando deste lugar.
            Meu nome é [player_name]."

            "Os dois trocam um firme aperto de mão; o aperto do grifo
            é esmagador, mesmo que não haja uma única gota de malícia em
            seus olhos. Você devolve a ele na mesma moeda."

            you "E você deve ser o senhor Lucas Walker. Fico feliz em recebê-lo
            aqui conosco, e espero que sua estadia seja agradável."

            $Luke.change("emotion", "horny")
            $Luke.change("arm", "hip")
            luke "Ah, nem se preocupe com isso. Com dois belos homens iguais a
            você e o menino Angus ali, tenho certeza que vai."

        else:
            you "Sim, eu sou o dono. Meu nome é [player_name]."

            "Luke agarra sua mão em um aperto esmagador. Você mal
            tem tempo para reagir conforme ele maltrata você enquanto ri."

            luke "Não é assim que um homem aperta uma mão! Bora, coloca força nisso aí!"

            "Você tenta seu melhor para esmagar a mão do grifo, mas ele nem demonstra
            reação. Na verdade, ele começa a esfregar o dedo indicador contra a
            palma de sua mão."
            $Luke.change("emotion", "wink")
            luke "Agora sim. Continua treinando essa
            pegada e um dia você chega lá."

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")

        "E então ele vira os olhos para Astério."

        luke "E {i}você{/i}... por mais que eu goste de te chamar de Angus,
        minha mãe me ensinou coisa melhor. Então, diz aí, quem é você?"

        asterion "Você pode me chamar de Astério. Eu trabalho aqui."

        luke "É mesmo é? E o que tem mais pra saber sobre você?"

        $Asterion.change ("emotion","tired")

        asterion "Perdão?"

        luke "Qual a sua história? O que você faz aqui? Como você
        conseguiu esse crânio pela metade? E, o mais importante,
        você é solteiro?"

        $Asterion.change ("emotion","sad")

        asterion "..."

        menu:

            "Ficar em silêncio.":

                asterion "Eu fui ferido, mas estou melhorando. Faço a maior parte
                do trabalho sob as ordens do senhor [player_name]."

                $Asterion.change ("emotion","angry")

                asterion "Eu não namoro."

                $Luke.change("emotion", "wink")

                luke "É mesmo, é? É uma pena, porque se tem uma coisa que eu sei é que não tem carne
                melhor que o Angus americano. O que eu não faria
                pra dar uma provada..."

                $Asterion.change ("rightarm", "hips")

                asterion "Eu não sou americano, sou mediterrâneo."

                luke "Hah! Como se isso fosse me impedir.

                Mas eu saquei a dica, não se preocupe. Vou parar."

                $Asterion.change ("rightarm", "loose")

            "\"Astério é o segundo no comando.\"":
                $Asterion.change("emotion", "contemplative")
                you "Astério é o segundo no comando da administração do Hotel
                e ele faz a maior parte do trabalho aqui. É tudo o que você precisa saber."
                $Luke.change("emotion", "wink")
                luke "Ah, bom saber. Então é melhor eu me comportar perto de vocês, hein?"

            "\"Isso não é da sua conta, vá se foder.\"":
                you "Isso não é da sua conta, vá se foder.
                Ele não tem que responder suas perguntas."

                $Luke.change("emotion", "cocky")
                $Luke.change("arm", "pointing")

                luke "Hah! É assim que eu gosto.
                Boa atitude essa sua."

                luke "Você vai ter que perdoar o meu jeitinho de ser, eu tô sempre metendo
                o pé no bico. Se eu passar dos limites, é só dar um toque;
                não tenho nenhum problema com isso."

        $Asterion.change ("emotion","neutral")
        $Luke.change("arm", "hip")
        $Luke.change("emotion", "neutral")

        luke "De qualquer forma, vocês tem um lugar e tanto aqui.
        É uma pena que ainda tenha tantos danos.
        Mas eu notei que cês tão reparando, isso é bom."

        luke "Mas é melhor vocês arrumarem uns funcionários. Um hotel
        não se mantém funcionando sem uma mãozinha, sabe?"

        you "Pode supreender você, mas eu e Astério conseguimos dar conta de muita coisa.
        Ainda assim, é, nós estamos procurando pessoas dispostas a fazer parte da nossa equipe."

        you "Astério, você pode contar ao senhor Walker como
        as coisas funcionavam antigamente?"

        $Luke.change("arm", "pointing")
        $Luke.change("emotion", "cocky")

        luke "Só \"Luke\" tá bom, aliás.
        Não precisa ser formal. Mas é, continue."

        $Luke.change("arm", "hip")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "raised")
        asterion "Sim... Antes que surgissem problemas com o gerente anterior,
        era bastante comum os hóspedes escolherem permanecer aqui indefinidamente."
        $Asterion.change ("rightarm", "hips")
        asterion "A maioria não tinha nenhum outro lugar para onde ir, entende.
        E nós podemos pagar razoavelmente bem. Ou devemos em breve,
        visto que o hotel não visa gerar lucros."

        $Asterion.change ("emotion","neutral")

        asterion "E os hóspedes que se juntam à nossa equipe podem usufruir
        das facilidades do Hotel pelo tempo que desejarem, gratuitamente."
        $Asterion.change ("leftarm", "loose")
        $Luke.change("emotion", "horny")
        luke "É mesmo?"

        luke "É, isso pode ser divertido.
        Você acha que a sua clientela tem muitos homens solteiros?"

        $Asterion.change ("emotion","tired")
        asterion "...Sim?"

        $Luke.change("emotion", "cocky")
        luke "Exatamente o que eu gosto de ouvir!
        Acha que tem um lugar pra mim, então?"

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "salute")
        luke "Olha, eu sei que não tenho toda a educação do pessoal da cidade e tudo mais.
        Eu fui criado em uma fazenda, me alistei assim que pude, eu sou deselegante."
        $Asterion.change ("emotion","neutral")
        $Luke.change("arm", "hip")
        luke "Mas eu trabalho duro, sabe? E eu posso entreter as pessoas,
        sei como fazer os hóspedes se sentirem bem. E sou muito bom em
        preparar algumas bebidas fortes."

        luke "Então! Vocês tem um bar aqui, já tem um barman?"
        $Luke.change("emotion", "cocky")
        luke "Confiem em mim e eu vou dar um pouco de ALMA pra esse lugar! O melhor lugar pra
        comer e beber nesse deserto inteiro."

        "Você olha para Astério. Quaisquer comentários rudes que o grifo possa
        ter feito antes parecem ser águas passadas para o minotauro."

        you "Deixa eu ver se entendi. Você quer uma posição aqui.
        Então, por quanto tempo você disse que pretendia ficar aqui mesmo?"
        $Luke.change("emotion", "annoyed")
        luke "Por quanto tempo?... Hein. Eu-eu não sei.
        Mas vai demorar um pouco, com certeza."

        "Você não diz nada e permite que o grifo sinta o peso de suas palavras."

        luke "Eu não tenho obrigações agora. Tô precisando de
        umas férias bem longas, ok? Então sim, conseguir um emprego aqui me ajudaria
        a manter minha mente ocupada."

        luke "A vida tem sido difícil e eu tenho que pensar sobre as coisas.
        É por isso que tô dando uma parada, por recomendação de um amigo."

        $Luke.change("emotion", "neutral")
        luke "Olha, eu quero fazer o meu melhor pra dar aos hóspedes de vocês uma experiência legal.
        Confiem em mim, eles nunca vão esquecer desse lugar se eu tiver alguma coisa pra dizer sobre ele."

        $Asterion.change ("emotion","smiling")
        "Novamente, você dá uma olhada em Astério — ele parece estar aberto à ideia."

        $Asterion.change ("emotion","contemplative")
        asterion "A missão do Hotel é acolher aqueles que estão perdidos.
        Você não parece se importar muito com formalidades, mas, à sua própria maneira,
        posso vê-lo contribuindo para esse propósito."

        $Asterion.change ("emotion","neutral")
        asterion "Você está disposto e pronto para cumprir a missão do Hotel e
        curvar-se à autoridade do proprietário?"

        pause 2
        $Luke.change("emotion", "annoyed")
        luke "Olha, amigo, eu só quero fazer as pessoas se sentirem bem e me manter ocupado.
        Então, claro — eu sigo minha intuição, e ela me diz que isso aqui vai ser uma etapa e tanto da minha vida."
        $Luke.change("emotion", "wink")
        $Luke.change("arm", "salute")
        luke "Conta comigo."
        $Luke.change("arm", "hip")

        $Asterion.change ("emotion","bowing")

        asterion "...Bem, senhor [player_name], ao seu comando,
        posso providenciar tudo. O que me diz?"

        $Asterion.change ("emotion","neutral")

        asterion "Visto que o senhor Walker já... \"jurou\" nossos termos, tudo o que você
        precisa dizer é \"Lucas Walker, por meio deste você é aceito neste Hotel como
        funcionário para cumprir sua missão e servir como gerente do salão.\""

        you "...Chique, hein?"

        you "Muito bem. senhor Walker, por meio deste você é aceito como funcionário
        do Hotel para cumprir sua missão e trabalhar como gerente do salão."

        "Você oferece seu aperto de mão."

        $Luke.change("arm", "pointing")
        show Luke:
            ease 0.5 zoom 1.05 yalign 1.05
        pause 1
        $Luke.change("arm", "hip")
        show Luke:
            ease 0.5 zoom 1.0 yalign 1.0
        "Luke sacode sua mão firmemente com um grande sorriso e uma seriedade em seus
        olhos que trai sua atitude anterior."
        show Luke:
            zoom 1.0 yalign 1.0

        play sound "sfx/hum.ogg"
        show backtitle
        with Dissolve(0.25)
        hide backtitle
        with Dissolve(0.25)

        "As luzes do hotel piscam por um segundo logo depois
        que vocês dois soltam as mãos."

        $Luke.change ("emotion","surprise")

        luke "Negócio sinistro. Eu só queria trabalhar em um bar e acabei de vender a
        minha alma pro diabo. O que minha mãe ia pensar se soubesse?"
        pause 1

        $Luke.change ("emotion","cocky")
        $Luke.change ("arm","pointing")

        luke "É, fazer o que, eu já tava indo pro inferno mesmo.
        Então, chefe, eu tô livre pra cuidar do lugar, né?"

        $Luke.change ("emotion","horny")
        luke "Agora, vamos ver..."

        "Luke olha ao redor do salão, seus olhos fixando em certos pontos. Ele
        esfrega o bico em ponderamento e ocasionalmente aponta para coisas, indo e
        voltando pelo cômodo."

        "Ele então descansa contra o balcão, tamborilando os dedos nos assentos de madeira.
        Depois de um momento, volta a atenção para você e Astério."

        $Luke.change ("emotion","cocky")
        $Luke.change ("arm","pointing")
        luke "Digam aí... não me interpretem mal, rapazes, mas esse salão, por mais chique que seja,
        parece muito antigo, não é? Eu acho que uma reforma não faria mal."

        "Astério olha para você."

        $Asterion.change ("emotion","contemplative")
        $Asterion.change ("rightarm","hips")
        asterion "Tenho boas lembranças do estilo atual deste salão,
        mas o labirinto sempre mudou de aparência ao longo dos
        anos. Talvez seja hora de dar uma atualização."

        you "Bem, poderia parecer mais moderno."

        $Luke.change ("emotion","hornier")
        "Luke mal pode conter a empolgação."

        $Luke.change ("emotion","cocky")
        luke "Beleza, chefe, vamos começar com esses banquinhos.
        A gente podia fazer eles ficarem mais confortáveis, sabe?
        Os viajantes vão chegar muito cansados, não é?"
        $Luke.change ("arm","hip")
        you "Sim, acho válido."

        show backtitle
        with Dissolve(0.25)
        hide backtitle
        with Dissolve(0.25)

        "As luzes do hotel piscam. Os bancos de madeira foram substituídos por
        assentos mais confortáveis de couro com estrutura de metal."

        $Luke.change ("emotion","surprise")
        luke "...É, realmente. Eu vendi mesmo minha alma pro diabo."

        pause 1
        $Luke.change ("emotion","neutral")
        $Luke.change ("arm","pointing")
        luke "Hm... é pedir demais transformar a cor desse couro marrom em vermelho?
        Acho que vai combinar com o salão."

        show backtitle
        with Dissolve(0.25)
        hide backtitle
        with Dissolve(0.25)

        "Todas as luzes piscam novamente. Os assentos de couro dos bancos agora estão vermelhos."
        $Luke.change ("emotion","cocky")
        luke "Beleza, agora vamos fazer alguma coisa com essas luzes."

        scene bg black
        with Dissolve(2)

        "Uma por uma, as luzes piscam conforme você aprova os pedidos de Luke.
        Ele começa com as lâmpadas, diminuindo o brilho do lustre a princípio, antes de
        livrar-se dele por completo."

        luke "Sim, adicione mais luzes vermelhas no balcão."

        luke "Não! Faz elas ficarem rosa. As luzes vermelhas vão ficar ali, por cima das mesas."

        luke "Espera um minuto, falando no balcão, faz ele ficar mais curvo.
        Sim, assim mesmo. Eu tô amando isso, mais curvas atrás do balcão."

        "Luke continua adicionando mais toques ao salão, essencialmente transformando-o
        em uma boate. E então seus pedidos seguem um caminho para o pior."

        luke "Tá, quero que isso tenha acesso à cozinha pra que a gente possa servir
        comida enquanto os hóspedes relaxam. Hambúrgueres que nem os do pai e da mãe."

        luke "Ah!—- E a gente pode ter uma barra aqui? Não posso esquecer das barras de metal e do palco."

        asterion "...Barras? Um palco consigo entender, mas para que servem as barras?"

        luke "Pras minhas performances, é claro! Confie em mim, Angus, vou dar os melhores shows que
        esse lugar já viu."

        you "Eu não acho que uma barra vai ser necessária, Luke."

        luke "Tudo bem, o que quiser, chefe. Mas vamos manter o palco, né?"

        "Você continua atendendo aos pedidos do grifo até que, eventualmente, ele fica satisfeito."

        scene bg barluke
        with Dissolve(2)

        $Asterion.change("emotion", "surprise")
        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "hip")
        show Asterion:
            xalign 0.1 yalign 1.0
        show Luke:
            xalign 0.9 yalign 1.0
        with Dissolve(1)

        "Quando vocês terminam, o antigo salão transformou-se em um clube
        sofisticado, com acesso rápido a fast food e bebidas."

        "O rosto de Luke está radiante. Este lugar é um sonho que se tornou realidade para ele.\n
        Astério pode apenas olhar com horror."

        luke "Bem, amigos, se eu realmente vendi minha alma, pelo menos {i}minha{/i} porção do inferno
        vai ser a melhor de todas."

        if global_affection >=3:
            $Asterion.change ("emotion","sad")
            asterion "...Este lugar costumava ser uma espécie de inferno."
            $Asterion.change ("emotion","contemplative")
            asterion "Mas isto está no passado."

        $Asterion.change ("emotion","smiling")

        you "Relaxa, Luke. O Hotel simplesmente funciona assim."

        asterion "Que tal tomarmos uma bebida para comemorar? Podemos explicar para você
        em mais detalhes."

    scene bg black
    with Dissolve(2)

###################################################################
#                      THIRD NIGHT
###################################################################

#Scene between the lounge and second guest.
    play music "music/JatoTheLion.ogg" fadeout 1.0 fadein 1.0

    $chapter = "Capítulo 7"
    call screen ChapterTransition("Capítulo 7", "Um momento de fraqueza")
    pause 0.5
    $save_name=output_save_name("Capítulo 7")

    "Você passa o resto do dia com Astério e [first_guest] no salão,
    admirando a mudança na decoração, compartilhando bebidas e trocando histórias."

    "[first_guest] tinha algumas histórias interessantes para contar sobre sua vida na estrada."


    if player_background == "humanities":
        "Você contou algumas das suas, por sua vez: casos em que esteve envolvido, organizações
        com as quais trabalhou e curiosidades de sua área de estudo."

    if player_background == "tech":
        "Você contou algumas das suas, por sua vez: empresas para as quais trabalhou,
        aquela vez em que você tentou ser autônomo..."

        "É claro, você e [first_guest] precisaram fazer uma pausa para
        explicar computadores para Astério."

    if player_background == "math":
        "Você contou algumas das suas, por sua vez: longas noites de estudo, brilhantes — e terríveis — professores
        que conheceu ao longo do caminho e curiosas aplicações da matemática."

        if first_guest == "Kota":
            "Kota fingiu interesse no início, mas depois começou a mexer com um saca-rolhas
            enquanto esperava por uma mudança no assunto."

        else:
            "Luke não estava terrivelmente interessado e demonstrou sua aversão por matemática
            bocejando na sua cara algumas vezes."

    if player_background == "arts":
        "Você contou algumas das suas, por sua vez: aquele projeto em que trabalhou, o instrumento que tentou aprender,
        aquele pintor renascentista que você gostou (e aquele que odiou)."

    if player_background == "leader":
        "Você contou algumas das suas, por sua vez: um colega de classe pediu sua ajuda para lidar
        com um valentão e você conseguiu que os dois se tornassem bons amigos..."

        "...ou aquela vez que você transformou um amigo magrinho seu em um
        colega de academia. Você o ensinou a usar as cordas e treinou ao lado dele..."

        "Uma noite, vocês dois e o irmão dele — um jogador de rugby — saíram para beber e
        {i}isto{/i} acabou em você dormindo com o referido irmão."

        if first_guest == "Kota":
            "Kota ficou um pouco apreensivo com sua franqueza no início, mas mesmo assim
            intrigado e impressionado com suas histórias."

        else:
            "Luke explodiu em uma gargalhada estridente e estendeu a mão para você bater."
    if player_background == "speedrunner":

        "Você contou algumas das suas, por sua vez: recordes batidos neste ou naquele jogo, a ida à sua primeira convenção,
        aquela vez que um streamer muito grande o seguiu de volta..."

        if first_guest == "Kota":
            "Kota fingiu interesse no início, mas depois começou a mexer com um saca-rolhas enquanto
            esperava por uma mudança no assunto."

        else:
            "Luke não estava terrivelmente interessado e demonstrou sua aversão por jogos eletrônicos
            bocejando na sua cara algumas vezes."

    "Astério ficou quieto durante a maior parte da conversa sobre experiências passadas —
    suas breves respostas deixaram clara a apreensão sobre compartilhar sua história
    com [first_guest]."

    "Ainda assim, o minotauro manteve seu sorriso tímido durante toda a noite. Assim
    que o assunto voltava para algo menos pessoal, ele retornava
    para a conversa."

    "Com a ajuda de algumas taças de vinho, a postura de Astério relaxou
    encostando em sua cadeira, olhos entreabertos, ele estava flutuando em um mar de felicidade."

    "Eventualmente, começou a ficar tarde e você despediu-se de [first_guest].
    Você e Astério, enquanto isso, retornaram para os aposentos do Mestre."

    scene bg oldquarters
    with Dissolve(2)

    $Asterion.change("emotion", "contemplative")
    $Asterion.change("leftarm", "loose")
    $Asterion.change("rightarm", "loose")

    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve(1)

    "Astério tropeça ao redor com você, sonolento, porém feliz. Ele cantarola e balança a
    cabeça para frente e para trás. Seus cascos adicionam um ritmo que ecoa pelos
    corredores."

    "Quando ele olha de volta para você, seu único olho possui um brilho suave."

    you "Dia longo, hein?"

    asterion "Sim, de fato. Faz tanto tempo.
    O tempo cobrou seu preço; tanta coisa mudou. Rostos peculiares, um salão diferente,
    uma época completamente nova, mas..."

    $Asterion.change("emotion", "smiling")

    asterion "Me sinto como costumava me sentir antigamente, cercado de amigos, conversando
    noite adentro."

    asterion "Eu... Eu tenho um propósito outra vez. Não posso agradecer o suficiente."

    you "Não é nada."

    $Asterion.change("emotion", "bowing")
    $Asterion.change("leftarm", "raised")

    asterion "Não, é bastante, na verdade. É uma honra servi-lo, Mestre."

    $Asterion.change("emotion", "contemplative")

    asterion "Já que estamos falando disso... há algo sobre o qual devo informá-lo.
    É seu direito como Mestre saber e meu dever como Zelador informá-lo."

    asterion "Lembra-se daquela história que contei no salão?"

    you "Qual delas? Você contou tantas."

    asterion "Aquela sobre o Mestre Roberto e seu filho, Mestre Bernardo,
    quem eu ajudei a criar."

    asterion "Agora, por onde começo..."

    $Asterion.change("emotion", "neutral")

    asterion "Perguntei a você hoje se gostou de minha aparência, quando experimentei minhas roupas.
    Esta não foi uma pergunta trivial."

    asterion "O Mestre tem o direito de determinar como o Zelador deve parecer.
    Isto, é claro, inclui como eu deveria me apresentar — qual deveria ser meu uniforme."

    $Asterion.change("leftarm", "loose")
    asterion "Mas vai muito além disso."

    asterion "Durante o mandato do Mestre Bernardo, ele considerou que eu deveria ter {i}pelo branco{/i}.
    Antes de chegar aqui, ele era médico, entende, e acreditava que isso transmitiria um ar de limpeza."

    asterion "Enquanto isso, Mestre Roberto sempre quis que eu tivesse {i}pelo preto{/i}.
    Mesmo quando criança."

    asterion "Ele achou que eu parecia respeitável e imponente desta forma e que ele também
    pareceria poderoso ao ser transportado nas minhas costas."

    asterion "Suspeito que, com o tempo, Mestre Roberto insistiu que eu tivesse pelo preto apenas para irritar seu pai.
    Os dois discutiam sobre isso com frequência. Eles até trocavam piadas sobre isso durante o jantar."

    asterion "Mas quando o pai estava em seu leito de morte, ele pediu um momento para conversar
    \"em privado\" com cada um de seus descendentes."

    asterion "Não tão privado, na realidade. Fiquei ao lado da cama para anotar seu testamento —
    para ter certeza de que cada um teria seu legado correspondente."

    asterion "No meio do caminho, pediu para me ver como ele se lembrava de mim. Seu filho aquiesceu.
    E assim eu o servi até o fim."

    $Asterion.change("emotion", "sad")

    asterion "\"Para meu servo inabalável.\" É o que ele escreveu na carta."
    $Asterion.change("emotion", "contemplative")
    asterion "E senhor Roberto... \"Para meu camarada de infância.\""

    $Asterion.change("emotion", "neutral")

    asterion "...Isto, também, é direito do Mestre. Você pode escolher a minha aparência...
    A magia do Labirinto cuidará disso.."

    $Asterion.change("leftarm", "raised")
    asterion "Pelo juramento que fiz, sou obrigado a informar.
    Sou obrigado a instruí-lo, da melhor maneira possível, sobre todas as capacidades do Hotel."

    asterion "Então entenda, eu perguntando ao Mestre o que ele pensa de minhas roupas...
    aquilo não foi trivial. Seu desejo é uma ordem."

    menu:
        "Permanecer quieto.":
            jump thirdnightfur

        "Mas por que é permitido que o Mestre faça isso?":
            $Asterion.change ("emotion","tired")

    asterion "O porquê..."
    $Asterion.change("leftarm", "loose")
    asterion "...Tenho sobrecarregado você terrivelmente, meu senhor, com minhas divagações.
    Eu preferiria não continuar o abarrotando com conhecimentos desagradáveis."

    asterion "Mas, respondendo sua pergunta de uma forma delicada...
    Como pode ver, posso me curar rapidamente. O vinho especial que bebo é usado para acelerar o processo."

    asterion "É terrivelmente difícil me ferir permanentemente."

    $Asterion.change ("emotion","sad")
    asterion "O Labirinto permite ao Mestre controlar minha forma até certo ponto,
    com o objetivo de... fazer com que eu não seja capaz de me curar de certos ferimentos,
    caso o Mestre assim deseje."

    asterion "..."

    menu:
        "Permanecer quieto.":
            jump thirdnightfur

        "Intrometer-se adiante.":
            you "O que você quer dizer com isso, exatamente?"

    $Asterion.change ("emotion","tired")

    asterion "...Sou obrigado a responder sua pergunta, meu senhor.
    Se realmente é de sua vontade saber, então contarei."

    $Asterion.change ("emotion","bowing")

    asterion "Existiram Mestres, antes do Hotel, que preferiam que meus membros fossem removidos.
    Em circunstâncias normais, o Labirinto me curaria e os retornaria."

    asterion "Outros preferiram me manter decapitado e consciente por meses ou anos."

    asterion "Com este poder, o Mestre pode determinar minha forma padrão."

    asterion "...Mas as pessoas desta época são piedosas.
    Mais que os primeiros Mestres atenienses, com certeza. Para eles, me torturar era um ato de adoração."

    asterion "Alguns diriam que a ingenuidade humana degradou o poder dos deuses."

    menu:
        "Permanecer quieto.":
            jump thirdnightfur

        "O que mais eles fizeram com você?":
            $Asterion.change ("emotion","sad")
            "O minotauro se move para frente e para trás em seus cascos.
            Sua expressão assume uma aparência fria, quase vítrea."

    $global_affection -=0.5

    $Asterion.change ("emotion","neutral")
    $Asterion.change("leftarm", "raised")

    asterion "Pelo juramento, sou obrigado."

    asterion "Eu fui morto por decapitação, desta forma, os Mestres e o Labirinto acharam
    apropriado usar isto como o elemento principal de minha sentença."

    asterion "Quando ficou defasado, eles perceberam que era mais angustiante me
    manter decapitado. Mas isto, também, tornou-se insatisfatório."

    asterion "Eu pensava sobre a dor e o desconforto com tanta frequência que...
    parava de fazer sentido. Pense na dor por tempo suficiente e ela para de doer."

    $Asterion.change ("emotion","tired")
    asterion "Então eles continuaram trocando."

    asterion "Amputações, a princípio. Para que pudessem me jogar aos
    monstros do vale e, como eu não tinha pernas,
    não seria capaz de escapar."

    asterion "Depois evisceração, quando aprenderam que remover meus rins e
    fígado causava formas únicas de sofrimento."

    asterion "Cada parte do meu corpo foi removida pelo menos uma dúzia de vezes,
    depois colocada de volta e removida novamente."

    asterion "Alguns Mestres eram preguiçosos. Em vez de inovar em minhas torturas,
    eles me mantinham decapitado ou moído em uma polpa sangrenta por décadas enquanto
    desfrutavam do Labirinto."

    asterion "Tudo isso é possível porque eles podem determinar minha forma."

    asterion "Fui submetido a todos os tipos de tortura conhecidas pelo homem, e mais algumas."

    asterion "Comparado com o que já passei, ter a cor do meu pelo escolhido pelo
    Mestre não é nada."

    asterion "Eu preferiria isso a ser esfolado vivo e largado para me defender
    sozinho no vale a qualquer dia."

    asterion "Agora você sabe."

label thirdnightfur:

    $Asterion.change("emotion", "neutral")
    $Asterion.change("leftarm", "loose")
    $Asterion.change("rightarm", "hips")

    asterion "Suponho que o Mestre enxerga para onde estou indo com isso."

    $Asterion.change ("emotion", "bowing")
    $Asterion.change("leftarm", "raised")

    asterion "Qual é a sua vontade, meu senhor?"
    $asked_color = False
    $myChoices = [ ("Você parece bem com pelo marrom.", "brown"), ("Pelo preto ficaria bem em você.", "black"), ("Pelo branco é bastante impressionante.", "white"), ("Qual {i}você{/i} quer, Astério?", "id4")]
label thirdnightfurmenu:
    $narrator("Escolha uma cor de pelo para Astério.", interact=False)
    $result = renpy.display_menu(myChoices)

    if result == "brown":
        #Brown fur
        $Asterion.change ("emotion", "smiling")
        asterion "É mesmo?"

        asterion "Esta é a cor que o Mestre Jean-Marie escolheu. Ele achou a mais despretensiosa...
        e admitiu para mim que sempre imaginou o minotauro com pelo marrom."
        asterion "Esta tem sido uma ocorrência bastante comum ao longo dos séculos.
        Cada senhor tinha sua própria visão de como eu deveria parecer."
        $Asterion.change ("emotion", "bowing")
        asterion "Ah, me perdoe. Não pretendo aplicar dúvida em seu julgamento, Mestre."
        asterion "Sua vontade é obedecida sem questionamento."

    elif result == "black":
        #Black fur

        asterion "Preto. Sim, meu senhor."

        $Asterion.change ("emotion", "smiling")

        asterion "Me foi dito que pelo preto combina bem com trajes formais.
        Houve um Mestre que insistiu que eu ajudasse no salão como tal."
        asterion "Alguns hóspedes até disseram que eu era um espetáculo impressionante."

    elif result == "white":
        #White fur
        if asked_color:
            $Asterion.change ("emotion", "contemplative")
            pause 1
            asterion "Ah... se o Mestre me permitir uma indagação impertinente,
            você escolheu pelo branco por causa do que eu disse?"
            asterion "Como disse, fico suficientemente feliz em saber que você se importou em perguntar.
            Não precisa restringir sua escolha por minha causa."
            $Asterion.change ("emotion", "bowing")
            asterion "De qualquer forma... Se branco é o que você realmente quer, então obedeço com prazer."
        else:
            $Asterion.change ("emotion", "smiling")
            asterion "Branco? Muito bem."
            $Asterion.change ("emotion", "contemplative")
            asterion "Isto é nostálgico... Ah, me perdoe. Eu estava pensando em voz alta.
            Não é nada com o que o Mestre deva se preocupar."

    else:
        #Asking him

        you "Que cor você prefere ter?"

        $Asterion.change ("emotion", "neutral")
        $global_affection +=0.5
        $asked_color = True

        asterion "Como?"
        $Asterion.change("leftarm", "loose")

        you "Você me ouviu. Que cor você prefere ter? Qual você mais gosta?"
        $Asterion.change ("emotion", "bowing")
        asterion "Eu... O Mestre não precisa se preocupar com o que eu quero.
        Eu sou o servo, minha vontade não deveria afetar seu julgamento."

        you "Mas eu quero aprender mais sobre você. Eu gostaria de saber,
        mesmo que você não ache que importa."

        $Asterion.change ("emotion", "contemplative")

        "O minotauro suspira e morde o lábio. Você acha que o desagradou de alguma forma,
        mas então um sorriso cresce, tímido como uma flor desabrochando."

        asterion "Significa muito para mim que você tenha perguntado. É muito gentil de sua parte."

        asterion "É apenas... Me perdoe, não estou acostumado a ser questionado sobre o que quero."

        if global_affection <3:
            asterion "Devo admitir que sinto falta de ter pelos brancos.
            Costumava ser minha cor original quando eu estava vivo.
            Sabe, sou descendente do touro branco de Poseidon."
            $Asterion.change ("emotion", "smiling")
            asterion "Mas qualquer coisa serve, meu senhor.
            Já estou muito feliz que você se importou o suficiente para perguntar."

        else:
            $Asterion.change ("emotion", "neutral")
            "O minotauro se vira e pega uma garrafa de vinho que você trouxe
            do salão.
            Com uma destreza experiente, ele a abre com um saca-rolhas."

            "Astério vira-se de volta para você, então olha para as taças de vinho na mesa.
            Ele segura a garrafa com as duas mãos,
            como se segurasse uma cruz no peito de alguém."

            "Ele dá um passo em direção às taças, mas faz uma pausa e leva a garrafa aos lábios."

            "Você pode ver seu pomo de Adão balançando enquanto ele afoga as mágoas."

            "Quando ele encontra seu olhar novamente, há uma suavidade em seus olhos que você não tinha visto antes."

            $Asterion.change ("emotion", "tired")
            asterion "Se o Mestre deseja minha honestidade... Eu ficaria aliviado se soubesse que o Mestre
            gosta de mim. A cor do meu pelo é secundária, na melhor das hipóteses, comparada a isto."

            $Asterion.change ("emotion", "neutral")

            asterion "Suponho que tenho dificuldade para colocar em palavras."

            asterion "Os Mestres ordenaram que eu mudasse para me adequar às suas visões.
            O mesmo vale para como devo agir ou abordá-los."

            asterion "E eu obedeci ansiosamente..."

            $Asterion.change ("emotion", "tired")

            asterion "Pois pensei que isto os faria gostar mais de mim.
            E se gostassem de mim, não seria menos provável que me enviassem para o vale?"

            asterion "Usarei ansiosamente qualquer cor que você desejar,
            caso faça com que o Mestre goste mais de mim."
            pause 1
            $Asterion.change ("emotion", "contemplative")

            asterion "...Talvez até me recompense."

            asterion "Não é sempre que me perguntam o que quero.
            Sou um prisioneiro, afinal — por que o carcereiro se preocuparia com o meu conforto?"

            asterion "Que você me ofereça tal consideração,
            é motivo suficiente para me alegrar."
            pause 1

            $Asterion.change ("emotion", "tired")
            asterion "Sendo assim, é certo que lhe darei uma resposta.
            Uma mais clara que tudo o que lhe contei até agora."

            asterion "Quando eu estava vivo, meu pelo era branco."

            asterion "Em meus sonhos, ainda me vejo com aquele mesmo pelo branco.
            No mundo de quando estou acordado eu olho para baixo e, às vezes, não consigo conter
            uma certa surpresa ao descobrir que não é o caso."

            asterion "Depois de todos esses anos trancado, eu até tinha esquecido qual era
            a cor atual do meu pelo."

            $Asterion.change ("emotion", "contemplative")
            asterion "Se o Mestre quer uma resposta, aí está.
            Pelo branco seria nostálgico para mim.
            Ainda assim, eu ficaria feliz independentemente de qualquer coisa. Contanto que você..."

            $Asterion.change ("emotion", "tired")
            pause 2
            asterion "Contanto que você não me machuque."

            $Asterion.change ("emotion", "contemplative")
            asterion "Por favor, não se sinta pressionado a considerar isso em sua decisão.
            Já estou feliz que você se importou o suficiente para perguntar.
            Seja qual for sua escolha, ficarei alegre."

            menu:
                "Permanecer em silêncio.":
                    $ myChoices.remove(("Qual {i}você{/i} quer, Astério?", "id4"))
                    jump thirdnightfurmenu

                "Eu não vou te machucar.":

                    you "Eu não vou te machucar."

                    $Asterion.change ("emotion", "tired")

                    you "Eu entendo porque você está com medo. Eu poderia me ver suspeitando de
                    qualquer outro novo mestre, depois do que aconteceu com você."

                    you "Minhas palavras podem não convencer você agora, mas vou dizer mesmo assim:
                    Eu não vou te machucar."

                    $Asterion.change ("emotion", "tired")

                    "O minotauro segura firmemente sua garrafa de vinho.
                    Ele olha para baixo e morde o lábio. Um peso repentino parece pesar sobre suas costas."

                    asterion "Eu sou apenas metade touro. Estou familiarizado com as artimanhas do coração humano."

                    asterion "Talvez o Mestre tenha pena de mim esta noite.
                    Mas eu sei como os caprichos humanos são frágeis — como eles desaparecem tão rapidamente."

                    asterion "Eu... eu pensei muito e pesadamente ao longo dessas décadas em que estive trancado.
                    Sobre este hotel, minha sentença, meus Mestres anteriores...
                    E um jovem menino que conhecia. Ele tinha mais ou menos a minha idade."

                    $Asterion.change ("emotion", "contemplative")

                    asterion "Seu nome era Ícaro. Seu pai fez asas com cera de abelha
                    e penas para eles dois,
                    mas Ícaro teve a arrogância de voar muito perto do sol."

                    $Asterion.change ("emotion", "sad")

                    asterion "Ele caiu para a morte no mar abaixo...
                    E nós nos conhecemos em Hades, após minha morte."

                    asterion "Eu pensei sobre ele, aquele menino.
                    Cometi o mesmo erro ao me permitir ser feliz?
                    Alegria nunca foi meu destino na vida."

                    "Astério acaricia a mesa como se ela fosse um amante.
                    Suas unhas roçam contra a madeira, estalando alto o suficiente para você ouvir."

                    asterion "Assim como Ícaro, aproveitei um vislumbre de liberdade.
                    Este hotel foi meu par de asas."

                    $Asterion.change ("emotion", "neutral")

                    "Uma brisa gelada sopra para dentro a partir da janela.
                    Ela envia um arrepio através de sua espinha e uma repentina frieza de pedra ao rosto de Astério."

                    asterion "Há promessas que não podem ser cumpridas, meu senhor.
                    O Hotel sabe disso muito bem."

                    asterion "Nem todos os contratos podem ser feitos para surtir efeito.
                    O Labirinto não permitiria um que se opusesse à sua missão declarada."

                    asterion "Houve um Mestre que, no início de seu mandato,
                    tentou aprovar um contrato proibindo todos e qualquer um de me machucar."

                    asterion "Não poderia fazer efeito. A tinta pingou para fora
                    dele, o papel envelheceu e apodreceu como leite."
                    $Asterion.change ("emotion", "tired")

                    asterion "Pior ainda, sua caridade acabou um dia.
                    É fácil oferecer um gesto de piedade, mas fazê-lo durar requer
                    um tipo especial de intensidade."

                    asterion "O poder revela o que está por baixo."
                    $Asterion.change ("emotion", "neutral")
                    asterion "Houve um número de Mestres gentis que azedaram e tornaram-se
                    confortáveis com punições severas."

                    asterion "Mesmo os mais gentis não se acanharam em me punir.
                    Era a missão deles, afinal."

                    if global_affection >=4:
                        stop music fadeout 2.0
                        pause 2
                        asterion "..."

                        you "..."

                        pause 1

                        "Você e Astério se encaram."

                        $Asterion.change ("emotion", "tired")

                        "Eventualmente, ele desvia o olhar, coçando o lado esquerdo do rosto."
                        asterion "Eu... Eu..."

                        pause 2
                        $Asterion.change ("emotion", "sad")
                        pause 2
                        $Asterion.change ("emotion", "bowing")

                        asterion "Por favor, esqueça o que eu disse, meu senhor."
                        if Promise_Valley:
                            play music "music/seikilos.mp3" fadeout 1.0 fadein 1.0

                            $Asterion.change ("emotion", "sad")

                            "Você se aproxima de Astério."

                            "Você levanta a mão e segura o lado esquerdo do rosto dele. Você passa os dedos
                            sobre seus pelos curtos, tomando cuidado para não
                            chegar muito perto do ferimento."

                            $Asterion.change ("emotion", "sad")
                            pause 2.5
                            $Asterion.change ("emotion", "bowing")

                            "Astério hesita, mas, com cada carícia de seus dedos,
                            os olhos dele se fecham ainda mais e ele apoia seu peso contra sua mão."

                            you "Eu prometi que não mandaria você para o vale.
                            E não vou. E eu não vou te machucar."

                            "Astério suporta o peso completamente em sua mão.
                            Sua pálpebra treme, como se ele já estivesse adormecendo."

                            "Você levanta sua outra mão e começa a acariciar o lado direito e
                            mais saudável do rosto de Astério. O minotauro se inclina em sua
                            direção e você se aproxima para equilibrar o peso dele."

                            "Você deixa o minotauro tirar sua soneca, até que sua orelha sacode.
                            Você a esfrega suavemente e os olhos dele se abrem."

                            $Asterion.change ("emotion", "sad")
                            pause 2

                            asterion "Eu... Mestre [player_name]."
                            asterion "Eu sinto muito, eu não sei o que deu em mim. Eu-Deve
                            ser a sonolência. Não vai acontecer de novo."

                            "Ele permanece com a cabeça em suas mãos."

                            you "Tudo bem. Como você está se sentindo agora?"
                            pause 1
                            asterion "...Eu estou bem."

                            you "Ótimo."

                            pause 1

                            "Astério hesita ainda mais antes de se afastar de você,
                            mas ele o faz com um suspiro."

                            asterion "Mais uma vez, eu sinto muito."

                            you "Você não fez nada de errado, não tem porquê dizer isso."
                            pause 2
                            $Asterion.change ("emotion", "bowing")
                            asterion "Como quiser, meu senhor."

                            #"When you're done, Asterion is smiling from ear to ear."

                            #asterion "T-thank you, Master [player_name]."
                        play music "music/JatoTheLion.ogg" fadeout 1.0 fadein 1.0
                        you "Está tudo bem, Astério."

                    you "Serei diferente. Não se preocupe."
                    $Asterion.change ("emotion", "bowing")

        $ myChoices.remove(("Qual {i}você{/i} quer, Astério?", "id4"))
        jump thirdnightfurmenu

    if result != "brown":
        "Astério fecha os olhos e se concentra. Diante de seus olhos, seu pelo começa a mudar."
        hide Asterion
        with Dissolve(1)
        $Asterion.change("fur", result)
        show Asterion
        with Dissolve(1)
        "A cor do pelo de Astério é agora um brilhante [result], de acordo com sua solicitação."

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("leftarm", "raised")
    $Asterion.change ("rightarm", "loose")

    asterion "Estou honrado com sua escolha, Mestre."

    hide Asterion
    with Dissolve(1)

    if result == "brown":
        "Astério vai para a cozinha preparar seu jantar."
    else:
        "Astério vai para a cozinha preparar seu jantar.
        Volta e meia, você o percebe olhando para os braços enquanto cozinha."
        "Talvez ele esteja se acostumando à nova cor de pelo."

    "Depois de um tempo, Astério retorna à mesa, serve seu jantar e
    senta na extremidade oposta, como de costume."

    if asked_color or global_affection >=4:
        "Quando olha para cima, você é saudado pelo grande sorriso estúpido de Astério.
        Ele tenta se conter, mas acaba tendo que impedir a própria
        risadinha."

        "Às vezes, ele quase cochila, ainda com um sorriso estampado no rosto."

    else:
        "Astério espera pacientemente você terminar. Ele olha para a janela atrás de você,
        observando a lua e as estrelas brilhando sobre a estrada do deserto."

    "Você termina sua refeição. Astério vai pegar seu prato, como sempre.
    Desta vez, você deixou um grande pedaço para ele no prato, Astério sorri enquanto se
    dirige para a cozinha."

    "Vocês desejam boa noite um para o outro e depois vão para seus respectivos
    quartos para passar a noite."

    scene bg black
    with Dissolve(2)

    play music "music/IslandJourney.ogg" fadeout 1.0 fadein 1.0

    "Na manhã seguinte, como de costume, o som dos cascos de Astério
    batendo no chão e o cheiro de café da manhã o acordam."

    scene bg oldquarters
    with Dissolve(2)

    "Você acorda, se veste e sai do quarto."

    show Asterion
    with Dissolve(1)

    "Astério, mais uma vez, o cumprimenta."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("leftarm", "loose")
    $Asterion.change ("rightarm", "hips")

    asterion "Bom dia, Mestre. Espero que tenha dormido bem."

    "Após a rotina do café da manhã, — desta vez, Astério serviu ovos mexidos,
    presunto e suco de laranja espremido na hora — ele lava os pratos e
    retorna para você."

    asterion "Quais são seus planos para hoje, Mestre?"

    you "Bem, ainda é muito cedo. Acho que vou ficar por aqui e mexer um pouco
    no meu celular, ver se consigo fazer ele funcionar. E você?"

    $Asterion.change ("emotion", "contemplative")

    asterion "Eu acho... Acho que vou descer para a recepção, ver se somos sortudos o suficiente para receber quaisquer novos hóspedes."

    you "Tão cedo? Bem, acho que [first_guest] chegou aqui logo depois que acendemos a lareira.
    Então é possível."

    pause 1

    if chapter6LieAboutUndies != 0:
        $Asterion.change ("emotion", "neutral")
        asterion "Hm... Mestre, antes de ir... Posso lhe fazer uma pergunta?"
        $Asterion.change ("emotion", "sad")
        asterion "Bem, hm... Como posso dizer..."
        $Asterion.change ("rightarm", "loose")
        if first_guest == "Luke":
            $Asterion.change ("emotion", "tired")
            asterion "Ontem, quando conheci Luke, ele fez alguns...
            comentários sobre o que eu estava vestindo."
            $Asterion.change ("emotion", "sad")
            asterion "Mestre [player_name]? Tangas são realmente apropriadas para usar, como você disse?
            Ou foi apenas... Luke sendo Luke?"
        else:
            $Asterion.change ("emotion", "tired")
            asterion "Ontem, quando conheci Kota, ele...
            Bem, ele olhou para mim de uma forma muito desconfortável."
            $Asterion.change ("emotion", "sad")
            asterion "Não tenho certeza se foi meu olho, ou eu sendo um monstro...
            Mas tenho estado com uma pulga atrás da orelha."
            asterion "Foi... foi minha roupa, Mestre [player_name]?
            As tangas realmente voltaram a ser apropriadas para vestir?"
        menu:
            "Me desculpe por mentir para você":
                you "Eu— você está certo. Sinto muito, Astério. Eu menti para você."
                pause 1
                $Asterion.change ("emotion", "bowing")
                asterion "Tenho certeza que tem seus motivos, Mestre.
                Aprecio sua honestidade agora."
            "Não se preocupe com isso":
                if first_guest == "Luke":
                    you "Aquilo foi só o Luke sendo Luke. Não se preocupe com isso."
                else:
                    you "Bem, talvez ele só estivesse chocado. Você não vê um minotauro todo dia.
                    Não se preocupe com isso."
                $Asterion.change ("emotion", "contemplative")
                asterion "Sim... deve ter sido isto. Obrigado por sua garantia, Mestre."
                $chapter6LieAboutUndies = 3

        $Asterion.change ("emotion", "smiling")
        asterion "De volta ao que importa.
        O que devo vestir hoje, Mestre? Meu pelo está com a cor correta?"
    else:
        $Asterion.change ("emotion", "smiling")
        asterion "Ah, antes de ir... o que eu deveria vestir hoje, Mestre?
        Meu pelo está com a cor correta?"

    $wardrobe.add("fur", "brown")
    $wardrobe.add("fur", "black")
    $wardrobe.add("fur", "white")

    call screen dayManager("wardrobe")

    if Asterion.clothes =="nude" and Asterion.underwear =="none":
        if not chapter6nude:
            pause 1
            $Asterion.change ("emotion","bowing")
            asterion "Receio não poder cumprir este comando."
            you "Como assim?"
            pause 1
            scene bg black
            with Dissolve(0.2)
            $Asterion.change ("underwear","loincloth")
            scene bg oldquarters
            show Asterion
            with Dissolve(0.2)
            pause 1
            $Asterion.change ("emotion","neutral")
            "As luzes do hotel piscam. Astério agora está vestido, bem diante de seus olhos."

            asterion "De acordo com os contratos assinados por Mestres anteriores,
            estou proibido de me expor quando estamos esperando por hóspedes."

            asterion "Também não posso estabelecer relacionamento com um hóspede."

            asterion "Estou sob uma variedade de restrições."

            asterion "Lamentavelmente, não posso cumprir seu comando, Mestre."
            if persistent.sfwMode == False:
                you "Mas você estava nu quando te encontrei. Qual é a diferença?"

                asterion "Não estávamos esperando hóspedes naquele momento."

        else:
            pause 1
            scene bg black
            with Dissolve(0.2)
            $Asterion.change ("underwear","loincloth")
            scene bg oldquarters
            show Asterion
            with Dissolve(0.2)
            pause 1
            $Asterion.change ("emotion","sad")
            asterion "...Mestre [player_name]..."
            $Asterion.change ("emotion","bowing")
            asterion "Por favor, eu ficaria grato se você parasse de fazer isto."
        $ global_affection -= 1
        $ abuse_act1 += 1

        "Astério tenta não se importar com isso, mas está claramente
        ofendido com sua escolha de vestimenta para ele."
    elif not chapter6nude:

        pause 1
        $Asterion.change ("emotion","contemplative")
        pause 1
        asterion "..."
        pause 1

        you "Qual é o problema, Astério?"

        $Asterion.change ("emotion","surprise")

        pause 1

        $Asterion.change ("emotion","smiling")

        asterion "Bem, estou debatendo se devo ou não contar isso para você... mas..."

        $Asterion.change ("emotion","bowing")
        $Asterion.change ("leftarm","loose")

        asterion "Suponho que não deva significar muito, mas...
        Eu aprecio que o Mestre tenha sido bom para mim em um sentido."

        you "O que você quer dizer?"

        $Asterion.change ("emotion","sad")

        asterion "Alguns dos mestres mais... impiedosos gostavam de me humilhar.
        De muitas maneiras."

        asterion "Me despindo e me fazendo andar de quatro.
        Isto era comum."

        asterion "Posso ser um híbrido, mas eu {i}sou{/i} meio humano. Não sou uma besta."

        $Asterion.change ("emotion","contemplative")

        asterion "Isso acabou, felizmente."
        asterion "De acordo com os contratos escritos e assinados por mestres anteriores,
        estou proibido de me explor quando estamos esperando hóspedes."

        asterion "Também não posso estabelecer um relacionamento com um hóspede.
        Estou sob uma variedade de restrições."

        $Asterion.change ("emotion","contemplative")

        asterion "Nem todos esses contratos foram escritos por gentileza. Mas eles
        foram benéficos."

        if persistent.sfwMode == False:
            you "Mas você estava nu quando te encontrei. Qual é a diferença?"

            asterion "Não estávamos esperando hóspedes naquele momento."

        $Asterion.change ("emotion","smiling")

        asterion "Fico feliz que você não tenha tentado quebrar essa regra,
        Mestre [player_name]."

        $Asterion.change ("emotion","bowing")

        asterion "Perdoe-me por tocar no assunto, mas achei importante
        que você soubesse."
        $global_affection += 0.5

    else:
        pause 1
        $Asterion.change ("emotion","contemplative")
        asterion "Bem... devo dizer que isto é uma melhoria."
        asterion "Pode não significar muito para você, mas... obrigado por me
        vestir mais... decentemente, Mestre [player_name]."

    pause 2
    asterion "Muito bem então. Devo seguir para a recepção."

    hide Asterion
    with Dissolve(1)

    "Astério sai e lhe dá um sorriso antes de fechar a porta atrás de si."

    "Você se senta no sofá, olhando para a porta e depois para a janela, e pensa em
    como passar sua manhã."

    scene bg black
    with Dissolve(2)

##############################################################################
#                      CHAPTER 8: THE SECOND GUEST
##############################################################################
label chapter7:

    if first_guest == "Kota":
        jump LukeIntro
    else:
        jump KotaIntro

label chapter7_1:

    $chapter = "Capítulo 8"
    call screen ChapterTransition("Capítulo 8", "Resolução de conflitos")
    pause 0.5
    $save_name=output_save_name("Capítulo 8")

    play music "music/IslandJourney.ogg" fadeout 1.0 fadein 1.0
    scene bg oldquarters
    with Dissolve(2)
    "Depois que Astério lhe serviu o café da manhã, você decidiu ficar em seus aposentos neste primeiro período do dia."

    if first_guest == "Luke":
        "Coisas que eram estranhas para você estão começando a se tornar familiares. O hotel que se dobra
        à sua vontade, o minotauro que jurou servi-lo, monstros-serpente traiçoeiros e o grifo
        texano que agora administra um clube de strip-tease sob seu teto."
    else:
        "Coisas que eram estranhas para você estão começando a se tornar familiares. O hotel que se dobra
        à sua vontade, o minotauro que jurou servi-lo, monstros-serpente traiçoeiros e o dragão
        japonês que agora administra um restaurante sofisticado sob seu teto."

    "Você está aos poucos se acostumando às suas novas circunstâncias e a esta nova rotina
    — acordar, tomar café da manhã com Astério, inspecionar os quartos,
    ver as pequenas mudanças nas condições do hotel e na estrutura todos os dias,
    tomar uma bebida e conversar no final do dia..."

    "Mais uma vez, você olha para fora da janela nos aposentos do Mestre."

    scene bg desert
    with Dissolve (1)

    "Considerando que seu celular está praticamente morto a essa altura e organizar seus
    pensamentos fica um pouco enfadonho depois de um tempo, você se pega fazendo isso com frequência
    quando Astério não está no quarto com você."

    "Com a chegada de novos hóspedes, momentos monótonos como este vão se tornar
    menos frequentes. Mas, por enquanto, você pode aproveitar este momento de meditação e
    o calor de seus esforços dando frutos."

    if first_guest == "Luke":
        "Você vê uma figura à distância."
        "Você tenta distinguir os detalhes, mas está muito longe e o brilho produzido
        pelo calor na estrada torna muito difícil de ver qualquer coisa além de um ponto
        azul escuro caminhando pelo deserto."
        "Está... caminhando, na direção do hotel?"
        "De fato, parece que a figura está se aproximando. Talvez seja um hóspede?
        As pessoas parecem encontrar o caminho para o hotel por meios estranhos,
        mas você e Luke chegaram aqui de carro. O cara deve estar exausto."
        "Enquanto você pensa sobre as circunstâncias que levaram um sujeito a vagar por uma estrada
        deserta a pé, a figura se aproxima cada vez mais, até que finalmente se encontra
        em frente à porta do hotel."
    else:
        "Algo chama sua atenção. Alguma coisa na distância."
        "Você aperta e foca os olhos na pequena mancha vermelha que deve estar a vários quilômetros de distância.
        O brilho produzido pelo calor na estrada torna muito difícil distinguir quaisquer detalhes."
        "Uma coisa é certa: está vindo para cá."
        "Talvez seja um hóspede? Você não viu nenhuma atividade nesta estrada desde que
        chegou, além de Kota caminhando por aqui. Pelo menos desta vez parece que
        o sujeito está digirindo um carro."
        "O carro se aproxima do Hotel. Ele desvia para o estacionamento, fazendo um barulho alto e
        estridente que você pode ouvir de seu quarto. Quem quer que seja esse cara, ou é um
        um péssimo motorista, ou um exibicionista ruim, ou dirige sob influência de drogas."
        "Você o observa sair e valsar para a entrada principal."

    scene bg oldquarters
    with Dissolve(1)
    "Quem quer que seja esse cara, ele despertou sua curiosidade."
    "Você se levanta, estica suas pernas e sai pela porta."

    scene bg staircase
    with Dissolve(1.0)
    "Conforme você sai dos aposentos do Mestre, as luzes piscam e você ouve o som familiar das paredes
    do hotel se fechando atrás de você para esconder seu quarto."
    "Você está prestes a descer para o saguão, quando vê algo um andar abaixo de você."
    if first_guest == "Luke":
        "É Luke, prestes a descer as escadas também. Mas algo parece... errado com ele."
        play music "music/VindalooBlues.ogg" fadeout 1.0 fadein 1.0

        $Luke.change("arm","salute")
        $Luke.change("emotion", "neutral")
        $Luke.change("clothes", "speedo")
        $Luke.change("bandanna", "True")
        $Luke.change("dogtag", "True")
        $Luke.change("glasses", "False")
        show Luke:
            xalign 0.5 yalign 1.0
        with Dissolve(2)
        "O traje de Luke deixa pouco para a imaginação.
        Ele estava vestido informalmente ontem, mas isto talvez seja um pouco demais."

        $Luke.change("emotion", "cocky")
        luke "Fala aí, chefinho. Que manhã linda, não é?"
        menu:
            "...":
                "Você decide não comentar sobre a estranha escolha de guarda-roupa de Luke."
                $Luke.change("arm","pointing")
                $Luke.change("emotion","wink")
                luke "Meus olhos tão aqui em cima, campeão. Mas você tá livre pra olhar se quiser."
                luke "Acho que se é pra dirigir o belo estabelecimento lá embaixo,
                eu tenho me vestir de acordo, não é?"

            "O que você está vestindo?":
                you "Luke, o que você está vestindo?"
                $Luke.change("arm","pointing")
                luke "Por que? Tem alguma coisa errada com a minha roupa?"
                you "É bem reveladora."
                $Luke.change("emotion","wink")
                luke "Então? Não é inapropriada considerando onde eu vou, não é?"
        pause 2
        you "Acho que sim."
        $Luke.change("emotion", "neutral")
        luke "Mais uma vez, obrigado por me deixar retribuir.
        Você não precisava fazer isso, e eu agradeço."
        "Luke lhe dá um aperto de mão firme e respeitoso. Ele pode ser rude e grosseiro,
        mas parece genuinamente grato que você o tenha deixado ficar."
        $Luke.change("arm","hip")
        luke "Eu tava indo pro salão. Ou deveria dizer, pro bar.
        Sabe, verificar se tá tudo funcionando. E você?"
        you "Eu estava indo para o saguão."
        $Luke.change("emotion", "cocky")
        luke "Beleza, então, parceiro, mostre o caminho!"
        hide Luke
        with Dissolve(1)
        "Você e Luke descem as escadas, indo na mesma direção."
    else:
        "É Kota. Parece que ele acabou de sair do quarto e está prestes a descer as escadas
        também. No entanto, suas roupas estão diferentes do yukata que ele estava vestindo ontem."
        play music "music/TheSorrow.ogg" fadeout 1.0 fadein 1.0

        $Kota.change("leftarm","relaxed")
        $Kota.change("rightarm","relaxed")
        $Kota.change("emotion", "neutral")
        $Kota.change("hair", "tied")
        $Kota.change("clothes","barman")
        show Kota:
            xalign 0.5 yalign 1.0
        with Dissolve(2)
        "Hoje, Kota está vestindo uma roupa formal, mas definitivamente mais ocidental.
        Ele está vestido como um barman elegante."
        kota "Bom dia, [player_name]. Bom te ver de novo."
        you "Vejo que você está levando essa coisa de restaurante a sério."
        $Kota.change("emotion", "happy")
        $Kota.change("rightarm","raised")
        kota "Você sabe o que dizem: vista-se para o trabalho que você deseja."
        you "Acho que sim."
        $Kota.change("emotion", "laughing")
        $Kota.change("leftarm","raised")
        kota "Mais uma vez, muito obrigado por sua hospitalidade.
        Não quero ser um fardo para ninguém, então assumirei com prazer qualquer tarefa que puder
        como um gesto de boa vontade."
        "Kota se curva em sua direção."
        $Kota.change("emotion", "surprise")
        $Kota.change("leftarm","relaxed")
        $Kota.change("rightarm","relaxed")
        kota "Eu estava a caminho do salão, na verdade. Ou talvez deva dizer o
        restaurante? Para ver se está tudo em ordem caso recebamos novos hóspedes.
        Posso saber para onde você está indo?"
        you "Eu estava indo para o saguão."
        $Kota.change("emotion", "laughing")
        kota "Ah! Ótimo então, podemos ir juntos."
        hide Kota
        with Dissolve(1)
        "Você e Kota descem as escadas, indo na mesma direção."

    scene bg oldlobby
    with Dissolve(2)

    $Asterion.change("emotion", "bowing")
    $Asterion.change ("rightarm","loose")
    $Asterion.change ("leftarm","raised")

    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve(1)
    if first_guest == "Luke":
        show Kota:
            xalign 1.2 yalign 1.0 xzoom -1
        with Dissolve(1)
    else:
        show Luke:
            xalign 1.2 yalign 1.0
        with Dissolve(1)

    asterion "Espero que você tenha uma estadia agradável conosco."
    pause 2
    $Asterion.change("emotion", "neutral")

    if first_guest == "Luke":
        show Luke:
            xalign -0.6 yalign 1.0 xzoom -1
            linear 2.0 xalign -0.2
        with Dissolve(1)
        "Você e Luke seguem todo o caminho até a recepção.
        Parados lá estão Astério e o que parece ser um dragão azul vestido em
        roupas tradicionais japonesas."
    else:
        show Kota:
            xalign -0.6 yalign 1.0
            linear 2.0 xalign -0.2
        with Dissolve(1)
        "Você e Kota seguem todo o caminho até a recepção.
        Parados lá estão Astério e o que parece ser um grifo águia careca
        vestido muito informalmente."

    $Asterion.change("emotion", "surprise")
    $Kota.change("emotion", "surprise")
    $Luke.change("emotion", "surprise")
    pause 3

    if first_guest == "Luke":
        $Kota.change("emotion", "angry")
        $ renpy.force_autosave(True, True)
        "O dragão olha Luke de cima a baixo e parece descontente."
    else:
        $Luke.change("emotion", "hornier")
        $ renpy.force_autosave(True, True)
        "O grifo olha Kota de cima a baixo e está lambendo o bico em antecipação."

    jump build03
