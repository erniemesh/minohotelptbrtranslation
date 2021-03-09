label build03:
    $build=3
    $new_build_update()
    $add_file('Contract', 'Servitude')
    $add_file('Contract', 'AsterionSentence')
    $add_file('Contract', 'ArgosContract')

    $LoungeBlobs =[True, 2]

    default BundleSacrifice = 'none'
    default build3Ending = 'none'
    default TimesSent = 0

    if player_background  == "speedrunner":
        $ArgosContract = "Speedrun"

    if ArgosContract == "Terrorized":
        $TimesSent = 1

    scene bg oldlobby
    stop music fadeout 2.0
    show Asterion:
        xalign 0.5 yalign 1.0
    if first_guest == "Luke":
        show Luke:
            xalign -0.2 yalign 1.0 xzoom -1
        show Kota:
            xalign 1.2 yalign 1.0 xzoom -1

        $Luke.change("emotion", "neutral")
        $Asterion.change("leftarm", "loose")
        "Alguma parte profunda e instintiva de você enxerga a expressão no rosto do novo hóspede,
        percebe o que está prestes a acontecer e grita para que você intervenha."
        $Asterion.change("emotion", "tired")
        $Luke.change("emotion", "horny")
        "Mas, assim como assistir a um acidente de trem em câmera lenta, tudo o que você pode fazer é ficar parado
        enquanto Luke se anima e sorri."

        play music "music/MayItBegin_Acoustic.ogg" fadein 2.0

        $Luke.change("emotion", "cocky")
        luke "Já fisgou outro,{w=0.2} hein? Legal!"
        show Luke:
            xalign -0.2 yalign 1.0
            linear 1.0 xalign 0.0
        $Luke.change("emotion", "horny")
        luke "{i}Muito{/i} legal."

        luke "Parece que vai ter sushi no cardápio hoje."

        "A voz do grifo praticamente goteja com insinuações. A cauda chicoteia atrás dele,
        batendo nos móveis."

        show Luke:
            xalign 0.0 yalign 1.0
            linear 1.0 xalign -0.25
        show Kota:
            xalign 1.2 yalign 1.0
            linear 1.0 xalign 1.25
        $Asterion.change("emotion", "neutral")

        show Kota behind Asterion
        show Luke behind Asterion

        "Astério limpa a garganta com um pigarreio, correndo para ficar entre o dragão e Luke —
        se apenas para chamar atenção para si mesmo com o movimento pesado."

        asterion "Senhor Kota,{w=0.2} devo apresentar o senhor Luke,{w=0.2} o proprietário do salão do Hotel.
        E, é claro, o Mestre e dono de nosso estabelecimento,{w=0.2} Mestre [player_name]."

        "Ele gesticula para você e o \"Senhor Kota\" lhe olha de cima a baixo, apreciando cada característica sua."

        $Kota.change("emotion", "neutral")
        "A expressão do dragão suaviza, sua testa franzida e lábios carrancudos deslizando
        sob um neutro sorriso como seixos desaparecendo sob a superfície de um lago."

        kota "Entendo."

        "Ele se curva— baixo, formal e com desdenho ao grifo quase nu parado
        ao seu lado."

        $Kota.change("leftarm", "raised")
        kota "É uma honra conhecê-lo,{w=0.2} Mestre [player_name].
        Agradeci a Astério,{w=0.2} mas agora também gostaria de agradecer a você por sua hospitalidade."

        you "Ah, sim. Só [player_name] já está bom."

        you "Você é bem-vindo para ficar o tempo que quiser, senhor Kota."

        show Asterion behind Luke
        show Luke:
            xalign -0.25 yalign 1.0
            linear 1.0 xalign -0.1
        $Luke.change("emotion", "laughing")
        $Kota.change("leftarm", "relaxed")
        "Luke, seja por não ser capaz de reconhecer quando está sendo ignorado ou simplesmente
        não acostumado a isto, dá um tapinha em suas costas com uma risada ruidosa."

        $Kota.change("emotion", "angry")
        $Luke.change("arm", "pointing")
        luke "É, esses belos rapazes aqui dirigem um ótimo lugar.
        Aconchegante pra dedéu, mesmo que pareça meio merda agora."

        $Luke.change("arm", "hip")
        luke "Mas é só dar um tempo que a gente vai transformar ele no melhor maldito lugar em todo o...{w=0.2}
        onde quer que a gente esteja."

        $Luke.change("emotion", "wink")
        luke "Só espera até ver o bar!
        Se você quiser eu te levo até lá, já tava indo naquela direção mesmo."

        luke "Posso te arranjar uma bebida, te deixar confortável..."

        $Luke.change("emotion", "horny")

        luke "Se você quiser se instalar agora, tudo bem também.{w}
        Tô ansioso pra ver {i}mais{/i} de você mais tarde..."

        kota "Claro..."

        $Kota.change("emotion", "puzzled")
        show Kota:
            xalign 1.25 yalign 1.0
            linear 1.0 xalign 1.15

        "O dragão vira de volta para você e se contenta em olhar na direção entre você e Astério.
        Você pode ver seus olhos vidrados por um mínimo de tempo enquanto passam por Luke,
        como se recusando a reconhecer a presença do grifo. "

        kota "Por favor, me perdoem, senhor Astério, senhor [player_name].
        Minhas viagens têm sido longas e árduas e eu os agradeço mais uma vez por me
        oferecerem um lugar para ficar. Eu apenas não estava, bem..."

        $Kota.change("emotion", "sad")
        $Kota.change("rightarm", "raised")
        kota "Quando ouvi falar do Hotel de vocês, não esperava que fosse...{w=0.3}
        este tipo de estabelecimento."

        $Asterion.change("emotion", "sad")

        you "Que tipo de —?"
        pause 1.0
        "Ah."
        pause 2.0
        "{i}Ah.{/i}"

        $Asterion.change("emotion", "surprised")

        "Você e Astério olham na direção de Luke e
        percebem como o dragão pode ter ficado com essa impressão."

        if Asterion.clothes =="nude":
            $Asterion.change("emotion", "sad")
            "Não ajuda que Astério também esteja exibindo muito mais do que
            você veria no balcão de um hotel legítimo."

            "Você olha para o minotauro, tentando dar a ele um pedido de desculpas silencioso,
            mas Astério apenas baixa o olhar para o chão enquanto intercala o peso entre os cascos."

        $Luke.change("emotion", "surprise")

        luke "O que? Tem alguma coisa na minha cara?"

        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")

        asterion "Por favor, nos perdoe, senhor Kota. Como eu disse, abrimos recentemente e
        alguns detalhes, como o código de vestimenta da equipe, ainda estão sendo resolvidos."

        $Luke.change("emotion", "annoyed")

        luke "\"Código de vestimenta\"?"

        $Asterion.change("emotion", "tired")
        $Luke.change("emotion", "surprise")

        luke "Ah!"

        $Luke.change("emotion", "laughing")
        $Kota.change("emotion", "angry")

        "Mais uma vez, o grifo explode em roucas gargalhadas;
        ele precisa se apoiar contra você para evitar ser derrubado pelos espamos de seu regozijo."

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "salute")
        luke "Não, não, você entendeu errado.{w=0.2} Isso é um lugar de respeito, não se preocupe.
        Mas ei, que tipo de estabelecimento fica completo sem um pouquinho de diversão?"

        $Luke.change("emotion", "wink")
        "Ele dá a Kota outra piscadela desleixada e sedutora, o que só faz o dragão
        retrair com outra carranca. Então o grifo se endireita e estende
        a mão para o novo hóspede."

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "pointing")
        $Asterion.change("emotion", "neutral")
        $Asterion.change("leftarm", "loose")
        luke "Foi mal se eu te deixei desconfortável. Tô só brincando...{w=0.2} na maior parte do tempo. Se você quer que eu cale a boca, é só me dizer."

        $Luke.change("emotion", "wink")
        luke "E ei, eu tava falando sério sobre aquela bebida. {w=0.2}Mas sem gracinha.
        Eu posso ser um tapado, mas consigo dizer quando um cara não tá interessado."

        pause 1.0

        $Luke.change("emotion", "neutral")

        luke "Vamo lá, relaxa, Azulzinho. Põe os pés pra cima e fica confortável.
        Quer dizer, você tá de roupão de banho, então já tá na metade do caminho, né?"

        $Kota.change("rightarm", "relaxed")
        "Cada palavra que sai do bico de Luke só faz o franzir de testa do dragão ficar mais profundo
        sobre seus olhos faiscantes e furiosos."

        kota "Vou passar esta, muito obrigado."

        $Luke.change("emotion", "annoyed")
        $Luke.change("arm", "hip")

        luke "Ei, eu disse foi mal. Não precisa ficar ofendidinho."

        kota "\"Foi mal\" não é o suficiente para compensar essa sua exibição grosseira e lasciva."

        $Luke.change("emotion", "surprise")
        $Kota.change("leftarm", "raised")
        kota "Se me permite falar o que penso, senhor Luke, você está me fazendo
        considerar dar meia volta e voltar para o deserto.
        Você é um cachorro sem vergonha, rude e desrespeitoso."

        kota "O tipo de exibição que você acabou de fazer espantaria qualquer um com
        um senso de decência para longe daqui, tenho dificuldade em entender por que o dono deste
        estabelecimento permite que você passeie por aí e o envergonhe dessa maneira."

        $Kota.change("emotion", "puzzled")
        "O dragão então vira para você e Astério; e enquanto sua expressão suaviza,
        você ainda pode enxergar a raiva fervendo por dentro."

        $Kota.change("rightarm", "raised")
        kota "E se {i}você{/i} me permite falar o que penso também, o fato de você confiar a
        alguém como...{w=0.2} {i}isto{/i}{w=0.2} qualquer tipo de responsabilidade por aqui
        transmite uma imagem terrível sobre a sua gestão deste hotel como um todo."

        show Asterion:
            xalign 0.5 yalign 1.0
            ease 1.0 xalign -0.1
        show Luke:
            xalign -0.1 yalign 1.0 xzoom -1
            ease 0.6 xalign 0.5
        show Kota behind Luke

        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "relaxed")
        $Kota.change("emotion", "surprise")
        $Asterion.change("emotion", "surprise")
        $Luke.change("emotion", "annoyed")
        $Luke.change("arm", "pointing")
        "Antes que você ou o minotauro consigam dizer qualquer coisa em resposta,
        Luke se aproxima brutamente e empurra um dedo no peito do dragão.
        As asas do grifo abrem atrás dele enquanto ele encara Kota."

        $Kota.change("emotion", "angry")

        luke "Ei! Você pode falar a merda que quiser de mim,
        mas não se atreva a insultar Angus e [player_name] onde eu posso te ouvir, beleza?"

        menu:
            "Intervir":
                $ global_affection += 0.5
                show Luke behind Kota
                $Luke.change("arm", "hip")
                $Kota.change("rightarm", "raised")
                "Kota afasta a mão de Luke com um tapa e grunhe, abrindo a boca para responder. Mas antes que ele
                consiga, você se coloca entre o grifo e o dragão."

                $Kota.change("rightarm", "relaxed")
                $Luke.change("emotion", "surprise")
                you "Basta, vocês dois!"

                $Asterion.change("emotion", "neutral")
                you "Luke, nós podemos cuidar disso. Vá e comece a deixar o bar em ordem para quaisquer
                hóspedes que possam vir hoje."

                $Luke.change("emotion", "annoyed")
                $Kota.change("emotion", "sad")
                you "E senhor Kota, peço sinceras desculpas por esta ser a primeira impressão que você tem do nosso
                hotel. Se você realmente quer ir embora, nem Astério nem eu vamos tentar impedi-lo. {w=0.2}Mas nós realmente
                queremos compensar você."

                you "Se você quiser que um de nós lhe mostre seu quarto, podemos acomodá-lo.{w=0.2}
                Platonicamente."

                pause 1.0

                you "Este é um lugar para viajantes, não...{w=0.2} não o que deve parecer para você. Se nos der uma
                chance, vamos mostrar que temos a melhor hospitalidade da região."

                $Kota.change("emotion", "puzzled")

                $Kota.change("leftarm", "raised")
                kota "...Muito bem. O senhor Astério não foi nada além de cortês e prestativo até agora,{w=0.2} e eu
                estou disposto a lhe dar uma chance de demonstrar que tipo de anfitrião você é,{w=0.2} senhor
                [player_name]."

                kota "No entanto, posso encontrar o caminho para meu quarto eu mesmo, muito obrigado."

            "Ficar fora disso":
                "Isso está começando a ficar feio, mas você não consegue pensar em nada para dizer e evitar que fique ainda
                mais feio. Mais uma vez, você pode apenas assistir e esperar o acidente de trem terminar."

                $Asterion.change("emotion", "angry")
                "Astério, no entanto, não fica onde está."
                show Luke behind Kota
                $Luke.change("arm", "hip")
                $Kota.change("rightarm", "raised")
                show Luke behind Asterion
                "Kota afasta a mão de Luke com um tapa e grunhe, abrindo a boca para responder."

                $Kota.change("emotion", "surprise")
                $Luke.change("emotion", "surprise")
                show Asterion:
                    xalign -0.1 yalign 1.0
                    ease 0.6 xalign 0.5
                show Luke:
                    xalign 0.5 yalign 1.0
                    ease 1.0 xalign -0.1
                "Mas, antes que ele consiga, o minotauro avança para colocar uma mão no ombro do dragão."

                asterion "Senhor Kota, por favor, se acalme. Como Zelador do hotel,
                ofereço minhas sinceras desculpas pelo comportamento do senhor Luke."

                $Luke.change("emotion", "annoyed")
                "Luke solta um grasno ofendido, mas Astério e Kota o ignoram."

                $Asterion.change("emotion", "neutral")
                $Asterion.change("leftarm", "raised")
                asterion "Permita que eu e o Mestre [player_name] compensemos você.{w=0.2} Se desejar,
                posso mostrar seu quarto e você pode se instalar sem maiores dificuldades."

                $Kota.change("emotion", "puzzled")
                kota "Obrigado, senhor Astério, mas isto não será necessário. Posso encontrar o caminho para meu quarto
                eu mesmo."

        $Asterion.change("leftarm", "loose")
        $Kota.change("emotion", "angry")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "relaxed")
        show Kota behind Asterion
        show Kota behind Luke
        "O dragão limpa a poeira imaginária do corpo e então dá ao grifo mal-humorado
        mais um olhar feroz. Seus lábios se curvam como se ele estivesse olhando para
        algo completamente repulsivo."

        kota "Qualquer coisa para ficar o mais longe possível... {i}disso.{/i}"

        show Kota:
            xalign 1.15 yalign 1.0
            ease 3.0 xalign -1.0

        show Luke:
            xzoom 1.0
            ease 2.0 xalign 0.85
        show Asterion:
            ease 2.0 xalign 0.15

        "Com isso e um último bufo, Kota se vira e segue pelo corredor em direção
        aos quartos do primeiro andar."

        hide Kota
        $Luke.change("arm", "pointing")
        $Asterion.change("rightarm", "hips")
        show Luke:
            linear 1.0 xalign 0.75
        luke "Isso, fica bem longe do meu bar, cuzão!
        Você acabou de ser banido pra sempre!"

        $Luke.change("arm", "hip")
        show Luke:
            ease 3.0 xalign 0.85
        "O grifo se volta para você e Astério, arrumando as penas eriçadas enquanto
        continua a ferver."

        luke "Dá pra acreditar nesse cara? A gente tenta fazer com que ele se sinta bem-vindo e é assim que ele agradece?"

        $Luke.change("emotion", "neutral")
        luke "Provavelmente você devia só ter mandado ele pro meio da rua, chefinho."

        menu:
            "\"Sim...\"":
                you "Talvez, mas ele ainda é um hóspede. Nossa missão é dar a quem precisa um lugar para
                ficar, não podemos simplesmente mandar as pessoas embora."
                you "Mesmo que sejam um pouco arrogantes."

            "\"Você não estava ajudando.\"":
                you "Astério e eu estávamos cuidando disso. E você não estava realmente ajudando, Luke."

                $Luke.change("emotion", "surprise")
                you "Ele está certo sobre uma coisa, você age muito grosseiramente. E com você se vestindo
                assim, bem, pode culpar o cara por confundir o lugar com um bordel ou algo assim?"

                you "Vamos falar sobre seu uniforme e atitude mais tarde. Por enquanto, vá esfriar sua cabeça."
                pause 1.0
            "Não dizer nada":
                "Você decide apenas ficar quieto; o que pode dizer depois de tudo isso?"
        $Asterion.change("emotion", "sad")
        $Luke.change("emotion", "annoyed")
        "O grifo solta um grasno de aborrecimento."

        show Luke:
            xzoom -1.0
        luke "Tanto faz. Vou lá pro bar. Não tô nem aí que tá cedo,
        preciso de uma bebida depois dessa merda."

        show Luke:
            ease 1.0 xalign 1.1

        pause 1.0
        $Luke.change("arm", "pointing")

        show Luke:
            xzoom 1.0
        luke "E ainda preciso deixar ele em ordem pros hóspedes que {i}não são uns puritanos de merda!{/i}"

        show Luke:
            xzoom -1.0
            ease 2.0 xalign 2.0
        $Luke.change("arm", "hip")

        "Luke se vira para gritar esta última parte em direção ao corredor para onde Kota
        foi, e então se vira para ir embora para o salão."

        hide Luke

    else:
        #The argument scene with Kota as the manager.
        show Kota:
            xalign -0.2 yalign 1.0
        show Luke:
            xalign 1.2 yalign 1.0

        $Luke.change("emotion", "hornier")

        "Alguma parte profunda e instintiva de você enxerga a expressão no rosto do novo hóspede,
        percebe o que está prestes a acontecer e grita para que você intervenha."

        "Mas, assim como assistir a um acidente de trem em câmera lenta, tudo o que você pode fazer é ficar parado
        enquanto o grifo se anima e sorri."

        play music "music/MayItBegin_Acoustic.ogg" fadein 2.0

        $Luke.change("emotion", "cocky")
        $Luke.change ("arm", "hip")
        $Kota.change ("rightarm", "relaxed")
        $Kota.change ("leftarm", "relaxed")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")
        luke "Ora ora, o que temos aqui? Não um, não dois, mas {i}três{/i}
        caras gostosos sozinhos em um hotel gigante no meio do nada?
        Eu devo ter morrido e ido pro céu!"

        show Luke:
            linear 1.0 xalign 1.1
        $Asterion.change("emotion", "neutral")
        $Luke.change ("arm", "pointing")
        "O olhar do grifo desliza como uma mão tateando para cima e para baixo em seu corpo,
        então se afasta para focar em Kota."

        show Luke:
            linear 1.0 xalign 0.95
        $Luke.change("emotion", "horny")
        $Luke.change ("arm", "hip")

        "Por um momento, você não tem certeza se fica aliviado por ele não estar mais despindo você com
        os olhos ou apenas um pouco insultado por ter sido posto para escanteio sem pensar duas vezes."
        $Luke.change("emotion", "cocky")
        luke "Meu nome é Luke.{w=0.2} Acabei de chegar aqui depois de uma viagem {i}longa, difícil e solitária{/i}. E você é..."
        $Kota.change("emotion", "angry")
        pause 1.0
        $Luke.change ("emotion", "hornier")
        $Luke.change ("arm", "hip")

        luke "...um maravilhoso pedaço de homem. O que acha de me ajudar com as malas e
        quando a gente chegar no meu quarto{w=0.2} eu ajudo {i}você{/i} com a {i}sua{/i} \"mala\"?"

        $Kota.change ("emotion", "puzzled")
        $Kota.change ("rightarm", "raised")
        kota "Como...{w=0.2} é?"

        $Luke.change ("emotion", "neutral")

        show Luke:
            linear 1.0 xalign 1.2
        show Kota:
            linear 1.0 xalign -0.3
        show Luke behind Asterion

        $Asterion.change ("emotion", "tired")

        "O som dos cascos de Astério batendo no chão enquanto ele anda rápido se aproximando chama
        a atenção de Luke de volta para o minotauro. Kota parece grato pela distração e
        vai para o seu outro lado, longe do novo hóspede."
        $Kota.change ("rightarm", "relaxed")
        $Asterion.change ("emotion", "bowing")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "raised")

        asterion "Senhor Walker,{w=0.2} por favor, permita-me apresentar o senhor Kota,{w=0.2}
        proprietário do salão do Hotel. E é claro,{w=0.2} o Mestre e dono de nosso
        estabelecimento,{w=0.2} Mestre [player_name]."

        $Asterion.change ("emotion", "neutral")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        $Luke.change ("emotion", "horny")
        $Luke.change ("arm", "hip")

        luke "\"Mestre\", hein...?"

        $Kota.change ("emotion", "angry")

        "Ele olha de você para Astério e de volta com um sorriso cada vez mais largo.
        A cauda dele treme atrás como se estivesse eletrizada."

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        if Asterion.clothes =="nude":
            $Luke.change ("emotion", "cocky")

            "O grifo dá outra boa e longa olhada em Astério, seu olhar ardente deslizando sobre
            o peito e coxas nus do minotauro antes de finalmente se estabelecer no nó da
            perizoma de Astério."

            $Luke.change ("emotion", "wink")

            "Luke dá a você uma piscadela de aprovação."

        luke "Depravado.{w=0.2} Eu aprovo!{w} E eu também não sou de enfiar meu nariz no que quer
        que esteja acontecendo entre você e o Angus aqui.{w} A não ser que estejam de boa, é claro, nesse caso..."

        $Luke.change ("emotion", "hornier")

        luke "Você pode fazer o que quiser comigo, também, {i}Mestre{/i}."

        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        you "Isso não... não é o que parece."


        $Luke.change ("emotion", "horny")
        "Luke ou não escuta você ou lhe está ignorando;
        seu foco voltou a ser flertar com Kota."

        $Kota.change ("emotion", "neutral")

        "O dragão tenta manter um sorriso educado diante do entusiasmo do
        grifo,{w=0.2} mas você pode ver quão tensa está a expressão
        pelo modo como a testa e os cantos dos lábios dele se contraem."

        $Luke.change ("arm", "pointing")
        $Luke.change ("emotion", "cocky")
        luke "E você é o di-... dito... é, cara encarregado do salão, né?
        {w} Ótimo!{w=0.2} Tava precisando mesmo de um lugar assim pra relaxar."

        $Luke.change ("emotion", "wink")
        $Kota.change ("emotion", "sad")
        luke "E se no meio do caminho eu for servido por um pitel absoluto que nem você, melhor ainda!"

        $Luke.change ("emotion", "cocky")

        luke "Então, onde que fica o salão? Que tipo de bebida você tem?
        E, o mais importante, você é solteiro?"

        $Luke.change ("arm", "hip")
        $Luke.change ("emotion", "neutral")
        $Kota.change ("emotion", "puzzled")
        $Kota.change ("rightarm", "raised")
        $Kota.change ("leftarm", "raised")
        kota "Eu... ah... bem..."
        "Kota vagueia com olhar, seus olhos implorando para você ou Astério o resgatarem do interesse lascivo de Luke."

        pause 1.0
        $Luke.change ("emotion", "laughing")
        pause 0.5
        $Kota.change ("emotion", "surprise")
        $Asterion.change ("emotion", "surprise")
        show Luke behind Kota
        show Asterion behind Luke
        $Luke.change ("arm", "pointing")
        show Asterion:
            ease 1.2 xalign 1.05
        show Luke:
            ease 0.8 xalign 0.15
        pause 0.8
        $Kota.change ("rightarm", "relaxed")
        show Luke:
            ease 1.3 xalign 0.35
        show Kota:
            ease 1.3 xalign -0.1

        "Depois de um longo e desconfortável momento, o grifo cai na gargalhada e
        dá um tapinha nas costas de Kota."

        $Kota.change ("emotion", "sad")
        $Luke.change ("emotion", "cocky")
        luke "Ei, relaxa, Azulzinho!{w=0.2} Eu só tô te provocando.{w} Na maior parte."
        $Luke.change ("emotion", "neutral")
        luke "Foi mal mesmo. Eu tenho uma tendência a chegar chegando e acabar sendo
        meio deselegante. Mas eu entendo quando um cara não tá interessado."

        "Ele dá um tapinha no ombro de Kota, então olha para você e Astério."
        $Luke.change ("arm", "hip")
        show Luke:
            xzoom -1
            linear 1.0 xalign 0.5

        $Asterion.change ("emotion", "neutral")

        luke "Isso vale pra vocês, também. Se eu passar dos limites, sintam-se à vontade
        pra me mandar calar a porra da boca, beleza?"

        $Asterion.change ("emotion", "bowing")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "raised")

        asterion "Como quiser, senhor Walker."

        $Kota.change ("emotion", "puzzled")
        $Asterion.change ("emotion", "neutral")
        you "Ei, tudo bem.{w=0.2} Você ainda é bem-vindo para ficar o tempo que quiser."

        $Luke.change ("emotion", "happy")
        show Luke:
            xzoom 1
            linear 1.0 xalign 0.35
        pause 0.5
        $Luke.change ("arm", "pointing")
        kota "Naturalmente."

        $Kota.change ("emotion", "puzzled")
        "O dragão lhe lança outro olhar. Você consegue concluir que Kota tem algo a dizer;
        e, pelo jeito que está olhando para o grifo, — o qual ainda mantém um braço em volta de seus ombros
        em um gesto íntimo demais — ele quer dizer sem que Luke ouça."

        you "Ei, Astério?{w=0.2} Se importa em mostrar ao Luke o quarto dele?"

        $Asterion.change ("emotion", "bowing")

        asterion "Muito bem, Mestre [player_name]."
        $Kota.change ("emotion", "sad")
        $Luke.change ("arm", "hip")
        show Luke:
            linear 1.0 xalign 0.45
        luke "Nah, nah, não precisa fazer isso.{w=0.2} Eu me viro."

        $Asterion.change ("emotion", "neutral")
        $Luke.change ("emotion", "neutral")

        luke "E, é... eu tava brincando com aquilo de \"me ajudar com as minhas malas\" agora há pouco.
        Tô com umas coisas no carro, mas posso ir pegar sozinho."

        $Asterion.change ("emotion", "smiling")

        asterion "Bobagem, senhor Walker. Como Zelador do Hotel, é meu dever servir
        aos hóspedes de todas as formas que puder."

        $Luke.change ("emotion", "neutral")
        show Luke:
            xzoom -1

        luke "Qual é, Angus, você tá me entregando a piada em uma bandeja de prata!"

        $Luke.change ("emotion", "cocky")

        luke "Mas é, não sou eu que vou recusar a ajuda de um homão igual você.
        Beleza, bora lá, então."

        $Asterion.change ("emotion", "tired")
        show Luke:
            ease 3.0 xalign 2.0
        show Asterion:
            ease 3.0 xalign 2.4

        "O minotauro e o grifo seguem o caminho até a porta da frente do hotel,
        Luke passeando enquanto Astério acompanha atrás dele."

        "Astério se vira para lhe lançar um olhar antes de seguir Luke até o pátio do Hotel e
        você faz uma careta de desculpa em troca."

        "Silenciosamente, você promete encontrar uma maneira de compensá-lo por isto."
        hide Asterion
        hide Luke

        show Kota:
            xalign -0.1
            ease 2.0 xalign 0.5
        you "Então, o que foi?"

        $Kota.change ("emotion", "puzzled")

        "Assim que a porta da frente se fecha atrás do novo hóspede e Astério,
        a máscara educada do dragão cai para revelar uma carranca de desprezo."

        $Kota.change ("leftarm", "raised")
        $Kota.change ("rightarm", "raised")

        "Ele passa a mão limpando os lugares onde Luke o tocou, como se estivesse tentando evitar
        que algo sujo manche suas roupas, e então se vira para você."

        kota "Se me permite falar o que penso, é... {i}esse{/i}
        é realmente o tipo de clientela que você deseja permitir no Hotel?"

        you "Como assim?"

        $Kota.change ("emotion", "angry")
        $Kota.change ("leftarm", "relaxed")

        "Kota gesticula para as portas da frente, como se a fonte de sua ira devesse ser óbvia."

        kota "{i}Esse{/i} tipo de pessoa...{w=0.2} rude,{w=0.1} sem vergonha{w=0.1}
        e desrespeitosa. Tenho calafrios só de pensar nele fazendo esse
        tipo de exibição em torno de qualquer outro hóspede que possa entrar.
        Isto afastaria {i}qualquer um{/i} com algum senso de decência."

        you "Ah, qual é, ele não parece tão ruim assim."

        $Kota.change ("emotion", "puzzled")

        "Uma das sobrancelhas do dragão arqueia para o alto, quase tocando a ponta de sua juba puxada para trás.
        Então Kota solta um suspiro longo e profundo."

        $Kota.change ("emotion", "sad")

        kota "Já lidei com clientes como aquele mais do que gostaria durante meus dias de bartender,
        e sim, [player_name]. Eles {i}são{/i} tão ruins assim."

        show Kota:
            xalign 0.5 xzoom -1
            ease 1.0 xalign 0.3

        $Kota.change ("rightarm", "relaxed")
        $Kota.change ("leftarm", "raised")

        kota "Tudo o que fazem é envenenar a atmosfera e arruinar a diversão dos outros clientes.
        Melhor mandá-los embora do que permitir que façam uma cena."

        kota "Ou pior."

        $Kota.change ("emotion", "puzzled")
        show Kota:
            xalign 0.3 xzoom 1
            ease 1.0 xalign 0.5
        $Kota.change ("leftarm", "relaxed")
        $Kota.change ("rightarm", "raised")

        kota "Não estou dizendo isto como um empregado, mas como um amigo que deseja o melhor para você,
        Astério e o Hotel. Se deixar uma desgraça como {i}aquela{/i} rondando por aí,
        ele apenas causará problemas."

        pause 1.0

        luke "Beleza,{w=0.1} Azulzinho,{w=0.1} conta pra gente como você {i}realmente{/i} se sente."

        $Luke.change ("emotion", "annoyed")
        $Luke.change ("arm", "pointing")
        $Kota.change ("rightarm", "relaxed")
        $Kota.change ("emotion", "surprise")
        $Asterion.change ("leftarm", "loose")
        show Kota:
            ease 1.3 xalign 0.0
        show Luke:
            xzoom 1 xalign 1.8 yalign 1.0
            ease 1.0 xalign 0.7
        show Asterion:
            xalign 1.8 yalign 1.0
            ease 1.3 xalign 1.1
        show Kota behind Luke
        show Asterion behind Luke

        "Parece que Astério e Luke voltaram para dentro enquanto você e
        Kota estavam conversando. E, julgando pela carranca no rosto do grifo, ele ouviu
        quase tudo que o dragão acabou de dizer."

        $Luke.change ("arm", "hip")

        "Luke fica parado com os braços cruzados, olhando de Kota para você e vice-versa enquanto bate com um pé no chão."

        $Kota.change ("emotion", "neutral")
        $Asterion.change ("emotion", "neutral")

        "A máscara neutra desliza de volta para o rosto do dragão enquanto ele se vira para dar ao novo hóspede uma profunda reverência."

        $Kota.change ("leftarm", "raised")

        kota "Senhor Walker,{w=0.2} peço sinceras desculpas se você ouviu qualquer coisa que-"

        "A mudança abrupta no comportamento do dragão parece apenas irritar Luke ainda mais.
        Ele se aproxima com um grito de aborrecimento, interrompendo Kota."

        $Kota.change ("emotion", "puzzled")
        $Kota.change ("leftarm", "relaxed")
        $Luke.change ("arm", "pointing")
        show Kota:
            ease 1.0 xalign -0.2
        show Luke:
            ease 0.7 xalign 0.5

        luke "Não, não, não me vem com essa baboseira de \"sinsinhô senhor Walker\".
        Qual é, se você tem algo pra falar, então diz na minha cara."

        pause 1.0

        luke "...Quer conversar sobre uma \"desgraça\"? Que tal um cara que sorri na sua
        frente e logo depois sai por aí falando merda nas suas costas?"

        $Luke.change ("arm", "hip")
        luke "Se você tivesse qualquer tipo de respeito, não ficaria fazendo rodeio."

        $Kota.change ("emotion", "laughing")
        kota "\"Respeito\"?"

        "O dragão explode em uma gargalhada alta e zombeteira, e então levanta para encontrar os olhos
        de Luke com um olhar penetrante."

        show Kota:
            ease 0.5 xalign -0.1
        $Kota.change ("emotion", "angry")
        show Luke behind Kota

        kota "Muito bem. Se me permite falar o que penso... Não tenho absolutamente nada a dizer
        para alguém como {i}você{/i}."

        luke "\"Alguém como eu\", hein?"

        show Luke:
            ease 1.4 xalign 0.4
        show Kota behind Luke

        "Luke se aproxima, seu bico estalando de raiva enquanto ele encara o dragão."

        luke "Tu é um verdadeiro cuzão do caralho, sabia disso?"

        show Luke behind Kota

        kota "E {i}você{/i}, senhor Walker, é um libertino bruto e infame."

        menu:
            "Intervir":
                $ global_affection += 0.5
                show Luke:
                    ease 1.0 xalign 0.5

                "Enquanto Kota empurra Luke, as garras do grifo se fecham em punhos ao lado dele.
                Mas antes que Luke possa fazer algo de que se arrependa, você se coloca entre
                os dois."

                $Luke.change ("emotion", "surprise")
                $Kota.change ("emotion", "surprise")

                you "Basta, vocês dois!"

                $Kota.change ("emotion", "sad")

                you "Kota, podemos cuidar disso.{w} Vá e comece a preparar o restaurante para receber
                quaisquer outros hóspedes que possam vir hoje."

                $Luke.change ("emotion", "annoyed")

                you "E senhor Walker,{w=0.1} Luke,{w=0.1} você precisa se acalmar.
                Peço sinceras desculpas por esta ser a primeira impressão que você tem do nosso hotel."

                you "Você ainda é bem-vindo para ficar. Nossa missão é dar a quem precisa um lugar para ficar
                por um tempo, e não mandamos ninguém embora. Se você abandonar a atitude
                de galanteador, Astério e eu ficaríamos felizes em compensar tudo isso para você."

                $Luke.change ("emotion", "neutral")
                pause 1.0
                $Luke.change ("emotion", "annoyed")
                you "...Não desse jeito."

                pause 1.0

                luke "...Tudo bem. Sinto muito a você e ao Angus por {i}causar problemas.{/i}"

                show Luke:
                    xzoom -1
                    ease 1.0 xalign 0.7

                "Ele lança um olhar petulante na direção de Kota. Em seguida, Luke segue o caminho de volta para
                Astério para pegar a mala de tecido grande e gasta nos braços do minotauro e pendurá-la
                sobre o ombro."

                show Luke:
                    xzoom 1

                luke "Vou me mandar pro meu quarto e deixar vocês em paz, beleza?"

            "Ficar fora disso":
                "Isso está começando a ficar feio, mas você não consegue pensar em nada a dizer para evitar que fique
                ainda mais feio. Mais uma vez, você pode apenas assistir e esperar o acidente de trem terminar."

                $Asterion.change ("emotion", "angry")
                "Astério, no entanto, não fica onde está."

                $Luke.change ("emotion", "surprise")
                $Kota.change ("emotion", "surprise")
                $Luke.change ("arm", "hip")
                show Luke:
                    ease 1.0 xalign 0.5
                show Kota:
                    ease 1.0 xalign -0.1
                show Asterion:
                    ease 0.8 xalign 0.9
                show Asterion behind Luke
                show Kota behind Asterion

                "Enquanto Kota empurra Luke para longe, as garras do grifo se fecham em punhos ao lado dele. Mas
                antes que Luke consiga fazer algo que provavelmente vai se arrepender, o minotauro dá um passo à frente
                para colocar uma mão em seu ombro."

                $Asterion.change ("emotion", "bowing")
                $Asterion.change ("leftarm", "raised")

                asterion "Senhor Walker, peço que se acalme."

                "Os séculos de Astério lidando com hóspedes indisciplinados brilham diante de vocês.
                Seja o tom de voz do minotauro, ou o peso de sua mão,
                ou o olhar em seu rosto, isto faz o grifo engolir seco e acenar com a cabeça."

                show Luke:
                    ease 1.0 xalign 0.7
                show Asterion:
                    ease 0.8 xalign 1.1

                "Luke permite que Astério o afaste de Kota, separando os dois."

                $Asterion.change ("emotion", "neutral")

                asterion "...Como Zelador do Hotel, ofereço minhas sinceras desculpas se Kota
                falou demais. Nossa missão é dar a todos que precisam um lugar seguro de descanso
                e conforto, e não mandaremos ninguém embora."

                $Kota.change ("emotion", "angry")

                "Kota solta um bufo insultuoso, mas Astério e Luke o ignoram. O minotauro
                olha em sua direção e você acena com a cabeça."

                asterion "Por favor, permita que eu e o Mestre [player_name] compensemos você. Se
                desejar, posso lhe mostrar seu quarto e você pode se instalar sem maiores
                dificuldades."

                pause 1.0

                $Luke.change ("emotion", "annoyed")
                show Luke:
                    xzoom -1

                luke "Não, você não precisa fazer isso, Angus. Desculpa. Eu vou...{w=0.2} Eu vou me mandar pro meu quarto
                e deixar vocês em paz."

                show Luke:
                    xzoom 1

                "Ele estende a mão para pegar a mala de tecido grande e gasta nos braços de Astério e a pendura
                sobre o ombro."

        $Asterion.change ("emotion", "neutral")
        $Asterion.change ("leftarm", "loose")
        show Luke:
            ease 3.0 xalign -1.0
        show Luke behind Kota

        $Kota.change ("emotion", "puzzled")

        "O grifo não dá a Kota um único olhar enquanto caminha pelo corredor
        em direção aos quartos de hóspedes."

        show Kota:
            ease 2.0 xalign 0.9
        show Asterion:
            ease 2.0 xalign 0.1
        pause 2.0
        show Kota:
            xalign 0.75 xzoom -1

        $Kota.change ("rightarm", "raised")
        $Kota.change ("leftarm", "raised")
        "Mais uma vez, o dragão se limpa passando as mãos, e então se vira para você e Astério."

        kota "Entende o que quero dizer? Estou chocado que você permitiu que ele ficasse depois {i}disso{/i}."

        menu:
            "\"Sim...\"":
                you "Sim, ele é um pouco... demais. Só não deixe ele conseguir te irritar, tudo bem?"

                $Asterion.change ("emotion", "tired")
                asterion "Devo admitir que também tinha minhas ressalvas sobre o Sr.Walker."

                $Asterion.change ("emotion", "contemplative")
                asterion "No entanto, não acho que ele seja malicioso. Ele é...{w=0.2} demais, como você disse, Mestre
                [player_name]. Mas o Hotel teve sua leva de excêntricos ao longo dos anos."

                $Kota.change ("emotion", "angry")
                kota "Não diga que eu não avisei quando ele incendiar o lugar, então."
                $Asterion.change ("emotion", "sad")
            "\"Você não estava ajudando.\"":
                you "Astério e eu estávamos lidando com isso muito bem até você falar sobre a expulsão.
                Isso não ajudou, Kota."

                $Kota.change ("emotion", "surprise")
                you "Olha, eu entendo sua preocupação e quero que me diga se achar que alguma coisa vai ser
                um problema. Mas nem Astério nem eu vamos simplesmente expulsar alguém porque você se ofendeu
                com algo que eles disseram."

                you "E eu não quero que você brigue com hóspedes por causa de coisas assim,
                certo?"

                you "Falaremos mais sobre isso depois. Por enquanto, vá esfriar sua cabeça."
                pause 1.0
                $Kota.change ("emotion", "puzzled")
            "Não dizer nada":
                "Você decide apenas ficar quieto; o que pode dizer depois de tudo isso?"

        "O dragão solta um bufo de aborrecimento, então dá a você e Astério uma reverência rasa."

        $Kota.change ("rightarm", "relaxed")

        kota "Peço desculpas por falar demais. Se me dão licença, irei ao restaurante para deixar tudo em ordem
        para quaisquer outros hóspedes que possamos receber."

        $Kota.change ("leftarm", "relaxed")
        $Kota.change ("emotion", "angry")

        kota "Se bem que, para ser franco, não quero ver uma única pena {i}daquele homem{/i} em qualquer lugar perto dali."

        show Kota:
            xzoom 1
            ease 3.0 xalign 2.0

        "Kota se vira e segue em direção ao restaurante, ainda resmungando baixinho."

        kota "Terei que colocar uma placa de \"sem camisa, sem sapatos, sem serviço\" para
        que ele não tire a roupa e desfile por aí de cueca. Céus, consegue imaginar?"

        hide Kota

    #both branches end here
    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "loose")
    $Asterion.change ("rightarm", "hips")
    show Asterion:
        ease 1.0 xalign 0.5

    "Para o melhor ou para o pior, acabou. Por enquanto, pelo menos."

#nanoff I specifically want these comments to be in the final game, some poor codefag will crack
#open the game one day and see all this fucking shit it's gonna be great
#yes, also keep the comments where I ask you to keep the comments, those are important too

#Scene description:
#A couple arrives at the hotel: it's Greta of the Abyss and Jean Jacques Rosseau.
#Asterion is having an uncontrollable fit of laughter. The Kota/Luke argument may have been tense,
#but it's such a small thing compared to everything he's been through.

    pause 1.0

    "Um suspiro força o caminho para fora de seu peito. Que começo para seu empreendimento na indústria da hospitalidade."

    "Poderia-se perdoar alguém que ficasse no limite por conta de tal confronto.
    Mas para alguém como Astério, depois de tudo o que ele passou, que impacto poderia ter?"

    stop music fadeout 3.0

    "Você se vira para ele."

    $Asterion.change ("emotion", "sad")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    you "Astério...{w=0.3}desculpe, não esperava que as coisas dessem uma virada tão brusca para o pior."

    you "Você está bem?"

    pause 1.0

    $Asterion.change ("emotion", "tired")

    "O minotauro olha para o chão. Seus olhos vão e voltam enquanto uma centena de ideias desliza por sua mente."

    "O ar sibila conforme ele inspira com os dentes cerrados e, a cada expiração, suas narinas dilatam e tremem."

    "Você tem um breve vislumbre dos olhos de Astério antes que eles se fechem. Que memórias,
    que emoções estão passando por sua cabeça neste momento?"

    "E então seus lábios tensionam, mas não da maneira que você esperava."

    play music "music/KoraDuet.ogg" fadeout 4.0 fadein 4.0

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    "No início, você precisa forçar sua audição para captar — um riso ocasional,
    aqui e ali, como as cordas de uma harpa suavemente tocadas."

    $Asterion.change ("emotion", "laughing")

    "De repente, as cordas são soltas de uma vez só e, em uma explosão, a risada de Astério se espalha pelos
    corredores do hotel e por todo o caminho até o vale."

    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")

    "Ele arremessa a mão para cobrir a boca e, no meio do caminho, empurra canetas e lápis para fora da mesa."

    "O gesto, no entanto, serve apenas para destacar os cantos de sua boca.
    Por mais que tente, eles o desobedecem e sobem em um sorriso — e seu único olho,
    para não ser excluído, se fecha em alegria."

    "Ele surfa ondas — desde uma risadinha furtiva até um berro estrondoso de curvar as costas."

    show Asterion:
        ease 1.0 xalign 0.4

    "Ele se debruça sobre a mesa para recuperar o fôlego e, mesmo entre soluços laboriosos, continua sorrindo."

    "Ele olha para você com os olhos turvos, raiados de lágrimas brilhantes.
    Ele precisa de uma dúzia de tentativas antes de conseguir cuspir uma frase coerente."

    $Asterion.change ("rightarm", "hips")
    show Asterion:
        ease 1.0 xalign 0.5

    if global_affection <= 3:
        asterion "Sinto muito, meu senhor...{w=0.2} me perdoe, eu não sei o que...{w=0.2} o que há de errado..."
        "O minotauro se dobra em um renovado ataque de risadas."
    else:
        asterion "Eu? Eu não me sinto tão bem há cem anos."
        asterion "Isso...{w=0.2} isso é ótimo, meu senhor. É disso que a vida é feita. Eu estou vivo novamente."

    $Asterion.change ("leftarm", "loose")
    "Atrás de você, a porta emite um clique não mais alto que um rangido."

    show Greta:
        xalign 1.8 xzoom -1 yalign 1.0
        ease 2.0 xalign 0.8
    show Ismael behind Greta:
        xalign 2.1 xzoom -1 yalign 1.0
        ease 2.0 xalign 1.1
    show Asterion:
        ease 1.2 xalign 0.2

    "Você se vira e se depara com um casal no momento em que eles jogam no chão um par
    de mochilas altas."

    "Os dois param de repente quando avistam o minotauro atrás do balcão,
    arfando em uma explosão de risadas histéricas."

    hide Ismael
    show Ismael_surprise behind Greta:
        xzoom -1 xalign 1.1 yalign 1.0

    "E naquele momento de tremer o chão, as mentes deles correm soltas — um hotel no meio de um deserto
    sem vida, aparentemente abandonado, mas abrigando nada menos do que um minotauro."

    "Um homem-touro sorridente, na verdade, cujo berro turbulento soa muito melodioso para impor terror."

    $Asterion.change ("leftarm", "raised")
    "Astério avista o casal no canto do olho, mas isto nada faz para impedi-lo
    — e, na verdade, a presença de uma audiência só parece amplificar sua alegria."

    if player_background == "speedrunner":
        asterion "PFFFT HAHAHAHAHA, OLHA A CABEÇA DELE!"

    show Asterion:
        ease 1.0 xalign 0.1

    "Não dura mais do que alguns segundos, mesmo que pareça uma eternidade —
    para o riso superar o medo e a apreensão, para preencher a lacuna entre o corriqueiro
    mundo lá fora e o hotel assustador."

    hide Ismael_surprise
    show Greta:
        ease 1.0 xalign 0.6
    show Ismael behind Greta:
        xzoom -1 xalign 1.1 yalign 1.0
        ease 2.0 xalign 0.9

    "Primeiro, a senhorita se aproxima e, em seguida, o homem segue enquanto os dois caminham
    até a mesa da recepção. Eles olham para você, depois para o minotauro, e então de volta para você."

    show Asterion:
        ease 1.0 xalign 0.2

    "Senhorita" "Com licença, mas que lugar é esse?"

    you "É...{w=0.2}um hotel."

    "Seus olhos grandes e afiados fixam-se no minotauro incapacitado enquanto ele finalmente recupera um semblante de compostura."

    "Senhorita" "Sim, mas..."

    "Senhorita" "O que deu nele?"

    show Asterion:
        ease 1.0 xalign 0.0

    "Astério está se apoiando contra a parede, respirando lenta e profundamente para
    se acalmar enquanto os tremores de riso o atingem."

    you "É um dia muito especial para ele. Faz um bom tempo que ele não recebe hóspedes e,
    pouco antes de você chegar, tivemos uma grande comoção."

    "Senhorita" "Não, eu quero dizer... O que {i}é{/i} ele?"

    you "Bem, ele é..."

    menu:
        "O zelador do hotel.":
            scene bg black
            with Dissolve (1.0)
        "Nosso bom anfitrião.":
            $global_affection += 0.5
            scene bg black
            with Dissolve (1.0)
        "Um homem.":
            $global_affection += 0.5
            scene bg black
            with Dissolve (1.0)

    "Pequena é a lacuna que mantém a humanidade longe de todos os tipos de verdades de tremer o chão."

    "Todos os humanos, quanto dada a oportunidade de vislumbrar um segredo, podem escolher
    voltar atrás e retornar para o lugar de onde vieram.
    Esquecer o que estava além daquela fenda não mais larga que a lateral de uma porta."

    "Mas o riso, aquela música essencialmente humana, acena."

    pause 1.5

    stop music fadeout 2.0

    asterion "Este é o Mestre [player_name],{w=0.2} e meu nome é Astério.{w=0.2}
    Aqui está a chave do seu quarto.{w=0.2} O jantar será servidor às 7PM.{w=0.2}
    É um prazer recebê-los e espero que aproveitem a estadia."

    pause 3.0

    $chapter = "Capítulo 9"

    call screen ChapterTransition("Capítulo 9", "Jantar no salão")
    pause 0.5
    $save_name=output_save_name("Capítulo 9")

    scene Lounge
    with Dissolve (2)

    image LoungeLight:
        contains:
            "pinktint"
            alpha 0.0
            linear 1.0 alpha 0.7
            pause 1.0
            linear 1.0 alpha 0.0
            pause 1.0
            repeat
        contains:
            "bluetint"
            alpha 0.7
            linear 1.0 alpha 0.0
            pause 1.0
            linear 1.0 alpha 0.7
            pause 1.0

    if first_guest == "Luke":
        play music "music/Solidarity.ogg" fadeout 1.0 fadein 1.0
        show LoungeLight
        with Dissolve (0.5)
    else:
        play music "music/TheSorrow.ogg" fadeout 4.0 fadein 4.0

    #scene at the lounge
    #MC mingles with the human normies in the lounge during dinner.
    #The lounge's manager and Asterion are busy cooking.
    #MC can talk with the guests who arrived recently

    "Nove hóspedes se estabeleceram ao final do dia."

    "O casal de caroneiros — eles estiveram mochilando pela Europa Oriental antes de
    serem atraídos para o hotel — que ficará um dia ou dois antes de prosseguir com a viagem."

    "Uma dupla de trabalhadores de colarinho azul da América do Sul que parecem ter se deparado com um
    bloqueio de estrada em sua viagem de trabalho e agora estão esperando alguns dias pela chegada de suprimentos."

    "Uma turma de quatro estudantes universitários do Oriente Médio, cujo carro quebrou no
    meio do nada. Serem atraídos para o hotel os poupou de uma noite
    tremendo no frio."

    if first_guest == "Luke":

        "E Lucas Walker, aquele grifo hiperativo — para dizer o mínimo."

        $LoungeBlobs[0] = False
        $Luke.change("clothes", "tankpants")
        $Luke.change("arm", "salute")
        $Luke.change("emotion", "wink")
        show Luke behind LoungeLight:
            xzoom -1 xalign -1.0 yalign 1.0
            ease 2.0 xalign 0.0

        "Luke aprendeu uma lição sobre modéstia e vestiu mais roupas. Agora ele está preparando, como esperado,
        uma refeição tradicional americana para satisfazer seus clientes famintos: uma grande fornada de hambúrgueres."

        "Você observa o grifo trabalhar com uma facilidade praticada, apesar da nova posição
        — ele está acostumado a cozinhar para um grupo se a velocidade com que molda a carne picada em suas
        garras é alguma indicação."

        "Em pouco tempo ele acumulou uma enorme pilha de hambúrgueres, cujo chiar logo impregna o
        salão com o aroma de carne assada."

        "Mesmo assim, ele parece ter feito uma baita quantidade — cada hóspede poderia comer dois
        ou três hambúrgueres cada e ainda sobraria meia dúzia."

        "Colocar cada hambúrguer em seu pão é uma tarefa simples, uma vez que estejam prontos, mas nenhuma
        quantidade de autocontrole pode impedi-lo de cobrir a boca ao ver Luke começar com o recheio."

        "Em vez de invocar fatias de queijo à mão, sua mente permite que a familiaridade
        supere a eficiência; cada quadrado laranja brilhante de queijo pasteurizado e processado é
        embalado individualmente em pacotes descartáveis."

        "Assim que tem todos os hambúrgueres cobertos, ele está andando em uma pilha de plástico que se estilhaça sob
        os pés como folhas crocantes de outono."

        "As coisas continuam a crescer como uma bola de neve fora de controle a partir daí: para o molho, ele mistura maionese
        e ketchup, seguido de uma porção saudável de queijo nacho e uma camada de migalhas de tortilha
        recém-moídas."

        "O conteúdo calórico do hambúrguer só continua disparando conforme o grifo prepara — ao ponto
        que fritar o pão de cima em banha e regá-lo com pedaços de bacon é o caminho esperado para
        este ataque cardíaco iminente em forma de hambúrguer."

        "Você consegue {i}sentir{/i} suas artérias entupindo só de olhar."

        show Luke:
            ease 2.0 xalign -1.0
        pause 2.0
        hide Luke
        $LoungeBlobs[0] = True
    else:
        "E Kota, aquele dragão bastante peculiar."

        $LoungeBlobs[0] = False
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        $Kota.change("emotion", "laughing")
        show Kota:
            xzoom -1 xalign 2.0 yalign 1.0
            ease 2.0 xalign 1.0

        "O comportamento de Kota na cozinha é tão cerimonioso e profissional quanto em qualquer outro lugar;
        antes de começar, ele caminha de mesa em mesa, apresentando-se como
        servente e fazendo uma educada reverência ao sair."

        "Em momentos como este, a força de sua confiança em normas sociais rígidas mostra-se evidente."

        "Ele trata o salão como um restaurante, perguntando se os hóspedes possuem alergia alimentar e tentando
        ajustar as coisas de forma a satisfazer o maior número de pessoas com uma única refeição."

        "O dragão azul também sente a necessidade de comentar sobre sua escolha com você e Astério antes
        de começar a cozinhar: parece que sopa de missô é o que está no cardápio."

        "Com a elegância de um riacho de montanha, Kota reúne seus ingredientes e põe-se a trabalhar,
        focado e preciso. Ele começa com o caldo primeiro — colocando alguns itens diferentes na
        panela e deixando seu sabor penetrar na água."

        "Você pode distinguir algas marinhas de algum tipo entrando primeiro enquanto a água esquenta acima de
        uma chama mediana, mas ela é coada pouco antes de o líquido começar a ferver."

        "Assim que o caldo começa a ficar turbulento, ele adiciona algum tipo de material flocoso,
        cuja natureza é mais difícil de discernir, mas quando o aroma de peixe começa a perfumar o ar,
        você sente que tem uma boa ideia do que era."

        "Reduzindo o calor e removendo o que restou dos flocos de peixe, ele acrescenta alguns acréscimos
        importantes: uma cebola verde finamente picada, cenoura ralada e pequenos cubos de tofu."

        "Para finalizar, Kota amassa uma bola de pasta esbranquiçada na choncha e mistura até que se
        dissolva."

        "Todo o processo leva cerca de 20 minutos — mas o dragão o executa com louvor,
        rapidamente invocando um conjunto de tijelas de laca e hashis para servir a sopa."

        show Kota:
            ease 2.0 xalign 2.0
        pause 2.0
        hide Kota
        $LoungeBlobs[0] = True


    "Você os observa de uma mesa a poucos metros do bar."

    "A refeição desta noite é simples. Para um hotel tão grande, não seria nada assombroso mas,
    com todos reunidos aqui, é como estar em um jantar em família educado, onde
    nenhum parente se faz de bobo."

    if first_guest == "Luke":

        "O grifo encontra-se vertiginoso enquanto inspeciona seu trabalho. A crescente expressão de
        horror abjeto no rosto de vários hóspedes não registra em seus olhos, de tão concentrado que
        ele está na elaboração de sua obra-prima."

        $LoungeBlobs[0] = False
        $Luke.change("clothes", "tankpants")
        $Luke.change("arm", "pointing")
        $Luke.change("emotion", "surprise")
        show Luke behind LoungeLight:
            xzoom -1 xalign -1.0 yalign 1.0
            ease 2.0 xalign 0.0

        "No entanto, assim que ele começa a andar em direção aos hóspedes, sua expressão muda para uma de perplexidade e depois para uma de revelação:"
        luke "Cacilda, I'll be a yankee-doodle dumbass! Esqueci das batatas fritas!"
        "As mãos de Luke transformam-se em um borrão de movimento assim que
        ele começa a trabalhar, cantarolando e dançando ao ritmo de uma melodia em sua cabeça."
        show Luke:
            ease 2.0 xalign -1.0
        "Sem perder o ritmo, ele despeja a gordura do bacon em uma panela e começa a
        trabalhar em seu acompanhamento enquanto o óleo esquenta."

        "No entanto, ao verdadeiro estilo americano, um acompanhamento não é apenas um acompanhamento:
        pode muito bem ser outra refeição em si."

        "Ele joga mais carne moída em uma panela separada e acrescenta especiarias e temperos
        mais rápido do que os olhos podem ver: pimenta caiena, chilli em pó,
        cominho e páprica entram na mistura um após o outro."

        "Sal, entretanto, prova-se problemático — por alguma razão, o hotel não o materializa,
        forçando Luke a recorrer à despensa."

        "Uma vez que a carne esteja dourada, ele pega alguns vegetais e, por um breve momento, você
        se permite ter esperanças de que o valor nutricional inerente deles de alguma forma equilibrem o que
        ele está prestes a fazer."

        "Você quase sente a necessidade de saudar aquela cebola solitária e corajosa, a brigada de pimentões e feijões e
        a cavalaria de chipotles e outros pimentões que se juntam à carne mexida antes de serem todos afogados
        em um mar de pasta de tomate."
        "Enquanto o chili ferve, Luke corta as batatas em formato julienne e as mergulha no óleo fervente com um chiado satisfatório
        — em seguida, as amontoa até formar uma pilha de batatas fritas crocantes e douradas."

        "Dividindo a pilha em algumas cestas grandes, o grifo despeja o chilli e, em seguida,
        polvilha uma porção generosa de queijo ralado, creme de leite e uma cebola verde picada por cima."
        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "hip")
        show Luke:
            ease 2.0 xalign 0.0
        "Enquanto ele se agita em direção aos hóspedes, ainda dançando ao ritmo de uma batida errática e inaudível,
        você pode apenas agradecer às suas estrelas da sorte por ele não ter optado em sair andando por aí com sua cueca tanga característica."
        play sound "sfx/clink.ogg"
        luke "O rango tá pronto!"

        "Assim que a comida é entregue, Luke se acomoda nos bastidores, satisfeito com um trabalho bem feito.
        Seu rosto assume uma aparência de inocência infantil quando ele se inclina sobre o balcão e observa a
        clientela, apesar da tensão crescente."
        "Alguns dos hóspedes olham para o abismo de calorias que se segue na esteira do grifo,
        como se esperando que ele olhasse de volta."
        "Cada um deve se resolver com o fato de que suas papilas gustativas serão
        alteradas para todo o sempre com a epifania que este maluco da culinária está prestes a transmitir."
        "Primeiro, um estudante do Oriente Médio, agarra um pequeno pingente de prata contra o peito na
        esperança de que ele desvie qualquer feitiçaria sombria da hegemonia cultural americana que o chef
        introduziu no preparo — sem sucesso."
        $Luke.change("emotion", "laughing")
        "Segundo, o francês que acompanha Greta, se aproxima de Luke para pedir talheres apenas para se
        deparar com uma gargalhada grasnada e estridente — nenhum cliente seu corromperá um cheeseburger o
        comendo com qualquer coisa que não as próprias mãos."

        show Luke:
            ease 2.0 xalign -1.0
        pause 2.0
        $LoungeBlobs[0] = True
        "Luke sai de trás do balcão e faz uma demonstração com um dos hambúrgueres extras."

        "Um fato novo e horripilante sobre Luke é revelado: ele não mastiga. Ele abre a boca,
        mais largo que até uma cobra poderia, e enfia tudo dentro."

        "Acontece tão rápido que você começa a duvidar se o hambúrguer realmente esteve lá alguma hora —
        não fosse pela maneira como ele lambe os dedos para limpar a gordura antes de passar para o próximo, e o próximo."

        "Você percebe seu erro tarde demais: a maior parte das \"sobras\" eram para o grifo o tempo
        todo, e ele está pronto para comer tudo sem pestanejar."

        "Com apenas um hambúrguer faltando antes dele se encher com mais carne que um
        turducken de ação de graças, ele só para duas vezes."

        "Uma para oferecer um prato para Astério, que gagueja explicando que não come carne bovina,
        e outra para dar um tapinha em suas costas, deixando uma marca de óleo em sua
        camisa."

        "Ainda assim, o entusiasmo de Luke é contagiante o suficiente para vencer, uma vez que a fome
        supera a apreensão; a tensão se quebra e a conversa continua,
        interrompida apenas por um ocasional arroto satisfeito ou um dos comensais entrando em coma alimentar."

        "Alguns dos hóspedes sentam-se no bar, perto suficiente uns dos outros para gritar em cima
        da música explodindo nos auto-falantes. Outros sentam-se nas grandes mesas redondas,
        conversando uns com os outros."

        #$Luke.change("clothes", "speedo")

    else:

        "Mesmo depois que a sopa está pronta e todos foram servidos, Kota não parece se contentar em
        relaxar — tão cedo quanto o último hóspede pega sua tijela de laca, o dragão volta para a cozinha
        para fazer mais."

        "Quando você o pressiona por detalhes, ele menciona que a sopa de missô costuma ser considerada um acompanhamento
        mais que uma refeição completa na culinária japonesa, e é geralmente servida com pelo menos três outros alimentos e
        uma tijela de arroz."

        "No entanto, a maioria dos outros pratos são simples de se fazer e brevemente acompanham a sopa na mesa:
        arroz integral, salada de pepino, cavala grelhada e frango frito."

        "Da mesma forma, o arroz é a única coisa feita sem adições — a salada é guarnecida com sementes de gergelim e
        vinagrete de molho de soja caseiro, a cavala é acompanhada de rabanete ralado e até mesmo o frango
        possui molho tártaro fresco regado por cima."

        $LoungeBlobs[0] = False
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        $Kota.change("emotion", "happy")
        show Kota:
            xzoom -1 xalign 2.0 yalign 1.0
            ease 2.0 xalign 1.0

        "Kota parece ter feito um verdadeiro banquete; embora, conforme ele afirma com uma reverência humilde que isso
        é tudo o que ele poderia fazer com o tempo de preparação de uma hora, você diz para ele que é mais do que o suficiente."

        $Kota.change("emotion", "puzzled")

        "Os hóspedes parecem estar felizes de coração em relação à comida em sua frente,
        mas as coisas se complicam assim que toda a comida está na mesa."

        "Kota pode apenas assistir em crescente desaprovação pela abominável falta de modos à mesa e
        seu largo sorriso logo torna-se tenso, da mesma maneira de quando ele e Luke
        se desentenderam mais cedo."

        $Kota.change("rightarm", "relaxed")

        "Vários hóspedes têm dificuldade com o uso dos palitinhos e o dragão fica mais que feliz em dar
        uma ajuda aos seus rebeldes protegidos — embora ele não interrompa seus conselhos sobre
        etiqueta adequada, mesmo depois de todos terem compreendido o básico."

        $Kota.change("emotion", "sad")

        "Até mesmo Astério frustra Kota neste quesito, embora inocentemente; o dragão solta um suspiro ao ver
        que as mãos do minotauro não possuem a destreza necessária para utilizar os palitinhos e
        continua zunindo pela sala de jantar para dar sermões aos casos menos desesperados e implacáveis."

        show Ismael:
            xzoom 1 xalign -1.0 yalign 1.0
            ease 2.0 xalign 0.0

        "Quando chega à mesa de Greta, Ismael leva o pior deles por ter ensinado errado aos outros.
        Suas tentativas de imitar a cultura japonesa são todas baseadas em animes que ele viu e,
        como resultado, o tiro sai pela culatra espetacularmente quando confrontado com o escrutínio do dragão."

        $Kota.change("emotion", "puzzled")
        $Kota.change("leftarm", "raised")

        kota "Senhor,{w=0.2} por favor,{w=0.2} não leve o arroz para tão perto do rosto. A tijela deve ser segurada
        em frente ao seu peito, para pegar o arroz que cai de sua boca.
        Fazer de outra maneira seria muito inapropriado."

        pause 1.5
        $Kota.change("leftarm", "relaxed")

        kota "Não,{w=0.2} assim não. Quatro dedos apoiam a parte inferior da tijela enquanto o polegar
        repousa na lateral. Sua outra mão segura os palitinhos."

        pause 1.0

        $Kota.change("emotion", "sad")

        kota "É aceitável sorver sua sopa,{w=0.2} mas, por favor, não arrote na cara dos outros comensais!"

        $Kota.change("emotion", "angry")
        $Kota.change("rightarm", "raised")

        hide Ismael
        show Ismael_surprise:
            xzoom 1 xalign 0.0 yalign 1.0

        "Quando o francês pega o molho de soja e o leva ao arroz,{w=0.2} Kota pode apenas apontar uma mão
        acusatória para ele e sussurrar{w=0.3} {i}\"Não ouse.\"{/i}{w=0.3} antes de partir e começar a
        recolher os pratos dos hóspedes que comeram mais rápido."

        show Kota:
            ease 2.0 xalign 2.0
        show Ismael_surprise:
            ease 2.0 xalign -1.0
        pause 2.0
        hide Kota
        hide Ismael_surprise
        $LoungeBlobs[0] = True

        "Apesar da atmosfera formal transmitida pela decoração meticulosa de Kota, os hóspedes
        conversam com um calmo entusiasmo. Eles movem as mesas e cadeiras do restaurante para acomodar
        grupos maiores de pessoas se necessário e sentam-se ao lado daqueles com os quais se misturam melhor."

    "Risadas deslizam nos arredores, sussurros e bate-papo zumbem e abafam o barulho da cozinha."

    "Eles trocam histórias de suas viagens e de como vieram parar aqui em primeiro lugar,
    mas a cada poucos minutos você ouve sussurros sobre \"o minotauro, o dragão e o grifo.\""

    "Alguns hóspedes ficaram mais apreensivos do que outros quando chegaram. Ver um minotauro como
    recepcionista foi um choque, mas Astério revelou um carisma e leveza que cativou a curiosidade deles."

    "De relance, ele soube como melhor abordar cada hóspede — alguns precisaram de reafirmação,
    outros não pensaram duas vezes antes de entrar e pedir um quarto. Às vezes, ele até fazia piadas sobre
    sua própria aparência bovina para quebrar o gelo."

    "Por sua vez, os olhares indiscretos e sussurros abafados dos hóspedes não fizeram Astério nem mesmo dar um tique
    — era como se ele nem os notasse."

    "Mas agora, durante o jantar, os hóspedes conversam entre si. Não lhes passa pela cabeça o quão
    peculiar é que todos falem a mesma língua neste hotel no meio do nada."

    "Embora vários deles se aproximem para oferecê-lo uma palavra de agradecimento, o bom humor dos hóspedes
    é elogio suficiente — uma prova de seu trabalho árduo na reforma do hotel com Astério."

    $LoungeBlobs[0] = False

    play sound "sfx/faucet.ogg"
    "E, ainda assim... bem fora de vista você ouve o barulho de pratos sendo lavados.
    Até agora, o minotauro passou todo o jantar escondido na cozinha."

    "Você ainda se lembra das risadas desta manhã. Astério não tinha ficado tão animado assim antes.
    Conhecer os hóspedes foi de longe uma ocasião mais alegre do que deixar a câmara fria."

    "Você não consegue suportar vê-lo se escondendo nos fundos enquanto todos se divertem."

    scene bg kitchen
    with Dissolve (1.0)

    "E então,{w=0.2} você segue o caminho até a cozinha."

    "Já que Astério tem cozinhado suas refeições nos últimos dias, você não teve motivo para voltar
    à cozinha desde que chegou ao hotel. Esta noite você descobre que não está nada parecido
    com quando você a encontrou pela primeira vez."

    play sound "sfx/faucet.ogg"
    "O silêncio, o fedor terrível, utensílios espalhados, manchas de comida que haviam se decomposto décadas
    atrás e, é claro,{w=0.2} o revólver em cima do balcão,{w=0.2} tudo foi substituído."

    "Agora, equipamento limpo de aço inoxidável, os sons de [first_guest] lavando a louça e
    o aroma da comida deliciosa que ele preparou enchem o cômodo."

    "\"Deve ser obra da lareira\", você pensa para si mesmo. Mas será que a lareira sozinha
    teria reunido todas essas pessoas?{w} Você se alegra em um pequeno momento de orgulho, observando (e cheirando)
    o que conquistou."

    "O minotauro e o gerente conversam enquanto lavam a louça. Eles não ouvem seus
    passos se aproximando."

    "[first_guest] desvia para um curto desabafo sobre o que aconteceu mais cedo,
    mas Astério muda de assunto antes de pegar uma pilha de pratos limpos."

    "No caminho para o armário, ele passa brevemente pela porta da câmara fria.
    Ele congela, estremece e solta uma tosse nervosa."

    play sound "sfx/clink.ogg"
    "Depois de guardar os pratos, Astério se vira e apenas então percebe sua presença."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("leftarm", "loose")
    $Asterion.change ("rightarm", "hips")
    $Luke.change ("arm","hip")
    $Luke.change("emotion", "laughing")
    $Kota.change("emotion", 'laughing')
    $Kota.change("rightarm", "mug")

    show Asterion:
        xalign 0.1 yalign 1.0
    if first_guest == "Luke":
        show Luke:
            xzoom 1 xalign 0.9 yalign 1.0
        with Dissolve (1.0)
    else:
        show Kota:
            xzoom -1 xalign 0.9 yalign 1.0
        with Dissolve (1.0)

    pause 1.5

    you "Astério."

    $Kota.change("emotion", 'neutral')
    $Luke.change("emotion", 'neutral')
    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "raised")

    asterion "Sim?"

    you "Não quer passar um tempo com os hóspedes? Você esteve aqui a noite toda."

    $Asterion.change ("emotion", "contemplative")

    asterion "Ah, você não deve se preocupar comigo. Está tudo bem, o conforto dos hóspedes vem primeiro."

    asterion "Este é o meu dever, afinal."

    you "Mas todos já comeram, estão só conversando agora. Você podia
    sentar e aproveitar a companhia por um tempo."

    $Asterion.change ("leftarm", "loose")

    show Asterion:
        ease 1.0 xalign 0.2
    pause 1.0
    show Asterion:
        ease 1.0 xalign 0.1

    "O minotauro anda ao redor e observa por cima de seu ombro, tendo um vislumbre de toda a comoção
    no outro cômodo."

    if Chapter4_Terrorized_Asterion == "False":
        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")
        "A orelha dele sacode para captar as vozes e ele morde o lábio inferior para conter um sorriso."
        asterion "Ah, você é gentil,{w=0.3} mas eu não deveria deixar [first_guest] aqui lavando a louça sozinho."
    else:
        $Asterion.change ("emotion", "tired")
        "Seu lábio inferior treme. As narinas dilatam a cada expiração e sua orelha intacta
        sacode como se estivesse eletrizada."
        asterion "Ah...{w=0.2} Eu estou bem aqui. O s-{w=0.2}senhor [first_guest] ainda está
        trabalhando e eu não posso deixá-lo."

    if first_guest == "Luke":
        pause 0.5
        $Luke.change ("emotion","laughing")
        "Luke gargalha ruidosamente com a observação de Astério."
        $Luke.change ("arm","pointing")
        show Luke:
            ease 1.0 xalign 0.8
        luke "Angus, cala a boca, porra, são só alguns pratos. Eu me viro."
        show Luke behind Asterion
        $Luke.change ("arm","hip")
        $Asterion.change ("emotion", "smiling")
        asterion "O-obrigado, {w=0.5} Luke,{w=0.5} mas eu insi...{nw}"

        $Asterion.change ("emotion", "surprise")
        show Luke:
            linear 0.5 xalign 0.5
        pause 0.5
        show Luke:
            linear 1.0 xalign 0.9
        "Luke se vira e dá um tapa no traseiro de Astério com uma garra ensaboada, deixando uma pequena marca de mão
        molhada e um pouco de espuma na bunda do minotauro."
        $Luke.change ("emotion","wink")
        luke "{i}Eu{/i} insisto. Vai se divertir."
        $Asterion.change ("emotion", "sad")
        pause 1.5
        $Asterion.change ("emotion", "smiling")
        "Astério parece um pouco envergonhado enquanto limpa a obra de Luke, mas apenas por um momento."

    else:
        $Kota.change ("emotion", "puzzled")
        "Kota bufa com a observação."

        $Asterion.change ("rightarm", "loose")

        you "Entendo. Sendo assim, com licença, Kota. Se importa se eu roubar Astério
        de você por alguns minutos?"

        $Kota.change ("emotion", "neutral")

        kota "Estou quase terminando aqui e não estamos recebendo mais pedidos. Vá em frente, Astério, divirta-se."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")

        asterion "Tem certeza? Posso ficar um pouco mais,{w=0.2} não é nenhum problema."

        $Kota.change ("emotion", "laughing")

        kota "Não será necessário."

        you "Vamos lá, eu não vou desistir dessa. Nós dois sabemos que você quer sair e conhecer todo mundo.{w}
        Não me faça te dar ordens."

    if Chapter4_Terrorized_Asterion == "False":

        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("emotion", "laughing")

        asterion "Muito bem. Se o Mestre então insiste,{w=0.2} com pesar,{w=0.2} devo obedecer.{w}
        Mas você me permitiria alguns minutos para jantar primeiro?"
        $Asterion.change ("emotion", "contemplative")
    else:
        $Asterion.change ("emotion", "sad")
        asterion "Is-{w=0.2}isto não será necessário, eu ob-{w=0.2}obedecerei. Seja qual for sua vontade."
        asterion "Ainda assim, poderia me dar alguns minutos para jantar primeiro?"
        $Asterion.change ("emotion", "neutral")

    if first_guest == "Luke":
        show Luke:
            ease 3.0 xalign 2.0
    else:
        show Kota:
            ease 3.0 xalign 2.0
    show Asterion:
        ease 3.0 xalign 0.5

    play sound "sfx/dishes.ogg"
    "Vocês dois se afastam de [first_guest] e o deixam com sua tarefa."

    pause 2.0

    if Chapter4_Terrorized_Asterion == "False":
        you "Você não comeu? Tudo bem, é claro que você pode jantar."

        you "Mas você poderia trazer sua comida para a mesa e comer com os outros."

        you "Você decide. Eu sei que você prefere comer sozinho,{w=0.2} mas...{w=0.5} se demorar muito,
        os hóspedes podem acabar voltando para os quartos."
        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")
        pause 1.0

        asterion "Ora, este é um verdadeiro dilema, Mestre [player_name]. Quão impróprio de minha parte
        seria comer ao lado de outras pessoas..."

        asterion "No entanto,{w=0.3} seria ainda mais rude me esconder."

        $Asterion.change ("emotion", "smiling")

        asterion "Muito bem, você me convenceu."

        you "Excelente. Então é isso!{w=0.3} Agora, o que você acha de dar um passo adiante e tomar uma bebida?"

        $Asterion.change ("emotion", "contemplative")

        you "É uma noite especial, o hotel está reabrindo! Não vamos meditar nas palavras,
        você não diria que a ocasião pede um pouco de vinho?"

        "Ele pega um par de taças do armário antes de você terminar de falar."

        asterion "Você nunca vai me encontrar rejeitando uma bebida."

        asterion "No entanto, devo dizer:{w=0.2} hoje você está revelando uma grande lábia.
        Não é sempre que me deixo persuadir a cumprir tarefas tão intimidadoras."

        you "O que eu posso dizer?{w=0.2} É esperado que eu coloque você para trabalhar, não é?{w} Só estou cumprindo o meu dever."

        "Astério pega seu prato e uma garrafa de vinho."

        asterion "Que senhor devoto. Os deuses teriam dificuldade para encontrar outro Mestre tão leal quanto você."

    else:
        you "Você não comeu? Seria melhor se você trouxesse comida para a mesa com você,
        coma com os outros. Se perdermos mais tempo, eles irão para os quartos."

        $Asterion.change ("emotion", "sad")

        pause 2.0
        $Asterion.change ("emotion", "tired")

        pause 1.0
        asterion "Tudo bem."

        you "Excelente. Então é isso!{w=0.3} Agora, o que você acha de dar um passo adiante e tomar uma bebida?"

        $Asterion.change ("emotion", "neutral")

        you "É uma noite especial, o hotel está reabrindo! Não vamos meditar nas palavras,
        você não diria que a ocasião pede um pouco de vinho?"

        "Antes que você termine de falar, ele já está pegando um par de taças."

        asterion "Sim... uma bebida agora acalmaria bastante meus nervos."

        you "Isso seria bom. Você parece bem tenso, tem algo errado?"

        asterion "...N-não. Ficarei bem, Mestre. Vamos."

    scene Lounge
    with Dissolve (1.0)

    if first_guest == "Luke":
        if first_guest == "Luke":
            show LoungeLight
            with Dissolve (0.5)
        show Asterion behind LoungeLight:
            xalign -1.0 yalign 1.0
            ease 3.0 xalign 0.5
    else:
        show Asterion:
            xalign 2.0 yalign 1.0
            ease 3.0 xalign 0.5

    "Com comida e bebida em mãos, vocês dois retornam para o salão.
    Cabeças viram em sua direção e a conversa morre quando a presença de Astério faz os
    hóspedes perderem a linha de pensamento."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    #Asterion's expression shifts. He's trying to look cheerful
    show Asterion:
        ease 2.0 xalign 0.4 yalign 2.0

    "Vocês dois sentam em lugares na ponta da mesa — perto o suficiente para funcionar como convite ao
    casal de caroneiros, mas não tão perto a ponto de forçá-los a conversar."

    "O minotauro não perde tempo servindo uma taça de vinho abundante, primeiro a você e depois para si mesmo."

    you "Um brinde.{w=0.2} Ao hotel."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")

    asterion "Ao nosso senhor mais magnânimo."

    you "Ao nosso trabalhador e{w=0.2} implacável zelador."

    $Asterion.change ("emotion", "smiling")

    asterion "Ao Imperador [player_name],{w=0.2} que seu reinado seja eterno."

    you "Agora você está só se divertindo."

    $Asterion.change ("emotion", "contemplative")

    asterion "Posso estar.{w=0.2} Isto é algo que o Mestre desaprova?"

    you "Eu não entraria na brincadeira se desaprovasse."

    "Astério bebe o vinho. Seu pomo de adão balança com cada um de seus goles até que a
    taça tenha apenas uma película transparente de roxo."

    "Ele dá uma boa olhada e balança a última gota de vinho antes de encher a taça novamente."

    asterion "Não estou ultrapassando os limites?{w=0.2} Hoje tem sido um dia tão adorável,
    mas admito que estive... esquecendo meu lugar."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    you "Você não precisa ser tão formal,{w=0.2} está tudo bem.{w} O que tem de errado em soltar uma piada de vez em quando?"

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "raised")

    asterion "Talvez não haja nada prejudicial,{w=0.2} mas alguns diriam que quebrar a
    hierarquia é sempre repreensível."

    $Asterion.change ("emotion", "sad")
    $Asterion.change ("leftarm", "loose")

    asterion "Nem sempre eu...{w=0.2} me permiti conversar com um Mestre de tal maneira."

    $Asterion.change ("emotion", "neutral")

    asterion "O senhor e eu não tínhamos que interagir tanto."

    you "Sério?{w=0.2} Com você e eu compartilhando e vivendo no mesmo espaço,{w=0.2}
    eu esperaria que fosse um relacionamento bem próximo."

    pause 1.0

    #note: if Asterion likes the MC enough he realizes he doesn't want to bring up sad topics at this moment.
    #That's why, this time around, the high affection branch is shorter

    if global_affection >= 4:
        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        asterion "O Mestre me permitiria falar o que penso?"

        you "Você nem precisa pedir."

        asterion "Muito bem:{w=0.3} melhor não falarmos sobre os Mestres de antigamente. Temos uma noite
        alegre pela frente,{w=0.2} e espero que muitas mais venham no futuro."

        asterion "Além disso, pelo pouco que captei, parece que o mundo mudou bastante
        nas últimas décadas. Não apenas o mundo {w=0.2}— as pessoas também."
    else:
        $Asterion.change ("emotion", "neutral")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        asterion "Desde a fundação do hotel, a chegada de um novo Mestre sempre foi uma situação
        muito profissional. Ninguém precisava...{w=0.2}me ajudar da maneira como você fez."

        asterion "Na verdade, costumávamos ter uma cerimônia bastante pomposa."

        asterion "Tratava-se mais sobre tornar-se o senhor do hotel que tornar-se meu senhor.
        Eu ficava em segundo plano."

        $Asterion.change ("rightarm", "hips")

        asterion "Presumindo que tudo corresse bem e o Mestre tivesse uma inclinação piedosa,
        eu ficaria calmamente sob seu comando."

        asterion "E depois que tudo fosse dito e feito, eles não precisavam e nem me queriam como companhia.{w}
        Sou um servo, afinal."

        asterion "Quanto menos eles me notassem, melhor — significava que eu estava fazendo bem meu trabalho."

        asterion "Então...{w=0.2} frequentemente costumávamos não trocar mais do que algumas palavras por dia."

        pause 1.0

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        asterion "Mas parece que o mundo e sua população mudaram muito nas últimas décadas."

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    you "Sim, é verdade. Nós temos um monte de tecnologias novas e talvez nós,{w=0.2}
    as pessoas,{w=0.2} tenhamos mudado também."

    if player_background == "humanities":
        #if the player has the Humanities background he either goes down this path or has the option to go,
        #by picking a well-marked option

        you "Você já ouviu falar dos \"direitos humanos\"? É um assunto que alguém já trouxe aqui para o hotel?"

        asterion "Direitos? {w=0.2}Este é um assunto que já ouvi de alguns hóspedes.
        Mas não sou nenhum estudante da lei, é claro."

        asterion "Direitos humanos, no entanto...{w=0.5} Receio nunca ter ouvido a expressão."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        you "São os direitos aos quais somos intitulados porque somos humanos.
        Eles não podem ser revogados, é o que chamamos de \"inalienáveis\"."

        you "Eles não são absolutos, veja bem. {w=0.2}Existem limites. Mas mesmo que você
        tenha feito algo errado, tem direito a eles. Simples assim."

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "loose")

        asterion "Mas, meu senhor...{w=0.2} Eu não sou humano.{w} Sou um híbrido."

        $Asterion.change ("emotion", "neutral")

        you "Isso torna você {i}no mínimo{/i} meio-humano, e isso é de longe o suficiente.
        Além disso, não se trata de sangue, mas da condição humana. O espírito humano."

        $Asterion.change ("emotion", "contemplative")

        you "Você é humano, Astério. E você tem direitos.{w=0.2} Você tem direito à dignidade,
        a ser tratado com respeito e ter suas necessidades atendidas."

        $Asterion.change ("emotion", "sad")

        asterion "Mesmo que eu tenha sido preso por um crime que realmente cometi?"

        you "Ser um preso significa que alguns dos seus direitos são restritos, mas
        não se trata de passar você por um triturador. Não é a coisa certa a se fazer, doa a quem doer."

        you "Aliás, qual foi o seu crime mesmo?{w=0.5} Mansidão?"

        asterion "Sim.{w=0.2} Permiti que meu assassino tirasse minha vida."

        you "Isto não é um crime. Não conheço os detalhes do que aconteceu,{w=0.2}
        mas não importa o que digam, isso não é um crime."

        you "Tudo pelo o que você passou, não está certo."

        pause 1.0

        $Asterion.change ("emotion", "bowing")

        asterion "Muitas vezes me pareceu, ao longo dos séculos, que as leis da humanidade são muito
        mais piedosas que as dos deuses."

        $Asterion.change ("emotion", "contemplative")

        asterion "Ah...{w=0.2} Eu não sei o que dizer."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        asterion "Você acredita que eu sou humano?"

        you "Sim. É claro. Por que não seria? Você é metade touro, mas humanidade
        vai muito além da aparência."

        you "É sobre quem você é lá no fundo. Não tenho dúvidas em mim de que você {i}é{/i} humano,
        talvez mais do que a maioria."

        $Asterion.change ("emotion", "contemplative")

        asterion "Você tem ideias muito ousadas, Mestre [player_name].
        Do tipo que faz o coração bater mais forte."

        "Ele toma um gole de vinho."

        $Asterion.change ("emotion", "smiling")

        asterion "Você diz palavras muito doces."

        $Asterion.change ("emotion", "contemplative")

        asterion "Ah, não entenda isto como uma piada.{w} Apenas...{w=0.2} me faltam palavras."

        asterion "Às vezes, ideias criam raízes em mim e eu me apego a elas até doer no peito e garganta."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "loose")

        asterion "...Não sei o que dizer. {w=0.2}Por favor, perdoe minha trapalhada."

        pause 1.0

        asterion "Não... imagino o que dirá, mas você responderia uma pergunta boba sobre
        este{w=0.2} companheiro humano?"

        you "É claro. E você não precisa pedir permissão."

        asterion "Ah,{w=0.2} Eu sei. Mas hoje...{w=0.2} suponho que esta festa, a cerimônia,
        me parece de alguma forma divertida.{w} Bem, sobre minha pergunta."

        $Asterion.change ("emotion", "smiling")

        asterion "Existe um direito humano sobre ter um lar?"

        you "Sim.{w=0.2} Existe uma coisa chamada Declaração Universal dos Direitos Humanos,{w=0.2}
        Tenho certeza que existe um artigo falando sobre moradia."

        you "Também existe o direito de ter uma nacionalidade, pertencer a um país.
        Esta também é uma maneira de se ter um lar, de certo modo."

        you "Esse assunto te interessa?{w} Desculpe se eu estou divagando."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        asterion "Sim, me interessa... Como você não imaginaria."

        you "Posso tentar mostrar a você algumas coisas sobre as Nações Unidas e a Declaração dos Direitos Humanos.
        É uma coisa legal que surgiu depois da Segunda Guerra Mundial."

        you "Que tal isso? Outra hora podemos passar uma noite inteira
        falando sobre isso, se você quiser."

        $Asterion.change ("emotion", "smiling")

        asterion "Parece ótimo, se não for nenhum problema."

        you "Poderia ser uma noite divertida.{w=0.3} Eu posso continuar falando sobre isso por horas e horas...
        Só vou precisar de uma conexão com a internet para mostrar tudo a você."

        "Mas parece que suas palavras caem em ouvidos surdos. O minotauro foi fisgado por outra ideia,
        resmungando para si mesmo."

        $Asterion.change ("emotion", "contemplative")

        asterion "Haha... Eu, um humano..."

        #flag for Asterion knowing about the UN is set to True

        #end Humanities dialogue here#

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    you "Não te contei sobre a internet, contei?"

    asterion "Receio que não. Pelo menos...{w=0.2} eu não reconheço o nome."

    you "Ah, a internet é uma das tecnologias que mais mudaram vidas no século XX.
    É realmente impressionante quando você pensa sobre isso."

    you "Você conhece o rádio, não é?"

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "loose")

    asterion "Sim.{w=0.2} Fazê-lo funcionar aqui foi um desafio, mas valeu a pena.{w} Todas as músicas..."

    you "Com um rádio, você pode ouvir o que as pessoas estão enviando à distância.
    A internet é assim, mas muito mais poderosa."

    you "Você pode conectar uma máquina a ela e isso permite {i}enviar e receber{/i}
    informação. Não é ótimo?"

    $Asterion.change ("emotion", "neutral")

    asterion "O que você quer dizer com informação?"

    you "Bem... conhecimento, por exemplo. Você pode enviar e receber mensagens em segundos, é tão rápido."

    you "Uma carta demoraria semanas para chegar ao seu destino, mas com a Internet leva segundos."

    $Asterion.change ("emotion", "surprise")

    you "Mas pode fazer muito mais. Você pode obter livros, ver imagens,
    ouvir músicas, até mesmo assistir a filmes em segundos."

    you "Você precisou esperar para os livros chegarem ao hotel, certo?{w}
    Com a internet, você pode simplesmente escolher o que deseja e começar a ler em sua máquina em segundos."

    you "E, ao contrário do rádio, você pode fazer suas próprias coisas e enviar para a web de forma que outras pessoas também desfrutem."

    you "Hoje em dia, temos até o que chamamos de \"impressoras 3D.\"{w}
    Você pode,{w=0.2} digamos,{w=0.2} encontrar a informação de uma pulseira e imprimir ela com a máquina."

    $Asterion.change ("emotion", "neutral")

    if player_background == 'humanities':
        you "Quando tivermos a internet funcionando, posso mostrar a você tudo sobre os direitos humanos.
        Pode ser um assunto um pouco nerd, mas...{w=0.2} Espero que você goste."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        asterion "Sim...{w=0.2} Eu adoraria isto. Parece que a humanidade esteve muito
        ocupada durante as últimas décadas."

    elif  player_background == 'tech':
        you "Caramba, novas disciplinas inteiras surgiram graças à internet e aos computadores."

        you "Você sabe como o rádio funciona, mais ou menos?{w=0.2} Alguém envia uma transmissão que
        uma ou mais pessoas podem captar, certo?"

        "Astério acena com a cabeça."

        you "Bem, a internet é um pouco mais complicada."

        you "Você insere um IP, que é meio como a frequência de rádio da estação que você
        sintoniza, e isto o conecta a um servidor{w=0.2} — que é um computador
        diferente em uma outra parte do mundo."

        you "E este computador pode conter uma página da web ou serviço que permite fazer coisas como navegar no
        conteúdo da internet, baixar arquivos, enviar ou receber mensagens..."

        you "Então, além de, você sabe, \"operador de rádio\" e \"cara no microfone\", existe todo
        um mundo de empregos envolvendo a internet."

        you "De pessoas que estabelecem as conexões físicas a provedores de serviço de internet
        que mantém servidores, a pessoas que criam os programas necessários para navegar na internet..."

        $Asterion.change ("emotion", "tired")

        you "...e as pessoas que fazem páginas da web para você acessar o conteúdo, as pessoas que fazem
        {i}conteúdo{/i} para estas páginas..."

        you "...cientistas de dados que medem as estatísticas sobre quem está visitando o que e em que momento
        é melhor vender os dados de anúncio..."

        you "...existem até mesmo pessoas interdisciplinares cujo trabalho é arquitetar páginas da web
        que pareçam mais bonitas e atraiam mais clientes, e advogados que garantam que tais páginas cumpram as leis de direitos autorais."

        you "Revolucionou o mercado de trabalho e a forma como as pessoas trabalham. Caramba, as pessoas encontram trabalhos
        na internet com mais frequência do que nunca a essa altura."

        pause 1.0

        you "Está acompanhando?"

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "hips")
        pause 1.0

        you "Ah, foi mal. Acho que fui um pouco rápido demais, não é?{w} Sou meio apaixonado por isso."

        $Asterion.change ("emotion", "neutral")

        asterion "N-não. Bem,{w=0.2} eu não compreendo muito disso..."
        asterion "Mas você é muito apaixonado por isso, posso notar."

    elif  player_background == 'math':
        you "Sabe de outra coisa para qual a internet é muito boa?{w} Compartilhar conhecimento."

        you "Hoje em dia você pode assistir a aulas online, cara a cara com um professor do outro lado do mundo."

        you "Caramba, às vezes você nem precisa assistir a uma aula,
        existem cursos que permitem que você aprenda todos os tipos de habilidades sozinho."

        you "Ou, digamos que você precisa de ajuda resolvendo um problema. Existem fóruns com grupos de pessoas,
        {w=0.2} algumas delas especialistas em seus campos,{w=0.2} dispostos a lhe dar conselhos."

        you "Colocar um eletrodoméstico para funcionar, aprender novos idiomas, conseguir ajuda com os estudos..."

        $Asterion.change ("emotion", "surprise")

        you "Até coisas mundanas, como conselhos sobre relacionamentos e sexo.{w}
        Existem grupos para qualquer coisa hoje em dia."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        asterion "Ah.{w=0.2} Algumas coisas nunca mudam, eu suponho."

        you "O que você quer dizer?"

        asterion "Como posso dizer...{w=0.2} Na época em que eu trabalhava com a equipe da cozinha...{w=0.2}
        digamos que eles tinham muito poucos limites quando se tratava de conversa."

        $Asterion.change ("emotion", "neutral")
        $Asterion.change ("rightarm", "loose")

        asterion "É uma coisa muito humana, suponho...{w=0.2} Digo, conversar sobre sexo."

        pause 1.0

        $Asterion.change ("emotion", "tired")

        pause 1.0

        you "Algum problema?"

        $Asterion.change ("emotion", "sad")

        asterion "Um pensamento apenas passou por minha cabeça...{w=0.2} você mencionou que a internet possui aulas."

        "Suas orelhas ficam vermelhas e se contraem enquanto ele pensa em como dizer o que quer dizer."

        asterion "É...{w=0.2} meu senhor, perdoe-me se isto é inapropriado..."

        asterion "As pessoas têm aulas sobre sexo na internet?"
        show Asterion:
            linear 4.0 xalign 0.38 yalign 3.0

        "Ao mesmo tempo que as palavras saem de sua boca, o minotauro encolhe os ombros e afunda em seu assento."

        "Você pode apenas captar uma rítmica batida de um de seus cascos batendo contra o chão."

        you "Aulas? Bem, eu não diria que é o caso, não. Seria muito estranho."

        you "Mas existe muita coisa sobre sexo lá. Vai além de grupos que falam sobre isso,
        existe toda uma indústria para..."

        $Asterion.change ("emotion", "surprise")
        "Isto não pode acabar bem. Astério está muito envergonhado para continuar."

        $Asterion.change ("emotion", "sad")
        you "...Sabe de uma coisa, esqueça o sexo. Parece que perdemos o fio da meada do assunto original."
        you "O que importa é que a internet é ótima, você pode fazer aulas e encontrar pessoas que pensam como você."

        pause 1.0

        show Asterion:
            linear 2.0 xalign 0.4 yalign 2.0

        $Asterion.change ("leftarm", "raised")

        asterion "O-{w=0.2}obrigado."
        you "De nada, amigo."

    elif  player_background == 'leader':
        you "A internet também mudou a maneira como as pessoas interagem umas com as outras."

        you "Já que você pode enviar mensagens, fotos e vídeos instantaneamente para amigos,
        família e conhecidos, estar longe das pessoas não é mais um fator limitante."

        you "Você sabe o que é, ahm...{w=0.2} pen-pal, certo, Astério?"

        $Asterion.change ("emotion", "laughing")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "raised")

        asterion "Sim, tenho familiaridade com o conceito! Agora, isto me traz de volta..."

        $Asterion.change ("emotion", "contemplative")

        asterion "Pode soar bobo para você, mas naquela época era chamado de \"amigo por correspondência\",
        e quando ouvi pela primeira vez um hóspede britânico dizer \"pen-pal\" em vez disso nos anos 30...
        Achei histérico."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        you "Bem, isso não existe mais, pelo menos não como costumava ser. Em certo sentido,{w=0.2}
        as pessoas ainda mantêm amizades de longa distância."

        you "Mas a comunicação é instantânea, então acredito que a natureza das mensagens não é exatamente a mesma."

        you "Você tinha um \"amigo por correspondência\"?"

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        asterion "Não...{w=0.2} Receio que não. Pensei sobre isso algumas vezes, enquanto organizava as correspondências do hotel."

        asterion "Talvez eu tivesse gostado, mas...{w=0.2} disse a mim mesmo que não tinha tempo para isso."

        asterion "Mas quando tinha, inventava outra desculpa...{w}
        Suponho que estava {w=0.2}com vergonha, {w=0.2}acima de tudo."

        $Asterion.change ("emotion", "smiling")

        you "Com vergonha de que, caso não se importe que eu pergunte?"

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "loose")

        asterion "Hum...{w=0.2} seria estranho falar sobre minha vida,{w=0.2}
        caso meu amigo por correspondência alguma vez perguntasse sobre isto."

        asterion "Seria mais prudente mentir, não é?{w} Inventar uma história sobre mim."

        asterion "Mas então não parecia valer a pena o esforço.{w=0.2} E também era difícil ensinar
        ao hotel como enviar cartas em primeiro lugar."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")

        asterion "Já troquei correspondências com hóspedes antigos, aqui e ali.{w}
        Mas não fiz disto um hábito."

        pause 1.0

        $Asterion.change ("emotion", "contemplative")

        asterion "Essa coisa de internet...{w=0.2} Gosto do que você está me contando até agora.
        Parece que seria útil utilizá-la para fazer amizades."

        you "Sim, é ótima para conhecer pessoas que pensam como você.{w=0.2} E não para por aí."

        $Asterion.change ("emotion", "smiling")

        you "Também existe uma coisa chamada rede social,{w=0.2}
        mas acho melhor ir com calma.{w} Não quero sobrecarregar você."

        asterion "Eu agradeço, Mestre."

    elif  player_background == 'arts':
        $Asterion.change ("emotion", "neutral")

        you "Diga, você gosta de arte? O hotel já teve algum tipo de museu?"

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        asterion "Receio que raramente fomos agraciados com muitas obras de arte ao longo dos anos."

        asterion "Aqui e ali, um mestre favorecia um artista e tornava-se seu patrocinador.
        Mas isto não significa que as obras ficavam aqui, muitas vezes foram vendidas."

        $Asterion.change ("emotion", "smiling")

        asterion "O que temos de fato são coisas que os hóspedes deixaram para trás como prova de gratidão, na maior parte."

        you "Você diria que gosta? Já teve a curiosidade de ver o que está sendo produzido?"

        $Asterion.change ("emotion", "contemplative")

        asterion "Certamente!{w=0.2} Para ser sincero, sempre tive a curiosidade de saber como
        anda o mundo lá fora..."

        asterion "Conversamos sobre Notre Dame, sim? Ouvi tantas histórias sobre isto, e tantos outros lugares..."

        asterion "Se eu pudesse ao menos ver essas obras de arte das quais tanto ouvi falar, por um único dia..."

        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "loose")

        you "Você terá esse desejo atendido, então. E se você gosta de arte, então será o seu sonho realizado."

        pause 1.0

        $Asterion.change ("emotion", "sad")

        pause 1.0

        asterion "Desculpe, mas...{w=0.2} o-o que?"

        you "Sim! {w=0.2} Você quer saber como anda o mundo lá fora, não é?"

        you "Ver arte, as cidades, os países? A internet é ótima para isso."

        $Asterion.change ("emotion", "neutral")

        you "Nos séculos passados, a única maneira de testemunhar a arte por conta própria seria viajando,
        seja para uma igreja ou para a propriedade de um patrono rico."

        you "Como você pode imaginar, simplesmente viajar para qualquer lugar era uma atividade cara, demorada e muitas vezes perigosa."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        you "Mas com a internet você pode ver fotos, assistir vídeos e escutar músicas quase que instantaneamente."

        you "Hoje em dia existem museus que disponibilizam a totalidade de seus acervos
        gratuitamente online. Se estivermos conectados, estaremos apenas a alguns minutos de
        testemunhar qualquer obra de arte que quisermos."

        show Asterion:
            ease 0.5 xalign 0.45
        pause 0.5
        show Asterion:
            ease 0.5 xalign 0.4

        "Conforme você fala, não pode deixar de notar Astério inquieto.
        Suas orelhas tremem e contraem, seu olhar brevemente fixa-se em você e segue o seu, como se estivesse encantado."

        "Sua cauda, também, balança para frente e para trás, como se estivesse eletrizada.
        A boca do minotauro fica aberta enquanto ele luta para encontrar palavras."

        asterion "Isso...{w=0.2} isso parece maravilhoso.{w} Ah, Mestre..."

        asterion "Essa coisa de internet... parece que eu poderia testemunhar o mundo inteiro, pelo que você está me dizendo."

        you "Você meio que pode!"

        you "Para ser justo, ainda existe uma magia única em ver uma obra de arte pessoalmente.{w}
        Ver a foto de uma obra e ver a verdadeira sempre serão experiências diferentes."

        you "As pinceladas, por exemplo...{w=0.2} não são transmitidas muito bem em uma imagem.
        Há uma sensação de espanto em ver você mesmo uma pintura impressionante."

        you "Apesar de tudo...{w=0.2} a internet tornou a cultura amplamente livre e abertamente acessível."

        you "Agora, mesmo se uma pintura é destruída — digamos, queimada em um incêndio —
        ela ainda pode ser preservada para sempre como informação para as gerações futuras."

        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        "Por mais bem-intencionado que você possa ter sido, o minotauro parece perdido no labirinto de sua própria mente
        — e as ideias que se escondem em sua cabeça não parecem tão agradáveis."

        show Asterion:
            ease 2.0 xalign 0.36

        "Ele morde os lábios, balança o rabo e, pela tensão em seu braço você pode adivinhar que ele está cravando
        as unhas no joelho."

        you "Algum problema?{w=0.2} Você parece um pouco angustiado."

        show Asterion:
            ease 0.8 xalign 0.4

        "Ele salta de volta à realidade com um bufo indigno, mas ainda assim seus lábios permanecem selados."

        $Asterion.change ("emotion", "sad")

        pause 2.0

        $Asterion.change ("emotion", "bowing")
        $Asterion.change ("leftarm", "raised")

        asterion "Mestre...{w=0.2} é inapropriado para mim fazer um pedido, mas mesmo assim..."

        $Asterion.change ("emotion", "sad")

        asterion "...você me ensinaria como usar essa internet?"

        $Asterion.change ("emotion", "contemplative")

        you "Não precisa ficar tão sério!{w=0.2} É claro que eu vou te ensinar, assim você pode ver tudo o que quiser."

        you "Você poderia ver o mundo sem sair do hotel."

    elif  player_background == 'speedrunner':

        $Asterion.change ("emotion", "neutral")

        you "A internet virou uma daquelas coisas como a prensa móvel onde você simplesmente
        não consegue imaginar a vida sem ela, sabe?"

        you "Para todos os efeitos, a internet é a principal fonte de entretenimento
        de todos a essa altura."

        you "Como eu disse, qualquer filme, livro, pintura, álbum de música que você consegue pensar?{w=0.2}
        Está bem ali, a alguns cliques de distância."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")

        asterion "Isto é fascinante. Filmes são demais, não são?
        Certa vez, recebemos um frequente hóspede francês que conhecia um projecionista o qual lhe devia dinheiro."

        asterion "Cada vez que ele voltava para o hotel, trazia novos rolos de filme com ele,
        nós os assistíamos no salão. Era maravilhoso."

        asterion "Acredito que ainda temos alguns rolos escondidos em algum lugar,{w=0.5}
        Mestre Clément adorava The Miracle Man de Lon Chaney {w=0.5} e tinha a réplica do hotel.{nw}"

        $Asterion.change ("emotion", "neutral")
        $Asterion.change ("rightarm", "loose")

        you "Claro, mas ainda nem chegamos na melhor parte, Astério!
        Agora existem pessoas produzindo conteúdo exclusivamente para a internet."

        you "Eles têm a coragem de abordar assuntos de nicho que a mídia tradicional nunca teria investigado."

        you "Como vídeos-ensaio sobre a profunda emocionalidade nos últimos filmes de super-heróis,
        ou diários de vídeo onde eles perturbam os solos há muito tempo intocados de culturas estrangeiras..."

        you "...ou mashups que misturam aberturas de moe anime com bandas norueguesas de black metal screamo,
        ou vídeos que narram dramas entre críticos de videogame que podem ou não ter abusado mentalmente uns dos outros..."

        you "Eu posso assistir aquela merda o dia todo."

        asterion "..."

        "O minotauro balança a cabeça e tenta sorrir."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")

        asterion "Isso... parece muito interessante, Mestre.{w} Mesmo que eu não tenha contexto algum
        para entender o que você está falando."

        you "Ah, confie em mim,{w=0.2} depois de um mês ou mais assistindo essas coisas, você fica em dia."

        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "loose")

        "O olhar de Astério fica em branco e sem foco enquanto ele contempla a quantidade de tempo precioso
        que será forçado a desperdiçar nesses próximos meses."

        "Ele se conforta pensando, claro, é melhor que ser trancado em uma despensa por
        setenta anos...{w=0.2} mas {i}quão{/i} melhor?"

        "\"Apenas aguente\", Astério pensa consigo mesmo.{w} \"Esconda sua expressão e aguente.\""

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "A internet parece de fato animadora, meu senhor. Mas...{w=0.2}
    como a trazemos aqui? Como funciona?"

    you "Boa pergunta.{w=0.2} Você mencionou que o Hotel costumava receber sinais de rádio, certo?"

    you "Como isso foi feito naquela época? Se você consegue um sinal de rádio aqui,
    então certamente podemos encontrar uma maneira de nos conectar à internet."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "loose")

    asterion "Ah,{w=0.2} isto."

    asterion "Foi uma situação... desafiadora, embora direta ao ponto.
    Nós reaproveitamos uma antiga {i}peça de equipamento.{/i}"

    asterion "É uma coisa velha, que remonta à época em que o domínio foi criado.
    Os Mestres a usaram para comunicar-se com o mundo exterior."

    $Asterion.change ("emotion", "neutral")

    asterion "Antes do rádio, era utilizada para enviar e receber cartas e, antes disso,
    como uma espécie de doca. Nós a reaproveitamos para uma série de tarefas ao longo dos séculos."

    you "Ah, isso é interessante. Como é essa máquina? Como ela funciona?"

    $Asterion.change ("emotion", "tired")

    asterion "Hum...{w=0.2}não é uma máquina. É mais...{w=0.2} uma coisa que os deuses deixaram para trás,
    talvez não percebendo o quão extensivamente poderia ser reaproveitada."

    $Asterion.change ("emotion", "neutral")

    asterion "Se essa \"Internet\" for parecida com o rádio, então tenho esperança de que possa funcionar."

    "A poucos metros de você, os rapazes do Oriente Médio explodem em gargalhadas.{w=0.2}
    Um deles se encolhe, envergonhado. Parece que há algum tipo de piada interna entre eles."

    $Asterion.change ("emotion", "surprise")
    $LoungeBlobs[0] = True

    if first_guest == 'Luke':
        play sound "sfx/clink.ogg"
        "Você ouve o som de vidro quebrando perto do bar. Ninguém parece reagir a isto,
        mas o {w=0.2}\"Porra!\"{w=0.2} de Luke provoca mais uma rodada de risos dos hóspedes."

        "Os trabalhadores sul-americanos, sentados ao lado do bar, olham incrédulos enquanto o
        grifo varre os cacos de vidro com os pés descalços, não dando a mínima, para um canto
        longe de qualquer lugar que os hóspedes possam passar."

        "Conforme Luke caminha para a parte de trás do bar (para,{w=0.2} você espera,{w=0.2} pegar uma vassoura de verdade
        e limpar a bagunça), ele pisca e faz arminhas com os dedos na direção dos homens antes de desaparecer para a cozinha."
    else:
        "Kota faz uma aparição e seu grande corpo flui ao redor da mesa enquanto
        ele enche os copos e recolhe os pratos vazios com uma reverência servil e um sorriso."

        play sound "sfx/clink.ogg"
        "A conversa morre onde o dragão vai, depois recomeça em murmúrios abafados e animados;
        pelo menos até sua mão escorregar e um copo cair no chão."

        "A expressão de horror em seu rosto vermelho corta a tensão como uma faca e os
        hóspedes gargalham e sorriem acenando para longe as desculpas envergonhadas do dragão com um calor aberto e aconchegante."

    $LoungeBlobs[0] = False
    $Asterion.change ("emotion", "sad")

    "Você e Astério podem sentir isto em meio à agitação que preenche o salão;{w=0.2}
    aquela mistura de melancolia pesada e luz,{w=0.2} esperança palpitante crescendo em seus peitos."

    "Apenas agora você percebe quão {i}silencioso{/i} esteve o Hotel até então."

    "Sem passos quebrando a monotonia dos corredores, sem vozes para trazer novos pensamentos
    deslizando para a mente. O ar estagnado do Hotel deixou vocês dois letárgicos."

    "E esta noite, depois de oitenta anos de silêncio, aquela besta foi vencida."

    $Asterion.change ("emotion", "contemplative")

    "Você olha para Astério,{w=0.2} seu novo parceiro de crime,{w=0.2} e os olhos dele transbordam com a mesma emoção."

    "As vozes,{w=0.2} a risada rouca e o copo quebrado,{w=0.2}
    os ocasionais olhares direcionados a você e ao minotauro{w=0.2} — é como uma libertação."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    "Você relaxa em seu assento, deslizando nesta corrente de auto-satisfação enquanto Astério desce
    outra taça de vinho."

    "Talvez seu sorriso o torne acessível. Nos dez minutos seguintes, dois hóspedes
    se dirigem até você para fazer algumas perguntas e agradecer a hospitalidade."

    $Asterion.change ("emotion", "contemplative")

    "O mesmo não pode ser dito sobre Astério. Por mais alegre que esteja, ninguém lhe poupa uma palavra
    — embora você perceba alguns olhares de soslaio direcionados a ele."

    "Você tenta integrar o minotauro na conversa, mas se depara com as mesmas paredes
    repetidamente.{w} Primeiro, Astério não mais exibe a eloquência de antes;
    e segundo,{w=0.2} os hóspedes não conseguem conter suas gagueiras na presença dele."

    "Você se aproxima do minotauro quando a atenção se desvia de vocês dois."

    you "Desculpa, é demais para você? Se não quiser ficar, tudo bem."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "loose")

    asterion "Ah não, estou gostando daqui. Estou mesmo. Todo mundo está tão animado, senti falta disto.
    É apenas que...{w=0.2} tantas vozes ao mesmo tempo, é um pouco confuso."

    asterion "É fácil quando eu estou falando apenas com você. Mas já faz muito tempo desde a última vez que estive
    ao redor de tantas pessoas. Sinto muito."

    you "Não se desculpe, nada disso é culpa sua. Você quer sair?"

    $Asterion.change ("emotion", "contemplative")

    "O minotauro balança em círculos o vinho em sua taça,{w=0.2}
    mais como uma distração que qualquer tentativa de extrair o aroma."

    show Asterion:
        linear 2.0 xalign 0.35 yalign 2.5

    "Ele o bebe,{w=0.2} encosta-se de volta na cadeira,{w=0.2} e aproveita o espalhar do calor vindo do peito e indo para as extremidades."

    $Asterion.change ("emotion", "smiling")

    asterion "Não,{w=0.5} apenas preciso de um tempo para me acostumar."

    $Asterion.change ("emotion", "contemplative")

    "Astério olha para a taça de vinho. Está tingida de roxo das últimas gotas restantes."

    "O minotauro solta uma tosse, limpando a garganta da sensação de queimação."

    "Quando olha de volta ele precisa de um segundo para se concentrar em você. Ele se move com uma lânguida deliberação,
    adorando o quão embriagado está ficando."

    $Asterion.change ("emotion", "neutral")

    "O relaxamento do minotauro, porém, levanta um tenso silêncio.
    Seus olhos, por mais sonolentos que estejam, denunciam um intenso propósito."

    "O que Astério está pensando? Vocês dois permanecem em silêncio, sozinhos em seus pensamentos, mas não solitários."

    "As orelhas dele sacodem uma, duas vezes. Elas se esforçam para abafar todo o resto — as
    risadas e conversas, o arrastar de cadeiras e o tilintar de talheres — e focar em você."

    "Em sua respiração e quaisquer palavras que você possa dizer em seguida."

    "Ele avalia todas as suas características, mas fixa em seus olhos."

    "Seus olhos. Por um momento, é como se ele estivesse tentando olhar para sua alma, mas um sorriso quebra seu próprio foco."

    $Asterion.change ("emotion", "contemplative")

    "Ele dá uma risadinha e desvia o olhar."

    you "Algum problema?"

    asterion "Ah...{w=0.2} um pensamento bobo tomou conta de mim."

    asterion "Você já olhou para alguém,{w=0.2} uma pessoa que você conhece,{w=0.2} e como se de surpresa a
    enxergou pela primeira vez?"

    $Asterion.change ("emotion", "smiling")

    asterion "Ah, que coisa preciosa.{w} Por um momento, senti como se eu tivesse acabado de
    conhecê-lo,{w=0.3} e ainda assim...{w=0.3} você era tão familiar,{w=0.2} [player_name]."

    you "Talvez você esteja me confundindo com um hóspede de muito tempo atrás."

    asterion "Não,{w=0.1} não,{w=0.1} não é isto.{w=0.2} Tenho certeza.{w} Não consigo me lembrar...{w=0.5}
    Talvez não um hóspede,{w=0.1} não...{w=0.5} certamente não um mestre."

    $Asterion.change ("emotion", "contemplative")

    asterion "Ah, esta velha mente minha.{w=0.2} De onde está vindo isso, esta..."

    asterion "Eu estava tentando apontar, o que sobre você que está fazendo...{w=0.5}
    Pensei que poderiam ser seus olhos,{w=0.2} mas..."

    asterion "Não, não é a forma como você olha.{w=0.2} Mas agora eu apenas..."

    pause 1.0

    asterion "Já sentiu como se tivessem{w=0.2} beija-flores{w=0.2} fazendo cócegas na parte de trás de seu crânio?{w}
    Era isto que eu estava sentindo."

    asterion "Mas agora eu estou apenas olhando para trás, pensando em um amigo aqui e ali...{w}
    não é doce saborear velhas memórias?"

    show Greta behind LoungeLight:
        yalign 1.0 xalign 1.5 xzoom -1
        ease 1.0 xalign 1.3

    asterion "Sinto muito, não sei onde quero chegar com isso.{w} Mas...{w=0.2}
    lembrar de todos os meus velhos amigos, parece como se eles estivessem aqui novamente."

    show Greta:
        ease 1.0 xalign 1.25

    asterion "Somos apenas eu e você,{w=0.2} mas eu sinto..."

    show Greta:
        ease 1.0 xalign 1.2
    stop music fadeout 6.0

    $Asterion.change ("emotion", "sad")
    asterion "Talvez eu deveria estar agradecido... {w=0.2}por..."

    stop music fadeout 1.0

    show Greta:
        ease 1.0 xalign 1.1
    pause 1.0

    show Asterion:
        linear 0.4 xalign 0.25 yalign 2.0
    $Asterion.change ("emotion", "surprise")

    show Greta:
        ease 1.0 xalign 1.0

    #sound of a chair being dragged

    play sound "sfx/chair.ogg"
    "A conversa ao seu redor diminui e morre{w=0.2}— isto é,{w=0.2} até vocês dois notarem uma cadeira sendo arrastada para perto de Astério e você."

    #show Greta

    #If it's ok with everyone I can show greta earlier at the edge of the screen slowly moving towards asterion in the middle, who only acknowledges her right here
    #Do eeeeeeeet
    #YES, IT'S GONNA BE GREAT

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    show Greta:
        ease 2.0 xalign 0.9 yalign 1.5

    play music "music/Obviously.ogg" fadeout 1.0 fadein 1.0

    "Greta" "Ah, olá!{w=0.2} Desculpem se eu estiver interrompendo alguma coisa. {w}Meu nome é Greta,
    eu sou da Alemanha...{w=0.2} e estou muito curiosa."

    "Greta" "Fico grata por esse...{w=0.2} tudo, mesmo.{w} Meu namorado e eu não tivemos a chance de tomar um banho
    há alguns dias, muito menos comer uma boa refeição. O cheiro estava se tornando um problema."

    if first_guest == "Luke":
        "Greta" "Mas sabe, em um único dia eu aprendi que existe algo como um minotauro,{w=0.2}
        e também uma águia falante!{w=0.2} Em um deserto!{w=0.2} Nós estávamos na Europa Oriental, e agora em um deserto!"
    else:
        "Greta" "Mas sabe, em um único dia eu aprendi que existe algo como um minotauro,
        e também um dragão falante!{w=0.2} Em um deserto!{w=0.2} Nós estávamos na Europa Oriental, e agora em um deserto!"

    "Greta" "Isso é muito para assimilar —{w=0.2} e deixa eu te contar, sempre fui uma garota muito curiosa."

    "Greta" "Então, se você não se importa que eu pergunte, como tudo isso funciona?{w=0.2} Seres não humanos, quero dizer."

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")

    asterion "Ah, nós existimos. Seres que não são exatamente humanos, volta e meia eles aparecem.{w=0.2}
    Mas se mantêm escondidos."

    $Asterion.change ("emotion", "neutral")

    asterion "Não é o caso aqui, onde seus amuletos encantados não funcionam.{w=0.2} Suas verdadeiras formas são reveladas."

    "Greta" "\"Suas\"?{w=0.2} Você fala como se fosse diferente deles."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("leftarm", "loose")

    pause 1.0

    $Asterion.change ("emotion", "sad")

    asterion "De certa forma, sim."

    "O minotauro olha para a própria taça vazia, em seguida, desvia o olhar para você."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")

    asterion "Gostaria de mais vinho?"

    you "Não, estou bem.{w=0.2} Esse é muito bom, estou saboreando cada gole."

    show Greta:
        ease 0.5 xalign 0.85
    pause 0.5
    show Greta:
        ease 0.5 xalign 0.9

    "Greta fica com as mãos inquietas enquanto Astério se serve com uma grande taça de vinho."

    "Greta" "Qual {i}é{/i} sua história, então?{w=0.4} Você é diferente dos outros?"

    "Astério mantém o olhar na taça, mas responde sem perder o ritmo e com uma peculiar entonação fria."

    $Asterion.change ("emotion", "neutral")

    asterion "Eu nasci aqui,{w=0.2} neste hotel.{w=0.2} Decidi ficar para trás e cuidar dele.{w}
    Mas como você pode ver,{w=0.2} as coisas não estavam indo bem."

    $Asterion.change ("emotion", "sad")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    "Astério dá uma olhada rápida em você, como se pedisse sua permissão para prosseguir.
    Você permanece quieto e ele entende isto como sua deixa."

    $Asterion.change ("emotion", "tired")

    asterion "Eu estava me recuperando de alguns ferimentos graves...{w=0.2}
    enquanto isso, o hotel caiu em ruínas.{w} Pois o proprietário anterior o negligenciou."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")

    asterion "Mas as coisas mudaram para melhor desde que a propriedade passou para o Mestre [player_name]."

    "Greta olha você de cima a baixo, mas com um olhar tão penetrante que quase parece ameaçador."

    "Greta" "Por que você chama ele de \"Mestre\"?{w=0.2} O que tem com isso?"

    "Astério não hesita desta vez."

    asterion "É assim que minha família sempre chamou o dono do estabelecimento.{w=0.2}
    Nossa linhagem os serviu por várias gerações."

    asterion "Foi por isso que escolhi estar aqui. {w=0.2}Esta é a minha vocação,{w=0.2} e estou ansioso para ver o hotel
    mais uma vez movimentado com vida...{w=0.5} como costumava ser."

    $Asterion.change ("emotion", "neutral")

    "Greta" "Então você é uma espécie de mordomo?"

    "Astério acena com a cabeça, sem se preocupar em tirar os olhos de seu vinho."

    "Greta" "Você já pensou em encontrar um emprego em outro lugar?"

    "Astério balança a cabeça de um lado para o outro."

    "Greta" "E ter filhos? Você planeja encontrar uma senhora minotauro e fazer bebês?"

    "Greta" "Digo,{w=0.2} é assim que funciona para você,{w=0.2} eu presumo?{w} Um homem e uma mulher minotauro.{w=0.3}
    Você não é filho de uma vaca e um humano,{w=0.2} é?"

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "loose")
    pause 1.0

    asterion "Meus pais eram minotauros."

    "Greta" "Ah, é bom ouvir isso.{w=0.2} A outra alternativa seria meio bizarra, não é?"

    "Greta" "Bem, sobre a minha outra pergunta,{w=0.2} e sobre ter filhos você mesmo?{w=0.3}
    Bebêzinhos minotauro devem ser tão fofos!"

    $Asterion.change ("emotion", "neutral")

    show Greta:
        ease 0.4 xalign 0.86
    pause 0.5
    show Greta:
        ease 0.4 xalign 0.9

    "Astério não se incomoda em responder — ele olha para ela apenas entre goles.
    Greta morde o lábio e se agita na cadeira."

    "Greta" "Sinto muito se estou sendo invasiva,{w=0.2} é que tudo isso é muito novo para mim.{w=0.3}
    Para nós, suponho."

    "Greta" "Essas perguntas incomodam você?"

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    "Apenas agora que Astério olha para você. O olhar dele se mantém em sua pessoa por um segundo a mais.
    O sorriso, você nota, possui um toque de falsidade."

    asterion "Estou acostumado com elas.{w=0.3} Há mais alguma coisa que você gostaria de saber?"

    "Greta" "Sobre seu olho...{w=0.2} Você precisa de assistência médica?{w=0.3} Meu namorado é um doutor,
    estávamos conversando mais cedo sobre isso."

    "Greta" "Olha, sabemos que tem mais coisas acontecendo por aqui do que parece.
    {w}Magia, ou seja lá como você chame.{w=0.2} Mas,{w=0.2} é,{w=0.2} existe algo que um médico poderia fazer para ajudar?"

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "loose")

    asterion "Você...{w=0.2}você é muito gentil.{w=0.2} Mas receio que um médico não poderá fazer muito por mim.{w=0.3}
    Eu não sou exatamente...{w=0.2} as coisas funcionam de forma diferente comigo."

    asterion "Mas você não precisa se preocupar.{w=0.3} Eu estou bem,{w=0.2} não demorará muito até que eu esteja curado novamente."

    pause 1.0

    "Greta" "Ah!{w=0.2} Então você pode fazer seu olho crescer de volta?{w=0.3} Isso é incrível!{w=0.2}
    Sabe, seria incrível estudar como você faz isso.{w=0.2} Certamente a medicina moderna teria a ganhar com —"

    $Asterion.change ("emotion", "sad")

    pause 2.0

    "Greta" "Sinto muito,{w=0.2} acho que fui longe demais."

    pause 1.0
    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    pause 1.0

    asterion "Perdoe a curiosidade,{w=0.2} mas de onde você é?"

    "Greta" "Sou de Berlim Oriental, cresci não muito longe de onde ficava o muro.{w=0.3}
    Mas nasci alguns anos depois que ele caiu."

    "Greta" "Meu namorado é de Dijon, França.{w=0.3} Do lugar de onde vêm todas as mostardas coloridas!"

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "loose")

    asterion "Eu{w=0.2} — Entendo. E como é a Berlim \"Oriental\"?"

    "Greta" "É ótima hoje em dia!{w=0.3} Claro que ainda há uma pequena lacuna,{w=0.2}
    vai demorar um pouco até que o Leste e o Oeste sejam realmente iguais."

    "Greta" "Mas é charmoso,{w=0.2} de certa forma.{w=0.3} Em todos os lugares você vai ver os bonequinhos soviéticos
    nos sinais de trânsito,{w=0.2} é tão fofo!"

    "Greta" "E a vida noturna é, obviamente, fantástica.{w=0.2} Afinal, é Berlim!"

    $Asterion.change ("emotion", "sad")

    "Com a menção de Berlim \"Oriental\" e \"Soviéticos\", os olhos de Astério se voltam
    para você por uma fração de segundo."

    $Asterion.change ("emotion", "tired")

    "Em seguida, pulam para as outras pessoas ao redor da mesa conforme ele percebe que elas estão
    ficando em silêncio e direcionando sua atenção para ele."

    "Greta" "Mas não vamos ficar em Berlim por muito tempo.{w=0.3} Meu namorado e eu estamos querendo
    morar na Inglaterra há anos,{w=0.2} e estamos tentando fazer isso funcionar."

    "Greta" "E sempre quisemos mochilar pela Europa,{w=0.2} então achamos que agora fosse
    um bom momento.{w=0.3} Minhas irmãs gêmeas todas fizeram isso, e eu tenho ouvido há anos como foi divertido."

    "Greta" "Então aqui estamos."

    "Agora que Greta quebrou o gelo, as pessoas estão {i}olhando{/i}{w=0.2} — e Astério fica rígido ao
    perceber."

#Panic attack scene, happens if player sent Asterion to the valley

    if Chapter4_Terrorized_Asterion == "True":
        pause 2.0
        play music "music/MayItBegin_Acoustic.ogg" fadeout 1.0 fadein 1.0
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        "Ele encara de volta todos os hóspedes, todos os pares de olhos fixos em seus traços inumanos que
        agora estão percebendo quão rígido ele ficou. Sua respiração torna-se dificultosa e ele congela enquanto
        o desespero afunda em seu estômago."

        "Quando o minotauro reúne forças suficientes para se mover outra vez, é como se seus membros fossem
        feitos de chumbo."
        show Asterion:
            ease 0.05 xalign 0.2501
            pause 0.05
            ease 0.05 xalign 0.2499
            pause 0.05
            repeat
        "Oprimido pelo peso terrível do olhar coletivo dos hóspedes, ele pode apenas
        contorcer-se e tremer, levantando os braços apenas alguns centímetros de cada vez."

        show Greta:
            ease 0.4 xalign 1.0
        "Os tremores propagam-se como ondas pela superfície de um lago: dos dedos
        aos braços, depois para o estômago e, finalmente, afundando como garras em seu peito."

        "A maré impiedosa varre por toda a parte, a consciência do Minotauro parece seguir atrás como
        um nadador seguindo a esteira de um barco que o jogou ao mar."

        $Asterion.change ("leftarm", "raised")
        "A mão do touro perdura no estômago, que se agita sob seu toque como um mar
        em uma tempestade."

        "Ele o agarra como se estivesse tratando de um hematoma — como se tivesse
        levado um soco no estômago e agora estivesse tentando não vomitar."

        $Asterion.change ("emotion", "surprise")
        show Asterion:
            ease 0.4 yalign 1.4
            ease 0.4 yalign 1.0
        pause 1.3
        show Asterion:
            ease 0.05 xalign 0.2501 yalign 1.0
            pause 0.05
            ease 0.05 xalign 0.2499
            pause 0.05
            repeat
        "Ele engulha algumas vezes, ofegando por ar, e alguns membros da multidão reunida afastam-se
        para ficar longe da área onde o vômito pode cair."

        show Greta:
            ease 0.4 xalign 1.05
            ease 0.4 xalign 1.1
        "Entre os estudantes, uma começa a procurar remédio para enjoo em sua bolsa,
        mas é parada por um de seus colegas."

        "Ele gesticula para o corpo inteiro do minotauro tremendo como uma folha em um vendaval
        e suando baldes como se tivesse corrido uma maratona no deserto em torno do hotel."

        "Qualquer um pode ver que náusea é apenas um sintoma de um problema maior
        em jogo com o bem-estar de Astério, jogar pílulas na situação não
        será de grande ajuda."

        "Mesmo assim, um dos uruguaios corpulentos se oferece para ajudar a
        conter o touro caso ele precise ser medicado contra sua vontade."

        "No momento em que a tensão atinge o pico, as mãos do minotauro alcançaram o peito.
        As grossas unhas pretas que tingem a ponta de seus dedos cavando sulcos na carne ao redor
        de seu esterno."

        "Seus lábios se mexem, mas seus pulmões não estão cooperando; como se cada olho sobre ele fosse uma
        mão invisível em volta de sua garganta, ele pode apenas soltar gemidos estrangulados
        e choramingos em sua tentativa de falar."

        "Seja qual for o motivo, Astério está {i}apavorado{/i} além do limite das palavras:
        a minúscula chama azul em seu olho denuncia a situação."

        "Ela faísca uma, duas vezes em sua cavidade ocular vazia — antes de disparar pela sala,
        como se procurasse por refúgio nos olhos de outra pessoa."

        "Quando o minotauro cambaleia ao redor para encontrar seu olhar, o rosto dele fica frio
        e distante ao mesmo tempo: olhos arregalados, sobrancelhas erguidas, lábios entreabertos —
        como um cervo nos faróis, paralisado pelo espectro da mortalidade que avança rapidamente."
        show blackback behind Asterion:
            alpha 0.0
            ease 2.0 alpha 1.0
        show Greta behind blackback
        if first_guest == 'Luke':
            show LoungeLight:
                ease 2.0 alpha 0.0
        "No entanto... ele não pode morrer.{w=0.2} É uma verdade absoluta, a única certeza a qual ele
        pode se agarrar durante qualquer problema:{w=0.4} sua sentença e prisão são invioláveis."

        $Asterion.change ("emotion", "tired")
        "Não importa quanto tempo passe ou quantos Mestres venham e vão,
        seus dias estão fadados a serem tão infinitos quanto o labirinto no qual ele os passará."

        "Ele também não teme a morte. Ele conhece e anseia pelo que o espera do outro lado:
        os campos de Asfódelos, seus amigos e seu serviço ao Lorde Hades como guarda."
        hide Greta
        "Ele não pode, racionalmente, temer a morte mais agora do que quando ofereceu
        sua cabeça àquele homem ateniense há milênios, e foi condenado por sua mansidão."
        $LoungeBlobs[0] = False
        "Mesmo assim, mente e corpo são superados.{w=0.2} O minotauro é arrastado para baixo
        da viciosa ressaca do trauma — sua biologia é seu Mestre agora."

        "Exige que ele acredite que pode morrer, que ele encontrará um fim rápido e
        calamitoso diante desta multidão de espectadores curiosos e bem-intencionados."

        "Ele não possui qualquer agência real aqui: como sempre."

        show Greta behind Asterion:
            xalign 0.6 yalign 1.0 xzoom -1
        show blackback behind Greta
        with Dissolve(2.0)

        "A voz de Greta é a primeira a romper o murmúrio caótico que
        consumiu os outros hóspedes — ela, pelo menos, está pronta para cuidar do assunto
        sem esperar a aprovação de ninguém."

        $Asterion.change ("emotion", "sad")
        show Ismael_surprise behind Greta:
            xalign 0.9 yalign 1.0 xzoom -1
        hide blackback
        if first_guest == "Luke":
            show LoungeLight
        with Dissolve(2.0)
        "Ela empurra um dedo no touro com cautela, como se um simples reajuste
        fosse tudo o que é necessário para as engrenagens da cabeça do minotauro engrenarem
        mais uma vez como deveriam."

        "Por um momento, Ismael até se levanta para rondar atrás dela,
        parecendo meio pronto para intervir em sua defesa se as coisas azedarem."

        show Ismael_surprise:
            xzoom 1
            pause 1
            xzoom -1

        "Mas, levando em conta seus olhos inquietos, fica claro que ele realmente quer apenas fugir
        até que a situação se acalme."

        "Ele também é mantido no lugar, assim como Astério, pelos olhos de seus colegas."

        "Greta" "Você está bem?"

        $Asterion.change ("emotion", "tired")
        "As palavras caem em ouvidos surdos:{w=0.3} como um nó de lã de aço contra um
        prato sujo, a tentativa de Greta de se aproximar parece apenas intensificar a
        impiedosa raspagem contra as superfícies internas do crânio do minotauro."

        "O passado o recebe e a memória se repete de novo e de novo."

        "O cômodo gira como um rolo de filme no projetor da alma de Astério.
        Agora, ele é a pedra — a ondulação que distorce a superfície plácida,
        fazendo a cena nadar enquanto o passado desaba sobre o presente."

        show blackback behind Asterion:
            alpha 0.6
        with Dissolve(2.0)

        "Ele se afoga no redemoinho de seus pensamentos — como se estivesse lá novamente,
        na noite mais importante de seu mais recente século de vida."

        "Os atores estão todos lá: o Mestre, uma jovem atraente, e uma
        multidão sem rosto. Velhos pensamentos ressurgem, não solicitados."

        hide Ismael_surprise
        show Ismael_surprise:
            xalign 0.9 yalign 1.0
            ease 3.0 xalign 1.4

        "Foi em uma noite como esta que o demônio foi solto em Mestre Clément.
        Sempre esteve lá, tanto quanto em qualquer alma perdida que o Hotel
        hospedou naquele dia: a falta de propósito, a dor e a agitação geral."

        $Asterion.change ("emotion", "sad")
        "Ele até foi gentil, uma vez — seus defeitos tornaram-se inócuos, até mesmo triviais, pelo pano
        de fundo de sofrimento humano no qual ele vivia."

        "Assim como o caolho é rei entre os cegos, também era Clément entre os
        veteranos e refugiados traumatizados da Primeira e Segunda Guerra Mundial."

        "Ele não estava lá por completo — mas era funcional o suficiente para que não precisasse estar,
        enquanto seu irmão estivesse por perto."

        "Apenas o Mestre Jean-Marie poderia conter a maré do delírio paranóico de Clément
        e mitigar o ego de um homem quebrado — mas o Mestre Jean-Marie estava morto,
        e coube ao lunático tomar conta do manicômio."

        "Talvez Clément tenha tentado à sua maneira fazer o que seu irmão havia feito,
        aliviar a dor de seus semelhantes e ganhar seu respeito."

        "Mas cada contratempo, cada falha, funcionava apenas como fertilizante para sua loucura criar
        raízes e sufocar todo o resto."

        "O amor e a admiração que ele buscava eram uma aventura tão condenada quanto a fuga de Ícaro;
        cegado pela arrogância, consumido pela inveja, Clément caiu e arrastou com ele
        tantos quanto pôde."

        "Em suas mãos, o poder de Mestre do hotel era apenas um meio de impressionar
        — um truque barato de salão, no máximo, para chamar a atenção de mulheres bonitas."

        $Asterion.change ("emotion", "tired")
        "Aquela noite, uma garota como a Srta. Greta reprimiu seus avanços — ele havia tentado antes,
        e ela o rejeitou gentilmente. Ele tentou novamente, esperando em vão que sua
        persistência fosse ser recompensada."

        "Então, algo rompeu — um silêncio desconfortável caiu sobre a multidão.
        A risada foi apagada de uma vez só, como uma vela entre dois dedos."

        "A distância começou a diminuir entre Clément e a jovem mulher;
        o Minotauro interpôs-se e levou o golpe, como sempre fazia quando
        surgia uma altercação física."

        "Na obstinação que se seguiu, todos foram acusados de traição — excomungados
        em virtude da blasfêmia contra o deus mesquinho do Hotel, para enfrentar o sofrimento
        que os aguardava nas ruínas ardentes da periferia europeia."

        "Todos,{w=0.5} exceto Astério."

        "Esta é sua maldição. Tal é a inconstância do coração de um Mestre,
        à qual ele sempre está sujeito."

        $Luke.change("emotion","surprise")
        $Luke.change("arm","hip")
        $Kota.change("emotion", "surprise")
        $Kota.change("rightarm", "raised")
        $Kota.change("leftarm", "raised")

        show blackback:
            ease 2.0 alpha 0.2
        show Luke behind Asterion:
            xalign 2.0 yalign 1.0 xzoom 1
            ease 2.0 xalign 1.2
        show Kota behind Asterion:
            xalign -1.0 yalign 1.0 xzoom 1
            ease 2.0 xalign -0.2

        "Fora da cabeça do minotauro, as coisas acontecem mais rapidamente. Atraídos pela
        confusão, Luke e Kota começam a abrir caminho no grupo de pessoas,
        em busca de direcionamento — um deles o chama de \"Chefe\", e a atmosfera se altera em um instante."

        "Como ninguém tem certeza de como melhor lidar com seja lá o que tenha acontecido com Astério,
        todos parecem concordar que a situação atual requer sua intervenção;{w=0.3}
        em virtude de seu escritório, você não tem o luxo de permanecer como espectador."

        "Todos os olhos estão em cima de você; algo deve ser feito."

        menu:
            "O que você faz?"
            "Ordenar Astério para se acalmar.":
                "A coisa natural a se fazer em tal crise seria tentar acalmar Astério.
                Dá-lo um pouco de atenção deve ajudá-lo."

                "Não há tempo para refletir sobre os detalhes do que causou esse ataque de pânico.
                Você possui uma audiência que claramente espera uma solução conveniente."

                show Luke:
                    ease 2.0 xalign 2.0
                show Kota:
                    ease 2.0 xalign -1.0
                show Greta:
                    ease 2.0 xalign 1.1

                "Amparado pela atenção, você levanta as mãos e gesticula para que o público se afaste;
                você tem tudo sob controle."
                $Asterion.change ("emotion", "sad")
                $Asterion.change ("leftarm", "loose")
                show Asterion:
                    ease 2.0 xalign 0.5 zoom 0.97 yalign 1.0
                pause 2.0
                show Asterion:
                    ease 0.05 xalign 0.501
                    pause 0.05
                    ease 0.05 xalign 0.499
                    pause 0.05
                    repeat
                "O minotauro parece encolher à medida que a distância começa a diminuir, embora ele
                não recue mais de um centímetro ou dois."

                $Asterion.change ("emotion", "bowing")
                "Suas pernas permanecem enraizadas no chão; mesmo assim, à medida que você se aproxima dele,
                ele vira a cabeça e fecha os olhos."

                "Que reação estranha. Você se afasta para não dar aos hóspedes a impressão errada."
                "É importante estabelecer os fatos, antes de mais nada. Você poupa os detalhes
                grotescos, é claro, e depois de um minuto todos estão um tanto informados sobre o assunto."

                "Pelo que os hóspedes podem dizer, o minotauro sempre teve um temperamento nervoso,
                o qual os proprietários anteriores exacerbaram."

                "O próprio Astério disse que foi criado no hotel — é fácil para eles
                aceitarem seu estado atual como consequência dos gerentes anteriores."

                "Afinal, Astério e o hotel estavam em um estado muito pior quando você os encontrou,
                e você cuidou de ambos de volta à boa saúde com a bondade de seu coração."

                you "Não se preocupem, é apenas um ataque de ansiedade."

                you "Pode ser assustrador para nós e constrangedor para ele, mas nada está
                seriamente errado. Tudo vai passar logo e vocês vão poder voltar a socializar."

                you "E Greta, não é culpa sua. Astério ficou um pouco superestimulado, só isso."

                you "É uma grande noite para nós e ele queria participar das festividades;
                foram apenas coisas demais de uma só vez."

                show Greta:
                    ease 2.0 yalign 1.2
                "Apesar de sua insistência para o contrário, está claro que a corajosa alemã sente-se
                cabisbaixa com sua percepção de responsabilidade pelo estado atual das coisas."

                "Seus olhos caem para o chão e ela se desculpa por deixar sua curiosidade levar o melhor de si
                mais uma vez."
                show Greta:
                    ease 2.0 xalign 1.5
                "O fato de que você escolheu dirigir-se a ela especificamente não passou despercebido aos outros
                hóspedes."

                "Por cima do ombro dela, você pode ver alguns outros membros da audiência
                a lançando olhares de desaprovação, ansiosos para aceitar um bode expiatório que os absolva
                de qualquer responsabilidade compartilhada."

                "Para o minotauro, você dirige um simples comando, em um sussurro enjoativo
                tão doce que poderia corroer ferro sólido:"

                you "Astério, olhe para mim.{w=0.2} O que tem de errado?"

                "Como ele fez quando você o enviou para o vale para se encontrar com Argos,
                o minotauro fica tenso sob o peso de suas palavras."

                "Seu corpo e mente são como um outra vez, embora brevemente, na
                resistência inútil à sua ordem."

                show Asterion behind blackback
                show blackback:
                    alpha 0
                    ease 0.3 alpha 0.8
                    ease 0.6 alpha 0
                    ease 0.3 alpha 0.8
                    ease 0.6 alpha 0
                play sound "sfx/hum.ogg"
                "Ainda assim, a força invisível que o liga à sua vontade trabalha
                imediatamente — anunciada, como de costume, por um piscar de luzes."

                $Asterion.change ("emotion", "sad")
                "Como se você de fato o tivesse agarrado pelos chifres, a cabeça do touro
                gradativamente se vira de volta em sua direção."

                $Asterion.change ("emotion", "surprise")
                "Ele retoma seu olhar apavorado e de olhos arregalados, assim que tem certeza
                de que conseguiu toda a atenção dele, você fala novamente."

                you "Você não tem nada a temer, certo?"

                "Um minuto se passa enquanto o Minotauro se atropela para responder, lutando para
                permitir que suas cordas vocais recuperem um semblante de funcionamento."

                $Asterion.change ("emotion", "tired")
                "Astério não pode se permitir fugir de seu dever, mesmo em um momento de colapso;
                ele sabe que deve responder, pelo menos para evitar que você force uma resposta dele."

                "Entre soluços incoerentes e sem fôlego, ele gagueja."

                $Asterion.change ("emotion", "sad")
                asterion "N-{w=0.2}não...{w=0.2} M-mestre..."

                "Mais silencioso ainda, quase inaudível, você responde."

                you "Achei que não."

                "Você traz sua mão de volta para o rosto de Astério e ele se inclina em seu
                toque, ainda pesando com angústia."

                "Mas qualquer resistência momentânea é indistinguível do tremor de pânico que
                domina o restante de sua linguagem corporal."

                "Sua pele de couro está pegajosa, escorregando com suor sob seu pelo; mas você
                segue em frente, jovial e intrépido."

                "A audiência ficou em silêncio há muito tempo, seja por ter sido conquistada por suas mentiras
                ou impotente para desafiar a atmosfera que você criou."

                $Asterion.change ("emotion", "bowing")
                show Asterion:
                    ease 0.5 yalign 2.1

                "Astério cai de joelhos espontaneamente e, tão rápido quanto seu corpo
                permite, pressiona o rosto em suas coxas."

                "Você não está totalmente certo de onde ele quer chegar, mas sua obediência
                voluntária é valiosa demais para ser desperdiçada; o gesto parece
                confortá-lo mais do que o abraço que você planejou."

                "Então você permite, esfregando a cabeça do touro enquanto ele chora."

                "Os braços dele estão apertados em torno de suas panturrilhas, mas a maior parte da força
                parece estar na maneira como ele agarra os próprios cotovelos."

                "Embora não fosse aparente de uma distância maior, de perto parece
                menos que ele está se segurando em você para obter conforto e mais como se estivesse
                tentando se esconder — ou implorando por misericórdia."

                show Asterion:
                    ease 2.0 yalign 1.4

                "Depois do que parece uma hora, o aperto do Minotauro diminui.
                Sua respiração fica mais lenta, seu estômago para de arfar e sua voz retorna
                — embora esteja fria e vazia."

                $Asterion.change ("emotion", "sad")
                $Asterion.change ("leftarm", "raised")
                asterion "Gentil Mestre, por favor... posso ser dispensado?"

                you "É claro. Eu te acompanho até o seu quarto."

                hide Astério
                with Dissolve(2.0)

                "A seu comando, Astério titubeia para fora do salão, o taciturno bater de
                seus cascos sendo o único som quebrando a quietude."

                "Ao adentrar o corredor escuro com ele, você pausa por um momento,
                uma vez que está fora de vista — esperando para ver como o clima muda em sua ausência."

                "O silêncio persiste pelo que parece um bom tempo depois,
                sucedido apenas por um murmúrio de descontentamento que nunca chega a se
                transformar em uma conversa completa."

                "Parece que, apesar de seus melhores esforços, a festa acabou."
                $ abuse_act1 += 1

            "Dar espaço a Astério.":
                $Asterion.change ("emotion", "bowing")
                $Kota.change ("emotion", "sad")
                $Kota.change ("rightarm", "relaxed")
                $Kota.change ("leftarm", "relaxed")
                $Luke.change ("emotion", "annoyed")
                "No repentino silêncio, a conclusão se afirma. A histeria de Astério
                {i}visivelmente{/i} piorou quando ele encontrou seus olhos: suas ações desempenharam um papel
                significante em levá-lo ao seu estado emocional atual."

                "Ao invés de deleitar-se com o poder da situação, este pensamento torna paralítico
                o olhar expectante da audiência."

                "Você se pega incapaz de se mover ou respirar — desejando nada mais do
                que escapar ou rastejar para dentro de um buraco, como Ismael parece tão desesperado para fazer."

                "Não importa o quão óbvio seja que alguém precise assumir o comando,
                você — de todas as pessoas — não tem o direito de avançar e bancar o herói."

                "No momento, você não tem certeza do que é pior: o fato de que os hóspedes
                permanecem alegremente inconscientes de seu envolvimento no que levou
                à situação atual..."
                "...ou a silenciosa expectativa de que você pode, de alguma forma,
                despuxar o gatilho e resolver tudo."

                pause 3.0

                "Os segundos se passam, embora cada um pareça durar um minuto; o pedido de socorro de
                Astério e as orações dos hóspedes por uma resolução rápida permanecem sem resposta."

                "Conforme a tensão continua a aumentar, você se pega olhando para as pessoas
                ao seu redor, procurando por uma faísca de orientação."

                "Às vezes, a coisa mais responsável que um líder pode fazer é adotar uma abordagem
                direta e ceder o controle para alguém com mais conhecimento.
                Em vez de dar um tiro no escuro e esperar pelo melhor, você expressa um pensamento."

                $Luke.change ("emotion", "surprise")
                $Kota.change ("emotion", "surprise")

                you "Alguém aqui tem experiência em tratamento de ataques de pânico?"

                "Qualquer tênue semblante de controle que o ofício de Mestre o concedeu
                começa a evaporar."

                show Luke:
                    ease 1.0 xalign 1.4
                show Greta:
                    ease 1.0 xalign 0.8
                show Kota:
                    ease 1.0 xalign -0.4

                "Suas palavras cortam o silêncio momentâneo como uma corda se partindo,
                a sala de jantar fica mais uma vez agitada enquanto os hóspedes voltam a
                discutir entre si sobre como melhor abordar a situação."

                $Asterion.change ("emotion", "surprise")
                $Asterion.change ("leftarm", "loose")
                "Em meio ao ruído crescente, Astério continua a ter espasmos e tremedeiras,
                contorcendo-se de vez em quando, na expectativa de ser golpeado."

                "Com cada nova onda de terror que se abate sobre ele, sua opinião sobre si
                mesmo continua a afundar mais e mais fundo sob o esmagador
                peso da culpa."

                $Luke.change ("emotion", "neutral")
                $Luke.change ("arm", "pointing")
                show Asterion behind Luke
                show Luke:
                    ease 2.0 xalign 1.1
                show Greta:
                    ease 1.0 xalign 1.7
                show Kota:
                    ease 1.0 xalign -1.0

                "Uma figura começa a seguir seu caminho para a frente, caminhando para o centro
                da multidão com as mãos de palmas abertas erguidas para o ar, pedindo por silêncio."

                "Luke tem uma ideia e, no verdadeiro estilo militar, pede a permissão
                explícita de seu oficial comandante antes de fazer sua jogada."

                "Você já viu a atitude dele e seu estômago revira com o prospecto de
                seja lá o que ele planeja para lidar com a ansiedade de Astério."

                "O grifo crasso e falastrão não tem a menor chance de acalmar
                o minotauro."

                "Na verdade, talvez ele apenas piore as coisas."

                "Uma fantasia de Luke em trajes completos de caubói saltita em sua mente: chapéu sertanejo,
                botas com esporas e tudo mais — amarrando uma sela nas costas de Astério e
                montando até que ele termine de chorar."

                "Mesmo que você não saiba o que fazer, não pode permitir que Luke —"

                show Luke:
                    ease 1.0 zoom 1.05 yalign 1.05

                "O grifo coloca uma mão em seu ombro e olha em seus olhos,
                interrompendo sua linha de pensamento sem dizer uma única palavra."

                "Apesar de suas dúvidas iniciais, você percebe uma atitude séria e perspicaz
                sobre ele que nunca viu antes."

                $Luke.change ("emotion", "wink")
                $Luke.change("arm", "salute")
                "Ele exala um foco frio e intenso que evidencia a disciplina
                e dignidade de um militar que resistiu a incontáveis
                campanhas."

                $Asterion.change ("emotion", "bowing")
                "Pode-se esperar que ele interrompa com um chiado agudo ou um
                grasnado ensurdecedor, como apenas alguém com pulmões americanos e cordas vocais
                meio-aquilinas poderia..."

                "...mas aqui está ele, preparado, esperando por seu sinal."

                $Luke.change("arm", "hip")
                $Luke.change ("emotion", "annoyed")
                show Luke:
                    ease 1.0 zoom 1.0 yalign 1.0

                "Você dá a ordem e é recrutado para o exército voluntário de Luke —
                acompanhado de Greta e Ismael, os outros dois mais próximos do centro.
                De acordo com as ordens dele, vocês ficam parados, aguardando por mais instruções."

                show Luke behind Asterion:
                    ease 2.0 xalign 0.9

                "O grifo dá um passo à frente – parando apenas à distância de um braço de Astério.
                Ele enuncia cada sílaba, alto e claro."

                $Luke.change ("emotion", "neutral")
                luke "Astério, o que aconteceu?"


                $Asterion.change ("emotion", "surprise")
                show Asterion:
                    ease 1.0 xalign 0.3
                "Os olhos do minotauro reestabelecem o foco e seu peito arfa com o esforço de
                forçar o ar para dentro e fora. Ao longo de um minuto,
                intercalando com tosse, ele gagueja."

                $Asterion.change ("emotion", "tired")

                asterion "O{w=0.2}-o v-{w=0.2}vale!{w} P-{w=0.2}p{w=0.2}-por favor...!"

                luke "Você precisa de espaço? Quer tomar um ar?"
                show Asterion:
                    ease 0.05 xalign 0.301
                    pause 0.05
                    ease 0.05 xalign 0.299
                    pause 0.05
                    repeat
                "O reconhecimento acende nos olhos de Astério — mas logo em seguida, a ansiedade do touro
                agrava novamente. Qualquer clareza momentânea que o grifo trouxe para fora
                é subordinada novamente pela maré de pânico."

                "Mesmo assim, Astério consegue engasgar para fora mais alguns fragmentos de frase
                antes de retornar à incoerência."

                show Asterion:
                    ease 1.0 xalign 0.2
                $Asterion.change ("emotion", "surprise")
                asterion "N-{w=0.2}não...{w=0.3} N-{w=0.2}não...{w} Eu-{w=0.2}Eu-{w=0.2}
                Eu nã-{w=0.2}não posso...{w} Eu ser-{w=0.2}serei...{w=0.2} Eu...!"

                show Asterion:
                    ease 0.7 xalign 0.3
                show Asterion:
                    ease 0.05 xalign 0.301
                    pause 0.05
                    ease 0.05 xalign 0.299
                    pause 0.05
                    repeat
                $Luke.change ("arm", "pointing")
                luke "Não fale.{w=0.2} Balance a cabeça pra \"sim\", ou \"não.\""

                "Mais algumas perguntas rápidas completam o engajamento inicial."

                $Asterion.change ("emotion", "tired")
                "Luke pergunta se Astério já teve ataques de pânico antes, se tem
                remédio para eles e uma série de coisas sensatas e sensíveis que você realmente gostaria
                de ter pensado em fazer antes de passar a bola."

                $Luke.change ("emotion", "happy")
                show Luke behind Asterion:
                    ease 2.0 xalign 0.7

                "Depois de se certificar que o minotauro está lúcido o suficiente para acompanhar,
                o grifo orienta seu encarregado rebelde através de alguns exercícios de respiração,
                reafirmando calmamente palavras de apoio no ouvido do touro a cada passo."
                show Asterion:
                    ease 0.1 xalign 0.301
                    pause 0.1
                    ease 0.1 xalign 0.299
                    pause 0.1
                    repeat
                $Asterion.change ("emotion", "bowing")
                "Luke valida os sentimentos de Astério, mencionando de vez em quando que
                que ele não irá embora, que eles estão seguros e que os ataques de pânico
                raramente duram mais de meia hora..."
                show Asterion:
                    ease 0.15 xalign 0.301
                    pause 0.15
                    ease 0.15 xalign 0.299
                    pause 0.15
                    repeat
                "...a experiência o ensinou que mais cedo ou mais tarde o touro
                vai se equilibrar, é uma questão de tempo."

                show Asterion:
                    ease 0.1 xalign 0.3
                $Luke.change ("emotion", "neutral")
                "Diante de seus olhos, quase imperceptivelmente, o inferno congela.{w} De alguma forma,
                {i}surpreendentemente{/i}, Luke era o homem certo para o trabalho."

                "A batalha de Astério contra sua própria psique, depois de toda sua fúria explosiva,
                chega a um fim tênue e choroso."

                "A maré de medo vaza para longe, revelando a alma do homem por trás
                da concha bestial. Luke oferece sua mão e o minotauro a agarra com a gratidão
                simples e desesperada de um homem que foi salvo de se afogar."

                $Asterion.change ("emotion", "sad")
                "Embora tenha parecido muito mais tempo para todos os envolvidos, uma rápida olhada
                no relógio confirma que durou apenas cerca de 20 minutos."

                "Os hóspedes começam a se dispersar, sentando-se e retomando
                uma conversa tranquila."

                "Quando Luke coloca a mão de Astério na sua, ele dá a primeira
                e última ordem antes de renunciar seu comando: leve o Minotauro de
                volta a seu quarto para passar a noite."

                "Greta sorri, e Ismael não consegue evitar um audível suspiro de
                alívio — apenas para receber uma rápida cotovelada nas costelas por arruinar
                aquilo que poderia ter sido um belo momento."

                hide Asterion
                with Dissolve(2.0)

                "Conforme você parte, caminhando na escuridão com o minotauro a reboque,
                seus ouvidos captam alguns hóspedes dando ao grifo um forte aplauso por um trabalho bem executado."

                show Luke:
                    ease 1.0 xalign 0.5
                $Luke.change("emotion", "wink")
                $Luke.change("arm", "salute")
                "De sua visão periférica, você percebe a solene saudação de adeus
                de Luke antes que sua personalidade usual reafirme-se sob a
                renovada atmosfera festiva."

        jump chapter10Hades


    "Greta" "Você devia nos visitar quando nos estabelecermos!{w=0.3} Ou em Berlim mesmo, seria ótimo!{w=0.2}
    Imagina mostrar a todo mundo um minotauro de verdade."

    "Greta" "Se dinheiro for um problema, existem tantos albergues excelentes lá,{w=0.2}
    e você também pode alugar um lugar online se quiser privacidade."

    $Asterion.change ("emotion", "sad")

    "O minotauro olha para você. Não é mais um sinal furtivo, ele vai tão longe a ponto de
    balançar a cabeça de um lado para o outro em um pedido de socorro."

    "Você não pode deixá-lo passar por isso. É fácil inventar uma desculpa."

    you "Astério, talvez seja hora de voltarmos ao escritório.{w=0.3} Temos uma
    papelada para revisar antes de amanhã, não é?"

    show Asterion:
        ease 0.8 xalign 0.15

    asterion "Ah sim, os contratos. Com licença, Srta. Greta, lamento, mas devo voltar ao trabalho."

    "Greta" "A essa hora? Agora é bem tarde.{w=0.3} Isso não é legal, senhor [player_name],
    você não deveria tratar seus funcionários assim!"

    $Asterion.change ("emotion", "contemplative")

    you "Você poderia dizer que o Astério é um parceiro de negócios para mim, na verdade.{w=0.3}
    Estamos nessa juntos, e começar um novo negócio envolve muitas noites sem dormir."

    you "Portanto, é com grande pesar que eu devo roubá-lo."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "Se é para o hotel, fico feliz em trabalhar a noite toda."

    pause 1.0

    show Greta:
        ease 0.06 yalign 1.45
        pause 0.06
        ease 0.06 yalign 1.5
        pause 0.06
        repeat

    "Greta olha para você, depois para o minutauro, e então de volta para você. Conforme ela faz isso, você
    percebe o sorriso dela ficando mais largo até os lábios se separarem e uma risadinha estridente e desagradável surgir."

    "Os estudantes do Oriente Médio se viram, assustados com o barulho."

    show Greta:
        ease 0.4 xalign 0.9 yalign 1.5

    "Greta" "Aaaah, entendi. Então tudo bem.{w=0.2} Foi um prazer conhecê-lo, senhor Astério.{w}
    Espero que minhas perguntas não tenham ofendido você."

    "Greta pontua a frase sorrindo e fechando os olhos em um gesto tenso.
    Você falha em entender isto por um momento, mas parece que ela está tentando dar uma piscada e falhando."

    asterion "Não se preocupe,{w=0.2} estou acostumado a elas.{w=0.4} Espero que tenha uma estadia agradável conosco."

    show Asterion:
        ease 0.8 yalign 1.0

    "Você e Astério começam a se levantar, quando Greta fala mais uma vez."

    "Greta" "Ah, uma última coisa!{w=0.2} Quase me esqueci, tem wi-fi aqui?{w=0.2}
    Meu 4G não está funcionando também, não tenho sinal."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    asterion "\"Uai-fai?\""

    you "Ah, isso.{w=0.2} Não, ainda não.{w=0.2} Ainda vou resolver."

    "...Mas como? Como a internet pode ser levada a um reino mágico que simplesmente atrai as pessoas?"

    scene bg black
    with Dissolve (1.0)

    stop music fadeout (2.0)

    pause 2.0

    scene bg staircase
    with Dissolve (1.0)

    play music "music/GreekFolkSong.ogg" fadeout 2.0 fadein 2.0

    #Asterion and MC are going up to the Master's quarters
    #MC is explaining what the Cold War was, with some humour
    #this eventually leads to the MC and Asterion talking about Asterion having dinner at the same table as him
    #also leads to them talking about Asterion's fit of laughter

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    show Asterion:
        xalign 0.5 yalign 1.1
    with Dissolve (1.0)
    pause 1.0

    show Asterion:
        ease 0.2 yalign 1.0
        pause 0.06
        ease 0.2 yalign 1.1
        pause 1.0
        repeat

    you "Ok, então...{w=0.2} Soviéticos.{w=0.2} Para começar, os Aliados venceram a Segunda Guerra Mundial, mas,
    perto do final da guerra, a América revelou um novo tipo de bomba,{w=0.2}
    uma que era mais poderosa que qualquer outra fabricada antes."

    you "Depois da guerra, a Rússia conseguiu fazer uma por conta própria.{w=0.2} O problema aqui é
    que a América era capitalista e a União Soviética comunista."

    you "Eles começaram a \"Guerra Fria,\" que não era uma \"guerra\" no sentido mais estrito da palavra."

    you "Eles estavam competindo por influência sobre outros países enquanto ameaçavam uns aos outros com as bombas."

    you "Ambos tinham tantas que poderiam destruir um ao outro ao mesmo tempo—
    é o que as pessoas chamaram de \"destruição mutuamente assegurada.\"."

    you "E isso tem relação com Berlim porque, depois da Segunda Guerra Mundial, os Soviéticos e os Americanos a dividiram em dois
    {w=0.2}— com um muro entre o Leste e o Oeste."

    you "Ele dividiu famílias e comunidades por anos.{w=0.2} Mas caiu na década de 90, junto com a União Soviética.{w=0.2}
    Esse foi um grande momento para a história mundial."

    $Asterion.change ("emotion", "sad")

    asterion "Tudo isso soa tão...{w=0.2} esmagador.{w=0.3} E essas bombas,{w=0.2}
    eram do tipo que se lançava de \"aviões?\""

    you "No começo sim, mas depois foram colocadas em \"mísseis\".{w=0.3} Isto é, como posso dizer,
    uma espécie de avião não tripulado que explode quando atinge o alvo."

    you "...Foi um período muito tenso para todo mundo.{w=0.2} Mas deixamos isso para trás, na maior parte."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "Sim, sim..."

    "As vozes do salão diminuem à medida que vocês dois sobem a escada em espiral, lado a lado."

    "O ar aqui está frio agora. Uma brisa vindo do vale passa por aquela saída estreita e rochosa
    abaixo, fluindo para cima. Ela serpenteia através da fenda no meio da escadaria até roçar em
    sua pele e no pelo de Astério."

    $renpy.music.set_volume(0.5, delay=1, channel='music')

    "Não é desagradável, entretanto. O arrepio que ela envia por sua espinha o torna consciente de todo seu corpo;
    ciente de cada passo oscilante e embriagado."

    $renpy.music.set_volume(0.2, delay=1, channel='music')

    "Astério perambula com um caminhar igualmente embriagado, para a esquerda e para a direita com cada passo
    ecoando por todo o caminho até o vale."

    $renpy.music.set_volume(5.0, delay=1, channel='sound')

    #play Asterion humming
    play sound "music/AsterionHums.mp3"

    "Sem perceber, Astério começa a cantarolar — e seus passos alinham-se com o ritmo.
    Às vezes, você até sente a cauda dele roçando em sua perna."

    #idea: CG here, roughly drawn shapes climbing up the staircase
    #no fuck you Carbon, you go draw four cgs on a single build

    "Que par peculiar vocês dois formam. Milhares de vezes os Mestres e seu servo subiram e desceram
    estas escadas, mas nunca o fizeram lado a lado balançando ao ritmo da mesma música."

    "Geração após geração, o minotauro fez seu melhor para se manter nas sombras.
    Quanto menos fosse notado, menor seria a chance da ira de um senhor voltar-se contra ele."

    "Mas, olhando de longe,{w=0.2} quando não se pode distinguir bem as características e vestimenta,{w=0.2} o que
    distingue um senhor de seu súdito?"

    "Talvez apenas um par chifres e cascos. Embora... a humanidade seja bastante flexível, não é?"

    "Quão difícil é ignorar as diferenças dos outros? Os humanos são familiarizados com mudanças,
    de fato muito diferentes dos deuses que dizem tê-los criado."

    "E este servo,{w=0.2} este prisioneiro,{w=0.2} esta noite um pequeno pedaço de humanidade se agita dentro dele.{w}
    Inquietação e desejo chiam logo abaixo da superfície."

    stop sound fadeout 1.0
    $renpy.music.set_volume(0.5, delay=1, channel='music')

    "Quando Astério fala, sua voz carrega uma nova gravidade."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")
    $renpy.music.set_volume(1.0, delay=1, channel='music')
    $renpy.music.set_volume(1.0, delay=1, channel='sound')

    asterion "Mestre, você quis mesmo dizer aquilo quando falou que eu era um parceiro de negócios para você?"

    "Em sua embriaguez, você responde sem pensar duas vezes."

    you "Sim.{w=0.3} Você e eu estamos nessa juntos."

    you "Foi só impressão minha ou a ideia te agradou?"

    $Asterion.change ("emotion", "laughing")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "Ah, você tem uma boa lábia, apenas isto. Como poderia eu não sorrir com suas palavras?{w}
    Ainda assim, você tem as ideias mais bobas, meu senhor!"

    asterion "Jamais seria possível que eu pudesse ser igual a você."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    you "Mesmo que o hotel não permita,{w=0.2} vou tratar você como tal.{w} É o que importa."

    asterion "Ah, o pensamento é suficiente, meu senhor.{w=0.2} É bom saber que você se importa."

    you "É a coisa certa.{w=0.2} E eu não estou tentando ser heróico aqui,{w=0.3}
    Só estou tratando você com o respeito que um humano merece."

    you "E sobre isso..."

    you "Sinto muito por colocar você em uma situação difícil hoje.{w} Eu devia saber
    que você poderia ficar desconfortável..."

    asterion "...Mas eu queria.{w=0.2} A Srta. Greta foi complicada, mas eu gostei de
    passar a noite com os outros, meu senhor."

    asterion "Comer na mesa com companhia,{w=0.2} isto é algo do qual senti falta."

    you "Ah, então você pode agraciar {i}eles{/i} com a sua presença,{w=0.2} mas se recusa a ter uma refeição na mesma mesa que eu?"

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    show Asterion:
        ease 0.2 yalign 1.1

    "Astério faz uma pausa e olha para você com um brilho nos olhos."

    asterion "Isto é algo que você {w=0.2}realmente{w=0.2} deseja?{w} Você já me pediu isso algumas vezes."

    asterion "Comer ao lado dos hóspedes e da equipe era minha rotina,{w=0.2} mas o senhor está acima de tudo.{w}
    Dividir a mesma mesa com o Mestre..."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "É muito pouco ortodoxo."

    you "Se for algo que eu realmente queira, você faria?"

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")

    asterion "Devo obedecer todas as suas ordens, meu senhor."

    you "Digo, não como uma ordem.{w} Você,{w=0.2} por vontade própria,{w=0.2} escolheria compartilhar suas
    refeições comigo na mesma mesa?"

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "Ah...{w=0.2} Como posso dizer..."

    asterion "Eu teria vergonha disso. {w=0.2}Ficaria tímido.{w=0.2} Pode soar como uma coisa pequena para você,{w=0.2}
    mas para mim é bastante arraigado."

    asterion "Você...{w=0.2} riria de mim, se eu de alguma forma agisse como um bobo?"

    you "Bem... vou tentar não rir.{w=0.2} Mas sem garantias.{w=0.2} O que eu posso te prometer é que,
    se eu rir mesmo, vai sem com você e não de você."

    "Astério abafa uma gargalhada e tenta fingir uma certa indignação.
    Ainda assim, suas orelhas e cauda balançam alegremente."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    asterion "Seu...{w=0.2} seu patife!"

    pause 1.0

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    show Asterion:
        ease 0.2 yalign 1.0
        pause 0.06
        ease 0.2 yalign 1.1
        pause 1.0
        repeat

    "Astério ri e continua subindo as escadas."

    asterion "Muito bem. Eu posso, {w=0.2}digo, eu vou,{w=0.2} compartilhar uma refeição com você se o
    convite for estendido."

    asterion "...Café da manhã?"

    you "Sim,{w=0.2} café da manhã."

    scene bg oldquarters
    with Dissolve (1.0)
    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve (1.0)
    pause 1.0

    asterion "Os tempos realmente mudaram, e os humanos junto com eles."

    you "Então é justo que você mude também. Você é pelo menos em parte humano, afinal."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")

    asterion "...Chamar suas palavras de doces é um eufemismo, seu língua prateada!"

    you "O que,{w=0.2} agora você está se voltando contra seu Mestre?"

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "O que tem de errado com uma piada,{w=0.2} hm?"

    you "Esse é o espírito. Nada de errado em brincar um pouco."
label chapter10Hades:
    scene bg black
    with Dissolve (2.0)
    pause 2.0

    play music "music/asterion.ogg" fadeout 2.0 fadein 2.0

    $chapter = "Hades"
    call screen ChapterTransition("Hades", "O barqueiro", 'Hades')
    pause 0.5
    $save_name=output_save_name("Hades III")

    "Era como o fim de uma chuva de verão no Palácio de Knossos.
    Fios de água caindo no chão de pedra do pátio, gotas escorrendo das
    árvores para os arbustos de açafrão."

    "Os sons de pancada de gotas gordas e pés de crianças enquanto o minotauro sentava
    próximo aos pilares vermelhos, pensando. Sem fazer um barulho."

    "Pensando, como seu pai o disse para fazer. Como ele fez agora."

    "Ele havia caminhado uma dúzia de passos morro abaixo antes de perder o equilíbrio e cair de joelhos.
    Agora ele se sentava, se recompondo."

    "O minotauro olhou para o teto de pedra centenas de metros acima dele,
    chovendo as mesmas gordas gotas de água em seu focinho."

    "Sua nuca doía como se um arame de ferro em brasa o tivesse queimado.
    Sua língua e garganta estavam congeladas por um nó em seu pescoço."

    "Astério pensou, e pensou bem enquanto colhia e então aninhava uma flor de
    asfódelo em suas mãos.{w} Ele estava cercado por elas, neste prado com vista
    para uma terra labiríntica de rios."

    "Seu corpo doía, mas... quão macias são as pétalas de uma flor contra a mão de uma pessoa.
    Seu branco e rosa eram como um corte de vida nesta terra escurecida."

    "Quanto tempo ele ficou lá no Campo de Asfódelos? Ele perdeu a noção do tempo,
    mas se lembra do momento em que levantou: quando se pegou cantarolando."

    $renpy.music.set_volume(3.0, delay=1, channel='sound')
    play sound "music/AstérioHums.mp3"

    "Uma melodia sem nome ou encanto vindo de uma parte profunda de si."

    "Uma gota fria caiu na palma de sua mão e o minotauro foi despertado de seu transe."

    "Príncipe Astério, filho adotivo do Rei Minos de Creta, levantou-se e olhou para baixo na direção
    dos rios. E lá estava ele, o homem esperando na costa."

    "Desta vez, ele desceu a colina, deixando o declive guiá-lo por barrancos.
    Ele não conseguia rir, o nó em sua garganta garantia isto,
    mas espalhado em seu focinho havia um sorriso."

    "Quando o declive terminou, ele deixou que a inércia o carregasse até a costa, para o homem esquelético e seu humilde barco."

    "Nunca antes tinha Astério visto uma criatura tão sórdida.
    Sua barba, mais seca que feno e endurecida com uma imundície ofensiva aos sentidos, tocava na costa lamacenta."

    "Seus pés, afundados pela metade na lama, tinham unhas muito crescidas e amareladas que
    pareciam mais com presas."

    "Um grosso capuz cobria a metade superior de seu rosto, mas à medida que ele mexia seus pés,
    Astério teve um vislumbre dos olhos do velho homem. Eles queimavam — o homem era oco
    como uma fornalha e fedia a fumaça pungente."

    "Imundo era o deus na margem do rio e comum era para aqueles de linhagem nobre
    fugirem dele por timidez."

    "A julgar pelo sorriso de Astério, no entanto, poderia-se supor que ele viu um emissário sagrado
    coberto com roupas finas e perfumado com o aroma de flores."

    "Os cascos de Astério afundaram no solo lamacento do rio enquanto o olhar do velho deus
    rastejava sobre o híbrido."

    "Sentindo movimento, meia dúzia de caranguejos que haviam se escondido na lama
    deslizaram para longe dos dois."

    "Caronte" "Que visão peculiar.{w} Nem um homem {w=0.4}e nem um uma besta, {w=0.4}muito menos um imortal.{w} Nem um jovem cabisbaixo, {w=0.4}nem um ancião apaziguado."

    "Caronte" "Um recém-morto sorridente, {w=0.4}saltitando colina abaixo como uma ninfa."

    "Caronte" "Agora, {w=0.4}permita-me receber meu pagamento."

    "Com sua mão esquerda, o ancião fedorento segurou o pescoço do minotauro e massageou o nó dentro dele com um polegar ossudo."

    "Com a outra mão, ele alcançou dentro da boca de Astério e arrancou a obstrução de sua garganta, como uma criança arrancaria uma flor."

    "Era uma moeda de ouro, tão recém-cunhada que brilhava como uma brasa."

    "Caronte" "Você deve ter tido um bom amigo, jovem híbrido.{w=0.4} Isto funcionará bem."

    "Caronte" "Agora me diga {w=0.4}qual é a sua linhagem, {w=0.4}filho híbrido?"

    "Palavras fluíram de seus lábios como mel. O coração do minotauro saltou como um potro recém-nascido e seu rosto recuperou um pouco da cor."

    asterion "Eu sou o filho da terra e do mar espumoso. {w=0.4}Mas minha raça é estrelada, celestial.{w} Meu nome é Astério."

    asterion "Senhor Caronte, posso cruzar o rio até meu lugar de descanso?"

    "O velho passou um dedo fino por sua barba emaranhada enquanto observava o recém-morto de cima a baixo."

    "Caronte" "Muito bem.{w=0.4} Venha, devemos cruzar os rios.{w=0.4} Será um passeio pitoresco para você, por um pagamento tão generoso."

    "Caronte" "Ah... Mas que dia.{w=0.4} Um recém-morto radiando com vida,{w=0.4} sangue celestial no cadáver de uma besta,{w=0.4} um ser amaldiçoado com ouro de sobra."

    "Caronte" "Diga-me, menino.{w=0.4} Por que a alegria?{w} É justo que o broto,{w=0.2} arrancado antes da primavera,{w=0.2} amaldiçoe a mão que o deixou para murchar.{w} Ainda assim, não vejo vinagre algum,{w=0.2} apenas mel e vinho."

    "Astério sentou no barco, de costas para o homem. Ele olhou para a frente na direção da costa distante."

    "O fogo em seu peito o manteve aquecido. Ele não se incomodou em responder à pergunta do velho deus."

    stop sound fadeout (1.0)
    $renpy.music.set_volume(1.0, delay=1, channel='sound')

    stop music fadeout (1.0)
    pause (1.0)

    $chapter = "Capítulo 10"

    call screen ChapterTransition("Capítulo 10", "O alicerce")
    pause 0.5
    $save_name=output_save_name("Capítulo 10")

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    play music "music/JatoTheLion.ogg" fadeout 2.0 fadein 2.0

    scene bg oldquarters
    with Dissolve (2.0)
    pause (2.0)

    if ArgosContract == "Terrorized":

        #If Asterion panicked the previous night
        #instead of playing the breakfeast scene, play this instead
        show Asterion:
            xalign 0.5 yalign 1.0 zoom 1.0
        $Asterion.change ("emotion", "bowing")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "raised")
        "Na manhã seguinte, você encontra Astério de volta às suas funções, apesar de seu ataque de pânico
        na noite anterior."

        $Asterion.change ("emotion", "sad")
        "Qualquer tentativa de falar sobre isso é recebida com um silêncio triste de lábios fechados."

        "Depois do café da manhã, você o lembra de toda a situação da \"internet\"."

        asterion "Ah, sim. Eu me lembro agora. Deseja então que eu o leve para...
        aquele lugar do qual lhe falei?"

        pause 1.0

        $Asterion.change ("emotion", "bowing")
        asterion "Muito bem.{w=0.2} O Mestre está pronto? Podemos prosseguir?"

        you "Sim, vamos lá."

        jump chapter10bedrock

    show quartertable

    show Asterion behind quartertable:
        xalign 0.5 yalign 1.0
    with Dissolve (1.0)

    "Existem regras para a disposição dos talheres. Garfos à esquerda, facas à direita,{w=0.2}
    com o primeiro conjunto disposto do lado de fora. Colheres são colocadas à direita das facas."

    "O básico é simples, mas é fácil de errar caso você esqueça que tipo de garfo é feito
    para cada refeição."

    "No final,{w=0.2} entretanto,{w=0.2} não tem importância.
    Poucos sentam-se à mesa de jantar para admirar seus talheres brilhantes primeiro e depois a comida, afinal."

    "Mas hoje, mesmo que apenas por um momento, talheres parecem ser uma questão de colossal importância."

    $Asterion.change ("emotion", "sad")

    "Astério ignora o queijo e as bolachas, carnes curadas e ovos cozidos, as geleias e os doces.
    Seus olhos estão fixos em sua colher, a desgraça de vida que ele colocou no lado errado do prato."

    "Gotas grossas de suor escorrem de sua testa até o queixo, depois caem no colo.{w}
    Você pode ouvir um murmúrio estrondoso vindo dele, um grunhido prolongado de angústia seguido pelo minotauro
    curvando-se diante de você."

    "Ele acordou diferente hoje, cambaleante e arisco,{w=0.2}
    já se questionando sobre a escolha de tomar café da manhã com você."

    "Mas ele não desistiria de sua palavra. Agora sua angústia está cravada em seu rosto."

    if player_background == "speedrunner":
        "Você larga sua tijela de mingau de soja coberto de maionese e bufa para ele."
        you "Você parece esquisito!{w=0.2} Quase como se tivesse acabado de perder uma tentativa de bater um recorde mundial por causa de um idiota.
        Você está bem?"
    else:
        "Você larga seu pão com manteiga e sorri para ele.
        Não faria bem algum deixá-lo mais nervoso em busca por respostas;
        você precisará ser delicado."
        you "Algum problema, Astério? Você parece mal."

    pause 1.0

    $Asterion.change ("emotion", "tired")

    pause 1.0

    "Os olhos do minotauro se voltam para o prato. Ele recua ainda mais em uma bola compactada de pelo,
    com as mãos cruzadas acima das pernas."

    show Asterion:
        ease 0.05 xalign 0.501
        pause 0.05
        ease 0.05 xalign 0.499
        pause 0.05
        repeat

    "A inquietação de Astério rasteja até você e corrói sua confiança sobre a situação."

    "Uma coisa tão simples, um café da manhã. Ontem mesmo ele carregava um sorriso contagiante
    quando o acusou de abrigar uma \"língua doce.\""

    "Talvez tenha sido o vinho. A ideia deve ter agradado a ele no momento
    mas, na sobriedade, toda a vergonha de um homem retorna com uma vingança."

    "Você procura algo para dizer. Existe sequer alguma combinação de palavras que
    pode tirar vocês dois deste lamaçal?"

    "Até que ponto as palavras podem ir contra a tragédia na vida de um homem?"

    "Astério permanece com as mãos travadas no colo, olhando para baixo como se em deferência."

    "Não há grande sabedoria que possa puxá-lo, mas talvez a honestidade possa oferecer algum alívio."

    $Asterion.change ("emotion", "sad")

    you "Você não devia se sentir mal."

    $Asterion.change ("emotion", "tired")

    show Asterion:
        ease 1.0 xalign 0.5 yalign 1.1

    "O olhar dele volta para seus talheres, para a colher infame, depois de volta para si mesmo."

    you "Eu não estou falando da colher.
    Você não merece passar por esse tipo de angústia,{w=0.2} de jeito nenhum."

    you "Nós nos divertimos ontem à noite, não foi?"

    $Asterion.change ("emotion", "sad")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    you "Nada mudou desde então. Você teve um jantar agradável com os outros hóspedes.
    Você e eu estávamos na mesma mesa, a única diferença é que dessa vez nós dois estamos comendo juntos."

    $Asterion.change ("emotion", "tired")

    "Ele olha para o lado e range os dentes."

    asterion "Eu me sinto muito inadequado. Esta experiência é muito inquietante para mim."

    you "Por que?"

    $Asterion.change ("emotion", "sad")

    asterion "Como disse ontem à noite, nunca tive efetivamente uma refeição com o Mestre.
    E...{w=0.4} a colher. Eu a coloquei no lugar errado."

    you "Sobre a colher... O que podemos fazer para resolver?"

    asterion "É tarde demais, já está no lugar errado."

    you "Mas pode ser consertado?"

    asterion "...Suponho que sim."

    "Você pega a colher e coloca no lugar correto, à direita das facas."

    you "Pronto.{w=0.2} Resolvido. Um motivo a menos para você ficar nervoso."

    you "Tem mais alguma coisa incomodando você? Pode me contar."

    $Asterion.change ("emotion", "surprise")
    $Asterion.change ("rightarm", "loose")

    show Asterion:
        ease 0.05 yalign 1.0
        pause 0.05
        ease 0.1 yalign 1.1

    pause 1.0

    $Asterion.change ("emotion", "tired")

    if global_affection > 5:

        "Ele solta um suspiro prolongado. Parece derrotado no início, mas seus ombros estão
        relaxados e seus olhos entreabertos."

        asterion "Ah,{w=0.2} às vezes esqueço. O Mestre não é alguém que aceitaria
        punição física."

        asterion "Devo superar este medo, não se preocupe."

    asterion "Além de me sentir inadequado, percebo agora que...{w=0.2}
    Não quero que você me veja tendo dificuldade em usar os talheres,
    e não consigo evitar a sensação de que você ficaria irritado comigo."

    you "Irritado porque você se enrolou com um garfo e faca? E então o que aconteceria?"

    pause 1.0

    $Asterion.change ("emotion", "bowing")

    asterion "...Eu não sei. Talvez o Mestre pensasse menos de mim, vendo-me como sou."

    $Asterion.change ("emotion", "sad")

    you "Eu não penso nem um pouco menos de você."

    "Você dá uma mordida."

    you "Por que você tem dificuldade com os talheres? Ninguém nunca te ensinou?"

    pause 1.0

    $Asterion.change ("emotion", "bowing")

    asterion "Eu simplesmente nunca precisei aprender enquanto crescia... ou por muito tempo depois, na verdade."

    asterion "Não foi até alguns séculos atrás que eu sequer tinha visto garfos. Era uma novidade na época."

    asterion "As pessoas tentaram me ensinar, mas...{w=0.3} eu tenho dificuldade com movimentos delicados.
    Prefiro comer com minhas mãos."

    you "Bem, então faça isso. Não tem problema."

    asterion "Mas seria indigno de minha parte me expor desta forma, e..."

    pause 1.0

    $Asterion.change ("emotion", "sad")

    pause 1.0

    $Asterion.change ("emotion", "contemplative")

    asterion "Os tempos realmente mudaram, não é? Todo este estresse é para nada?"

    you "Sim. É difícil para mim entender por que você está tão nervoso.
    Nada do que você fez hoje, mesmo desde que eu cheguei ao Hotel, merece qualquer reação negativa."

    you "Mas... se você quiser usar os talheres, então tente.
    Não tem problema se você errar ou fizer uma bagunça."

    pause 1.0

    $Asterion.change ("emotion", "sad")

    pause 1.0

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("leftarm", "raised")

    pause 1.5

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "loose")

    "O minotauro pega os preciosos talheres em suas mãos..."

    play music "music/KoraDuet.ogg" fadeout 1.0 fadein 1.0

    $Asterion.change ("emotion", "sad")

    pause 1.0

    $Asterion.change ("emotion", "neutral")

    "E de jeito nenhum tem como isso acabar bem."

    "Você não tinha parado para assistir antes, mas...{w=0.2} a falta de jeito de Astério
    com pequenos objetos é nada menos que um crime."

    "Não se pode deixar de sentir o impulso de saltar e guiar sua mão,
    mas esse é um desafio que ele deve superar por contra própria."

    "Os talheres são tão finos que ele tem dificuldade em mantê-los entre os dedos grossos.
    Eles continuam escorregando em sua mão, também."

    "No geral, o relacionamento problemático de Astério com os talheres segue uma estrutura de três atos."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("leftarm", "raised")

    "Primeiro, ele reencontra seus dedos com o metal fino.
    Suas mãos tremem como amantes perdidos há muito tempo, tocando os lábios pela primeira vez em anos."

    $Asterion.change ("emotion", "surprise")
    play sound "sfx/clink.ogg"
    "Há uma tentativa de graciosidade, como adolescentes se atrapalhando em um momento de paixão.
    Por uma gloriosa fração de segundo, ele o segura corretamente,{w=0.5}
    e então o garfo escorrega conforme ele aplica pressão em um pedaço de queijo."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("leftarm", "loose")

    "No segundo ato, as coisas tomam um caminho para o pior. Conforme o minotauro fica novamente angustiado,
    ele se esquece de como os talheres devem ser segurados."
    play sound "sfx/clink.ogg"
    "Ele o agarra como duas canetas, ou talvez como um par de bisturi e pinças.
    Vai bem por meio minuto antes de o garfo escorregar e cair em seu copo de suco de laranja."

    $Asterion.change ("emotion", "bowing")

    "O garfo implora por ajuda, pela mão de seu precioso amante.
    Mas a mente de Astério ficou fria junto com o rio de suor escorrendo por suas
    costas e manchando sua camisa."

    "A tragédia chega no terceiro ato da peça.
    Nosso herói outrora corajoso é consumido pela dor, ira e arrogância.
    Os deuses desistiram dele, assim como ele desistiu do amor."

    $Asterion.change ("emotion", "angry")

    "Como se você não existisse, como se dignidade fosse um conceito alienígena,
    Astério segura a faca e o garfo (pegajosos de suco) como uma criança:
    agarrando a alça como se estivesse pronto para apunhalar o queijo miserável espalhado em seu prato."


    "E lá vai ele; a batalha pelo café da manhã acabou e ele está prestes a saborear sua única fatia de queijo.{w}
    Custou sua dignidade, mas este é um pequeno preço a se pagar pelo sustento."

    $Asterion.change ("emotion", "surprise")
    $Asterion.change ("leftarm", "raised")

    "Mas a humilhação nunca acaba, pois o queijo foi cortado muito fino.
    Ele parte e cai em seu colo, manchando ainda mais suas roupas."

    "Com um gorduroso {i}plap{/i} ao cair no chão, a tragédia chega ao fim."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("leftarm", "loose")

    pause 2.0

    "Quanto abuso pode um homem aguentar antes de explodir? Quão injusto o mundo pode ser?"

    "Em outros períodos da história humana, traumas tão profundos como este certamente levariam
    qualquer homem a levantar os braços contra a própria criação."

    "Não Astério, entretanto. O minotauro, criatura desgraçada, é deixado com apenas uma saída."

    #a destroyed Asterion
    asterion "...Muuu."

    pause 2.0

    you "...Você acabou de fazer{w=0.5} \"muu\"?"

    $Asterion.change ("emotion", "sad")

    "Astério olha para cima, seu rosto inundado de vergonha e constrangimento.
    Ele se solta em total derrota, uma mão errante derrubando uma maçã próxima para fora da mesa."

    $Asterion.change ("emotion", "tired")

    asterion "Pelos deuses, que dia miserável!"

    "O minotauro desvia o olhar de você."

    you "Desculpa, acho que te ouvi errado... eu poderia jurar que você, é, disse \"muu.\""

    pause 1.0

    asterion "Sim. Às vezes faço isto quan{w=0.2}-quando eu...{w=0.2} se há muito — {w=0.3}
    quando é demais..."

    asterion "É como estar no meio de uma tempestade, fico perdido e nem sempre consigo segurar...
    e então acontece."

    asterion "Eu... eu solto um \"muu\"."

    pause 2.0

    you "Isso é adorável."

    $Asterion.change ("emotion", "surprise")

    asterion "Desculpe, mas o que você acabou de dizer?"

    you "É {i}adorável!{/i} Eu não sabia que você fazia isso."

    "O conteúdo de uma xícara caída de café rasteja até a borda da mesa.
    Uma gota é empurrada para fora, duas, e então torna-se uma corrente enquanto
    cai em cascata até o chão ao lado de seu pé."

    "Antes que o copo também possa rolar para fora, você o coloca de volta para cima; com apenas um dedo,
    para não chamar a atenção de Astério para ele."

    asterion "Por que é adorável?"

    you "Só é! Você pode não concordar, mas é adorável."

    "O minotauro solta um gemido de lamentação e você aproveita a oportunidade para colocar o pé sobre
    a maçã incômoda enquanto ela tenta rolar para longe. Você a puxa de volta e a pressiona
    contra a lateral de sua cadeira."

    "Algumas gotas escorrem pela lateral do copo de suco de laranja,
    uma poça do tamanho de uma impressão digital encontra-se na base."

    asterion "De alguma forma, acho isto difícil de acreditar."

    you "Vamos lá, é um elogio."

    asterion "Por que alguém me elogiaria?{w=0.2} O que há para dizer?{w=0.2}
    Não consigo nem segurar um garfo como uma pessoa."

    you "Não faz assim,{w=0.2} você é ótimo. Ontem mesmo nos divertimos tanto.
    Gostei muito da sua companhia."

    you "E você lidou tão bem com as perguntas da Greta. Você tem jeito para situações difíceis."

    asterion "Não pode ser, o Mestre deve estar me provocando..."

    you "Pouco provável. Eu estou sendo honesto aqui..."

    "Suas palavras, entretanto, não parecem ter muito efeito.
    Talvez você precise fazer algo um pouco melhor para animá-lo."

    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    $myChoices = [("Fazer um sanduíche e comer com suas mãos.", 'sandwich'), ("Contar trocadilhos de vaca para fazê-lo rir.", 'pun')]
    if player_background == "speedrunner":
        $myChoices.append(("{color=[UIColorSpeedrunner]}(SPEEDRUNNER) Fazer uma bagunça você mesmo.{/color}", 'mess'))

    $narrator("O que você faz?", interact=False)
    $result = renpy.display_menu(myChoices)

    if result == 'sandwich':

        $Asterion.change ("emotion", "tired")

        "Você olha de volta para o campo de batalha na mesa — poças de suco de laranja,
        uma fatia de queijo jogada sobre uma xícara de café, geleia sobre as carnes curadas,
        manchas de gordura espalhadas por toda a lateral de Astério."

        "Não é, porém, mais bagunçado do que você veria em uma noite
        turbulenta em um bar com amigos."

        "E a comida, em sua maior parte, ainda deve ser segura para comer."

        "Com quatro fatias de pão e o que resta do queijo e carnes curadas
        (com a geleia raspada), você faz dois sanduíches básicos."

        "Você certifica-se de embalá-los o máximo possível antes que a coisa vaze dos lados —
        se isto será tudo o que você vai comer, nada mais justo que torná-lo abundante."

        $Asterion.change ("emotion", "sad")

        you "O que me diz de deixar toda essa bagunça para trás e desfrutar disso no nosso café da manhã?
        Não precisa usar talheres assim."

        "O minotauro cerra as mandíbulas enquanto aceita sua oferta."

        $Asterion.change ("emotion", "tired")

        "Ele se vira um pouco para o lado, evitando seu olhar, e você segue o exemplo.
        A sala se enche com o som da mastigação de vocês, interrompido uma ou duas vezes
        quando Astério estende a mão para pegar o copo de suco."

        "Os sanduíches, de todas as coisas, quebram o ar de tensão na sala.
        O que resta da geleia na carne adiciona um toque inesperado ao seu sabor salgado,
        balanceado pelo sabor neutro do queijo."

        $Asterion.change ("emotion", "sad")

        "Ao dar outra mordida, você lança ao minotauro um olhar de soslaio —
        e o encontra olhando de volta para você, depois desviando o olhar."

        "Você olha para a janela, para o horizonte laranja e azul, e então de volta para Astério.
        Desta vez, é ele quem capta o seu olhar, mas nenhum de vocês desvia."

        "Você se curva, cotovelos apoiados em seus joelhos. Apenas então você ouve o barulho
        da cauda do minotauro contra o chão."

        asterion "Obrigado. E... o sanduíche está bom."

        you "De nada."

        you "Sabe, eu poderia fazer mais sanduíches para nós de vez em quando."

        $Asterion.change ("emotion", "bowing")
        $Asterion.change ("leftarm", "raised")

        "Astério abre a boca para dizer algo, mas muda de ideia.
        Em vez disso, ele grunhe e desvia o olhar para terminar sua refeição."

        "Assim que termina, ele relaxa um pouco, apoiando as mãos entre as pernas —
        e quase manchando as calças com a melequeira de geleia, suco de laranja e óleo de queijo."

    if result == 'pun':

        you "Mas agora que você falou, eu {i}posso{/i} provocar você."

        $Asterion.change ("emotion", "tired")

        "O café continua a derramar e, ainda assim, Astério está focado demais na conversa para notar."

        asterion "O que o Mestre poderia querer dizer com isto?"

        you "Bem...seria muita maldade se eu provocasse você até o {i}{w=0.2}tauro{/i}{w=0.2}?"

        $Asterion.change ("emotion", "sad")

        pause 1.0

        asterion "Receio não ter compreendido."

        you "Ah, Astério."

        you "Right now you {w=0.2}{i}cowldn't{/i}{w=0.2} be more {w=0.2}{i}adorabull.{/i}{w}
        Nothing as small as a spill or a moo could {i}taur{w=0.2}-us{/i} apart."

        pause 1.0

        $Asterion.change ("emotion", "neutral")

        "Ele não parece estar entendendo."

        you "Mas sério, Astério..."

        "Your eyes are dead-set on the minotaur.{w=0.2}
        He can't meet your gaze without looking down to his clumsy hands,
        as if they were criminals on whom he could pin the blame."

        "Heaving a deep sigh, he can't bear to hear what might be coming next."

        you "Well, I thought that might make you {i}chuck-le{/i} a little.
        I guess I shouldn't beat {i}a-round{/i} right now."

        $Asterion.change ("emotion", "sad")

        you "I don't want to make you worry too much.{w} After all, you're much too
        {i}tender...{w=0.2}loin.{/i} The {w=0.2}{i}steaks{/i}{w=0.2} are way too high to be joking like this."

        you "{i}Steer-ing{/i} this conversation away from the problem at hand would be boring."

        you "Your punishment won't be {i}mino-ver{/i} yet."

        you "You will be in utter {i}angus{/i} once I'm done."

        "But so far it's to no avail — he remains speechless at your display of \"wit\"."

        you "There's no {i}oxen{/i} out of this one.{w=0.2} Is this punishment more {i}heif-ier{/i} than you can bear?"

        pause 1.0

        you "Come on, Astério.{w} Give me a {i}minotaur two.{/i}"

        "With a muffled groan, the defeated Astério finally entertains his master."

        asterion "Please, you're {i}toro-ing{/i} me apart."

        you "Okay, okay, you might have a point..."

        "Your fingers flick the tip of one of Asterion's horns and the Asterion shoots right up."

        you "Or two."

        $Asterion.change ("emotion", "contemplative")

        asterion "I guess, after all, you are the \"bouss\"...{w=0.8} get it?
        Because \"bous\" means \"wild bull\" in old Greek."

        pause 1.0

        $Asterion.change ("emotion", "tired")

        asterion "Soou engraçado na minha cabeça..."

        "Ele recua um pouco, apoiando a mão entre as pernas — e quase manchando as calças
        com a melequeira de geleia, suco de laranja e óleo de queijo."

    if result == 'mess':

        "Olhando para Astério com intenções nada boas, você pega a colher outrora
        irritante."

        $Asterion.change ("emotion", "neutral")

        "Astério fica quieto, quase prendendo a respiração, em questionamento sobre o que você pode fazer agora."

        "Você a traz para o pote de geleia, como se para tirar um punhado para espalhar na torrada,
        mas você continua. A colher passa sobre a manteiga, as compotas, o mel,
        até você chegar ao copo de suco de laranja."

        "Em vez disso, a colher paira sobre a jarra e a deixa intocada.
        Seu braço se estica ainda mais e a colher passa sobre a manteiga, as compotas, o mel,
        e Astério pode apenas observar enquanto a colher paira bem em cima de seu suco de laranja."

        $Asterion.change ("emotion", "surprise")

        "Você mergulha no copo e levanta uma colher cheia."

        show Asterion:
            ease 0.05 yalign 1.0
            pause 0.05
            ease 0.1 yalign 1.1

        asterion "O que você —{nw}"

        "A voz de Astério cai quando você a derrama na torrada.
        O suco respinga em sua roupa, mas você não liga."

        "Você coloca a colher para descansar no pote de geleia,
        como uma poderosa Excalibur enterrada em sua pedra antiga."

        "O horror continua à medida que você parte a torrada em pedacinhos de pão mole
        e encharcado. O suco continua pingando em suas roupas conforme você o levanta
        e coloca na sua boca."

        you "Mmmh! Delícia! Você tem que experimentar, Astério!"

        $Asterion.change ("emotion", "sad")
        $Asterion.change("rightarm", "hips")

        "Mas seu massacre ainda não acabou. Você olha em volta, procurando sua próxima vítima."

        "Você pega a faca de pão. Com sua ponta arredondada, mal consegue furar
        uma fatia de carne curada. Você a pega e mergulha na geleia."

        "Ela cai dentro da jarra e você luta para tirá-la com a faca antes que a coisa
        toda vire, esparrinhando na mesa."

        you "Ops.{w=0.2} Foi mal."

        "Você começa a perceber que está criando uma bagunça ainda maior —
        uma que Astério pode ter que limpar sozinho."

        "Mas seu cérebro subdesenvolvido não consegue manter um pensamento tão complexo por muito tempo,
        e ele desaparece em um piscar de olhos."

        you "Acho que não sou muito bom com etiqueta, não é?"

        "Astério olha para as manchas terríveis que perfuram o pano outrora brilhante e cerra os dentes para se impedir de chorar."

        asterion "Esta toalha de mesa foi tricotada por um sobrevivende da Grande Guerra como um presente pessoal para mim depois que o ajudei a recuperar o uso de seus dedos aleijados."

        you "Ei, vamos limpar isso juntos, mas deveríamos começar com você primeiro antes
        de voltar a comer."

        $Asterion.change("emotion", "tired")
        $Asterion.change("rightarm", "loose")

        asterion "Não sei se consigo depois... disso."

        you "Vamos lá, nós conseguimos. Acho que ainda não terminei de provocar você."

        "Astério respira fundo e olha para a pia antes de olhar para você.
        Parte dele percebe que você está apenas tentando ajudar, tão ansioso por agradar quanto ele normalmente está em relação ao Mestre."

        "Ele recua um pouco, apoiando as mãos entre as pernas — e quase manchando as
        calças com a melequeira de geleia, suco de laranja e óleo de queijo."


    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    you "Quer ajuda com isso?"

    $Asterion.change ("emotion", "sad")

    "Astério balança a cauda, sacode as orelhas e solta um murmúrio estrondoso de seu peito."

    "Suas pernas se movem, cascos arranham o chão — mas ele acena com a cabeça."

    "Ele estende a mão esquerda para colocá-la sobre a sua. O pelo nas costas é curto,
    mas nas articulações e no lado oposto ao polegar há manchas desalinhadas — mais grossas,
    cerca de um centímetro mais compridas."

    "É um pelo liso e firme, como se poderia esperar de sua herança bovina.
    E logo abaixo desta camada fina está sua mão, completamente humana em sua forma."

    "As unhas, no entanto, são pretas e mais grossas do que qualquer outra que você já viu."

    "Você pega um guardanapo com a mão esquerda. Conforme você limpa entre os dedos,
    o antebraço dele fica tenso e envia contrações até a palma da mão e ponta dos dedos."

    if global_affection > 4:
        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "raised")

        "Como a pata de um gato se contraindo sobre o dedo de seu dono, todos os dedos de Astério se
        contraem e curvam de uma vez só, prendendo sua mão em um aperto."

        "A palma dele está suada e as batidas de seu coração se fazem notar apesar de sua pele áspera
        e espessa."

        $Asterion.change ("emotion", "contemplative")

        "Assim que você olha para ele, sente o pelo em seu punho se eriçar,
        seguido por um murmúrio estrondoso rastejando do peito todo o caminho até sua mão."

        $Asterion.change ("emotion", "tired")

        asterion "Ah, eu sinto muito."

        "Ele solta sua mão com o mesmo ritmo deliberado e glacial com que a prendeu
        em primeiro lugar. Assim que solta você, os dedos dele seguem os seus antes de parar."

        "Você podia jurar que a respiração dele acelerou, mas não há duvidas de que ele
        puxa a cadeira para mais perto de você."

    else:
        "Eles se contraem e enrolam de uma vez só, em um movimento que não parece inteiramente voluntário."

    $Asterion.change ("emotion", "tired")

    "Quando você alcança mais para frente para limpar a fina teia dos dedos dele, sente uma certa resistência."

    "O olhar de Astério perfura sua própria mão. Ele tenta separar mais os dedos para
    permitir a você um melhor acesso, mas é como se seus nervos fossem feitos de pedra."

    "Seus dedos tremem e vacilam.{w=0.2}
    O minotauro suspira e grunhe cada vez que tenta moldar sua mão para facilitar seu trabalho."

    "Por fim, você limpa a palma da mão e — assim que seu guardanapo roça o centro
    onde as linhas se encontram — todos os dedos dele se enrolam novamente."

    show Asterion:
        ease 0.2 xalign 0.52
        pause 0.2
        ease 0.2 xalign 0.5

    "Seus movimentos são inquietos, mais como um reflexo involuntário e descoordenado que um ato intencional."

    if global_affection < 4:

        "O minotauro solta outro gemido gutural, mas possui um toque de náusea nele.
        O som é seguido pelo sacudir de sua cauda, levantando a poeira do chão para frente e para trás."

        "O minotauro se eleva sobre você — ele está curvado e mantém a cabeça inclinada
        de forma que a ponta dos chifres não fique muito mais alta do que você. Quanto à mão dele,
        poderia segurar a sua com espaço de sobra."

        "Mas a diferença em tamanho, eu suas unhas escuras e movimentos bruscos,
        não importa durante aquele segundo em que — apesar de seus chifres, focinho e cascos —
        as duas mãos humanas, sua e dele, ficam juntas como se pertencessem a um único homem."

        "Depois que acaba, você ainda sente a imagem residual da mão dele contra a sua, aquele calor persistente."

        "Você coloca o guardanapo sujo em seu prato. Olhando de lado, você
        faz uma avaliação rápida dos danos: em sua maioria, são apenas alguns
        itens caídos no chão, uma poça aqui e ali, um pedaço de queijo sob o casco dele."

        "O plip plop do café pingando cessa. Quando você olha para ele, o encontra inconsciente
        da tragédia sobre a mesa — ele está olhando para você, ou talvez olhando para atrás de você,
        para algo enterrado dentro de sua própria mente."

    else:

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "raised")

        asterion "Não consigo controlar quando você a toca assim. Simplesmente fecha como reflexo."

        you "Estou vendo.{w=0.3} Eu com certeza estou aprendendo muita coisa sobre as suas mãos hoje."

        $Asterion.change ("emotion", "contemplative")

        asterion "Suponho que esteja."

        "Ele abre a mão mais uma vez, e então você paira um dedo sobre a palma,
        ameaçando tocá-la. O olhar de Astério não mostra oposição ao que você está prestes a fazer."

        "Você roça a ponta do dedo, lento o suficiente para deixar sua unha acariciar
        as colinas e vales da palma da mão dele."

        "A mão do minotauro agarra a sua, mas desta vez sua deliberação
        presenteou Astério com um pouco da dele — os dedos dele descansam entre as articulações do topo da sua mão,
        com o dedo mindinho pendurado para o lado."

        "Ele murmura algo baixinho.
        Quando você olha para o rosto dele, encontra seu olhar perdido,
        seu peito subindo e descendo em respirações rasas."

        "Você move a mão um pouco, mas ele não quer soltar{w=0.3} — e, na verdade, há uma pequena
        pressão adicionada,{w=0.2} como se ele quisesse separar seus dedos para enlaçá-los com o dele."

        $Asterion.change ("emotion", "bowing")

        "Algo como um miado escapa de sua garganta, embora ele não pareça perceber isto."

        if result == 'pun':
            you "And you doubted me when I said you were {i}adorabull.{/i}"
        else:
            you "E você duvidou de mim quando eu disse que você era adorável."

        pause 1.0

        asterion "Uhum."

        "Ele está em um mundo completamente diferente."

        "A sensação não é nada desagradável, caso não se dê importância para a palma da mão suada.
        Na verdade, ter uma mão tão grande segurando a sua faz você
        se sentir como uma criança novamente."

        "Mais uma vez, você tenta abrir a mão e, desta vez, ele deixa —
        mas você não a solta. Com um espírito tão jovem tomando conta de sua mente,
        surge uma ideia."

        "Antes que suas mãos se separem, você puxa a dele de volta para entrelaçar seus dedos
        novamente, com os polegares apontando para cima desta vez."

        you "Você já brincou de guerra de polegares? É uma coisa que as pessoas costumavam fazer?"

        pause 2.0

        $Asterion.change ("emotion", "neutral")

        asterion "Ãhn?"

        asterion "Guerra de polegares?"

        you "Sim. É uma coisa que as crianças brincam hoje em dia... Por \"hoje em dia\" eu quero
        dizer que brincava quando estava na escola, não é de forma alguma uma coisa nova."

        you "Nós seguramos as mãos assim e..."

        "Você demonstra tentando prender o polegar dele, embora seja uma
        disputa injusta desde o início — a mão dele é como um Golias para o seu Davi."

        you "E então tentamos prender o polegar um do outro, como se estivéssemos lutando."

        $Asterion.change ("emotion", "contemplative")

        asterion "Entendo..."

        $Asterion.change ("emotion", "neutral")

        "Exceto que ele não entende. A primeira rodada que vocês jogam é definida pela
        passividade e falta de reflexos rápidos dele."

        $Asterion.change ("emotion", "neutral")

        "Na segunda, ele se sai melhor — ele coloca um pouco mais de esforço, mas
        quando se trata de uma disputa de força, ele deixa você vencer sem muita oposição."

        "Ele está se concentrando na tarefa, no entanto. Sua respiração volta à regularidade e
        seus olhos ficam mais aguçados."

        you "Você está pegando leve comigo? Vamos lá, coloque alguma resistência!"

        $Asterion.change ("emotion", "contemplative")

        asterion "Ah. Ok. Que tal isso?"

        "Desta vez, Golias esmaga a concorrência — o polegar de Astério engole o seu
        e o domina."

        $Asterion.change ("emotion", "smiling")

        asterion "Pronto. Assim?"

        you "Isso!{w=0.2} Agora, que tal um melhor de três?"

        "A mão dele pode ser maior que a sua e coberta de pelos, e a unhas podem ser
        escuras como carvão, mas, enquanto você se entrega a tal momento de brincadeira infantil,
        é fácil deixar o mundo derreter ao seu redor."

        "De que Astério gostava de brincar quando era criança? Guerra de polegares
        pode não ter sido uma das brincadeiras, mas desperta algo nele mesmo assim."

        "Ele sorri, dá uma risadinha, sacode as orelhas e balança o rabo.
        É difícil dizer com certeza, mas até suas bochecas parecem um pouco coradas agora."

        "Esses intervalos de admiração infantil não podem durar muito, entretanto.
        O cômodo ainda está uma bagunça."

        $Asterion.change ("leftarm", "loose")

        "Depois da pausa (Astério venceu) vocês dois arrumam o lugar,
        carregando ainda a dor nas bochechas que aparece quando se ri demais."

        "Às vezes, ele lhe lança um olhar desavergonhado, sem nenhuma tentativa de disfarçar."

    hide quartertable
    with Dissolve (2.0)

    pause 2.0

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    pause 1.0

    asterion "O Mestre acreditaria em mim se eu dissesse que você me lembra...{w=0.2} de um velho amigo?"

    you "Sério? Como ele era?"

    pause 1.0

    asterion "...Talvez este seja um assunto para outra hora. Temos nossos deveres
    a cumprir, não é mesmo?"

    asterion "...E eu também tenho uma bagunça para limpar."

    "Você dá uma boa olhada no chão."

    you "Receio que você esteja certo. Na verdade, temos uma missão especial para hoje,
    uma de importância excepcional."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "loose")

    asterion "É mesmo? Ora, o que meu sábio senhor tem em mente?"

    you "Bem, você se lembra da nossa conversa ontem à noite sobre \"a internet\"?
    Isso é o que precisamos fazer: conectar esse lugar solitário ao mundo exterior."

    you "Hoje em dia, todo hóspede espera ter uma conexão de internet sempre que passa por um hotel.
    Precisamos nos manter atualizados com os tempos modernos."

    asterion "Ah, sim. Eu me lembro agora. Você deseja então que eu o leve para...
    aquele lugar que lhe contei sobre?"

    pause 1.0

    asterion "Muito bem.{w=0.2} O Mestre está pronto? Podemos prosseguir?"

    you "Sim, vamos lá."

label chapter10bedrock:
    "Astério caminha até a porta que leva de volta à escada, mas para."

    $renpy.music.set_volume(3.0, delay=1, channel='sound')
    play sound "music/AsterionHums.mp3"

    pause 2.0

    "Você ouve o mais fraco som. Ele está cantarolando?"

    show blackback:
        alpha 0.0
        linear 0.2 alpha 0.5
        pause 0.2
        linear 0.1 alpha 0.0
        pause 0.1
        linear 0.2 alpha 0.7
        pause 0.2
        linear 0.1 alpha 0.0
        pause 0.1
        linear 0.2 alpha 1.0
        pause 1.0
        linear 0.5 alpha 0.0
    play sound "sfx/hum.ogg"
    pause 3.0

    stop sound fadeout 1.0
    $renpy.music.set_volume(1.0, delay=1, channel='sound')

    "E então a porta se fecha e o que você vê do lado de fora não se parece em nada com a luz convidativa da escada."

    stop music fadeout 2.0

    scene bg black
    with Dissolve(3.0)

    "Um túnel se estende à sua frente, descendo. Suas paredes são de pedra bruta."

    play music "music/CrossingTheAstralBridge.ogg" fadeout 2.0 fadein 2.0

    "Astério anda como se não houvesse nada fora do comum no que acabou de acontecer.
    Ele lhe dá apenas um breve olhar, convidando-o a segui-lo."

    "Assim que você cruza a porta, o próprio ar ao seu redor muda."

    "Uma umidade pungente atinge você como um caminhão. Ela abre sua boca e queima seus pulmões."

    "Todo o Hotel até agora tinha um ar tão seco que poderia fazer seu nariz sangrar, mas este lugar já está
    cobrindo sua pele em uma camada de suor e fuligem. O simples fato de estar aqui faz você se sentir sujo."

    "Mas Astério continua indo, e você o segue a uma certa distância.
    A luz da porta atrás de você vai ficando mais fraca e,
    quanto mais longe vocês vão, mais altos são os passos do minotauro."

    "Vocês dois viajam por um labiríntico conjunto de voltas e viradas e, com
    cada mudança de ambiente, as paredes vão se transformando em rocha polida."

    "O ar piora a tal ponto que você precisa fazer esforço para não tossir.
    Apesar de tudo, sua língua está coberta por um óleo amargo que você não consegue engolir nem cuspir."

    "O som áspero dos cascos de Astério contra a pedra, ecoando por
    todo o corredor, é tanto um convite para prosseguir como um som
    não natural espantando você deste lugar."

    "Isto é, até o minotauro pisar em algo quebradiço."

    play sound "sfx/crack.ogg"
    "Você arrasta os pés ao longo do chão e consegue sentir a textura da pedra mudar. Sua suavidade anterior
    deu lugar a uma superfície mais dura e áspera que raspa contra suas solas."

    scene Bedrock
    with Dissolve (4.0)

    "Os corredores claustrofóbicos dão lugar a uma grande câmara. É mais escuro do que qualquer outro cômodo que
    você viu no hotel até então, exceto talvez pela câmara fria. Mas a luz de alguma fonte que você não consegue determinar bem ainda permite que você examine a câmara em todos os detalhes."

    "O piso e as paredes de pedra polida, mesmo no caminho que leva aos corredores anteriores, são cobertos por uma fina camada de
    poeira roxa. As camadas ficam cada vez mais grossas conforme seus olhos as seguem até o centro da sala, onde uma grande parede de
    rocha cristalina daquela mesma cor escura corta o cômodo pela metade."

    "À direita e à esquerda, há duas grandes mesas de madeira nas quais várias
    pessoas poderiam trabalhar juntas. Os pés também estão cobertos de poeira roxa e
    parecem estar grudados no chão por pedaços de cristal acumulado."

    "Livros, esboços, documentos e esquemas estão espalhadoss pelas mesas,
    e um velho vaso com penas de escrever feitas com penas de pavão encontra-se em meio à bagunça."

    "Colunas de pedra ao longo da parede sustentam o teto sombreado. Elas, também, estão cobertas de poeira, mas
    a tinta vermelha e preta que fica por baixo é brilhante e fresca."

    "A parte intermediária do piso da sala é peculiar.{w} Parece ter sido uma piscina rasa algum dia,
    30 centímetros mais fundo que o chão ao redor.{w} Mas agora está seca e coberta por grossos crescimentos de rocha roxa."

    "Bem no centro da câmara encontra-se uma larga bacia consumida pela mesma rocha."

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    show Asterion:
        xalign 0.0 yalign 1.0
    with Dissolve(1.0)

    pause 1.0

    asterion "Aqui está. Chamamos este lugar de \"o alicerce.\"
    A pedra que você vê é uma forma de obisidiana."

    asterion "Este lugar é tão antigo quanto o labirinto. Sempre existiu."
    play sound "sfx/crack.ogg"
    "Você esfrega a mão na parede de cristal. A pedra é quebradiça e, com uma pincelada de seu dedo
    você arranca um fragmento."

    $Asterion.change ("emotion", "tired")
    $Asterion.change("rightarm", "hips")

    "Apenas esfregá-lo entre as pontas dos dedos o transforma em um pó grosso que suga a umidade do ar."

    "Ao prosseguir examinando, você sente que a mancha deixada em sua mão é irregular.
    Há locais com um preto oleoso e pústulas vermelhas aquosas."

    show Asterion:
        ease 1.0 xalign 0.1 yalign 1.0

    asterion "Meu senhor, isto... {w=0.2}é sujo. Coberto de poeira e sujeira com séculos de idade.
    Para seu próprio bem, eu aconselharia não tocar na obisidiana."

    you "Ah.{w=0.3} Bem pensado."

    "Você esfrega a mão na camisa."

    asterion "Obrigado. Prefiro não ver o Mestre entrando em contato com substâncias
    impuras. Eu recomendaria ainda que você trocasse de roupa assim que voltamos."

    show Asterion:
        ease 1.0 xalign 0.2 yalign 1.0

    "O minotauro dá um passo em sua direção, ficando entre você e a parede de cristais escuros."

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")

    asterion "Podemos prosseguir? A bacia no centro da sala, é o que usamos para o rádio."

    you "Este é o \"equipamento\" que transmite sinais de rádio?"

    asterion "...Suponho que seja uma maneira de se colocar. Uma descrição mais apropriada é que esta
    é a ligação do domínio com o mundo exterior."

    "Você dá uma olhada na bacia. É difícil saber com certeza, já que está coberto
    de pedra escura, mas é quase como se não houvesse fundo."

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "Esta sala é o lugar mais próximo do mundo exterior,{w=0.2}
    se podemos dizer isto. Ela opera por diferentes regras."

    asterion "Milênios atrás, era um santuário para o deus Hermes, padroeiro do comércio e dos mensageiros.{w=0.2}
    Há outros locais como este no domínio dedicados a deuses específicos."

    asterion "Os Mestres por muito tempo o usaram como um cais, para enviar e receber mercadorias
    do mundo exterior. Em seguida, tornou-se uma sala de correios quando o hotel foi estabelecido."

    asterion "Se você puder oferecer instruções adequadas, ela encontrará uma maneira de transportar
    mercadorias de ida e volta."

    asterion "Poderia receber sinais de rádio de fora depois que a instruíssemos sobre como eles funcionam."

    asterion "Se você puder descrever {i}como{/i} a internet funciona, então pode ser feito."

    asterion "Isto conectará {i}o domínio{/i} à... {w=0.2}o que quer que seja a internet.
    Então, se for de alguma forma parecida com o rádio, pode retransmitir sinais para seus...{w=0.2} equipamentos."

    you "Hum.{w=0.2} E como podemos ensinar a bacia a fazer isso? Qual é o procedimento?"

    asterion "Um contrato."

    $Asterion.change ("emotion", "bowing")

    show Asterion:
        ease 3.0 xalign 0.5 yalign 1.0


    asterion "Sim. Tudo neste domínio funciona por meio de contratos,
    principalmente aqueles assinados pelo Mestre. Sua vontade, salvo algumas exceções, é soberana."

    asterion "Em um único contrato, podemos descrever como a internet funciona e,
    em seguida, comandar o hotel — através da bacia — para conectar-se a ela."

    you "Ei, isso é meio que como programar um computador."

    $Asterion.change ("emotion", "neutral")

    asterion "Perdão?"

    you "É como os computadores funcionam, isso que quero dizer. Eles seguem suas instruções, nada mais."

    you "Se você der instruções erradas a um computador, eles não vão funcionar. Você precisa ser muito preciso,
    dizer passo a passo, na própria linguagem dele, o que precisa fazer."

    asterion "Sim, Suponho que sua comparação seja adequada. É assim de fato que o hotel funciona..."

    asterion "O que me lembra, eu ainda não lhe dei instruções sobre como invocar objetos, não é?"

    you "Sim. Já estou aqui há alguns dias e... aham, eu realmente gostaria se você
    pudesse me ajudar com isso."

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")

    asterion "Lamento terrivelmente por minha negligência, meu senhor.
    Não fosse pelas circunstâncias excepcionais em que nos conhecemos,
    eu teria lhe ensinado em seu primeiro dia como Mestre."

    you "Não se preocupe com isso. Agora, me conte... como funciona?"

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "loose")

    asterion "Muito bem.{w=0.2} Para começar, o labirinto pode gerar a maioria dos materiais
    e substâncias encontrados na natureza. Isto inclui produtos de origem animal e vegetal."

    asterion "Também pode gerar seres vivos... mas por uma série de motivos esta função foi desativada. É uma longa história, podemos discuti-la em outro momento."

    asterion "O labirinto pode gerar estruturas completas e objetos manufaturados,
    se você puder instruí-lo sobre como tal coisa pode ser construída com matérias primas."

    asterion "Para roupas, temos um grande arquivo de instruções.
    Você pode confiar no hotel para fabricar até mesmo trajes complexos sem problemas."

    asterion "Ele não pode, entretanto, fabricar moeda. Nem produzirá metais como ouro
    ou prata em grandes quantidades, e algumas outras substâncias que eram utilizadas no comércio quando o domínio foi criado."

    asterion "E caso uma grande massa de bens produzidos pelo labirinto for exportada
    para o mundo exxterior, ele pode se tornar rebelde e recusar a obedecer ordens por um tempo."

    asterion "Os deuses colocaram estas restrições em vigor para impedir os mortais de usar o
    labirinto para obter lucro."

    you "Entendo... mas não é uma restrição muito efetiva, não é?{w=0.2}
    Consigo imaginar uma série de coisas que poderiam ser exploradas caso eu quisesse lucrar."

    you "Não podemos fazer ouro e prata, claro, mas e quanto às pedras preciosas?{w=0.2}
    Elas são valiosas o suficiente para que possamos exportar uma quantidade pequena por um alto lucro."

    $Asterion.change ("emotion", "contemplative")

    asterion "Ah, sim, bem pensado{w=0.2}. Isto é o que costumávamos fazer, na verdade."

    $Asterion.change ("emotion", "neutral")

    asterion "Tínhamos um contato externo que recebia nossas pedras preciosas, vendia sem deixar rastros
    e mandava a moeda de volta."

    asterion "Desta forma, podíamos pagar nossos empregados — e não éramos avarentos de forma alguma, devo acrescentar."

    you "Interessante. Então, todo esse sistema é, digamos, abusável?"

    asterion "Sim, meu senhor, não há dúvidas quanto a isto.
    Afinal, não foi isto que nos permitiu construir este estabelecimento?"

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    asterion "Os deuses me sentenciaram à danação eterna, mas encontramos uma maneira de
    fazer algo de bom com isto."

    asterion "E conseguimos, digamos, sendo bastante criativos e ligeiros ao interpretar as regras básicas que eles estabeleceram."

    asterion "Não é diferente de como conseguimos trazer o rádio para o Hotel.
    Duvido que alguma vez Hermes tenha imaginado as utilidades que poderíamos encontrar para seu santuário."

    asterion "É uma sorte que os deuses foram, digamos, bastante desleixados com a forma
    como redigiram as regras para este domínio."

    $Asterion.change ("emotion", "neutral")

    asterion "Ah, há mais uma coisa. O labirinto pode reunir materiais,
    mas, como eu disse, precisa de instruções sobre como colocá-los juntos."

    asterion "Para coisas tais como livros... ele pode copiar os que já existem aqui,
    mas não pode invocar um livro que não conhece."

    $Asterion.change ("leftarm", "loose")

    asterion "Dito isso, posso ensinar meu senhor como a invocação é feita?"

    you "Sim, estou pronto. Vamos em frente."

    asterion "É uma tarefa simples."

    $Asterion.change ("emotion", "contemplative")
    pause 1.0

    asterion "Ah, talvez você ache bobo. Mas acredite em mim, para esta tarefa você precisa apenas...
    {w=0.3}cantarolar. Esta música em particular."

    $renpy.music.set_volume(4.0, delay=1, channel='sound')
    play sound "music/AsterionHums.mp3"

    pause 2.0

    "O minotauro começa a cantarolar uma melodia lenta e prolongada."

    "O cantarolar de Astério às vezes estremece, perdura, se estende.
    A música em si é simples, fácil de aprender e bem diferente do que você ouviria de músicos modernos."

    "Embora ele não cante nenhuma letra, parece que está pensando nelas e cantarolando em uníssono."

    pause 2.0

    stop sound fadeout 2.0
    $renpy.music.set_volume(1.0, delay=1, channel='sound')
    "Depois de repetir a música mais duas vezes, ele para."

    asterion "Precisamos chamar o labirinto, informá-lo que estamos fazendo uma demanda.
    Exigimos um gesto inequívoco."

    asterion "Ao longo dos séculos, os Mestres empregaram uma série de ações para isto,
    tais como estalar os dedos ou bater os pés."

    asterion "Mas meu senhor pode imaginar como era problemático quando eles involuntariamente
    davam ordens para o hotel."

    $Asterion.change ("emotion", "smiling")

    asterion "Portanto, há alguns séculos, adotamos esta música como gesto.
    O Mestre precisa apenas cantarolar...{w=0.3} Com o tempo, você até poderá fazer isto sem que
    ninguém perceba."

    asterion "Se eu estiver por perto, posso cantarolar para você também.
    Funciona da mesma maneira — cantarolei em seu lugar quando você tentou invocar roupas para mim."

    asterion "E agora, diga o que você deseja."

    "Você repete a música que Astério acabou de cantarolar, e..."

    "Você pensa em algo simples que pode invocar para testar as habilidades do labirinto.
    Talvez um pequeno presente para o minotauro."

    $myChoices = [("Um lenço de pescoço.", 'neckerchief'), ("Uma pulseira.", 'wristband')]
    if player_background == "speedrunner":
        $myChoices.append(("{color=[UIColorSpeedrunner]}(SPEEDRUNNER) Um medalhão.{/color}", 'medallion'))

    $narrator("Escolha um item para criar para Astério.", interact=False)
    $result = renpy.display_menu(myChoices)

    if result == "neckerchief":
        "Você pensa de volta sobre as roupas modernas que fez para Astério usar.
        Fabricar tecidos, ao que parece, é uma tarefa simples para o labirinto."

        "Mas, ao contrário daquele momento, onde Astério aparentemente comandou o labirinto para executar
        suas instruções em seu lugar, você faz isto sozinho."

        "Você fecha os olhos, visualiza na mente um simples pedaço de pano, e cantarola a melodia."

        pause 1.0

        show blackback:
            alpha 0.0
            linear 0.2 alpha 0.5
            pause 0.2
            linear 0.1 alpha 0.0
            pause 0.1
            linear 0.2 alpha 0.7
            pause 0.2
            linear 0.1 alpha 0.0
            pause 0.1
            linear 0.2 alpha 1.0
            pause 1.0
            linear 0.5 alpha 0.0
        play sound "sfx/creak.ogg"

        "Você sente a mudança familiar das luzes na sala, mas desta vez o piso de ladrilhos
        também vibra sob seus pés."

        "As rochas escuras ao seu redor estalam, como carvão estalando ao ser jogado
        em uma fogueira."

        "Em seguida, você se assusta com a sensação das pedras se estilhaçando e caindo sobre você —
        mas quando abre seus olhos, a parede está intacta e inalterada."

        "Talvez porque você esteja muito profundamente no coração do labirinto, dentro de sua camada mais baixa."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        "Indendentemente disso, você olha para baixo. O labirinto produziu um pequeno quadrado de tecido
        de algodão vermelho com um padrão espiralado branco nas bordas."

        show Asterion:
            ease 3.0 zoom 1.1 yalign 2.5

        "O minotauro se aproxima de você e olha para ele também."

        asterion "Ora ora, esse é um padrão que não vejo há um tempo."

        "Você pega duas pontas opostas do pano, dobra-o diagonalmente e toma vantagem
        da proximidade de Astério."

        $Asterion.change ("emotion", "surprise")
        $Asterion.change ("rightarm", "loose")

        $Asterion.change("neckwear", "neckerchief")
        $wardrobe.add("neckwear", "neckerchief")

        "Você envolve as duas pontas em volta do pescoço dele e as amarra nas costas.
        O minotauro estremece, mas não se afasta e apenas deixa acontecer.
        Quando você remove suas mãos e examina sua obra, ele está corando."

        $Asterion.change ("emotion", "contemplative")

        asterion "O-obrigado Mestre. Combina comigo?"

        you "Sim, parece ótimo."

        $Asterion.change ("emotion", "smiling")

        show Asterion:
            ease 2.0 zoom 1.0 yalign 1.0


        $ global_affection += 0.5


    elif result == "wristband":

        "Você imagina uma pequena pulseira. Se o labirinto pode invocar equipamentos
        de cozinha ou artigos de vestuário modernos, algo simples como algumas
        miçangas e um pouco de linha não deve ser difícil de fazer."

        "Você fecha os olhos e cantarola a mesma música que Astério murmurou antes."

        pause 1.0

        show blackback:
            alpha 0.0
            linear 0.2 alpha 0.5
            pause 0.2
            linear 0.1 alpha 0.0
            pause 0.1
            linear 0.2 alpha 0.7
            pause 0.2
            linear 0.1 alpha 0.0
            pause 0.1
            linear 0.2 alpha 1.0
            pause 1.0
            linear 0.5 alpha 0.0
        play sound "sfx/creak.ogg"

        "Você sente a mudança familiar das luzes na sala, mas desta vez o piso de ladrilhos
        também vibra sob seus pés."

        "As rochas escuras ao seu redor estalam, como carvão estalando ao ser jogado
        em uma fogueira."

        "Em seguida, você se assusta com a sensação das pedras se estilhaçando e caindo sobre você —
        mas quando abre os olhos, a parede está intacta e inalterada."

        "Talvez porque você esteja muito profundamente no coração do labirinto, dentro de sua camada mais baixa."

        "E aí está. Não é um design complexo, apenas algumas miçangas de madeira preta
        e anéis metálicos com um cordão passando por eles."

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        "Astério olha para o que você fez e sorri."

        asterion "Nada mal para sua primeira tentativa."

        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "raised")

        "Você olha para o minotauro e pega sua mão. Ela fica mole com o seu toque —
        você sente todo o corpo dele relaxar enquanto você amarra a pulseira para ele."

        $Asterion.change("armwear", "wristband")
        $wardrobe.add("armwear", "wristband")

        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        asterion "O-obrigado, Mestre. Combina comigo?"

        you "Sim, parece ótimo."

        $ global_affection += 0.5

    elif result == "medallion":
        "Este é um bom momento para dar a Astério um pequeno gesto de agracimento por
        seus serviços nestes últimos dias."

        "Algo simples que ele possa gostar. Você estuda cada característica dele —
        o formato de sua cabeça, a curva de seus chifres, o tamanho de seus olhos."

        "O olho de sua mente captura sua aparência e, em seguida, a imbui com um toque de conforto e
        afeição tirado de seu próprio coração."

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        "O minotauro olha de volta, preocupado com seus olhos entreabertos e testa franzida
        enquanto você cantarola a melodia em voz alta."

        show blackback:
            alpha 0.0
            linear 0.2 alpha 0.5
            pause 0.2
            linear 0.1 alpha 0.0
            pause 0.1
            linear 0.2 alpha 0.7
            pause 0.2
            linear 0.1 alpha 0.0
            pause 0.1
            linear 0.2 alpha 1.0
            pause 1.0
            linear 0.5 alpha 0.0

        play sound "sfx/creak.ogg"
        "Você erra todas as batidas e faz alguns ruídos estranhos com o nariz enquanto o controle
        do fluxo de ar se perde um pouco. Uma bolha de ranho escapa de suas narinas."

        "Mas parece funcionar, quando você percebe o familiar piscar das luzes e um
        leve estrondo sob seus pés."

        "Você abre as mãos e encara sua criação."

        "Você não pode deixar de sorrir e se alegrar um pouco com suas habilidades artísticas.
        Você até incluiu um cordãozinho fofo para Astério usar a sua criação."

        show Asterion:
            ease 3.0 zoom 1.1 yalign 2.5

        "Você se aproxima de Astério e entrega a ele o medalhão."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        asterion "Ah, isto é para mim, Mestre?"

        you "Sim, você gostou?"

        $Asterion.change ("emotion", "neutral")

        asterion "Por favor, me desculpe, mas... estou confuso. Isto deveria ser eu?"

        you "Sim!"

        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "loose")

        if Asterion.fur != 'brown':
            asterion "Eu-eu entendo. {w=0.4}Você tomou algumas... liberdades artísticas.
            Eu não acho que meus chifres sejam assim, meu pelo não é mais marrom
            — a seu pedido, devo lembrá-lo — e... bem..."
        else:
            asterion "Eu-eu entendo. Você tomou algumas... liberdades artísticas.
            Eu não acho que meus chifres sejam assim, e... bem..."

        pause 1.0

        $Asterion.change ("emotion", "sad")

        asterion "...meus olhos não estão assim no momento."

        you "Bem, agora não estão, mas não vão ficar assim para sempre, vão?"

        $Asterion.change ("emotion", "contemplative")

        "Ele dá uma olhada. Mesmo para algo feito apenas com a mente,
        suas impressões digitais estão evidentes por toda parte; até a inscrição na parte de trás
        parece ter sido feita com uma unha."

        "Um trabalho desajeitado de mãos dedicadas. Astério examina as marcas de seu polegar;
        as bochechas trabalhadas demais — sinceramente trabalhadas demais; e o focinho redondo como o de um bezerro.
        Os chifres, mesmo que desiguais, foram feitos à imagem dele."

        "Ele suspira, olha nos olhos do medalhão, e murmura:"

        asterion "Não olhes para o topo da montanha a qual miras\nMas de volta para cada passo que extasiado destes."

        you "O que?"

        asterion "Nada{w=0.5} — Apenas, suponho que não será para sempre, sim.
        Obrigado, Mestre.{w=0.3} É um doce gesto."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        $Asterion.change("neckwear", "medallion")
        $wardrobe.add("neckwear", "medallion")

        "Astério pega o colar e o coloca."

        "A corda azul é um pouco curta demais para a cabeça dele, então fica
        presa em um de seus chifres no início. Mas depois de algumas tentativas, o medalhão
        repousa em seu peito, seu sorriso malformado combinando com
        o sorriso gentil do verdadeiro minotauro."

        show Asterion:
            ease 2.0 zoom 1.0 yalign 1.0

        $ global_affection += 1.0

    pause 3.0

    you "Tudo bem, chega de ficar à toa."

    you "Que tal começarmos com a coisa da internet? Por onde sequer começamos?"

    hide Asterion
    with Dissolve(1.0)
    pause 3.0
    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")
    show Asterion
    with Dissolve(1.0)

    "Astério pede licença para voltar aos corredores emaranhados e
    retorna alguns minutos depois com uma pasta cheia de esquemas."

    "Ele os coloca sobre as duas mesas."

    if player_background in ["math", "tech"]:
        "Mesmo com sua experiência, você leva um minuto para fazer sentido deles —
        parece que eles se tratam sobre receber e transmitir sinais de rádio."

        "Mesmo que você não consiga entender os detalhes, ele parece seguir uma espécie de design modular
        — cada parte do processo é compartimentalizada com bastante
        documentação em volta."

        "Não seria exagero dizer que, talvez, parte desta estrutura possa ser reaproveitada para
        trazer internet ao hotel."

    elif player_background == "speedrunner":
        "Eles têm desenhos muito bonitos."
    else:
        "Astério permite que você verifique sem interrupções. Você não consegue fazer sentido deles
        — é apenas uma bagunça confusa de desenhos geométricos e cálculos."

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "loose")

    "Pela próxima hora, você e Astério tentam decifrar o quebra-cabeça."

    $Asterion.change ("emotion", "contemplative")

    "Ele explica para você como uma equipe, décadas atrás, fez esses esquemas para traduzir o
    funcionamento de um rádio no \"alicerce\" do hotel."

    "E você, por sua vez, tenta explicar da melhor maneira possível como a internet funciona."

    $Asterion.change ("emotion", "tired")

    "Torna-se aparente que, independentemente de sua experiência anterior, há muito mais detalhes minuciosos sobre
    o funcionamento da internet que você não consegue descrever de memória."

    "Isto vai exigir um pouco de pesquisa. E se for apenas você e Astério, levaria dias ou semanas para concluir."

    "Sua concentração é interrompida quando você ouve o estremecimento de rocha movendo contra si mesma
    bem atrás de você."

    "Você se vira, mas nada mudou — ainda é a mesma sala escura e úmida."

    $Asterion.change ("emotion", "neutral")

    asterion "Algum problema?"

    you "Eu poderia jurar que ouvi alguma coisa se movendo atrás de mim..."

    asterion "Receio não ter ouvido nada, meu senhor. Talvez você esteja apenas ficando cansado."

    you "Talvez seja o caso. Se importa se dermos uma pequena pausa?"

    asterion "Sim, sobre isto...{w=0.5} o Mestre estaria disposto a ouvir uma sugestão
    impertinente deste servo?"

    if global_affection <= 4:
        you "Claro, vá em frente."

    else:
        pause 2.0
        $Asterion.change ("emotion", "laughing")
        "Antes que você tenha a chance de responder, ele solta uma risadinha."
        $Asterion.change ("emotion", "contemplative")
        asterion "Ah, estou apenas brincando. Presumo que você estava prestes a me dizer para não
        referir a mim mesmo como servo deste modo."
        $Asterion.change ("emotion", "smiling")
        asterion "Também posso ser espirituoso, meu senhor todo-poderoso. Agora, indo direto ao ponto..."

    $Asterion.change ("emotion", "neutral")

    asterion "Sabe, já é um pouco tarde da manhã e novos hóspedes podem chegar em breve.
    Se nós dois ficarmos aqui para trabalhar nesta tarefa, então quem os receberá no saguão?"

    asterion "O processo de redação do contrato exige bastante conhecimento específico,
    portanto, eu deveria ficar aqui para fazê-lo."

    asterion "Podemos talvez recrutar [first_guest] para me ajudar enquanto você cuida da recepção?"

    you "Parece razoável."

    you "Não tenho certeza se ele sabe muito sobre a internet... mas pode ser capaz de te dar uma mãozinha,
    até certo ponto."

    play music "music/GreekFolkSong.ogg" fadeout 2.0 fadein 2.0

    $persistent.main_menu_files = True
    $persistent.main_menu_files_contract = True
    $persistent.main_menu_files_tech = True
    $UI_permissions['files'] = True
    $UI_permissions['file_contracts'] = True
    $UI_permissions['file_tech'] = True
    $UI_permissions['rd'] = True

    "Agora você pode atribuir hóspedes à equipe de {color=[UIColorOrange]}Pesquisa e Desenvolvimento{/color}."

    $myChoices = [("Ver tutorial.", 'yes'), ("Pular tutorial.", 'no')]
    if player_background == "tech":
        $myChoices.append(("{color=[UIColorTech]}Regras especiais para Tecnologia.{/color}", 'tech'))
    if player_background == "math":
        $myChoices.append(("{color=[UIColorMath]}Regras especiais para Matemática.{/color}", 'math'))
    if player_background == "humanities":
        $myChoices.append(("{color=[UIColorHumanities]}Regras especiais para Humanas.{/color}", 'humanities'))

label tutorial1:

    $narrator("Ver o tutorial de formação de equipes?", interact=False)
    $result = renpy.display_menu(myChoices)

    if result == 'yes':
        contract "No início de cada dia dentro do jogo, você terá a chance de designar
        alguns de seus hóspedes para uma equipe e realizar tarefas para aprimorar o hotel."

        contract "A {i}{color=[UIColorOrange]}Equipe de P&D{/color}{/i} pesquisará projetos
        de tecnologia para expandir as capacidades do hotel, ou elaborar novos contratos que modifiquem as
        regras do hotel."

        show image "gui/teamexplanation.jpg":
            xalign 0.5 yalign 0.4

        contract "Para atribuir um hóspede a uma equipe na tela de gerenciamento, clique/toque em seu ícone (1),
        e então selecione a opção apropriada (2)."
        "Da mesma forma, você pode dispensar um hóspede já atribuido a uma equipe clicando/tocando
        em seu ícone na equipe e selecionando a opção 'dispensar'."

        contract "Cada hóspede possui um conjunto de atributos: tecnologia e contratos. Quanto maior for o atributo,
        mais um hóspede pode contribuir para a conclusão de um projeto de cada tipo."

        hide image "gui/teamexplanation.jpg"

        contract "A cada sessão, o atributo total de sua equipe será gasto trabalhando para obter uma recompensa,
        como concluir um projeto de tecnologia ou elaborar um contrato."

        contract "Cada recompensa precisa de um requisito de atributo que deve ser cumprido para que você possa obtê-la.
        Se sua equipe não consegue chegar a esse total, não se preocupe!
        Seu progresso na obtenção de uma recompensa continuará em sessões futuras."

        $myChoices[0] = ("Repetir explicação.", 'yes')

    if result == 'tech':
        you "Se vamos desenvolver projetos de tecnologia,
        tenho certeza que posso ajudar com isso."
        contract "Sua experiência em tecnologia adiciona 2 pontos passivos extras em Tecnologia!"

    if result == 'math':
        you "Essa coisa toda está me dando flashbacks de pesquisa operacional...
        Não é minha primeira vez lidando com otimização de modelo."
        contract "Seu conhecimento em matemática permite que você veja quantas recompensas possíveis
        uma composição de equipe renderá. Isto ajudará você a otimizar sua equipe!
        Você também pode ver os pontos acumulados em cada atributo."

    if result == 'humanities':
        you "Aposto que posso ajudar a equipe com esses Contratos."
        contract "Sua experiência em humanas adiciona 2 pontos passivos extras a Contratos!"

    if result != 'no':
        jump tutorial1

    "Você pode ver este tutorial a qualquer momento no menu de ajuda."

    if player_background == "tech":
        $inventory.increase_passive_bonus('Tech', 2)
    if player_background == "humanities":
        $inventory.increase_passive_bonus('Contract', 2)

    if first_guest == "Luke":
        $guests.disable_guest('Kota')
    else:
        $guests.disable_guest('Luke')

label RD1:
    call screen dayManager("teams")

    if 'Asterion' not in rd_team_names() or (first_guest == "Kota" and 'Kota' not in rd_team_names()) or (first_guest == "Luke" and 'Luke' not in rd_team_names()):

        asterion "Mestre... Seria um desperdício de recursos não atribuir [first_guest] e eu nesta tarefa."
        jump RD1

    asterion "Muito bem, meu senhor. Devo realizar sua vontade rapidamente.
    Convocarei [first_guest] por sua ajuda."

    if renpy.variant("android"):
        "Os atributos de seus hóspedes podem ser vistos na {color=[UIColorOrange]}Tela de Hóspedes{/color} no menu.
        Você também pode inspecionar os membros atuais da equipe na {color=[UIColorOrange]}Tela de Equipe{/color}."
    else:
        "Os atributos de seus hóspedes podem ser vistos na {color=[UIColorOrange]}Tela de Hóspedes{/color} no menu.
        Você também pode inspecionar os membros atuais da equipe na {color=[UIColorOrange]}Tela de Equipe{/color}.
        Você também pode inspecioná-los no Livro de Registros no canto superior da tela."

    "Com isso, você sai. Assim que está saindo, você ouve novamente —
    o som da rocha roçando contra si mesma atrás de você, além de seu alcance."

    scene bg black
    with Dissolve(2.0)

    pause 3.0

    scene bg oldlobby
    with Dissolve (1.0)

    "Já está na hora de novos hóspedes chegarem. De volta à recepção,
    você veste seu melhor sorriso e espera."

    "As coisas estão mais lentas hoje. Durante a manhã, apenas três novos hóspedes chegam, todos sozinhos."

    "À medida que o dia avança, entretanto, você percebe certa comoção enquanto as pessoas perambulam por aí."

    $LoungeBlobs[0] = False
    $LoungeBlobs[1] = 1
    scene Lounge
    with Dissolve (1.0)

    "Na hora do almoço, você encontra apenas alguns sanduíches dispostos no
    balcão do salão. Alguns hóspedes estão desaparecidos — Greta,
    seu namorado e os homens sul-americanos."

    if first_guest == 'Kota':

        $Luke.change('emotion', 'annoyed')
        $Luke.change('arm', 'hip')
        show Luke:
            xalign -1.0 xzoom -1 yalign 1.0
            ease 2.0 xalign 0.5
        "Enquanto almoça, você vê o que logo poderá se tornar uma visão comum no hotel:
        Luke entrando no restaurante, olhando em volta por um momento e (se não há nenhum sinal de Kota)
        indo direto ao balcão para pegar comida."

        show Luke:
            xzoom 1
            ease 2.0 xalign 0.2
        "Antes de sair do cômodo e voltar para a recepção,
        Luke já desembrulhou um dos sanduíches e o partiu ao meio com suas garras."

        show Luke:
            ease 0.5 yalign 1.2
            pause 0.5
            ease 0.6 yalign 1.0
        "Ele abre bem o bico — tão largamente que parece {i}errado{/i} —
        e engole a porção inteira."

        show Luke:
            ease 2.0 xalign -1.0
        pause 2.0
        "Por mais que você deseje que ele e Kota se deem bem,
        você está um tanto feliz por ser poupado do espetáculo."

    else:
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "relaxed")
        $Kota.change("emotion", "sad")
        show Kota:
            xalign -1.0 xzoom 1 yalign 1.0
            ease 2.0 xalign 0.5
        "Enquanto almoça, você vê o que logo poderá se tornar uma visão comum no hotel:
        Kota entrando no bar com uma expressão descontente, olhando em volta por um momento e
        (caso Luke não esteja em nenhum lugar à vista) pegando um pouco de comida do balcão."

        show Kota:
            xzoom -1
        "Kota possui uma atitude muito desconfortável em relação a toda esta dolorosa situação.
        Ele tenta manter a compostura, curvando-se para alguns hóspedes se eles estiverem no caminho,
        mas seu olhar desdenhoso mostra que ele não quer estar lá."

        show Kota:
            ease 2.0 xalign -1.0
        pause 2.0
        "Ele pega alguns sanduíches e caminha de volta para a recepção."

    "Você pode ver que isso está se tornando uma rotina um tanto triste."
    hide Kota
    hide Luke

    scene bg oldlobby
    with Dissolve (1.0)

    pause 1.0
    "Você se preparou para uma tarde sem intercorrências,
    mas quando retorna à recepção, algo parece estranho."

    stop music fadeout 1.0

    "Você ouve um ruído sutil vindo de trás do balcão."

    pause 2.0

    "Você caminha em direção a ele e espia a parte de trás, apenas para encontrar..."

    show Ismael_surprise:
        xalign 0.5 yalign 4.0 xzoom 1
        ease 2.0 yalign 2.0

    pause 2.0

    you "Com licença, mas quem é você e o que pensa que está fazendo?"

    show Ismael_surprise:
        ease 1.0 yalign 1.0
        ease 0.5 yalign 1.1

    play music "music/GreekFolkSong.ogg" fadeout 2.0 fadein 2.0

    "Ismael" "Ah.{w} D{w=0.2}-desculpa.{w} Eu só tava,{w=0.2} hã,{w=0.2}
    procurando um lugar tranquilo. Meu nome é Ismael."

    you "E você escolheu ficar atrás do balcão da recepção?"

    hide Ismael_surprise
    show Ismael:
        xalign 0.5 yalign 1.1 xzoom 1

    "Ismael" "S{w=0.2}-sim.{w=0.2} Hã,{w=0.2} não faz sentido, né?{w}
    É mais porque eu queria ficar sozinho por um tempo."

    you "E,{w=0.2} mais uma vez,{w=0.2} você escolheu ficar sozinho atrás do balcão da recepção?{w}
    De todos os lugares nesse hotel, esse é o que você escolheu?"

    "Ismael" "S-sim. Haha, n{w=0.2}-não é bobo?"

    pause 1.0

    "Ismael" "Por favor, entenda. Eu venho pegando carona com a minha namorada já tem semanas
    e ela não{w=0.2} para{w=0.2} de falar."

    "Ismael" "E hoje ela,{w=0.2} tipo,{w=0.2} ficou toda animada com essa coisa que ela tava ajudando."

    if first_guest == "Luke":
        "Ismael" "Aquele pássaro excitado convenceu ela a ajudar ele com alguma coisa.
        Quando me deparei com ela no almoço, ela tava toda empolgada."
    else:
        "Ismael" "Aquele dragão gordo convenceu ela a ajudar ele com alguma coisa.
        Quando me deparei com ela no almoço, ela tava toda empolgada."

    hide Ismael
    show Ismael_surprise:
        xzoom -1 xalign 0.5 yalign 1.1
        pause 0.5
        xzoom 1
        pause 0.5
        xzoom -1

    pause 1.0

    "Ismael" "V{w=0.2}-você não entende como ela é.{w=0.2}
    Ela continua falando e falando, mesmo quando eu tô tentando dormir."

    hide Ismael_surprise
    show Ismael:
        xzoom 1 xalign 0.5 yalign 1.1
        ease 1.0 yalign 1.6

    "Ismael" "Por favor, deixa eu me esconder, ela nunca vai procurar aqui. {w=0.2}Tô só assistindo uns animes,
    não vou te atrapalhar."

    you "Anime? Como você está fazendo isso? Não temos conexão com a internet aqui,
    e eu duvido que você esteja recebendo qualquer sinal."

    "Ismael" "É, sim. E isso tá me deixando louco, não consigo navegar merda nenhuma."

    "Ismael" "Mas eu planejei com antecedência. Tenho mais de cento e oito gigas de anime no
    meu celular. O suficiente pra durar toda a viagem."

    you "Jesus. Você gosta mesmo da Greta?"

    hide Ismael
    show Ismael_surprise:
        xzoom 1 xalign 0.5 yalign 1.6

    "Ismael" "Eu não sei, ela fala tanto que eu nem consigo pensar.
    Achei que ia ter um pouco de paz e sossego nessa viagem, mas me enganei. Foi um erro."

    hide Ismael_surprise
    show Ismael:
        xzoom 1 xalign 0.5 yalign 1.6

    "Ismael" "Pensei que ter uma namorada seria divertido,{w=0.2} e meus amigos da
    politécnica iriam parar de tirar sarro de mim.{w} Mas ter um relacionamento é difícil."

    "Ismael" "E{w=0.2}-e ela fica me perguntando o que eu acho, e eu não sei."

    "Ismael" "Teve uma vez que ela perguntou se eu queria ter filhos depois que ela terminasse
    o doutorado, e{w=0.2}-e eu só quero ir pra casa depois do meu expediente e relaxar, cara."

    you "Hum.{w=0.2} Você já tentou conversar com ela sobre isso?"

    hide Ismael
    show Ismael_surprise:
        xzoom 1 xalign 0.5 yalign 1.6

    pause 1.0

    hide Ismael_surprise
    show Ismael:
        xzoom 1 xalign 0.5 yalign 1.6

    "Ismael" "Mas eu não quero conversar...{w=0.2} Ela não pode só ficar quieta? Eu trabalho tão duro,
    e a politécnica foi tão difícil, ela devia entender que eu preciso do meu tempo de solidão."

    menu:
        "O que você diz a ele?"
        "Se vira.":
            you "Se vira, cara. Ser capaz de falar sobre as coisas é uma habilidade
            adulta importante."
            you "Se isso te incomoda tanto, então você tem que fazer algo a respeito.
            Converse com ela, ou pelo menos reflita um pouco sobre o seu papel em tudo isso."
            hide Ismael
            show Ismael_surprise:
                xzoom 1 xalign 0.5 yalign 1.6
            "Ismael" "Eu s{w=0.2}-só não quero pensar sobre essas coisas agora.
            Afinal, eu tô de férias. Eu poderia aproveitar um pouco de distração. Vai fazer as coisas ficarem mais claras pra mim."
            hide Ismael_surprise
            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.6

        "Chato ser você.":
            you "Ah, bem.{w=0.2} Isso é bem chato. O que você vai fazer?"
            "Ismael" "Eu vou, é, como se diz mesmo?{w=0.2}
            Sim, vou me preocupar com isso quando chegar a hora. Vai ficar tudo bem."

        "Pobrezinho.":
            you "Pobre criaturinha, não consigo imaginar o que você deve estar passando.
            Deve estar tão cansado."
            hide Ismael
            show Ismael_surprise:
                xzoom 1 xalign 0.5 yalign 1.6
            pause 1.0
            hide Ismael_surprise
            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.6

    you "Bem, vou deixar você assistir seus animes, então."
    pause 2.0
    "Ismael" "E-{w=0.2}ei, você tem um momentinho só pra bater um papo?"
    you "Hum? Pensei que você queria paz e sossego."

    "Ismael" "Bem, a Greta ficando quieta por um minuto ou dois é pelo o que eu tenho rezado.
    Se for outro ser humano, tudo bem.{w=0.2}
    Não conversei com mais ninguém por mais de uma semana."

    you "Acho que sim.{w=0.2} Sobre o que você quer conversar?"

    "Ismael" "Eu não sei, só coisas, eu acho. Tem algum anime favorito?"

    you "Sobre isso..."

    $opinion_anime = "none"

    menu:
        "Qual é o seu anime favorito?"
        "Eu amo muitos animes para conseguir escolher um favorito.":
            you "Cara, eu não saberia nem por onde começar.
            É como escolher quem é seu filho favorito, sabe?"
            hide Ismael
            show Ismael_surprise:
                xzoom 1 xalign 0.5 yalign 1.6
                ease 1.0 yalign 1.1
            "Ismael sorri, tento encontrado uma alma gêmea até mesmo neste lugar."

            "Ismael" "Ah, não, cara, eu tenho um favorito bem claro.{w=0.2}
            Me diz que você assistiu Suitosho no On'nanoko. Eu sei que é uma escolha meio
            padrão, mas eu adoro, fico pensando nele toda noite antes de dormir."

            you "...Sério?"

            hide Ismael_surprise
            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.1

            "Ismael" "Agora eu sei que todo mundo prefere a parte três porque as \"garotas são mais fofas\",
            mas cara, elas trocam de roupa {i}todo{/i} episódio na série original.{nw}"

            "Ismael" "Eu não sei se você é familiarizado com ele, mas tem um episódio em que
            a menina loira entra numa roupa de inverno violeta fofa e cara,
            isso despertou algo em mim, ha ha.{nw}"

            "Ismael continua falando continuamente e tentando justificar suas opiniões terríveis.
            Você se pergunta como alguém que diz assistir tantos animes pode ter um gosto tão terrível
            — e pior ainda, ser tão arrogante sobre isso."

            "Mas você sabe que é apenas como os fãs de moe são.
            Você o tolera um pouco mais, mas depois de um tempo decide que é hora de retomar suas funções."

            you "Ei.{w=0.2} Escuta. Eu tenho trabalho a fazer.{w=0.2}
            Que tal você colocar os fones de ouvido e assistir seu anime?"

            hide Ismael
            show Ismael_surprise:
                xzoom 1 xalign 0.5 yalign 1.1

            "Ismael" "Ah sim!{w=0.2} Eu tava ouvindo ele esse tempo todo,
            consigo ser multitarefa, mas beleza.{w=0.2} Sim, vou fazer isso.
            Obrigado por me ouvir."

            hide Ismael_surprise
            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.1
                ease 3.0 yalign 4.0

            $opinion_anime = "great"

        "Hã. Aquele shonen com o arco do torneio.":

            you "Eu estava assistindo aquele shonen com um arco de torneio na casa de um amigo
            que foi muito foda...{w} merda, não consigo lembrar o nome."

            hide Ismael
            show Ismael_surprise:
                xzoom 1 xalign 0.5 yalign 1.6

            "Ismael" "Qual deles?{w=0.4} Tinha armas medievais que se transformam
            em armas de fogo?{w=0.2} Todos os meus amigos da internet não param de
            falar dele agora que tá sendo adaptado."

            "Ismael" "Ainda não consegui assistir o anime,
            eu tô lendo o mangá perto da parte que Raion treina pra-"

            you "Não, esse não. É sobre artes marciais e essas coisas."

            "Ismael" "É aquele com a personagem irmã fofa de cabelo rosa que todo mundo anda fazendo
            fanart?{w} Tá em um monte de serviços de streaming agora, talvez seja esse."

            you "Esse parece novo, você pode dizer que o qual eu estou falando parece meio antigo,
            como se fosse da velha guarda ou algo assim."

            "Ismael" "Certo, então é um shonen de artes marciais com um arco de torneio
            que é um pouco antigo.{w} Vamos ver..."

            hide Ismael_surprise
            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.6

            "Você passa quinze minutos com Ismael enquanto ele lista uma miríade de animes
            que podem corresponder à sua descrição com você descartando um por um."

            "Em um ponto, você percebe que ele pode ter acertado há um tempo,
            mas agora seria embaraçoso demais interrompê-lo."

            "Mas já faz um tempo, de qualquer forma, você o fez companhia por tempo suficiente.
            Você decide seguir em frente com o seu dia."

            hide Ismael
            with Dissolve(2.0)

            $opinion_anime = "great"

        "Eu não me importo muito com animes.":
            you "Sinto muito, anime não é minha praia."

            "Ismael" "Ah. Tem certeza? Mais uma vez, eu tenho tipo uma tonelada aqui. Tenho certeza que
            deve ter algum que você vai gostar. Quer dizer, se você gosta de programas de ação,
            é muito melhor que as coisas ocidentais.{nw}"

            "Ismael" "E tem animes inteiramente dedicados a garotas fofinhas. Tipo, sério,
            você acha que Greta se compara até mesmo com a pior garota de uma série tipica
            de cotidiano que você gosta?{nw}"

            "Ismael" "Você acha que gatinhas da vida real podem sequer competir com isso?{nw}"

            "Ismael" "Ou se você gosta de comédia, eu tenho os primeiros trinta ou mais
            episódios desse anime...{nw}"

            "Ismael" "...é sobre uma colegial que tem uma irmã mais velha, ela trabalha
            em uma cafeteria vestida que nem uma empregada doméstica francesa...{nw}"

            "Ismael" "...e deixa eu te contar, os japoneses têm um conhecimento muito profundo da
            nossa cultura, é diferente de tudo o que eu já vi na mídia estrangeira.{nw}"

            pause 1.0
            you "Não.{w=0.2} Obrigado, eu passo."

            hide Ismael
            show Ismael_surprise:
                xzoom 1 xalign 0.5 yalign 1.6
            "Ismael parece desapontado."

            hide Ismael_surprise
            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.6
            "Ismael" "Não, eu entendo, não é pra todo mundo. Não se preocupe."
            "Ismael coloca de volta os fones de ouvido e volta para atrás do balcão."

            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.6
                ease 3.0 yalign 4.0
            "Ismael" "Só não diz à Greta que eu tô aqui, tá?"

            "Você dá de ombros e segue em frente."
            $opinion_anime = "neutral"

        "Anime é uma abominação doentia no nosso planeta.":
            you "Por tudo que é sagrado, anime é uma abominação nesse planeta.{w}
            Se esse hotel não fosse dedicado a abrigar os pobres,{w=0.4} os amaldiçoados,{w=0.4}
            e a escória da sociedade,{w=0.4} eu expulsaria você nesse instante!"

            you "Não é eufemismo que pelo menos dez por cento de todas as doenças
            que assolam nossas sociedades desapareceriam se exterminássemos o intermédio conhecido como anime."
            you "Acabar com o anime em sua totalidade é um imperativo moral, o mínimo que uma pessoa deve
            fazer para se classificar como um ser humano bem intencionado que deixará um mundo melhor para as
            gerações futuras."

            hide Ismael
            show Ismael_surprise:
                xzoom 1 xalign 0.5 yalign 1.6

            "Ismael" "Hã.{w=0.2} Jesus."

            hide Ismael_surprise
            show Ismael:
                xzoom 1 xalign 0.5 yalign 1.6
                ease 1.0 yalign 2.0

            "Ismael" "Nah, eu entendo você. Muitas pessoas que eu conheço me disseram que anime é ruim pra mim."

            "Ismael" "Uma vez eu assisti uma série shonen com o meu pai,
            ele não ficou impressionado e me disse pra ler um livro em vez disso."

            "Ismael" "Mas ele só não tava prestando atenção o suficiente. Ele teria gostado se tivesse
            continuado até o episódio 97."

            "Ismael" "É quando o salto de tempo acontece, depois dessa parte fica muito bom.{w=0.2}
            Mas, em vez disso, ele tá sempre tentando me levar pras festas da alta sociedade dele."

            "Ismael" "Eu não quero, ok? Isso deveria ser o suficiente pra ele, mas nunca é."

            you "Talvez você devesse ouvir seu pai. Pare de assistir essa merda hoje mesmo e você
            vai me agradecer em alguns meses.{w} Agora saia da minha recepção."

            show Ismael:
                xzoom -1 xalign 0.5 yalign 2.0
                ease 3.0 yalign 1.0 xalign -1.0

            "Você vê Ismael correr de volta em direção à grande escadaria com lágrimas nos olhos."

            "Você dá um suspiro de alívio, contente com um trabalho bem feito."

            "Um dia ele verá."

            $opinion_anime = "abomination"

    pause 3.0
    hide Ismael
    hide Ismael_surprise

    "Depois deste breve episódio, a tarde segue sem intercorrências. Mais alguns hóspedes fazem check-in."

    "Às 19h, você segue seu caminho até o salão para jantar."

    $LoungeBlobs[1] = 2
    $LoungeBlobs[0] = False

    scene Lounge
    with Dissolve(1.0)

    if first_guest == "Luke":
        play music "music/AberdeenDoneIt.ogg" fadeout 1.0 fadein 1.0
        show LoungeLight
        with Dissolve (0.5)
    else:
        play music "music/TheSorrow.ogg" fadeout 4.0 fadein 4.0

    "Os hóspedes já chegaram e se acomodaram para esperar por suas refeições."

    #It is impossible for the player to get any rewards on the first day so we just accumulate the stats
    $inventory.accumulate_stats(calculate_rd_team_stats(), 'RD')

#    "End of first day, reaping rewards here."
#    $nextLabel = "day1_EOD"
#    jump teamRewards
#label day1_EOD:

    $Asterion.change('emotion', 'neutral')
    $Asterion.change('rightarm', 'loose')
    $Asterion.change('leftarm', 'loose')
    show Asterion behind LoungeLight:
        xalign 0.5 yalign 1.0 zoom 0.8
    show Greta behind LoungeLight:
        xalign 0.8 yalign 1.1 zoom 0.8 xzoom -1
    with Dissolve(1.0)

    "Astério e a senhorita alemã estão conversando enquanto sentam juntos em uma mesa perto dos fundos."

    show Asterion:
        ease 2.0 xalign 0.8
    show Greta:
        ease 2.0 xalign 1.1

    if first_guest == "Kota":
        $Kota.change("rightarm", "relaxed")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("emotion", "sad")
        show Kota:
            xalign -1.0 yalign 1.0 xzoom 1
            ease 2.0 xalign 0.5

        "Antes que você possa seguir o caminho para falar com eles, [first_guest] se aproxima de você. O dragão
        mexe com os dedos, reajusta o cabelo, e então resmunga
        baixinho antes de falar."

        $Kota.change("emotion", "neutral")

        kota "Ah, boa noite, Mestre [player_name]. É um prazer vê-lo novamente."

        $Kota.change("emotion", "sad")

        kota "Tem sido...{w=0.5} um dia bastante difícil,{w=0.2} para dizer o mínimo."

        $Asterion.change("emotion", "contemplative")
        $Asterion.change ("leftarm", "raised")

        $Kota.change("rightarm", "raised")

        kota "Por favor, não me entenda mal. Fico mais que feliz em ajudar com o hotel
        tanto quanto puder, mas...{w=0.2} devo admitir, tecnologia não é meu forte."

        show Greta:
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1

        kota "Na verdade, houve momentos ao longo dos anos em que hesitei
        me atualizar com os tempos."

        kota "Piorou depois da Segunda Guerra Mundial, desde então tem sido uma
        enxurrada sem fim de avanços.{w=0.2} Não sou mais tão jovem,
        não consigo acompanhar este ritmo."

        $Kota.change("rightarm", "relaxed")

        kota "Mas fiz as pazes com o fato de que deveria pelo menos tentar
        me manter atualizado com as tendências atuais."

        $Asterion.change ("leftarm", "loose")

        $Kota.change("emotion", "puzzled")

        kota "Então,{w=0.2} considerando que tenho dificuldade em operar um smartphone,{w=0.2}
        receio que fui incapaz de ajudar muito na tarefa em questão."

        kota "Sendo assim,{w=0.2} Astério e eu fomos incapazes de fazer qualquer progresso."

        show Greta:
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1

        $Kota.change("emotion", "happy")
        $Kota.change("rightarm", "raised")
        $Kota.change("leftarm", "raised")

        kota "No entanto — e por favor, perdoe-me por puxar meu próprio saco por um segundo —
        tive uma ideia que acabou ajudando mais do que eu jamais poderia."

        $Asterion.change("emotion", "neutral")

        $Kota.change("emotion", "angry")
        $Kota.change("rightarm", "relaxed")

        kota "Veja bem,{w=0.2} eu tive uma...{w} digamos {w=0.3}\"interessante\"{w=0.3}
        conversa com a Srta. Greta ontem enquanto ajudava seu companheiro
        a agir como um adulto."

        show Greta:
            xzoom 1
            ease 1.0 xalign 1.15

        $Kota.change("emotion", "happy")

        kota "Acontece que ela é engenheira. E quando eu a convidei para inspecionar
        a bacia, ela estava mais que ansiosa para ajudar."

        $Asterion.change ("rightarm", "hips")
        $Kota.change("leftarm", "relaxed")

        kota "Astério e eu ficamos muito impressionados com as contribuições dela.{w=0.5}
        Eu realmente acredito que estamos um pouco mais perto de resolver esse problema."

        show Greta:
            xzoom -1
            ease 1.0 xalign 1.1

        $Kota.change("emotion", "laughing")
        $Kota.change("rightarm", "raised")
        $Kota.change("leftarm", "raised")

        kota "Ela teve o trabalho de explicar tudo. Em um ritmo muito rápido,{w=0.3}
        devo acrescentar,{w=0.3} coisa que me deu nos nervos depois de um tempo.{w}
        Mas realmente sinto que consegui entender um pouco."

        play sound "sfx/asterionchord.mp3"
        $guests.increase_guest_stat(first_guest, "Tech", 1)
        "O atributo de {color=[UIColorTech]}Tecnologia{/color} de Kota aumentou em 1!"

        $Asterion.change("emotion", "tired")
        show Greta:
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1

        $Kota.change("emotion", "sad")

        kota "E por falar em me dar nos nervos...{w} eu não sei o que era,
        mas havia algo...{w=0.5} estranho{w=0.5} sobre aquela sala em que tivemos que nos amontoar."

        $Kota.change("rightarm", "relaxed")

        kota "Tudo sobre ela parecia {i}errado.{/i}"

        kota "Suponho que o senhor Astério esteja acostumado,{w=0.3} e a Srta. Greta parecia
        muito envolvida com o projeto para se importar,{w=0.3} mas algo sobre aquela sala me deixou nervoso.
        Foi tão longe a ponto de me dar azia."

        kota "E entre isto e o entusiasmo da Srta. Greta,{w=0.3}
        lamento dizer que tive uma tarde muito estressante."

        show Greta:
            ease 0.5 xalign 1.05
            ease 1.0 xalign 1.1

        $Kota.change("emotion", "neutral")
        $Kota.change("rightarm", "mug")

        kota "Então,{w=0.2} tenho certeza de que você entende quando digo que anseio
        por um pouco de paz e tranquilidade agora."

        kota "Irei para a cozinha. Há algo muito reconfortante
        sobre preparar ramen. Espero que chegue na hora certa, você não vai querer perder!"

        $Asterion.change("emotion", "neutral")

        kota "Astério e Greta estão bem ali caso precise deles."

        show Kota:
            ease 3.0 xalign 2.0

    else:
        $Luke.change("clothes", "tankpants")
        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "salute")

        show Luke behind LoungeLight:
            xalign -1.0 yalign 1.0 xzoom -1
            ease 2.0 xalign 0.5

        luke "Ei, chefinho!"

        $Luke.change("arm", "pointing")

        luke "Mas o que diabos passava na sua cabeça quando você me colocou em um serviço de nerd?{w=0.2}
        Eu não sei merda nenhuma sobre como a internet funciona."

        $Asterion.change("emotion", "contemplative")
        $Asterion.change ("leftarm", "raised")

        luke "Também não sei como ler aquele monte de coisa sem sentido que o Angus escreveu.
        Ele me pediu pra revisar os documentos e, olha, como você espera que eu saiba o que é um protocolo
        {i}tê cê pê{/i}?"

        $Luke.change("arm", "hip")

        luke "Inferno, se tivesse sinal no meu celular eu poderia só pesquisar online, mas aí
        que tá, né?"

        show Greta:
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1

        $Luke.change("emotion", "annoyed")

        luke "Olha, as coisas não tavam indo bem. A gente passou uma hora inteira naquela sala apertada,
        eu girando os polegares enquanto Astério tentava explicar como tudo isso funciona pra mim."

        $Luke.change("emotion", "neutral")

        luke "Mas então eu {w=0.2} — Quer dizer, {i}nós{/i} tivemos uma ideia. A alemã gordinha,
        ela é uma engenheira, né? Então, a gente bateu na porta dela, amarramos ela."

        $Asterion.change ("leftarm", "loose")

        luke "A gente acabou trazendo os dois uruguaios, também. Acontece que eles trabalham com algum
        provedor de internet. Instalando canos ou alguma merda aí."

        show Greta:
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1

        luke "Aí eles juntaram todos os nossos cérebros, depois colocaram tudo em um quadro negro,
        e Astério passou pro papel."

        $Asterion.change("emotion", "neutral")

        $Luke.change("emotion", "laughing")
        $Luke.change("arm", "pointing")

        luke "Eu fiz sanduíches! Os nerds tavam falando sobre pacotes, então eu embrulhei
        em umas caixinhas. Fez eles se sentirem especiais e tudo mais."

        $Luke.change("arm", "hip")

        luke "Enfim, a gente tá ficando perto de descobrir toda essa merda da internet!
        Eu não sei os detalhes, mas eles conseguiram enviar e receber alguns sinais.
        É só que o {i}wi-fi{/i} ainda não tá funcionando."

        show Greta:
            xzoom 1
            ease 1.0 xalign 1.15

        $Luke.change("emotion", "surprise")
        $Luke.change("arm", "pointing")

        luke "Mas deixa eu te contar uma coisa, aquele lugar que a gente tava trabalhando?{w}
        Mó bagulho sinistro, chefe."

        $Luke.change("arm", "hip")

        luke "Angus {i}não{/i} quer ninguém mexendo nas pedras escuras nas paredes."

        show Greta:
            xzoom -1
            ease 1.0 xalign 1.1

        $Luke.change("emotion", "annoyed")

        luke "E aquele negócio de bacia, é absolutamente perturbador.{w}
        Todo mundo tava esperando instalar uns cabos e roteadores,{w=0.2} mas nah,{w=0.2}
        acabou que a bacia é a coisa toda."

        luke "É isso que eles tavam fazendo o dia todo, ensinando a bacia a se conectar com a internet."

        pause 1.0

        $Luke.change("emotion", "surprise")

        luke "...Olha,{w=0.2} eu tava brincando quando disse que vendi minha alma pro diabo, sabe?{w=0.2}
        Eu sei que magia estranha existe.{w} Mas aquela sala me assusta pra caralho."

        luke "Todo mundo sentiu isso.{w=0.2} A não ser Astério e aquela moça, Greta.{w=0.2}
        Ela tava muito animada com a coisa toda."

        $Asterion.change("emotion", "tired")
        show Greta:
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1
            ease 0.1 yalign 1.05
            ease 0.1 yalign 1.1

        $Luke.change("emotion", "annoyed")

        luke "Ela continuava me importunando de um jeito que você não ia acreditar.{w} Rapaz,{w=0.2}
        aquela mulher tem a língua solta, viu."

        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "pointing")

        luke "Ela tava tentando explicar as coisas pra mim e eu insisti que
        sou burro demais pra entender...{w} Mas ei,{w=0.5}
        passa manteiga na minha bunda e me chama de bolacha!{w=0.5} Eu acho que aprendi mesmo alguma coisa!"

        play sound "sfx/asterionchord.mp3"
        $guests.increase_guest_stat(first_guest, "Tech", 1)
        "O atributo de {color=[UIColorTech]}Tecnologia{/color} de Luke subiu em 1!"

        luke "Falando em importunar,{w=0.3} tenho certeza que ela ainda tá enchendo a cabeça do menino Angus com isso."

        show Greta:
            ease 0.5 xalign 1.05
            ease 1.0 xalign 1.1

        $Luke.change("emotion", "wink")
        $Luke.change("arm", "salute")

        luke "Enfim, fica aí meu relatório.{w=0.2} Agora, se me dá licença,{w=0.2} eu tenho que cozinhar.{w}
        Ser um bom dono de casa pra todos vocês,{w=0.2} lindos homens robustos,{w=0.2} sabe?"

        $Asterion.change("emotion", "neutral")

        $Luke.change("emotion", "laughing")
        $Luke.change("arm", "hip")

        luke "Hoje a gente vai ter...{w=0.5} hambúrgueres!{w} De novo!"

        luke "Vou deixar você sabendo,{w=0.2} contudo,{w=0.2} que essa noite eu tenho que sair mais cedo."

        $Luke.change("emotion", "wink")

        luke "Já trabalhei pra caramba hoje animando todo mundo,{w=0.2} e eu {i}talvez{/i}
        tenha um encontro especial pra ajudar um dos nossos belos uruguaios a instalar uns canos."

        show Luke:
            xzoom 1
            ease 3.0 xalign -1.0


    pause 1.0

    #Asterion and Greta are sitting a few meters away from others, talking
    #Greta is very excited
    show Asterion:
        ease 2.0 xalign 0.3 yalign 1.0 zoom 0.9
    show Greta:
        ease 2.0 xalign 0.8 yalign 1.1 zoom 0.9 xzoom -1

    pause 2.0

    "Você segue em direção a Astério e Greta."

    $LoungeBlobs[0] = True

    "Greta" "— absolutamente fantástico! O que você tem aqui poderia revolucionar, bem, {i}tudo!{/i}"

    show Greta:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.1
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.1

    "Greta" "Você pode simplesmente criar matéria do nada!{w=0.2} Isso quebra a termodinâmica como a conhecemos,
    poderíamos resolver a crise de energia e acabar com a escassez em si para sempre."

    "Greta" "Esse{w=0.2} — esse lugar poderia mudar o futuro do planeta!"

    $Asterion.change ("emotion", "tired")
    show Greta:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.1

    "Greta" "Onde estava você e esse hotel todo esse tempo?!
    Por que ninguém fez um bom uso desse lugar?"

    $Asterion.change ("emotion", "sad")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    asterion "S-srta. Greta, por favor, contenha-se. O Hotel permaneceu abandonado por décadas,
    não havia nada que eu pudesse fazer."

    asterion "Ainda assim, eu tenho — quero dizer, minha família tem pressionado em direção
    a isto há um bom tempo. Colocar este domínio em bom uso."

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("rightarm", "hips")

    asterion "Mas os proprietários anteriores não pensaram em investir o esforço.
    No máximo, eles aprovavam um punhado de remessas de livros a cada ano."

    "Greta" "Isso é simplesmente absurdo. Imagine como nós poderíamos resolver a escassez de recursos..."

    asterion "Bem, havia uma boa razão para não interferir frequentemente com o mundo exterior.
    Este tem sido o protocolo do hotel há séculos."

    asterion "Um pouco antes da 2ª Guerra Mundial, houve um incidente. Naquela época, o Mestre
    era um certo Jean Marie, ele tinha um irmão chamado Clément."

    asterion "Clément passou anos fazendo lobby para que o hotel fornecesse matéria-prima para a Alemanha,
    para o desgosto do Mestre Jean-Marie."

    asterion "Materiais como tecidos, minério de ferro, cal virgem..."

    show Greta:
        ease 2.0 xalign 0.9

    "Greta" "Ah.{w=0.5} Ah, isso não é bom."

    asterion "Sim. Pode imaginar que tipo de geringonça a Alemanha poderia ter fabricado com
    estes materiais? Bem, fico feliz por termos desempenhado nosso pequeno, porém importante papel
    em evitar isto completamente."

    "Greta" "S-sim. Ah, Deus..."

    asterion "Então você entende, muitas vezes os Mestres temeram como as capacidades do Hotel
    poderiam ser mal utilizadas.{w} Com razão."

    asterion "E não é tão simples como se poderia imaginar. O domínio não pode
    exportar muito.{w=0.2} Ele cessará a geração de novos materiais caso muita massa saia dele."

    show Greta:
        ease 2.0 xalign 0.8

    "Greta" "Entendo. Então há uma boa razão para não exportar.
    Mas ainda pode ser usado para pesquisa, que problema teria com isso?"

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    asterion "Suponho que esteja certa. O Hotel abrigou muitos artistas e
    cientistas ao longo dos séculos, mas, como eu disse...{w=0.2} os mestres
    não pensaram muito nisso."

    asterion "Era apenas algo ocasional. Ou, muito frequentemente, uma questão de nepotismo,
    para beneficiar os queridos do Mestre."

    show Asterion:
        ease 1.0 zoom 1.0
    show Greta:
        ease 1.0 zoom 1.0

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    pause 1.0
    show Greta:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.1 zoom 1.0

    "Greta" "Ah, [player_name]! Desculpe, eu não vi você.
    Venha, nos faça companhia. Temos muito o que conversar!"

    "Greta" "[first_guest] lhe contou sobre as descobertas do dia?{w} Pedimos para ele fazer isso."

    you "Sim, ele me deu um resumo do que vocês conseguiram fazer.{w=0.3} Você ajudou bastante,
    não foi?{w} E eu aqui pensei que esses dias seriam férias para você..."

    "Greta" "Eu ajudei, mas não preocupe sua linda cabecinha.
    Cada segundo valeu a pena. Trabalhar nisso foi incrível."

    "Greta" "[player_name], permita-me falar francamente."

    "Greta" "Você tem muito mais que uma mina de ouro aqui. Se quiser ficar rico, sim,
    você pode conseguir com esse Hotel."

    you "Eu estou ciente disso. {w=0.2}Esse lugar tem muito potencial, com certeza."

    menu:
        "Vou fazer dele um lar para aqueles que estão perdidos.":

            you "Uma casa é uma coisa tão simples no papel.{w} Comida, cama, roupas, um teto, amigos."

            you "Mas não importa o quanto a humanidade tenha avançado, ainda somos limitados
            por recursos e circunstâncias."

            you "Ainda hoje crianças ficam sem educação, desnutridas e doentes."

            you "Mesmo nos países mais desenvolvidos, as pessoas morrem de doenças raras que
            requerem medicamentos proibitivamente caros. O mundo está cheio de iniquidades assim."

            $Asterion.change ("emotion", "contemplative")

            you "Com esse hotel, podemos ser capazes de realizar um imenso projeto humanitário."

            show Greta:
                ease 0.1 yalign 1.05
                ease 0.1 yalign 1.1

            "Greta" "Você está pensando muito pequeno! Escute, o mundo sempre terá esses problemas.
            Todos os dias uma nova criança pobre e faminta nasce, e isso nunca vai parar."

            "Greta" "Quando mais você ajuda, mais eles pedem ajuda! Enquanto isso, se você usar esse
            lugar para pesquisas, fará a própria humanidade avançar!"

        "Vou revolucionar a ciência com ele.":
            you "Parece que este domínio quebra uma série das leis mais fundamentais da física.
            É um tesouro pra qualquer cientista que se preze."

            you "Não só isso, a capacidade absoluta de gerar quaisquer materiais e equipamentos que quisermos
            torna esse o melhor lugar para qualquer laboratório de pesquisa, ponto final."

            you "Todos os obstáculos que se encontram em um ambiente universitário — bolsas escassas, falta de equipamento,
            política — tudo pode ser ignorado aqui."

            you "Se alguém acredita que a busca pelo conhecimento é um imperativo moral e ético,
            então esse hotel pode ser o caminho a seguir para algumas das virtudes mais brilhantes da humanidade."

            show Greta:
                ease 0.1 yalign 1.05
                ease 0.1 yalign 1.1
                ease 0.1 yalign 1.05
                ease 0.1 yalign 1.1

            "Greta" "Sim. [player_name], seu gênio magnífico, você compreende!"

            "Greta" "Não há um único campo da ciência que não se beneficiaria, de uma forma ou outra,
            com a existência desse lugar."

        "Posso realmente fazer uma fortuna aqui.":
            $Asterion.change ("emotion", "neutral")

            you "Eu estava conversando com Astério sobre isso mais cedo. Esse domínio tem algumas regras peculiares.
            Por exemplo, ele não pode gerar muito ouro, prata ou moeda falsificada."

            you "Também não pode exportar muita massa."

            you "Mas parece ser um sistema muito ruim, existem tantas lacunas.
            Poderíamos fabricar e vender diamantes, por exemplo. Baixa massa, alto valor."

            you "Mas mesmo isso é pensar pequeno. Poderíamos fazer muito dinheiro ainda deixando
            intacto o propósito do hotel."

            you "Ao exportar tais produtos, podemos pagar muito dinheiro aos nossos funcionários para que possam
            reconstruir suas vidas."

            you "Não quero parecer um cara desonesto. O que quero dizer é que o dinheiro também é importante."

            you "Além de abrigar pessoas, podemos pagar salários que lhes permitirão decolar — comprar uma casa,
            começar um negócio, pagar suas dívidas."

            show Greta:
                ease 0.1 yalign 1.05
                ease 0.1 yalign 1.1
                ease 0.1 yalign 1.05
                ease 0.1 yalign 1.1

            "Greta" "Não, não! Não é isso o que eu quero dizer!"

            "Greta" "Você está pensando muito pequeno.{w} Diamantes!{w=0.2} Como se dinheiro importasse!"

            "Greta" "Ouça, até mesmo pensar em dinheiro nesse momento abre um precedente ruim.
            Enquanto falamos, sou consumida por mil e uma ideias de pesquisas..."

            asterion "Se me dá licença, Srta. Greta...{w=0.2} enquanto eu sempre enfatizarei a
            missão humanitária do Hotel, o Mestre [player_name] está correto."

            asterion "Posso não ter muita experiência fora deste Hotel, mas dinheiro é essencial
            para pagar nossos funcionários para que possam dar os próximos passos na vida."

            $Asterion.change ("emotion", "contemplative")

            asterion "Ao longo dos séculos, muitos trabalharam aqui como um trampolim para
            objetivos maiores na vida. E isto, eu acredito, é admirável."

    "Greta" "Bem, eu já estou repleta de ideias sobre como explorar esse lugar!"

    "Greta" "Contamos com cabos submarinos gigantescos para nos comunicarmos entre os continentes, quando
    poderíamos simplesmente retransmitir tudo através desse hotel, por exemplo."

    "Greta" "Há tantas substâncias para pesquisa cuja aquisição é proibitivamente cara,
    e aqui você pode simplesmente gerar o que quiser!"

    "Greta" "Por favor, [player_name]!{w=0.2} Você deve pensar sobre o progresso da humanidade."

    "Greta" "Astério já me convenceu de que exportar bens pode não ser a decisão
    mais sábia, sim...{w=0.2} Mas pesquisa!{w=0.2} Permita que a ciência domine esse poder."

    show Greta:
        ease 0.5 yalign 1.0

    "Greta" "Não ceda a banalidades sufocantes sobre poder, [player_name]!
    A humanidade esculpiu seu caminho para fora da natureza primitiva e brutal apenas com nossa inteligência."

    "Greta" "Astério me disse que existem tais coisas como deuses, disse sim.
    Os patetas permitiram que esse domínio existisse, ainda assim não fizeram uso dele!"

    "Greta" "Se dependesse dos deuses, ainda estaríamos atirando pedras em bois selvagens.
    Foi a humanidade que criou a arte e, com o auxílio da ciência, permitiu padrões de vida decentes."

    "Greta" "Por favor, você não deve deixar esse domínio inutilizado."

    "Greta" "Olhe{w=0.2} — olhe para mim,{w=0.2} Eu sei o que você está pensando.
    Você está dizendo a si mesmo que eu sou uma alemã, correto?"

    "Greta" "Meu país fez coisas tão terríveis, tenho isso em mente!{w=0.4}
    Os campos de concentração!{w=0.4} Atrocidades horríveis são uma visão comum na história."

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    "Greta" "O que a Alemanha fez, mas olhe o que aconteceu em Hiroshima e Nagasaki!{w}
    Pense na Unidade 731 do Japão!"

    "Greta" "A humanidade está bastante familiarizada com o horror, nós estamos.
    Mas não significa que deveríamos parar de tentar alcançar a bondade."

    $Asterion.change ("emotion", "neutral")

    "Greta" "O poder não necessariamente corrompe, [player_name]!
    E você tem poder, muito poder. Talvez mais do que qualquer humano na história jamais teve."

    "Greta" "Recusar-se a usá-lo para o bem não é muito longe de usá-lo para o mal absoluto."
    #Greta keeps going
    #still gonna expand here

    pause 2.0

    show Greta:
        ease 1.0 yalign 1.1

    "Greta" "Ah... posso ter exagerado um pouco aí. Eu sinto muito."

    "Greta" "Astério, tive o dia mais agradável e fascinante da minha vida com você hoje.
    Não posso superestimar o privilégio de aprender mais sobre o seu hotel."

    "Greta" "Estou eufórica para voltar amanhã, para terminar nossa tarefa.{w=0.2} Ah, que baita impulso você me deu!
    {w=0.2}Tão estimulante."

    you "Ah. Você acha que podemos resolver o negócio da internet amanhã mesmo?"

    $throwaway1 = str(preset_rewards['WiFi']['stats']['Contract'])
    $throwaway2 = str(preset_rewards['WiFi']['stats']['Tech'])
    $throwaway3 = str(inventory.accumulated_stats['RD'].get_value('Contract'))
    $throwaway4 = str(inventory.accumulated_stats['RD'].get_value('Tech'))
    "Greta" "Bem... você sabe como o hotel funciona por meio de contratos?
    Eu estimaria que ainda faltam {color=[UIColorHumanities]}[throwaway1] contratos{/color} que precisamos terminar
    e {color=[UIColorTech]}[throwaway2]{/color} esquemas de{color=[UIColorTech]} Tecnologia{/color} que precisamos finalizar para que a internet funcione.
    E estamos em {color=[UIColorHumanities]}[throwaway3]{/color} e {color=[UIColorTech]}[throwaway4]{/color} respectivamente agora."

    you "Bem, isso é perfeitamente realizável."

    show Greta:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.1

    "Greta" "É sim! Agora, se me dão licença, acredito que meu namorado pode ter passado o dia inteiro
    no nosso quarto, e eu não posso aceitar. {w}Vou trazer ele aqui para socializar com os outros."

    "Greta" "Tenham uma noite maravilhosa, vocês dois."

    show Greta:
        ease 3.0 xalign -1.0 yalign 1.0

    pause 3.0

    show Asterion:
        ease 1.0 xalign 0.5

    $Asterion.change ("emotion", "tired")
    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("leftarm", "loose")

    pause 1.0

    asterion "Mestre..."

    $Asterion.change ("emotion", "sad")

    asterion "O que a Srta. Greta quis dizer com \"campos de concentração\"?{w=0.2} E o que aconteceu com
    \"Hiroshima e Nagasaki\"?"

    you "Ah,{w=0.2} Astério..."

    you "Que tal conversarmos sobre tudo isso uma outra hora?{w=0.2} É um assunto complicado."

    $Asterion.change ("emotion", "smiling")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "loose")

    asterion "Claro!{w=0.2} O que quiser, Mestre."

    you "Espero que o jantar fique pronto logo."

    $Asterion.change ("rightarm", "hips")
    show Asterion:
        ease 1.0 yalign 1.7

    "Você e Astério sentam-se, ficam confortáveis e têm uma curta e agradável
    conversa com alguns dos hóspedes enquanto esperam pela refeição."

    $LoungeBlobs[0] = False

    if first_guest == "Luke":
        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")
        show Luke:
            xalign -1.0 xzoom -1 yalign 1.0
            ease 3.0 xalign 0.1

        "Logo depois, Luke sai da cozinha e serve hambúrgueres para todo mundo.
        Você teve uma conversa com ele e — pelo bem de sua saúde e de todos,
        pediu-lhe que fosse menos generoso com os condimentos."

        show Luke:
            ease 1.0 yalign 1.15
            ease 1.0 yalign 1.0
        $Luke.change("arm", "pointing")

        play sound "sfx/clink.ogg"
        "A contragosto, Luke concordou com seu pedido. A refeição em seu prato
        pode ainda não ser ótima para você, mas não há mais tanta gordura acumulada
        no fundo do prato."

        $Luke.change("emotion", "wink")
        show Luke:
            ease 3.0 xalign -1.0

        $Asterion.change ("emotion", "contemplative")
        "Sabendo da dificuldade do minotauro em usar talheres e de sua relutância em comer carne bovina,
        Luke tomou a liberdade de cozinhar frango frito para Astério,
        que aprecia o gesto."

        $Asterion.change ("emotion", "surprise")
        show Asterion:
            ease 0.2 yalign 1.15
            ease 0.3 yalign 1.7

        "Isto é, até que ele dá uma mordida e a mistura de cinco ervas e temperos do grifo
        (seria mais, mas o hotel teve dificuldade em invocar alguns deles)
        faz uma festa na boca dele."

        "Você faz uma nota mental para ter uma outra conversa com Luke enquanto Astério desce uma garrafa
        de refrigerante (a única bebida não alcoólica que Luke está servindo hoje) em questão de segundos."

        $Asterion.change ("emotion", "neutral")
        "Astério havia recusado educadamente a bebida antes,
        mas vai aceitar o que puder nestas circunstâncias."

        pause 1.0
        $Asterion.change ("emotion", "contemplative")
        pause 0.5
        asterion "Beber uma colmeia inteira:\n
        Mas como alguém poderia querer isto?\n
        Tão doce e enjoativo."
        pause 1.0
    else:
        $Kota.change("emotion", "sad")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        show Kota:
            xalign 2.0 xzoom -1 yalign 1.0
            ease 4.0 xalign -1.0

        $Asterion.change("emotion", "surprise")
        "Pouco tempo depois, Kota emerge da cozinha e começa a servir ramen para os hóspedes."

        $Asterion.change("emotion", "neutral")
        "Você teve uma conversa com o dragão durante a manhã e pediu-lhe que fosse um pouco mais
        tolerante com as maneiras dos hóspedes na cozinha. Kota parece ter entendido a mensagem,
        mas ainda faz caretas ao passar por alguns dos hóspedes."

        show Kota:
            xalign -1.0 xzoom 1
            ease 4.0 xalign 2.0

        "Greta retorna pouco tempo depois de sair, arrastando Ismael atrás dela. Os dois sentam-se perto do bar,
        tornando as caminhadas de ida e volta de Kota para a cozinha mais longas, conforme ele faz seu melhor para evitá-los."


        $Kota.change("emotion", "happy")
        show Kota:
            xalign 2.0 xzoom -1 yalign 1.0
            ease 2.0 xalign 1.2 yalign 1.6
            ease 1.0 yalign 1.0
        $Asterion.change("emotion", "smiling")

        "Depois que você informou Kota sobre o fiasco de Astério com os talheres, ele conectou os
        os pontos e concluiu que os pauzinhos não serviriam."
        "Em vez disso, ele preparou onigiri para o minotauro comer com as mãos;
        uma trégua muito apreciada da opressão dos talheres."

        show Kota:
            ease 2.0 xalign 2.0
        pause 2.0
    hide Kota
    hide Luke

    $LoungeBlobs[0] = True
    #both return here

    $Asterion.change("emotion", "tired")
    "No meio de sua refeição, Astério para e suspira."

    you "Algum problema?"

    $Asterion.change("emotion", "sad")
    asterion "Ah...{w=0.2} É que a Srta. Greta é bem difícil de lidar, não é?"

    asterion "Hoje eu escorreguei e mencionei que costumava tocar a lira. Desde que estas
    palavras saíram da minha boca, ela não parou de me pedir para me ouvir tocar."

    if ArgosContract == "Terrorized":
        asterion "Algumas pessoas ouviram e disseram para ela me deixar em paz, mas também mencionei que
        a lira sempre me fazia relaxar.{w} Ela continuava dizendo que tocá-la para os hóspedes me ajudaria a
        \"sair da caverna e dar as caras para o mundo.\""

        $Asterion.change("emotion", "tired")
        asterion "Eu não sabia como dizer não a ela...{w=0.2} Suponho que em algum momento
        ao longo do caminho ela simplesmente presumiu que eu
        concordei com isso e começou a dizer a todos que eu o faria."

    else:
        $Asterion.change("emotion", "contemplative")
        asterion "Então, ela reuniu mais algumas pessoas para me pedir para tocar algumas músicas
        antes de partirem.{w=0.2} Não consegui dizer não para eles."

    asterion "Então...{w=0.2} em dois ou mais dias, farei um pequeno concerto para os hóspedes."

    you "Tem certeza de que está ok com isso?{w=0.2} Você não parece muito entusiasmado."

    $Asterion.change("emotion", "neutral")
    asterion "Eu apenas terei que me familiarizar novamente com minha lira. Não deve ser tão difícil,
    eu a toquei por tanto tempo..."

    scene bg black
    with Dissolve(2.0)

    pause 3.0

    $Asterion.change("emotion", "contemplative")

    scene bg staircase
    show Asterion:
        xalign 0.5 zoom 1.0 yalign 1.1
    show Asterion:
        ease 0.2 yalign 1.0
        ease 0.2 yalign 1.1
        pause 1.0
        repeat
    with Dissolve(1.0)

    "Após a refeição, vocês dois sobem a grande escadaria e voltam para os aposentos do Mestre.
    Ao longo do caminho, vocês têm uma pequena discussão sobre os acontecimentos do dia."

    "Astério está bastante infeliz por ter que levar as pessoas para o alicerce do hotel,
    mas reconhece que é um mal necessário para dar a todos uma experiência melhor."

    "A presença de [first_guest] lá embaixo foi muito reconfortante,
    apesar de ele não ter ajudado muito na tarefa em questão."

    "Ele também fala sobre Greta. Vocês dois concordam que, apesar de estarem mais do que gratos por sua ajuda,
    ela é uma pessoa muito intensa. Astério menciona que ela estará partindo em alguns dias para continuar sua jornada, mas ainda há bastante tempo para concluir o projeto da internet."

    if opinion_anime == "great":
        "Por sua vez, você conta a ele sobre quando se deparou com Ismael à tarde,
        mas precisa fazer uma pausa para explicar o que é anime."

        $Asterion.change("emotion", "smiling")

        "Acaba se transformando em uma divagação bastante longa, mas Astério fica feliz em ouvir mais.
        Você se pergunta se deveria ou não mostrar a ele alguns de seus animes favoritos assim que conseguirem
        fazer o wi-fi funcionar."

    elif opinion_anime == 'neutral':
        "Por sua vez, você conta a ele sobre quando se deparou com Ismael à tarde,
        mas a conversa precisa ser constantemente interrompida já que Astério não faz ideia
        do que é anime."

        "Você decide que é melhor não tocar no assunto.
        Você terá bastante tempo para explicar a ele mais tarde."

    elif opinion_anime ==  'abomination':
        "Por sua vez, você conta a ele sobre quando se deparou com Ismael à tarde,
        mas precisa fazer uma pausa para explicar o que é anime."

        $Asterion.change("emotion", "surprise")

        "Acaba se transformando em uma divagação bastante longa e Astério fica cada vez mais horrorizado
        à medida que você descreve os terríveis efeitos da animação japonesa em mentes
        jovens e inocentes."

        "Você decide que a pobre criatura já passou por sofrimento suficiente e
        poupa-lhe os detalhes."

    scene bg oldquarters
    with Dissolve(1.0)
    $Asterion.change("emotion", "bowing")
    $Asterion.change("leftarm", "raised")
    $Asterion.change("rightarm", "loose")
    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve(1.0)

    "Vocês dois chegam aos aposentos do Mestre e, depois de uma reverência,
    Astério segue para seu quarto. Exausto depois de um longo dia, você faz o mesmo.
    Se tudo der certo, amanhã você resolverá o problema da internet de uma vez por todas."

    scene bg black
    with Dissolve(2.0)

    stop music fadeout 2.0

    pause 3.0

    play music "music/Calliopeia.ogg" fadeout 2.0 fadein 2.0

    "Se ele tivesse sido deixado na câmara fria por tempo suficiente, seu corpo teria congelado
    e seu último fragmento de mente queimado?"

    "Isto havia passado por sua mente com frequência. Seria possível algum dia se transformar em pedra?"

    "Por oitenta anos ele pensou — e se o próximo Mestre fosse filho de Clément? Ou talvez um bastardo de Jean Marie há muito tempo perdido e esquecido?"

    "E se ele tivesse as características sombrias de José, de dois mil anos atrás,
    ou talvez se parecesse com aquele homem ateniense ainda mais no passado?
    Algum outro redentor viria um dia?"

    "Astério construiu incontáveis cenários, criados com a paixão de um artesão — tornados ainda mais
    vívidos pela escuridão e silêncio que o cercava."

    "Mas tudo isso ficou para trás, mesmo que seu quarto seja mais claustrofóbico que a câmara fria.
    Esta noite o minotauro deita em sua cama, tão pequena para seu corpo."

    "Os lençóis que o cobrem formam um labirinto de vales e picos, serpenteando e
    se amontoando ao redor de seu corpo. Em seu sono, ele curva os dedos, dobrando o
    lençol em uma nova espiral de cobras."

    pause 1.0
    $Asterion.change("emotion", "tired")
    $Asterion.getNude()
    $Asterion.change("underwear", "loincloth")
    $Asterion.change("leftarm", "loose")
    $Asterion.change("rightarm", "loose")

    scene bg asterionbed
    show blackback:
        alpha 0.6
    show Asterion behind blackback:
        xalign 0.7 yalign 3.0
        ease 3.0 yalign 1.8
    with Dissolve (4.0)

    "Ele acorda.{w} Como um raio, sua mente é lançada de volta à existência e
    ele está consciente antes mesmo de perceber.{w} Que noite;
    é como se ele não tivesse dormindo nada."

    "Nada de fazer amor sereno com a cama e o travesseiro. Existir aqui nesta cama de cobras,
    de olhos bem abertos, é um desconforto da variedade mais mundana."

    "É então que ele diz em voz alta."

    asterion "Será que algum dia me tornarei pedra?"

    "Sua mente, ainda no devaneio entre sonho e plena consciência,
    é atacada por esta claridade significante."

    show Asterion:
        ease 3.0 yalign 1.0 xalign 0.5

    "Uma ideia o tira da cama. Por oitenta anos ele foi mantido afastado de
    uma certa amiga, a qual temia ver mais uma vez."

    "Mas agora é tão claro, tão simples. O que os manteve separados por tanto tempo,
    uma vez que eram tão próximos? Ainda na escuridão, o minotauro levanta e abre sua gaveta."

label chapter10wr:

    call screen dayManager("wardrobe")

    if Asterion.clothes == "nude":
        "Astério considera não vestir nada, mas acaba cedendo e veste algo."
        jump chapter10wr

    "Assim que está vestido, ele olha por trás do resto de suas roupas e encontra sua lira."

    $Asterion.change("emotion", "contemplative")
    $Asterion.change ("leftarm","raised")

    "Velha amiga, de fato. Sua mão encontra a superfície como um aperto de mão firme.
    As cordas sussurram à medida que o minotauro puxa a coisa toda de sua caixa."

    asterion "Enquanto viveres, brilha."

    "Juntos, eles escapam sorrateiramente, dois irmãos animados em sua rebelião."

    scene bg staircase
    with Dissolve(1.0)

    "O minotauro não ousa levantar os cascos por medo de acordar o Mestre ou qualquer
    um dos hóspedes enquanto segue o caminho para baixo. Exceto pelas escadas, ele patina com os
    cascos pelo marmore, provocando um leve som de assobio."

    "Através da claraboia acima das escadas, a luz do luar chove sobre o minotauro.
    Se houvesse uma testemunha para assistir à sua descida, um véu azul o cobrindo e o instrumento
    aninhado em seu peito, não haveriam dúvidas de sua linhagem real."

    scene entrancenight
    with Dissolve(1.0)
    play music "music/crickets.mp3" fadeout 1.0 fadein 1.0

    "Ele segue o caminho até a recepção e vai para fora.
    Um céu escuro o saúda com apenas a mais tímida faixa de roxo do amanhecer."

    "O minotauro se senta nas escadas do lado de fora e, sem cerimônia, dedilha as cordas."

    show CG5Asterion
    with Dissolve(1.0)

    $renpy.music.set_volume(1.0, delay=1, channel='music')
    play music "music/seikilos.mp3" fadeout 1.0 fadein 1.0

    "São como dois amantes separados por muito tempo — seu toque não produz a reação
    desejada. Não traz nenhum gemido de gratidão ou sensação de arrepiar."

    "Mas, conforme o minotauro afina sua lira e seus próprios ouvidos, as brasas sob todas
    as cinzas e carvão ressurgem. Uma única nota atinge a verossimilhança e faz seu coração cantarolar."

    "Mas esta é apenas a primeira corda. Ele continua com a afinação."

    asterion "Você acha que algum dia me tornarei pedra?"

    "Sua lira solta um soluço, uma nota tão aguda que dói."

    asterion "Eu costumava gostar da ideia, sim. Mas isso é bom, não é?"

    asterion "Os deuses não nos deixaram escolha. Estamos aqui para sempre. Mas fosse este
    nosso eterno destino...{w=0.2} Eu escolheria existir."

    "Durante a noite, uma doce umidade instalou-se no asfalto mais adiante, e agora rasteja até
    o minotauro, enviando arrepios em sua espinha."

    "De volta a Knossos, quantas vezes seu quarto foi deixado destrancado durante a noite,
    permitindo que ele se levantasse antes do amanhecer para testemunhar o palácio ganhando vida?"

    "Quantas vezes ele havia feito a mesma coisa neste hotel?"

    "Uma pessoa não deve se segurar com muita força a esses momentos preciosos;
    quanto mais alguém se apega ao tempo, mais rápido ele escapa."

    "Se Astério aprendeu alguma lição com seu aprisionamento,
    foi deixar tudo passar e segurar apenas um único grão de areia.
    Apenas o suficiente para transformá-lo em uma pérola. Uma memória eterna."

    "Nada mais é necessário."

    pause 2.0
    $renpy.music.set_volume(0.0, delay=1, channel='music')
    "Passos se aproximam por trás. O minotauro não olha na direção do som,
    mas sua orelha sacode em resposta."

    if first_guest == "Luke":
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "relaxed")
        show Kota:
            xalign 0.0 yalign 1.0 xzoom 1
        with Dissolve(1.0)
        pause 1.0
        $Kota.change("emotion", "surprise")
        kota "Ah, senhor Astério, bom dia. Por favor, perdoe-me pela intromissão."

        asterion "Não há necessidade para desculpas, senhor Kota.{w=0.2} Você teve uma noite agradável?"

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        kota "Sim, de fato.{w=0.2} Embora o quarto ainda estivesse um pouco mofado,
        a cama era muito mais confortável que qualquer outra que me deitei em um bom tempo."

        kota "Tive um sono muito tranquilo, obrigado."

        asterion "Fico feliz que tenha encontrado conforto em nosso alojamento."

        $Kota.change("emotion", "sad")

        kota "Bastante.{w=0.2} E... eu queria me desculpar por...{w=0.2} pelo que aconteceu ontem.
        Fui uma vergonha como hóspede para você e [player_name] com minha presunção."

        asterion "Está tudo bem. [player_name] e eu podemos ver de onde você tirou essa impressão,{w=0.2}
        mas garanto que estamos lidando com as coisas."

        asterion "São águas passadas, sim?"

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        kota "Sim. Soa bem para mim."

        $renpy.music.set_volume(1.0, delay=1, channel='music')
        "A conversa morre e o foco de Astério retorna para sua lira.
        Cada puxada de corda quebra o silêncio que caiu com uma elegância suave,
        perdurando no ar frio do crepúsculo até que sua descendente a substitua."

        "Astério não percebe a princípio que, assim como as notas cantarolando a partir das cordas da lira,
        Kota está demorando na porta do hotel. Quando uma educada tosse desliza para o som de seu dedilhar,
        sua orelha sacode para reconhecer a presença do dragão mais uma vez."

        $Kota.change("emotion", "happy")

        kota "Você é bastante habilidoso, se não se importa que eu diga. Um som tão puro e bonito-{w=0.2}
        quase soa como um koto tocando."

        asterion "Uma lira. Eu a venho tocando há{w=0.2} muito tempo."

        kota "Percebe-se."

        "O calor se acumula nas bochechas do minotauro enquanto o elogio arranca um sorriso tímido dele."

        asterion "Obrigado. Já faz um bom tempo que não toco para uma audiência,
        então, se você quiser se juntar a mim,{w=0.2} por favor, fique à vontade."

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")

        kota "Já que não se importa."

        hide Kota
        with Dissolve(2.0)
        show cg5Kota
        with Dissolve(1.0)

        "O dragão se aproxima, seus passos quietos e medidos de forma a evitar que se
        tornem uma interrupção indesejada para o som da lira de Astério.
        Kota se senta, suas costas contra a parede e seu olhar subindo para o céu estrelado."

        "A dupla permite que os pensamentos vagueiem enquanto seus ouvidos absorvem as notas suaves
        invocadas pelos dedos de Astério."

        "A batida dos dedos de Kota encontram o ritmo da música improvisada. E então o dragão fala,
        suas palavras retumbam como um contraponto a cada dedilhada."

        kota "Nove vezes ascendendo{w=0.3}\npara assistir à lua, cujo ritmo solene{w=0.3}\nainda marca apenas a meia-note."

        asterion "Hm?"

        kota "Ah, perdoe-me.{w=0.2} Eu estava perdido em pensamentos."

        "Astério não diz nada; seja por cortesia ou subserviência, nem mesmo ele tem certeza no momento.
        No canto do olho, ele observa enquanto a boca de Kota abre, fecha,
        e então abre mais uma vez para compartilhar os pensamentos enredando o dragão."

        kota "Sentar sob a luz das estrelas assim, ouvindo música e assistindo o
        mundo acordar...{w=0.3} me lembrou de..."

        pause 1.0

        kota "Me lembrou do momento que eu passaria com um companheiro de muito tempo atrás."

        "Astério espera por quaisquer palavras a mais, mas apenas isso parece ter sido uma luta
        para Kota ter tirado de si mesmo."

        $renpy.music.set_volume(0.0, delay=1, channel='music')
        "Os dedos do minotauro vacilam nas cordas da lira quando ele reconhece a solene matiz na
        expressão do dragão. A configuração da mandíbula de Kota. O olhar distante em seus olhos.
        A inquietação sob a superfície da calma forçada."

        "Quantas vezes o minotauro percebeu aquele mesmo olhar espiando por trás de um espelho?"

        asterion "E{w=0.2} este companheiro não está mais com você?"

        "A mão de Astério quase solta a lira de seu aperto para estender a mão e pegar as palavras
        de volta. Ele abaixa a cabeça."

        asterion "Desculpe por me intrometer."

        kota "Não, está...{w=0.2} está tudo bem."

        kota "Devo dizer, você é muito perceptivo, senhor Astério."

        $renpy.music.set_volume(1.0, delay=1, channel='music')
        "Novamente, o som da lira domina a conversa."

        pause 1.0

        kota "Suponho que agora seja um momento tão bom quanto qualquer outro. Eu esperava perguntar isso a você ou ao senhor
        [player_name],{w=0.2} mas talvez você esteja mais apto a responder."

        asterion "Vá em frente.{w=0.2} Se houver algo em que eu possa ajudar um hóspede, ficaria mais
        que feliz em oferecer assistência."

        kota "Obrigado."
        $renpy.music.set_volume(0.0, delay=0.5, channel='music')
        pause 1.5
        $renpy.music.set_volume(1.0, delay=0.5, channel='music')
        "Por um momento, as mãos de Astério congelam nas cordas da lira. Mas a escuridão e
        vastidão do deserto ao amanhecer em seus arredores estimulam seus dedos de volta ao movimento."

        "Kota percebe a curta pausa e dá ao minotauro um olhar agradecido quando a música suavemente
        tocada começa mais uma vez."

        "Às vezes, a música pode ser tão eficaz quanto o álcool para acalmar a alma
        e afrouxar a língua."

        kota "Já houve um dragão como eu que visitou seu hotel?{w=0.2} Um da
        terra de Nihon, com escamas vermelhas como fogo?"

        "Um cantarolar suave acompanha o toque agudo das cordas da lira. O minotauro pensa,
        procurando por memórias antigas e desvanecidas dos muitos hóspedes que ficaram ao longo dos séculos."

        "Ao perceber que não se lembra, ele dá ao dragão um aceno de cabeça de lamentação."

        asterion "Sinto muito, senhor Kota. Eu...{w=0.2} minha família e eu não temos memória ou registro
        de outro dragão já hospedado em nosso hotel.{w=0.2} Muito menos um do Japão."

        kota "Entendo."

        "Kota acena com a cabeça em aceitação, e Astério finge não ver os lábios do dragão tremendo."

        kota "Eu esperava que esta fosse a resposta."

        asterion "E, ainda assim, posso dizer que ainda lhe dói ouvir.{w=0.2} Minhas desculpas."

        "Kota olha na direção de Astério. Mesmo sem encontrar os olhos do dragão, o minotauro
        pode sentir o quão contemplativo é o olhar do outro homem."

        pause 1.0

        kota "...Perceptivo, de fato."

        "Astério continua a tocar, seus olhos em algum ponto distante nas areias inconstantes.
        No entanto, sua orelha sacode; um convite aberto para o dragão falar."

        kota "Senhor Astério... me permitiria mais uma pergunta?"

        asterion "Por favor, vá em frente."

        kota "Você já sentiu a dor da perda?{w=0.2} Como se alguma parte integrante de você
        tivesse sido escavada para fora de seu peito,{w=0.2} e tudo o que você pode fazer é implorar para virar pedra?"

        $renpy.music.set_volume(0.0, delay=1, channel='music')
        "Um estrépito cortante interrompe o momento de paz, fazendo Astério e Kota retraírem.
        A mão do minotauro se move para deter a corda vibrante, mas, como suas palavras anteriores,
        o som não pode ser pego de volta e silenciado."

        "Ele olha para a área desertificada em torno do hotel. Ele não esperava um eco dos
        pensamentos que o tiraram do calor do sono vindo de um dos hóspedes."

        "Seu dedo volta para as cordas e toca uma única nota.
        E depois outra, e outra."

        $renpy.music.set_volume(1.0, delay=1, channel='music')
        "Mais uma vez, o silêncio é preenchido com aquele doce licor que até agora manteve suas
        línguas soltas."

        asterion "Sim."

        asterion "Verdade seja dita, esse é um dos motivos pelos quais...{w=0.2}
        minha família e os Mestres mantiveram este hotel. Ele...{w=0.2}
        nós esperávamos torná-lo um local de cura."

        asterion "Desde veteranos de guerra feridos até aqueles sem nenhum lugar para ir,{w=0.2}
        temos nos empenhado em fornecer um local de conforto e segurança para todos que passam por nossas portas."

        kota "Um esforço nobre, com certeza."

        asterion "Há quanto tempo você está procurando por seu companheiro, senhor Kota?{w=0.2} Se eu puder perguntar."

        "O dragão abre a boca, fecha-a novamente e, em seguida, uma risada fraca e desanimada escapa de sua mandíbula."

        kota "Tempo suficiente para quase esquecer o início da minha busca. Pelo menos um século
        desde que saí de Nihon."

        "Kota afunda contra a parede, cansaço profundo em cada linha de seu rosto escamoso."

        kota "Às vezes me pergunto se algum dia irei encontrá-lo."

        "Rostos antigos pairam diante dos olhos de Astério. Pai Minos e Mãe Pasífae.
        Ariadne. José. Jean-Marie. [player_name]."

        asterion "Enquanto viveres, brilha."

        kota "Hm?"

        pause 1.0

        "Astério pisca e então abaixa a cabeça. O doce vinho da música manteve sua língua solta
        o suficiente para permitir que os pensamentos que o haviam tirado de sua cama escapassem."

        asterion "Desculpe, eu estava perdido em pensamentos."

        pause 1.0

        asterion "Mas...{w=0.2} se me permite?"

        "Kota não diz nada, mas um olhar na direção do dragão permite que Astério encontre o olhar
        atento de outro homem solitário pelo mais breve dos momentos. Tempo suficiente para a centelha de compreensão
        que esteve queimando na escuridão do amanhecer brilhar."

        asterion "É bom guardar as memórias de seu companheiro.{w=0.2} Especialmente se você
        tiver certeza de que ele está por aí em algum lugar."

        asterion "E{w=0.2} talvez, se ele for como você, pode acabar entrando em nossas portas
        um dia desses."

        asterion "Mas isto não vem ao caso."

        asterion "Tenha em mente que o passado pode consumir e deixá-lo cego para o presente."

        asterion "Muitos de nossos hóspedes no passado tiveram esse problema.{w=0.2} Tão obcecados
        com o que havia sido, que não podiam enxergar o que poderia ser."

        asterion "Eu..."

        pause 1.0

        asterion "...Me perdoe, estou ultrapassando meus limites."

        kota "Não, não.{w=0.2} Você é sábio, Astério."

        "Mais uma vez, os dois voltam seus olhares para o deserto; para o céu acima,
        muito mais vasto que suas minúsculas vidas."

        kota "Apesar… da presença de uma certa pessoa,{w=0.2} eu me diverti ontem à noite.
        Faz tanto tempo desde que eu apenas... descansei e conversei com companheiros durante uma refeição."

        kota "Eu esperava que durante minha estadia, você me permitisse... entrevistar quaisquer
        outros hóspedes que vierem para ver se eles podem oferecer alguma pista em minha busca.
        Mas isto..."

        "Ele gesticula ao redor de si mesmo. Para Astério nas proximidades, dedilhando sua lira.
        Para o alpendre ao redor deles, protegendo-os do ar frio da madrugada.
        Para a vista aberta diante deles, bela mesmo em sua desolação."

        kota "Apenas{w=0.2} {i}isto{/i}{w=0.2} é algo do qual estive sentindo a falta quase tão profundamente."

        asterion "Você é bem-vindo para ficar o tempo que quiser."

        kota "Obrigado."

        "Um sorriso flutua sobre o rosto de Kota, mas depois se transforma em uma pequena carranca."

        kota "Se ao menos um certo alguém não estivesse encarregado daquele… \"bar.\""

        "Astério cantarola, permitindo que as notas flutuando no ar pontuem suas próximas palavras."

        asterion "Senhor Luke pode ser... demais. Ele é{w=0.2} bruto{w=0.2} e grosseiro,{w=0.2}
        e frequentemente diz a pior coisa nos momentos mais inapropriados."

        asterion "Mas, apesar disso, ele também é um trabalhador diligente.{w=0.2} E você pode dizer que
        sua visita ao bar dele foi completamente desagradável?"

        kota "...Suponho que não."

        "Astério olha para cima para encontrar os olhos de Kota."

        asterion "Você deve dar pelo menos algum crédito a ele por isso."

        asterion "O que aconteceu ontem foi desagradável, isto eu vi com meus próprios olhos.{w=0.2} No entanto, você vai deixar isso colorir o resto de sua experiência aqui?"

        asterion "Se vocês dois ficarão em curta proximidade um do outro, não seria melhor
        permitir que o que aconteceu no passado permanecesse lá?"

        kota "Águas passadas, hm?"

        "O olhar de Kota cai para seu colo, onde seus dedos tocam uns aos outros. Suas narinas dilatam conforme ele bufa. Ele murmura algo que a orelha oscilante de Astério não consegue captar, então suspira."

        kota "Vou pensar sobre isso."

        asterion "Uhum."

        pause 1.0

        asterion "...Enquanto faz isso, gostaria de continuar me ouvindo tocar enquanto assistimos ao
        nascer do sol juntos?"

    else:
        $Luke.change("clothes", "tankpants")
        $Luke.change("dogtags", "false")
        $Luke.change("bandanna", "false")
        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")
        show Luke:
            xalign 0.0 yalign 1.0 xzoom -1
        with Dissolve(1.0)
        pause 1.0
        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "pointing")
        luke "Olha só, se não é o Angus."

        $renpy.music.set_volume(0.0, delay=1, channel='music')

        hide CG5Asterion
        with Dissolve(1.0)
        $Asterion.change("emotion", "contemplative")
        $Asterion.change("rightarm", "loose")
        $Asterion.change("leftarm", "raised")
        show Asterion:
            xalign 1.0 yalign 1.0
        with Dissolve(1.0)
        asterion "Saudações, senhor Walker.{w=0.2} Você teve uma noite agradável?"

        $Luke.change("emotion", "wink")

        luke "Agradável? Eu não diria que uma noite pode ser agradável se não tem
        ninguém na cama comigo.{w=0.2} Mas é, claro, foi um sono legal."

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")

        luke "O quarto é meio empoeirado e tem um cheiro estranho, mas caramba... a cama é ótima.{w}
        E essa música aí?{w=0.4} Ouro.{w=0.4} Ouro puro."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        asterion "Muito obrigado."

        $Luke.change("emotion", "laughing")

        luke "Só que assim...{w=0.2} admito que eu não pensei que você fosse um tocador de harpa, rapaz.{w=0.2}
        Você parece muito bruto pra isso, sabe?"

        $Asterion.change ("emotion", "neutral")

        luke "Além do mais, harpas são negócio de mulherzinha."

        asterion "Não é uma harpa, é uma lira."

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "pointing")

        luke "Mesma merda, Angus."

        $renpy.music.set_volume(1.0, delay=1, channel='music')
        $Luke.change ("arm", "hip")

        "Astério volta a tocar sua lira."

        asterion "Senhor Walker, eu poderia talvez fazer um pedido?"

        $Luke.change("arm", "pointing")

        luke "Você não tem que ser todo formal comigo, Angus.{w=0.2} Só dizer o que tá pensando."

        asterion "Meu nome é Astério, e eu peço que você dirija-se a mim como tal."

        $Luke.change("emotion", "cocky")
        luke "O que, você não gosta de ter um nome de mascote?"

        $Luke.change ("arm", "hip")

        asterion "Um nome de mascote?"

        pause 2.0

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")
        $renpy.music.set_volume(0.0, delay=1, channel='music')

        asterion "Por que? Eu não entendo. Seu tratamento me confunde
        profundamente, senhor Walker.{w=0.2}
        O que você quer dizer com tudo isso?"

        luke "O que, você não entendeu?{w=0.3} Eu te acho gostoso, simples assim."

        $Asterion.change ("emotion", "surprise")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")
        $Luke.change("emotion", "horny")

        luke "Eu te deixaria me foder a noite toda, fazer loucuras com a minha bunda."

        show Luke:
            ease 1.0 xalign 0.3
            ease 1.5 xalign 0.0
        $Luke.change ("arm", "pointing")
        luke "Eu sou um cara durão, sabe? Consigo aguentar tudo o que você quiser,
        então não precisa se conter. E deixa eu te contar... eu realmente espero que tenha
        uma tora escondida aí."

        pause 2.0

        $Asterion.change ("emotion", "sad")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        asterion "Eu...{w=0.3} me desculpe, você quer que eu...{w=0.3} você?"

        luke "Sim!{w=0.3} O que tem de tão estranho nisso? Jesus, pela sua reação
        , acho que você nunca conheceu um homem gay antes."

        $Luke.change ("arm", "hip")
        $Luke.change("emotion", "laughing")
        luke "O que, te criaram em uma caverna ou algo assim?"

        $Asterion.change ("emotion", "tired")
        $Asterion.change ("rightarm", "loose")

        asterion "...Gay?"

        $Luke.change("emotion", "wink")

        luke "Sim, eu gosto de homens. {w=0.2}Tanto foder quanto ser fodido.{w=0.2} Cê sabe, gay."

        luke "Porra, realmente te criaram numa caverna. Você é da Grécia, não é?{w=0.3}
        Que tipo de vida você teve lá?"

        pause 1.0
        $Asterion.change ("emotion", "sad")

        asterion "Então... isto é normal hoje em dia? Ser \"gay,\" quero dizer."

        $Luke.change("emotion", "annoyed")

        luke "...Você realmente não sabe, né."

        $Luke.change("emotion", "neutral")
        luke "Sim.{w=0.2} Com certeza é normal, e é a melhor merda de todas.
        Nem todo mundo gosta, claro, mas os homens são incríveis."

        luke "Você pode conseguir todo o sexo que quiser, ser hétero nem se compara."

        luke "Agora ser gay é normal. Tá na TV, as pessoas falam sobre isso
        nas ruas, existe tanto pornô gay..."

        pause 1.0

        $Asterion.change ("emotion", "tired")

        asterion "Entendo."

        $Luke.change ("arm", "pointing")
        luke "Então, você é?"

        $Asterion.change ("emotion", "sad")

        asterion "O que?"

        $Luke.change ("arm", "hip")
        luke "Gay, dã."

        $Asterion.change ("emotion", "tired")

        pause 2.0

        asterion "Não importa o que eu sou, senhor Walker. Eu sirvo ao hotel."

        asterion "Isto me dá toda a satisfação que eu poderia desejar."

        $Luke.change("emotion", "wink")
        luke "Ah, então trabalhar é o seu fetiche, né. Tipo de cara viciado em trabalho, isso é legal."

        luke "Quer saber qual é a minha praia?"

        $Asterion.change ("emotion", "neutral")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")
        $renpy.music.set_volume(1.0, delay=1, channel='music')
        "Astério dedilha suas cordas e lança um olhar de soslaio no grifo."

        luke "Então...{w=0.2} isso é um sim?"

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        pause 0.5

        $Luke.change("emotion", "happy")
        luke "Tá, então lá vai a coisa que me excita:{w=0.2} as estrelas."

        luke "Olha pra esse céu, Ang {w=0.3}— quer dizer, Astério. Eu já fui em todo lugar,
        conheço as minhas constelações."

        $Asterion.change ("emotion", "smiling")
        $Asterion.change ("rightarm", "hips")
        $Asterion.change ("leftarm", "loose")

        luke "Eu tenho o hábito de observar as estrelas, sabe?{w=0.3} E esse céu noturno
        é diferente de tudo o que eu já vi. Nenhuma das estrelas ou constelações que eu tô acostumado consigo encontrar nele."

        hide Luke
        hide Asterion
        with Dissolve(2.0)
        show cg5Luke
        show CG5Asterion
        with Dissolve(1.0)

        luke "É como se a gente tivesse em outro planeta.{w=0.2} Como que é isso,
        se não se importa que eu pergunte?"

        asterion "Ah... {w=0.2}talvez. Esta terra de fato não é um lugar comum,
        como você já deve ter adivinhado."

        asterion "Mas receio não saber o que contar para você sobre o céu noturno.
        Já faz um bom tempo desde a última vez que estive fora, então não consigo lembrar
        das constelações por nada."

        luke "Entendo... Então, você sabe se alguém mapeou esse céu noturno?"

        asterion "É possível, eu suponho.{w=0.2} Recebemos vários hóspedes ao longo dos anos."

        asterion "Alguns eram bastante aventureiros e gostavam de explorar o vale,
        talvez tenham mapeado o céu na época."

        asterion "Mas tenho quase certeza de que não há constelações oficiais."

        asterion "Agora... este trabalho lhe interessa, senhor Walker?"

        luke "Me interessa? {w=0.3}Rapaz, olha, eu não tenho ideia do tipo de magia estranha que
        tá acontecendo aqui. Talvez seja uma péssima ideia ficar por aqui nesse lugar."

        luke "Mas, caramba, mapear todo um novo céu noturno!"

        luke "Vai ser igual a quando eu era criança!"

        pause 1.0

        luke "Mas...{w=0.2} isso iria demorar muito, não é?
        Não sei se vou ficar aqui por tanto tempo."

        asterion "Entendo. Há assuntos externos que requerem sua assistência?"

        luke "Ah.{w=0.2} Não, acho que não. Posso parecer jovem, e com certeza ainda tenho muito
        {i}culhão{/i} sobrando, mas eu tô aposentado."

        luke "Ainda assim, eu tenho uma casa pra voltar.{w=0.2} Uma cabaninha.{w=0.2}
        Então, sim, não sei quanto tempo vou ficar."

        asterion "Eu entendo, deve haver pessoas esperando por você em casa."

        pause 3.0

        asterion "Sabe, Luke, você é muito mais agradável de se conversar quando não está
        permitindo que seus impulsos básicos o controlem."

        asterion "Por que você age assim?{w=0.2} Precisa ser tão lascivo o tempo todo?"

        pause 2.0

        luke "Bem, se eu {i}preciso{/i}? Nah, preciso não.{w=0.3} Mas é divertido,
        e você ficaria surpreso com o quanto isso me faz conseguir uma transa."

        luke "Me mete em um monte de brigas também, mas eu consigo me segurar."

        luke "Dá uma sensação boa, sabe? Simplesmente liberar tudo, faz os outros saberem o que eu quero e,
        aconteça o que acontecer...{w=0.2} vai ser emocionante."

        luke "Além disso, não é como se importasse, de qualquer forma. As pessoas vão acabar
        me esquecendo mesmo, então é melhor eu causar uma impressão enquanto posso."

        luke "Até você, tenho certeza que você vai me esquecer quando eu for embora."

        $renpy.music.set_volume(0.0, delay=1, channel='music')
        pause 1.5
        asterion "Não. Me lembrarei bem de você, senhor Walker."

        pause 1.0

        luke "Oi?"
        $renpy.music.set_volume(1.0, delay=1, channel='music')

        asterion "Não me esquecerei de você. Eu tenho uma memória muito boa, e alguém tão... \"notável\"
        como você não fica para trás facilmente."

        luke "Você só tá dizendo isso pra me provocar. Não é uma coisa que você consegue controlar, tá?
        {w=0.2}É o amuleto."

        asterion "O amuleto não funciona aqui, lembra? Eu não sei como eles funcionam,
        então você terá que me desculpar, mas aqui eles são inúteis."

        asterion "Talvez seja algo que você deva ter em mente; tudo o que você disser e fizer
        aqui, nada será apagado."

        pause 1.0

        luke "Isso meio que dá tesão."

        $renpy.music.set_volume(0.0, delay=1, channel='music')

        asterion "Por que você é assim?"

        asterion "Posso segurar minha língua com frequência...{w=0.2} talvez com frequência até demais.{w=0.2}
        Tenho um dever e reputação a zelar, afinal."

        asterion "Mas aqui estamos, apenas você e eu."

        asterion "Por que você é assim?{w=0.2} Não pode falar comigo direito?"

        asterion "Certamente você pode, mas escolhe não fazer isto."

        asterion "Talvez você esteja tão acostumado a ser esquecido que não tem mais ideia de como
        se dirigir aos outros de maneira adequada. Ou talvez você simplesmente não se importe sobre como os outros se sentem."

        #luke is astonished at his doctrine
        #luke gets angry

        pause 1.0

        luke "Eu, eu —"

        pause 1.5
        #gets sad

        luke "Eu me importo sim, ok? Eu sou só um idiota de merda."

        luke "Mas é melhor você acreditar que eu me importo, eu daria as roupas que cobrem a minha bunda pra um estranho em necessidade."

        luke "Sim, claro, toda essa coisa de ser esquecido fode comigo. Mas eu...
        Eu {i}sou{/i} inútil, eu só não sou um merda."

        $renpy.music.set_volume(1.0, delay=1, channel='music')

        asterion "Você deseja ser lembrado?"

        luke "Sim, é claro que sim, porra."

        asterion "Então você é bem-vindo para ficar aqui. Há muito trabalho a ser feito,
        e estamos sempre precisando de mais ajuda."

        luke "..."

        luke "Mas...{w=0.4} porra, aquele dragão é um cuzão."

        asterion "É mesmo? Ele parecia abrupto, verdade, mas...{w=0.4} esta é uma maneira muito rude de se
        enxergar isto, senhor Walker."

        asterion "Mas, diga-me, isso importa? Supondo que o senhor Kota seja de fato desagradável,
        está me dizendo que você é melhor do que ele?"

        asterion "Ele precisa ser, digamos, simpático? Não é suficiente ser
        bom e gentil, mesmo que seja imperfeito?"

        pause 3.0

        luke "Caramba, Astério, não sei o que te mordeu. Achei que você fosse meio caipira ou
        sei lá,{w=0.4} como eu costumava ser."

        luke "Eu vou pensar nisso, é tudo o que eu vou dizer."

        asterion "Uhum."

        pause 2.0

        asterion "Há mais uma coisa."

        asterion "Será que as pessoas neste hotel esqueceriam o homem que mapeou seu céu noturno?"

    stop music fadeout 4.0
    scene bg black
    with Dissolve (3.0)
    pause 2.0

    $chapter = "Capítulo 11"

    call screen ChapterTransition("Capítulo 11", "A expedição")
    pause 0.5
    $save_name=output_save_name("Capítulo 11")

    play music "music/OneWitness.ogg" fadeout 1.0 fadein 1.0
    play sound "sfx/flute.ogg"
    "Você acorda, mas, ao contrário dos outros dias, não é por causa do bater de cascos.
    Não, esta bela manhã você salta da cama com uma urgência esbaforida."

    "Há o som distante, mas inconfundível de...{w} uma flauta.{w} Um arrepio sobe
    através de sua espinha até a parte de trás de seu crânio."

    scene bg oldquarters
    $Asterion.change("emotion", "sad")
    $Asterion.change("leftarm", "loose")
    $Asterion.change("rightarm", "loose")
    show Asterion:
        xalign 0.5 yalign 1.5 zoom 0.9
    with Dissolve(1.0)

    "Assim que você sai de seu quarto, encontra Astério sentado à mesa de jantar,
    olhando para as próprias mãos, sem palavras. Apenas o som de seus passos faz a cabeça dele
    virar para você, as orelhas sacudindo."

    "Imagens de Argos, a cobra, já estão passando pela mente do minotauro.
    Você diz para ele ficar, hoje você lidará com o Capataz sozinho."

    scene bg staircase
    with Dissolve(1.0)

    "Você segue o caminho até lá."
    play sound "sfx/flute.ogg"
    scene bg valley_exit
    with Dissolve(1.0)

    "A flauta de madeira da cobra acena para você. A melodia às vezes é desconcertante
    considerando quão largos são os intervalos entre as notas — muito sobra para a imaginação."

    "É mais um chamado tribal do que uma canção, que você ouviria como um sinal entre
    aldeias enviando mensagens umas às outras. As notas puxam seus passos adiante."

    "As pedras soltas na base do hotel estremecem conforme você pula de uma para a outra.
    É um ato de equilíbrio, cada uma representando uma mudança de escala sob seu peso."

    if player_background == "speedrunner":
        "Mas seus membros magros e estrutura descoordenada não possuem a elegância necessária para conseguir.
        Como uma besta, você cai e anda de quatro."

    else:
        "Você mantém os pés tensos e os braços abertos. Às vezes, é quase como se as pedras
        balançassem a seu favor para manter o centro de gravidade alinhado."

    scene bg valley
    with Dissolve(1.0)

    "Você sente o calor do sol em sua cabeça primeiramente, penteando seu crânio.
    E então os rosas, laranjas e azuis da terra são expostos diante de você."

    "Na entrada, é claro como o vento uiva e assobia enquanto desliza para
    dentro da caverna do hotel e rasteja para cima."

    "Uma brisa fria constante pinica sua pele{w=0.2} — mas não é completamente desagradável.
    O frio torna seu próprio calor interior ainda mais vivo."

    "É você, uma partícula bruxuleante de humanidade, contra a magnitude inflexível deste vale assombrado."

    $PressQuestions = ['n','n','n','n','n','n','n','n','n']
    $KnowAboutKiln = False
    $KnowAboutShrine = False

    if ArgosContract == "Tricked":
        "E ainda... a canção da cobra paira pesadamente. Às vezes, Argos fica sem fôlego e
        uma tosse seca corta caminho através do vale."

        $Argos.change("pelt","True")
        $Argos.change("emotion","sad")
        $Argos.change("pose","straight")

        show Argos:
            xalign 0.5 yalign 1.0 zoom 0.6
        with Dissolve(1.0)

        "Ele parece não notar você. O olhar da cobra permanece em sua pequena flauta de madeira,
        como se não houvesse nada mais no mundo além dela."
        show Argos:
            ease 1.5 xalign 0.515
            ease 1.5 xalign 0.485
            repeat

        "Na verdade...{w=0.2} Ele oscila de um lado para o outro, ou nauseado ou com tontura,
        respirando pela boca."

        argos "Ah, que vida miserável! Ser açoitado por este sol impiedoso, congelado
        pela terrível noite, ressecardo pelo ar morto! E, o pior de tudo, faminto pela dureza humana!"

        "Ele parece não ter notado você, mas se empoleira em cima da estátua e fala
        com todo o talento dramático de um ator em um palco."

        $Argos.change("emotion","surprised")
        $Argos.change("pose","straight")

        you "Eu estou aqui, sabe. Posso ouvir tudo o que você está dizendo."

        argos "Ah!{w=0.2} Meu senhor, quando você chegou?{w} Por favor, perdoe minha insolência!"
        show Argos:
            ease 0.4 xalign 0.53 zoom 0.7
            ease 0.4 xalign 0.47 zoom 0.8
            ease 0.4 xalign 0.53 zoom 0.9
            ease 0.4 xalign 0.5 zoom 1.0

        "Ele passeia em volta, alisando sua capa para deixá-la limpa e apresentável."

        $Argos.change("emotion","sad")
        $Argos.change("pose","crossed")

        argos "Mais uma vez, meu senhor, lamento terrivelmente por meu estado inadequado."

        you "Alguma coisa aconteceu com você? Há algum problema?"

        argos "Ah, acontece que eu tenho...{w=0.2}passado um pouco de fome nos últimos dias.{w}
        Consegui encontrar apenas insetos o suficiente para me acalmar até dormir."

        argos "Quanto à água, tudo o que pude encontrar foi uma poça lamacenta de água parada dentro de uma gruta...
        Não fosse eu uma cobra, já teria perecido a essa altura!"

        $Argos.change("emotion","surprised")
        $Argos.change("pose","straight")

        argos "Por favor, meu senhor, hoje vim à sua porta para pedir{w=0.2} — implorar, na verdade —{w=0.2}
        que reconsidere.{w} Conceda-me os direitos para invocar minha própria comida e moradia!"

        you "Mas por que eu deveria fazer isto? Você está aqui para torturar Astério, que,
        como você pode ver, não é algo que eu pretendo permitir que aconteça."

        you "Por que eu deveria te dar qualquer coisa? Por que você acha que é bem-vindo aqui
        em primeiro lugar?"

        argos "Mas meu senhor... sou seu seguidor mais leal! A punição do bezerro é nosso
        dever, tanto seu quanto meu, e eu sou o único que seguirá você até o fim!"

        $Argos.change("emotion","sad")
        $Argos.change("pose","straight")

        argos "Eu nasci para servi-lo...
        é a razão pela qual este vale me gerou de suas entranhas..."

        argos "Por favor, conceda-me comida e provarei meu valor!
        Minha dedicação não possui limites."

        argos "Nas últimas noites, não comi nada além de insetos, as mais baixas das criaturas
        que vagam por este vale."
        argos "Tamanha falta de dignidade é imprópria para meu papel como Capataz, mas isto eu farei
        mil vezes caso signifique receber seu favor."

        argos "Por favor... eu já consigo ouvir o fluir das águas do Estige..."

        pause 2.0

        you "Nah."

        pause 3.0

        $Argos.change("emotion","cocky")
        $Argos.change("pose","straight")

        argos "Bem, valeu a pena tentar."

        argos "Para sua informação, estou realmente vivendo de insetos.{w} E odeio isto."

        $Argos.change("emotion","smug")
        $Argos.change("pose","crossed")

        argos "Que mestre diabólico você é! Primeiro engana seu único seguidor,
        aquele que esperou uma vida inteira por você, e agora o faria morrer de fome!"

        argos "Quão caloroso seria banhar suas mãos em meu sangue! É isto o que você deseja?"

        you "E se eu desejar?{w=0.2} Existe uma regra contra?"

        argos "Sua serpente de língua prateada!"

        $Argos.change("emotion","cocky")
        $Argos.change("pose","straight")

        argos "...O que significa que somos almas gêmeas, você e eu."

        argos "Sei como você pensa. Você quer alguma coisa em troca.
        Então, vamos ao que interessa."

        argos "Se você gosta tanto do híbrido, tenho algo que será de seu interesse."


    if ArgosContract == "Contested":
        $Argos.change("pelt","True")
        $Argos.change("emotion","smug")
        $Argos.change("pose","straight")

        show Argos:
            xalign 0.5 yalign 1.0 zoom 0.6
        with Dissolve(1.0)

        "A música de Argos termina com uma nota estendida — grave a princípio, conforme flutua pelo vale,
        mas ficando animada por apenas um momento antes de cessar."

        $Argos.change("emotion","cocky")

        "A cobra olha para você da estátua, não menos que cinco metros acima de você.
        A diferença deixaria muitos desconfortáveis; quão fácil seria para ele atacar você?"

        "Mas a cobra segura sua flauta com as duas mãos, quase embalando-a contra o peito.
        Com os braços juntos, ele parece inteiramente pequeno, mesmo com o persistente sorriso de língua prateada."

        "Ele também leva um momento para olhar você de cima a baixo.
        Ele cobre a boca para abafar uma explosão de risadinhas infantis."

        $Argos.change("emotion","neutral")

        argos "Meu senhor de olhos brilhantes, mais uma vez é uma honra testemunhar seu encanto.{w=0.2}
        É um belo dia, e sempre será enquanto seu semblante abençoar este vale."

        $Argos.change("pose","crossed")

        argos "Ah,{w=0.2} como é bom ser presenteado com um propósito!{w=0.2} Para que serve um cão de guarda sem mestre para
        seguir e sem bezerro para vigiar?"

        argos "Espero que sua experiência até agora tenha sido tão enriquecedora quanto a minha.
        {w=0.2}Diga-me, o espelho lhe forneceu conforto?{w=0.2} Seu primeiro lote de hóspedes chegou?"

        show Argos:
            ease 0.4 xalign 0.53 zoom 0.7
        "A cobra se inclina para frente, ansiosa por cada palavra sua.
        Não estivesse ele enrolado em torno da estátua, cairia como um macarrão molhado,
        mas isto parece não lhe trazer nenhum desconforto."

        "Na verdade, quase parece como se ele quisesse descer e ficar cara a cara com você.
        Seu olhar entreaberto não se afasta de você,
        acompanhando até mesmo as menores mudanças em sua postura."

        "Não é sempre que um foco tão intenso é disposto em alguém. Desconforto seria uma
        reação comum, ainda assim, seu olhar carece de um toque de predador."

        you "Estou indo bem, Argos.{w=0.2} O espelho tem sido muito útil — o hotel
        mudou completamente depois que acendemos o fogo."

        you "É incrível o que este domínio pode realizar.{w=0.2}
        Astério estava me mostrando algumas das capacidades dele, e temos pessoas
        trabalhando em uma tecnologia agora."

        $Argos.change("emotion","smug")

        argos "Entendo, entendo.{w=0.2} Muito bem, realmente é dever do prisioneiro informá-lo
        sobre o funcionamento do domínio. Suas obrigações não devem ser negligenciadas."

        $Argos.change("emotion","cocky")

        argos "Mas...{w=0.2} Ah, eu não posso mentir. Não é surpresa que nosso senhor se importe tanto
        com tecnologia. Isto, de fato, é da natureza humana, sempre buscar mudança e movimento."

        $Argos.change("pose","straight")

        argos "Estas paredes lisas não devem entreter um homem por muito tempo. E se é de seu
        interesse não gastar seu tempo colocando o híbrido através de provações, então
        a tecnologia se torna ainda mais imperativa."

        argos "A natureza humana, como fogo, frequentemente requer lenha adicional."

        $Argos.change("emotion","neutral")
        $Argos.change("pose","crossed")

        you "O que você sabe sobre a natureza humana? Você não é um homem,
        e o que você viu da humanidade nesse lugar?"

        you "E sobre tecnologia, como você pode saber de qualquer coisa?
        Julgando pelo que posso ver, o máximo que você domina é
        costura e escultura."


        $Argos.change("emotion","smug")

        argos "Ah, nosso senhor tem uma língua afiada!"

        argos "De fato, sei muito pouco. Nunca me aventurei além deste vale e
        para sempre permanecerei aqui."

        argos "Mas tenho conhecimento dos deuses e das antigas histórias dos heróis."

        argos "Sou uma cobra antiquada.{w} Todos os épicos eu memorizei,{w=0.2}
        todas as suas belas poesias."

        argos "A humanidade às vezes exibe qualidades que excedem às dos deuses.
        Não desprezo a engenhosidade humana, meu senhor."

        $Argos.change("emotion","cocky")

        argos "Diminuir a importância disto seria muito{w=0.2}
        não-cobra de minha parte, não seria?"

        argos "Ai de mim, que bela maneira de chegarmos ao propósito da visita de hoje.
        Meu senhor de olhos brilhantes, tenho o contrato pronto para sua assinatura."

        you "Ótimo.{w=0.2} Pare de enrolar e vamos fazer isso."
        show Argos:
            ease 0.4 xalign 0.47 zoom 0.8
            ease 0.4 xalign 0.53 zoom 0.9
            ease 0.4 xalign 0.5 zoom 1.0

        "Ele enfia a mão dentro de sua capa, mas para enquanto contém uma risadinha."

        if contestContract == '4':

            $Argos.change("pose","straight")
            $Argos.change("emotion","neutral")

            argos "Antes de prosseguirmos, devo perdir seu perdão.{w=0.2}
            Cometi um grave erro ao redigir a versão anterior."

            argos "Por assim dizer, ela implicava que eu teria o direito de entrar e inspecionar o hotel.
            E isto, como ambos sabemos, é proibido por lei antiga."

            argos "Estaríamos \"simetricamente comprometidos\" pelo artigo. Já que você poderia
            inspecionar minhas acomodações, eu seria capaz de inspecionar as suas."

            $Argos.change("emotion","cocky")

            argos "Que honra é servir a um senhor tão perspicaz como você!
            Eu vejo as qualidades da Atenas de olhos brilhantes em você, tenho certeza de que foi a
            mão dela que tirou você dentre a humanidade."

            "Ele joga o pergaminho para você.{w=0.2} Você dá uma boa olhada nele, em todos os artigos;
            agora você pode dizer com certeza que este contrato está correto e agradavelmente a seu favor."

            "Afirma que você tem o direito de inspecionar a residência do Capataz, ao mesmo tempo que reforça
            a antiga lei que proíbe as criaturas do vale de entrar no hotel."

            you "Sem truques dessa vez. Ótimo."

            $Argos.change("pose","crossed")

            argos "Certamente não.{w=0.2} Você deve pensar que minhas palavras são lisonjeiras, mas hoje estou
            inspirado apenas pela honestidade: eu respeito um homem alerta que pode separar a verdade do engano."

            argos "Ah, que diversão teremos, você e eu! Um privilégio isto é, servir a um mestre como você!"

            $Argos.change("emotion","angry")

            you "Diversão? Receio discordar. Sua definição de \"diversão\"
            envolve um monte de tortura, uma coisa da qual este domínio será privado durante
            a minha gestão."

            you "Acredito que sua vida comigo por perto será de um tédio intenso e interminável.
            Talvez você deva pedir aos seus deuses que removam você."

            $Argos.change("emotion","smug")

            argos "Ah, mas aí que está a diversão!"

            argos "Tudo se resume à natureza humana. Todos da sua espécie ficam entediados com tudo isso...
            a monotonia, dia após dia, sempre a mesma coisa!"

            $Argos.change("pose","straight")
            $Argos.change("emotion","cocky")

            argos "E aí, bem lá em cima, está aquele híbrido."

            argos "Você pode fazer aquilo que seu coração desejar, ele não pode se defender.
            E, caso seja de sua vontade, ele também não contará a ninguém!"

            argos "Há um fascínio nisto. Não é divertido,
            estimulante até, ver alguém como ele sofrendo?
            Um miserável submetido aos extremos que ele merece!"

            $Argos.change("pose","crossed")

            argos "Assistir à sua mudança inevitável — isto, para mim,
            será o maior espetáculo!{w=0.2} Está claro que você e eu
            seremos queridos amigos no devido tempo."

            $Argos.change("emotion","neutral")

            you "Sem chance. Você ainda tem muito a aprender sobre a natureza humana."

            you "Bem, terminamos aqui? Eu gostaria muito de voltar para o meu hotel."

            $Argos.change("emotion","smug")

            argos "Não, ainda não! Primeiro, assine o contrato e, em seguida, há mais um tópico que devemos discutir."

            "Você o assina e joga de volta para a cobra."

            argos "Muito bem. Agora, tenho algumas informações que podem interessar a você."

        else:

            $Argos.change("pose","straight")
            $Argos.change("emotion","neutral")

            argos "Antes de prosseguirmos, no entanto, devo dizer que lamento terrivelmente.
            Passei incontáveis horas estudando o contrato, mas não consegui encontrar falha alguma."

            argos "É um contrato perfeitamente normal, de acordo com os antigos costumes
            entre o Capataz e o Mestre."

            "Ele joga o pergaminho para você.{w=0.2} Você dá uma boa olhada, e é exatamente
            como você se lembra; nenhuma mudança foi feita."

            you "Ãhn...{w=0.2} Eu pensei..."

            $Argos.change("pose","crossed")
            argos "Sim?"

            you "...Eu não me lembro exatamente o que achei que estava errado.{w=0.2} Posso ter um pouco
            mais de tempo para pensar sobre isso?"

            $Argos.change("emotion","smug")

            argos "Ah, mas meu senhor, você deve se lembrar que lhe permiti pegar emprestado o espelho
            enquanto eu revisava o documento."

            argos "Se é de sua vontade revisar o contrato por um período de tempo prolongado,
            então lamento informar que devo pegar o espelho de volta."

            argos "Ah... que tal nos encontrarmos novamente em uma semana?{w=0.2} Tenho que inspecionar
            e vasculhar o vale, veja bem, e demorará um pouco até que seja conveniente para mim passar
            por aqui novamente."

            you "Mas aí nós ficaríamos uma semana sem o espelho!"

            $Argos.change("emotion","cocky")

            argos "Sim, isto é muito lamentável, de fato. Mas é o que é."

            argos "Seu hotel ficará sem todas as suas fantásticas capacidades.
            Seus hóspedes ficarão tão desapontados. Uma lástima, eu sei."

            $Argos.change("emotion","neutral")

            argos "Então, como será? Você vai assiná-lo
            ou deixará seu precioso hotel sofrer?"

            argos "Veja bem — não tenho obrigação alguma de arranjar tempo para uma negociação daqui a uma semana.
            Sucedido o contratempo, poderia demorar ainda mais para o meu retorno!"

            "A cobra pegou você pelas bolas. Não há escolha viável, exceto assinar o contrato."

            "Você o assina."

            $Argos.change("emotion","smug")

            argos "Maravilhoso! E com isto, você terá todos os
            confortos de que vocês, humanos, gostam tanto."

            argos "Quão diferente seria se os humanos não estivessem acorrentados a tais luxos!
            Mesmo alguém como eu pode viver da terra, por que não os humanos também?"

            you "Sabe, nós, humanos, realmente gostamos de dormir sob um teto.
            Talvez você devesse tentar um dia desses."

            $Argos.change("emotion","angry")

            argos "Hum!{w=0.4} Talvez sim, agora que o contrato está assinado.
            Me certificarei de contá-lo quão desagradável é a experiência.{w=0.2}
            Deve ser tão claustrofóbico estar cercado por paredes."

            you "Bem, então terminamos aqui? Posso voltar para o meu hotel claustrofóbico?"

            $Argos.change("emotion","smug")

            argos "Ainda não, meu bom senhor. Há um assunto final que desejo abordar,
            algo do qual tenho certeza que despertará seu interesse."


    if ArgosContract == "Signed":
        $Argos.change("pelt","True")
        $Argos.change("emotion","neutral")
        $Argos.change("pose","straight")

        show Argos:
            xalign 0.5 yalign 1.0 zoom 0.6
        with Dissolve(1.0)

        "Assim que você põe o pé para fora,{w=0.2} os olhos da cobra se fixam em você e..."
        play sound "sfx/flute.ogg"
        show Argos:
            ease 1.5 xalign 0.515
            ease 1.5 xalign 0.485
            repeat

        $Argos.change("emotion","cocky")

        "Ele faz um desfile solo,{w=0.2} balançando sua flauta da esquerda pra a direita
        enquanto seu corpo inteiro balança no ritmo."

        "Toda a pele que ele usa como capa sacode junto com ele,{w=0.2} e da parte de baixo
        ele puxa algo que você não consegue distinguir direito."

        "Ele assume uma espécie de marcha estacionária. Seus movimentos de lado a lado servem para
        agitar sua capa e caminhada simulada, bem como para dissipar seu fôlego o mais rápido
        possível. Torna cada nota ainda mais estridente."

        "Então você percebe a cauda dele se movendo, enrolando-se para trás, visando embalar algum tipo de disco marrom.
        E então a ponta sobe: está agarrando uma baqueta lisa. Ele golpeia para baixo."
        play sound "sfx/drum.ogg"
        "Um ritmo enfadonho corta através do vale,{w=0.2}e então novamente sua cauda sobre e desce!{w}
        Mas desta vez,{w=0.2} ela erra e atinge a estátua em que ele está, ou ainda mais abruptamente
        atinge a sua cauda enrolando em torno do tambor."

        $Argos.change("emotion","angry")

        "A cobra segue em frente, tentando acertar a baqueta no disco,
        mas lhe falta a coordenação. Com certa frequência, ele acerta em si mesmo e,
        mesmo quando acerta, ainda é fora de ritmo."

        $Argos.change("emotion","neutral")
        $Argos.change("pose","crossed")
        stop sound

        "Finalmente,{w=0.2} ele termina a música e faz uma reverência para você."
        show Argos:
            ease 0.5 yalign 1.1
            ease 0.5 yalign 1.0

        argos "O herdeiro dos Olímpios nos agracia mais uma vez com seu semblante!{w=0.2} Ah,
        bom senhor, sua presença de alguma forma acalma e revigora este servo."

        argos "Eu não consigo me controlar, entende.{w=0.2} Esperando seu retorno,
        o mero pensamento envia alegria e música do meu crânio para a ponta de minha cauda."

        argos "Por favor, diga,{w=0.2} nosso senhor gostou do pequeno show que preparei?"

        you "Hã.{w=0.2} O que era aquela coisa que você estava batendo?"

        argos "Não incomodarei você com modéstia. Em vez disso, lhe contarei minha ideia velada
        agora — minha ideia sobre a música de grande e bela importância que veio desta colina
        longínqua. {w}...Bem... {w=0.2} não adiciona um ritmo afiado a esta música?"

        $Argos.change("emotion","smug")

        argos "Este aqui é um instrumento magnífico, um {i}tímpano{/i}!{w=0.2}
        É uma forma muito tradicional de tambor."

        "Ele bate duas vezes à \"mão\" com sua cauda desajeitada e descoordenada."

        if player_background  == "arts":
            you "Então, por que você está usando um bastão e não sua mão?"
            "A cobra, no entanto, parece não ouvir seu comentário."

        $Argos.change("emotion","cocky")

        argos "Certamente você concordará{w=0.2} — inspira uma chama no coração,{w=0.2}
        e não se pode evitar dançar em seu ritmo antigo."

        argos "O Mestre é atento e devoto.{w=0.2} Certamente em seu sangue ainda corre
        a herança da glória antiga{w=0.2} — o suficiente para apreciar um instrumento tão clássico."

        $Argos.change("emotion","neutral")

        argos "Eu invoquei os materiais e o montei sozinho,{w=0.2}
        graças àquele pequeno contrato que você assinou! Se tivesse um pouco mais,
        poderia ter dobrado meu som aqui e invocado um aulo."

        "Um som estridente em sua flauta simples perfura o ar."

        argos "Depois de minha apresentação, sei que o Mestre entende o fascínio dos clássicos.
        Você já ouviu sons tão magníficos em seu mundo humano?"

        you "Lamento dizer,{w=0.2} mas nos últimos milhares de anos os humanos foram um pouco além
        de tubos de madeira e tambores de couro."

        you "Podemos até gravar músicas agora. Se eu quiser ouvir uma música que gosto,
        só preciso colocar ela no meu celular."

        $Argos.change("emotion","surprised")
        pause 1.0
        $Argos.change("emotion","neutral")

        argos "Desculpe-me? Como alguém poderia {w=0.2}{i}colocar{/i}{w=0.2} música?{w}
        A música é efêmera,{w=0.2} dura apenas por um momento."

        you "Bem, agora nós podemos gravar e armazenar elas. Eu tenho algumas músicas de caras
        que morreram há muito tempo. É uma das maravilhas da tecnologia humana."

        $Argos.change("emotion","smug")

        argos "Mestre, você é tão bobo!{w} \"Não posso acreditar que qualquer besta faça música
        quando morrem.\"{w=0.2} A música vem da alma, nascida do sopro divino que os próprios deuses
        nos concederam."

        $Argos.change("emotion", "cocky")
        argos "Nenhum objeto,{w=0.2} desprovido de alma e sem a ajuda de uma mente virtuosa{w=0.2}
        jamais poderia reproduzir uma beldade tão elevada quanto a música."

        you "Você ficaria surpreso com o que nós, humanos, criamos, então.
        Talvez tenhamos que concordar em discordar."

        argos "Ah,{w=0.2} tenho certeza de que você voltará na hora certa,{w=0.2}
        você só precisa ouvir mais algumas de minhas músicas.{w} Então, o que achou de meu espetáculo?"

        menu:
            "O que você achou da música?"
            "Foi horrível.":
                you "Foi horrível. Parecia uma criança tocando um conjunto de tambores
                enquanto tinha um derrame."

                you "Seu instrumento antigo soa igual merda."

                $Argos.change("emotion", "neutral")
                show Argos:
                    ease 0.3 xalign 0.55
                "As sobrancelhas da cobra levantam em choque com a franqueza.
                Seu sorriso imperturbável permanece."

                pause 1.0

                argos "Ah."

                show Argos:
                    ease 1.0 xalign 0.5

                argos "F{w=0.2}-foi p{w=0.2}-porque eu continuava errando?{w} Eu sinto muito,
                {w=0.2} pratiquei tanto nos últimos dias..."

                argos "Farei melhor na próxima vez — vou tentar! E eu tenho o poder...!{w=0.2}
                Eu prometo."

                you "Na verdade,{w=0.2} a coisa toda soava horrível.{w}
                Quase não teve qualquer lógica ou sentido."

                you "Se isso era o que costumava ser considerado música na Grécida Antiga...{w}
                Estou muito feliz por termos chegado tão longe daqueles tempos primitivos."

                pause 1.0

                $Argos.change("emotion", "sad")

                pause 2.0

                argos "Ah..."

                "Mesmo da base da estátua, você pode ver seu rosto se contraindo.
                Seu lábio inferior estremece e ele se esforça para engolir o nó em sua garganta."

                show Argos:
                    ease 1.0 yalign 1.2

                "Ele solta a baqueta. Ela quebra assim
                que atinge o solo, mas a cobra não liga para isto.{w}
                Ele desaba na própria cauda em uma simulação de cair em joelhos."

                "Ele abraça sua flauta e bufa,{w=0.2} tentando evitar que saia ranho de seu nariz."

                $Argos.change("emotion", "angry")

                "Mas então, algo se contorce dentro dele — ele se agarra a uma nova
                ideia em meio à tempestade ao seu redor, segurando-se com toda a energia vital
                contra as ondas implacáveis do mar."

                $Argos.change("pose", "straight")
                show Argos:
                    ease 1.0 yalign 1.0

                argos "B—{w=0.2}bem, o que {i}você{/i} sabe?!{w}
                Vocês humanos gostam de todas as suas músicas estranhas,{w=0.2} todos aqueles instrumentos
                de sopro barulhentos e estridentes! Como se algum dia houvesse prazer em um carnyx!"

                argos "O que você sabe sobre música, sequer?
                Fico feliz que o companheiro Clément tenha mandado todo mundo embora,
                pelo menos o vale não ouviu nada daquilo por um tempo!"

                $Argos.change("pose", "crossed")

                "Ele cobre os olhos com a mão que segura a flauta e aponta na sua direção
                com a outra. Suas mãos tremem de tensão e ele recua."

                argos "Você...{w=0.2}você...{w=0.2} Eu mostrarei a você!{w=0.2}
                Farei uma música tão boa que você terá que admitir que suas músicas modernas são ruins!"

                argos "Você até admitirá que minha flauta e tambor são melhores que a lira do minotauro,
                {w=0.2} você verá!{w=0.2} Eu mostrarei a você!"

                "Chicoteando sua cauda para o lado, arremessando o tambor girando além para o vale,
                ele desliza para fora e atrás do pedestal da estátua na qual se apresentou.
                Quando fora de vista, ele solta um lamúrio."

                you "Se contenha.{w=0.2} Você só me chamou aqui fora para mostrar sua música?"

                #angry Argos
                "A cobra espreita o nariz por cima da estátua, ainda franzida."

                argos "Não!{w=0.2} A música era apenas para tornar especial antes de contá-lo o motivo
                pelo qual estou aqui hoje."

                you "Desembucha, então."

                #Argos grumbles


            "Foi ok.":

                you "Foi... bom.{w=0.2} Parabéns, Argos, tenho certeza de que você deve
                ter se esforçado muito."

                $Argos.change("emotion", "surprised")
                $Argos.change("pose", "straight")

                pause 2.0

                $Argos.change("emotion", "sad")

                show Argos:
                    ease 2.0 yalign 1.1

                argos "Master [player_name]...{w=0.5} Did my song truly bring you enjoyment?{w=0.2}
                Are you, perhaps, proud of this servant?"

                you "Sim.{w=0.2} Claro."

                pause 2

                show Argos:
                    ease 0.2 yalign 1.0
                    ease 0.2 yalign 1.05

                "Com a flauta ainda sendo segurada entre os dedos, ele a balança enquanto levanta
                a mão para enxugar o olho do que deve ser uma lágrima emocional.
                Sua outra mão servindo de escudo para o coração."

                you "Você está bem?"

                $Argos.change("pose", "crossed")
                argos "É-é apenas...{w=0.2}Mestre, por acaso você saberia qual é o seu propósito na vida?{w=0.2}
                Esta sabedoria é transmitida aos mortais?"

                you "Receio não ter recebido uma resposta para isso,{w=0.2} não."

                $Argos.change("pose", "straight")
                argos "Mas eu,{w=0.2} eu {i}realmente{/i} sei meu propósito.{w} Este conhecimento é esclarecido pelo
                mandato divino que me foi conferido."

                argos "Eu sirvo ao labirinto{w=0.3} e seu senhor."

                argos "Estou tão feliz... Os próprios deuses devem estar orgulhosos de mim hoje também.{w=0.2}
                Eles devem enxergar a alegria que eu trouxe ao meu Mestre!"

                argos "Não há nada mais honorável que o trabalho honesto.{w} E entre aqueles que trabalham duro,{w=0.2}
                nenhum se destaca mais daqueles que temem,{w=0.2} respeitam,{w=0.2} e obedecem à vontade dos Olímpios!"

                argos "Meus ancestrais...{w=0.2} Eles se enchem de contentamento, sabendo da honra que trouxe para nossa linhagem."

                show Argos:
                    ease 0.2 yalign 1.0
                    ease 0.2 yalign 1.05
                "Com lágrimas escorrendo pelo rosto e olhos fechados, ele leva a
                flauta à boca novamente."
                play sound "sfx/flute.ogg"
                "Ele continua a música.{w=0.2} É... é a mesma?{w=0.2} Porém, mais lenta, talvez."

                "Pequenos bufos e soluços cortam a melodia, fazendo-o exagerar no sopro
                e deixar notas singulares estridentes novamente, tão cheio de emoção que ele está."
                "Estes momentos ele parece antecipar, batendo no tambor {w=0.2}(ou sua cauda){w=0.2}
                mais uma vez com a pequena baqueta."

                you "Agora, Argos...{w=0.2} Por que você me chamou? Algum problema?"

                $Argos.change("emotion", "neutral")
                argos "Ah, s-{w=0.2}sim!{w=0.2} Há um motivo,{w=0.2} tal que um senhor culto
                como você apreciará!"

        show Argos:
            ease 0.4 xalign 0.53 zoom 0.7
            ease 0.4 xalign 0.47 zoom 0.8
            ease 0.4 xalign 0.53 zoom 0.9
            ease 0.4 xalign 0.5 zoom 1.0

        argos "Muito bem, vamos direto ao assunto.
        Tenho algo que pode despertar seu interesse."


    if ArgosContract == "Terrorized":
        $Argos.change("pelt","True")
        $Argos.change("emotion","cocky")
        $Argos.change("pose","straight")
        show Argos:
            xalign 0.5 yalign 1.0 zoom 0.6
        with Dissolve(1.0)

        argos "Meu senhor de olhos brilhantes,{w=0.2} mais uma vez é uma honra testemunhar seu encanto.{w}
        É um belo dia,{w=0.2} e sempre será,{w=0.2} quando seu semblante abençoa este vale."

        argos "Ah, ser presenteado com um propósito!{w=0.2} Para que serve um cão de guarda sem mestre para
        seguir e sem bezerro para vigiar?"

        argos "Posso apenas esperar que sua experiência até agora tenha sido tão enriquecedora quanto a minha."

        argos "Diga-me, o espelho lhe forneceu conforto? Seu primeiro
        lote de hóspedes chegou são e salvo?"

        show Argos:
            ease 0.4 xalign 0.53 zoom 0.7
        $Argos.change("pose","crossed")

        "A cobra se inclina para frente, ansiosa por cada palavra sua. Não estivesse ele enrolado em torno da estátua,
        cairia como um macarrão molhado, mas isto parece não lhe trazer desconforto algum."

        "Na verdade, quase parece como se ele quisesse descer e ficar cara a cara com você.
        Seu olhar entreaberto não se afasta de você,{w=0.2} acompanhado até mesmo as menores mudanças em sua postura."

        "Não é sempre que um foco tão intenso é disposto em alguém. Desconforto seria uma reação
        comum, ainda assim, seu olhar carece de um toque de predador."

        you "Estou indo bem, Argos.{w=0.2} O espelho tem sido muito útil — o hotel
        mudou completamente depois que acendemos o fogo."

        you "É incrível o que este domínio pode realizar.{w=0.2} Astério estava
        me mostrando algumas de suas capacidades,{w=0.2} e temos pessoas trabalhando em uma tecnologia agora."

        $Argos.change("emotion","neutral")

        argos "Entendo, entendo.{w=0.2} Muito bem, realmente é dever do prisioneiro informá-lo sobre
        o funcionamento do domínio.{w=0.2} Suas obrigações não devem ser negligenciadas."

        show Argos:
            ease 0.4 xalign 0.47 zoom 0.8
            ease 0.4 xalign 0.53 zoom 0.9
            ease 0.4 xalign 0.5 zoom 1.0

        "Argos se aproxima de você."

        argos "Meu senhor, hoje receio ter de lhe fazer alguns questionamentos impertinentes.
        Mas não deve ser um desafio para alguém como você."

        you "Muito bem. Não é sobre contratos, é?"

        $Argos.change("emotion","smug")

        argos "De forma alguma!{w=0.2} Eu meramente procuro entendê-lo melhor,{w=0.2} como um Mestre
        e como um...{w=0.2} humanp."

        argos "Diga-me,{w=0.2} após o nascimento, os humanos são presenteados com o conhecimento de seu propósito na vida?"

        you "Receio que não recebamos esta resposta de graça."

        you "Temos que lutar nossas vidas inteiras para resolver esse problema,{w=0.2}
        e é seguro assumir que um bom número de nós nunca vai resolvê-lo."

        you "Então, não.{w=0.2} Não sabemos para que estamos aqui, pelo menos não quando nascemos."

        you "Veja bem, uma criança humana leva anos para amadurecer.{w=0.2}
        Mesmo se um deus sussurrasse a verdade para eles,
        um bebê não seria capaz de entender uma única palavra."

        $Argos.change("emotion","cocky")

        argos "Entendo, entendo...{w=0.2} que estranho, devo dizer."

        argos "Isto sempre me intrigou, devo admitir.{w=0.2}
        Conheço as histórias dos heróis, é claro{w=0.2}
        — Teseu e seu pai Egeu, Odisseu e seu filho Telêmaco."

        argos "E é claro, Zeus e sua criação, Atena de olhos brilhantes!"

        $Argos.change("emotion","neutral")

        argos "Mas eu os conheço apenas através de histórias.{w=0.2} Nunca testemunhei uma família por conta própria,
        muito menos um bebê humano."

        you "Suponho que você mesmo não tenha parentes,{w=0.2} então."

        $Argos.change("emotion","smug")

        argos "Eu tenho antepassados,{w=0.2} centenas deles, na verdade — todas as cobras que me
        precederam, cumprindo nosso dever sagrado neste vale."

        $Argos.change("pose", "straight")

        argos "Mas uma família?{w=0.2} Uma esposa e filhos?{w=0.2} Receio que não."

        $Argos.change("pose", "crossed")

        argos "Mas para que serve isto?{w=0.2} Minha vida é repleta de significado e
        glória,{w=0.2} algo que poucos humanos poderiam compreender algum dia."

        $Argos.change("emotion","neutral")

        argos "Eu me pergunto, os humanos são meramente ignorantes,{w=0.2} ou suas vidas são desprovidas
        de inerente significado?{w=0.2} Quão vazio deve ser ficar todos os dias sem
        a orientação das estrelas."

        argos "Um propósito sempre corroeu meu peito, incessantemente.{w=0.2}
        Minha espécie nasce para um único objetivo, cumprir este mandato divino."

        $Argos.change("emotion","smug")

        argos "Para decretar punição sobre o híbrido que condenou sua linhagem.{w=0.2}
        Vingança sobre aquele que dilapidou o berço dos berços."

        argos "Um homem culto como você deve ter ouvido que a Grécia é o berço
        da civilização ocidental.{w=0.2} E Creta, meu senhor,
        é o útero que gerou aquela preciosa cultura ateniense."

        argos "Foi a covardia de Astério que a condenou,
        a causa da queda da ilha.{w=0.2} Apenas então, em meio a seus escombros apodrecidos,
        Atenas floresceu."

        $Argos.change("emotion","cocky")

        argos "Torturar o touro é nada menos que um rito de adoração divina."

        pause 1.0

        argos "O que meus antepassados pensariam de mim, se ao menos pudessem testemunhar
        meu desempenho?{w=0.2} Espero que eles me aplaudam do além no Estige."

        argos "De seus anceestrais, não espero nada menos.{w=0.2} Você enviou o híbrido para o
        meu vale,{w=0.2} que poder você possui!"

        $Argos.change("emotion","neutral")

        argos "Meu senhor, se puder responder a um último questionamento impertinente...{w}
        Por que você enviou Astério para o vale?{w=0.5}
        Que ideia inspirou sua mão a,{w=0.2} com razão,{w=0.2} reiniciar suas provações?"

        menu:
            "Não tive a intenção de machucá-lo. Fui ingênuo.":
                you "Eu não queria causar nenhum mal...
                Achei que você fosse só conversar com ele."
                $Argos.change("emotion","cocky")
                argos "Entendo, entendo... Ah,{w=0.2} meu bom senhor, mesmo?
                {w=0.2} Você confia demais."
                argos "Não deixei meu objetivo claro?
                Ou talvez minhas palavras o fizeram cometer um deslize,{w=0.2} sim?"
                you "Você disse que não iria machucá-lo...{w} Eu acreditei na sua palavra."
                argos "E eu não o machuquei. Nem um único dedo o tocou{w=0.2}
                — minhas presas também não roçaram seu pescoço."
                argos "Apenas um pouquinho de angústia, no entanto...
                Ah, não é delicioso quando ele entra em pânico?"

            "Achei que não tinha outra escolha.":
                you "Achei que não tinha outro jeito de conseguir o espelho."
                $Argos.change("emotion","smug")
                argos "Mesmo?{w=0.2} Então que isso sirva de lição{w=0.2}
                — sempre há outra maneira."
                $Argos.change("emotion","sad")
                argos "Ah...{w=0.2} e aqui pensei que você tinha o poder de Héracles dentro de você!
                Que decepção..."
                $Argos.change("emotion","cocky")
                argos "Bem, devo dizer que não é nenhuma surpresa. É apenas como os humanos são hoje em dia."

            "É o que os deuses queriam.":
                you "É o que os deuses querem,{w=0.2} correto?"
                you "Não é este o mesmo motivo de você estar aqui, Argos?
                Temos um dever a cumprir."
                you "Você deixou bem claro."
                $Argos.change("emotion","surprised")
                pause 1.0
                #Argos is speechless for a moment
                #almost breaks character, but gets back on his groove
                $Argos.change("emotion","neutral")
                argos "Ah, um devoto, de fato."
                $Argos.change("emotion","smug")
                argos "Ahh...{w=0.5} que diversão teremos..."
                argos "Sim...{w=0.5} certamente..."
                $Build3Ending = 'bad'
                $abuse_act1 +=1

            "Era a maneira de melhor custo-benefício de se obter o espelho.":
                you "Foi uma situação muito simples, sério.
                Mandar ele para fora era a opção de melhor custo-benefício."
                you "Eu fui pragmático."
                #Argos remains in-character, but looks sternly at the player for a second
                $Argos.change("emotion","angry")
                pause 1.0
                $Argos.change("emotion","smug")
                argos "Entendo, nós temos um intelectual como mestre. Um homem racional."
                $Build3Ending = 'bad'
                $abuse_act1 +=1

            "Eu sou um sádico.":
                you "O que você acha, Argos?{w=0.2} Eu sou o que alguns podem chamar de sádico."
                you "Senti prazer em enviar Astério para fora, é simples assim.{w=0.2}
                Na verdade, acho que você e eu teremos um futuro muito frutífero pela frente."
                you "Conhecer você tem sido bastante incrível.{w=0.2}
                Estou feliz por ter conseguido a escritura do hotel, que oportunidade."
                $Argos.change("emotion","angry")
                you "Estou fazendo o que os deuses querem e gostando."
                show Argos:
                    ease 0.5 xalign 0.55
                pause 1.0
                show Argos:
                    ease 0.5 xalign 0.5
                $Argos.change("emotion","smug")
                argos "Oh meu..."
                argos "Chegou o dia em que temos um mestre digno e apropriado entre nós, finalmente."
                $Argos.change("emotion","cocky")
                argos "Ah, devo admitir que esperava um senhor fraco, como os que vieram antes de você."
                argos "Que mudança inesperada dos acontecimentos."
                $Build3Ending = 'bad'
                $abuse_act1 +=2

        $Argos.change("emotion","neutral")
        $Argos.change("pose","crossed")
        argos "Dito isso... admito que devo refletir um pouco sobre sua resposta."

        argos "Devo manter isso em mente em nossas futuras negociações.
        Agora, não entenda errado, há outro assunto que devo discutir com você."

    if ArgosContract == "Speedrun":
        "E ainda assim... o canto da cobra engasga aqui e ali.
        Não parece haver nenhuma razão para isto — ele apenas para no meio da nota."

        $Argos.change("pelt","True")
        $Argos.change("emotion","surprised")
        $Argos.change("pose","straight")
        show Argos:
            xalign 0.5 yalign 1.0 zoom 0.6

        "Argos está no topo da estátua como da última vez, meio protegido por ela.
        Seus olhos já perfuram você."

        "Novamente sua música engasga no meio, mas nunca retorna.
        Ele guarda a flauta e permanece olhando para você."

        "Sua falta de comunicação se estende por mais de um minuto.
        Você tenta pensar em algo para dizer, mas está timido e confuso."

        "Você é tão pequeno comparado a esta imensa criatura.
        Os joelhos da dama são maiores que toda sua cabeça."

        "Quão inadequado você é comparado à gigante dama, em todos os sentidos.
        Toda a ansiedade causada por isto faz você suar — em um piscar de olhos, sua camisa está molhada em torno de suas axilas."

        "O suor chega a escorrer até suas calças."
        show Argos:
            ease 0.4 xalign 0.55 yalign 1.1

        "Enquanto isso, a cobra observa cada movimento seu. Quando você olha para sua camisa
        cada vez mais molhada, ele recua e se esconde atrás da estátua."

        show Argos:
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1

        "Você dá um passo à frente, quase tropeçando em uma pedra, e a cobra solta um gritinho."

        argos "Não dê mais um passo!"

        argos "Seja lá o que você for,{w=0.2} o que quer que esteja pensando em fazer,{w=0.2}
        não cairei em seus truques."

        you "Desculpe, eu não entendo o que você está —"

        argos "Eu sou mais esperto do que isso!{w=0.5} Você não é normal!{w}
        Deve ter havido algum tipo de engano, como o destino permitiu que algo
        como você herdasse o hotel?"

        $Argos.change("emotion","angry")
        argos "Você está tentando fazer alguma coisa, eu simplesmente sei disto."

        argos "Bem, eu não entrarei no jogo! Tenho um dever a cumprir,
        e pelos deuses o farei, mas não baixarei a guarda!
        Nem mesmo tente algum de seus truques."

        "Você fixa seu olhar na cobra, tentando transmitir sua fraqueza para ele.
        Talvez ele veja a criatura miserável que você é, veja que não há necessidade de ter medo."

        $Argos.change("emotion","sad")
        show Argos:
            ease 0.08 xalign 0.553
            ease 0.08 xalign 0.55
            repeat

        "Quanto mais você olha, no entanto, maior se torna o pânico dele.
        Ele atinge o auge quando você finalmente rompe a gagueira e consegue dizer algo."

        you "Ok."

        $Argos.change("emotion","surprised")
        show Argos:
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1

        "Ele recua em aversão."

        $Argos.change("emotion","angry")
        argos "Retire sua máscara, demônio, e revele sua verdadeira forma!
        Você não é humano, disto eu tenho certeza."

        you "Eu sou só um speedrunner."

        pause 2.0

        show Argos:
            ease 0.5 xalign 0.5 yalign 1.0

        $Argos.change("emotion","surprised")
        argos "O-o que é um speedrunner?"

        you "Sou um especialista em vencer jogos rapidamente, destruindo eles,
        explorando cada falha que existe.{w=0.2} Milhares me assistem maravilhados com as minhas proezas."

        pause 2.0

        $Argos.change("emotion","sad")

        argos "Zeus Olympios, Atena de Olhos Brilhantes, por que, oh, por que permitiu que esta
        criatura entrasse no domínio?{w=0.2} Ele trará o fim para todos nós?"

        you "Eu não entendo sobre o que você está falando."

        hide Argos
        with Dissolve (1.0)
        "A cobra se esconde atrás da estátua e fica em silêncio por uns bons dez minutos.
        Às vezes você ouve soluços,{w=0.2} ou maldições lançadas aos céus."

        "A noção de alguém se escondendo atrás de um objeto ilude você.{w=0.2}
        Ele sequer ainda está lá?{w=0.2} Se você fechasse os olhos, ele deixaria de existir?"

        "Você pensa sobre suas mãos.{w=0.2} Seus dedos param de existir quando você
        não está olhando para eles?{w=0.2} Mas você ainda pode segurar as coisas,
        mesmo se não estiver olhando para eles."

        "Houve uma vez em que você fez um speedrun vendado.{w}
        O jogo continuou a existir mesmo quando você não conseguia vê-lo."

        "Demora um pouco, mas você chega à conclusão de que Argos ainda deve existir,
        mesmo que você não consiga vê-lo atrás da estátua."

        $Argos.change("emotion", "angry")
        $Argos.change("pose","straight")
        show Argos:
            xalign 0.5 yalign 1.0 zoom 0.6
        with Dissolve(1.0)

        "Quando ele reaparece, todo o medo parece ter sumido de seu rosto."
        show Argos:
            ease 0.4 xalign 0.53 zoom 0.7
            ease 0.4 xalign 0.47 zoom 0.8
            ease 0.4 xalign 0.53 zoom 0.9
            ease 0.4 xalign 0.5 zoom 1.0 yalign 1.1

        argos "Escute aqui, eu irei pará-lo — não sei qual é o seu plano,
        mas vou destruí-lo!"

        argos "A ordem natural já foi subvertida,{w=0.2}
        e se isto significa salvar tudo o que é sagrado, farei tudo o que for necessário."

        show Argos:
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1

        argos "E você vai me obedecer,{w=0.2} ou vai se arrepender!"

        #he tells what the player has to do now

        $Argos.change("pose","straight")
        argos "Você tem um dever, sua abominação profana. Escolha um de seus lacaios e vá para o leste."

        show Argos:
            ease 0.5 yalign 1.0
        argos "Você sabe o que é \"leste\"? Fica {i}naquela{/i} direção, apenas siga o sol."

        argos "Depois de algumas horas de caminhada, você encontrará um conjunto de estufas."

        argos "Talvez seu cérebro esponjoso não saiba o que esta palavra signifique.
        É um conjunto de grandes fornalhas onde as pessoas costumavam cozinhar recipientes de argila."

        argos "Vá até lá, pegue o pacote que lá deixei e vá para o oeste — fica {i}naquela{/i} direção
        — para sacrificá-lo em uma colina onde há estátuas para os deuses."

        argos "Isto significa queimar a coisa! Faça isso e me encontre aqui ou
        não haverá garrafa para você! Está claro?"

        "Você concorda com a cabeça. Caminhe em direção ao sol, pegue o pacote dos potes de argila, depois vá para uma colina e queime o pacote.
        Você entende o que deve fazer agora."

        jump chapter11PostInterrogation

    $Argos.change("emotion","smug")
    $Argos.change("pose","crossed")

    argos "É uma questão bastante simples; Eu encontrei uma {color=[UIColorOrange]}garrafa de vinho{/color},
    {w=0.2}daquele tipo especial que cura o minotauro."

    argos "É uma coisa bastante rara hoje em dia, uma vez que não pode ser criada intencionalmente
    pelos mestres...{w=0.2} Tem uma tendência a aparecer principalmente,{w=0.2} mas não exclusivamente,
    {w=0.2}aqui no vale."

    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")

    argos "É claro, estou proibido de beber e, de qualquer maneira, é inútil para mim.
    {w=0.2}Portanto, estou disposto a fornecê-lo, se certas condições forem atendidas."

    argos "O que me diz, Mestre?{w=0.2} Você está disposto a negociar com este humilde servo?"

    #some internal monologue
    pause 2.0

    $Argos.change("emotion","neutral")
    $Argos.change("pose","crossed")

    you "Sim, {w=0.2}mas quero saber exatamente quais são seus termos antes de me envolver."

    $Argos.change("emotion","smug")

    argos "É claro!{w=0.2} Na verdade, quero que você ouça muito atentamente minhas condições {w=0.2}
    — elas são muito específicas...{w=0.2} tenho pensado nelas há tanto tempo..."

    you "Quando você coloca dessa forma, é quase como se tivesse algum tipo de pegadinha.
    {w=0.2}Uma cobra tão honrada como você não faria isso, faria?"

    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")

    argos "Eu?{w=0.5} Enganar o mestre?{w=0.5} Jamais!"

    argos "Veja bem... é meu dever garantir que você se torne um Mestre correto e apropriado.
    {w=0.2}E isto inclui ensinar a você a importância dos contratos — tanto os escritos como os verbais!"

    $Argos.change("pose","crossed")
    argos "Vamos descartar toda a pretensão, sim? Permita-se ser enganado e eu {i}irei{/i}
    aproveitar a oportunidade."

    argos "Mas saiba que é para o seu próprio bem, Mestre. Será uma excelente oportunidade
    de aprendizado de qualquer maneira!"

    $Argos.change("emotion","neutral")
    argos "Agora, devo recitar minhas condições."

    you "Ótimo. Vá em frente, vamos acabar logo com isso."

    pause 1.0

    #argos first lists his conditions

    argos "Ontem à noite, após terminar minhas orações e rituais, encontrei uma garrafa de vinho."

    $Argos.change("emotion","smug")

    argos "Agora, pensei em dá-la a você — afinal, você {i}é{/i} o senhor
    — mas por que não tomar isto como um momento divertido de união?
    Eu o darei a você, se você fizer uma coisa específica para mim."

    $Argos.change("pose","straight")
    argos "Quero que você prove sua devoção sincera ao divino. Afinal,
    o Mestre do domínio deve servi-los e cumprir sua vontade, não é?"

    $Argos.change("emotion","neutral")
    $Argos.change("pose","crossed")

    argos "Nos tempos antigos, uma hecatombe seria promulgada — cem touros seriam
    sacrificados aos deuses. Mas os humanos de hoje raramente gostam de sujar as mãos."

    argos "Aqui está o que deve ser feito: mais para o leste você encontrará um leito de rio seco
    ao lado de um antigo conjunto de fornalhas quebradas."

    $Argos.change("emotion","smug")

    argos "Lá você encontrará um sacrifício adequado. Deve haver um pacote com um
    caroço endurecido — não muito diferente de carvão — dentro da mais deteriorada de todas as fornalhas."

    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")

    argos "Você deve pegar a oferenda e queimá-la, dedicando-a ao divino."

    $Argos.change("emotion","neutral")

    argos "Ao sul do hotel, o vale segue mais adiante, até chegar a um planalto.
    Há um caminho até o topo, onde você encontrará santuários para algumas divindades."

    $Argos.change("emotion","smug")
    argos "Santuários antigos e majestosos para os deuses, criados pelas próprias divindades
    quando este domínio nasceu. Escolha qualquer um dos santuários divinos e queime a oferenda."

    $Argos.change("emotion","cocky")
    $Argos.change("pose","crossed")
    pause 2.0

    you "Espere..."

    $Argos.change("emotion","smug")
    you "Então, você só vai me dar essa garrafa se eu me aventurar no vale e buscar essa coisa?
    Em primeiro lugar, como posso ter certeza de que não é uma garrafa falsa?"

    $Argos.change("emotion","neutral")
    you "Como posso saber que você não está me dando direções falsas? É absolutamente necessário
    para mim provar a devoção aos Deuses desse jeito?"

    $Argos.change("emotion","angry")
    you "Não posso só ordenar você a me dar a garrafa já que, como você diz, é meu servo?
    Como vou saber a aparência da oferenda? Isso é muita coisa para descarregar{nw}"

    $Argos.change("pose","straight")
    show Argos:
        ease 0.4 xalign 0.45
        ease 0.6 xalign 0.5

    argos "Bah! Em nome dos Deuses, por que tantas perguntas, Mestre?"

    $Argos.change("pose","crossed")

    argos "Eu estou lhe fazendo uma oferta gentil — admito, esperando {i}algum{/i} esforço de
    sua parte — e é assim que você me retribui?{w=0.2} Me enchendo de perguntas?"

    pause 2.0
    $Argos.change("emotion","neutral")
    pause 1.0

    argos "Muito bem, vamos... fazer disto um jogo, vamos?"

    you "Já tive o suficiente dos seus jogos, Argos."

    $Argos.change("emotion","cocky")

    argos "Você prefere que eu não responda nenhuma de suas perguntas, Mestre?"

    you "Tudo bem. O que você quer?"

    $Argos.change("emotion","neutral")

    argos "Repetirei tudo que acabei de dizer.{w} Você pode me interromper a qualquer momento
    para perguntar o que quiser,{w=0.3} {i}mas{/i},{w=0.5} permitirei apenas que você faça isto
    três vezes."

    you "Três vezes?"

    argos "Sim. Nove termos, três interrupções. Eu diria que é justo."
    $PressTries = 3
    menu:
        "{color=[UIColorLeader]}(LÍDER)O mínimo que posso aceitar são cinco.{/color}" if player_background == "leader":
            you "Três está longe de ser o suficiente e você sabe disso.
            Você tem todas as cartas, não é um jogo divertido se for unilateral.
            O mínimo que posso aceitar são cinco."

            $Argos.change("emotion","smug")
            argos "Eu posso, novamente, apenas deixar as coisas como estão, não posso?"

            pause 1.0

            you "Mas onde fica a diversão?"
            $Argos.change("emotion","surprised")
            $Argos.change("pose","straight")
            pause 1.0
            $Argos.change("pose","crossed")
            $Argos.change("emotion","cocky")
            argos "Isto... sim, suponho que esteja certo.
            Tudo bem, permitirei cinco interrupções."
            $PressTries = 5

        "Três parece bom para mim.":
            "Você decide ficar feliz com o que recebe e não pressiona Argos por mais."

            you "Tudo bem."

            $Argos.change("emotion","cocky")
            argos "Esplêndido!"

    $Argos.change("emotion","neutral")
    argos "Repetirei meus termos, então."

    pause 1.0

    $PressLabel = 'argosPress1'
    $PressQuestions = ['n','n','n','n','n','n','n','n','n']
    $showCEButton = False
    show screen CEPressScreen("argosPressFail", "Questionar frase!")

label argosState1:
    $showCEButton = True
    $PressQuestions[0]='c'
    $Argos.change("emotion","neutral")
    $Argos.change("pose","crossed")
    argos "{i}Ontem à noite, após terminar minhas orações e rituais, encontrei uma garrafa de vinho."
    $PressQuestions[0]='y'
label argosState2:
    $showCEButton = True
    $PressQuestions[1]='c'
    $PressLabel = 'argosPress2'
    $Argos.change("emotion","smug")
    $Argos.change("pose","crossed")
    argos "{i}Agora, pensei em dar a você — afinal, você {i}é{/i} o senhor
    — mas por que não aproveitar isto como um momento divertido de união?
    Darei a você, se você fizer algo específico para mim."
    $PressQuestions[1]='y'
label argosState3:
    $showCEButton = True
    $PressQuestions[2]='c'
    $PressLabel = 'argosPress3'
    $Argos.change("emotion","smug")
    $Argos.change("pose","straight")
    argos "{i}Quero que você prove sua devoção sincera ao divino. Afinal,
    o Mestre do domínio deve servi-los e cumprir sua vontade, não é?"
    $PressQuestions[2]='y'
label argosState4:
    $showCEButton = True
    $PressQuestions[3]='c'
    $PressLabel = 'argosPress4'
    $Argos.change("emotion","neutral")
    $Argos.change("pose","crossed")
    argos "{i}Nos tempos antigos, uma hecatombe seria promulgada — cem touros seriam
    sacrificados aos deuses. Mas os humanos de hoje raramente gostam de sujar as mãos."
    $PressQuestions[3]='y'
label argosState5:
    $showCEButton = True
    $PressQuestions[4]='c'
    $PressLabel = 'argosPress5'
    $Argos.change("emotion","neutral")
    $Argos.change("pose","crossed")
    argos "{i}Aqui está o que deve ser feito: mais a leste, você encontrará um leito de rio seco
    ao lado de um antigo conjunto de fornalhas quebradas."
    $PressQuestions[4]='y'
label argosState6:
    $showCEButton = True
    $PressQuestions[5]='c'
    $PressLabel = 'argosPress6'
    $Argos.change("emotion","smug")
    $Argos.change("pose","crossed")
    argos "{i}Lá você encontrará um sacrifício apropriado. Deve haver um pacote com
    um caroço endurecido — não muito diferente de carvão — dentro da mais deteriorada de todas as fornalhas."
    $PressQuestions[5]='y'
label argosState7:
    $showCEButton = True
    $PressQuestions[6]='c'
    $PressLabel = 'argosPress7'
    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")
    argos "{i}Você deve pegar a oferenda e queimá-la, dedicando-a ao divino."
    $PressQuestions[6]='y'
label argosState8:
    $showCEButton = True
    $PressQuestions[7]='c'
    $PressLabel = 'argosPress8'
    $Argos.change("emotion","neutral")
    $Argos.change("pose","straight")
    argos "{i}Ao sul do hotel, o vale segue adiante até chegar a um planalto.
    Há um caminho até o topo, onde você encontrará santuários para algumas divindades."
    $PressQuestions[7]='y'
label argosState9:
    $showCEButton = True
    $PressQuestions[8]='c'
    $PressLabel = 'argosPress9'
    $Argos.change("emotion","smug")
    $Argos.change("pose","straight")
    argos "{i}Santuários antigos e majestosos para os deuses, criados pelas próprias divindades
    quando este domínio nasceu. Escolha qualquer um dos santuários divinos e queime a oferenda."
    $PressQuestions[8]='y'
    jump argosPressEnd


label argosPress1:
    $showCEButton = False
    $PressTries-=1
    you "É o vinho curativo? Ou é do tipo normal?"
    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")
    argos "Ora, claro que é aquele vinho curativo especial que o touro tanto gosta.
    Uma garrafa cheia, selada e intacta."
    argos "Há vinho o suficiente para curá-lo por completo, eu diria."
    $PressQuestions[0]='q'
    pause 1.0
    jump argosState2

label argosPress2:
    $showCEButton = False
    $PressTries-=1
    you "Não posso simplesmente ordenar que você me dê? Você também não é meu servo?"
    $Argos.change("emotion","cocky")
    $Argos.change("pose","crossed")
    argos "Ãhn? O Mestre está agora ansioso para impor sua vontade a este humilde servo?
    Ah, como eu desejava que este dia chegasse, ser usado e receber ordens!"
    $Argos.change("emotion","smug")
    $Argos.change("pose","crossed")
    argos "Infelizmente, não sou servo como o bezerro. Eu sirvo a uma missão dada pelos Deuses
    acima de tudo, e obedeço ao Mestre na medida em que sua vontade esteja de acordo com essa missão."
    argos "E eu também tenho meu próprio arbítrio, meu senhor. {w=0.2} Basta dizer,
    não sou estritamente obrigado a obedecê-lo."
    argos "Se é minha conformidade que você busca,{w=0.2} então deve se comprometer comigo."
    $PressQuestions[1]='q'
    pause 1.0
    jump argosState3

label argosPress3:
    $showCEButton = False
    $PressTries-=1
    you "Não posso provar minha devoção de outra forma?"
    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")
    argos "Eu receberia sua fé em todas as formas, mas se é o vinho que você
    busca, então eu cooperarei apenas se você cumprir este ritual."
    argos "Eu detestaria vê-lo fazendo uma oferta inadequada, como aquelas nas
    religiões modernas! Desgraçados ímpios, todos eles."
    $PressQuestions[2]='q'
    pause 1.0
    jump argosState4

label argosPress4:
    $showCEButton = False
    $PressTries-=1
    you "Espere...{w=0.2} O que você quer dizer com isso?{w=0.2} O que é isso sobre cem touros?"
    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")
    argos "Você não sabia? Os gregos antigos eram muito devotos.{w=0.2}
    Após o saque de Troia, cem touros foram sacrificados."
    argos "Veja bem, Odisseu, o trapaceiro, optou por renunciar a tais rituais e,
    por sua arrogância, a punição chegou rapidamente."
    argos "Ser coroado como Mestre do domínio é um grande privilégio, entende?
    Uma hecatombe seria adequada."
    $Argos.change("emotion","smug")
    $Argos.change("pose","crossed")
    argos "Mas, novamente... sacrificar a mesma vaca cem vezes, seria uma tarefa tão árdua!"
    argos "Então, meu querido senhor... quero dizer o que digo, e digo o que quero dizer.
    Quando digo hecatombe, quero dizer uma hecatombe."
    $PressQuestions[3]='q'
    pause 1.0
    jump argosState5

label argosPress5:
    $showCEButton = False
    $PressTries-=1
    you "\"Mais para o leste?\"{w=0.2} Isso soa muito vago."
    argos "Não se preocupe, meu senhor.{w=0.2} No devido momento, direi a você exatamente como chegar lá!"
    argos "Desejo verificar sua dedicação aos Olímpios acima de tudo.{w=0.2}
    Não tenho interesse em vê-lo se perder, pois isto apenas prejudicaria meu objetivo."
    argos "Não se preocupe com tais detalhes."
    $PressQuestions[4]='q'
    pause 1.0
    jump argosState6

label argosPress6:
    $showCEButton = False
    $PressTries-=1
    you "Como sei que isso vai estar lá?"
    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")
    argos "Você pode confiar em mim! Eu mesmo o deixei lá para você encontrar, meu bom senhor.
    Deve ser fácil de encontrar, está lá, dentro da fornalha quebrada."
    $Argos.change("emotion","neutral")
    argos "Era usada para cozinhar potes de argila há muito tempo. Mas é inútil agora.
    Apenas abra e o sacrifício estará bem ali."
    argos "Devo adicionar... há mais algumas outras bugigangas atrás das fornalhas também,
    caso queira verificar."
    you "Isso soa desnecessariamente complicado.{w=0.2} Por que você simplesmente não deu a oferenda para mim,
    por que eu tenho que ir até lá para encontrar?"
    $Argos.change("emotion","cocky")
    argos "Para testar sua fé, é claro!{w=0.2} Um sacrifício só vale o esforço necessário
    para realizá-lo.{w=0.2} Se eu simplesmente o desse para você, não seria sacrifício algum."
    $KnowAboutKiln = True
    $PressQuestions[5]='q'
    pause 1.0
    jump argosState7

label argosPress7:
    $showCEButton = False
    $PressTries-=1
    you "Não existe outro jeito de sacrificar?"
    argos "Absolutamente não!{w=0.3} Desde os tempos antigos, é assim que a carne foi
    dedicada aos deuses."
    $PressQuestions[6]='q'
    pause 1.0
    jump argosState8

label argosPress8:
    $showCEButton = False
    $PressTries-=1
    you "\"Para o sul\"? Isso soa muito vago."
    $Argos.change("emotion","smug")
    $Argos.change("pose","straight")
    argos "Não se preocupe, meu senhor.{w=0.2} No devido momento, direi a você exatamente como chegar lá!"
    argos "Desejo verificar sua dedicação aos Olímpios acima de tudo.{w=0.2}
    Não tenho interesse em vê-lo se perder, pois isto apenas prejudicaria meu objetivo."
    argos "Não se preocupe com tais detalhes, Mestre."
    $PressQuestions[7]='q'
    pause 1.0
    jump argosState9

label argosPress9:
    $showCEButton = False
    $PressTries-=1
    you "\"Um dos santuários divinos\"... você está insinuando que um deles não é feito por eles?"
    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")
    argos "Talvez. Oh meu, você é perspicaz, não é?"
    argos "Um dos santuários — o menor e, de longe, o mais tímido — é dedicado a alguma
    divindade esquecida que remonta a sabe-se lá quando."
    argos "Uma coisa tão diminuta. É apenas um monte de pedras, uma pilha de rochas, com um pedaço de tecido
    amarrado em volta. Suponho que seja alguma forma antiga de adoração."
    $Argos.change("emotion","angry")
    $Argos.change("pose","crossed")
    argos "Seja o que for, garanto que não é uma homenagem aos Olímpios,{w=0.5}
    e apenas isto já deveria ser razão para evitá-lo."
    argos "Pior de tudo, temo que tenha sido erguido pelo próprio touro.
    Não possui legitimidade."
    argos "Ignore-o.{w=0.2} Não tenho o dever de lhe dar a garrafa
    caso você ofereça o sacrifício a ele."
    $Argos.change("emotion","cocky")
    $Argos.change("pose","straight")
    argos "Dito isto...{w=0.3}qualquer um dos santuários divinos vai servir!{w=0.2}
    E eu falo sério."
    $KnowAboutShrine = True
    $PressQuestions[8]='q'
    pause 1.0
    jump argosPressEnd

label argosPressFail:
    $showCEButton = False
    $Argos.change("emotion", "smug")
    argos "Ora, ora, Mestre! Você esgotou todas as suas perguntas!"
    $Argos.change("emotion", "neutral")

label argosPressEnd:
    $showCEButton = False
    python:
        for i, j in enumerate(PressQuestions):
            if j in ['n', 'c']:
                PressQuestions[i] = 'y'
    $Argos.change("emotion", "smug")
    $Argos.change("pose","crossed")
    if PressTries != 0:
        argos "Qual é o problema, Mestre? Sem perguntas, de repente?\nTudo bem,
        devo guardar meus segredos, então."
    else:
        argos "Espero que esteja satisfeito com suas perguntas, Mestre."
    hide screen CEPressScreen
    pause 1.0
    you "Então, essa é a tarefa em mãos. Fazer um sacrifício e provar minha devoção aos deuses?
    E então você vai me dar a garrafa?"
    $Argos.change("emotion", "cocky")
    argos "Não cumpri minha palavra até então, Mestre?"

    if PressQuestions[5] != 'q':
        if ArgosContract == "Terrorized":
            $Argos.change("pose","straight")
            argos "Tornarei a proposta ainda mais atraente para você, já que você foi devoto o suficiente para
            mandar o bezerro para fora — deixei um tesouro atrás da fornalha."
            $KnowAboutKiln = True
        elif ArgosContract == "Tricked" or (ArgosContract == "Contested" and contestContract == '4'):
            $Argos.change("pose","straight")
            argos "Tornarei a proposta ainda mais atraente para você, como um sinal de boa vontade —
            deixei um tesouro atrás da fornalha."
            $KnowAboutKiln = True

label chapter11PostInterrogation:
    $Argos.change("emotion", "neutral")
    $Argos.change("pose","crossed")
    you "...Vou pensar sobre isso. Talvez eu devesse perguntar ao Astério, ficar ciente
    do que posso encontrar aqui."

    $Argos.change("emotion", "angry")
    argos "Você precisa mesmo envolver o prisioneiro em todos os seus assuntos? Muito bem, então,
    volte para a criatura. No entanto..."

    $Argos.change("emotion", "smug")
    argos "Ao subir as escadas para seu 'hotel'... certifique-se de subir dois degraus
    de cada vez."

    argos "Afinal, não sei por mais quanto tempo poderei segurar esta garrafa
    sem deixá-la escorregar e quebrar. Posso ser tão desastrado às vezes…"

    you "Como é?"

    $Argos.change("emotion", "cocky")
    argos "Sim, eu realmente acho que seja algo que pode acontecer,{w=0.4} se sua devoção aos
    deuses não for comprovada em...{w=0.5} digamos, dois dias?{w} Isto funciona para você?"

    you "Espera, dois dias? Você não pode estar falando sério. Isso não fazia parte do acordo!"

    $Argos.change("emotion", "angry")
    $Argos.change("pose","straight")
    argos "Ah, então você acha que devoção é algo que se pode procrastinar, não é?{w=0.2}
    Bem, isto é simplesmente maravilhoso.{w=0.2} Que Mestre você é!"

    $Argos.change("pose","crossed")
    argos "Sabe, estou começando a ter dúvidas sobre esta garrafa.{w=0.2}
    Talvez você não seja realmente digno, afinal.{w=0.2} Que coisa, estou terrivelmente sedento esta manhã!"

    you "Ótimo!{w=0.3} Dois dias, então,{w=0.2} contanto que você não invente mais
    regras idiotas.{w} Temos um acordo?"

    $Argos.change("emotion", "cocky")
    show Argos:
        ease 0.4 zoom 1.05 xalign 0.53 yalign 1.05
        ease 0.4 zoom 1.1 xalign 0.47 yalign 1.1
        ease 0.4 zoom 1.15 xalign 0.5 yalign 1.15

    $Argos.change("pose","straight")
    "A cobra se aproxima de você.{w=0.2} Você recua por um segundo, mas quando olha para trás,
    vê a mão dele estendida em sua direção. Argos exibe o sorriso mais largo que ele
    deu a você até agora."

    argos "Parece bom para mim, Mestre."

    menu:
        "Apertar a mão dele.":
            "Você está sem opções, e qualquer beco sem saída que ele possa fazer você saltar dentro
            vale a recompensa."

    "Você aperta a mão de Argos, mas deixa claro sua aversão ao arrancar sua mão para
    fora do aperto dele quando acaba. A serpente ri de você."

    show Argos:
        ease 1.0 zoom 1.05 yalign 1.05
    argos "Então, não há tempo a perder!{w=0.2} Vá em frente!"

    stop music fadeout 1.0
    scene bg valley_exit
    with Dissolve(1.0)

    "Você se vira e começa a caminhar de volta para a caverna.{w=0.2}
    Não é assim que você esperava que sua manhã começasse."

    "Conforme você avança, as palavras de Argos ecoam em sua cabeça, e todo o peso da
    tarefa em mãos começa a cair a ficha em você.{w=0.2} Ao se lembrar de sua última frase,
    você percebe que seus pés estão acelerando o ritmo."

    scene bg staircase
    with Dissolve(1.0)

    "No momento em que você chega à escada, está em alta velocidade.
    Você xinga a cobra mentalmente enquanto, de fato, sobe dois degraus de cada vez; assim como ele disse que você faria."

    "As coisas começaram mal. Você ainda nem começou sua tarefa e
    já está caindo em um dos becos sem saída de Argos."

    scene bg oldquarters
    $Asterion.change("emotion", "sad")
    $Asterion.change("leftarm", "loose")
    $Asterion.change("rightarm", "loose")
    show Asterion:
        xalign 0.5 yalign 1.2 zoom 0.9
    with Dissolve(1.0)
    play music "music/GreekFolkSong.ogg" fadeout 1.0 fadein 1.0

    "Você chega aos aposentos do mestre, onde Astério já está vestido e esperando
    por você com uma expressão sombria. Ele está mordendo o lábio, se segurando para não
    fazer perguntas enquanto você recupera o fôlego."

    you "Bom dia, Astério."

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("leftarm", "raised")

    show Asterion:
        ease 1.0 yalign 1.0 zoom 1.0

    asterion "Bom dia, Mestre."

    $Asterion.change("emotion", "sad")

    asterion "Como foi?"

    you "Bem... eu tenho boas notícias, e más notícias."

    "Você atualiza Astério sobre tudo o que Argos disse para você{w=0.4}
    — o contrato, a garrafa, sua tarefa e o limite de dois dias."

    "Você esperava que ele se animasse ao ouvir sobre a garrafa de vinho,
    mas parece que ele conteve a empolgação; como se estivesse esperando
    o embargo inevitável."

    you "Então, sim, nós temos dois dias para ir buscar a garrafa.
    Decidi vir perguntar a você que tipo de coisa eu precisaria enfrentar em vez de ir para o
    labirinto logo de uma vez."

    if ArgosContract == "Terrorized":
        show Asterion:
            ease 0.05 xalign 0.503
            ease 0.05 xalign 0.5
            repeat
        pause 1.0

        asterion "Eu-{w=0.2}Não será necessário, Mestre.{w=0.4} Não preciso do vinho."

        asterion "Posso me curar por conta própria sem problemas, vai apenas demorar um pouco mais.{w}
        A{w=0.2}-além disso, temos outras prioridades."

        $Asterion.change ("leftarm", "loose")
        asterion "Fizemos progresso no projeto da internet ontem,
        certamente isso vai apenas nos distrair."

    else:
        pause 1.0
        $Asterion.change ("emotion", "contemplative")
        $Asterion.change ("leftarm", "loose")

        "Astério pondera sobre a situação por um momento, antes que sua expressão se transforme em um sorriso
        — tenso, com muita bagagem por trás, mas ainda assim, um sorriso."

        asterion "Agradeço sua preocupação, Mestre, mas não acho que a garrafa
        valha a pena o esforço. O labirinto abriga muitos perigos dos quais eu
        prefiro que você seja poupado."

        asterion "Posso me curar por conta própria sem problemas, vai apenas demorar um pouco mais."

        you "Não, é sério.{w=0.2} Se eu puder ajudar você a voltar ao normal,
        farei tudo o que puder."

        $Asterion.change ("emotion", "sad")

        asterion "Há também a questão do projeto da internet...{w=0.2}
        Acredito que isso vai nos distrair de concluí-lo."

        asterion "Temo que, se não forcarmos nele, perderemos alguns hóspedes
        — ou, pior ainda, falhar ao atraí-los em primeito lugar."

    you "Mas isso é urgente."

    $Asterion.change ("emotion", "neutral")
    show Asterion:
        ease 1.0 xalign 0.5

    pause 1.0

    $Asterion.change ("emotion", "bowing")
    asterion "Temos um dilema em nossas mãos, então.{w=0.2} Se tivermos que escolher
    entre um e outro, sugiro focarmos no projeto da internet."

    pause 2.0

    you "Espera um minuto.{w=0.2} Talvez possamos focar nos dois."

    $Asterion.change ("emotion", "neutral")
    asterion "Focar nos dois?"

    you "Bem, nós temos você, [first_guest] e eu.{w=0.2} Talvez possamos dividir a tarefa entre nós três?"

    $Asterion.change ("emotion", "sad")

    "Astério se retrai."

    asterion "Eu preferiria muito não ser enviado para o vale, Mestre."

    $not_first_guest = 'Kota' if first_guest == 'Luke' else 'Luke'

    asterion "Além disso... Tive uma conversa com [not_first_guest].
    Eu sei que ele está chateado com [first_guest], mas talvez possa ajudar com a outra tarefa."

    asterion "Eu sei que ele tem seus problemas, mas depois da noite passada ele pode estar disposto a ajudar."

    you "Parece uma boa ideia.{w=0.2} Talvez devêssemos todos nos encontrar no saguão, então?"

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("leftarm", "raised")

    asterion "Como quiser, Mestre.{w=0.2} Irei procurá-los imediatamente."

    scene bg black
    with Dissolve (1.0)

    pause 1.0
    "Meia hora depois…"
    pause 1.0

    scene bg oldlobby
    $Kota.change("emotion", "sad")
    $Kota.change("rightarm", "relaxed")
    $Kota.change("leftarm", "relaxed")
    show Kota:
        xzoom -1 zoom 1.0 yalign 1.0 xalign 0.6
    with Dissolve(2.0)
    pause 1.0

    $Kota.change("emotion", "angry")
    $Kota.change("rightarm", "raised")
    $Kota.change("leftarm", "raised")
    if first_guest == 'Kota':
        kota "Isto é absurdo.{w=0.4} Quanta audácia.{w=0.4} Ficarei feliz
        em deixar meu posto no restaurante para ajudá-lo, senhor [player_name],
        mas espero respeito em troca."
        $Kota.change("leftarm", "relaxed")
        kota "Até agora, quinze minutos do meu tempo foram desperdiçados por este {i}imbecil{/i}-"
    else:
        kota "Isto é absurdo.{w=0.4} Quanta audácia."

        kota "Fico mais que feliz em ajudar com o que precisar, senhor [player_name]
        — afinal, estou gostando de sua hospitalidade gratuita —
        mas eu pelo menos espero um mínimo de respeito."
        $Kota.change("leftarm", "relaxed")
        kota "Até agora, quinze minutos do meu tempo foram desperdiçados por este {i}imbecil{/i}-"

    you "Kota, eu sei que vocês estão chateados um com o outro, mas podemos, por favor, manter a civilidade?{w=0.2}
    Isso é importante."
    $Kota.change("leftarm", "relaxed")
    $Kota.change("rightarm", "raised")
    kota "Tudo o que estou dizendo é que podemos começar imediatamente —{w=0.2} apenas você,{w=0.2}
    Astério{w=0.2} e eu.{w} Não consigo imaginar qualquer tarefa que não possa ser realizada sem —"

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("leftarm", "raised")
    $Kota.change("emotion", "surprise")
    $Kota.change("rightarm", "relaxed")
    $Luke.change("emotion", "annoyed")
    $Luke.change("arm", "hip")
    $Luke.change("bandanna", "True")
    $Luke.change("dogtag", "True")
    if first_guest == 'Luke':
        $Luke.change("clothes", "speedo")
    else:
        $Luke.change("clothes", "tankpants")
    show Kota:
        ease 2.0 xalign 1.1
    show Luke:
        xalign -1.5 yalign 1.0 zoom 1.0 xzoom -1
        ease 2.0 xalign -0.2
    show Asterion:
        xalign -1.0 yalign 1.0 zoom 1.0
        ease 2.0 xalign 0.5

    $Kota.change("leftarm", "raised")
    kota "Ah.{w=0.2} Bom dia, senhor Astério.{w} Bom dia, senhor Walker."

    $Luke.change("arm", "pointing")

    $Asterion.change ("emotion", "tired")
    luke "É,{w=0.2} cala a boca.{w} Não age como se eu não tivesse acabado de escutar você falando merda."

    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "angry")
    $Kota.change("leftarm", "relaxed")
    luke "Oi, [player_name].{w=0.2} Desculpa pelo atraso, Astério
    demorou pra me encontrar."

    $Luke.change("emotion", "wink")
    luke "Eu não tava exatamente, digamos, no meu quarto.{w=0.2} Então, do que se trata?"
    $Luke.change("arm", "hip")

    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "puzzled")
    you "Bem, temos uma situação em nossas mãos. Como vocês dois sabem, estamos fazendo todo o
    possível para estabelecer uma conexão com a internet no hotel."

    if first_guest == "Luke":
        $Kota.change("emotion", "happy")
        kota "Ah, é ótimo ouvir isto.{w=0.2} Tenho certeza de que apaziguará alguns dos hóspedes,
        é uma reclamação bastante comum que ouço nos corredores."
    else:
        $Luke.change("emotion", "laughing")
        luke "Olha, tá aí uma boa notícia. Não falo com a minha mãe já tem um tempo."

    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "neutral")
    you "É, mas parece que nos deparamos com outro problema que precisa da nossa atenção,
    {w=0.2} e parece que estão faltando pessoas na equipe — por isso chamamos você, [not_first_guest]."

    $Asterion.change ("emotion", "neutral")
    $Asterion.change ("leftarm", "loose")
    $Asterion.change ("rightarm", "hips")
    asterion "O Mestre irá para o vale abaixo do hotel hoje e poderia aproveitar
    um pouco de ajuda com isto. E também precisamos trabalhar para estabelecer
    a conexão de internet."

    asterion "Há três de nós, acredito que possamos ser divididos em duas equipes.
    Um trabalhará na pesquisa e desenvolvimento e os outros explorarão o vale."

    $Luke.change("arm", "pointing")
    luke "Bem, conta comigo, [player_name]!"
    $Luke.change("arm", "hip")
    $Kota.change("leftarm", "raised")
    kota "Certo."

    $Kota.change("emotion", "angry")
    kota "Contanto que ele esteja longe de mim."
    $Kota.change("leftarm", "relaxed")
    $Luke.change("emotion", "annoyed")
    luke "Bem, eu vou!{w=0.3} Pela primeira vez a gente concorda em alguma coisa."

    you "Claro, acho que podemos resolver."

    $Kota.change("emotion", "neutral")
    $Asterion.change ("emotion", "neutral")
    $Luke.change ("emotion", "neutral")

    $persistent.main_menu_files_artifact = True
    $persistent.main_menu_files_memento = True
    $UI_permissions['file_artifacts'] = True
    $UI_permissions['file_mementos'] = True
    $UI_permissions['exploration'] = True
    $guests.free_guest(not_first_guest)

    $myChoices = [("Ver tutorial", 'yes'), ("Pular tutorial.", 'no')]
    if player_background == "speedrunner":
        $myChoices.append(("{color=[UIColorSpeedrunner]}Regras especiais para Speedrunner.{/color}", 'speedrunner'))

label tutorial2:

    $narrator("Ver o tutorial de exploração?", interact=False)
    $result = renpy.display_menu(myChoices)

    if result == 'yes':
        contract "Explorar o labirinto funciona de maneira semelhante aos projetos de P&D.
        Seus hóspedes agora possuem quatro atributos adicionais: Artefato, Lembrança,
        Inspeção e Perigo."
        contract "O atributo de Artefato afeta sua probabilidade de encontrar itens que podem
        aumentar seus atributos. Lembrança funcionará para encontrar itens antigos
        que podem revelar alguns conhecimentos sobre o passado de Astério."
        contract "Inspeção age de maneira diferente: produzirá recompensas aleatórias. Quanto
        maior for o atributo, mais você poderá encontrar. Inspeção também pode contrubuir para recompensas de
        artefatos e lembranças."
        contract "Artefato, Lembrança e Inspeção também são cumulativos. Se você não encontrar um
        item em uma operação, seus pontos não gastos estarão disponíveis na próxima sessão."
        contract "Uma última coisa: fique de olho em seu atributo de Perigo. Se Perigo for o maior
        atributo total de sua equipe de exploração, há uma chance das forças do labirinto
        atacarem seus hóspedes."
        contract "Isto pode deixar seus hóspedes indisponíveis por dois dias. Se isto acontecer,
        você não poderá atribuí-los a uma equipe, então não vale a pena correr o risco."
        contract "Lembre-se: você pode dividir seus hóspedes da maneira que quiser entre as equipes."
        $myChoices[0] = ("Repetir explicação.", 'yes')

    if result == 'speedrunner':
        you "Espera um minuto. O tutorial acabou de dizer, 'isto pode deixar seus hóspedes
        indisponíveis por dois dias'."
        asterion "Sim, o que tem?"
        you "...'Pode'? Isso significa que existe uma chance de as coisas darem certo.
        Pensa em todos os atalhos que eu posso oegar se derem."
        asterion "..."
        contract "Devido ao seu repertório de escolha, recompensas de inspeção têm uma chance maior de duplicarem!"
        contract "Além disso, se você decidir enfrentar os perigos do labirinto de frente,
        há uma chance de colher recompensas adicionais em vez de
        desabilitar personagens temporariamente."

    if result != 'no':
        jump tutorial2




label RD2:
    $AsterionSent2ndDay = False
    $Kota.change("emotion", "neutral")
    $Kota.change("rightarm", "relaxed")
    $Asterion.change ("emotion", "neutral")
    $Luke.change ("emotion", "neutral")
    $Luke.change ("arm", "hip")

    call screen dayManager("teams")
    $throwaway1 = renpy.random.randint(1, 2)
    if 'Kota' in exploration_team_names() and 'Luke' in exploration_team_names():
        if throwaway1 ==1:
            $Kota.change("emotion", "angry")
            $Luke.change ("emotion", "annoyed")
            $Luke.change ("arm", "pointing")
            luke "Ah não, eu não vou fazer isso. Não vou levar esse cara pra porra de um piquenique comigo."
        else:
            $Kota.change("rightarm", "raised")
            $Kota.change ("emotion", "puzzled")
            kota "[player_name], tem certeza de que é uma boa ideia colocar nós dois na mesma equipe?
            Acredito que vai atrapalhar a cooperação e desacelerar nosso progresso."
        jump RD2
    elif 'Kota' in rd_team_names() and 'Luke' in rd_team_names():
        if throwaway1 ==1:
            $Kota.change("emotion", "angry")
            $Luke.change ("emotion", "annoyed")
            $Luke.change ("arm", "pointing")
            luke "Ah não, eu não vou fazer isso. Não vou me enfiar numa sala minúscula com esse cara."
        else:
            $Kota.change("rightarm", "raised")
            $Kota.change ("emotion", "puzzled")
            kota "[player_name], tem certeza de que é uma boa ideia colocar nós dois na mesma equipe?
            Acredito que vai atrapalhar a cooperação e desacelerar nosso progresso."
        jump RD2
    if 'Asterion' in exploration_team_names():
        $Asterion.change ("emotion", "sad")
        asterion "M-mestre… tem certeza de que quer me mandar para o vale?"
        menu:
            "Manter Astério na equipe de exploração?"
            "Sim":
                if Promise_Valley == "True":
                    asterion "M-mas Mestre... você prometeu..."
                    $ global_affection -= 2
                    $ Promise_Valley == "Broken"
                pause 1.0
                $AsterionSent2ndDay = True
                $Asterion.change ("emotion", "bowing")
                asterion "Muito bem. F-farei como quiser."
                $ global_affection -= 2
                $ abuse_act1 += 2
                $TimesSent += 1
            "Não":
                $Asterion.change ("emotion", "smiling")
                asterion "Obrigado, Mestre."
                jump RD2
    if guests.get_guest_status('Kota') == 'available':
        if first_guest == 'Kota':
            kota "Ficarei no restaurante, suponho. Boa sorte, senhor [player_name]."
        else:
            kota "Bem... isto anula o propósito de me convocar, eu suponho. Boa sorte para você."
    if guests.get_guest_status('Luke') == 'available':
        if first_guest == 'Luke':
            luke "Tudo bem, então, já que não precisa de mim, vou estar no bar. Boa sorte, parceiro."
        else:
            luke "Acho que vou voltar pra cama, então. Boa sorte, parceiro."
    if guests.get_guest_status('Asterion') == 'available':
        asterion "Assumirei as funções da recepção, então, Mestre."


    $throwaway1 = list_into_text(exploration_team_names() + ['you'])
    $throwaway2 = list_into_text(rd_team_names())

    if len(exploration_team_names()) != 0 and len(rd_team_names()) != 0:
        "Com vocês quatro designados às suas funções, você se despede de [throwaway2] enquanto
        [throwaway1] seguem em direção à escada que leva ao vale."
    elif len(exploration_team_names()) == 0 and len(rd_team_names()) != 0:
        "Com vocês quatro designados às suas funções, você se despede de [throwaway2] enquanto se
        prepara e segue em direção à escada que leva ao vale, sozinho."
    elif len(exploration_team_names()) != 0 and len(rd_team_names()) == 0:
        "Com vocês quatro designados às suas funções,
        [throwaway1] segue em direção à escada que leva ao vale."
    elif len(exploration_team_names()) == 0 and len(rd_team_names()) == 0:
        "Você se despede de todos enquanto se prepara e segue em direção à
        escada que leva ao vale, completamente por conta própria."

    scene bgwhite
    with Dissolve (2.0)

    pause 2.0
    play music "music/MayItBegin_Full.ogg" fadeout 1.0 fadein 1.0

    scene bg valley
    with Dissolve(3.0)

    "O vale está exposto à sua frente em todas as suas curvas. Rios e camadas de
    rocha serpenteiam através da paisagem, guiando sua visão para o horizonte laranja e azul."

    "O ar é, de alguma forma, frio e úmido. Ele sopra contra seu peito e rasteja
    até sua coluna, fazendo seus cabelos se arrepiarem e suas bochechas corarem."

    "Os dias passados dentro do hotel o deixaram acostumado a seus odores estéreis e estagnados.
    Esta terra desafia isto completamente — o próprio odor está vivo."

    "Uma espessa nuvem de petricor sopra para cima, como se uma leve garoa tivesse acabado de
    cair sobre o vale, junto com o cheiro de ervas e vegetação rasa."

    "Você não consegue evitar estremecer ao dar o passo final em direção ao sol e entrar nesta terra
    esquecida pelos deuses."
    if len(exploration_team_names()) == 0:
        "Você segue as instruções da cobra e parte para o leste."
    else:
        $throwaway1 = list_into_text(exploration_team_names() + ['you'])
        "[throwaway1] segue as instruções da cobra e parte para o leste."
        if len(exploration_team_names())==2:
            if 'Kota' in exploration_team_names():
                "Você tenta puxar conversa com Kota, mas ele não está muito comunicativo.
                Astério andando atrás de vocês com um olhar miserável em seu rosto parece ter
                azedado o humor do dragão."
            else:
                "Você tenta puxar conversa com Luke, mas ele não está muito comunicativo.
                Astério andando atrás de vocês com um olhar miserável em seu rosto parece ter
                azedado o humor do grifo."
            "A longa e árdua caminhada pela frente e o sol escaldante que se recusa a ceder
            também não ajudam em nada. Uma pessoa não consegue continuar conversando por muito tempo nessas circunstâncias."

        elif 'Asterion' not in exploration_team_names():
            "Por um momento, a conversa flui entre vocês dois. No entanto, a caminhada à sua frente
            é longa e árdua, e o sol escaldante se recua a ceder.
            Uma pessoa não consegue continuar conversando por muito tempo nessas circunstâncias."

    "Vocês estabelecem um ritmo e entram em um transe."

    scene bg valley2
    with Dissolve(3.0)

    "Deixe um lugar sem vigilância por muito tempo e algo mais denso que o silêncio cria raízes.
    Ele se enterra e deixa apenas os olhos para fora,{w=0.2} espiando da areia."

    "Ele espalha as raízes, cresce galhos, floresce e espera até que uma alma
    errante passe perto o suficiente para roçar em sua espinha."

    "Ele abaixa seus galhos para agarrá-lo e puxá-lo de volta para o lugar que você pertence.
    Eles pinicam a parte de trás do crânio e arrepiam os cabelos da nuca."

    "Querem que você vá embora. Estas criaturas não dão boas-vindas aos vivos."

    "Algo tão tímido quanto a respiração é o suficiente para tensionar seus galhos,{w=0.2}
    contraindo-os em garras nodosas."

    "Mas vá em frente.{w=0.2} Uma vez que um lugar é tomado por essas teias de aranha, está comprometido
    a demorar para bani-las."

    "Reinvidique a terra.{w=0.2} Esmague os seixos sob a força de sua debandada;{w=0.2}
    com seu passo forte, quebre-os para revelar a carne espinhosa no interior."

    "Salte sobre as pedras precárias, sinta-as se mexendo e reequilibrando com o seu peso.
    Enquanto ameaçam tombar, pule para a próxima, pouse com os pés macios — e que seu calcanhar
    pouse sem um pio vindo da rocha."

    "Prove seu próprio passo oscilante ao escalar uma duna de areia fofa.{w=0.2}
    Não tenha vergonha quando ficar íngreme, mas avance como uma besta e afunde suas garras
    no tenro peito da areia."

    "Torça sua mão como se fosse um ritual pagão,{w=0.2} como se, em vez de areia
    dispersa, o sangue de um inimigo fosse espalhado."

    "Quando sua respiração acelerar e suor pingar de sua testa,{w=0.2} olhe para o horizonte
    e ouça seus gritos contra sua força.{w=0.2} Deixe a raiva ferver no topo de sua
    garganta, mas engula-a e prossiga, campeão."

    "Saiba bem: este é o seu vale.{w=0.2} Uma terra amaldiçoada, legada pelos deuses para
    os humanos fazerem o que quiserem."

    "Seus seixos ameaçam derrubá-lo,{w=0.2} mas são clivados por sua marcha em vez disso.{w=0.2}
    Suas precárias pedras se movem para frente e para trás para impedi-lo, mas são deixadas expostas e de ponta-cabeça."

    "A vegetação se estende para puxá-lo pelos tornozelos e ombros,{w=0.2}
    mas sua vontade é soberana.{w=0.2} Em seu rastro, tudo o que resta são galhos quebrados e folhas secas."

    "Não tenha piedade deste solo estéril.{w=0.2} Esmague-o sob seu calcanhar{w=0.2}
    — você é o Mestre do domínio,{w=0.2} então o deixe temer seu poder."


    if 'Asterion' in exploration_team_names():
        $Asterion.change("emotion", "sad")
        $Asterion.change("leftarm", "loose")
        $Asterion.change("rightarm", "loose")
        show Asterion:
            xalign 0.5 yalign 1.0 zoom 1.0
        with Dissolve(2.0)
        "No entanto...{w=0.2} para Astério, é uma história diferente."

        "As mesmas pedras nas quais você se equilibra ameaçam derrubá-lo, como se empurrado por alguma
        força invisível e, ao escalar morros, o solo sob seus cascos se esfarela e o faz escorregar."

        "A cada poucos minutos, Astério sacode de susto quando cobras e escorpiões emergem
        de buracos e fendas para rastejar em sua direção."

        "Não demora muito para que seus tornozelos fiquem cobertos de urticária e erupções cutâneas por entrarem
        em contato com a hera venenosa — enquanto você permanece bem, mesmo tento tocado nas mesmas plantas."

        "Quando você faz uma pausa para recuperar o fôlego por alguns minutos, o minotauro faz questão
        de ficar andando de um lado para o outro — caso contrário, seus cascos seriam enredados
        pelas raízes e galhos de arbustos próximos."

        "E quando vocês atingem o topo de colinas ou dunas, ou passam por baixo de árvores retorcidas, pássaros
        descem para bicá-lo. Vespas zumbem ao redor, esperando uma oportunidade para ferroá-lo.
        Larvas caem de madeira apodrecida em seu pescoço."

        "E, no entanto, até agora, você não viu nada assustadoramente perigoso — nenhuma monstruosidade
        correndo em sua direção, nem mesmo o próprio Argos."

    scene bg valley ruins
    with Dissolve(2.0)
    "Assim que o sol atinge seu ápice, meia dúzia de estruturas surgem no horizonte.
    Há uma regularidade humana em sua disposição."

    "A essa altura, suas roupas estão encharcadas e seu rosto está coberto por uma camada de suor,
    óleo e sujeira. Mas nenhuma fome o atormenta, nem seus olhos se cansam."

    "Na verdade, a ideia de alcançar seu objetivo e {i}parar{/i} o deixa inquieto."

    "À medida que você se aproxima, fica claro qual é a \"mais deteriorada\" de todas:
    parte de seu teto desabou, deixando entrar um raio de sol."

    if 'Asterion' in exploration_team_names():
        "Astério se afasta e se esconde na sombra de uma das fornalhas. Ele permanece em silêncio."
    if 'Kota' in exploration_team_names():
        "Enquanto Kota investiga o lugar, você procura pela oferenda que Argos descreveu.
        Você abre a porta da fornalha rachada."
    elif 'Luke' in exploration_team_names():
        "Enquanto Luke investiga o lugar, você procura pela oferenda que Argos descreveu.
        Você abre a porta da fornalha rachada."
    else:
        "Você procura pela oferenda que Argos descreveu. Você abre a porta da fornalha rachada."

    "A luz derrama dentro e um cheiro rançoso rasteja para fora{w=0.2} — ele se agarra às suas narinas e língua,
    um odor metálico e rançoso."

    "Ele rasga através do caminho até seu peito e alarga as chamas que ardem em você.
    O conteúdo de seu estômago sobe para a garganta e você se contorce ao tentar
    manter a compostura."

    "O fedor cauterizante é implacável. Ele se debate dentro de você, tentando agarrar seu coração
    — até que um gemido o traz de volta à realidade."

    "Lá dentro há um fosso, com mais de um metro e meio de profundidade, cavado muito tempo depois da
    construção original da fornalha."
    play sound "sfx/crack.ogg"
    "Algo se move dentro da fornalha{w=0.2} — um semblante escuro em que cada movimento é acompanhado
    pelo estrondo de rocha batendo contra si mesma."

    "Há uma cabeça, com olhos voltados para você e balançando da esquerda para a direita,
    como alguém preso em uma convulsão."
    play sound "sfx/moan.ogg"
    "A coisa toda estremece quando volta à vida e joga um braço em sua
    direção — mas grita com a luz que vem de trás de você."

    "Você recua com o susto e, ao fazer isto, abre ainda mais a porta.
    A coisa recua, grita novamente e cai em prantos arruinados enquanto sua forma é revelada."

    "É escuro como o breu e feito de pedra, mas sua forma é humana.
    Na verdade, possui curvas abundantes e os cabelos longos e soltos de uma mulher."

    "Mas abaixo da cintura, não há nada; suas pernas foram esmagadas,
    e apenas pedaços escuros de rocha espinhosa permanecem."
    play sound "sfx/moan.ogg"
    "A coisa intercala entre recuar da luz e jogar os braços
    em sua direção."

    "Mas mesmo se ela avançasse contra você, falharia — o buraco é muito profundo para que a mulher
    de pedra o pudesse alcançar em seu estado desprovido de pernas."

    show image "gui/inventory/icons/big/item_Bundle.png":
        xalign 0.5
        yalign 0.4
    with Dissolve(1)

    "É apenas então que você olha para baixo, para um pequeno pacote de folhas
    esperando por você a alguns centímetros da porta.
    Corresponde à descrição de Argos. Deve ser o que ele quer que você sacrifique."

    $inventory.add_item("Bundle")

    play sound "sfx/asterionchord.mp3"
    "Você obteve um {color=[UIColorOrange]}pacote{/color}."

    hide image "gui/inventory/icons/big/item_Bundle.png"
    with Dissolve(1)

    "Você pega o pacote e fecha a porta atrás de você."

    if len(exploration_team_names()) == 0:
        "Você já teve o suficiente. Se aventurou no vale, adquiriu o pacote a ser sacrificado,
        e esteve perto de ser atacado por uma criatura do Labirinto."
        if KnowAboutKiln:
            "Você se lembra do que Argos mencionou sobre ter deixado algo atrás
            da fornalha, mas se recusa a ficar mais um minuto sequer."
        "Você sente que já conquistou o suficiente por hoje. É hora de voltar."

    else:
        $Luke.change("emotion", "surprise")
        $Kota.change("emotion", "surprise")
        $Luke.change("arm", "hip")
        $Asterion.change("emotion", "surprise")
        scene bg valley ruins
        $show_team(exploration_team_names())
        with Dissolve(1.0)
        if 'Luke' in exploration_team_names():
            $Luke.change("arm", "pointing")
            luke "Puta merda, parceiro, tenha mais cuidado da próxima vez!"
            $Luke.change("arm", "hip")
        elif 'Kota' in exploration_team_names():
            kota "Senhor [player_name], você deveria ter mais cuidado!"
        elif 'Asterion' in exploration_team_names():
            asterion "M-mestre, por favor, peço que seja mais cuidadoso. O labirinto carrega muitos perigos."
        $Luke.change("emotion", "neutral")
        $Kota.change("emotion", "neutral")
        $Asterion.change("emotion", "neutral")
        you "Sim, isso foi assustador. Acho que a curiosidade matou o gato."

        you "Mas peguei o pacote, suponho."

        if 'Luke' in exploration_team_names():
            if 'Asterion' in exploration_team_names():
                luke "Escuta, [player_name], acho que seria melhor se Ang— quer dizer, Astério
                e eu cuidássemos disso no caso de mais criaturas pularem em você e você não tiver tanta sorte."
                luke "Pode não parecer, mas seu velho amigo Luke aqui já passou por muita merda.
                Merdas piores que essa."
                $Asterion.change("emotion", "sad")
                asterion "..."
                luke "E Astério definitivamente já passou por coisa pior que isso. Eu dou cobertura a ele."
                you "Tem certeza?"
                $Luke.change("emotion", "wink")
                luke "Claro, deixa com a gente. {i}Você{/i} deveria levar esse seu traseiro de volta pro hotel."
                "Você deixa Luke e Astério explorarem o resto das fornalhas e se prepara para
                a longa caminhada de volta ao hotel."
                if KnowAboutKiln:
                    you "Ah, sim. Antes que eu me esqueça, Argos falou alguma coisa sobre olhar
                    atrás das fornalhas. Vocês podem querer verificar isso."
                    $Luke.change("arm", "pointing")
                    luke "Beleza, amigão."
            else:
                luke "Escuta, [player_name], acho que seria melhor se eu cuidasse disso
                no caso de mais criaturas pularem em você e você não tiver tanta sorte."
                luke "Pode não parecer, mas seu velho amigo Luke aqui já passou por muita merda.
                Merdas piores que essa."
                you "Tem certeza?"
                $Luke.change("emotion", "wink")
                luke "Claro, deixa comigo. {i}Você{/i} deveria levar esse seu traseiro de volta pro hotel."
                pause 1.0
                "Você deixa Luke explorar o resto das fornalhas e se prepara para
                a longa caminhada de volta ao hotel."
                if KnowAboutKiln:
                    you "Ah, sim. Antes que eu me esqueça, Luke, Argos falou alguma coisa sobre
                    olhar atrás das fornalhas. Você pode querer verificar isso."
                    $Luke.change("arm", "pointing")
                    luke "Beleza, amigão."

        elif 'Kota' in exploration_team_names():
            if 'Asterion' in exploration_team_names():
                $Kota.change("emotion", "puzzled")
                $Kota.change("leftarm", "raised")
                kota "Agora que você tem o essencial... talvez seja mais prudente se
                voltar para o hotel enquanto o senhor Astério e eu exploramos o restante
                deste lugar."
                $Kota.change("leftarm", "relaxed")
                you "Tem certeza que vocês podem se virar com isso?"
                $Kota.change("emotion", "neutral")
                kota "Senhor [player_name], por favor. Sou um viajante ávido e experiente.
                Posso parecer deslocado nessas situações, mas confie em mim, estou mais confortável do
                que pareço."
                kota "Você não acreditaria nas coisas com as quais me deparei em minhas viagens."
                $Asterion.change("emotion", "sad")
                asterion "..."
                pause 1.0
                $Kota.change("emotion", "sad")
                kota "E tenho certeza que Astério já passou por coisa pior."
                you "Se você insiste, Kota. Eu agradeço."
                if KnowAboutKiln:
                    you "Ah, sim. Antes que eu me esqueça, Argos falou alguma coisa sobre
                    olhar atrás das fornalhas. Vocês podem querer verificar isso."
                    $Kota.change("emotion", "neutral")
                    kota "Cuidaremos disso, então."
            else:
                $Kota.change("emotion", "puzzled")
                $Kota.change("leftarm", "raised")
                kota "Agora que você tem o essencial... talvez seja mais prudente se
                voltar para o hotel enquanto eu exploro o restante deste lugar."
                $Kota.change("leftarm", "relaxed")
                you "Tem certeza que pode se virar com isso?"
                $Kota.change("emotion", "neutral")
                kota "Senhor [player_name], por favor. Sou um viajante ávido e experiente.
                Posso parecer deslocado nessas situações, mas confie em mim, estou mais confortável do
                que pareço."
                kota "Você não acreditaria nas coisas com as quais me deparei em minhas viagens."
                you "Se você insiste, Kota. Eu agradeço."
                if KnowAboutKiln:
                    you "Ah, sim. Antes que eu me esqueça, Argos falou alguma coisa sobre
                    olhar atrás das fornalhas. Você pode querer verificar isso."
                    kota "Cuidarei disso, então."

        elif 'Asterion' in exploration_team_names():
            $Asterion.change("emotion", "sad")
            asterion "Sim, é isto o que importa. Talvez fosse melhor se partirmos."
            menu:
                "Devíamos voltar para o hotel.":
                    you "Sim, sinto que já fizemos o suficiente por hoje.
                    Poderíamos explorar mais, mas eu não quero correr mais nenhum risco,
                    e você deveria vir comigo."
                    "Pela primeira vez desde que vocês partiram para o labirinto, a expressão de Astério
                    se suaviza em um sorriso aliviado."
                    $Asterion.change("emotion", "contemplative")
                    $guests.free_guest('Asterion')
                    asterion "Obrigado, Mestre. Por favor, vamos voltar para o hotel."
                    $ global_affection += 1
                "Você deveria ficar e explorar mais.":
                    you "Bem, chegamos até aqui. Talvez você deva continuar explorando,
                    ver se encontra mais alguma coisa."
                    $Asterion.change ("emotion","bowing")
                    $Asterion.change ("leftarm","raised")
                    $Asterion.change ("rightarm", "loose")
                    "Astério parece estar de coração partido, mas curva-se ao seu comando de qualquer maneira."
                    $Asterion.change ("emotion","sad")
                    asterion "S-se o Mestre assim deseja."
                    $ global_affection -= 1
                    $ abuse_act1 += 1
                    if KnowAboutKiln:
                        you "...Antes de eu ir, Argos disse algo sobre olhar atrás das fornalhas."
                        asterion "... Então começarei aqui, Mestre.
                        Por favor, retorne em segurança."

    scene bg valley2
    with Dissolve(1.0)

    stop music fadeout 2.0

    "A expedição tomou bastante de seu tempo, e se você não quiser estar aqui ao anoitecer,
    precisa retornar logo. Você pega tudo o que precisa e parte para casa."

    scene bg black
    with Dissolve(1.0)

    "Sua primeira parada ao chegar no hotel é o salão. Já que você passou a última semana
    em um lugar onde comida e bebida estão sempre à sua disposição, há muito tempo você não
    sente tanta sede."

    "Sua próxima parada são os aposentos do Mestre. Você toma um banho demorado para lavar toda a sujeira
    e tensão, e então se senta no sofá para descansar e refletir sobre o dia."

    $throwaway3 = exploration_team_names()
    $throwaway1 = list_into_text(exploration_team_names())

    if len(exploration_team_names()) > 0:
        "O pacote está na mesa de jantar. Volta e meia, seus pensamentos se
        voltam para ele e quão pouco tempo lhe resta para sacrificá-lo.
        Você pode apenas esperar que [throwaway1] tenha descoberto algo que possa ajudar."
        if 'Asterion' in exploration_team_names():
            "Você também pensa em Astério, e se pergunta se ele está bem."
    else:
        "O pacote está na mesa de jantar. Volta e meia, seus pensamentos se
        voltam para ele e quão pouco tempo lhe resta para sacrificá-lo.
        Talvez você devesse ter aceitado alguma ajuda e levado alguém com você para o vale."

    play music "music/KoraDuet.ogg" fadeout 1.0 fadein 1.0

    "Depois de um tempo, você decide verificar o progresso de suas equipes."

    $nextLabel = "chapter11_EOD"
    jump teamRewards
label chapter11_EOD:

    #add a bonus tablet if no one got injured, the team is not empty and the player asked question 6
    $throwaway2 = True
    if not KnowAboutKiln:
        $throwaway2 = False
    if throwaway3 != exploration_team_names():
        $throwaway2 = False
    if len(exploration_team_names()) ==0:
        $throwaway2 = False

    if throwaway2:
        $throwaway2 = exploration_team_names()[renpy.random.randint(1, len(exploration_team_names()))-1]
        you "A propósito... você teve a chance de olhar atrás da fornalha?"
        if throwaway2 == 'Asterion':
            $Asterion.change("emotion", "bowing")
            asterion "S-sim, Mestre. Como você disse."
        elif throwaway2 == 'Luke':
            $Luke.change("emotion", "cocky")
            luke "Sim, eu tava meio que esperando outra daquelas coisas pulando em
            mim, mas realmente encontrei algo lá."
        elif throwaway2 == "Kota":
            $Luke.change("emotion", "laughing")
            kota "Para minha surpresa, sim, de fato havia algo mais lá!"
        "[throwaway2] entrega a você uma tábua de argila."
        $nextLabel = "chapter11PostTablet"
        jump RandomTabletReward

label chapter11PostTablet:


    scene bg black
    with Dissolve(1.0)
    "Depois de verificar suas equipes, você vai até o salão para jantar."
    $LoungeBlobs =[True, 2]
    scene Lounge
    with Dissolve(1.0)

    if guests.get_guest_status(first_guest) != 'available':
        "O jantar desta noite não é notável — afinal, [first_guest] passou o dia
        ocupado com outras tarefas — mas todo mundo parece estar curtindo a noite."
    else:
        "Já que [first_guest] não estava ocupado hoje, o jantar desta noite é excepcionalmente elaborado;
        ele parece estar dando tudo de si para compensar e contribuir o quanto puder.
        Todo mundo parece estar curtindo a noite."

    if AsterionSent2ndDay:
        "Astério, no entanto, senta sozinho no bar. Ele apenas beberica seu drinque enquanto [first_guest]
        tenta manter uma conversa fiada."
        "Você fica distraído com sua própria refeição e com todas as pessoas ao seu redor,
        competindo por sua atenção.{w=0.2} O tempo passa rápido e, antes que você perceba,
        as pessoas já estão retornando para seus quartos."
        "É então que você percebe que Astério não está em lugar algum.
        Você pergunta se alguém o viu, mas ele parece ter saído
        enquanto todo mundo estava distraído."
        "Depois de uma busca infrutífera pelo hotel, você retorna aos seus aposentos e vai para a cama."
    else:
        $Asterion.change("emotion", "smiling")
        $Asterion.change("rightarm", "hips")
        $Asterion.change("leftarm", "loose")
        show Asterion:
            xalign 0.5 yalign 1.0
        if 'Asterion' in rd_team_names():
            with Dissolve(1.0)
            "Os hóspedes que trabalharam no projeto da internet cercam Astério —
            todos eles parecem ter se familiarizado bastante uns com os outros durante toda a experiência."
        else:
            "Astério, que cuidou da recepção o dia todo,
            sente-se em casa no salão lotado, cercado de hóspedes."

        $Asterion.change("emotion", "contemplative")
        "Ele sorri e gargalha com suas piadas, até mesmo brinca junto na maioria das vezes,
        mas, com certa frequência, seu olhar desvia para o lado assim como suas orelhas caem."


        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")
        "No meio da refeição, Astério pede licença e deseja a todos uma boa noite.
        Pouco antes de sair, ele olha para você e acena com a cabeça."
        hide Asterion
        with Dissolve(1.0)

        "Depois de terminar sua refeição e desfrutar de um tempo com os hóspedes, você se levanta para
        voltar aos seus aposentos."

        scene bg black
        with Dissolve(1.0)

        "No entanto, conforme você caminha em direção às escadas, algo chama sua atenção."

        play music "music/seikilos.mp3" fadeout 1.0 fadein 1.0

        "Um pouco mais à frente, vindo de fora do hotel, há um tocar de cordas.{w=0.2}
        Nenhuma melodia amarra estas notas ociosas, e cada uma fica suspensa no ar
        até se silenciar."

        "Há uma pontada aguda precedendo cada nota, como se quem a tocou
        tivesse forçado a corda e a soltado em agonia."

        "Você segue o som e abre a porta."

        scene entrancenight
        with Dissolve(1.0)
        show CG5Asterion
        with Dissolve(1.0)

        play music "music/crickets.mp3" fadeout 1.0 fadein 1.0

        "As orelhas do minotauro sacodem para captar seus passos e o barulho da porta,
        mas seu olhar permanece voltado para as estrelas."

        "Seu dedo médio acaricia uma corda, e então a puxa enquanto ela rola em sua pele.
        O minotauro deixa-a enganchar na unha e continua puxando, forçando o fio
        enquanto sua mão enrijece e se contrai em uma garra."

        "Ele puxa a corda da lira com aquela mesma intensidade e retrai ao soltá-la.
        Um grunhido escapa de sua garganta e a cauda se agita."

        "Ele coloca uma mão sobre as cordas, cessando o zumbido moribundo, e deixa sua cabeça cair."

        asterion "Boa noite, meu senhor."

        you "Boa noite, Astério. Curtindo um pouco de ar fresco?"

        asterion "Sim...{w=0.7} Eu precisava pensar um pouco e{w=0.6} ensaiar."

        pause 1.0

        you "Algum problema?"

        "O minotauro curva-se sobre sua lira, reajustando suas mãos sobre ela,
        tentando encontrar uma posição que não pareça tão estranha."

        "Seu antebraço se contrai enquanto ele suga ar até que suas costas se expandam,
        então o deixa sair pela boca."

        asterion "Suponho que tudo se tornou demais hoje. Tantas coisas têm
        acontecido todas de uma vez só."

        asterion "Coisas boas, mas são tantas. Tudo quicou dentro da minha cabeça.
        Todas as pessoas, todas as tarefas, a expedição ao vale também."

        asterion "Então eu vim aqui. Para pensar."

        you "Ah. Se você quiser, posso voltar e deixar você ter sua privacidade. Desculpe interromper."

        pause 1.0

        asterion "Não...{w=0.3} Se você tiver um minuto de sobra, eu gostaria de
        chamar sua atenção para um assunto."

        you "Claro, vá em frente."

        asterion "Apenas...{w} Você não precisa fazer isto."

        pause 1.0

        you "O que você quer dizer?"

        pause 1.0

        asterion "Você não precisa...{w=0.3} você {i}não deveria{/i} me ajudar.{w}
        Indo para o vale sozinho,{w=0.4} dedicando seu tempo e se arriscando,
        {w=0.6} por mim."

        asterion "Vou sarar por conta própria,{w=0.4} dado o tempo necessário."

        you "Você está dizendo isso porque a expedição pode atrapalhar a
        pesquisa da internet?{w} Não precisa se preocupar. Agora que nos
        dividimos em equipes, é realizável."

        asterion "Não é isto."

        "Ele toca as cordas da lira, soltando uma canção de notas sem rumo."

        asterion "Temo que você ficará desapontado depois que tudo isso terminar."

        "O minotauro olha para baixo e junta as pernas para suportar o peso
        da lira, em seguida, levanta as mãos para coçar e arranhar a parte de trás
        do crânio."

        "O pelo atrás de sua nuca fica arrepiado enquanto ele coça,
        cavando com tanta ferocidade que você não ficaria surpreso ao ver tufos de cabelo saindo."

        "O tempo todo ele murmura e grunhe baixinho, procurando
        por palavras que não virão."

        you "Acho que não entendi o que você quer dizer."

        asterion "Às vezes é demais para mim.{w}
        Mesmo que eu goste da companhia, todavia, não consigo evitar desejar
        que tudo pare."

        you "Bem, você ficou trancado por um longo tempo.{w=0.2}
        Não é de se admirar que as coisas estejam sobrecarregando você, depois de todos aqueles anos em um quarto silencioso e escuro."

        pause 2.0

        asterion "Ainda era assim antes de acontecer."

        asterion "Meu estômago se contorce, o fogo sobe até o fundo de minha garganta e
        esta naúsea maçante me faz engulhar."

        asterion "Parece que o mundo inteiro está prestes a desmoronar a qualquer momento.{w=0.2}
        Eu só quero que ele pare."

        "Ele abraça a lira. Quando tenta falar novamente, as palavras ficam presas em sua garganta.
        Ele se curva para cuspi-las, mas tudo o que sai é outro gemido de lamentação."

        you "Você não parece muito bem.{w=0.2} Parece estar tendo um ataque de ansiedade,
        ou talvez esteja entrando em pânico."

        you "Sei que você já passou por muita coisa e não consigo ver minhas palavras contribuindo muito
        para tranquilizar você.{w=0.2} Quer dizer, quanto as palavras significam?"

        you "Mas vou dizer mesmo assim.{w=0.2} Vou fazer tudo o que estiver ao meu alcance
        para fazer com que o hotel cumpra sua missão.{w} Nada de ruim vai acontecer com você."

        "As costas do minotauro se endireitam e sua cauda balança junto com as orelhas.
        Ele olha novamente para as estrelas, segurando seu instrumento, bem na hora que uma brisa
        passa, enviando arrepios em sua espinha."

        "Astério bufa, se sacode e, por um momento, parece que um espírito revigorado
        está assumindo seu corpo."

        "Sua voz, entretanto, conta outra história. Quando ele fala novamente, sai
        entorpecida, vagarosa, com cada sílaba deliberadamente enunciada."

        asterion "Esta lira, meu senhor...{w=0.4} ela não parece tão velha, não é?{w}
        Suas cordas sempre emitirão notas tão vivas, tão fáceis de se tecer em uma melodia encantadora."

        "Uma por uma, todas as peculiaridades ansiosas de Astério — o pelo em pé
        na nuca, seus cascos raspando contra o chão, os dedos
        estremecendo sobre as cordas — todas elas se silenciam."

        "Em seu lugar está outro ser que, embora tranquilizado, parece desanimado
        de uma nova forma completamente fria e controlada."

        asterion "Mesmo assim, esta lira é mais velha que qualquer país no mundo dos vivos."

        asterion "A toco desde que eu era criança."

        asterion "Quando meu pai me enviou para o labirinto, não pude levar muito comigo.
        Ele pensou que seria uma distração.{w=0.2} Mas um guarda a contrabandeou para mim."

        pause 3.0

        asterion "É tão estranho para mim. Por mais de um século tentei aprender a usar talheres e,
        como você pôde ver, eu nunca consegui."

        asterion "Mas não era assim quando eu era criança,{w=0.4} eu conseguia aprender qualquer coisa naquela época.{w=0.2}
        Como esculpir madeira, atirar flechas, tocar esta {w=0.2}velha{w=0.2} amiga lira."

        asterion "Me ajuda a pensar, abafa todo o resto, até mesmo apenas afiná-la
        parece colocar todo o resto em ordem.{w} Minha velha amiga."

        pause 3.0

        asterion "Gostaria de sentar-se comigo esta noite?{w} Por mais turbulenta que minha
        mente possa estar, uma pequena audiência seria...{w=0.4} Eu gostaria de sua companhia."

        $ global_affection += 2

    stop music fadeout 3.0

    scene bg black
    with Dissolve(3.0)
    pause 2.0

    $chapter = "Capítulo 12"

    call screen ChapterTransition("Capítulo 12", "O Concerto")
    pause 0.5
    $save_name=output_save_name("Capítulo 12")


    $nextLabel = "chapter12_daily"
label chapter12_daily:
    $dailyLabel = daily_events.get_daily_event_label()
    if dailyLabel != "none":
        $ renpy.jump(dailyLabel)
    $advance_day()


    play music "music/JatoTheLion.ogg" fadeout 1.0 fadein 1.0

    "Quando você acorda na manhã seguinte, sente a queimação antes mesmo de se levantar.
    Suas pernas não ficam tão doloridas já faz um tempo."

    "Você estica todo o seu corpo e aquela mesma dor se estende até suas costas —
    mas é satisfatória à sua própria maneira."

    "A expedição de ontem para o vale foi uma longa caminhada, uma mudança de ritmo bem-vinda
    depois de passar todos esses dias dentro do hotel. Além disso, você concluiu muita coisa em um dia."

    "Quando você olha para o relógio, descobre já estar um pouco mais tarde que seu horário
    habitual de acordar. Mas, depois de tudo, você merece começar o dia um pouco mais tarde."

    scene bg oldquarters
    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("leftarm", "raised")
    $Asterion.change ("rightarm", "loose")
    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve(3.0)

    if guests.get_guest_status('Asterion') == 'available':
        $Asterion.change ("emotion", "neutral")
    elif guests.get_guest_status('Asterion') == 'RD':
        $Asterion.change ("emotion", "smiling")
    else:
        $Asterion.change ("emotion", "sad")

    "O café da manhã deve ser rápido para compensar por isto, no entanto.
    Enquanto Astério faz ovos mexidos, você vai pelas costas dele e prepara uma torrada."

    "Quando ele põe o prato na mesa e faz menção de preparar outra coisa,
    você o surpreende fazendo um sanduíche com a torrada e os ovos."

    $Asterion.change ("emotion", "contemplative")
    $Asterion.change ("leftarm", "loose")
    $Asterion.change ("rightarm", "hips")

    asterion "Hã?{w=0.2} Isto não é um pouco humilde para o senhor do domínio?"

    you "Talvez, mas já está tarde.{w=0.2} O que você acha de sentarmos juntos
    e compartilharmos um sanduíche enquanto planejamos o dia?"

    $Asterion.change ("emotion", "sad")

    asterion "Ah.{w=0.2} Eu prefero não repetir o desastre do outro dia, se não se importa..."

    you "Bem, os talheres não eram o problema?{w=0.2} Estamos comendo sanduíches hoje, afinal."

    if first_guest == 'Luke':
        you "Tenho certeza que Luke teria um ataque se nos visse comendo
        isso com garfos e facas."

    $Asterion.change ("emotion", "contemplative")

    asterion "Hum.{w=0.2} Suponho que não haja argumento contra isto.{w=0.2}
    Antes de me sentar... minhas roupas estão adequadas para o dia?"


    call screen dayManager("wardrobe")
    if Asterion.clothes =="nude" and Asterion.underwear =="none":
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
        asterion "Por favor, eu gostaria se você parasse de fazer isto."
        $ global_affection -= 1
        $ abuse_act1 += 1

    $Asterion.change ("emotion", "contemplative")

    "Astério inspeciona suas roupas e aparência geral enquanto você come."

    asterion "Obrigado por sua seleção. Hoje pode ser um dia importante, afinal."

    you "Se conseguirmos a garrafa?"

    $Asterion.change ("emotion", "tired")

    asterion "{i}Se{/i} conseguirmos a garrafa,{w=0.2} sim.{w} Devo lembrá-lo
    de que ainda posso sarar sem ela.{w=0.2} Nossa prioridade deveria ser fazer a
    a internet funcionar para não deixar os hóspedes chateados."

    $Asterion.change ("emotion", "sad")

    asterion "Baseado em como você a descreve — e o quanto ouço sobre isto no salão
    — parece ser essencial para todos vocês agora.{w=0.2}
    Seria uma tragédia se perdêssemos hóspedes por causa disso."

    you "É um incômodo viver sem ela, claro. Mas eu diria que estamos fazendo
    um bom trabalho no gerenciamento do hotel sem isso."

    you "Estamos enfrentando muitos desafios e fazendo nosso melhor. Isso fala por si só.
    Duvido que as pessoas parariam de vir para cá por causa da falta de internet."

    you "Além disso...{w=0.2} ainda podemos, espero, conseguir fazer as duas coisas até a noite de hoje."

    $Asterion.change ("emotion", "contemplative")

    "Você dá uma mordida em seu pão com ovo."

    asterion "Você parece otimista, Mestre."

    you "Veremos. Espero que Luke e Kota sejam mais cooperativos hoje."

    "Vocês terminam o café da manhã em silêncio,{w=0.3} juntos,{w=0.3}
    sem qualquer situação catastrófica de talheres."

    scene bg staircase
    with Dissolve(1.0)

    "Depois de limpar a mesa de quaisquer migalhas, você e Astério caminham juntos em direção
    à escadaria antes de se separarem. Você vai para a recepção,
    enquanto Astério convoca os outros."

    scene bg black
    with Dissolve(2.0)

    $LoungeBlobs = [False, 1]

    if first_guest == 'Luke':
        $LoungeBlobs = [False, 0]

        play music "music/AberdeenDoneIt.ogg" fadeout 1.0 fadein 1.0
        scene bg kitchen
        $Luke.change('clothes', 'tankpants')
        $Luke.change('arm', 'hip')
        $Luke.change('emotion', 'neutral')
        show Luke:
            xalign 0.5 yalign 1.0 xzoom 1
        with Dissolve (2.0)

        "Pouco a pouco, Luke vai colocando cada pedaço na bandeja. Ele olha da direita,
        depois da esquerda, antes de finalmente dar alguns passos para trás para ver como fica à distância."

        "Sob qualquer outra circunstância, ele não se importaria com a apresentação —
        os sabores deveriam falar por conta própria, ele acredita — mas hoje, não há margem
        para erro. Precisa ter o sabor {i}e{/i} aparência corretos."

        "Algumas décadas atrás, Luke tinha um amigo para o qual tudo isso era rotina.
        Seu amigo era um chefe cuja conversa de cama frequentemente girava em torno de pratos requintados,
        empratamento artístico e coisas do gênero."

        "As memórias do grifo eram um guia verdadeiro o suficiente— foram necessários apenas
        alguns pequenos ajustes depois de sua tentativa inicial de alcançar o padrão necessário."

        scene Lounge
        show LoungeLight
        with Dissolve(1.0)
        pause 1.0
        show Luke behind LoungeLight
        with Dissolve(1.0)

        "Luke sai para o bar, bandeja em mãos, e a dispõe atrás do balcão."

        "Ele verifica o relógio na parede — cinco para as oito da manhã."

        "Embora o salão estivesse vazio, Luke preferia ter as luzes e a música ligadas
        enquanto cozinhava. Fazia o lugar parecer vivo, cheio de pessoas."

        $Luke.change('arm', 'pointing')
        pause 0.3

        play sound "sfx/beep.ogg"
        hide LoungeLight
        with Dissolve(0.1)
        stop music
        pause 0.2
        $Luke.change('arm', 'hip')

        "Mas isso vai atrapalhar, ele pensa, então os desliga e senta em silêncio."

        pause 2.0

        play music "music/TheSorrow.ogg" fadeout 1.0 fadein 1.0
        pause 1.0
        show Luke:
            ease 2.0 xalign 1.1
        $Luke.change('emotion', 'annoyed')
        $Kota.change('emotion', 'puzzled')
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "relaxed")
        show Kota:
            xalign -1.0 yalign 1.0 xzoom 1
            ease 2.5 xalign -0.2
        pause 2.0

        $Kota.change("rightarm", "raised")
        kota "Bom dia."

        $Kota.change("rightarm", "relaxed")
        luke "Oi."

        show Kota:
            ease 1.0 xalign 0.0
            ease 1.0 yalign 2.0
        "Kota caminha até o bar, inspeciona um banquinho e depois outro,
        antes de se sentar no primeiro."

        "Luke gira os polegares atrás do balcão. Ele se repreende por não ter um pano em mãos
        para limpar o balcão — se apenas para ter uma desculpa para
        evitar conversar com Kota por mais alguns minutos."

        "Ele olha para o lado, procurando, sem sucesso; mesmo sabendo que o deixou
        na cozinha, ele aproveita os últimos segundos antes de ter que
        enfrentar o escrutínio do dragão mais uma vez."

        "Enquanto isso, Kota endireita seu kimono e olha no salão ao redor, depois para o relógio,
        antes de fixar seu olhar em Luke."

        $Kota.change("emotion", "neutral")
        kota "Bom ver que você chegou cedo hoje."

        "O grifo procura no rosto do dragão um toque de sarcasmo ou malícia.
        Ele se descobre querendo isso, aquela vantagem, mesmo que uma parte mais consciente de sua
        mente queira fazer a coisa certa."


        $Luke.change('arm', 'pointing')
        luke "É sério que você tá me criticando agora?"

        $Luke.change('arm', 'hip')
        $Kota.change('emotion', 'puzzled')
        $Kota.change("rightarm", "raised")
        kota "Não, espero não ter soado como tal."

        show Luke:
            ease 1.0 yalign 1.5
            ease 0.5 yalign 1.0

        "Em vez de retrucar, Luke puxa a bandeja que estava deixando atrás do balcão e a dispõe
        em frente ao dragão."
        $Kota.change("rightarm", "relaxed")
        show Luke:
            ease 1.0 xalign 0.9
            ease 1.0 xalign 1.1 yalign 1.0
        $Luke.change("emotion", "neutral")
        luke "É um pouco cedo, mas pensei que você ia estar com fome."

        $Kota.change('emotion', 'surprise')

        "Kota olha para sua refeição com surpresa: uma enorme pirâmide de sushis,
        com uma variedade de molhos e condimentos ao lado."

        "Comida demais para o café da manhã — demais para qualquer refeição."

        $Luke.change("emotion", "cocky")
        $Luke.change('arm', 'pointing')
        luke "Os de salmão na esquerda ficaram ótimos, eu sugiro que você comece com eles."

        $Luke.change("emotion", "neutral")
        $Luke.change('arm', 'hip')
        "Kota olha ao redor da montanha de comida em busca de pauzinhos, mas tudo o que
        vê é uma caneca ao lado com garfos e facas."

        $Kota.change('emotion', 'puzzled')
        "A própria caneca tem \"viva, ria, ame\" estampada em si com uma fonte espalhafatosa de arabescos, embora Luke tenha raspado
        e escrito \"culinária tradicional americana\" por cima."

        "Lutando contra cada fibra de seu ser, ele pega e, seguindo a sugestão do
        grifo, garfa um dos sushis à esquerda e o leva à boca."

        $Kota.change('emotion', 'surprise')
        "Tem gosto de... nenhum sushi ao qual ele esteja acostumado.
        Na verdade, Kota tem certeza de que pode sentir algum tempero entre as algas e este
        arroz que não tem nada o que estar fazendo em um sushi."

        "Mas, de alguma forma, não é ruim."

        $Kota.change('emotion', 'happy')
        kota "Agradeço o gesto."

        $Luke.change('emotion', 'annoyed')
        luke "Se gostou desses, espera até provar meus hambúrgueres, você perdeu uns
        realmente bons no outro dia. Se pelo menos não tivesse agido igual um babaca."

        $Kota.change('emotion', 'angry')
        kota "Acredito que minha atitude foi justificada. Você fez uma introdução terrível
        com seu traje espalhafatoso e comportamento rude."

        $Luke.change('arm', 'pointing')
        luke "Tudo bem, eu admito, não foi a melhor das impressões.
        Eu percebi que alguns dos hóspedes novos não gostaram também e deixei meu traseiro
        fora da recepção o resto do dia."

        $Kota.change('emotion', 'puzzled')
        $Luke.change('arm', 'hip')
        luke "Aprendi minha lição, não quero estragar as coisas com mais ninguém,
        Astério e [player_name] principalmente."

        "Kota estende a mão para outro sushi."

        $Kota.change('emotion', 'sad')
        kota "Sim, de fato. Devo admitir, acho sua devoção ao senhor Astério
        e ao senhor [player_name] admirável."

        $Kota.change('emotion', 'happy')
        $Kota.change("rightarm", "raised")
        $Kota.change("leftarm", "raised")
        kota "E este bar... não é tão mal administrado como eu imaginava.{w=0.2}
        Talvez eu o tenha julgado mal."

        $Luke.change("emotion", "neutral")
        $Kota.change('emotion', 'puzzled')
        $Kota.change("leftarm", "relaxed")
        "Para o desalento de Kota, Luke pega um sushi do topo da pilha, mergulha em ketchup,
        e engole inteiro."

        $Kota.change("rightarm", "relaxed")
        luke "Espero que não se importe, tem bastante aí pra nós dois."

        "Normalmente, Kota realmente se importaria. Mas hoje já é um dia peculiar—
        por que não ir até o fim?"

        $Kota.change("emotion", "neutral")
        "O dragão pega outro sushi da borda da bandeja: o mais distante da
        tijela de ketchup."

        $Luke.change("emotion", "annoyed")
        luke "Eu acho que é isso que importa, sabe. O troço da internet e a expedição
        pro vale— tudo isso. A gente só vai atrapalhar se continuar agindo que nem uns babacas."

        $Kota.change("emotion", "sad")
        kota "Isto é verdade."

        $Luke.change("emotion", "neutral")
        $Kota.change("emotion", "neutral")
        "Ambos continuam comendo em silêncio. À medida que mais da comida abre caminho para o fundo
        prateado da bandeja, a postura de Kota torna-se menos rígida e a expressão de Luke relaxa."

        "Ambos se olham, sorriem e conversam. Kota concorda em experimentar os hambúrgueres de
        Luke na próxima vez, e o grifo fica extasiado com as histórias do dragão
        sobre um condimento exótico conhecido como \"molho de soja.\""

        "Depois que a conversa se esgota, eles voltam a ficar em silêncio —
        desta vez sem uma gota da tensão que pairava entre eles
        no dia anterior."



    else:
        play music "music/TheSorrow.ogg" fadeout 1.0 fadein 1.0
        $Kota.change('emotion', 'sad')
        $Kota.change("leftarm", "mug")
        scene Lounge
        show Kota:
            xalign 0.5 yalign 1.0 xzoom 1
        with Dissolve(2.0)
        "Kota dispõe o último prato do lote e se vira para o relógio na parede.
        Cinco para as oito."

        "Pouquíssimos hóspedes apareceram para um café da manhã cedo hoje.
        As únicas pessoas até agora foram os trabalhadores sul-americanos."

        $Kota.change('emotion', 'happy')
        "Kota começou a gostar da companhia deles nos últimos dias.
        E eles, por sua vez, gostavam de sua voz grave e das piadas, sorrisos, e
        extensas explicações que ele trazia com cada prato..."

        "Talvez não estivessem acostumados a serem tratados tão bem."

        "E, é claro, eles amavam sua comida; mesmo que fosse tão distante
        do que suas esposas cozinhavam em casa."

        "Então, havia uma certa decepção no ar quando, esta manhã,
        Kota não serviu seu arroz cozido no vapor, truta grelhada e kobachi de costume{w=0.2}
        Em vez disso, o dragão cozinhou um especial bastante incomum para o dia."

        $Kota.change('emotion', 'sad')
        "Ainda assim, a comida de Kota não deixou nada a desejar, e eles comeram mesmo assim.
        Um cliente feliz sempre animou Kota;{w=0.2}
        mas conforme o relógio continuava correndo,{w=0.2} ele começou a se perguntar se o esforço valeu a pena."

        play music "music/AberdeenDoneIt.ogg" fadeout 1.0 fadein 1.0
        pause 1.0
        $Luke.change('arm', 'hip')
        $Luke.change('emotion', 'annoyed')
        $Kota.change('emotion', 'puzzled')
        show Kota:
            xzoom -1
            ease 2.0 xalign 1.1
        show Luke:
            xalign -1.0 yalign 1.0 xzoom -1
            ease 2.0 xalign -0.1
        pause 2.0
        $Kota.change('emotion', 'neutral')
        $Kota.change('leftarm', 'raised')
        kota "Ah. Bom dia,{w=0.2} senhor Walker."

        $Kota.change('leftarm', 'relaxed')
        $Luke.change('arm', 'pointing')
        luke "Dia."

        show Luke:
            ease 1.0 xalign 0.1
            ease 1.0 xalign 0.1 yalign 1.5
        $Luke.change('arm', 'hip')
        "Luke puxa um banquinho para trás, senta-se do outro lado do bar
        e repousa as mãos no balcão."

        pause 1.0

        $Kota.change('emotion', 'sad')
        $Kota.change('leftarm', 'mug')
        "Luke olha para o lado, para os outros hóspedes batendo papo.
        Ele balança os pés enquanto gira os polegares."

        "Kota, enquanto isso, baixa os olhos para lavar algumas xícaras. Ele espera por ela — pela
        inevitável piada de mal gosto do grifo. Ele nem mesmo olha para cima,
        tão certo ele de que está chegando."

        "Mas ela nunca chega. Ele lança um olhar em Luke, dois, três, até
        que eles estão se encarando em reconhecimento."
        show Kota:
            ease 1.0 xalign 0.9
            ease 1.0 xalign 1.1
        "Kota puxa uma bandeja e a coloca na frente do grifo."

        $Kota.change('emotion', 'neutral')
        $Kota.change('leftarm', 'relaxed')
        $Kota.change('rightarm', 'raised')
        kota "Você apareceu a tempo."

        $Kota.change('rightarm', 'relaxed')
        "Luke olha para seu prato.{w} Panquecas,{w=0.2} ovos fritos,{w=0.2} bacon,
        {w=0.2} e suco de laranja espremido na hora."

        $Luke.change('arm', 'pointing')
        luke "Sim.{w=0.2} E você não tava falando merda de mim quando eu cheguei aqui,
        então acho que nós dois merecemos um 'êêêêê'."

        $Luke.change('arm', 'hip')
        $Kota.change('emotion', 'sad')
        pause 1.0
        $Kota.change('leftarm', 'raised')
        kota "Você me deu razões mais do que suficientes para fazer isso."

        $Luke.change('emotion', 'hornier')
        $Kota.change('emotion', 'puzzled')
        "Luke pega uma tira de bacon do prato com as mãos, mergulha na
        gema de ovo e abre bem o bico para engoli-la inteira."

        $Kota.change('emotion', 'neutral')
        $Luke.change('emotion', 'neutral')
        $Kota.change('leftarm', 'relaxed')
        "Talvez tal exibição teria causado desgosto em Kota apenas uma semana antes,
        mas desta vez ele não se encontra incomodado com isso."

        $Luke.change('emotion', 'annoyed')
        luke "Não dei não.{w=0.2} Eu sei que eu posso ser difícil de lidar, mas
        isso não significa que você pode falar mal de uma pessoa quando ela não
        tem a chance de se defender.{w=0.2} Não é algo que um cavalheiro faria."

        $Kota.change('emotion', 'sad')
        pause 1.0

        $Luke.change('emotion', 'neutral')
        luke "Mas...{w=0.2} você tem razão.{w=0.2} Eu fui até você, te deixei
        desconfortável e depois piorei a situação."

        $Luke.change('emotion', 'annoyed')
        luke "Foi uma coisa escrota de se fazer.{w=0.5} Eu peço desculpas."

        $Kota.change('emotion', 'neutral')
        pause 1.0

        $Kota.change('leftarm', 'raised')
        kota "Você está perdoado."
        $Kota.change('leftarm', 'relaxed')
        pause 1.0

        $Luke.change('emotion', 'cocky')
        $Luke.change('arm', 'pointing')
        luke "Eeeeee?"

        $Kota.change('emotion', 'sad')
        pause 1.0

        $Kota.change('rightarm', 'raised')
        $Luke.change('arm', 'hip')
        kota "Eu admito que o julguei mal. E, na verdade, sua vontade de ajudar o
        senhor Astério e o senhor [player_name] revelou algumas qualidades suas que devo respeitar."

        $Kota.change('emotion', 'neutral')
        $Luke.change('emotion', 'neutral')
        kota "Você poderia ter ficado parado sem fazer nada, mas ofereceu sua ajuda para uma tarefa difícil
        e arriscada.{w=0.2} Isto, eu suponho, diz mais sobre seu caráter do que nossa briga mesquinha
        jamais poderia."

        $Kota.change('rightarm', 'relaxed')
        $Luke.change('emotion', 'cocky')
        "Luke sorri,{w=0.3} corta um grande pedaço de panqueca{w=0.3} e, em seguida,
        dobra ao meio e desce todo o pedaço enorme pela goela."


        $Kota.change('emotion', 'puzzled')
        kota "Mesmo que — e devo ser honesto a respeito disso —
        suas maneiras deixem muito a desejar."

        "Luke engole{w=0.2} e limpa a garganta enquanto passa um guardanapo na mão."

        $Kota.change('emotion', 'neutral')
        "Ele corta um pedaço menor desta vez, um que ainda faria um humano
        engasgar, e o leva à boca."

        $Luke.change('emotion', 'happy')
        luke "Desculpa.{w} É que isso tá bom pra ca—{w=0.2} quer dizer, tá uma delícia."

        $Kota.change('emotion', 'happy')

        "Luke toma um gole do suco de laranja."

        $Luke.change('emotion', 'annoyed')
        $Kota.change('emotion', 'neutral')
        luke "Mas você tá certo.{w=0.2} Tem coisas que importam mais por aqui,{w=0.2}
        e a gente seria mais útil pra essa joça se não agíssemos que nem uns babacas
        idiotas um com o outro."

        $Luke.change('emotion', 'neutral')
        show Luke:
            ease 1.0 xalign 0.2 yalign 1.0
        pause 1.0
        $Luke.change('arm', 'pointing')
        $Kota.change('emotion', 'puzzled')
        "Luke estende sua mão direita para Kota. O dragão hesita —
        os dedos escamosos do grifo estão cobertos por uma película de gema de ovo e
        gordura de bacon, transformando de volta em fogo as brasas de inimizade."

        $Kota.change('emotion', 'neutral')
        $Kota.change('rightarm', 'raised')
        show Kota:
            ease 1.0 xalign 0.9
        pause 1.0
        show Luke:
            ease 0.5 yalign 1.4
            ease 0.5 yalign 1.0
        show Kota:
            ease 0.5 yalign 2.2
            ease 0.5 yalign 1.0
        pause 2.0

        $Kota.change('emotion', 'laughing')
        $Luke.change('emotion', 'laughing')
        $Luke.change('arm', 'hip')
        $Kota.change('rightarm', 'relaxed')
        "O dragão azul pega a mão de Luke, apesar de tudo."

        "Ele se lembra, conforme sua palma encontra às do americano com um
        som molhado, que ele pode lavá-las depois— engolindo seu orgulho tão
        prontamente quanto Luke engole o restante de seu café da manhã."

        "Paz restaurada, compreensão substitui inquietação; em pouco tempo,
        ambos recordam seu primeiro encontro e riem."

    $Kota.change('emotion', 'neutral')
    $Luke.change('arm', 'hip')
    $Luke.change('emotion', 'neutral')
    $LoungeBlobs = [False, 2]

    "Os dois passam a meia hora seguinte sem dizer uma palavra um ao outro,
    mas sem se incomodar com a companhia. Eles aproveitam o café da manhã, se ocupam com tarefas básicas
    e cumprimentam os outros hóspedes à medida que o salão se enche."

    "Os outros hóspedes sussurram — que grande diferença comparando às brigas dos dias anteriores."

    if first_guest == 'Kota':
        show Kota:
            ease 2.0 xalign 1.1
        show Luke:
            xzoom 1
            ease 2.0 xalign 0.5
    else:
        show Kota:
            xzoom -1
            ease 2.0 xalign 0.5

    $Asterion.change("emotion","neutral")
    $Asterion.change("leftarm", "loose")
    $Asterion.change("rightarm", "loose")

    show Asterion:
        xalign -1.0 yalign 1.0
        ease 3.0 xalign -0.1

    pause 3.0

    $Asterion.change("emotion","surprise")
    "Quando Astério entra no salão ele, como os outros hóspedes,
    não consegue conter sua supresa ao ver os dois se dando bem."

    $Asterion.change("emotion","bowing")
    $Asterion.change("leftarm", "raised")

    asterion "Luke, Kota, a presença de vocês é solicitada na recepção."

    $Luke.change('arm', 'salute')
    luke "Beleza, parceiro. Vamo lá."
    $Kota.change('leftarm', 'raised')
    kota "Claro."

    scene bg black
    with Dissolve(1.0)

    pause 2.0

    scene bg oldlobby
    with Dissolve(1.0)

    "Você se apoia na mesa da recepção."

    "Você pensa sobre quão vazio costumava ser este lugar, e no quão ocupado está agora.{w=0.2}
    Hoje será um outro dia estressante, mas pode-se esperar que no final
    tudo tenha valido a pena."

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "hip")
    $Kota.change('leftarm', 'relaxed')

    show Asterion:
        xalign -0.1 yalign 1.0
    with Dissolve(0.5)
    show Kota behind Asterion:
        xalign 1.9 yalign 1.0 xzoom -1.0
        ease 2.5 xalign 0.5
    show Luke behind Kota:
        xalign 2.0 yalign 1.0 xzoom 1.0
        ease 2.5 xalign 1.1

    "Você não tem muito tempo para refletir, entretanto, uma vez que Astério retorna
    do salão muito mais rápido do que você esperava."

    "Para sua surpresa, Luke e Kota andam atrás dele. Ainda distantes um do outro,
    mas não brigando."

    you "Bem, parece que está todo mundo aqui."

    $Asterion.change("emotion","neutral")
    $Asterion.change("leftarm", "loose")

    #if Internet not achieved
    if not rewards.is_obtained('WiFi'):
        you "Então, estamos um pouco apertados se tratando de tempo e recursos.
        Hoje é nossa última chance de conseguir a garrafa. Precisamos sacrificar o
        pacote que encontramos ontem em algum lugar do labirinto."

        you "{i}E{/i} nós ainda temos o problema da internet para resolver."

        $throwaway1 = str(preset_rewards['WiFi']['stats']['Contract'])
        $throwaway2 = str(preset_rewards['WiFi']['stats']['Tech'])
        $throwaway3 = str(inventory.accumulated_stats['RD'].get_value('Contract'))
        $throwaway4 = str(inventory.accumulated_stats['RD'].get_value('Tech'))

        you "Greta mencionou ontem que precisávamos reescrever {color=[UIColorHumanities]}[throwaway1] contratos{/color}
        e completar {color=[UIColorTech]}[throwaway2]{/color} esquemas de {color=[UIColorTech]}Tecnologia{/color} para conseguir acesso à internet.
        Até então nós temos {color=[UIColorHumanities]}[throwaway3]{/color} e {color=[UIColorTech]}[throwaway4]{/color} respectivamente."

        $throwaway1 = str(preset_rewards['Wine']['stats']['Artifact'])
        $throwaway2 = str(preset_rewards['Wine']['stats']['Surveying'])
        $throwaway3 = str(inventory.accumulated_stats['Exploration'].get_value('Artifact'))
        $throwaway4 = str(inventory.accumulated_stats['Exploration'].get_value('Surveying'))

        you "E, no que diz respeito à garrafa... Astério?"

        asterion "Bem, há {color=[UIColorMath]}[throwaway2] lugares que precisariam ser inspecionados{/color},
        e {color=[UIColorArts]}[throwaway1] artefatos{/color} necessários. Até então, temos
        {color=[UIColorMath]}[throwaway4]{/color} e {color=[UIColorArts]}[throwaway3]{/color} respectivamente."

        you "Se todo mundo estiver ok com isso, podemos dividir nossos recursos como fizemos ontem.
        Devo presumir que vocês dois não querem trabalhar juntos de novo?"

    else:
        you "Então, hoje é nossa última chance de pegar a garrafa. Precisaremos sacrificar o
        pacote que encontramos ontem em algum lugar do vale."

        $throwaway1 = str(preset_rewards['Wine']['stats']['Artifact'])
        $throwaway2 = str(preset_rewards['Wine']['stats']['Surveying'])
        $throwaway3 = str(inventory.accumulated_stats['Exploration'].get_value('Artifact'))
        $throwaway4 = str(inventory.accumulated_stats['Exploration'].get_value('Surveying'))

        you "Quanto progresso fizemos, Astério?"

        asterion "Bem, há {color=[UIColorMath]}[throwaway2] lugares que precisariam ser inspecionados{/color},
        e {color=[UIColorArts]}[throwaway1] artefatos{/color} necessários. Até então, temos
        {color=[UIColorMath]}[throwaway4]{/color} e {color=[UIColorArts]}[throwaway3]{/color} respectivamente."

        you "Felizmente, o problema da internet foi resolvido, mas ainda podemos colocar pessoas na equipe de P&D
        para trabalhar em outras coisas se não quiserem explorar o vale, ou..."

        pause 1.0

        you "Acho que vocês dois vão querer ficar separados."

    $Luke.change("emotion", "cocky")
    luke "Nah. Não se preocupe com isso."
    $Luke.change("emotion", "neutral")

    $Kota.change('leftarm', 'raised')
    kota "Faremos o que for necessário para ajudar, sim."
    $Kota.change('leftarm', 'relaxed')

    you "Bem, é uma boa notícia.{w=0.2} Obrigado, vocês dois."

    #if guests are injured
    if guests.get_guest_status('Asterion') == 'unavailable' or guests.get_guest_status('Kota') == 'unavailable' or guests.get_guest_status('Luke') == 'unavailable':
        you "Eu sei que alguns de vocês passaram por maus bocados ontem, e eu acho que é melhor se ficarem de fora dessa
        e se recuperarem. O resto de nós fará o que for preciso."

    you "Então, esse é o estado das coisas.{w} Agora, vamos —{nw}"

    show Ismael_surprise:
        yalign 6.0 xalign 0.5 xzoom 1 zoom 1.0
        ease 1.0 yalign 1.1

    pause 0.5
    $Asterion.change("emotion","surprise")
    $Kota.change("emotion","surprise")
    $Luke.change("emotion","surprise")

    show Asterion:
        ease 0.5 xalign -0.3
    show Kota:
        ease 0.5 xalign 0.7
    show Luke:
        ease 0.5 xalign 1.3

    "Ismael" "Ah merde, desculpa!"

    luke "Que porra é essa?!"

    show Ismael_surprise:
        ease 0.4 yalign 1.0
        ease 0.4 yalign 1.1

    "Ismael" "Foi mal, foi mal, pensei que não ia ter ninguém aqui por um tempo!"
    show Ismael_surprise:
        ease 1.5 yalign 1.0 xalign 1.6
    pause 1.0
    show Asterion:
        ease 0.5 xalign -0.1
    show Kota:
        xzoom 1.0
        ease 0.5 xalign 0.5
    show Luke:
        xzoom -1.0
        ease 0.5 xalign 1.1

    "Ismael corre de forma desajeitada na direção do salão, os braços atrás das costas."
    pause 1.0
    $Asterion.change("emotion","neutral")
    $Kota.change("emotion","neutral")
    $Luke.change("emotion","neutral")
    show Kota:
        xzoom -1.0
    show Luke:
        xzoom 1.0
    pause 1.0

    you "Enfim…"

    $BundleSacrifice = 'none'

    if KnowAboutShrine:
        play sound "sfx/dishes.ogg"
        "Você ouve um barulho de batida vindo do salão, seguido pelo som de vidro quebrando e uma farra
        estridente de xingamentos."

        "É apenas Ismael tropeçando, você assume. Lá no salão está a lareira, que está
        ao lado de alguns sofás e elevada em um degrau do térreo."

        "Várias pessoas tropeçaram neste local; você recebeu várias reclamações sobre isto."

        "Você tentou usar a magia do hotel para realocá-lo em algum lugar com menos tráfego, mas
        parece permanecer preso onde está."

        "Talvez haja um contrato no caminho que torne a sua posição no hotel um ponto
        fixo no espaço. Você terá que discutir isto com Astério em algum momento."

        play music "music/asterion.ogg" fadeout 1.0 fadein 1.0
        pause 2.0

        "E é aí que você percebe."

        "Você pressionou Argos a dizer algo, dá-lo uma ideia, que talvez ele não devesse."

        argos "{i}Dito isto...{w=0.3}qualquer um dos santuários divinos vai servir!{w}
        E eu falo sério.{/i}"

        "Você olha para o salão, para o fogo queimando na lareira. Talvez uma solução
        para o seu problema esteve embaixo de seu nariz esse tempo todo e você não percebeu."

        "Na verdade, você pensa sobre o que Astério mencionou dois dias atrás, em relação à
        bacia no alicerce do labirinto."

        asterion "{i}Milênios atrás, era um santuário para o deus Hermes, patrono do comércio e dos mensageiros.{w=0.2}
        Existem outros locais semelhantes neste domínio dedicados a deuses específicos.{/i}"

        "Talvez... você não precise percorrer todo o caminho até o vale para fazer um sacrifício digno."

        $Asterion.change("emotion","surprise")
        you "Astério, temos algo como um \"santuário divino\" no hotel?"

        $Asterion.change("emotion","neutral")
        asterion "Receio não saber sobre o que você está falando, Mestre."

        you "Quer dizer...{w=0.2} algo como um santuário, mas criado pelos próprios deuses.{w=0.2}
        Suponho que eles devam ser coisas bem antigas, datando de quando esse lugar foi criado."

        you "Isso te dá alguma ideia?"

        $Asterion.change("emotion","contemplative")
        asterion "Sim, algumas vêm à mente."

        asterion "A lareira perto do salão,{w=0.2} como você sabe,{w=0.2} é um santuário para a
        deusa Héstia."

        $Asterion.change("emotion","contemplative")
        asterion "A bacia no alicerce é um santuário para Hermes,{w=0.2} hum..."

        $Asterion.change("emotion","smiling")
        pause 1.0
        asterion "Também temos um santuário de Hades em um dos jardins.
        Eu costumava mantê-lo em bom estado, embora ainda não tenha conseguido..."
        pause 1.0
        $Asterion.change("emotion","neutral")
        asterion "Mas...{w=0.2} por que você pergunta?"

        you "Quando eu pressionei Argos por mais informações, ele me disse que aceitaria um
        sacrifício em qualquer \"santuário divino.\""

        pause 1.0

        $Asterion.change("emotion","smiling")
        pause 0.5
        $Kota.change("emotion","happy")
        pause 0.5
        $Luke.change("emotion","cocky")

        you "Então, sim, não acho que precisamos fazer uma grande expedição para sacrificar o pacote."

        $Kota.change('rightarm', 'raised')
        kota "Esta é uma notícia excelente!"
        $Kota.change('rightarm', 'relaxed')

        $Asterion.change("emotion","contemplative")
        $Asterion.change("rightarm", "hips")
        asterion "De fato."

        $Luke.change("emotion","annoyed")
        luke "Espera, isso significa que vão me colocar no serviço de nerd?{w} Merda.{w=0.4} Eu tava querendo
        ir pra caminhada,{w=0.2} pra ser sincero."

        you "Bem,{w=0.2} ainda podemos enviar pessoas até o vale para encontrar outras coisas
        úteis, suponho."

        $Luke.change("emotion","neutral")
        you "Então, Astério e eu vamos ficar e fazer o sacrifício, então.{w=0.2}
        Talvez eu não devesse arriscar nenhum encontro como o de ontem se não for estritamente necessário."

        you "Ok, eu tenho três opções, então…"

        menu:
            "Fazer um sacrifício para Hermes na bacia do alicerce.":
                you "Então, Astério, tudo o que eu preciso fazer é ir para o alicerce e queimar o pacote
                perto da bacia no meio do cômodo?"
                $BundleSacrifice = 'Hermes'

            "Fazer um sacrifício para Héstia na lareira do salão.":
                you "Então, Astério, tudo o que eu preciso fazer é ir até a lareira
                e jogar o pacote no fogo?"
                $BundleSacrifice = 'Héstia'

            "Fazer um sacríficio para Hades na estátua do jardim.":
                you "Então, Astério, tudo o que eu preciso fazer é ir até a estátua com o cachorro de três cabeças
                no jardim e queimar o pacote na frente dela, certo?"
                $BundleSacrifice = 'Hades'

        $Asterion.change("emotion","smiling")
        asterion "Mais ou menos, sim."
        $guests.disable_guest('Asterion')
        "Isso é o que eu vou fazer. Quanto ao restante..."

    else:
        $Asterion.change("emotion","smiling")
        you "Se estiver tudo bem para todo mundo, não vou me aventurar no vale hoje,
        considerando com o que me deparei ontem."
        asterion "Sim, seria melhor para você evitar quaisquer riscos desnecessários, Mestre."
        you "Quanto ao restante, vamos nos dividir em times de novo, certo?"

    call screen dayManager("teams")

    if 'Asterion' in exploration_team_names():
        $Asterion.change ("emotion", "sad")
        if Promise_Valley == "True":
            asterion "M-mas Mestre... você prometeu..."
            $ global_affection -= 2
            $ Promise_Valley == "Broken"
            pause 1.0
            $Asterion.change ("emotion", "bowing")
            asterion "Muito bem. F-farei como desejar."
        $TimesSent += 1
        $ abuse_act1 += 1
        $ global_affection -= 2

    you "Tudo bem, a função de todos aqui está clara? Muito bem, vamos em frente, então."

    if len(rd_team_names()) != 0:
        $throwaway1 = list_into_text(rd_team_names())
        "Astério cantarola a melodia e uma passagem descendente para o alicerce
        se materializa próximo à porta que leva à escadaria. Você se despede de [throwaway1]."
        if 'Luke' in rd_team_names():
            hide Luke
        if 'Asterion' in rd_team_names():
            hide Asterion
        if 'Kota' in rd_team_names():
            hide Kota
        with Dissolve (1.0)

    if len(exploration_team_names()) != 0:
        $throwaway1 = list_into_text(exploration_team_names())
        $throwaway2 = 'o' if len(exploration_team_names()) == 1 else 'os'
        $throwaway3 = 'ele anda' if len(exploration_team_names()) == 1 else 'eles andam'
        if BundleSacrifice == 'none':
            "Você entrega a [throwaway1] o pacote e [throwaway2] deseja sorte."
        else:
            "Você deseja boa sorte a [throwaway1] enquanto [throwaway3] em direção ao vale.
            Você segura o pacote em suas mãos com um largo sorriso."
            if ArgosContract == "Tricked":
                "Mais uma vez, você conseguiu passar a perna na cobra."

        if 'Luke' in exploration_team_names():
            hide Luke
        if 'Asterion' in exploration_team_names():
            hide Asterion
        if 'Kota' in exploration_team_names():
            hide Kota
        with Dissolve (1.0)
    else:
        if BundleSacrifice == 'none':
            "Você segura o pacote nas mãos e encara a escada que leva ao vale.
            Parece que ele não será sacrificado hoje."
        else:
            "Parece que mandar pessoas ao vale não é necessário por enquanto.
            Você, enquanto isso, segura o pacote em suas mãos com um largo sorriso."
            if ArgosContract == "Tricked":
                "Mais uma vez você conseguiu passar a perna na cobra."

    hide Kota
    hide Luke
    with Dissolve (1.0)
    if BundleSacrifice != 'none':
        show Asterion:
            ease 2.0 xalign 0.5
        you "Bem, quer se livrar dessa coisa, Astério?"
        $Asterion.change ("emotion", "bowing")
        $Asterion.change ("rightarm", "loose")
        $Asterion.change ("leftarm", "raised")
        asterion "Seria um grande prazer, [player_name]."

        if BundleSacrifice == 'Héstia':
            scene bg black
            with Dissolve(2.0)
            pause 2.0
            if first_guest not in guests.get_guests_with_status(['RD', 'Exploration']).names():
                $LoungeBlobs = [True, 2]
            else:
                $LoungeBlobs = [False, 2]
            $Asterion.change ("emotion", "smiling")
            $Asterion.change ("rightarm", "loose")
            $Asterion.change ("leftarm", "loose")
            scene Lounge
            show Asterion:
                xalign 0.5 yalign 1.0
            with Dissolve(1.0)
            "Você e Astério vão até a lareira do salão, mas no caminho ele chama os hóspedes para
            segui-lo — haverá uma \"pequena celebração\"."
            $inventory.remove_item('Bundle')
            "Na lareira, Astério começa derramando punhados de azeite em suas mãos e depois
            jogando no fogo."

            $Asterion.change ("emotion", "contemplative")
            "O minotauro então invoca garrafas de vinho — ele derrama um longo fio diante do fogo,
            que só parece alimentar seu brilho."

            "Ele então serve vinho para você e para os hóspedes e diz que eles estão livres para saboreá-lo.{w=0.2}
            Ele se volta novamente para a chama."

            "Eles não entendem o ritual, mas apreciam a oferta de álcool."

            $Asterion.change ("emotion", "bowing")
            asterion "Héstia, filha de Cronos, gloriosa é tua parcela e o teu direito em nossa morada.{w=0.2}
            Tua é a graça que nos dá propósito."

            asterion "Héstia, tu te destacas entre os deuses imortais e os homens errantes que encontram
            descanso neste domínio."

            asterion "Venha e habite em nosso hospitaleiro lar em amizade.{w=0.2}
            Conceda-nos sua aprovação em manter a missão humana do hotel."

            asterion "Salve, Filha de Cronos.{w=0.2} Preencheremos esta morada com hóspedes e
            canções em tua homenagem."

            "Ele coloca a oferenda no fogo, sem medo de queimar as pontas dos dedos.
            Em segundos, uma nuvem de fumaça espessa e pungente brota e sobe pela chaminé."

            "Você e Astério se distanciam dela, mas não antes de o minotauro derramar mais
            um pouco de vinho."

            $Asterion.change ("emotion", "smiling")
            $Asterion.change ("rightarm", "hips")
            asterion "Fui ensinado a venerar Héstia quando era criança, meu senhor.
            Estou bem familiarizado com todos os seus rituais."

            $Asterion.change ("emotion", "contemplative")
            asterion "Ah... Em outra vida, eu poderia ter sido um sacerdote de sua graça,
            tão conhecedor era eu de sua sabedoria."

            $Asterion.change ("emotion", "smiling")
            asterion "E olhe para nós...{w=0.3} Cuidando de um hotel.{w=0.2} Tenho certeza que sua graça olha
            para nós com alegria em seus olhos, onde quer que ela esteja."

        elif BundleSacrifice == 'Hermes':
            hide Asterion
            with Dissolve(1.0)
            "O minotauro vai para os aposentos do mestre para pegar algo."
            $Asterion.change ("emotion", "contemplative")
            $Asterion.change ("rightarm", "loose")
            $Asterion.change ("leftarm", "loose")
            show Asterion:
                xalign 0.5 yalign 1.0
            with Dissolve(1.0)
            "Minutos depois, ele retorna com sua lira. Ele olha para ela, depois para você por um segundo,
            e então cantarola para chamar uma porta para o alicerce."

            scene bg black
            with Dissolve(2.0)
            pause 2.0
            "Você deve fechar seus olhos e permitir-se ser guiado por Astério.
            E então, vocês dois seguem seu caminho para a bacia."
            $Asterion.change ("emotion", "neutral")
            scene Bedrock
            show Asterion:
                xalign 0.1 yalign 1.0
            with Dissolve(1.0)
            "Astério toma o máximo de cuidado para evitar que você se arranhe nas pedras roxas."

            $inventory.remove_item('Bundle')
            "O minotauro não quer que você fique lá por muito tempo — ele começa o ritual o mais rápido
            possível, invocando e derramando vinho na bacia."

            "Depois de limpar a mão, ele toca música. É uma tarefa mecânica, pulando de uma música para a outra sem nenhuma pausa para aproveitar o momento."

            $Asterion.change ("emotion", "bowing")
            asterion "Hermes Psicopompo, que nossa comunicação seja clara e nossas trocas justas."

            asterion "Que nossas orações sejam ouvidas e nossos insultos esquecidos."

            asterion "Que nossos jogos sejam agradáveis e nossos trabalhos recompensados."

            $Asterion.change ("emotion", "neutral")
            "O minotauro segura as cordas com os dedos, levanta, e coloca o caroço escuro na
            bacia. Sem hesitar, ele acende uma chama — e em segundos cresce o suficiente até
            quase tocar o teto."

            scene bg black
            with Dissolve(2.0)

            "Você e Astério retornam para o hotel no mesmo caminho que vieram, com seus olhos fechados
            e o minotauro segurando sua mão."


        elif BundleSacrifice == 'Hades':
            scene bg black
            with Dissolve(2.0)
            pause 2.0
            $Asterion.change ("emotion", "contemplative")
            $Asterion.change ("rightarm", "loose")
            $Asterion.change ("leftarm", "loose")
            scene asphodel1
            show Asterion:
                xalign 0.0 yalign 1.0
            with Dissolve(1.0)
            "Você e Astério vão para o jardim além do salão."

            "No meio de um campo de flores está a estátua,
            com o cachorro de três cabeças ao seu lado."

            "Hades pode ser o deus dos mortos, mas sua estátua não retrata a aura sinistra
            que se esperaria de tal posição."

            "Ele parece sério, firme, mas nem um pouco hostil ou maligno.{w=0.2} E Cérbero
            — não mais alto que seus joelhos — parece tão ansioso e feliz quanto qualquer cãozinho mortal."

            $Asterion.change ("emotion", "bowing")
            "Você e Astério atravessam o lago de flores. Conforme se aproximam, a marcha de Astério
            se altera — ele tenta exibir alguma forma de atração cerimonial, ficando em postura reta com os
            ombros puxados para trás."

            "Antes de começar o ritual, o minotauro faz questão de limpar as duas estátuas.
            Uma atenção especial vai para o cão — ele acaricia cada cabeça, uma por uma."

            "Depois de terminar, ele faz um gesto para você se aproximar."

            $Asterion.change ("emotion", "contemplative")
            $Asterion.change ("leftarm", "raised")
            asterion "Hades Chthonios, meu antigo general.{w=0.2}
            Muito tempo se passou desde a última vez que cuidei de seu santuário."

            asterion "Hoje viemos para demonstrar nosso respeito...{w=0.2} à pura Perséfone e a você."

            asterion "Para a mais bela das donzelas e para o guia dos destinos,{w=0.2}
            uma chama nascida de uma oferenda icorosa e perfumada com romãs."

            $Asterion.change ("emotion", "bowing")
            asterion "Rainha e rei do subterrâneo, condeda-nos sua orientação."

            $inventory.remove_item('Bundle')
            "O minotauro coloca a oferenda aos pés da estátua,
            coberta por uma pilha de romãs, e as incendeia.
            Em segundos, uma grande chama brota dela, soltando uma ondulante nuvem de fumaça pungente."

            "Você e Astério se afastam."

            $Asterion.change ("emotion", "contemplative")
            $Asterion.change ("leftarm", "loose")
            $Asterion.change ("rightarm", "hips")
            asterion "O hotel foi construído ao redor da estátua e da lareira.
            Há muito tempo, eu costumava vir sorrateiramente para cá — as criaturas deste domínio nunca gostaram deste lugar."

            asterion "A lareira naquela época não era nada mais que uma fogueira."

            asterion "Lorde Hades...{w=0.2} Depois da minha morte, fui enviado para o reino dele,
            como seria de se esperar.{w} Ele me levou para sua corte, digamos,
            e eventualmente me juntei à sua guarda."

            asterion "Hades era um monarca bom e justo.{w=0.2} Ele nunca aceitou oferendas —
            afinal, não deveria haver barganha alguma com o senhor dos mortos."

            asterion "Mas nós{w=0.2} que trabalhamos sob seu comando,{w=0.2}
            sabíamos que ele tinha uma queda por sua esposa.{w} A trazíamos frutas e flores para mantê-lo satisfeito."

            asterion "Fiz isto mais do que a maioria."

            scene bg black
            with Dissolve(2.0)

            "Você e Astério retornam para o Hotel."

        $obtain_reward('Wine', 'Exploration', subtract=False)
        scene bg black
        with Dissolve(2.0)

    else:
        hide Asterion
        with Dissolve (1.0)

    "Você passa o resto do dia sozinho, seguindo a rotina habitual.
    Você passa algum tempo cuidado da recepção, vai almoçar no salão e faz uma
    pausa à tarde nos aposentos do Mestre."

    scene bg black
    with Dissolve(1.0)
    "Eventualmente, chega a hora de verificar as duas equipes."

    #saved original exteam for later in case one of them gets injured
    $throwaway4 = exploration_team_names()

    $nextLabel = "day3_EOD"
    jump teamRewards
label day3_EOD:

    if not rewards.is_obtained('Wine'):
        #scene that plays if player hasn't obtained the wine through either legitimate mean
        $show_team(throwaway4)
        $pose_team(throwaway4, 'defeat')
        $throwaway2 = list_into_text(throwaway4 + ['you'])
        $throwaway3 = list_into_text(throwaway4)
        pause 2.0
        if len(throwaway4) >= 1:
            "Esta não é a notícia que você estava esperando."
        else:
            "Você não sabe o que estava esperando ao vir para cá."
        pause 2.0
        scene bg valley_exit
        with Dissolve(1.0)
        $show_team(throwaway4)
        $pose_team(throwaway4, 'neutral')
        with Dissolve(1.0)
        if len(throwaway4) > 1:
            "[throwaway2] caminha de volta para a caverna que leva à escadaria, um bem-vindo refúgio
            da intensa e implacável luz solar do vale."

            "Eles ficam para trás, descansando contra as paredes rochosas da caverna,
            recuperando-se da expedição."

            "Eles discutem a experiência com um tom despreocupado um tanto forçado. É evidente
            que eles estão tão decepcionados quanto você por não terem conseguido completar o sacrifício.
            Mas estão tentando tirar o melhor proveito da situação."

            "Você pergunta se eles precisam de companhia, mas eles insistem que você vá na frente. Tudo o que precisam
            é de alguns minutos para recuperar o fôlego e se refrescar na sombra antes de
            subir as escadas."

        elif len(throwaway4) == 1:
            "[throwaway2] caminha de volta para a caverna que leva à escadaria, um bem-vindo refúgio
            da intensa e implacável luz solar do vale."

            "Ele fica para trás, descansando contra as paredes rochosas da caverna, recuperando-se
            da expedição."

            "Você pergunta se ele precisa de companhia, mas ele insiste que você vá em frente.
            Tudo o que ele precisa é de alguns minutos para recuperar o fôlego e se refrescar na sombra
            antes de subir as escadas."

        else:
            "Você caminha de volta para a caverna que leva à escadaria, um bem-vindo refúgio
            da intensa e implacável luz solar do vale. Ainda não está anoitecendo e você
            ainda pode analisar suas opções antes de enfrentar a serpente."

        scene bg staircase
        with Dissolve(2.0)

        "Você sobe as escadas de volta à recepção."

        "Você começa em um ritmo decente, colocando um pé na frente do outro em um ritmo
        constante e mecânico, mas logo você começa a demorar em cada andar
        até um grau perceptível e preocupante."

        "Quando você menos percebe, está parado, na metade do caminho
        entre a entrada do vale e o andar térreo.
        Seus pés estão pesados, puxados pelo prospecto de admitir a derrota."

        "Depois de um minuto, sua decisão de continuar caminhando é esmagada pelo peso
        do pavor; você se senta para descansar."

        "Se você não vai sair de sua posição atual,
        nada mais justo que tornar sua estadia mais confortável."

        "Você olha para cima, não para a recepção, mas para os aposentos do Mestre. Você começa a
        analisar suas opções: Argos estaria disposto a aceitar mais barganhas?
        Que condições ele exigiria em troca da garrafa?"

        "Ou talvez haja uma lacuna que você não considerou, e ele nunca teve a intenção de lhe
        dar a garrafa em primeiro lugar."

        "Esta é outra possibilidade, talvez mais atraente e reconfortante, que o
        absolveria da culpa por seu fracasso."

        "Alguém anda atrás de você, mas você não reage. Você tem que pensar em uma maneira
        de sair disso, e está completamente focado em descobrir como."

        "Ou… precisa mesmo? Não é o fim do mundo, é? Astério disse que iria
        sarar de qualquer maneira, não é? Em suas próprias palavras,
        ele apenas levaria mais tempo para fazer isto."

        "A questão então é: quanto tempo? Levaria semanas, meses, anos?
        Ele passou décadas sujo, ferido e emaciado. Imortal ou não,
        é bastante coisa para se recuperar."

        "Seu otimismo momentâneo evapora. Tudo o que lhe resta é o silêncio
        das escadas e a luz solar chovendo de cima,
        a qual você pode dizer que mudou na direção de um tom mais vermelho."

        "Logo chegaria a hora de confrontar Argos e admitir a derrota. A cobra,
        você imagina, não desperdiçará a oportunidade de espremer um pouco mais de sofrimento de você."

        "Talvez ele quebre a garrafa bem diante de seus olhos,
        ou a desarrolhe de cima da estátua, fazendo sua própria libação
        para o solo ressecado que o gerou."

        "Talvez ele fizesse você convocar Astério para o vale em troca da garrafa
        para continuar brincando com você."

        "Isto é improdutivo. Chega de lamentação."

        "Você se levanta de volta. Dá seu primeiro passo para baixo. Depois outro."

        "O próximo passo exige um pouco mais de esforço, pois você considera abandonar
        completamente a ideia de se encontrar com Argos, já que não tem nada a ganhar com a troca.
        Mas você continua, de qualquer maneira."

        scene bg black
        with Dissolve(1.0)

        "Você ouve o som dos passos de outra pessoa, mas segue em frente com
        uma determinação obstinada, ignorando a distração, mesmo conforme
        ela fica cada vez mais alta em seus ouvidos."

        "Você simplesmente continua andando{nw}"

        scene bg staircase
        if first_guest == 'Luke':
            $throwaway1= False
            $Kota.change("emotion", "surprise")
            $Kota.change("rightarm", "raised")
            $Kota.change("leftarm", "raised")
            show KotaWound:
                xalign 0.5 xzoom -1 yalign 1.2
            show Kota behind KotaWound:
                xalign 0.5 xzoom -1 yalign 1.2
        else:
            $Luke.change("emotion", "surprise")
            $Luke.change("arm", "pointing")
            $Luke.change("bandanna", "False")
            show Luke:
                xalign 0.5 xzoom 1 yalign 1.2
        with Dissolve(0.1)


        if first_guest == 'Luke':
            play music "music/TheSorrow.ogg" fadeout 4.0 fadein 4.0

            kota "Ai! Senhor [player_name], por favor, tenha mais cuidado!"

            "Você abre seus olhos. Kota está parado diante de você, bem distante de sua
            aparência arrumada e bem cuidada de costume: ele está coberto de sujeira, seu kimono está rasgado
            e o tecido ao redor do ombro direito está escuro e ensanguentado."

            $Kota.change("rightarm", "relaxed")
            $Kota.change("leftarm", "relaxed")
            you "Kota, o que aconteceu? Você está bem?"

            $Kota.change("emotion", "puzzled")
            kota "S-sim, [player_name], ficarei bem. Não foi um corte profundo, felizmente."

            you "O que aconteceu?"

            show Kota:
                ease 1.0 yalign 3.0
            show KotaWound:
                ease 1.0 yalign 3.0
            pause 1.0
            hide Kota
            hide KotaWound
            with Dissolve(1.0)

            $Kota.change("clothes", "none")
            $Kota.change("fundoshi", "True")
            show KotaWound:
                yalign 3.0 xalign 0.5 xzoom -1
            show Kota behind KotaWound:
                yalign 3.0 xalign 0.5 xzoom -1
            with Dissolve(1.0)
            $Kota.change("emotion", "sad")
            "Kota se senta na escada, sem fôlego. Em seguida, ele remove
            e dobra seu kimono, revelando o ferimento em seu ombro.
            É um corte feio, mas não profundo o suficiente para causar preocupação."

            show KotaWound:
                ease 0.6 yalign 3.8 xalign 0.4
            show Kota:
                ease 0.6 yalign 3.8 xalign 0.4
            pause 0.6
            hide KotaWound
            with Dissolve(0.3)
            $throwaway1= True
            show Kota behind KotaWound:
                yalign 3.8 xalign 0.4 xzoom -1
            show KotaWound:
                xzoom -1 yalign 3.8 xalign 0.4
            with Dissolve(0.3)
            with Dissolve(0.5)
            show Kota:
                ease 0.6 yalign 3.0 xalign 0.5
            show KotaWound:
                ease 0.6 yalign 3.0 xalign 0.5

            play sound "sfx/clink.ogg"
            $Kota.change("emotion", "puzzled")
            "Kota coloca a trouxa de roupas na escada, depois pega a faixa obi que usa na cintura
            e a envolve no ombro como uma bandagem improvisada."

            you "Não se preocupe com isso, posso fazer o hotel invocar uma réplica."

            $Kota.change("emotion", "sad")
            $Kota.change("leftarm", "raised")
            kota "Agradeço, [player_name], mas prefiro costurar e lavar meu kimono
            a fazer uma réplica e descartá-lo. Essas roupas têm sido minhas companheiras
            de viagem há um tempo."

            $Kota.change("leftarm", "relaxed")
            show Kota:
                ease 0.6 yalign 3.8 xalign 0.4
                ease 0.6 yalign 3.0 xalign 0.5
            show KotaWound:
                ease 0.6 yalign 3.8 xalign 0.4
                ease 0.6 yalign 3.0 xalign 0.5
            "O dragão suspira e alcança a trouxa de roupas novamente.
            Ele puxa um grande objeto de dentro e entrega para você."

            show image "gui/inventory/icons/big/item_Wine Bottle.png":
                xalign 0.5
                yalign 0.4
            with Dissolve(1)

            $Kota.change("rightarm", "raised")
            kota "Acredito que isto seja para você."

            $Kota.change("rightarm", "relaxed")
            you "Que? Kota, como você conseguiu isso?"

            $inventory.remove_item("Bundle")
            $inventory.add_item("Wine Bottle")

            play sound "sfx/asterionchord.mp3"
            "Você obteve uma {color=[UIColorOrange]}garrafa de vinho{/color}."

            hide image "gui/inventory/icons/big/item_Wine Bottle.png"
            with Dissolve(1)

            $Kota.change("emotion", "neutral")
            $Kota.change("leftarm", "raised")
            kota "Ora, Argos, é claro. Pegar a garrafa à força não foi uma opção que
            avaliamos como possibilidade, ao que parece."

            $Kota.change("leftarm", "relaxed")
            you "Engraçado, não imaginava você como um lutador."

            $Kota.change("emotion", "laughing")
            kota "Você ficaria surpreso. Tempos desesperadores exigem medidas desesperadas."

            $Kota.change("emotion", "puzzled")
            show Kota:
                ease 0.2 yalign 2.2
                ease 0.4 yalign 3.0
            show KotaWound:
                ease 0.2 yalign 2.2
                ease 0.4 yalign 3.0
            "Você o ajuda a apertar a ferida."

            you "Devíamos dar uma olhada nisso. Acho que Ismael tem algum
            conhecimento de primeiros socorros— ou pelo menos é o que diz a Greta."

            $Kota.change("emotion", "sad")
            kota "Ah, não se preocupe. Eu curo muito rápido, e a ferida é superficial."

            you "Bem, se isso é obra do Argos, não sabemos se ele é venenoso—
            eu não correria o risco."

            $Kota.change("emotion", "happy")
            kota "Ah, não foi o Argos! Ele é… bem, ele é muitas coisas, isso eu digo
            a você, mas ele também é um late e não morde."

            kota "Ele queria barganhar pela garrafa no começo, me fazer assinar um contrato,
            sabe, o que se esperaria dele."

            $Kota.change("rightarm", "raised")
            kota "Então eu prometi um aperto de mão e o atrai para dentro. Enquanto ele estava fazendo, digamos,
            um discurso muito rude e arrogante, eu dei um soco, o atordoei e
            tentei prendê-lo com uma chave de braço. Ele gritou e começou a correr."

            $Kota.change("emotion", "laughing")
            kota "Eu fiz o mesmo— embora eu possa não ser muito rápido, ele parou
            por um segundo, o que me permitiu alcançá-lo. Foi quando ele jogou a
            garrafa para chamar minha atenção, consegui pegá-la enquanto ele fugia."

            $Kota.change("rightarm", "relaxed")
            $Kota.change("emotion", "sad")
            kota "Mas, infelizmente, foi quando percebi {i}por que{/i} ele parou.
            Uma daquelas… criaturas uivantes e sem pernas o pegou."

            you "Sim, uma dessas pulou em mim ontem."

            $Kota.change("emotion", "puzzled")
            kota "Coisinhas desagradáveis, sim. Então, já que Argos estava fora de cena,
            a atenção da criatura estava toda em mim e… bem, como eu disse. Não sou muito rápido."

            you "Merda, sinto muito, Kota."

            $Kota.change("emotion", "neutral")
            kota "Não sinta. Eu faria isto de novo e de novo por você e o senhor Astério."

            kota "Espero que você me perdoe se eu tirar o dia de folga amanhã, entretanto.
            Não demorarei para sarar de um arranhão como este, mas gostaria de descansar um pouco."

            if guests.get_guest_status('Kota') == 'unavailable':
                you "Você já não estava ferido por causa da exploração de ontem?"
                kota "Bem, sim. Acredito que vou demorar mais um dia que o esperado, então."
            else:
                you "Com certeza, Kota. Leve o tempo que precisar."
            $guests.disable_guest("Kota", days=1)

            show Kota:
                ease 1.0 yalign 1.0
            show KotaWound:
                ease 1.0 yalign 1.0
            "Você ajuda Kota a levantar e subir as escadas."

            hide Kota
            hide KotaWound
            with Dissolve(1.0)

            show KotaWound:
                xalign 0.5 xzoom 1 yalign 1.0
                ease 0.2 yalign 1.0
                pause 0.06
                ease 0.2 yalign 1.2
                pause 1.0
                repeat
            show Kota behind KotaWound:
                xalign 0.5 xzoom 1 yalign 1.0
                ease 0.2 yalign 1.0
                pause 0.06
                ease 0.2 yalign 1.2
                pause 1.0
                repeat
            with Dissolve(1.0)
            "Nenhuma quantidade de insistência o convence a checar com Ismael.
            Você abandona o assunto antes que ele fique irritado com você."

            show KotaWound:
                xalign 0.5 yalign 1.0
            show Kota behind KotaWound:
                xalign 0.5 yalign 1.0

            you "Mais uma vez, obrigado, Kota."

            $Kota.change("emotion", "laughing")
            $Kota.change("rightarm", "raised")

            kota "Por favor. É o mínimo que posso fazer por sua hospitalidade. Cuide-se."

            $Kota.change("rightarm", "relaxed")
            show KotaWound:
                ease 0.5 yalign 1.8
                pause 0.5
                ease 0.5 yalign 1.0
            show Kota:
                ease 0.5 yalign 1.8
                pause 0.5
                ease 0.5 yalign 1.0
            pause 1.5
            hide Kota
            hide KotaWound
            with Dissolve(1.0)
            "Kota se curva e se dirige para o próprio quarto, deixando você sozinho para subir os andares
            restantes até os aposentos do Mestre."

        else:
            play music "music/Solidarity.ogg" fadeout 1.0 fadein 1.0
            luke "AI! Mas que porra, [player_name], olha por onde anda!"

            $Luke.change("arm", "hip")
            "Você abre os olhos. É o Luke. Seus olhos estão mais arregalados do que você já viu antes.
            Ele está tremendo e sem fôlego, e faltando algumas penas por todo o corpo,
            ao ponto de você conseguir enxergar a vermelhidão da pele abaixo."

            you "Luke, você está bem?"

            $Luke.change("emotion", "crying")
            show Luke:
                ease 0.5 yalign 1.8
                pause 1.0
                ease 0.2 yalign 1.4
                ease 0.2 yalign 1.8
                ease 0.2 yalign 1.4
                ease 0.2 yalign 1.8
            "Luke se curva e tosse. O som é rouco e áspero, seguido por uma respiração ofegante
            e ruidosa. Ele, evidentemente, não está bem."

            $Luke.change("emotion", "annoyed")
            show Luke:
                ease 1.0 yalign 1.2 xalign 0.6
            "Ele se levanta e se inclina na grade. Você diz a ele que esta é uma ideia
            terrível e o instrui a se sentar na escada."

            luke "Cuidado, chefe. Se eu sentar, vou acabar quebrando {i}isso{/i}."

            $Luke.change("arm", "pointing")
            "Luke puxa algo de trás e dá para você."

            show image "gui/inventory/icons/big/item_Wine Bottle.png":
                xalign 0.5
                yalign 0.4
            with Dissolve(1)

            you "Luke, que porra é essa? Como você conseguiu isso?"

            $inventory.remove_item("Bundle")
            $inventory.add_item("Wine Bottle")

            play sound "sfx/asterionchord.mp3"
            "Você obteve uma {color=[UIColorOrange]}garrafa de vinho{/color}."

            hide image "gui/inventory/icons/big/item_Wine Bottle.png"
            with Dissolve(1)

            show Luke:
                ease 1.0 xalign 0.5 yalign 2.0

            $Luke.change("arm", "hip")
            "Luke se joga na escada e se inclina para trás, tentando recuperar o fôlego."

            $Luke.change("emotion", "cocky")

            luke "Quer ver se consegue adivinhar?"

            you "Luke, o que você fez?"

            $Luke.change("emotion", "annoyed")
            luke "Sabe, aquele cobra lá realmente se acha a última bolacha do pacote.
            Ele se acha o gostosão, não é? Deixa eu te contar: ele não é."

            $Luke.change("arm", "pointing")
            luke "Ele tem uma visão de merda, para começar. Não quero me gabar, mas eu sou metade águia-careca,
            consigo enxergar uma cobra rastejando por aí de {i}muito{/i} longe.
            E ele nem me viu chegando de fininho."

            $Luke.change("arm", "hip")
            luke "Então eu agarrei o filho da puta por trás, prendi os braços dele atrás das costas
            e empurrei ele no chão. Não foi minha primeira vez— eu sou bom no que eu faço.
            Imobilizei ele antes mesmo dele perceber o que tava acontecendo."

            $Luke.change("emotion", "surprise")
            "Luke faz uma pausa para recuperar o fôlego."

            $Luke.change("emotion", "neutral")
            luke "Então eu perguntei pro babaca onde que tava a garrafa. Ele choramingou que
            nem uma puta antes de admitir, tava escondido naquela capa dele.
            Eu comecei a apalpar e adivinha, tava lá mesmo."

            luke "Eu peguei a garrafa e antes que eu percebesse, bem…"

            $Luke.change("emotion", "annoyed")
            "Luke para, engole em seco e continua respirando pesadamente."

            luke "Bem, eu não contava com o fato dele ter uma cauda, então, antes que eu percebesse,
            aquela merda tava em volta do meu pescoço me empurrando pra trás e apertando, com força."

            $Luke.change("emotion", "laughing")
            show Luke:
                ease 0.3 yalign 1.8
                ease 0.3 yalign 2.0
            luke "Haha, com muita força."

            $Luke.change("emotion", "neutral")
            $Luke.change("arm", "pointing")
            luke "Mas, sim. Deixa eu te contar, [player_name], eu sou difícil de derrubar,
            já passei por muita coisa. Se cair dentro, eu aguento. Já fui socado,
            esfaqueado, baleado, explodido e vivi pra contar a história."

            $Luke.change("emotion", "annoyed")
            $Luke.change("arm", "hip")
            luke "Mas eu, é...{w=0.2} sabe aqueles caras que ficam com tesão sendo
            estrangulados e desmaiando? Eu sou o oposto disso."

            luke "Só de tocar meu pescoço eu já fico surtado, e..."

            luke "Eu quase morri de tanto guinchar, mas mantive a calma porque, sabe,
            se eu quebrasse a garrafa, teria sido tudo em vão."

            luke "Foi aí que as garras saíram, e meu filho, se você acha que eu tô todo lascado,
            devia ver como ele tá agora."

            show Luke:
                ease 1.0 yalign 1.6
            "Luke senta direito."

            $Luke.change("emotion", "neutral")
            luke "Então, tá aí."

            you "Luke, vamos para o salão— você precisa pelo menos de um copo
            d'água. Talvez possamos perguntar por aí e ver se algum dos hóspedes pode tratar {nw}"

            $Luke.change("emotion", "happy")
            luke "[player_name]. Relaxa. Eu vou ficar bem."

            $Luke.change("emotion", "surprise")
            show Luke:
                ease 0.3 yalign 1.3
                ease 0.3 yalign 1.6
            pause 1.0
            $Luke.change("emotion", "wink")

            luke "E pode apostar que eu quero ir pro salão e tomar uma bebida,
            mas não tenho certeza se é água que eu prefiro no momento."

            $Luke.change("emotion", "cocky")
            luke "Espero que você não se importe se eu tirar um dia de folga amanhã. Ainda tô um pouco
            surtado, sabe?"

            if guests.get_guest_status('Luke') == 'unavailable':
                you "Você já não estava ferido por causa da exploração de ontem?"
                luke "Sim, talvez tenha sido idiota da minha parte tentar fazer isso...
                {w=0.2}Mas não se pode discutir os resultados, não é? Vou tirar {i}mais um{/i} dia de folga, então."
            else:
                you "Claro, Luke, leve todo o tempo que precisar. Isso foi incrível, obrigado."
            $guests.disable_guest("Luke", days=1)

            $Luke.change("emotion", "wink")
            $Luke.change("arm", "pointing")
            luke "Ei, qualquer coisa por você e pelo Astério, parceiro."
            show Luke:
                ease 1.0 yalign 1.0
            $Luke.change("arm", "hip")
            pause 1.0
            $Luke.change("emotion", "happy")
            "Você ajuda o grifo a se levantar. Ele te dá um largo sorriso."

            luke "Tô de boa, [player_name], falo sério. Agora vai lá fazer um brinde,
            ou sejá lá pra que você quer esse vinho, tá?"

            hide Luke
            with Dissolve(1.0)
            pause 1.0
            $Luke.change("emotion", "laughing")
            show Luke:
                xalign 0.5 xzoom -1 yalign 1.0
                ease 0.2 yalign 1.0
                pause 0.06
                ease 0.2 yalign 1.1
                pause 1.0
                repeat
            with Dissolve(1.0)
            "Luke e você sobem a escada juntos. Você tenta colocar um braço em volta do ombro dele,
            mas ele recusa, chama você de idiota e ri, antes de tossir novamente."

            hide Luke
            with Dissolve(1.0)

            $Luke.change("emotion", "wink")
            $Luke.change("arm", "salute")
            show Luke:
                xalign 0.5 yalign 1.0
            with Dissolve(1.0)

            "Quando você chega ao térreo, Luke caminha em direção à recepção, mas se vira
            para saudá-lo. Você retribui o gesto em consideração e sobe as escadas
            em direção aos aposentos do Mestre."

        $obtain_reward('Wine', 'Exploration', subtract=False)
        $add_file('Artifact', "Wine")
        $BundleSacrifice = 'Force'

    else:
        scene bg black
        with Dissolve(1.0)

        pause 1.0

        play music "music/MayItBegin_Full.ogg" fadeout 4.0 fadein 4.0

        scene bg valleysundown
        with Dissolve(2.0)

        #if the player did obtain the bottle, either by themselves or by sending guests out
        #this is the scene where Argos gives you the bottle.

        "As sombras do vale rastejam até a entrada do hotel. Elas se estendem das colinas
        e penhascos à frente dos arbustos e árvores mais à frente na ladeira."

        "Elas se misturam em um labirinto de sombras, rastejando e aproximando
        o caminho até seus pés."

        "Se você pudesse montar nesses tentáculos de escuridão — seguir a sombra de um galho
        até a das rochas salientes ao lado dele e, em seguida, pular para a sombra imponente do grande penhasco —
        descobriria que estão todas conectadas."

        "O labirinto está nas sombras rastejantes, no leito dos rios sinuosos,
        nas vastas redes de terra rachada que se estendem até o horizonte."

        "E, por baixo de tudo, há uma agitação — algo despertando, atraído por sua
        existência, a existência de seu Mestre."

        "Quando você para e planta os pés no chão, é mais fácil perceber.
        Um zumbido maçante que vai e vem, grave e lento."

        "E então,{w=0.2} um estalo.{w} Um galho seco quebra, seguido por uma massa cinza
        movendo-se sob as artemísias."

        $Argos.change("emotion", "neutral")
        $Argos.change("pose", "crossed")

        show Argos:
            xalign 0.5 yalign 1.0 xzoom 1 zoom 1.0
        with Dissolve(1.0)

        "Argos se revela."

        you "Você está um pouco atrasado."

        $Argos.change("emotion", "smug")

        argos "Sinto muito, meu senhor.{w=0.2} Veja bem, eu estava apenas fazendo minhas rondas,
        cuidando de meus lindos jardins."

        argos "Mas estou aqui, afinal.{w=0.2} Está ficando tarde,
        então que tal não perdermos tempo e irmos direto ao assunto?"

        if BundleSacrifice in ["Zeus", "Athena"]:

            $Argos.change("emotion", "cocky")

            argos "Eu estava observando, sabe.{w=0.2} Segui sua expedição no caminho
            para o planalto — precisava ter certeza de que chegaria são e salva, veja bem."

            $Argos.change("emotion", "smug")

            if BundleSacrifice == 'Athena':
                argos "E eu vi com meus próprios olhos, que lindo sacrifício para a
                Atena de olhos brilhantes.{w=0.2} Que disposição devota nos dias de hoje!"

                argos "A sábia deusa ficará revigorada com sua oferenda.
                Seu antigo coração baterá com tal força juvenil!"

            else:
                argos "E eu vi com meus próprios olhos, que lindo sacrifício para o Zeus Areios.{w=0.2}
                Que disposição devota nos dias de hoje!"

                argos "O Rei dos Deuses certamente ficará revigorado com sua oferenda.
                Ah, que raio poderoso ele ordenará, a humanidade ouvirá sua estrondosa voz
                mais uma vez!"

            show image "gui/inventory/icons/big/item_Wine Bottle.png":
                xalign 0.5
                yalign 0.4
            with Dissolve(1)

            $Argos.change("emotion", "neutral")
            $Argos.change("pose", "straight")
            argos "Bem, eu sou uma cobra de palavra.{w=0.2} Aqui está o vinho — o com propriedades curativas,
            é claro.{w=0.2} Em um piscar de olhos, deverá sarar as feridas do bezerro."

            "A cobra lhe entrega a garrafa de vinho."

            $inventory.add_item("Wine Bottle")
            $add_file('Artifact', "Wine")

            play sound "sfx/asterionchord.mp3"
            "Você obtém uma {color=[UIColorOrange]}garrafa de vinho{/color}."

            hide image "gui/inventory/icons/big/item_Wine Bottle.png"
            with Dissolve(1)

            pause 1.0

            you "Obrigado, Argos.{w=0.2} Você pode ser uma cobra traiçoeira, mas tem integridade, eu suponho."

            $Argos.change("pose", "crossed")
            argos "Ah, que acervo de elogios!{w=0.2} Estou feliz que o Mestre estime
            este humilde servo."

            $Argos.change("emotion", "smug")
            argos "Entretanto, por mais que alegre meu espírito ouvir suas doces palavras...{w=0.2}
            Presumo que você tenha seus deveres a cumprir, não é mesmo?"

            $Argos.change("emotion", "cocky")
            argos "Vá, meu senhor.{w=0.2} E preste atenção no vale, em seus sons —
            eu o chamarei novamente com minha flauta quando chegar a hora."

        else:
            #if player sacrificed the thing to Hades/Hermes/Hestia
            $Argos.change("emotion", "cocky")
            argos "Bem... receio não ter visto ninguém subindo ao planalto para fazer uma oferenda."

            argos "Diga-me, meu bom senhor, o que aconteceu?{w=0.2} Você tem força de sobra
            e há um hotel inteiro repleto de pessoas que você poderia usar para seus objetivos."

            $Argos.change("emotion", "smug")
            argos "O que o fez falhar em uma tarefa tão simples?"

            $Argos.change("emotion", "neutral")
            you "Bem, não acho que eu falhei de forma alguma.{w=0.2} Sabe, eu estava pensando
            na nossa pequena conversa outro dia."

            you "Me lembro de você falando que qualquer santuário divino serviria.{w=0.2}
            Não está certo?"

            $Argos.change("emotion", "cocky")

            argos "Está correto, qualquer um dos santuários serviria.{w=0.2}
            Mas, ah, para onde nosso bom senhor poderia estar indo com isto?"

            you "Eu cumpri a missão, é claro.{w=0.2} Mas acontece que eu fiz
            a oferenda para {i}outro{/i} santuário, um dentro do hotel."

            $Argos.change("emotion", "neutral")
            if BundleSacrifice == 'Hades':
                you "Tem uma estátua do antigo deus dos mortos, Hades,
                a qual Astério me disse que data da criação do domínio.{w=0.2}
                Nós queimamos a oferenda a seus pés."

            elif BundleSacrifice == 'Héstia':
                you "Tem a lareira, iluminada por aquele espelho sagrado.{w=0.2}
                Não é o santuário de Héstia? Queimamos a oferenda na fogueira
                e agora ela está mais brilhante do que nunca."

            else:
                you "Tem uma sala que abriga uma bacia, Astério me disse ser um antigo
                santuário para Hermes.{w=0.2} Nós queimamos a oferenda nela."

            you "Então...{w=0.2} eu cumpri minha parte no acordo, Argos."

            $Argos.change("emotion", "surprised")
            $Argos.change("pose", "straight")
            you "Uma oferenda a um dos santuários divinos, assim como você instruiu.
            {w=0.2}Agora é sua vez."

            pause 1.0

            if TimesSent == 0 and (ArgosContract == 'Tricked' or (ArgosContract == "Contested" and contestContract == '4')):
                $Argos.change("pose", "crossed")

                show Argos:
                    ease 0.5 xalign 0.55 zoom 0.96
                    ease 0.5 xalign 0.45 zoom 0.91
                    ease 0.5 xalign 0.5 zoom 0.85

                "A cobra desliza enquanto mantém o olhar fixo em você. Ele coça
                a cabeça — primeiro sobre a pele que usa como capa, depois com as duas mãos embaixo dela."

                $Argos.change("emotion", "angry")
                "Sua língua entra e sai de sua boca, culminando com ele, curvando-se
                como se estivesse consumido por náusea. Mas quando ele olha para você novamente..."

                $Argos.change("emotion", "smug")

                "...Parece não ter se incomodado com o que você acabou de dizer, ou talvez..."

                $Argos.change("emotion", "cocky")

                "...esteja até alegre."

                show Argos:
                    ease 0.5 xalign 0.52
                    ease 0.5 xalign 0.48
                    repeat

                "Ele solta um gemido agudo — você precisa forçar sua audição para captá-lo.{w=0.2}
                Mas ele oscila para os lados até cair em risadinhas abafadas,
                como as cordas de uma harpa docemente tocadas."

                play music "music/MayItBegin_Acoustic.ogg" fadein 2.0 fadeout 2.0

                $Argos.change("emotion", "laughing")
                "De uma vez só, as cordas estalam; numa explosão, a risada de Argos se espalha pelo
                extenso vale e subindo até as escadas do hotel."

                "Ele surfa ondas — de uma risadinha escapando de sua mandíbula a um berro estridente que o faz
                curvar para trás — até que ele recupera compostura o suficiente para demonstrar uma reação adequada."

                $Argos.change("pose", "straight")
                show Argos:
                    ease 0.3 xalign 0.55 zoom 0.91
                    ease 0.3 xalign 0.45 zoom 0.96
                    ease 0.3 xalign 0.55 zoom 1.0
                    ease 0.3 xalign 0.5 zoom 1.1
                "Em um piscar de olhos, ele avança em você com os braços bem abertos. Você sente a
                cauda dele enrolando em torno de você por trás assim que ele faz contato físico."

                "Você se prepara para lutar por sua preciosa vida e, de fato, chega ao ponto de
                lançar seu punho para trás em preparação para socá-lo no rosto."

                pause 1.0

                "Mas algo parece estranho{w} — ele não está {i}apertando{/i} você."

                "Argos está lhe dando...{w=0.2} {i}um abraço.{/i}"

                argos "Pelos doze,{w=0.3} você será o melhor mestre que este vale já viu!"

                argos "Quem sabe quantas gerações de mestres humanos ao longo dos séculos..."

                argos "Ricos e pobres, estúpidos e inteligentes, miseráveis e heróicos..."

                "O abraço de Argos se aperta em torno de você, forçando o ar de seus pulmões para fora.
                Pareceria que ele está tentando sufocar você,
                se não estivesse enterrando o focinho em sua camisa como um cachorrinho."

                $Argos.change("emotion", "smug")

                argos "E pensar que eu, em toda a linhagem de Argos, terei a honra
                de servir ao maior mestre de todos os tempos!"

                argos "Você é uma cobra, sim, você é,{w=0.2} tão elegante e traiçoeiro como nós."

                $Argos.change("emotion", "sad")

                "Quando ele olha para você com um sorriso radiante, você não consegue deixar de notar
                que há um fio de ranho escorrendo pelo focinho dele, quase pingando em sua camisa."

                argos "Que privilégio nascer em tal época— para servir alguém como você."

                you "Ok, Argos, é muito gentil de sua parte.{w=0.2} Você é um bom menino, agora, pode me soltar?"

                $Argos.change("pose", "crossed")

                show Argos:
                    ease 1.0 zoom 1.0
                "Ele solta você e desliza de volta a uma distância respeitosa."

                $Argos.change("emotion", "cocky")

                argos "Eu sou?!{w=0.2} Bem, é claro que sou! Afinal, não há seguidor mais leal do que eu!"

                you "Não sei não, hein.{w=0.2} Astério tem uma ótima vantagem inicial, you'll
                have to step it up if you want to be number one."

                $Argos.change("emotion", "sad")

                argos "St{w=0.2}-step it up?{w} B-but I have neither legs nor feet — I can only slither..."

                argos "Você não pode por favor fazer uma exceção para mim?"

                you "I am afraid I can't, lowering my standards is unacceptable.{w=0.2}
                Let's be honest... if I'm not strict, how could I ever look you in the eyes and say anyone is number one?"

                $Argos.change("emotion", "smug")
                argos "Suponho que esteja certo...{w=0.2} Bem, então terei apenas que mostrar a você o quão
                melhor eu sou que o Astério."

                you "Você é bem-vindo para tentar."

                $Argos.change("emotion", "cocky")

                argos "Aposto que ele não consegue subir em árvores e estátuas como eu, não com aqueles cascos!{w=0.2}
                E com aqueles lábios dele, não há como ele tocar uma flauta."

                "Ele leva a flauta à boca novamente, mas você afasta o bocal
                e o segura no ar."

                $Argos.change("emotion", "sad")
                "Ele ainda consegue assoprar uma vez antes disso."

                you "Ele consegue tocar uma lira e cozinha muito bem."

                $Argos.change("emotion", "smug")

                argos "Bah!{w=0.3} Inútil, inútil!{w=0.2} Por que se preocupar com algo tão trivial como
                cozinhar quando você pode simplesmente invocar um pedaço de carne crua e se deliciar com ele?{w=0.2}
                O fogo apenas remove o sabor."

                you "Não sei, isso soa muito como uma coisa de cobra para o meu gosto."

                argos "Aww, será que meu mestre traiçoeiro não compartilha do nosso gosto
                por carne fresca?{w=0.2} Que decepção."

                argos "Embora eu suponha que você já seja perfeito o suficiente."

                "O anoitecer caiu conforme seu pequeno encontro progredia. Agora está tão escuro que você não
                consegue distinguir a forma geral da cobra na escuridão."

                "Ele percebe você deixando os olhos entreabertos."

                $Argos.change("emotion", "neutral")

                argos "Bem, está ficando tarde e os perigos do vale não são motivo de riso.{w=0.2} Seria rude
                e irresponsável de minha parte mantê-lo aqui por mais tempo."

                show image "gui/inventory/icons/big/item_Wine Bottle.png":
                    xalign 0.5
                    yalign 0.4
                with Dissolve(1)

                $Argos.change("emotion", "neutral")
                $Argos.change("pose", "straight")

                argos "Aqui, como prometi.{w=0.2} Uma garrafa do vinho curativo do vale,
                colhido em sua homenagem, em troca de uma demonstração da devoção do mestre."

                argos "É com grande honra e alegria que cumpro a minha parte do trato."

                show Argos:
                    ease 0.5 yalign 1.2
                    ease 0.5 yalign 1.0

                "Com uma reverência elaborada demais para não ser ensaiada em suas horas vagas,
                Argos entrega a garrafa de vinho."

                $inventory.add_item("Wine Bottle")
                $add_file('Artifact', "Wine")

                play sound "sfx/asterionchord.mp3"
                "Você obteve uma {color=[UIColorOrange]}garrafa de vinho{/color}."

                hide image "gui/inventory/icons/big/item_Wine Bottle.png"
                with Dissolve(1)

                pause 1.0

                you "Obrigado.{w=0.2} Fico feliz que você seja uma cobra tão honesta, sempre cumprindo suas promessas."

                $Argos.change("emotion", "smug")
                $Argos.change("pose", "crossed")

                argos "Isto, gostaria que você soubesse, não é nada menos que meu dever.{w=0.2}
                Eu não valeria minha própria pele se fosse um mentiroso descuidado."

                $Argos.change("emotion", "laughing")
                argos "Estou ansioso pelo nosso próximo encontro, bom Mestre.{w=0.2}
                Fique tranquilo, pois mais uma vez tentarei enganá-lo, esperando
                que sua inteligência saia vitoriosa.{w=0.2} Assim como nas lendas!"

                hide Argos
                with Dissolve(2.0)

                "Você volta para cima, ansioso pela calorosa luz do hotel novamente.{w=0.2}
                Um sorriso é pintado em seu rosto, o qual só fica maior quando você ouve a flauta de Argos
                se elevando em uma melodia alegre e distante."

            else:
                pause 2.0
                $Argos.change("emotion", "sad")
                argos "Como é?{w=0.2} Você pode repetir isto?"

                you "Eu fiz um sacrifício, sim — mas no conforto do meu hotel, e para
                [BundleSacrifice].{w=0.2} Você está ficando surdo, devo repetir mais uma vez?"

                pause 1.0

                $Argos.change("emotion", "angry")
                "O olhar da cobra oscila conforme ele mergulha em pensamentos.{w=0.2} Ele olha para o oeste,
                para o planalto agora escuro, depois para o hotel."

                "Seus lábios movem como se contando, ou listando os nomes dos deuses."

                $Argos.change("emotion", "sad")
                argos "Não..."

                pause 3.0

                $Argos.change("emotion", "neutral")
                $Argos.change("pose", "crossed")

                show image "gui/inventory/icons/big/item_Wine Bottle.png":
                    xalign 0.5
                    yalign 0.4
                with Dissolve(1)

                argos "Bem, eu sou uma cobra de palavra.{w=0.2} Aqui está o vinho{w=0.2}
                — o com propriedades curativas, é claro. Em um piscar de olhos,
                deve sarar as feridas do bezerro."

                "A cobra lhe entrega a garrafa de vinho."

                $inventory.add_item("Wine Bottle")
                $add_file('Artifact', "Wine")

                play sound "sfx/asterionchord.mp3"
                "Você obteve uma {color=[UIColorOrange]}garrafa de vinho{/color}."

                hide image "gui/inventory/icons/big/item_Wine Bottle.png"
                with Dissolve(1)

                pause 1.0

                you "Obrigado, Argos.{w=0.2} Você pode ser uma cobra traiçoeira,
                mas tem integridade, eu suponho."

                $Argos.change("pose", "crossed")
                argos "Ah, que acervo de elogios!{w=0.2} Estou feliz que o Mestre
                estime este humilde servo."

                argos "Gostaria que você soubesse que seria uma grande vergonha para alguém como eu,
                uma cobra do labirinto, não cumprir minha promessa."

                argos "Sempre fomos cuidadosos com nossas palavras, entende?{w=0.2}
                Nada nos escapa."

                $Argos.change("emotion", "smug")
                argos "Entretanto, por mais que alegre meu espírito ouvir suas doces palavras...{w=0.2}
                Presumo que você tenha seus deveres a cumprir, não é mesmo?"

                $Argos.change("emotion", "cocky")
                argos "Vá, meu senhor.{w=0.2} E preste atenção no vale, em seus sons —
                eu o chamarei novamente com minha flauta quando chegar a hora."

    scene bg black
    with Dissolve(2.0)

    #Either way, at this point you have the bottle for asterion and the teams are done.
    #Asterion introspection scene

    if TimesSent == 0:
        #this only plays if the MC never sent Asterion to the valley
        play music "music/asterion.ogg" fadeout 1.0 fadein 1.0
        pause 4.0

        "Havia algo nos olhos de Clément: uma faísca oscilante. Percebi isto
        anos antes de ele se tornar o mestre."

        "A vi com muita frequência ao longo dos séculos,{w=0.4} desde que José lavou os
        rios do vale pela primeira vez.{w} Uma coisa tão humana,{w=0.4} aquela chama."

        "Ela deseja glória,{w=0.4} procura queimar cada vez mais brilhante para que olhos sejam
        atraídos à sua luz.{w} E para este fim, desempenhará o papel de bom samaritano."

        "Se vestirá com os finos tecidos da nobreza,{w=0.4} colorirá seus dedos
        com anéis polidos e pedras preciosas brilhantes,{w=0.4} andará com aquela marcha
        de ombros e passos largos."

        "Eles,{w=0.4} os mestres da antiguidade,{w=0.4} estenderiam uma mão transbordando de riqueza —
        {w=0.4} toda a riqueza que para eles veio com o cantarolar de uma música —{w=0.4} e sorririam
        ao ver como as massas os consideravam poderosos."

        "Todos os olhos em seus rostos.{w=0.4} Todos os hóspedes e almas nesta terra.{w=0.4}
        Todos transbordando de amor e respeito."

        "Era isto que Clément queria e, para tal, ele jogou o mesmo jogo que Jean-Marie.{w=0.4}
        Mas havia uma diferença.{w=0.4} Nem todos os homens são feitos do mesmo tecido."

        "Aquelas chamas queimando em seus peitos,{w=0.4} não poderiam ser mais diferentes."

        "Jean-Marie teve uma visão.{w=0.3} Ele tinha visto a dor;{w=0.4} ela havia rastejado para dentro de seu peito,
        cavado um buraco em seu coração e se enrolado dentro dele."

        "Quando ele olhava para os hóspedes,{w=0.4} membros faltando e com os olhos vidrados daquela velha guerra,
        {w=0.4} seu rosto se contraía enquanto seu coração batia forte."

        "Nunca parava de doer; não enquanto ele estivesse aqui, e não até que seu coração
        parasse de bater. Eu sei disso, com tanta certeza quanto me conheço."

        "Clément queria adoração, Jean-Marie tinha uma visão.{w=0.4} Não houvesse olhos neste mundo,
        o bom mestre teria feito tudo da mesma forma, sabendo bem que cair na obscuridade não
        era problema de forma alguma."

        pause 3.0

        "Velho amigo...{w=0.5}quem é este mestre que agora reina sobre nós?"

        "Eu me pergunto...{w=0.3} Que chama se esconde dentro de seu peito?"

        "Qual é a pegadinha?{w=0.3} Por que um mestre,{w=0.5} livre de qualquer algema que possa
        limitar um mortal,{w=0.5} olharia para nós e nos consideraria dignos de seu esforço?"

        "Ele agora sabe como fazer chover diamantes na palma de sua mão.{w=0.3} Comida e abrigo
        nunca mais serão um problema para ele,{w=0.2} e companhia será abundante à medida que os hóspedes
        se aglomerem para expressar sua gratidão."

        "Ele aprecia as artes?{w=0.3} Se sim, seus artistas favoritos podem vir e produzir para ele,
        {w=0.3}até que se sinta satisfeito."

        "As ciências?{w} Traga seus acadêmicos,{w=0.3} ensine-os como gerar todos os materiais
        que desejarem,{w=0.3} e quaisquer mistérios que o corroem serão quebrados em pedaços."

        "Dinheiro?{w=0.2} O mais fácil de todos,{w=0.5} mas podemos nos perguntar para que serve dinheiro
        em um domínio sem escassez.{w=0.5} Qualquer coisa que ele possa descrever pode ser criada
        com o cantarolar de uma música."

        "O que é este mestre?{w=0.2} Que homem ele é?..."

        "...por que ele olha para mim assim?..."

        "...por que ele se esforçou para me trazer o vinho?..."

        "...qual é a pegadinha?..."

        #current affection max is 9.5 (10 if your bg is speedrunner or art)
        if global_affection > 7.5:

            pause 1.0

            "...por que ele olha para mim{w=0.5} {i}assim?...{/i}"

            pause 1.0

        "Ele não enxerga o que eu sou?{w=0.3} Que ele pode fazer o que quiser comigo,{w=0.5}
        ou ignorar minha existência por completo enquanto desfruta de todos os prazeres terrenos
        que esta terra lhe proporciona?"

        "Talvez ele ainda não tenha percebido.{w=0.5} Certamente perceberá, no devido tempo.
        E então será como os mestres anteriores, quando eles também entenderam
        que eu poderia ser jogado de lado."

        "Sessenta anos esgueirando-se nas sombras,{w=0.3} fingindo que eu não existo,
        {w=0.3} tentando não incomodá-los.{w} Fazendo o meu melhor para que todos esqueçam que eu existo."

        if global_affection > 7.5:

            pause 2.0
            "...Qualquer bem que possa haver para alguém como eu, maior infortúnio se segue.{w=0.3}
            Não demorará muito para que ele perceba o que eu sou."
            "Que eu sou uma besta estúpida, que eu não serei bom o suficiente para entretê-lo por muito tempo.{w=0.2}
            Tudo o que posso pedir é que ele me deixe em paz."

            pause 2.0

            "Mas por que ele olha para mim assim?"

            if Promise_Valley == "True":
                "Por que ele prometeu não me enviar para o vale?{w} Uma promessa que não pode ser
                forçada, mas...{w=0.3} mesmo assim, foi mantida."

            #if asterion did not panic
            if ArgosContract != "Terrorized":
                "Por que ele, na frente dos hóspedes, {i}me{/i} chamou de parceiro de negócios?{w}
                Pelos doze...{w=0.3} para sequer dar tanto crédito a um escravo..."

            "Por que ele{w=0.3} me tocou?"

            "Por que ele perde seu tempo me entretendo?{w=0.3} Qual é o objetivo dele
            compartilhando uma refeição comigo?"

            pause 2.0

            "A maneira como ele olha para mim..."
            pause 1.0
            "Pelos deuses, parece que ele está mais cuidando de mim que eu o servindo."

            pause 1.0

            "Quando ele segurou minha mão..."
            pause 1.0
            "Deve...{w=0.3} deve haver uma pegadinha."

            "Mas a maneira como ele olha para mim...{w=0.3} Eu posso...{w=0.3} é sequer permitido que eu...?"

        else:
            pause 1.0

            "Mas não seria o melhor?{w=0.3} Quanto maior a distância entre nós
            dois, menos provável que ele veja como eu sou."

            "Podemos encontrar normalidade nisto, e entre os hóspedes e funcionários posso
            desfrutar de algo próximo ao que os vivos têm."

            "Isto, por si só, é motivo de regozijo.{w=0.3} Já estou evitando o destino
            que os deuses escolheram para mim."

            "Isto é mais do que um desgraçado como eu poderia merecer.{w=0.3}
            Ser um híbrido é razão suficiente para a danação, mas o que eu fiz..."

            "O que me tornei...{w=0.3} O que permiti..."

            "Talvez, com este mestre, eu tenha um período de paz.{w=0.3} Se ao menos ele
            não compreender o que eu sou."

            pause 2.0

            "Mas...{w=0.3} por que?{w=0.3} Por que ele se esforçou tanto para me trazer o vinho?{w}
            Que diferença isto faz para ele?"

            pause 1.0

    else:
        $renpy.music.set_volume(0.8, delay=1, channel='music')
        #if asterion has been sent at least once
        play music "music/RedDistortion.ogg" fadeout 2.0 fadein 2.0
        pause 4.0
        "Há{w=0.5} um atraso,{w=0.3} ele percebe."
        pause 1.0
        "Mesmo que nenhuma palavra passe por sua mente,{w=0.5} ele sabe."
        "O indicador do minotaro repousa sobre as cordas da lira,{w=0.5} dedilhando para cima e para baixo,
        {w=0.5} sentindo o zumbido vibrando contra{w=1.0} sua mão."

        "Ele puxa a corda.{w} A nota pula da corda para o ar,{w=0.5} depois rasteja
        para dentro de seus ouvidos,{w=0.5} escorre para sua{w=0.2} mente.{w} E aí está o atraso."

        "Há uma lacuna{w=0.2} entre ação e reação.{w} Esta noite o mundo
        parece lento para o minotauro,{w=0.5} enquanto ele olha para o deserto abaixo."

        "Aquela terra com a qual ele está tão familiarizado,{w=0.5} e a qual o novo mestre
        o familiarizou novamente."

        "Seus dedos acariciam a corda,{w=0.3} para cima e para baixo,{w=0.3} para cima e para baixo.{w}
        Ele está olhando para fora,{w=0.3} para as colinas e vales,{w=0.3} para a costura entre
        terra e céu,{w=0.3} para os milhares de pontos acima."

        "Ele ordena seu dedo para puxar a corda,{w=0.8} mas há{w=0.3} um atraso.{w}
        Seus movimentos são lentos,{w=0.3} assim como seus pensamentos. Seus olhos direcionam-se para a escuridão."

        "Tocado, o som se arrasta para cima— e, na maioria das circustâncias,
        provocaria uma sensação de conforto em sua mente.{w} Mas.{w} Há{w=1.0} um atraso."

        "Astério desliza o dedo sobre a corda.{w} Ele a engancha com uma unha,{w=0.4}
        a puxa,{w=0.4} sente aquela tensão insuportável e antecipa seu estalo."

        "Há uma lacuna entre ordenar que sua mão solte{w=0.5}
        e ouvir aquele chicote estalando contra sua orelha."

        "Sua outra mão aperta o cabo da lira,{w=0.5} unhas cravam em sua carne.{w}
        Há um atraso{w=1.0} entre senti-las cravando e aquela,{w=0.5} agonia familiar."

        "Astério desliza o dedo sobre a corda da lira, antecipando o aproximar dos passos
        de um mestre.{w} Ele olha para fora, mas não vê nada e, na verdade, o próprio tempo parece inconsistente."

        "Desta vez, a corda fere seu dedo, porque{w=0.7}
        ela esfregou a ponta do dedo em carne viva.{w} Ele engancha uma unha na corda, puxa,
        e percebe que nem sua unha e nem o acorde quebrarão."

        "Ele puxa a corda, {w=0.5} e há um atraso."
        pause 3.0
        "Há quanto tempo este miserável está fazendo isso?"

        asterion "Que tolice. {w=0.8}Branda indulgência,{w=0.6} lamúria e —"

        "Apenas lamúria.{w=0.4} Ele está tendo um acesso de raiva, sentado na varanda puxando
        aquela mesma corda de novo e de novo.{w=0.4} Ele também costumava fazer isto quando criança."

        "Naquela época, ele receberia um sermão por causa disso, dado por sua ama de leite."

        asterion "Que tolice. {w=0.8}Branda indulgência,{w=0.6} lamúria e —"

        pause 1.0

        "E então ele foi enviado para o labirinto.{w} Com sua {w=0.7}lira contrabandeada, pronta
        para ser puxada de novo e de novo."

        pause 1.0

        "Até que se partiu, uma noite quando ele e Laomedonte conversaram."

        "Ele rumina sobre pensamentos e memórias.{w=0.4} Seu convidado alguma vez
        falou estas mesmas palavras em suas costas?"

        "Qualquer resposta que poderia passar por sua mente, não importa.{w=0.4}
        Não há lugar para nada, exceto a certeza absoluta de que, sim,
        Laomedonte realmente acreditava que —"

        asterion "Que tolice. {w=0.8}Branda indulgência,{w=0.6} lamúria e —"

        "Uma monodia que ele poderia berrar, ele apenas murmura. Uma túrgida timidez
        o impede até de segurar o timbre."

        "Apesar do atraso, ele puxa a corda, agora manchada de preto e vermelho.{w=0.4}
        E o labirinto de sua juventude — aquele com o santuário no centro
        e paredes com o triplo de sua altura — embaralha-se e muda."

        "Um novo rasteja das profundezas do Tártaro.{w=0.4} Ele ouve velhos deuses resmungando
        suas maldições, brincando com seu fio de vida— e o cacarejar dos Destinos à distância."

        "Ele puxa sua corda e não consegue deixar de pensar o quão facilmente alguém poderia se perder
        entre uma pilha de pedaços desgrenhados de tecido."

        "Corda e tecido. Enrole-os. Faça um novelo de lã com eles. Ele o guiará através —"

        asterion "Que tolice. {w=0.8}Branda indulgência,{w=0.6} lamúria e —"

        "Deixe reto, amarre nos pinos, aperte. Puxe a corda,{w=0.5}
        com o atraso, e ela {w=0.5}martela em sua mente contra aquele seu cérebro inconsistente."

        asterion "Que tolice. {w=0.8}Branda indulgência,{w=0.6} lamúria e —"

        "E então dezenas de séculos de um novo labirinto."

        "Agora ele está aqui, hoje, depois de oitenta anos trancado em uma câmara fria.{w=0.4}
        Lamuriando porque o mestre o mandou para o vale."

        asterion "Que tolice. {w=0.8}Branda indulgência,{w=0.6} lamúria e —"

        "É tão ruim assim?{w=0.4} O que pode cair sobre ele que não o ocorreu mais de mil vezes?"

        "A dor é uma coisa tão frágil.{w=0.4} Cerre os dentes e aguente, deixe-a vir.{w=0.3}
        Ser permitido um momento de segurança, como este, é razão suficiente para ser grato."

        "Pare de reclamar, quaisquer excursões que este mestre ordene não são nada
        comparadas ao que já foram.{w=0.4} Deixe um demônio pegar um braço, uma perna,
        ainda não é nada mais que um arranhão."

        asterion "Que tolice. {w=0.8}Branda indulgência,{w=0.6} lamúria e —"

        if TimesSent == 1:

            $renpy.music.set_volume(0.4, delay=1, channel='music')

            "A dor passa, cerre os dentes e aguente, seja grato pelo mestre
            achar adequado que você tenha um teto sob sua cabeça."

            "O minotauro silencia as cordas com a palma da mão. Ele vê o que aconteceu
            com seu dedo, vermelho e preto agora, e o ar deixa seus pulmões. "

            "Mas esse ainda é o pior cenário, não é?{w}
            Talvez o Mestre seja simplesmente ingênuo, em oposição a —"

            "Ele coloca a ferida em carne viva em sua boca, acalmando-a com a língua.
            Apenas aguente, por enquanto.{w=0.3} Seja ele quem for, ainda está para ser revelado."

            pause 1.0

            asterion "Apenas aguente."

        else:
            $renpy.music.set_volume(1.0, delay=1, channel='music')
            "Ele para.{w} O atraso diminuiu, ele percebe, mesmo que as palavras ainda lhe escapem."

            "Ele quase se engasga.{w=0.3} O aperto em seu peito havia reduzido sua respiração,
            ele só agora percebe a tensão em sua mandíbula e uma tontura na cabeça."

            "Mas isto traz uma nova onda de turbulência.{w=0.3} Conforme a mente do minotauro
            se recupera aos poucos, velhas dores rastejam da escuridão."

            "Seu estômago se enche de fogo, agitando-se e fervendo, ameaçando subir
            pela garganta."

            "A pressão de seu estômago sufoca seus próprios pulmões e o mantém
            em um estado sem fôlego, lutando para expandir seu peito. Ele sufoca quando pensa
            em qualquer coisa além de sua respiração."

            "Ele leva uma mão à bochecha e a segura no local.{w=0.4}
            Seu polegar cava sob a mandíbula.{w=0.4} Mais forte.{w=0.4} Sua garganta seca e—"

            asterion "Que tolice. {w=0.2}Branda indulgência,{w=0.2} lamúria,{w=0.2} e —"

            "E ele respira com a língua para fora, semblante curvado para conter a náusea.{w=0.3}
            Mas nada disso impedirá suas entranhas de serem bicadas como estão sendo agora."

            "Ele se levanta e anda com pesar.{w=0.3} Entre cada poucos passos, uma respiração rígida e concentrada,
            lentamente em direção ao seu quarto.{w=0.3} Aquela pequena caixa."

            "Com seu andar pesado, sustentando o corpo em cada perna em sucessão,
            seus chifres balançam e batem nas paredes do corredor."

            "Ele bufa.{w=0.3} Sua mão volta para a bochecha, o polegar sob a mandíbula.{w=0.4}
            ele poderia arrancar o maxilar fora, mas apenas se arrasta para frente como uma criança punida."

            "Ele cruza a entrada.{w=0.3} Fecha a porta. {w=0.3}O ar ferve."

            pause 1.0

            $renpy.music.set_volume(1.2, delay=1, channel='music')
            "O ácido se agita em seu estômago, sobe até a garganta seca e agora fechando.{w=0.3}
            Seus dentes marcam sua língua enquanto a náusea rodopia e bate dentro dele."

            "Há muito as palavras falham com o minotauro, mas agora mais do que nunca. A hidra
            cuspindo veneno dentro dele não pode ser controlada ou morta, pois a cada decapitação,
            seu veneno ressurge com vigor renovado."

            "Mas o minotauro pode afogá-la, ele sabe.{w=0.3} Pode retornar, mas ele pode afogá-la
            por enquanto. Ele pode parar de tensionar contra o impulso agora que está sozinho."

            "O miserável levanta as mãos para o teto esbranquiçado, para a única lâmpada oscilante,
            como alguém de luto preso em lamentação."

            "E os traz de volta para baixo: uma bate em seu rosto, a outra agarra e conduz seus próprios chifres."

            "Ele puxa e gira até ouvir um estalo.{w=0.3} Ele grunhe e se lança no ar para
            tentar arrancar osso do osso, ou cérebro do corpo.{w=0.3} Sua cabeça sacode e tenta
            se afastar de seu próprio alcance."

            "Após puxar, ele dá um tapa no focinho.{w=0.3} Mais forte.{w=0.3} Punho fechado."

            "Ele quase machuca as bases dos dedos socando para cima até os chifres.{w=0.3}
            Algumas vezes ele fere a mandíbula.{w=0.3} Ele puxa os chifres novamente, narinas
            dilatando enquanto ele balança a cabeça ao redor como em um rodeio."

            "Ainda assim, a cada puxão, um membro da multidão ruidosa de seus pensamentos sai
            ou se senta."

            $renpy.music.set_volume(1.0, delay=1, channel='music')
            "Torna-se um caso rítmico enquanto o minotauro cavalga a si mesmo,
            sincroniza sua respiração, seus grunhidos e ranger de dentes,
            com suas próprias mãos nos chifres."

            "Mas isto o levará apenas até certo ponto.{w=0.3} Seu cotovelo atinge a parede
            e a dor repentina não intencional o leva a um ganido ofegante."

            "Ele não está em condições de pensar no que está fazendo, mas sabe como está.{w=0.3}
            Sua cauda balança e sua mente cambaleia.{w=0.3} Ele bufa e abaixa a cabeça."

            $renpy.music.set_volume(0.8, delay=1, channel='music')

            "Com uma pisada para frente, bem no meio de sua cama, Astério {i}bate{/i}
            bate seus chifres na parede e afunda dentro."

            "Ele joga a cabeça para a esquerda; arranca um pedaço de gesso da parede.{w=0.3}
            Sua cabeça chicoteia de volta para a direita: outro amassado."

            "Ele se joga contra a parede, amontoando, partindo o papel de parede e fazendo rachaduras
            no gesso."

            $renpy.music.set_volume(0.6, delay=1, channel='music')

            "Quando sua cabeça encontra um canto, ele solta um soluço de choro.{w=0.3} Seus olhos estão secos, mas sua garganta
            corta o silêncio à medida que ele estica o pescoço para cima, levando outro pedaço de gesso com ele.{w=0.3}
            Ele bate a cabeça lateralmente contra as vigas de madeira e metal até que estejam retorcidos."

            "Poeira e destroços são vomitados no quarto, mas o minotauro está de olhos bem fechados.{w=0.3}
            A poeira vagueia através da luz da lamparina e amplifica as sombras projetadas pelo touro
            colidindo a si mesmo contra o que quer que esteja presente."

            "Marcas de chifre cobrem as paredes.{w=0.3} Uma gaveta em um armário que prendeu em uma ponta foi
            batida até a madeira se estilhaçar contra seu couro cabeludo."

            "Uma mão segura sua garganta e a outra aperta seu estômago.{w=0.3}
            Ele bufa e tosse na poeira e abre os olhos.{w=0.3}
            Sua expressão vazia afunda.{w=0.3} Ele chuta um pedaço caído da parede o mais forte que consegue."

            $renpy.music.set_volume(0.4, delay=1, channel='music')
            play sound "music/AsterionHums.mp3"

            "Isso é o suficiente para trazer a si uma parte dele mesmo, um pedaço suficiente — ele cantarola,
            comandando o hotel para voltar à forma original, reconstruindo a parede com sua voz."

            stop sound fadeout 0.5
            "Seus chifres o conduzem novamente, no entanto; o minotauro destrói as paredes
            antes mesmo de terminarem de reparar."

            "Destroços nevam sobre ele, mas desaparecem antes de atingir o solo.{w=0.3}
            Ele bate na parede cada vez mais forte, triturando o gesso com seus chifres,
            e indo tão longe a ponto de arranhar sua cabeça com os fragmentos."

            "De novo e de novo ele corre e atinge a parede, em seguida, tudo."

            "Ele fecha os olhos em meditação, enquanto o atraso desaparece de sua mente,
            caindo no chão da mesma forma que faz quando sente uma ferida começar
            no centro de seu crânio."

            $renpy.music.set_volume(0.2, delay=1, channel='music')
            play sound "music/AsterionHums.mp3"

            "Ele se permite deitar no chão, o nariz arrastado ao longo da parede."

            "Ele respira profundamente sem concentração.{w=0.3}
            O touro quer dizer algo, mas não diz.{w=0.3}
            A bola de chumbo no meio de seu cérebro se foi; nada a substitui."

            stop music fadeout 1.0

            stop sound fadeout 2.0
            pause 2.0

            "Quando o minotauro abre os olhos e se vê fixado no presente,
            tão vivo quanto poderia estar, seu cantarolar aumenta repentinamente e cessa."

            "Ele limpa a poeira de sua cabeça e roupas enquanto verifica o quarto,
            certificando-se de que está todo consertado, e o encontra limpo e arrumado — exceto pela
            poeira nevando de seu pelo e a cama desarrumada, seus lençóis ainda com marcas de cascos."

            "O minotauro caminha de volta para o labirinto, levando o dedo à boca."

    $renpy.music.set_volume(1.0, delay=1, channel='music')

    play music "music/Lullaby.ogg" fadeout 2.0 fadein 2.0
    scene bg staircase
    with Dissolve (2.0)

    #we have a reprise of the player running up to the master's quarters, two steps at a time,
    #but this time he's victorious

    #he arrives at the quarters, building up

    "Faz pouco mais de uma semana desde que você cruzou o deserto, avistou o vale
    abaixo e abriu todas as portas dentro deste hotel."

    "Desde aquela noite quando você e Astério se sentaram diante da lareira, tanta coisa mudou.
    O hotel foi restaurado: seus corredores antes silenciosos agora estão salpicados com passos e vozes de hóspedes."

    "E o minotauro, aquela figura arruinada no fundo da câmara fria — tão certo quanto
    o sol nasce no leste e se põe no oeste — ele também mudou."

    "Ao longo dos anos, surgiram mestres que viram virtude em servir aos deuses — afinal,
    o que poderia ser mais legítimo que reencenar esses antigos ritos?"

    "E mesmo assim, também surgiram mestres que acharam por bem descartar aqueles antigos arreios
    e mergulhar fundo em algo humano — e ainda mais profano, em decorrência disso."

    "Para libertar um prisioneiro de sua sentença legítima, para corromper um domínio sagrado
    visando cumprir os caprichos de humanos inconstantes. Para invocar diamantes das mãos,
    para abrigar miseráveis e imundos, para desviar os recursos desta terra para seus próprios objetivos."

    "Que tolices estranhas fazem esses humanos, tais deuses devem pensar.
    Algum Prometeu ou outro lhes oferece fogo, um presente adequado para queimar gordurosas hecatombes,
    e é usado, em vez disso, para aquecer os pés de alguém."

    "O que este novo mestre, subindo a grande escadaria, fará com seu mandato?"

    "Quando ele olha para o prisioneiro e revela seu verdadeiro eu, despreza o
    julgamento dos humanos sob seus pés? Ou ele teme os deuses, onde quer que estejam?"

    "Ele sonha em bater o peito contra o legado do velho herói, Teseu,
    ou se contentará em ser decente e não mais especial que seus colegas?"


    if TimesSent == 0 and global_affection > 7:
        "Será que suas pernas não se cansarão de pisar dois degraus de cada vez e tirar algo bom de negociações estranhas?{w=0.2}
        Serão seus passos acompanhados,{w=0.2} três degraus por passo,{w=0.2} por outra pessoa?"

    if TimesSent == 0 and global_affection <= 7:
        "Será que ele ascenderá sobre os ombros de uma besta quando tiver que descansar,{w=0.2}
        liderando o caminho em espírito com a ajuda de outros para um lugar mais próspero?"

    if TimesSent ==1:
        "Será que ele se cansará na metade da escada um dia,{w=0.2}
        e se perderá em seus próprios pensamentos:{w} de algumas decisões feitas pela metade,
        {w=0.2} algumas feitas por ele e apenas ele,{w=0.2} que ele não sabe como faria de novo?"

    if TimesSent >1:
        "Seu coração cederá ao tédio e à indisposição,{w=0.2}
        tal controle mágico perdendo sua fascinante aura de mistério?"

    "Qualquer que seja sua escolha, ninguém pode lançar julgamento — pois o senhor detém todo o
    poder neste domínio, e os próprios deuses não estão em lugar algum."

    "Sem freios e contrapesos, sem medo de represálias, apenas as pegadas petrificadas
    de contratos e maldições."


    if TimesSent == 0:
        "Talvez estes, também, possam ser alterados?"
    else:
        "Talvez estes, também, possam ter utilidade?"

    "Exceto, talvez, por aquele vigia solitário lá embaixo. O guardião da vontade divina.{w=0.3}
    Que olhos perspicazes ele possui."

    "Quanto a nós...{w=0.3} Não se preocupe, não julgaremos você.{w=0.3} Isto não é um julgamento."

    "Um homem como você não carrega arrependimentos na maneira como conduz seus assuntos."

    scene bg black
    with Dissolve(1.0)

    "Agora, melhor não desperdiçar mais do precioso tempo do monarca.{w=0.3}
    Diante de você está a porta, e além dela o prisioneiro aguarda seu carcereiro."

    scene bg oldquarters
    show quartertable
    if TimesSent == 0:
        $Asterion.change("emotion", "sad")
    else:
        $Asterion.change("emotion", "contemplative")
    $Asterion.change("rightarm", "loose")
    $Asterion.change("leftarm", "loose")
    show Asterion behind quartertable:
        xalign 0.5 yalign 1.2 zoom 0.8
    with Dissolve(2.0)

    #Build 0.3's ending is determined here
    #current affection max is 9.5 (10 if your bg is speedrunner or art)
    #if you sent asterion first and gave a bad reason to do so, you get the bad ending.
    #if you never sent him and have over 6 affection, you get the good ending
    #if you sent him out once but have more than 5 affection,
    #or you never sent him but affection is under 5, you get a neutral
    #you also get the bad ending if you sent him twice, or just once and didn't have enough affection

    $Build3Ending = "none"

    if Build3Ending != 'bad':
        if TimesSent == 0 and global_affection >6:
            $Build3Ending = 'good'
        elif TimesSent == 2 or (TimesSent == 1 and global_affection <= 5):
            $Build3Ending = 'bad'
        else:
            $Build3Ending = 'neutral'
    if Build3Ending == 'bad':
        #Asterion's perspective
        stop music fadeout (2.0)
        "Isso já aconteceu antes, estrelinha.{w=0.3} Nada que você não tenha resistido antes."
        "Inspire.{w=0.3} Sorria."
        $Asterion.change("emotion", "contemplative")
        "Ainda não é o suficiente, mais."
        $Asterion.change("emotion", "smiling")
        "Expire.{w=0.3} Inspire.{w=0.3} Expire.{w=0.3} Diga alguma coisa."

        asterion "Saudações, meu senhor."

        hide Asterion
        hide quartertable
        with Dissolve(1.0)
        pause 1.0
        show Asterion:
            yalign 1.0 zoom 1.0 xalign 0.5
        with Dissolve(1.0)

        "Ele se aproxima. Parece que você está se sufocando, mas isto é mentira, você não pode.
        Você já passou por isso antes,{w=0.2} precisa ser forte."

        $inventory.remove_item('Wine Bottle')
        "Ele disse algo, e agora oferece o vinho.{w} Aquele caroço escuro aderido ao seu braço.{w}
        Pode muito bem ser um tumor."

        "Águas turbulentas: é um mar profundo e escuro lá dentro.{w=0.3} Uma garrafa de mar podre,
        com espuma e bolhas nas bordas de sua superfície, chamando, acenando."

        "Estenda seu braço.{w=0.3} Não, seus dedos estão errados, alargue a pegada{w=0.5} — sim,{w=0.2}
        agora aproxime.{w} Traga para mais perto."

        $Asterion.change("emotion", "laughing")

        "Ele diz alguma coisa.{w=0.3} Uma piada?{w} Ria.{w} Curve os cantos de sua boca, ria agora {w=0.5}
        — não, isto é {w=0.2} — você está tossindo."

        $Asterion.change("emotion", "surprise")
        "Sua garganta não está fechando, você não ficará sem ar.{w=0.3} Morda sua língua.{w=0.3} Mais forte."

        $Asterion.change("emotion", "bowing")
        "Você será curado de qualquer maneira, não tenha medo de um pouco de sangue e icor agora.{w=0.3}
        Morda mais forte, droga, seu miserável maldito —"

        "Isso, agora inspire.{w=0.3} Segure a garrafa assim, isso, e com a outra mão
        puxe a rolha.{w} Aperte com mais força.{w=0.3} Sim.{w=0.3} Agora puxe."

        hide Asterion
        with Dissolve(1.0)

        "Beba."

        "Puxe a rolha.{w} Aí está,{w=0.2} seu mar,{w=0.2} sua enseada."

        "Seja forte, estrelinha."

        "Você {i}é{/i} forte. Quantos mestres vieram e se foram?"

        "Graças aos deuses, pois eles o tornaram forte o suficiente para carregar um fardo insuportável.{w=0.2}
        Você pode cumprir seu dever,{w=0.2} você é um escravo,{w=0.2} esta é sua sentença,
        e eles nos deram tudo o que precisamos para servir bem."

        "Reine a si mesmo.{w=0.2} Morda mais forte.{w=0.2} Você é um escravo, foi feito para
        trabalhar duro, e agora terá o corpo para acompanhar esta mente imortal."

        "Você vai sobreviver e servir bem.{w=0.2} Agora beba o vinho, ele vai lavar o icor."

        "Isso é o que eu mereço."

        scene bg black
        with Dissolve(2.0)

        asterion "Obrigado, meu senhor."

        asterion "Assim, o servirei melhor."

        $Asterion.setOutfit()
        $Asterion.change ("stage", "buff")
        $Asterion.loadOutfit()
        $throwaway1 = False
        if 'vneck' in Asterion.clothes:
            $throwaway1 = True
            $Asterion.change ("clothes", "nude")
            $Asterion.change ("underwear", "jeans")

        $wardrobe.add("underwear", "jeans")
        $Asterion.change ("clothes", "40s")
        $Asterion.change ("emotion", "neutral")

        you "Ótimo.{w=0.2} Agora...{w=0.2} tem um concerto, não é?{w} Deveríamos ir."

        asterion "Sim.{w=0.2} Estou pronto para a performance."

        $LoungeBlobs=[False,2]
        scene Lounge
        if first_guest == "Luke":
            show LoungeLight
        with Dissolve(2.0)

        #long fade, show lounge
        #we are still in Asterion's perspective
        pause 2.0

        "...Eles estão falando sobre mim..."

        $Luke.change("emotion", "surprise")
        $Kota.change("emotion", "surprise")
        $Luke.change("arm", "hip")
        $Kota.change("rightarm", "relaxed")
        $Kota.change("leftarm", "relaxed")

        show Luke:
            xalign 1.0 xzoom 1 yalign 1.0
        show Kota:
            xalign 0.1 xzoom 1 yalign 1.0
        with Dissolve(1.0)

        "Quem? Luke? Kota?"

        "Sim, eles estão vendo que estou diferente.{w=0.2} Meu olho está..."
        hide Luke
        hide Kota
        with Dissolve(1.0)
        pause 2.0

        "Xiu, não se preocupe com isso."

        "Mas todo mundo está olhando."

        pause 2.0

        "Eu estou aqui com você, estrelinha.{w} Venha agora...{w=0.2} Somos só você e eu. Como sempre."

        scene bg black
        with Dissolve(2.0)
        "Se apegue ao momento, me segure e não me deixe escapar."

        "Um passo de cada vez...{w=0.2} Lá está o banquinho.{w} Sente nele."

        "Vamos, agora.{w=0.3} Você sempre foi forte, estrelinha."

        "Os bons e maus tempos vêm e vão.{w=0.3} Mestres também.{w=0.3}
        Você já sabe o que de pior pode acontecer
        e pode resistir novamente se chegar a esse ponto."

        "...Eles estão olhando para mim..."

        "Sim, o tempo nunca para, não é?{w=0.2} Mesmo agora, os segundos estão passando."

        "Cante, agora."

        jump Build3End

    #if you've been good or neutral

    "Você termina sua subida e abre a porta, e lá está ele, sentado na mesa da sala de estar
    enquanto abraça sua lira."

    #giving Asterion the wine
    you "Conseguimos o vinho!"

    show Asterion:
        ease 0.5 zoom 0.77 yalign 1.15
    $Asterion.change("emotion", "tired")
    "Com sua entrada, o minotauro recua como se tivesse sido atingido no estômago.
    Uma respiração presa é arrancada dele como um soco."

    show Asterion:
        ease 0.5 zoom 0.8 yalign 1.2
    "Leva um momento até mesmo para olhar para o lado e enxergar você lá —
    e outro para enxergar o vinho. Esta forma escura em sua mão, parecendo tão estranha,
    sacudindo e rodopiando."

    $Asterion.change("emotion", "sad")

    "O minotauro abre a boca para falar e hesita, silêncio.
    Ele estremeve, calafrios correndo por sua espinha todo o caminho até a nuca."

    "E então o ataca novamente, aquela terrível sensação, como se beija-flores estivessem
    bicando a parte de trás de sua cabeça."

    "Parecia que ele estava prestes a falar, mas com toda a turbulência,
    ele apenas respira fundo em vez disso."

    pause 1.0

    you "Você está bem?"

    $Asterion.change("emotion", "bowing")

    "Ele exala um pouco mais forte. Suas narinas dilatam em um bufo."

    asterion "Sim,{w=0.2} Mestre,{w=0.2} Estou bem.{w} Estou apenas um pouco chocado,{w=0.2} mesmo agora."

    $Asterion.change("emotion", "sad")

    "O minotauro não se levantou. Você balança a garrafa na direção dele."

    you "Bem,{w=0.2} não olhe para mim como um cervo nos faróis,{w=0.2} venha cá."

    "A respiração do minotauro é curta e agitada, como se ele estivesse descansando de uma corrida.
    Seus olhos denunciam algum tipo de torpor."

    show Asterion:
        ease 1.0 yalign 1.0

    $Asterion.change("emotion", "neutral")

    asterion "Um cervo? Eu?"

    "Ao ouvir suas palavras, ele estende a mão e acaricia os chifres — verificando
    se foram transformados em galhadas — e se levanta com a ordem."

    hide Asterion
    hide quartertable
    with Dissolve(1.0)
    pause 1.0
    show Asterion:
        yalign 1.0 zoom 1.0 xalign 0.5
    with Dissolve(1.0)

    "Ele se aproxima, com os braços para baixo nas laterais, como se não soubesse
    o que fazer com eles. Talvez ele esperasse mais calma, mais cerimônia."

    "Receber a garrafa assim, como um amigo entregaria um presente, torna
    seu movimento hesitante."

    if global_affection < 3:
        you "Espere,{w=0.2} como é que se diz quando alguém lhe dá um presente?"
        $Asterion.change("emotion", "sad")
        asterion "Obrigado, senhor."

    "Astério estende as mãos e cuidadosamente a pega."

    $inventory.remove_item('Wine Bottle')


    if Build3Ending == 'good':

        #moderately high affection, never sent Asterion to the valley

        #he holds the bottle, examines it
        $Asterion.change("emotion", "contemplative")

        "Seu aperto é tão suave que a superfície da garrafa desliza sobre sua mão.
        Apenas um momento de distração seria o suficiente para fazê-la escorregar."

        "Seu polegar remove algumas manchas do pescoço enquanto ele observa os sedimentos se mexerem
        com cada movimento. Ele a alinha com uma lâmpada e olha através do vidro, como
        se fosse um grande mar escuro."

        "Suas sobrancelhas estão franzidas, seu olhar é implacável, sua cauda cai para
        baixo e fica imóvel. Ele fica como uma estátua quando deveria
        estar pulando de alegria."

        you "É o acordo real? Não é o vinho certo?{w} Que Deus me ajude
        se aquela cobra nos ferrou assim —"

        $Asterion.change("emotion", "neutral")
        asterion "Não,{w=0.2} é o certo.{w} É apenas..."

        "As orelhas do minotauro sacodem enquanto ele se perde em seus pensamentos."

        "Ele desarrolha a garrafa com cuidado e delicadeza e a leva ao nariz."

        "Ele inala, e então seus ombros desabam conforme ele dispõe a garrafa na mesa."

        $Asterion.change("emotion", "sad")
        asterion "Argos não mentiu.{w} No entanto,{w=0.3} com licença, mestre,{w=0.3}
        talvez eu tenha me levantado rápido demais.{w} Eu preciso{w=0.5} me sentar."

        show Asterion:
            ease 2.0 yalign 1.6

        "Ele olha da garrafa para você, para a janela, para a lira, de volta para a garrafa."

        "Seus olhos estão bem abertos, suas narinas dilatam-se a cada respiração curta.
        Ele tenta olhar de volta para você, mas algo mudou — seus olhos parecem opacos,
        como se ele estivesse perdido em pensamentos."

        stop music fadeout 2.0
        show blackback behind Asterion
        with Dissolve(2.0)
        pause 2.0
        #Here it's just Asterion's internal monologue, these are all thoughts:

        $Asterion.change("emotion", "tired")
        "O que eu posso fazer para retribuir isto? Sua bondade cessará se eu não retribuir..."

        $Asterion.change("emotion", "sad")
        "Como ele pôde se desviar tanto de seu caminho para se encarregar disso?{w=0.2} Ele não
        pode possivelmente querer algo além de usar isso para alguma coisa, pode?{w=0.2} No que eu estou me metendo aqui?"

        "Deve haver uma pegadinha, sempre há.{w=0.2} Exatamente como o que aconteceu com Titônio."

        $Asterion.change("emotion", "tired")
        "Um não pode libertar outro sem se prender a algemas.{w=0.2}
        Então, porque ele faria isso?{w=0.2} O que ele quer de mim?"

        "Estou em dívida agora.{w=0.2} Além de ser um escravo, agora tenho mais uma coleira em meu pescoço.
        {w=0.2}Teria sido melhor se ele nunca tivesse passado pelo transtorno."

        pause 2.0
        $Asterion.change("emotion", "bowing")
        pause 1.0

        "Por que sequer hesitar e tagarelar em sua cabeça assim{w=0.2} — não importa
        o que você pensa.{w=0.2} Ele lhe deu algo, então você precisa aceitar.{w=0.2}
        Pare de perder tempo.{w=0.2} Não fique tenso."

        "É a coisa mais educada a se fazer{w=0.2} — ele lhe uma coisa, então aceite."

        hide blackback
        with Dissolve(2.0)
        pause 2.0

        play music "music/seikilos.mp3" fadeout 1.0 fadein 1.0

        "Por quase um minuto agora, o minotauro ficou em silêncio— imóvel,
        exceto por orelhas contraídas e sobrancelhas franzidas."

        you "Astério, tem certeza que não tem nada de er—"

        show Asterion:
            ease 1.0 yalign 1.0
        $Asterion.change("emotion", "neutral")

        asterion "Obrigado, meu —{nw}"

        $Asterion.change("emotion", "sad")
        "Ele fica de pé enquanto fala, mas para."

        $Asterion.change("emotion", "tired")
        show Asterion:
            ease 1.0 zoom 1.05 yalign 1.1
        "Ele dá mais um passo à frente, mas não encontra seus olhos."

        asterion "Peço desculpas por atropelar sua fala, Mestre,{w=0.2} mas...{w} obrigado."

        "Ele levanta os braços até a metade do peito.{w} Não é bem um dar de ombros."

        asterion "Ah.{w=0.3} Hm.{w=0.2} Hã.{w=0.2} Obrigado.{w=0.2} Apenas —"

        you "Ei,{w=0.2} escuta...{w=0.4} está tudo bem,{w=0.2} ok?"

        $Asterion.change("emotion", "sad")
        you "Você parece estar um pouco sobrecarregado hoje,{w=0.2} eu entendo isso.{w}
        Eu estava conversando com o Argos agora mesmo, afinal, e eu sei que isso pode afetar você."

        you "Essa tem sido uma semana tão ocupada, tirando toda a situação do vale."

        you "Então...{w=0.2} não se preocupe, ok?{w=0.2} Está tudo bem.{w=0.2}
        Agora, que tal você tomar um gole?"

        you "Vamos aos poucos.{w=0.2} Quer uma taça?"

        pause 1.0

        asterion "Não, tudo bem.{w=0.2} Eu posso beber da garrafa..."

        you "Ok.{w=0.2} Então,{w=0.2} agora,{w=0.2} beba."

        $Asterion.change("emotion", "bowing")
        "O minotauro acena com a cabeça. Ele endireita os ombros e expira,
        no que se pode presumir que é alívio."

        asterion "Como desejar,{w=0.2} senhor.{w=0.3} Obrigado."

        $Asterion.change("emotion", "sad")
        "Ele pega a garrafa. Enquanto a leva à boca, ele olha para você novamente,
        para se certificar de que está tudo bem."

        "Você faz seu quase dar de ombros em resposta, então ele bebe."

    else:
        #(neutral)
        $Asterion.change("emotion", "contemplative")
        "O minotauro sente o fundo da garrafa com o polegar.{w=0.2} Ele olha para cima e seus
        olhares se encontram.{w} Ele olha de volta para a garrafa."

        "Ele remove a rolha e leva a garrafa ao nariz.{w=0.2} Ele não parece se
        dar ao trabalho de cheirá-la, apenas respira normalmente."

        you "Você está...{w=0.3} determinando o \"ano de fabricação\"?"

        $Asterion.change("emotion", "bowing")
        show Asterion:
            ease 2.0 yalign 1.6

        "Ele não parece ouvir você- por um momento é como se a respiração dele
        parasse completamente.{w=0.2} Ele se senta, com a garrafa ainda perto do rosto,
        braços tensos, mas rosto inexpressivo."

        $Asterion.change("emotion", "contemplative")
        "O minotauro olha para a garrafa. Ele a cheira novamente. Ele parece notar
        seu olhar curioso, mas não mantém contato visual."

        "Seus olhos arregalados ficam opacos, como se ele estivesse perdido em pensamentos."

        #do the same thing you did for the previous one, we are going into Asterion's point of view
        stop music fadeout 2.0
        show blackback behind Asterion
        with Dissolve(2.0)
        pause 2.0

        "Não tenho como agradecê-lo o suficiente. {w=0.2} Nada que eu possa fornecer compensará isto."

        "Eu não deveria me sentir culpado por um presente quando ele está apenas — sendo tão bom.
        Se é para me tornar propriedade, espero que seja adequadamente."

        "Sei que ele deve saber o que preciso fazer para retribuí-lo.{w=0.2}
        Não posso retribuir aos deuses, mas para o Zeus vivo, posso retribuir os favores terrenos que receber."

        "Não espere que isso se torne um hábito dele,{w=0.2} estrelinha,{w=0.2} não.{w}
        Mas não haja como se ele não pudesse ter feito o que fez."

        "É um bom dia{w=0.2} — e talvez algumas canções e bebidas possam ser necessárias em breve."

        hide blackback
        with Dissolve(2.0)
        pause 2.0

        play music "music/seikilos.mp3" fadeout 1.0 fadein 1.0

        pause 2.0

        $Asterion.change("emotion", "smiling")
        asterion "Peço desculpas,{w=0.2} Mestre,{w=0.2} se estou atrasando você.{w}
        Não desejo falar além de minha posição aqui ao dizê-lo..."

        $Asterion.change("emotion", "tired")
        pause 1.0
        $Asterion.change("emotion", "neutral")
        "Ele abre a boca para falar novamente, mas se detém. Seu olhar vagueia
        ao redor como se procurasse as palavras certas, mas elas continuam fugindo de seu alcance."

        $Asterion.change("emotion", "bowing")
        asterion "Quando um mestre me faz um favor,{w=0.2} como você fez,{w=0.2}
        Quero ter certeza de que posso me apegar àquele momento.{w} Quase sempre é como um choque."

        asterion "Você me desorientou, um pouco."

        "A tensão em seu pescoço aumenta à medida que ele move a língua ao redor da boca,
        como se ensaiando sua própria declaração antes de falar."

        show Asterion:
            ease 2.0 yalign 1.0
        $Asterion.change("emotion", "tired")
        asterion "Já faz bastante tempo...{w=0.2} Mas não tenho certeza se algum mestre
        trabalhou tão rapidamente quanto você,{w=0.2} pelo menos nos últimos mil anos ou mais..."

        "Ele fala um pouco mais rápido, forçando as palavras agora."

        asterion "...E por as coisas estarem acontecendo tão rápido, eu apenas{w=0.2}
        — Eu posso ficar{w=0.2} — Bem...{w} Devo admitir que até esqueci que você
        estava aí parado por um momento...{w} Minhas desculpas,{w=0.2} Mestre."

        $Asterion.change("emotion", "neutral")
        you "Por que eu não faria um favor para você?{w=0.2} Você é um cara legal."

        you "Não é nem um favor,{w=0.2} é só...{w=0.2} eu tratando você como um amigo.{w}
        Estamos nessa juntos,{w=0.2} não estamos?"

        $Asterion.change("emotion", "tired")
        "O minotauro expira.{w=0.2} Desta vez, toda a sua postura muda,
        como se toda a tensão o tivesse deixado com aquele sopro de ar fresco."

        $Asterion.change("emotion", "sad")
        asterion "O Mestre me lisonjeia.{w=0.2} Obrigado."

        "Ele levanta a garrafa."

        $Asterion.change("emotion", "contemplative")
        asterion "Um brinde...{w} Que eu sirva bem à vontade de Zeus,{w=0.2} para merecer
        seus favores em perenidade."


    $Asterion.change("emotion", "contemplative")
    "Começa com um gole pausado para apreciar o sabor do vinho,
    para inspirar e expirar, antes de continuar."

    "Suas narinas dilatam-se conforme o vinho — por mais agradável que seja —
    queima sua garganta."

    $Asterion.change("emotion", "bowing")

    "O minotauro fecha os olhos e joga a cabeça para trás. Seu pomo de adão balança
    com cada gole, e a garrafa borbulha conforme seu conteúdo é esvaziado em torno
    do selo imperfeito dos lábios de Astério."

    "Enquanto isso,{w=0.2} nada acontece.{w} Ele permanece exatamente o mesmo,
    uma orelha ainda sem pelos e um olho..."

    show Asterion behind blackback
    show blackback:
        alpha 0.0
        linear 0.2 alpha 0.5
        pause 0.2
        linear 0.1 alpha 0.0
        pause 0.1
        linear 0.2 alpha 0.7
        pause 0.2
        linear 0.1 alpha 0.0
        pause 0.1
        linear 0.2 alpha 0.8
        pause 0.4
        linear 0.1 alpha 0.0
        pause 0.1
        pause 0.1
        linear 0.2 alpha 0.9
        pause 0.6
        linear 0.1 alpha 0.0
        pause 0.1
        linear 0.2 alpha 1.0
    play sound "sfx/creak.ogg"
    "O hotel estremece — o chão abaixo de você chacoalha, e você ouve novamente:
    o som estridente da obsidiana no alicerce batendo contra si mesma."

    "Quase soa como um grito distante..."

    hide Asterion

    hide blackback
    with Dissolve(3.0)
    #lights return, slowly
    #don't show Asterion yet
    $Asterion.setOutfit()
    $Asterion.change ("stage", "buff")
    $Asterion.loadOutfit()
    $throwaway1 = False
    if 'vneck' in Asterion.clothes:
        $throwaway1 = True
        $Asterion.change ("clothes", "nude")
        $Asterion.change ("underwear", "jeans")

    $wardrobe.add("underwear", "jeans")
    $Asterion.change ("emotion", "neutral")


    "A mesa range quando Astério bate a garrafa de vinho vazia contra ela.
    Sua cauda sacode sobre o chão."

    "Seus olhos estão bem fechados; seu olho esquerdo fechou pela primeira vez em muito tempo,
    e ele parece estar se concentrando nele."

    #show fully healed Asterion, neutral
    show Asterion:
        xalign 0.5 yalign 1.0 zoom 1.0
    with Dissolve(4.0)

    you "Caramba,{w=0.2} uau."

    $Asterion.change ("emotion", "contemplative")

    you "Hã.{w=0.2} Como você se sente?"

    asterion "Eu me sinto...{w} me sinto bem,{w=0.2} um pouco tonto."

    asterion "É...{w=0.2} bastante perturbador, ter dois olhos novamente depois de tanto tempo.{w}
    Mas de um jeito bom."

    "O minotauro se sacode como um cachorro faria ao tentar se secar — suas orelhas
    e cauda balançam."

    $Asterion.change ("emotion", "smiling")

    asterion "Eu me sinto...{w=0.2} pesado!{w=0.4} Já faz tanto tempo desde a última vez que estive assim!"

    $Asterion.change ("emotion", "neutral")

    asterion "Ah...{w=0.2} espero que eu..."

    $Asterion.change ("emotion", "relieved")

    asterion "É assim que eu costumava parecer,{w=0.2} mais ou menos.{w=0.3} Espero que não esteja..."

    you "Nah, não se preocupe com nada, Astério.{w=0.3} Está tudo bem e, na verdade,
    você parece ótimo!"

    $Asterion.change ("emotion", "embarrassed")

    asterion "Ah.{w=0.3} Hã.{w=0.3} Hum..."

    pause 1.0

    $Asterion.change ("emotion", "contemplative")

    asterion "Obrigado."

    pause 1.0

    you "Mas...{w=0.2}talvez devêssemos ir?{w=0.2} Você não tem o concerto?"

    $Asterion.change ("emotion", "surprise")

    asterion "Pelos doze..."

    if throwaway1:
        "Você olha para os restos da camisa que fez para Astério, caída no chão e
        rasgada em pedaços."
        $Asterion.change ("emotion", "sad")
        asterion "...Eu sinto muito, Mestre."
        $Asterion.change ("emotion", "horny")
        asterion "É... é por isso que prefiro togas.
        Meu... meu pescoço não se dá muito bem com colarinhos apertados."

        you "Bem... não se preocupe com isso. Podemos consertar mais tarde.
        Agora, você deveria estar se preparando para o seu show."

        $Asterion.change ("emotion", "contemplative")
        asterion "Sim, eu deveria."
    elif Asterion.clothes != "40s":

        $Asterion.change ("emotion", "neutral")

        asterion "Mestre, se me der licença... posso me preparar?"

        you "Claro, é sua grande noite!"

    "As orelhas dele sacodem como se para afastar o esquecimento."

    hide Asterion
    with Dissolve(1.0)

    "O minotauro se move pelo quarto para se arrumar, pegar sua lira e
    certificar-se da afinação das cordas."

    "Conforme ele prepara sua lira, você o escuta murmurando.
    Aqui e ali você capta uma ou duas palavras."

    asterion "Se perdeu no vinho..."

    if Asterion.clothes != "40s":
        $Asterion.change("clothes", "40s")
    $Asterion.change ("emotion", "contemplative")
    show Asterion
    with Dissolve(1.0)

    asterion "Alceu disse,{w=0.2} e é verdade..."

    asterion "En oinoi aletheia..."

    "Entre as poucas palavras que você compreende, há vestígios de canto,
    tentando acertar as notas da lira."

    $Asterion.change ("emotion", "surprise")

    "Quando ele volta o foco em ficar pronto para sair, lira na mão, seu rosto se contorce
    em surpresa ao ver que você ainda está lá."

    $Asterion.change ("emotion", "embarrassed")

    asterion "Ah...{w=0.2} Mestre,{w=0.3} eu achei que...{w=0.4} Uhm..."

    asterion "Obrigado mais uma vez..."

    you "O que você estava dizendo antes, se não se importa que eu pergunte?{w=0.2} \"Ay noy noy\"?"

    $Asterion.change ("emotion", "neutral")

    asterion "É,{w=0.2} hã,{w=0.2} Alceu.{w} En oinoi aletheia."

    asterion "Ele...{w=0.2} ele cantava muito sobre beber.{w=0.2} Que há verdade no vinho."

    $Asterion.change ("emotion", "embarrassed")

    asterion "Quer dizer... beber me ajudou a relaxar um pouco.{w=0.2}
    Eu não sabia o que dizer, mas ajudou."

    pause 1.0

    you "Hm.{w=0.2} Fiquei curioso, o hotel não traduz o que as pessoas dizem?{w=0.2}
    Eu não deveria ter ouvido a tradução?"

    you "Mas suponho que isso seja assunto para outra hora.{w=0.2}
    Que tal irmos para o salão juntos?"

    $Asterion.change ("emotion", "sad")

    asterion "Hum."

    "Astério tensiona a mandíbula.{w=0.2} Ele olha para seus pés, como se estivesse perdido em pensamentos."

    asterion "Sim,{w=0.2} Mestre,{w=0.2} muito bem."

    scene bg black
    with Dissolve(1.0)

    "Você e Astério saem, lado a lado."
    $Asterion.change ("emotion", "neutral")

    scene bg staircase
    show Asterion:
        xalign 0.5 zoom 1.0 yalign 1.1 xzoom -1
    show Asterion:
        ease 0.2 yalign 1.0
        ease 0.2 yalign 1.3
        pause 1.0
        repeat
    with Dissolve(1.0)

    "É noite lá fora.{w=0.2} A grande escadaria está envolta em escuridão, mas um vislumbre
    na direção dos céus revela as estrelas cintilantes — um imenso mar espumoso, movendo-se muito lentamente."

    "Murmúrios e música vêm para cima do andar térreo."

    you "Então,{w=0.2} o que você tem em mente para hoje?"
    $Asterion.change ("emotion", "contemplative")

    asterion "Apenas algumas das músicas antigas que conheço.{w} Nada especial,{w=0.2}
    na verdade, elas podem soar estranhas para as sensibilidades modernas."

    asterion "Elas são...{w=0.2}hum..."
    $Asterion.change ("emotion", "sad")

    "Astério suspira e olha para sua lira. Ele esfrega o polegar na lateral dela,
    para frente e para trás, seguido por um sacudir de orelhas."

    "Há um ritmo aderido a ele — seu polegar é duas vezes mais rápido que seus passos escada abaixo,
    suas orelhas sacodem a cada terceiro passo e seu rabo balança a cada cinco."

    show Asterion:
        ease 0.1 yalign 1.0
        ease 0.1 yalign 3.0

    $Asterion.change ("emotion", "surprise")

    "Então ele quase tropeça — ainda não está acostumado a seu novo centro de gravidade.{w=0.2}
    Ele coloca uma mão no corrimão e bufa."

    show Asterion:
        ease 0.5 yalign 1.0
        ease 0.1 yalign 3.0

    "Assim que ele dá o próximo passo, tropeça novamente.{w=0.2} Você estende a mão para segurar a mão dele."

    $Asterion.change ("emotion", "sad")
    show Asterion:
        ease 1.0 yalign 1.0

    you "Tem certeza que não tem nada de errado?"

    asterion "Sinto muito,{w=0.2} Mestre,{w=0.2} acho que estou pensando demais."

    "Você tenta soltar a mão dele — agora maior e mais brusca que antes —
    mas os dedos dele se entrelaçam entre os seus e resistem, pelo menos até que ele o solte com cuidado.{w=0.2}
    Ele respira fundo e parece se concentrar."

    scene bg black
    with Dissolve(1.0)

    "Vocês chegam ao andar térreo e seguem pelo corredor que leva ao salão.{w=0.2}
    As luzes ainda não estão acesas, então você e Astério caminham na escuridão mais uma vez."

    $Asterion.change ("emotion", "contemplative")

    "Mais à frente, há uma fenda de luz fluindo da porta do salão —
    e mais além está o corredor que leva vocês até a cozinha, onde você encontrou
    Astério poucos dias atrás."

    "As risadas e vozes dos hóspedes, os gritos barulhentos de Luke, a voz estrondosa de Kota...
    E agora seus passos misturados com o bater de cascos de Astério."

    "O andar dele é maior que o seu agora — movimentos lerdos e pesados, cada passo
    o balançando como um pêndulo de um lado para o outro."

    "Ainda assim, vocês dois encontram um ritmo comum: três seus para cada segundo passo dele."

    "Vocês estão quase lá agora. Você olha para o minotauro — ele olha para o lado, depois de volta para você,
    e leva o olhar para seus pés."

    $Asterion.change ("emotion", "contemplative")
    scene bg oldlobby
    show Asterion:
        xalign 0.5 yalign 1.0 xzoom 1
    show blackback:
        alpha 0.6
    with Dissolve(2.0)

    if Build3Ending == 'good':

        you "Tenho certeza de que você vai se sair bem, Astério, mas boa sorte.{w=0.2} Vou pegar
        um copo d'água para você quando subir no palco."

        $Asterion.change ("emotion", "embarrassed")

        "Você se vira para andar em outra direção, mas a mão do minotauro segura a sua.{w=0.2}
        Ele puxa você para perto com um puxão rígido e o envolve com o outro braço."

        show Asterion:
            ease 1.0 zoom 1.05 yalign 1.1

        "Ele aperta você, mas de uma forma quase glacial, suave, misturada com o calor
        de sua pele e respiração ao seu redor."

        "Apesar de seu novo corpo gigante, Astério é macio, seu pelo é como seda contra sua
        pele e espalhando ao seu redor um perfume suave — sem fragrância, exceto por um
        toque distante de pelo quente e pele bronzeada."

        "Seus cascos se embaralham, não sabendo onde pisar, mas cada movimento é tímido —
        eles arranham o chão em vez de pisoteá-lo, com medo até de roçar em seus sapatos."

        "Ele apoia a cabeça em cima da sua, com o focinho em particular acariciando seu cabelo.{w=0.2}
        Ele resmunga algo e leva algumas tentativas para dizer em voz alta."

        $Asterion.change ("emotion", "relieved")

        asterion "{size=-4}Obrigado...{w} Obrigado.{/size}"

        "Há calor ao seu redor, mas também tensão; os movimentos de Astério permanecem espasmódicos e rígidos.{w}
        Sua própria surpresa passa, entretanto.{w=0.2} Você responde ao abraço dele da mesma maneira."

        "Sua cauda sacode e balança em resposta — em seguida, cai.{w=0.2} Um murmúrio estrondoso escapa da
        garganta dele conforme você aperta a barriga."

        "A tensão se dissipa.{w=0.2} Os ombros relaxam, seus braços se ajustam e moldam em torno de você,
        o peso da cabeça dele cai sobre a sua.{w} Ele respira através de seu cabelo e acaricia você
        — seu nariz rosa é macio, até mesmo um pouco molhado."

        "Você o aperta com mais força, mas com o mesmo ritmo glacial que os movimentos dele exibiram.{w=0.2}
        Você se depara com outro grunhido, embora agora possa dizer que não é um de queixa."

        $Asterion.change ("emotion", "mooing")

        asterion "Muuu..."

        "Vocês dois permanecem bem quietos enquanto as vozes mais adiante celebram e comemoram suas
        próprias vitórias, suas breves noites de descanso, ou talvez até mesmo um novo lar."

        $Asterion.change ("emotion", "relieved")

        "Fora de vista, cercados por luz, eles celebram.{w=0.2}
        E aqui, nesta escuridão aveludada, você e Astério respiram os aromas um do outro."

        show Asterion:
            ease 1.0 zoom 1.0 yalign 1.0

        "Quando chega a hora de se despedir, vocês dois relaxam as pontas dos dedos, depois as mãos e,
        finalmente, os braços, à medida que aos poucos se desenbrulham."

        "E acaba, a única evidência que sobrou do gesto —
        além da doce memória — é a respiração acelerada e superficial do minotauro."

        "Ele olha para suas roupas, agora amassadas, e se move para arrumá-las antes
        de olhar para você, depois para o salão e a lira."

        $Asterion.change ("emotion", "embarrassed")
        "O momento da partida está próximo; é hora de o concerto começar.{w}
        Ele vira para o lado na metade do caminho,{w=1.0} e então gira de volta para você,{w=0.2}
        boquiaberto e olhos procurando palavras.{w=0.2} Aquela rigidez retorna gradualmente para seus movimentos."

        "Ele resmunga alguma coisa. Possivelmente outro \"obrigado\", embora ele pareça transitar
        para outra frase mais complexa que você não conseguiu entender."

        you "Obrigado, eu gostei disso.{w=0.2} Você não precisa ficar todo nervoso, foi legal da sua parte."

        $Asterion.change ("emotion", "smiling")
        you "Mais uma vez, obrigado."

        asterion "Hum.{w=0.3} Hm.{w=0.2} O —{w=0.2} hm...{w} Obrigado.{w=0.2} Também."

        "A agitação crescente não se dissipa, mas também não aumenta."

        you "Então,{w=0.2} sinta-se livre para me abraçar de novo{w=0.2} se quiser.{w} Posso fazer o mesmo com você?"

        $Asterion.change ("emotion", "relieved")

        asterion "Bem...{w=0.2} hah.{w} Sim,{w=0.2} Mestre,{w=0.2} seria muito agradável.{w}
        Obrigado."

        "Algo muda em seus olhos.{w=0.2} Havia uma nitidez lá,
        talvez algum grau de medo.{w} Ondulava para dentro e para fora, como uma chama resistindo ao vento,
        desde que você o libertou da câmara fria."

        "Mas agora sumiu, e ele enxerga você."

        $Asterion.change ("emotion", "contemplative")

        asterion "Às vezes olho para você e é como se eu estivesse vendo um velho amigo
        que conheci em Creta.{w=0.2} Como uma pequena janela para o passado."

        you "E é uma coisa boa?"

        pause 1.0

        $Asterion.change ("emotion", "excited")

        asterion "Sim.{w=0.2} Amigos são uma coisa muito preciosa, [player_name]."

        $Asterion.change ("emotion", "smiling")

        pause 1.0

        asterion "Talvez eu queira acreditar.{w=0.2} Eu estava tão confuso hoje...{w=0.2}
        Mas o vinho deve ter me soltado, e agora..."

        asterion "Estou divagando, eu sei.{w=0.2} Me perdoe."

        "As orelhas do minotauro sacodem à medida que as vozes dentro do salão ficam mais barulhentas.{w=0.2}
        Ele se move, como se estivesse voltando para a porta, mas os olhos dele não querem deixar você."

        $Asterion.change ("emotion", "contemplative")
        show Asterion:
            ease 1.0 zoom 1.05 yalign 1.1

        "O minotauro respira fundo novamente. Com um movimento quase idêntico,
        quase ensaiado, ele puxa você para perto de novo em seus braços— porém mais gentil,
        mais deliberado."

        "Ele segura você apenas por um segundo, curto demais para você responder na mesma moeda.
        Antes que perceba, ele o deixa sair de seu breve abraço novamente."

        show Asterion:
            ease 1.0 zoom 1.0 yalign 1.0
        "Ele não exatamente encontra seu olhar."

        $Asterion.change ("emotion", "horny")
        asterion "Você, é, disse que eu podia abraçá-lo de novo...{w=0.2} se eu quisesse…{w=0.2} então…"

        "Você ri."

        you "Eu disse mesmo, e falei sério. Então… obrigado de novo. Podemos entrar?"

        $Asterion.change ("emotion", "smiling")
        "Ele acena com a cabeça para você. Ele sorri, para si mesmo. E ele acena, novamente, para você."

    else:
        "Enquanto vocês olham nos olhos um do outro, ele endireita os ombros como um fio tenso.{w=0.2}
        Seus olhos permanecem gentis, entretanto— talvez mais gentis quando seu olhar encontra-se com o dele."

        "Ele parece muito aliviado quando você desvia o olhar, no entanto."

        "Há um olhar consternado e, em seguida, um aceno de cabeça para si mesmo."

        $Asterion.change ("emotion", "neutral")

        asterion "Você reza, meu senhor?"

        menu:
            asterion "Você reza?"
            "Sim":
                you "Sim.{w} Nem sempre,{w=0.2} mas...{w=0.2} sim."

                $Asterion.change ("emotion", "contemplative")
                asterion "Talvez nossas orações tenham sido atendidas, então, e seja lá qual deus
                tenha as ouvido, cuidou para o evento de nosso encontro."

                "Ele inclina a cabeça."
            "Não":
                you "Acho que eu nunca rezei de fato."

                $Asterion.change ("emotion", "contemplative")

                asterion "Ah, claro que não.{w=0.2} Você parece levar a vida com suas próprias mãos."

                "Ele inclina a cabeça ligeiramente."

                $Asterion.change ("emotion", "smiling")

                asterion "Talvez eu deva orar por você também, então.{w=0.2} Seria um acréscimo
                adequado aos meus deveres."

                "Ele parece quase orgulhoso de dizer isso."


        asterion "Que seu mandato seja próspero, senhor."

        you "Tenho certeza que vamos nos dar muito bem, Astério.{w} Vamos cumprir a
        missão desse hotel, certo?"

        "O vinho deve tê-lo relaxado a essa altura, conforme uma espécie
        de contente gentileza entra em suas palavras."
        $Asterion.change ("emotion", "smiling")
        asterion "O que quer que o bom mestre diga."

    "Você dá um passo à frente e, lado a lado, os dois entram."

    $LoungeBlobs = [True, 2]
    scene Lounge
    if first_guest == "Luke":
        show LoungeLight
    show Asterion behind LoungeLight:
        xalign -1.3 yalign 1.0 zoom 1.0
        ease 2.0 xalign 0.5
    with Dissolve(1.0)

    you "Bem, o palco deve estar pronto. Você quer ir se preparar?"

    $Asterion.change ("emotion", "contemplative")

    asterion "Ah, sim, eu deveria fazer isto."

    show Asterion:
        ease 3.0 xalign 2.3

    pause 3.0

    "A atmosfera no salão hoje à noite parece festiva e animada; muito longe de quando você
    veio aqui pela primeira vez."

    if first_guest == 'Luke':
        "Luke está administrando o bar servindo seu cardápio
        de costume enquanto grasna, dança e sarra ao ritmo da música."
        if BundleSacrifice == 'Force':
            "Kota senta em uma das mesas, apertando seu ombro e cercado por
            hóspedes curiosos, contanto a história de como ele arrancou um tesouro
            das mãos de um monstro."
        else:
            "Kota, mais confortável no bar que nos dias anteriores,
            está sentado com os alunos do Oriente Médio e tendo uma discussão apaixonada
            sobre as diferenças entre a prosódia árabe e japonesa."
    else:
        "Kota, que em qualquer outro dia administraria seu restaurante como o orgulhoso capitão de um
        navio apertado, não se incomoda com o falatório e o clima festivo do salão."
        if BundleSacrifice == 'Force':
            "Luke se senta ao lado dos trabalhadores uruguaios, falando com uma voz
            mais áspera, mas recontando como ele chutou o traseiro inexistente da cobra."
        else:
            "Luke se senta perto dos trabalhadores uruguaios. Ele está chegando um pouco perto
            demais do mais corpulento da dupla, rindo de todas as suas piadas e fazendo algumas próprias
            sempre que possível, para desgosto do outro."

    if not rewards.is_obtained('WiFi'):
        #This is a scene that plays out if the wifi has still not been enabled by this date.
        "Quanto a Ismael e Greta..."
        show Greta:
            xalign 1.3 yalign 1.1 xzoom -1 zoom 1.0
            ease 1.5 xalign 0.5

        "Greta" "[player_name]! {w=0.2}[player_name]!{w=0.2} Ah, estou tão feliz que pude encontrar você agora."

        "Greta" "Eu só queria...{w=0.2} agradecer por tudo."

        show Greta:
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1

        "Greta" "Eu me diverti tanto aqui, o momento da minha vida!"

        "Greta" "Vou contar essa história para os meus netos — encontrar um hotel no meio de
        um deserto e estudar como replicar eletrônicos com magia!{w}Em uma bacia, no porão!"

        "Greta" "Muito obrigada por tudo.{w=0.2} Ismael e eu vamos embora amanhã,
        então eu tinha que dizer adeus."

        you "De nada, Greta.{w=0.2} Fico feliz que você tenha se divertido tanto, mas..."

        "Greta" "Espere, não terminei ainda, [player_name].{w=0.2} Verifique seu celular, por favor."
        play sound "sfx/vibratephone.mp3"
        "Você tira seu celular do bolso e...{w=0.2} não há nada diferente, ainda sem sinal, exceto..."

        "Você olha mais de perto e vê que agora há uma rede wi-fi."

        you "É... colocaram o nome de \"Hotel Minotauro\"?"
        stop sound
        show Greta:
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1
        "Greta" "Isso mesmo!{w=0.2} Vamos lá, é fofo!{w}
        E a senha é fácil, é \"Netzwerkdurchsetzungsgesetz.\""

        pause 1.0

        show Greta:
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1
        #show greta doing a little hop

        "Greta" "Ok,{w=0.2} apenas me dê seu celular."

        "Você dá a Greta seu celular.{w=0.2} Ela escreve a senha para você."

        "Greta" "Não se preocupe,{w=0.2} anotei a senha em um papel que deixei no cômodo da bacia."

        "Greta" "Então, no geral, eu tive uma ideia de última hora e nós...{w=0.2} nós conseguimos fazer o wi-fi funcionar,
        {w=0.2} mas teve uma grande confusão sobre como conseguir um provedor de serviços de internet e..."

        "Greta" "Podemos estar...{w=0.5}ha ha...{w=0.5} podemos estar usando o provedor de internet
        para o qual os uruguaios trabalham, ok?"

        "Greta" "Então, as coisas são bem improvisadas nesse sentido, sabe.{w=0.2}
        A banda larga é muito limitada.{w} Mas funciona!{w=0.2} Está tudo em ordem."

        "Greta" "...Mas se algo der errado, receio não ter a menor ideia de como consertar, haha."

        "Greta" "Eu não sou uma engenheira de redes. Dá um tempo, ok?"

        "Greta" "Você pode querer enviar um e-mail à central de vez em quando,
        e também vai ter que pagar as contas.{w} Mas tenho certeza que vai ser fácil para você,
        com um hotel mágico e tudo."

        you "Uau, obrigado Greta. Eu não sei o que dizer."
        show Greta:
            ease 0.2 yalign 1.0
            ease 0.2 yalign 1.1
        "Greta" "Ah, não foi nada, [player_name].{w=0.5} Isso tudo foi muito emocionante.
        Espero podermos nos encontrar novamente no futuro, tenho tantas ideias{nw}"

        show Greta:
            yalign 1.0
            ease 1.5 xalign -1.3

        "Greta" "EI! Onde você pensa que está indo?"

        "Greta corre atrás de Ismael, o qual já está colocando os fones de ouvido
        e tentando abandonar o salão enquanto ela está distraída conversando com você."

        $obtain_reward('WiFi', 'RD', subtract=False)
        $add_file('Tech', "WiFi")

        play sound "sfx/asterionchord.mp3"
        "Contra todas as possibilidades, você conseguiu estabelecer {color=[UIColorOrange]}Acesso à Internet{/color}
        no hotel. Agora você pode ver seus projetos de tecnologia completos na aba de tecnologia na tela de
        {color=[UIColorOrange]}Arquivos{/color} no menu de pausa."

    else:
        "Ismael e Greta estão sentados em uma das mesas ao longe. Ele está colado
        no celular, assistindo a algo, enquanto ela o pressiona para socializar."

    "E pensar que, apenas uma semana atrás, este lugar estava morto e manchado de sangue.{w=0.2}
    Que grande conquista."

    "Você se volta para Astério conforme ele sobe no palco."

    "O minotauro cobre os olhos — as luzes olham para ele, causando uma dor maçante em
    sua nuca."

    "Ele olha para baixo, para os degraus que conduzem à plataforma, e vai passo a passo,
    enquanto se arrasta com o novo peso de seu corpo."

    "Vinte ou mais pares de olhos estão fixos nele — em suas feições de touro, seus chifres,
    seu eu recém-curado."

    "Já faz um tempo desde a última vez que ele esteve sob os holofotes desta maneira.
    Quando ele era criança, idosas vinham e colocavam flores em seus chifres,
    dezenas de mulheres em sucessão, e ele cobria os olhos da mesma forma na época."

    "Elas pediam suas bênçãos, os homens imploravam que ele abençoasse suas colheitas,
    até que se tornasse demais. Ele chorava, e seu pai ou ama de leite o puxavam
    e o repreendiam por ter feito birra."

    "Ele segura a lira contra seu peito.{w=0.2} Uma corda roça sua camisa
    e solta um zumbido — isto envia uma faísca de confiança.{w}
    Ele afasta o braço, puxa o banquinho, e se senta."

    if Asterion.neckwear == 'neckerchief':
        "Astério ajusta o lenço que você fez para ele, o exibindo com orgulho
        para todos os seus hóspedes."
    if Asterion.neckwear == 'medallion':
        "Astério olha para o peito e vê o medalhão que você fez para ele.
        Ele dá uma risadinha e não se importa se parece ridículo: como você previu,
        os olhos agora realmente correspondem aos dele."
    if Asterion.armwear == 'wristband':
        "O olhar de Astério se volta para sua mão— mais especificamente para a pulseira que
        você fez para ele, e ele sorri."

    "Ele olha para os hóspedes — para cada um deles em sucessão, depois para você."

    asterion "Ei...{w=0.3} Olá, todo mundo."

    asterion "Eu... eu acho que deveria me apresentar primeiro.{w=0.2} Meu nome é Astério e,
    como podem ver, eu não sou exatamente... humano."

    asterion "Eu trabalho aqui, no hotel.{w=0.2} É onde passei a maior parte da minha vida, de certa forma."

    asterion "Hã..."

    pause 1.5

    "Ele traça o polegar ao longo da corda novamente, deixando-a
    vibrar no ar, sem realmente puxá-la."

    asterion "Até semana passada, este lugar estava abandonado. Apenas eu estava aqui.{w=0.2}
    Fico feliz de ver pessoas novamente, tantos rostos novos..."

    asterion "Então...{w=0.2} Entre vocês estão nossos primeiros hóspedes após a reabertura,
    e eu sei que alguns de vocês vão embora amanhã de manhã.{w}
    Então nós...{w=0.2} então pensamos que seria bom fazer algo especial."

    asterion "Isto é para vocês, nossos hóspedes."

    pause 2.0

    if Build3Ending == 'good':
        asterion "Mas...{w} estou dedicando a um amigo."
    else:
        asterion "Mas...{w} estou dedicando ao nosso excelente anfitrião, Mestre [player_name],
        cuja gentileza nos permitiu desfrutar desta noite em primeiro lugar."

    asterion "Espero que vocês aproveitem esta noite, e quando partirem...{w=0.2}
    que levem com vocês boas lembranças."

    asterion "Se qualquer dia precisarem de um lar, ou apenas um lugar para descansar, nossas portas estão abertas."

    "O minotauro posiciona sua lira e respira."

    scene CG4
    with Dissolve(1)

    pause 2.0

    "Ele coloca as pontas dos dedos ao longo de algumas cordas em um lado da lira e dedilha
    com a outra mão."

    "Ele começa a cantarolar. Fica mais alto por meio de notas tristes do
    ritmo cântico. Ele diz alguns fragmentos de palavras enquanto começa a
    dedilhar a melodia que cantarolou."

    "Ele cantou apenas a última linha — um olhar de consternação e preocupação
    transformando-se em uma calma simples conforme as últimas notas se silenciam."

    asterion "Eu...{w=0.3} Espero que não se importem por eu não ter cantado nesta...{w} Descobri,
    assim que entrei no palco, que não conseguia lembrar da letra,
    então esperava que as cordas sozinhas bastassem."

    asterion "Não tinha tanta certeza se as musas estavam comigo esta noite.
    Mas as nove de Hélicon {i}estão{/i} aqui, ao que parece, e elas merecem reconhecimento antes
    que eu continue."

    asterion "Meu irmão mais velho me ensinou a tocar, e uma das primeiras coisas que você faz em uma
    apresentação é invocar as musas, ele disse."

    asterion "Esta noite elas não acharam por bem remover a música completamente de mim
    e me fizeram lembrar do meu irmão. Que a reverência de minha música com elas seja sempre
    como suas bençãos são para mim."



    asterion "Então... eu as agradeço,{w=0.2} Musas, que não ficaram muito zangadas comigo;{w=0.3}
    por favor, auxiliem minha música."

    "Ele toca outra melodia — uma única linha de notas se estendendo através
    do salão,{w=0.2} cordas soltas para tocar."

    "Depois de perceber o quanto a melodia tem o contorno e a cadência do discurso,
    você ouve seus dedos pararem algumas cordas.{w=0.3} Ele dedilha novamente e começa a cantar,
    colocando palavras no que acabou de tocar."

    "Não é exatamente um berro, mas sua garganta bovina está aberta enquanto sua voz entoa um hino épico."

    "Um lírico."

    "Uma canção sobre beber."

    "Enquanto a música perdura ele permanece desavergonhado, sua presença flui e cativa.
    Seu peso nunca ficou menos pesado. Entre cada um desses fatos, entretanto,
    a timidez de Astério retorna à medida que ele explica sobre o que é a música."

    "Mas enquanto ele canta e toca, não está constrangido.
    Seus olhos não estão fechados por timidez, mas por se sentir como si mesmo."

    asterion "Eu... Obrigado por virem.{w} Espero que tenham gostado de sua estadia e...{w=0.3}
    Obrigado, mais uma vez."

    pause 2.0

    scene bg black
    with Dissolve (2.0)
label Build3End:
    stop music fadeout 4.0
    pause 5.0
    play sound "sfx/vibratephone.mp3"
    pause 5.0

    $P.change("emotion", "deepthinking")
    if player_background  == "speedrunner":
        $P.change("clothes", "cia")
    else:
        $P.change("clothes", "dressshirt")
    $P.change("rightarm", "thinking")
    $P.change("leftarm", "hip")
    stop sound
    play sound "sfx/beep.ogg"
    pause 3.0
    pq "Venho tendo os sonhos mais estranhos ultimamente,{w=0.2} pai."

    scene officeP
    show blackback:
        alpha 0.5
    show P behind blackback:
        xalign 0.5 yalign 1.0
    with Dissolve(3.0)
    pause 1.0

    pq "Eu enxergo dentro de uma sala escura, parece algum tipo de templo da Grécia Antiga
    ou algo assim.{w=0.3} No meio dela tem um grande pedaço de pedra roxa."

    $P.change("emotion", "thinking")

    pq "Eu venho tendo eles desde que o vô morreu e vimos toda aquela coisa sobre o testamento dele.{w=0.3}
    Mas ultimamente, é diferente..."

    $P.change("emotion", "dominant")
    $P.change("rightarm", "hip")

    pq "Tinham pessoas lá{w=0.2} — várias delas, na verdade.{w}
    E,{w=0.2} sabe, uma delas era...{w} um minotauro."

    pause 1.0

    $P.change("leftarm", "loose")
    $P.change("emotion", "content")

    pq "Exatamente como o vô disse."

    play sound "sfx/phonevoice1.mp3"
    pause 2.0

    $P.change("emotion", "deepthinking")

    pq "Tenho pensado nisso, sim.{w} Quer dizer...{w=0.4} não é como se eu tivesse
    nada melhor para fazer agora."
    stop sound
    play sound "sfx/phonevoice2.mp3"
    pause 2.0

    $P.change("emotion", "sad")

    pq "Eu meio que,{w=0.2} recebi uma oferta de emprego,{w=0.2} mas eles não têm certeza ainda.{w}
    E eu tenho algumas economias."

    $P.change("emotion", "deepthinking")

    pq "Bem, estive pensando em fazer uma visita ao vô.{w=0.3} Uma viagenzinha de carro.{w}
    Quem sabe, talvez..."

    $P.change("emotion", "content")
    $P.change("leftarm", "hip")

    pq "Talvez as histórias sobre aquele hotel fossem verdadeiras, afinal?{w=0.3}
    Eu quero descobrir por conta própria."

    play sound "sfx/phonevoice1.mp3"
    pause 2.0
    $P.change("emotion", "neutral")
    $P.change("rightarm", "pointing")
    play sound "sfx/phonevoice2.mp3"
    pause 2.0

    pq "Olha, isso é uma coisa muito cruel de se dizer sobre o seu próprio pai.{w=0.3}
    Você me ensinou coisa melhor."

    play sound "sfx/phonevoice1.mp3"
    pause 2.0

    $P.change("emotion", "tired")

    pq "Escuta, nada disso vai me impedir.{w=0.3}
    É melhor você economizar a saliva."

    play sound "sfx/phonevoice2.mp3"
    pause 1.0

    $P.change("emotion", "wrath")
    $P.change("rightarm", "hip")

    pq "É melhor eu desligar agora.{w} Tchau."
    stop sound
    play sound "sfx/beep.ogg"
    #click sound effect, telephone hanged up

    pause 2.0

    $P.change("emotion", "tired")

    pq "Bostinha."

    $ renpy.force_autosave(True, True)
    hide P
    with Dissolve(0.1)
    $P.change("tail", "raised")
    show P behind blackback
    with Dissolve(0.1)
    pq "Eu vou te mostrar."

    scene bg black
    with Dissolve (2.0)

#end of build
    jump build04
