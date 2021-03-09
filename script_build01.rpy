##############################################################################
#                      PROLOGUE: GETTING THE DEED
##############################################################################

label prologue:
    $chapter = "Prólogo"
    stop music
    play music "music/Calliopeia.ogg"
    scene bg black
    with Dissolve(.5)
    $show_quick_menu=False

    #the game starts with a poem that's different with each playthrough.

    if persistent.first_save:
        $throwaway1 = [["{i}(...)\n\"Além do mar, você deve encontrar a ilha de\nCreta, da qual o tirano Minos exigiu tributo\nem forma da melhor juventude de Atenas.\n"
        "{i}Após a chegada, eles foram enviados para um local\nabominável erguido por Dédalo, o grande arquiteto.\nEra um labirinto no qual vivia o touro de Minos.",
        "{i}O híbrido foi concebido quando a esposa do tirano,\numa ninfa outrora sagrada, foi acometida por uma\nmaldição lasciva, submetendo-a à estocada do touro."],
        ["{i}O resultado foi o monstro chamado Astério,\nmeio touro, meio humano. Não possuindo lugar na\nnatureza, recorreu ao consumo de carne humana.",
        "{i}Ele viveu no labirinto, alimentando-se de\nAtenienses. Porém, entre os sacrifícios, veio um\nnotável herói: Teseu, futuro rei.",
        "{i}O ateniense de olhos brilhantes cativou as\npaixões da princesa Ariadne, a qual revelou\no segredo para derrotar o minotauro.",
        "{i}Mais tarde, a espada de bronze do príncipe vitorioso brilhou\nesplendidamente sob o sol enquanto ele e a princesa\nnavegavam para longe de Creta, em direção a Naxos.\"\n(...)"]]

    else:
        $throwaway1 = [["{i}\"Eu canto sobre o Astério de Olhos Estrelados, herdeiro do dia e da noite,\ndo mar e da terra, cuja história eu testemunhei e as Musas agora cantam.\nSenhor Zeus, encoraje suas filhas a concederem uma beleza tão doce\nquanto fora a incessante hospitalidade do filho de Poseidon."]]

        $RNJesus = renpy.random.randint(1, 6)

        if RNJesus == 1:
            $throwaway2 = ["{i}Sua mãe era uma ninfa, seu progenitor era Poseidon, dado a forma mortal,\nseu pai era o Rei de Creta, Mestre Arqueiro dotado de visão de longa distância.\nEle segurou a mão e seguiu os passos do poderoso Androgeu,\nflor de Creta, arrancada muito cedo pelas mãos invejosas do além-mar.",
            "{i}Astério tinha cascos sonoros, cujas batidas traziam alegria aos corredores,\ne seus chifres emolduravam a lua enquanto colhíamos açafrões.\nQuando a água salgada tocava seus tornozelos, conchas brotavam da areia\ne os cardumes de peixe nadavam ao redor em honra ao icor de Poseidon.",
            "{i}Sua lira, abençoada por Apolo, dedilhava apenas melodias doces\ne, em sua mesa, os convidados sempre encontrariam seu melhor vinho."]

        elif RNJesus == 2:
            $throwaway2 = ["{i}Injusta era a sua sentença, mas o espírito do menino não era nada senão piedoso.\nEle cuidou da chama de Héstia, para ela toda primeira e última libação é devida.\nCada convidado ganhou a completa graça de sua hospitalidade, como Zeus comanda.",
            "{i}Ele era acalentado entre os fazendeiros e suas esposas,\nque engrinaldavam seus chifres com açafrão e ditamno quando ele era uma criança.\nO Rei Minos gabou-se da arquearia de seu filho, e quando Astério alcançou\no poder da idade adulta, ele apreciava também seu domínio sobre o Lábris.",
            "{i}Suas costas, tão largas quanto as estepes, explodiam de poder enquanto seus olhos estrelados\ncarregavam apenas bondade e generosidade, condizentes com sua linhagem sagrada."]

        elif RNJesus == 3:
            $throwaway2 = ["{i}Seus detratores o acusavam de misantropia, covardia, sacrilégio.\nEle se alimentou da carne de sua própria espécie, gritaram em três vozes.\nDiante do rei, eles o puxaram pelos chifres e cuspiram incontáveis venenos.",
            "{i}Rei Minos, que amava seu povo, cuja visão era a frente de seu tempo,\nmas não omissora de mentiras, sentenciou o menino a guardar um santuário sagrado\nno labiríntico coração de Creta."]

        elif RNJesus == 4:
            $throwaway2 = ["{i}Sua casa possui tantas portas quanto há estrelas em seus olhos\ne, mesmo assim, nenhuma trancada, tão como costumava ser seu coração.",
            "{i}No centro de tudo há um templo, um com uma bacia rachada,\nonde antes enfureceu um grande e suave incêndio em homenagem a Héstia.\nA bacia era cercada por uma piscina de água cristalina, mas em suas bordas\ncresceram cracas, trazidas pelo icor navegante do príncipe."]

        elif RNJesus == 5:
            $throwaway2 = ["{i}Astério de olhos estrelados, último príncipe de Creta, ele era amado,\nmesmo que a injustiça fosse seu jugo e a calúnia seu destino.",
            "{i}Seus detratores no exterior diriam que tributos foram enviados à sua casa\npara saciar sua suposta fome canibal. Mas nós realmente testemunhamos\nisso, todo ano o Rei Minos exigiria tributos pelo mar,\nmas na forma de riquezas, como era por seu direito de conquista.",
            "{i}Um vilão veio entre os tripulantes da embarcação, ninguém menos\nque o incansável príncipe ateniense que sequestrou Ariadne,\nassassinou Astério de olhos estrelados e profanou sua residência."]

        else:
            $throwaway2 = ["{i}Musas, sempre tão gentis com meu querido Astério, por favor, concedam a este guardião\num último suspiro de música antes que o talento me deixe completamente.\nOuvir sobre o homem que chamei de irmão uma última vez.",
            "{i}Ele amava o cheiro de ditamno lanoso, quando seus deveres principescos\no sobrecarregavam, Androgeu e eu engrinaldávamos seus chifres com flores.\nSua mãe era uma ninfa, enlouquecida na flor da juventude e\nque, mesmo assim, às vezes tentava amamentar o menino de nariz branco.",
            "{i}Seu pelo era imaculado, de um fino tom branco que refletia a luz do sol três\nvezes mais, de forma tão intensa quanto o mais finamente polido espelho da ilha,\nexceto pela marca de nascença em forma de estrela que inspirou seu nome.",
            "{i}Ele tinha um par de chifres nos quais se poderia emoldurar as estrelas e a lua.\nSuas mãos tinham nós tão ásperos nos dedos, ainda assim ele\nconseguiu ser um arqueiro tão preciso que o Rei gabou-se de seu talento."]

        $throwaway1.append(throwaway2)

        $throwaway1.append(["{i}Adeus, herdeiro estrelado do Sol, filho terrestre de Poseidon.\nPenas flutuam na superfície do Estige enquanto você segue seu caminho\npara o principesco Androgeu em Elísio, local de descanso dos heróis.\nA noite estrelada e o cosmos se seguiram, mas não meu irmão.",
        "{i}Então, adeus, orgulhoso filho de Poseidon, cujas cinzas pontilham o mar,\ne obrigado, Musas de doce canto, que concederam talento a este camponês,\nmesmo que por uma única noite de luto.\nLembrarei de vocês e de outra música também.\""])

        $throwaway1.append(["Autor desconhecido (presume-se que seja Deucalião), estimado em 1600 A.C.\nDesenterrado por Matias Corges em Creta."])

    pause 2.0
    call screen Poem(throwaway1)
    pause 1.0

    # Prologue. It'll branch into two scenes that come together
    # after a few lines. This choice is for flavor and doesn't change anything
    # in the long run.
    # The player picks his name and background.

    call screen ChapterTransition("Prólogo", "A Escritura")
    pause 0.5

    $save_name= "Prólogo"
    $show_quick_menu=True
    #New version for the game's intro. This time around there is no truck stop/airport choice.
    #It happens in a bus station, because I figured it would be the most relatable form
    #of transportation.

    pause 1

    "Você não lembra muito sobre aquela noite."

    pause 1.0

    #show bg threshold
    scene bg bus_stop
    show blackback:
        alpha 0.5
    with Dissolve (1)

    "Suas viagens o levaram para longe de casa. {w}Você estava meio morto depois
    de todas as noites se revirando sob tetos desconhecidos."

    "Eram 3 da manhã e era como se você não tivesse dormido em uma cama apropriada por pelo menos duas noites.
    Você estava usando todo o espírito que lhe restava para continuar, reduzindo
    sua mente ao pó."

    "Mas em breve isto acabaria. Você estava tão perto de casa -- apenas mais uma
    viagem de ônibus, uma longa o suficiente para uma boa noite de sono."

    "Até lá, no entanto, você precisava se manter acordado. Você levantou e
    saiu para explorar a estação."

    "Todo o lugar passava uma visão lamentável. Não havia muito, e o pouco
    que restava estava mal conservado:{w}
    o banheiro uma atrocidade, o piso do saguão manchado pelo
    tempo, o asfalto nos terminais rachando."

    $myVar=2

    "Ainda assim, ele foi construído para durar, decorado com pilares
    de obsidiana bruta, cortados diretamente da própria terra, e ladrilhos de mármore
    polidos em padrões labirínticos."

    "As paredes eram alinhadas com estátuas em um estilo grotesco, suas
    expressões exageradas trancadas em gritos de olhos arregalados."

    "O teto era coberto com reproduções treliçadas de pinturas;
    {i}A Criação de Adão{/i}, de Michelangelo e, um pouco mais acima, {i}Guernica{/i},
    de Picasso."

    "O saguão aparentava extender-se para sempre em diante, forrado em ambos os lados
    por filas de lojas fechadas. A música de elevador tocando de algum
    alto-falante oculto era distração o suficiente para mantê-lo no caminho."

    scene bg bar
    with Dissolve (1)

    "Uma repentina crepitação de estática interrompeu a música. Você encontrou o caminho até
    uma cafeteria, habitada apenas por um rádio velho e um senhor ainda
    mais velho."

    jump chapter1_1

label chapter1_1:

    show oldman
    with Dissolve(1.0)

    "Sua pele era fina como papel. Ele estava segurando um copo de café e, cada vez que
    bebia, suas mãos trêmulas derramavam metade de cada gole."

    "O olhar vidrado do velho passou por você algumas dezenas de vezes antes dele
    perceber que você estava lá."

    "Enquanto olhava para você, ele deu um tapinha no banco ao lado e balançou a mão
    em sua direção. Ele encheu um copo para você."

    "Você se senta, curvado sobre o balcão, e toma um gole.{w} Uma brisa de vida
    derrama sobre sua face. Você nem consegue registrar como é o gosto,
    apenas sabe aqui e agora que está vivo e bem acordado."

    "Você olha para o lado, para o velho. Seu rosto encontra-se contorcido em
    alguma forma de angústia, os lábios tremendo enquanto seus olhos miram de um lado para o outro."

    "Ele põe uma mão sobre cada um dos bolsos, o rosto ainda travado de medo, até
    que sua mão direita cai sobre o bolso da camisa. Ele dá um suspiro de alívio
    e olha para você."

    show oldman:
        ease 2.0 zoom 1.05 yalign 1.05


    "Ele começa a falar, mas não em um idioma que você entende. Ele não está nem
    olhando para você -- seu olhar vagueia nos arredores, aparentemente sem destino. Mas,
    eventualmente, ele alcança uma linha que você consegue seguir."

    old "Você parece do tipo viajante. Você me lembra..."

    "Ele hesita, olha em volta, medita sobre as palavras."

    old "Sim, você me lembra de mim mesmo em minha juventude."

    "Ele olha para frente e toma um gole da bebida. Você capta um vislumbre em
    seus olhos, uma súbita vigília."

    old "Eu era um imbecil. Nunca me estabeleci e desperdicei a minha única chance de
    ter uma vida de verdade. Senti que a estrada sempre me aceitaria."

    old "Acabei jogando fora o único lugar que eu poderia chamar de casa. Esteve
    apodrecendo por quem sabe quanto tempo e agora eu estou velho."

    old "Sempre me perguntei se alguém o assumiria algum dia e o trataria bem."

    old "Ora, você realmente me lembra de mim mesmo, mas eu não era um bom homem. Com sorte
    você não possui a propensão maldosa que eu costumava ter."

    #A flavor choice. Does not change anything.
    menu:
        you "Bem..."

        "Eu tento meu melhor.":

            you "Estou longe de ser perfeito, mas tento o meu melhor."

        "Estou descobrindo as coisas.":

            you "Eu não diria que sou uma ótima pessoa nem nada, mas suponho que eu esteja
            encontrando meu caminho."

label chapter1_2:

    show oldman:
        ease 1.0 zoom 1.03 xalign 0.53

    old "É mesmo? Suponho que isto seja o melhor que se pode alcançar."

    show oldman:
        ease 1.0 zoom 1.05 xalign 0.5

    old "Pelo menos hoje em dia você pode tentar. Na minha época, meu pai me
    tratava como lixo e ninguém piscava um olho. Eu vi isso acontecer muito, também --
    eu não fui o único."

    old "Isso fez de mim e meus irmãos umas pestes, ter um pai assim. Mas
    não pense que eu estou culpando ele. Você só pode apontar o dedo para o seu
    pai por um certo tempo, hein?"

    old "Eventualmente, pelo menos, eu achei um jeito de ganhar a vida. E quanto a você,
    jovem, encontrou uma vocação?"

    pause .5

    #This sets the PC's starting bonus.
    call screen BackgroundPicker()
    $player_background = _return
    $save_name=output_save_name("Prólogo")
    play sound "sfx/asterionchord.mp3"

    if player_background == 'humanities':
        old "Bom, muito bom. Um homem das palavras! Eu só tive o privilégio de
        aprender a como escrever mais tarde na minha vida."
    elif  player_background == 'tech':
        old "Tecnologia? Ah, eu nunca fui bom em entender todas as coisas
        novas saindo o tempo todo. Sempre foi difícil para mim..."
    elif  player_background == 'math':
        old "Ah, eu nunca fui bom com números, mas certamente posso respeitar
        um homem familiarizado com eles!"
    elif  player_background == 'leader':
        old "Ótimo, ótimo! Líderes sempre são necessários, e sempre serão."
    elif  player_background == 'arts':
        old "Um homem de cultura, sim? Isto é bem escasso hoje em dia."
    elif  player_background == 'speedrunner':
        show oldman:
            ease 1.0 zoom 1.09
        "O velho olha para você como se um terrível insulto tivesse sido cuspido de sua boca
        na direção dele."
        "Ele fica sem palavras, seus lábios tremem em choque. Ainda assim, ele mantém
        uma fachada de educação, mesmo que você tenha acabado de revelar sua natureza
        desumana."
        "Este homem é um cavalheiro -- ele mostrará respeito até mesmo para
        uma monstruosidade como você."
        show oldman:
            ease 1.0 zoom 1.05

label chapter1_3:
    "O velho divaga no mesmo idioma de antes."

    "Às vezes, ele para e olha para você, como se estivesse esperando por uma resposta. Um aceno
    com a cabeça ou um grunhido são suficientes para fazê-lo continuar."

    "A voz dele fica mais grave e profunda conforme a noite avança. É reconfortante, de certa
    forma, mesmo que às vezes ele alude novamente a ter um passado difícil e doloroso."

    "Eventualmente ele para e seu olhar parece brilhar com lucidez uma vez mais."

    old "Devo dizer que sinto muito. Receio nunca ter perguntado seu nome."

    $ player_name = renpy.input("Qual é o seu nome?", length=20)
    $ player_name = player_name.strip()

    if player_background == "speedrunner":
        "O velho se esforça para compreender seus resmungos incoerentes. Uma
        carranca se espalha na testa dele, ele parece preocupado de que talvez você possa
        estar tendo um derrame."
        "A esperança se esvai de seu rosto quando ele percebe que você provavelmente é apenas estúpido,
        mas ele se apega à ideia de que possivelmente ainda lhe resta uma salvação."
        "Ele fala lentamente, em palavras simples para não sobrecarregar sua mente débil."
        old "Bem, eu estou muito feliz por ter te conhecido, %(player_name)s."

    if player_name in ["ANON", "Anon", "anon"]:
        old "Ah, agora que penso sobre isso, Anon é um nome bem peculiar."
        old "Eu juro, já ouvi isso antes..."

    elif player_background != "speedrunner":
        old "Estou feliz por ter te conhecido, %(player_name)s."

    show oldman:
        ease 1.0 zoom 1.0 yalign 1.0
    "Os olhos do velho ficam vidrados novamente e sua mão começa a tremer. O café
    derrama para todos os lados, mas já ficou frio a essa altura."

    old "Você parece um homem bem viajado."

    old "Ah, viajar na minha juventude era tão difícil.
    Agora você pode estar do outro lado do mundo em um dia ou dois."

    old "Ah, como o mundo mudou. Uma vez conversei com meu irmão apenas
    sobre este assunto."

    old "Lá em casa tinhamos esse vinhedo onde passamos tantos verões,
    comendo e bebendo. Eu me lembro disso tão bem, é como um filme."

    old "E você sabe o que ele me disse? Que quando nós éramos jovens havia tanta
    magia e maravilha ao nosso redor."

    old "É verdade! Podíamos descer pela estrada, uma coisinha pedregosa da
    época romana, e quando éramos crianças, uma ou duas vezes por semana,
    víamos fantasmas subindo de marcos de pedra e cruzes para se misturar por aí."
    show oldman:
        ease 1.0 yalign 1.05
    old "Mas as coisas mudaram tanto. {w}Eu acho que é a tecnologia, espíritos
    e o arcano não se misturam bem com ela."

    old "Ou talvez... seja algo nos olhos."

    old "Meu irmão, ele costumava dizer que é porque falta devoção na raça humana hoje em dia.
    O desconhecido também não é mais tão assustador, tanto mistério se perdeu.
    E assim a ponte com o fantástico se quebrou."

    "O velho congela por um momento, depois olha de volta para você."
    show oldman:
        ease 1.0 yalign 1.0
    old "Ah, eu estava divagando de novo, não estava? Eu sinto muito."

    you "Não se preocupe com isso, é interessante de ouvir."
    menu:
        "Eu também já vi algo sobrenatural.":

            you "Eu já vi uma ou duas coisas que não consigo imaginar a ciência explicando algum dia."

            you "O mundo é um lugar mais misterioso do que gostamos de pensar. {w}Talvez
            coisas fantásticas não sejam mais tão comuns, mas elas conseguem escapar pelas brechas
            de vez em quando."

            you "Qualquer um que viaja tanto quanto eu eventualmente vai se deparar com algo
            desse tipo."

            you "Ou talvez o sobrenatural ainda esteja lá fora, falando por meio de sussurros
            em vez de se expressar claramente."

            old "Sussurros... Você é um jovem bastante sensível."

            old "Há humildade em sentir o quanto ainda há por aí a ser
            aprendido."

            old "Talvez... Sim, você parece ser bom. Especial."

        "A ciência explica muita coisa.":
            you "Eu já vi uma série de coisas aparentemente inexplicáveis."

            you "Qualquer um que viaja tanto quanto eu vai se deparar com demais delas para se
            contar, de verdade."

            you "Mas eu sou bom em manter a calma e prestar atenção. Muitas vezes,
            esses fenômenos inexplicáveis são bem mundanos na origem."

            you "Eu não estou dizendo que existem pessoas fantasiadas por aí criando boatos{w} -- bem,
            na verdade, existem sim.{w} Ou fazendo deep fakes e postando online."

            you "Mas, com muita frequência, existe uma explicação perfeitamente plausível em algum lugar.
            Você só precisa prestar atenção e desemaranhar a linha."

            old "Desemaranhar a linha, hein? Muito perspicaz de sua parte."

            old "Eu posso acreditar em fantasmas, sim, mas eu enxergo a sabedoria em suas palavras.
            Não se deixe enganar!"

            old "Você realmente parece alguém especial, eu diria."

    old "Hum...{w} talvez você sirva."

    show oldman:
        ease 2.0 zoom 1.1 yalign 1.1

    old "Aqui, gostaria que você ficasse com isso. Tenho certeza que cuidará dele melhor
    do que eu."

    "O velho tira um pedaço de papel antigo do bolso da camisa e o estende
    para você."

    show blackback behind oldman:
        alpha 0.8
    with Dissolve(2)

    play sound "sfx/pageflip.ogg"
    show image "gui/inventory/icons/big/item_Old Deed.png":
        xalign 0.5 yalign 0.7
        ease 1.0 yalign 0.4
    with Dissolve(1)


    old "A escritura do lugar sobre o qual lhe falei. Aquele que eu despedicei."

    old "Eu estou velho, cansado. Gostaria que alguém ficasse com ele, eu estive procurando
    por um... herdeiro, há um tempo, e eu não sinto que tenho mais tempo
    a perder."

    old "Apenas fique com ele. É seu. Um lugar grandioso, um hotel. O tempo cobrou
    seu preço, mas você vai adorar. Só, por favor, cuide dele, seja bom.
    Dê a ele um propósito."

    "Você levanta uma sobrancelha para ele. Esse velho tentou dar para você um hotel assim
    do nada? Ora, quem faria isso?"

    "Seu olhar errante denuncia sua senilidade. Às vezes, ele parece completamente confuso,
    como se não soubesse como veio parar aqui em primeiro lugar."

    "Você não pode aceitar. Não seria certo tirar vantagem de alguém como ele."

    "E isso levando em conta que este pedaço de papel é uma escritura. Pode ser apenas um
    guardanapo usado com um belo lacre."

    "O olhar do velho vagueia. Com a mão ainda estendida, ele aperta os olhos
    em sua direção, depois olha para o papel. Ele se esforça para organizar
    os pensamentos... mas, por um breve momento, sua expressão fica firme e lúcida."

    old "Você deve pensar que eu sou louco. Mas, por favor, entenda, esta é minha última chance
    de fazer isso da forma correta."

    old "Apenas... pegue a escritura."

    menu:
        "O velho homem lhe oferece uma escritura para uma propriedade. Você aceita?"

        "Aceitar.":
            "Você cede ao apelo do velho. Está apenas aceitando um pedaço de
            papel, afinal. Provavelmente não é nada e, se realmente for alguma coisa
            importante, você pode tentar devolver."
            jump chapter1_4

        "Rejeitar.":
            "Você não pode aceitar. Seria errado. Este idoso deve estar
            desorientado. Onde estão seus cuidadores? Certamente alguém tão velho e
            senil não está aqui sozinho."

            "Você rejeita a oferta dele e volta a beber. Provavelmente deveria
            ir embora deste lugar o mais rápido possível, ou pelo menos informar a alguém
            sobre este homem."

            "Ele continua olhando em sua direção. Você tenta não fazer contato visual, mas um
            olhar de soslaio é o suficiente para perceber que ele está com os olhos marejados e seu rosto,
            pálido e fino como papel, contorcido em um choro silencioso."

            "Droga."

            "Você abaixa sua bebida."

            "E daí se essa \"escritura\" for apenas um pedaço de papel aleatório? Talvez
            aceitá-la venha a apaziguar o velho, e você pode devolvê-la quando ele
            tiver um de seus lapsos."

            "Você estende sua mão e pega o documento."

            jump chapter1_4

label chapter1_4:

    hide image "gui/inventory/icons/big/item_Old Deed.png"
    with Dissolve(.5)

    $UI_permissions['items'] = True
    $inventory.add_item("Old Deed")
    play sound "sfx/asterionchord.mp3"
    "Você obteve a {color=[UIColorOrange]}Escritura Antiga{/color}.\n
    Para verificar seus itens, abra o menu e vá para a subtela {color=[UIColorOrange]}itens{/color}."

    hide blackback
    with Dissolve (2)

    "Este velho pedaço de pergaminho parece inimaginavelmente antigo — mais velho que você,
    certamente. Mas a cera em cima parece razoavelmente nova,
    talvez até fresca."

    stop sound

    show oldman:
        ease 1.0 zoom 1.0 yalign 1.0

    "Você parte o lacre e examina o conteúdo do papel."

    "São rabiscos sem sentido, escritos em um alfabeto que você nunca viu antes."

    "Bem, parece que tudo isso foi para nada. Você enfia a \"escritura\" no
    bolso de sua jaqueta."

    "Você olha de volta para o velho. Os cantos de sua boca dobram para cima e ele
    treme levemente. Mas sua alegria dura pouco. Seu olhar vagueia mais uma vez."

    "Quando o foco dele retorna para você, ele franze a testa, observando
    cada uma de suas características, uma de cada vez."

    "O velho resmunga algo para si mesmo, bebe um gole de café e
    sorri."

    if player_background == "speedrunner":
        old "Você é um speedrunner gentil, %(player_name)s. Talvez nem todos do seu tipo sejam ruins."

    else:
        old "Você é um jovem muito gentil, %(player_name)s."

    "Ele lembra de seu nome, pelo menos."

    "Você verifica seu relógio de pulso e os números também viraram rabiscos sem sentido.
    Você toma isso como deixa para acreditar que gastou muito tempo aqui."

    "Você recolhe a bagagem, se despede do velho e
    o agradece pelo café maravilhoso. Ele se curva sutilmente para você."

    show oldman:
        ease 1.0 yalign 1.15
        ease 1.0 yalign 1.0

    old "Não, %(player_name)s. Sou eu quem deveria estar agradecido.
    Foi um prazer negociar com você."

    show oldman:
        ease 1.0 zoom 0.9 alpha 0

    scene bg black
    with Dissolve(2)

    "Você sai da cafeteria e segue seu caminho até o terminal de ônibus. A estação está deserta,
    exceto por um único homem fumando um cigarro do lado de fora da cafeteria."

    "Você o cumprimenta com um aceno de cabeça e ele responde em consideração."

    "Além do velho, ele é a única outra pessoa que você encontra. Mas talvez isto deva
    ser esperado a esta hora da noite."

    "Você segue seu caminho através da estação vazia."

    "Não há ninguém para recebê-lo na plataforma de embarque. O ônibus está tão escuro
    que você mal consegue distinguir a silhueta do motorista."

    "Assim que você senta e se encosta, tenta processar os acontecimentos da noite,
    mas seus pensamentos se dispersam."

    "É tão difícil dizer exatamente há quanto tempo você está viajando. Todos os
    aeroportos, paradas de caminhões, estações de trem e portos se misturam. A
    inquietação da viagem sem fim é a única constante."

    #"There was a \"you\" back home, and you knew who that individual was. But to
    #be a wanderer is to face the \"traveler you\", and that person's face seems
    #alien sometimes."

    "Não demora muito para você desistir."

    "Um calor piedoso escoa de seu peito à medida que você adormece."

    ##This ends PROLOGUE.

    stop music fadeout 2.0


##############################################################################
#               CHAPTER 1: FINDING THE HOTEL AND ASTERION
##############################################################################
#Chapter 1 starts here.
#The MC finds the Hotel and explores it a bit. Checks the reception, bedrooms,
#lounge and restaurant.
#The restaurant is destroyed. Finds Asterion in the cold room.
#Player can be kind or indifferent to Asterion.
#Asterion always rejects the last offer.
label chapter2:
    $chapter = "Capítulo 1"
    $persistent.first_save = False
    define global_affection = 0
    define chapter2_affection = 0

    call screen ChapterTransition("Capítulo 1", "O Hotel")
    pause 0.5
    $save_name=output_save_name("Capítulo 1")

    play music "music/CrossingTheAstralBridge.ogg" fadein 1.0 fadeout 1.0
    "{i}Alguns dias depois."

    play sound "sfx/carstart.ogg"

    scene bg desert
    with Dissolve (4)

    "O horizonte se estende pelo para-brisas manchado. A sintonia do rádio se
    desintegrou em estática. O ar-condicionado não consegue competir com o calor
    do sol no teto do carro."

    "O deserto se estende por todo o horizonte à frente -- um terreno ermo
    de planícies amareladas."

    "À direita, a cerca de cem metros da estrada, o solo poeirento
    dá lugar a um penhasco acentuado. Um vale surge
    por baixo, estendendo-se até o horizonte azul."

    "Você verifica a escritura novamente. Não conseguiu ler da primeira vez — talvez
    estivesse muito cansado. Mas agora os rabiscos outrora sem sentido possuem alguma coerência para o
    seu cérebro."

    "É como ler um idioma que se ramificou de sua língua nativa
    alguns séculos antes. É estranha apenas o suficiente para se tornar irreconhecível
    na primeira vez."

    "No entanto, quando você aperta os olhos com força o suficiente, descobre que os símbolos
    o lembram de seu alfabeto. E então o significado das palavras surgem em sua
    mente."

    "É perturbador, de certa forma. Parece que seu cérebro está virando
    do avesso quanto mais você olha para o papel. Mas, por mais que você tente, é difícil até
    mesmo reconhecer este desconforto — ele desaparece em um piscar de olhos."

    "Você estreita os olhos para a escritura. Há apenas uma hora, mais ou menos, você a verificou
    e percebeu o quão perto estava do endereço."

    "E então você entrou no carro e partiu, com uma curiosidade recém-descoberta
    e uma ansiedade persistente lutando contra ela em seu peito."

    "Talvez o velho realmente tenha lhe dado algo de valor, afinal,
    não um pedaço de papel inútil."

    "Poderia ser mesmo? Você conseguiu uma escritura para um hotel de um homem senil em uma
    cafeteria? Claro, muitos não reclamariam de receber algo de graça tão
    facilmente, mas... Ao mesmo tempo, a maioria contestaria que parece errado."

    "...O hotel deve estar apenas um pouco mais à frente. Você liga o motor e
    segue seu caminho outra vez."

    play sound "sfx/carstop.ogg"

    "Ele surge no horizonte em apenas cinco minutos. Um tempo depois,
    você entra no estacionamento de cascalho."

    scene bg hotelexterior
    with Dissolve (2)

    "É como olhar para trás no tempo no que deve ter sido um dos maiores
    hotéis dos anos 30 e 40. É inteiramente construído em mármore, decorado
    em estilo art déco."

    "É majestoso, até mesmo grandioso, mas completamente arruinado pelo tempo e com um ar sinistro
    por causa dos arredores. Quem pensou que construir um lugar tão incrível em um deserto
    seria uma boa ideia?"

    "Você olha para o horizonte infinito atrás de você. Não há nada além
    do Hotel. Sem plantas de qualquer tipo, sem cactos, arbustos ou até mesmo árvores mortas."

    "Apenas um hotel, no meio de um deserto, construído no topo da parede do penhasco."

    "Sem animais, também. O céu é azul, sem uma nuvem ou ave de rapina à
    vista. O chão abaixo de você não tem insetos, nem mesmo um escorpião ou aranha."

    "Também não havia outros carros na estrada. Você olha de volta para o painel de seu
    carro. O hodômetro indica que você dirigiu apenas cerca de 6,5 km."

    "O capô de seu carro está frio ao toque, como se estivesse desligado por horas."

    "Você olha de volta para o Hotel enquanto pensa em todos esses detalhes. Algo
    chama sua atenção, entretanto; uma varanda com vista para o vale abaixo do Hotel."

    scene bg deathvalley
    with Dissolve(1.0)

    "O vale se estende até o horizonte sem nuvens, emoldurado à direita e
    à esquerda por mais penhascos. Olhando para baixo, no fundo, você pode apenas
    distinguir o contorno de um leito de rio seco estendendo-se."

    "Você percebe que há uma abertura de caverna na parede do penhasco, logo abaixo do
    Hotel. Sua saída é forrada com estátuas, cujos detalhes você não consegue distinguir
    a esta distância."

    "Bem do lado de fora, há pisos rochosos se espalhando em caminhos.
    Você apostaria que foi feito para uma espécie de labirinto quando o rio ainda
    corria."

    "O labirinto termina com um único caminho que leva a uma alta colina, a qual
    teria facilmente se transformado em uma ilha no meio
    do vale inundado."

    "O terreno dessa região é muito parecido com o do Hotel — pode ter sido
    lindo antigamente, mas agora está carcomido pelo tempo."

    "Sua reflexão é interrompida quando um assunto mais urgente espreita sobre você: o
    calor. Independentemente da estranheza ao seu redor, não há como escapar do
    sol escaldante."

    "Você se dirige até a entrada. As portas estão destrancadas."

    show bg abandoned_lobby
    show blackback:
        alpha 0.5
    with Dissolve (2)

    "É difícil dizer por quanto tempo este lugar esteve abandonado. O edifício
    em si certamente é antigo, o exterior está severamente deteriorado."

    "Não seria surpreendente se o interior estivesse repleto de animais selvagens,
    paredes deterioradas e pedaços de teto caídos."

    "Em vez disso, está apenas... empoeirado. Também úmido e estagnado — as paredes estão
    com infiltração de água e há muito mofo. No entanto, não está tão ruim quanto se poderia pensar."

    "Você chama por alguém, na esperança de que qualquer pessoa possa estar aqui. Talvez alguns
    invasores? Porém, assim como lá fora, não há qualquer sinal de vida no hotel."

    "Você caminha até a recepção. O balcão se encontra tão empoeirado quanto você esperaria e
    há canetas e pedaços de papel amarelado espalhados ao redor. Parece que, sejá lá quem esteve aqui,
    deixou este lugar com pressa sabe-se lá há quantos anos."

    "Há uma porta atrás da recepção que leva você a um escritório pequeno, mas
    digno, que parece ter sido abandonado sob um estado semelhante de pressa.
    Há até porta-retratos na mesa mostrando fotos em preto e banco de uma
    família sorridente."

    "No canto da sala há um cofre enferrujado."


$myChoices = [ ("Investigar mesa", "id1"), ("Verificar o cofre", "id2")]
label reception_investigation:
    $narrator("Qual você deveria investigar?", interact=False)
    $result = renpy.display_menu(myChoices)

    if result == "id1":
        if ("Verificar o cofre", "id2") not in myChoices:
            show image "gui/inventory/icons/big/item_Passports.png":
                xalign 0.5 yalign 0.4
                linear 1.0 xalign 0.7
            pause 1
            show image "gui/inventory/icons/big/item_Ledger.png":
                xalign 0.5 yalign 0.4
                linear 1.0 xalign 0.3
            with Dissolve (1)

        else:
            show image "gui/inventory/icons/big/item_Ledger.png":
                xalign 0.5 yalign 0.4
            with Dissolve (1)

        "Sobre a mesa há um livro de registros. Assim como tudo neste hotel, suas páginas
        estão amareladas e enrugadas, mas ainda encontram-se legíveis."

        "Ele contém uma lista de hóspedes, seus respectivos quartos, datas de entrada e
        saída, assinaturas e assim por diante."

        "O último hóspede chegou em 1944. Para ser mais preciso, alguém
        tentou fazer o check-in naquela data, mas foi interrompido
        no processo.{w} Todas as páginas seguintes do registro estão em branco."

        "Você também encontra um segundo livro, encadernado em couro — este possui \"FUNCIONÁRIOS\"
        escrito em cima com tinta dourada descascando."

        "Ele lista todos os funcionários do hotel durante 1944, seus países de
        origem, função...{w} e alguns possuem uma estrela rabiscada ao lado do nome."

        "Este lugar empregava um bom número de pessoas...{w} mais de
        cinquenta, na verdade."

        "Parece não haver mais nada que você possa deduzir a partir
        deste livro."

        $ myChoices.remove(("Investigar mesa", "id1"))
    if result == "id2":
        "É um daqueles cofres antigos que você via em filmes dos anos 90,
        com o botão giratório e tudo."

        "Você se prepara para tentar descobrir a senha...{w} Porém,
        já se encontra destrancado, embora enferrujado."

        if ("Investigar mesa", "id1") not in myChoices:
            show image "gui/inventory/icons/big/item_Ledger.png":
                xalign 0.5 yalign 0.4
                linear 1.0 xalign 0.3
            pause 1
            show image "gui/inventory/icons/big/item_Passports.png":
                xalign 0.5 yalign 0.4
                linear 1.0 xalign 0.7
            with Dissolve (1)
        else:
            show image "gui/inventory/icons/big/item_Passports.png":
                xalign 0.5 yalign 0.4
            with Dissolve (1)


        pause 1.0

        "Há apenas um estoque de livretos dentro dele — quatro
        passaportes, todos de países diferentes."

        "Sem surpresa, todos já estão expirados. Não parece haver
        nada de especial sobre eles,{w} mas é estranho o fato de alguém guardar
        passaportes em um escritório como este."

        $ myChoices.remove(("Verificar o cofre", "id2"))

    $ long = len(myChoices)
    if long > 0:
        jump reception_investigation

    "Você reserva um momento para analisar os livros e passaportes juntos."

    "Uma passada de olho revela um padrão: os passaportes são dos quatro
    funcionários com estrelas ao lado de seus nomes. Você os leva consigo e
    deixa o registro sobre a mesa."

    $inventory.add_item("Passports")
    play sound "sfx/asterionchord.mp3"
    "Você obteve os {color=[UIColorOrange]}Passaportes{/color}."

    hide image "gui/inventory/icons/big/item_Passports.png"
    hide image "gui/inventory/icons/big/item_Ledger.png"
    with Dissolve (1)

    "Você retorna para a recepção e continua olhando em volta. Em frente há
    uma escada alta em espiral que vai para cima e para baixo. Existem vários caminhos que
    se ramificam a partir do saguão."

    "Você segue um dos corredores que levam aos quartos e encontra
    todas as portas destrancadas."

    scene bg oldbedroom
    with Dissolve(2)

    "Assim como no saguão, as paredes deterioradas dos quartos foram consumidas pelo tempo."

    "Caminhar por eles perturbou a fina névoa de esporos estagnados e poeira, os quais
    foram transformados em uma cortina de diamantes pelo sol brilhando através das janelas."

    "Cada quarto estava equipado com pelo menos uma cama king size. As molas
    estavam quebradas na maioria delas e o tecido, amarelado. Mas nem mesmo tal
    desolação poderia esconder a passada glória deste lugar."

    "Você retornou para o corredor, o qual parecia estender-se para sempre em diante."

    "De fora, o hotel parecia grande, mas nem de perto extenso o suficiente para possuir um
    andar térreo com mais de cem quartos."

    "De nada adiantaram as voltas e mais voltas que você deu, o corredor nunca curvou-se
    em si mesmo. Voltar todo o caminho até o saguão era a única opção."

    "A escada em espiral parecia muito mais convidativa que vagar pelos corredores
    aparentemente intermináveis."

    scene bg staircase
    with Dissolve(2)

    "Acima da escada, no final da subida, havia uma claraboia cobrindo
    seus ombros com o calor do sol. Costumava ser um farol, guiando os viajantes
    para este hotel outrora majestoso."

    "O caminho até embaixo era tão sinistro quanto graciosa era a claraboia. Os corrimãos de mármore
    estavam alinhados com lâmpadas queimadas. Seria impossível enxergar muita coisa na escuridão
    lá embaixo."

    "O segundo andar era novamente composto principalmente por quartos. Mas aqui os
    corredores externos eram forrados com amplas janelas que mostravam um pátio
    atrás do Hotel, próximo à borda do penhasco."

    scene asphodel2
    with Dissolve(2)

    "Era um espetáculo para ser visto. Enquanto o hotel foi consumido pelo tempo, o
    jardim do lado de fora floresceu. Era um campo transbordando com flores brancas, balançando
    com o vento deste deserto miserável."

    "No centro havia uma estátua de um homem e um cachorro. As flores
    subiam até os joelhos do homem e apenas o topo da cabeça do cachorro podia ser visto."

    "A mão do homem estava estendida, como se acenando para as flores crescerem
    mais alto e para as pessoas se aproximarem."

    "O jardim parecia uma aventura mais convidativa. Você desceu de volta pela
    escadaria de mármore, transbordando de clareza, e era como se um manto --ou um abraço--
    estivesse enrolado em suas costas."

    "Você seguiu o corredor que conduzia em direção à parte de trás do hotel e uma única
    volta à direita o levou para um grande salão."

    show bg oldlobby
    show blackback:
        alpha 0.5
    with Dissolve(2)

    "Bem ao lado de sua entrada havia um bar e, à esquerda: mesas, sofás e
    cadeiras reclináveis."

    "Mais à esquerda, havia uma janela alta de vitrais, como as de uma
    catedral. E, através de uma porta de vidro ao lado desta janela, estava o jardim."

    scene asphodel2
    with Dissolve(2)

    "O vento soprando através do jardim provocou um longo e contínuo assobio.
    Deste ângulo baixo, a estátua destacava-se como um rei, alto, porém humilde,
    acenando para seus queridos súditos."

    "As flores balançavam para frente e para trás com o vento cantante e a cabeça do cachorro
    mal era visível acima delas. Suas orelhas estavam em alerta e sua língua
    pendurada para fora de sua boca sorridente."

    "Atrás da estátua, além do pátio, havia uma grade de segurança com vista para a queda
    até o vale abaixo."

    "Ao caminhar ao redor da estátua, você notou pelo canto do olho que o
    cachorro pareceu ter virado a cabeça para segui-lo."

    scene asphodel1
    with Dissolve(2)

    "Você olhou de volta. A estátua do cachorro não se moveu, mas estava de fato olhando diretamente
    para você. Você separou as flores e caminhou até ele, foi quando percebeu que o
    cachorro tinha três cabeças -- uma olhando para frente e outra em cada lado."

    "Todas as três emanavam calor. Você acariciou uma de suas cabeças e percebeu
    quão gasto estava o mármore -- as pessoas vêm o acariciando há muito tempo."

    "Então você seguiu seu caminho até a beira do penhasco. Mais uma vez foi saudado
    pelo vale. Bem abaixo, ao longe, você podia ver a saída da caverna revestida de estátuas."

    "Você podia apenas se perguntar o quão vibrante esta terra deve ter sido há muito tempo, quando o
    rio do vale ainda corria."

    scene bg oldlobby
    show blackback:
        alpha 0.5
    with Dissolve(1)
    "Você volta para dentro do vasto salão. Está escuro, porém familiar, agora
    que sua vista acostumou-se com a claridade do lado de fora."

    "Você ainda pode perceber o assobio vindo do lado de fora, você se senta
    no bar. Esta escuridão recém-chegada é macia, suave como veludo. É como
    estar em uma sala à luz de velas."

    "Atrás do balcão, as garrafas de destilados ainda estão pela metade.
    Elas brilham em tons de marrom, vermelho e azul requintados."
    show blackback:
        ease 1.0 alpha 1.0
    pause 1
    "Você fecha seus olhos e imagina como era este lugar décadas atrás."

    "O assobio se altera novamente. Transforma-se no murmúrio da vida humana,
    passos e respiração. Cadeiras sendo arrastadas, talheres e pratos retinindo.
    Risadas, sussurros, pessoas se cumprimentando de diferentes mesas."

    "Pessoas tão bem vestidas. Um barman à sua frente, servindo as melhores
    bebidas que você pode imaginar. Ele sabe seu nome e como você gosta. Esteja
    você cansado ou transbordando de vida, ele lhe oferece um ouvido atencioso."
    show blackback:
        ease 1.0 alpha 0.5
    pause 1
    "Você abre seus olhos. Está de volta ao hotel abandonado,
    majestoso e destruído."

    "Pode-se entender por que o velho quis passá-lo adiante para alguém
    que cuidasse dele. Você dá um tapinha no bolso da jaqueta, certificando-se de
    que o pergaminho amassado ainda está lá."

    "Até mesmo o papel manchado e amarelado emana calor agora."

    "Você se levanta e sai andando. Ao fazer isto, nota uma grande mancha roxa
    no chão atrás do balcão e os cacos de vidro do que costumava ser uma
    garrafa de vinho."

    "Você prossegue adiante no hotel. Ainda há muito para se ver."

    "No final do corredor, um conjunto de portas de vidro deslizantes revelam-se para você.
    Mas, de longe, a discrepância é clara. O papel de parede está rasgado e uma das portas
    está rachada."

    play music "music/RedDistortion.ogg" fadeout 4.0 fadein 4.0

    "Você pisa em algo duro. Uma bala de revólver."

    "Você empurra a porta para o lado e é saudado por uma visão ainda mais
    caótica. É o restaurante do hotel. As mesas estão viradas e tanto
    cadeiras como pratos encontram-se quebrados no chão."

    "Há uma mancha escura no meio do cômodo que leva
    até a cozinha."

    scene bg cold_room_door
    show blackback:
        alpha 0.4
    with Dissolve(1.0)

    "Ela o guia além da despensa até a massiva porta de ferro de uma câmara fria,
    que está trancada por fora e fechada com tábuas."

    "Há objetos espalhados por toda a cozinha. Até mesmo uma panela no
    fogão com o que deve ser comida fossilizada, e a pia está cheia de pratos
    sujos."

    "Em um balcão próximo, há um revólver coberto em poeira espessa e você se lembra
    da bala no corredor e da mancha no chão do restaurante."

    "O velho não estava brincando quando disse que não era uma boa pessoa."

    "Você verifica seu celular. Talvez precise chamar a polícia, ou um necrotério.
    Mas não há sinal aqui."

    play sound "sfx/chair.ogg"

    "Você inspira, preparando-se para uma visão terrível. A porta enferrujada
    luta contra sua vontade, mas não consegue impedir."

    "A escuridão despeja para fora."

    play sound "sfx/creak.ogg"


    scene bg coldroom
    with Dissolve(1)

    "O fedor atinge primeiro. É o cheiro estagnado de sangue e podridão. Ele
    se agarra ao seu nariz e boca como um óleo amargo."

    "Antes que seus olhos possam se ajustar à escuridão, uma segunda onda de fedor o atinge.
    E é como uma fazenda, também -- o cheiro de pelo com poeira, talvez até feno, mas
    confinado em uma sala quente e úmida por décadas."

    "E, por último, mas não menos importante, fezes e urina envelhecidas. Este lugar tem tudo, o
    fedor de milhares de mortes diferentes."

    "A luz que derrama para dentro da câmara fria brilha no piso em frente à passagem da
    porta. Latas de sopa e potes de geleia vazios encontram-se espalhados ao redor sobre
    o rastro de sangue velho."

    "Quem quer que tenha sido trancado aqui dentro não morreu rapidamente."

    "A câmara fria estende-se para dentro da escuridão absoluta.
    Você prossegue, raspando os sapatos no chão para não tropeçar
    no entulho."

    "Todo o piso está coberto com latas e potes de vidro descartados. Quaisquer
    restos que tenham sobrado neles há muito apodreceram, secados e desintegrados em pó."

    "Tanto seus passos quanto sua respiração ecoam. A umidade insuportável cobre
    suas costas e sua respiração fica agitada. O fedor fica mais forte."

    "Sua visão finalmente se adapta ao escuro. No que deve ser a parede mais distante da câmara fria,
    você percebe o mais leve brilho."

    scene image "images/cg/cg1.png"
    with Dissolve(1)

    "Seja lá o que for, está largado ao chão, imóvel. Como se tivesse morrido
    onde ficou depois de sabe-se lá quanto tempo trancado aqui."

    "Entretanto, um tímido brilho azul pisca onde seu olho esquerdo deveria estar."

    menu:
        "O que você faz?"

        "Chamar a polícia.":

            "Você puxa seu celular, mas não há sinal. Talvez a câmara
            fria esteja causando interferência."

            "Antes de sair, você tira um momento para dar uma boa olhada na
            coisa, já que precisará descrevê-lo para quem atender a ligação."

            jump chapter2_1

        "Examinar corpo.":
            jump chapter2_1

label chapter2_1:
    "Sua visão está acostumada à escuridão agora. O distante pilar de luz
    vazando da porta é o suficiente para evitar tropeçar
    no vidro descartado."

    "Você se agacha em frente à coisa."

    "Ela possui uma cabeça de touro. Você olha em volta do pescoço, procurando por um
    zíper ou a borda de uma máscara, mas não há nada."

    "Está coberta de pelos, exceto pelos trechos de pele exposta
    e enferma. Possui cascos em vez de pés."

    "Seus chifres poderiam facilmente escornar uma pessoa."

    "Metade de seu crânio está exposto. O osso ainda contém um punhado
    de pó de sangue próximo à carne restante."

    "A cavidade ocular esquerda está vazia, mas algo brilha dentro dela.
    Uma brasa azul."

    "O pelo está grosso e despenteado, mas não é capaz de esconder o quão terrivelmente
    magra estava esta criatura. Ela morreu de inanição, não do que quer que tenha
    destruído seu rosto."

    "É o bastante. Você se levanta e volta para sair. Ao fazer isto, o
    farfalhar de suas roupas e os passos ecoantes quebram a cortina de silêncio."

    "É quando você ouve a criatura. Respirando tão fraco quanto o bater de asas de uma mariposa."

    "Você olha de volta para o corpo. A chama azul pisca para você. O peito
    expande e contrai."

    "Você dá um passo à frente e a faísca o acompanha como se fosse um olho."
    menu:
        "O que você faz?"

        "Falar com a criatura.":
            $ chapter2_affection += 1
            "Você fixa o olhar na coisa, tentando ler seu rosto desfigurado."

            you "Você consegue me entender?"

            "Ela mal reage à sua voz no começo. Suas palavras escapam para ela
            e rastejam para dentro da cabeça, cavando caminho para sua mente e, em seguida,
            torcendo-se até que ela acorde."

            "Como uma borboleta saindo de sua longa soneca, o olho restante da coisa
            volta à vida."

            "Ela acena com a cabeça para você."

            jump chapter2_2

        "Continuar em silêncio.":
            "Você fica onde está. A chama da coisa permanece fixa em você,
            sacudindo quando uma corrente de ar fresco sopra dentro da câmara fria."

            "A saída está a apenas cinco segundos de distância se você voltar e correr.
            Caso haja necessidade, a arma ainda está do lado de fora."

            "A coisa permanece no chão, mal se movendo. O piscar de seu
            único olho é prolongado e deliberado. Sua cabeça pende para baixo, como
            se ela mal pudesse se manter acordada."

            "Seus lábios, ou o que resta deles, se separam. Sua respiração
            fica mais fácil de se ouvir."

            thing "Eu imploro seu perdão. Estou em um estado tão lamentável."

            "Que eufemismo."

            jump chapter2_2

        "Sair.":
            "Você recua com um pé de cada vez. A criatura pode parecer fraca e quase morta,
            mas não é humana. Quem pode dizer o que ela é capaz de fazer?"

            "Você está no meio do caminho até a porta quando a criatura fala."

            thing "Eu não posso machucá-lo."

            "Sua voz falha. Pela distância você não consegue mais
            enxergar seus olhos, mas sua forma, esta
            coisa abandonada, implora para você voltar."

            jump chapter2_2

label chapter2_2:
    play music "music/CrossingTheAstralBridge.ogg" fadeout 6.0 fadein 5.0

    scene bg coldroom
    with Dissolve(1)

    $Asterion.change("stage", "skull")
    $Asterion.change("light","dark")
    if persistent.sfwMode:
        $Asterion.change("underwear", "loincloth")

    show Asterion:
        yalign 1.7 xalign 0.5
        ease 4.0 yalign 1.4
    with Dissolve(4)

    you "O que é você?"

    thing "Eu sou o zelador do Hotel e prisioneiro do Labirinto."

    "Sua voz é rouca, quase uma série de grunhidos ecoando através da sala
    em contraste com seu corpo desgrenhado. Ele franze a testa na área de seu olho remanescente."

    thing "E você é o Mestre agora, o que me torna seu servo, limitado
    à sua vontade. Eu não posso desobedecer suas ordens."

    "A coisa embala a cabeça entre os braços. Sua voz sai abafada."

    thing "Se deseja saber o que sou, eu sou um monstro híbrido.
    Sobre meu estado lamentável, o Mestre anterior fez isto comigo."

    thing "E, como seu servo, responderei às perguntas do Mestre."

    "Ele permanece com o rosto escondido por mais algum tempo. Quando finalmente olha para cima,
    ele encara a saída e não você. Ele aperta o olho e levanta um antebraço
    terrivelmente fino sobre si."

    show Asterion:
        ease 2.0 xalign 0.52

    "Ele se move um centímetro para o lado, de forma que sua sombra o cubra."

    $ myChoices = [ ("Por que você estava trancado aqui?", "opA"), ("Você é o... 'zelador' do Hotel?", "opB"), ("Por que o Mestre anterior fez isso com você?", "opC"), ("Quem vivia aqui?", "opD") ]
label ch2_2_before_choice:
    $ narrator("Faça sua pergunta.", interact=False)
    $ result = renpy.display_menu(myChoices)

    if result == "opA":
        you "Por que você estava trancado aqui?"
        thing "Isso foi o que o último Mestre achou adequado. Ele atirou em mim e ordenou
        que eu ficasse aqui, nesta sala."
        thing "Mas, como você pode observar, eu sou imortal. Apenas doeu, eu não posso ser morto."
        thing "Posso apenas presumir que ele expulsou todos os hóspedes pouco tempo depois.
        E agora o Hotel deve estar em um estado tão lamentável quanto eu."
        thing "Ele também trancou a porta, mas seu comando foi o suficiente.
        Eu não posso desobedecer, então não tive saída. Eu sou um prisioneiro, afinal."
        $ myChoices.remove(("Por que você estava trancado aqui?", "opA"))

    elif result == "opB":
        you "Você é um prisioneiro, mas também é o zelador do Hotel?"

        "Seus olhos se estreitam e suas orelhas caem."

        thing "Sim. Fui sentenciado pelos deuses a passar a eternidade aqui. Não
        lutei contra meu assassino e, por tal mansidão, fui condenado."

        thing "Os deuses fizeram esta terra, a qual chamaram de o Labirinto, para me abrigar em
        minha danação."

        thing "É esperado que o Mestre seja meu torturador e, para este fim, recebe
        o controle da terra. Mas houve um Mestre que acreditava que o Labirinto
        poderia ser transformado em um lugar relaxante, e que eu poderia cuidar dele."

        thing "Então, pela vontade dele, tornei-me o zelador."

        thing "E pela antiga ordem dos deuses, o Labirinto atrai aqueles que estão
        perdidos e não têm para onde ir. Eles se tornaram nossos valiosos hóspedes."

        "Ele fecha o olho por um momento, perdido em um devaneio."

        you "Mas e a sua vida antes de vir para cá? Como ela era?"

        thing "Mestre Jean-Marie me contou que isso se tornou uma lenda. Eu nasci
        de uma rainha que teve um caso ilícito com o touro branco do deus dos mares,
        Poseidon."

        thing "Fui criado na corte do Rei Minos, em Creta. Ele me tratava como
        um filho, mesmo que eu fosse... muito pior que um bastardo. Mas, eventualmente, minha
        irmã exigiu que eu fosse mandado embora."

        thing "Pai Minos aquiesceu, Mãe disse não. Então, eles me mandaram
        para o meu primeiro labirinto, sozinho, com apenas um machado para fazer companhia.
        Fiquei lá por anos..."

        thing "Até que um dia, o guerreiro Teseu veio por minha cabeça em rebelião
        contra o reinado de meu pai. Ele estava preparado para lutar comigo, mas eu não tinha nada pelo que viver.
        Então, em vez disso, ele me deu misericórdia."

        thing "Como você pode observar, o proprietário anterior tentou exatamente o mesmo. Mas
        eu não posso morrer, não desta vez. Eu apenas perdi um pouco de carne.{w}... e os hóspedes do Hotel."

        "O olho dele pisca loucamente."
        $ myChoices.remove(("Você é o... 'zelador' do Hotel?", "opB"))

    elif result == "opC":
        you "Por que o Mestre anterior fez isso com você?"

        "A criatura recua, encolhendo-se ainda mais em uma posição fetal."

        thing "Ser um monstro é razão suficiente para a danação, Mestre. Ele escolheu
        devolver o Labirinto ao seu propósito original, eu presumo."

        "Sua mandíbula ossuda abre e fecha, mastigando o nada."

        thing "Alguém precisa de um motivo para seguir a vontade dos deuses?"

        thing "De qualquer forma, isso dificilmente importa. Eu não posso morrer."

        "Suas feridas abertas se destacam enquanto ele fala, assim como a chama sacudindo
        loucamente. É brilhante o suficiente para ser visível de longe, mesmo na escuridão."

        you "Como eu posso ajudar com os seus ferimentos?"

        "Ele expira bruscamente com suas palavras. Seu rosto afunda novamente entre as pernas."

        thing "O Mestre não precisa se preocupar comigo. Não posso morrer e já parou de doer
        há muito tempo. Um crânio não sente dor."

        thing "O que dói de verdade é pensar em nossos hóspedes... Por todo esse tempo
        me perguntei o que aconteceu com eles. Espero que tenham encontrado outro lugar."

        $ myChoices.remove(("Por que o Mestre anterior fez isso com você?", "opC"))

    elif result == "opD":
        you "Que tipo de pessoas costumavam considerar esse lugar como a casa delas?"

        thing "Qualquer um em necessidade, se o destino considerasse adequado que
        eles parassem aqui. Órfãos e crianças fugitivas, andarilhos sem teto perseguidos por
        seus passados, homens traumatizados pela guerra em busca de refúgio."

        thing "Aqueles que não têm mais ninguém e nenhum lugar para chamar de lar."

        thing "Antes de o último Mestre assumir, o Hotel pertencia a um homem
        que lutou na...{w} Primeira Guerra Mundial. Mestre Jean-Marie. Ele achou adequado
        trazer para dentro aqueles deslocados pelo derramamento de sangue."

        "Sua voz falha por um momento, e você ouve um pequeno estalo."

        thing "... O Hotel era glorioso na época."

        thing "O Mestre Jean-Marie sobreviveu à Primeira Guerra, mas não à Segunda... Portanto,
        seu irmão herdou o Hotel, e achou adequado decretar sua vontade contra mim."
        "Você puxa a escritura do hotel de dentro do bolso da jaqueta."

        you "Então é isso que faz de mim o novo Mestre?"

        thing "Correto. A posse do Labirinto foi transferida para você.
        Eu sempre sei quem é o Mestre atual e o nome dele."
        $ myChoices.remove(("Quem vivia aqui?", "opD"))

    $ long = len(myChoices)
    if long > 0:
        jump ch2_2_before_choice

    "Você fez todas as suas perguntas."
    "Outra vem à mente, agora."

    menu:
        "Qual é o seu nome?":
            you "Qual é o seu nome?"

    "Ele hesita antes de responder. Seu olho ardente estremece com leveza."

    show Asterion:
        ease 2.0 xalign 0.5

    thing "O Mestre tem o direito de escolher meu nome. Mas, se é de sua vontade saber,
    meu nome de nascença é Astério.{w} Astério, o Minotauro, filho
    adotivo do Rei Minos, de Creta."

    "Astério olha para você enquanto fala. Talvez, em um passado distante,
    aquelas palavras, \"filho adotivo do Rei Minos, de Creta\", transbordassem de orgulho."

    "Mas hoje gotejam a nostalgia e a esperança de um homem que, pela
    primeira vez em décadas, pronuncia o próprio nome."

    show Asterion:
        ease 1.0 yalign 1.5

    "Por uma fração de segundo, seu olho restante reflete um raio de luz
    do lado de fora. Ele percebe então o quão cansado, com sede e com fome está."

    "Mas não importa. Afinal, ele não pode morrer. Como um servo, seu dever
    tem precedência."

    show Asterion:
        ease 1.0 yalign 1.2

    play sound "sfx/crack.ogg"

    "O minotauro reajusta para uma posição ajoelhada. O estalo de suas
    patelas ricocheteia nas paredes da câmara fria."

    "Ele curva a cabeça para você."

    asterion "O vínculo entre carcereiro e prisioneiro nasce a partir da escritura, enquanto
    aquele entre o Mestre e o Servo é escolhido deliberadamente."

    asterion "O Mestre ouvirá meu juramento de servidão?"

    "Você levanta uma sobrancelha com o gesto do minotauro esquelético. Você não consegue
    formular uma resposta. Em seu silêncio, o minotauro olha para você."

    show Asterion:
        ease 1.0 yalign 1.4
    pause 1
    show Asterion:
        ease 0.05 xalign 0.501 yalign 1.4
        pause 0.05
        ease 0.05 xalign 0.499
        pause 0.05
        repeat

    "Ele começa a tremer, mal conseguindo manter as mãos juntas. Seus lábios
    tremem em antecipação."

    asterion "Mestre, o Labirinto foi projetado para me torturar."

    "A voz do minotauro falha. Pela primeira vez você nota uma cauda balançando
    atrás dele."

    asterion "O juramento de servidão é o que mantém as entidades longe. Por favor, Mestre,
    permita-me recitá-lo e submeter-me ao seu serviço."

    "Você só consegue acenar com a cabeça em resposta. Com sua autorização, ele é capaz
    de prosseguir depois de um minuto para se recompor."

    show Asterion:
        ease 2.0 yalign 1.3
    pause 3


    asterion "{i}Pelas provisões sob o Estatuto de José, o Misericordioso,
    o Prisioneiro Astério promete lealdade e servidão ao Mestre do Labirinto."

    asterion "{i}O Prisioneiro é instituído Zelador do Hotel acima do
    vale e lhe é legado o poder de realizar a vontade do Mestre."

    asterion "{i}O Mestre, por sua vez, restringe o Labirinto, proibindo suas entidades
    maliciosas de deixarem dito vale."

    asterion "{i}O domínio foi projetado para torturar o Prisioneiro e, de fato, sua
    missão deve ser cumprida. O Prisioneiro carregará o fardo da servidão,
    mas não sofrerá a ira do Labirinto dentro do território do Hotel."

    asterion "{i}O Prisioneiro, amparado pela vontade de seu Mestre, fica seguro desde
    que cumpra seu dever, sob os termos do Estatuto."

    "Astério não ousa olhar para você. Assim que termina o juramento, seu silêncio
    é interrompido apenas pelas gotas de suor escorrendo de seu rosto trêmulo."

    you "É bastante informação para assimilar de uma vez só. Se você quiser qualquer
    coisa de mim, vai ter que explicar as coisas um pouco melhor."

    you "Para começar, deuses? Você está me dizendo que deuses são reais?"

    asterion "...Sim. Perdoe-me,{w=0.2} falhei em considerar a época."

    asterion "Os deuses...{w=0.3} eles são, ou talvez {i}eram{/i} bastante reais. Não posso
    saber com certeza os detalhes, mas eles parecem ter desaparecido."

    asterion "Na minha época, eles estavam muito presentes na vida dos homens{w=0.1} e,
    na maioria das vezes, os mortais encontravam-se em pior situação por causa disto."

    asterion "Eu não sei por quanto tempo estive aqui, nem o que mudou desde
    então. Mas,{w=0.1} das histórias que ouvi,{w=0.1} pareceu que a maioria dos traços
    do sobrenatural desapareceram do mundo dos vivos."

    asterion "Isso responde à pergunta do Mestre?"

    you "Não completamente.{w=0.1} Como eram os deuses?"

    show Asterion:
        ease 0.05 xalign 0.501
        pause 0.05
        ease 0.05 xalign 0.499
        pause 0.05
        repeat

    asterion "Eles...{w=0.4} era raro que os mortais os conhecessem pessoalmente, mas as consequências
    de enfurecê-los ficavam facilmente à mostra.{w=0.2} O panteão era respeitado, mas acima de tudo temido."

    asterion "Eles não eram...{w} piedosos."

    pause 1.5

    asterion "...Você pode observar por conta própria.{w=0.3} Eles me sentenciaram aqui."

    you "Isso é muito para absorver, para ser honesto. Que deuses gregos são reais, ou
    pelo menos foram, é uma baita mudança de paradigma. Todos os outros deuses também são reais?"

    asterion "Todos os outros?...{w=0.5} Eu não sei. Acredito que muitos deles foram, sim,
    mas não posso saber com certeza como sei em relação aos deuses do meu tempo."

    you "Existiam outros minotauros?"

    show Asterion:
        ease 0.05 xalign 0.5
    pause 1.5

    asterion "Não.{w=0.5} Eu era o único."

    asterion "Nunca vi ou ouvi falar de outro minotauro em todos esses séculos."

    asterion "Existem outros seres sobrenaturais. Alguns apareceram
    no Hotel aqui e ali. Uns eram funcionários, até."

    asterion "Mas eles se tornaram muito raros nos últimos séculos."

    asterion "Mas sem minotauros."

    you "Por que eu não vi nenhum em outros lugares, então? Eles vivem na
    floresta, isolados da civilização?"

    asterion "...Antes de eu ter sido trancado aqui, eles usavam disfarces.
    Se passavam por humanos comuns por meio de um amuleto encantado."

    asterion "Mas eu não saberia se isso ainda é o que eles fazem hoje."

    you "E esse juramento que você estava falando, o que significa?"

    show Asterion:
        ease 0.05 xalign 0.501
        pause 0.05
        ease 0.05 xalign 0.499
        pause 0.05
        repeat

    asterion "É o que me protege, meu senhor. Há criaturas no vale,
    elas não podem me fazer mal dentro do Hotel enquanto eu estiver a serviço
    do Mestre."

    asterion "O juramento anterior permaneceu enquanto o Hotel continuou
    sem um Mestre."

    asterion "Com sua chegada, fico vulnerável novamente."

    asterion "Por favor, permita-me estar a seu serviço."

    menu:
        asterion "O Mestre %(player_name)s aceitará Astério como seu servo,
        sob os termos do Estatuto?"

        "Aceitar Astério.":
            you "Tudo bem. Levando em conta que você esteja falando a verdade... sim, eu
            aceito você como meu servo."
            jump chapter2_3

label chapter2_3:
    play sound "sfx/creak.ogg"

    "Suas palavras ricocheteiam nas paredes e escorregam para fora da câmara
    fria."

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

    "A luz gotejando da porta atrás de você oscila. Sua sombra,
    espalhada sobre o minotauro, pisca e tremula ligeiramente."

    "O próprio mundo estremece sob suas palavras e responde resvalando em
    uma nova forma ao seu redor."

    show Asterion:
        ease 1.0 yalign 1.2

    "Astério ainda olha para baixo, seu corpo agora curvado para frente e
    não mais tremendo."

    asterion "Minha gratidão não conhece limites. Não irei decepcionar."

    asterion "Posso estar em um estado lamentável agora, mas me recuperarei rapidamente."

    asterion "Se o Mestre assim permitir, vou me retirar. Preciso apenas passar
    na enfermaria para cuidar de meus ferimentos."

    "Ele levanta a cabeça levemente, olhando para a porta."

    asterion "...Eu ainda estou incapaz de sair da câmara, até que você me ordene
    o contrário."

    menu:
        "Oferecer-se para acompanhá-lo.":
            "Por mais imortal que seja, o corpo do minotauro está atrofiado. Ele não
            irá muito longe por conta própria."
            "Você se ajoelha ao nível dele. Apesar da escuridão, você consegue distinguir
            suas escápulas e pele flácida."
            you "Você consegue andar sozinho?"
            "Astério desvia o olhar para as próprias pernas."
            asterion "O Mestre não deve se preocupar comigo. Posso
            ir à enfermaria sozinho. Já passei por coisa pior."
            "Ele não vai olhar para você. Há apenas um toque de orgulho em sua voz."
            $ chapter2_affection += 1

            menu:
                "Permitir que Astério saia da câmara.":
                    jump chapter2_asterion_leaves_room

                "Ordenar que ele aceite sua ajuda.":
                    $ chapter2_affection += 1
                    jump chapter2_command_asterion


        "Permitir que Astério saia da câmara.":
            jump chapter2_asterion_leaves_room

label chapter2_asterion_leaves_room:
    you "Tudo bem. Você tem minha permissão para sair da sala."

    show Asterion:
        ease 1.0 yalign 1.4

    "Sem dizer uma palavra, o minotauro se curva para você, depois põe as mãos
    no chão para tentar se levantar."

    show Asterion:
        ease 2.0 yalign 1.2
        ease 1.0 yalign 1.0

    "Ele luta, primeiro para estalar os joelhos nesta nova posição, depois
    para encontrar o equilíbrio. Ele consegue após segurar em uma das prateleiras."

    show Asterion:
        ease 1.0 xalign 0.45 alpha 0.8
        ease 1.0 xalign 0.40 alpha 0.4
        ease 1.0 xalign 0.35 alpha 0

    "Um passo de cada vez, ele caminha em direção à porta, fazendo pausas para descansar
    contra uma parede e ajustar sua visão à luz."

    scene bg cold_room_door
    with Dissolve(1)
    $Asterion.change("light","light")

    "Demora um longo tempo, mas ele sai da câmara fria e segue seu caminho até a
    enfermaria. Você o segue de perto, certificando-se de que ele não tropece e se machuque."

    "Suas costas estão cobertas de escaras."

    "Contra todas as probabilidades, Astério realmente consegue prosseguir sozinho."

    jump chapter2_4

label chapter2_command_asterion:
    you "Sinto muito, não posso permitir isso. Você não está em condições de andar para
    qualquer lugar."

    you "Você vai me deixar te levar até lá. Isto é uma ordem."

    show Asterion:
        alpha 1.0
        ease 1.0 yalign 1.4

    "Ele permanece com a cabeça baixa, olhando para os próprios joelhos."

    "Ele suspira profundamente, os ombros caindo ao mesmo tempo. Quando fala,
    ele pronuncia cada sílaba com uma fria nitidez."

    asterion "Eu obedeço."

    "A pele e o pelo do minotauro estão terrivelmente finos. Ele não deve ser pesado, você
    poderia carregá-lo. Mas isto por si só poderia machucá-lo."

    you "Posso encontrar uma cadeira de rodas por aqui em algum lugar?"

    asterion "A enfermaria deve ter uma. Em..."

    asterion "...Um dos quartos mais adiante no corredor."

    show blackback:
        alpha 1.0
    with Dissolve(2)

    "Você diz ao minotauro para esperar enquanto faz a busca. No momento em que
    está saindo do restaurante destruído, sua visão falha. Por uma fração
    de segundo, o mundo fica preto."

    "A enfermaria acontece de ser na porta imediatamente após o
    restaurante. Você encontra uma cadeira de rodas enferrujada e
    ligeiramente mofada jogada em frente à porta. Vai servir."

    show Asterion:
        xalign 0.5 yalign 1.2

    hide blackback
    with Dissolve(2)

    "Astério espera onde você o deixou, embora agora ele tenha voltado a se encolher,
    seu rosto coberto por seus braços. Sua única orelha restante sacode enquanto você
    se aproxima, mas ele não fala nada -- seja em agradecimento ou protesto."

    "Ele é leve como uma criança, certamente não pesa mais que vinte quilos. Ele grunhe
    e estremece sob seu contato. Depois de ajudá-lo a se sentar na cadeira, você nota que
    uma de suas mãos está coberta de sangue vermelho-escuro por ter tocado nas costas dele."

    scene bg cold_room_door
    with Dissolve(1)
    $Asterion.change("light","light")

    "Enquanto segue seu caminho para fora da câmara fria, você vê que as costas dele
    estão cobertas de terríveis escaras. Com um olhar de soslaio, ele pega você encarando."

    "A luz, entretanto, parece machucá-lo. Ele cobre o olho com as duas mãos."

    jump chapter2_4

label chapter2_4:
    scene bg infirmary
    with Dissolve(1)
    $Asterion.change("light","light")

    "A enfermaria é como olhar para uma obra de época sobre a Segunda Guerra
    Mundial, com uma camada adicional de poeira e ferrugem."

    "Bem como a cozinha, foi evacuada às pressas. Há pranchetas espalhadas,
    frascos de medicamentos largados entreabertos, até mesmo uma agulha hipodérmica
    ainda carregada com um líquido amarelo."

    show Asterion:
        xalign 0.6 yalign 1.0 alpha 0
        ease 2.0 xalign 0.4 alpha 1.0
    with Dissolve(1)
    show Asterion:
        alpha 1.0
    "Apertando o olho, Astério caminha até as gavetas. Ele examina cada uma,
    em silêncio, até que uma delas revela cacos de vidro verde e uma mancha roxa
    seca."

    show Asterion:
        ease 1.0 yalign 1.1

    "O minotauro se inclina para frente e suspira. Ele raspa um dedo na gaveta,
    tentando juntar um pouco do pó roxo, mas é inútil."

    "Ele continua olhando em volta e você faz o mesmo. Tudo o que você encontra são
    ataduras empoeiradas, remédios apodrecidos há muito tempo e, no fundo de uma das gavetas,
    uma garrafa de vinho quase vazia."

    "Você a segura contra a janela. Há apenas dois centímetros de vinho sobrando. A rolha
    está seca e esfarelando. Neste calor, já deve ter se transformado em
    vinagre."

    show Asterion:
        ease 2.0 xalign 0.5 yalign 1.0 alpha 1.0

    "Você está prestes a colocá-lo de volta quando nota o olhar de Astério seguindo
    a garrafa."

    "Ele olha brevemente para os seus olhos, o rosto dele contorcido em uma carranca suplicante."

    menu:
        "\"É isso que você está procurando?\"":
            $ chapter2_affection += 1
            "O minotauro acena com a cabeça mansamente."
            jump chapter2_5

        "Permanecer em silêncio.":
            jump chapter2_5

label chapter2_5:
    asterion "O vinho me cura."

    "Ele não se move até você estender o vinho para ele. Apenas então ele se curva."

    show Asterion:
        ease 2.0 xalign 0.6 yalign 1.4

    "O minotauro se senta em uma das camas da enfermaria. A rolha esfarela em pó
    quando ele a puxa, deixando a garrafa ainda entupida."

    menu:
        "Oferecer-se para abrir.":
            $ chapter2_affection += 1
            "Você estende uma mão para ele."

            "Ele intercala entre olhar para a garrafa, segurando-a próxima ao peito,
            e olhar para a sua mão."

            "A contragosto, ele o devolve para você. Sobrou rolha o suficiente para
            conseguir puxar para fora."

            "Você retorna a garrafa para o minotauro."
            jump chapter2_6

        "Deixá-lo descobrir como abrir.":
            "O minotauro eventualmente encontra uma solução, mesmo que deselegante."

            "Ele não consegue puxar a rolha, então a empurra para dentro, até que ela se desfaça
            em pó dentro da garrafa."
            jump chapter2_6

label chapter2_6:
    "As mãos dele tremem enquanto ele tenta derramar algumas gotas do vinho na
    palma da mão. Ele põe a garrafa na mesa de cabeceira."

    "O minotauro mergulha o dedo no vinho, deixando uma única gota quase
    caindo, e toca uma de suas feridas."

    "Ele repete o processo de novo e de novo. Algumas gotas caem na cama.
    Seu rosto franze a testa amargamente."

    "Quando seu punhado de vinho está quase no fim, ele esfrega a mão ainda molhada
    no crânio exposto."

    "Passaram-se apenas alguns minutos, mas você já pode notar algumas das feridas
    curando."

    "O minotauro percebe você assistindo. Seus lábios, ou o que resta deles, se curvam
    em um meio sorriso orgulhoso."

    asterion "Sim. Posso curar rapidamente, desde que tenha o vinho necessário."

    asterion "É uma pena que a garrafa cheia que escondi estava quebrada..."

    "Astério leva uma mão até as costas. Ele se encolhe quando esbarra em uma das
    escaras."

    menu:
        "Oferecer-se para espalhar o vinho para ele.":
            $ chapter2_affection += 1
            you "Me deixe ajudar você com isso. Não vai conseguir enxergar aí atrás."

            show Asterion:
                ease 1.0 yalign 1.45

            "Ele abaixa as orelhas em derrota, sabendo muito bem que você está certo."

            "No entanto, ele estende a garrafa de volta para você com uma velocidade que denuncia
            sua ansiedade. Sua cauda balança para frente e para trás."
            jump chapter2_7

        "Não fazer nada.":
            "Você fica onde está, observando enquanto o minotauro se esforça para tocar as
            escaras nas costas com um dedo molhado. Muitas gotas de vinho são desperdiçadas."

            show Asterion:
                ease 1.0 yalign 1.45
            "Ele olha para seus pés, orelhas caídas em derrota."

            "Você estende uma mão e ele devolve o vinho para você."
            jump chapter2_7

label chapter2_7:
    "Você encharca um pedaço de gaze velha com o vinho e começa o trabalho."

    "As feridas do minotauro têm uma coloração negra. Um óleo escuro parece ter
    se acumulado nelas, escorrendo por suas costas em rios claramente definidos."

    show Asterion:
        ease 0.2 yalign 1.42
        ease 0.3 yalign 1.45

    "Ele se contorce quando o tecido toca sua pele danificada, mas empurra de volta contra
    você ao mesmo tempo."

    "Suas feridas fecham rapidamente -- em uma velocidade quase inquietante."

    "Cinco minutos depois, você está sem vinho, mas foi o suficiente para livrar Astério
    de suas escaras mais egrégias."

    "Ele coloca uma mão em seu crânio."

    asterion "Precisarei de muito mais vinho para isto."

    "Você pergunta se há alguma outra maneira de ajudá-lo."

    if chapter2_affection >= 3:

        play music "music/seikilos.mp3" fadeout 4.0 fadein 4.0
        "Astério possui uma curva tímida nos lábios quando ele olha para você da
        cama. Sua cauda balança para a esquerda, para a direita. Ele balança os cascos
        sobre o chão."

        "Porém, quando ele fala, sua voz encontra-se grave e trovejando com sobriedade."

        asterion "Você já foi muito gentil, Mestre. Seria terrivelmente inapropriado da parte
        de um Zelador impôr uma tarefa ao seu Mestre, ainda mais na quantidade
        que você me ajudou até agora."

        "Seu único olho restante está aberto pela metade."

        asterion "Por favor, não se preocupe comigo."

        "Ele fala, então, com uma pontada de alívio."

        asterion "A menos que o Mestre tenha uma tarefa para mim, devo descansar um pouco aqui
        e depois ir me lavar. Estou muito inadequado agora para um Zelador do Hotel."

        asterion "O Mestre não precisa se preocupar."
        jump chapter2_8

    else:
        asterion "O Mestre não deve se preocupar comigo. Como eu disse antes, não posso morrer.
        Meu estado atual é transitório, deve passar antes que você perceba."

        asterion "Se o Mestre não tiver uma tarefa para mim, devo descansar um pouco
        e então ir me lavar para que eu possa estar apresentável."
        jump chapter2_8

label chapter2_8:
    you "Você não deveria comer um pouco primeiro? E se você desmaiar no
    banheiro?"

    show Asterion:
        ease 2.0 yalign 1.0 xalign 0.5

    asterion "Isto não será um problema. Posso obter sustento agora que você me
    aceitou a seu serviço."

    asterion "O Mestre comanda o Labirinto e, através do juramento, você
    me legou parte de seu poder. Não passarei fome outra vez."

    asterion "Há muito que posso lhe ensinar com prazer sobre o Labirinto, Mestre.
    Deve atender às suas necessidades se souber como conduzi-lo. Observe."

    pause 0.5

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

    pause 0.5

    "Por meio segundo, é como se o mundo inteiro piscasse ao seu redor e sua mente
    ficasse em branco durante o processo."


    if chapter2_affection >= 3:

        "Agora Astério tem em suas mãos um cacho de uvas transbordando."

        asterion "Você gosta de uvas? Espero que essas sejam de seu agrado."

        "Você hesita antes de aceitar a comida. Não deveria ele ser o primeiro
        a comer?"
        show Asterion:
            ease 1.0 zoom 1.05 yalign 1.05
        asterion "O Mestre come primeiro, só então o Zelador pode se alimentar. Independentemente disso,
        o Mestre tem sido gentil comigo e eu ficaria feliz em compartilhar com você."
        show Asterion:
            ease 1.0 zoom 1.0 yalign 1.0
        "O minotauro parece ansioso para que você prove as uvas. Elas são
        incrivelmente doces, mas você só pega algumas, de forma que ele comece a comer. Ele
        balança as orelhas e a cauda com sua apreciação, depois começa a devorar as uvas."

        "Ele mal olha para você agora. Assim que as uvas acabam, um novo cacho aparece
        em suas mãos, depois um copo d'água e mais frutas."

        "Quando ele finalmente olha para você, diminui a velocidade e tenta limpar
        o focinho de todos os pedaços suculentos. Seu olho denuncia um toque de autoconsciência."

        show Asterion:
            ease 1.0 yalign 1.2

        asterion "Sinto muito. Sou mais fera do que homem. Às vezes leva
        o melhor de mim. Eu não deveria ser tão bruto na presença do Mestre."

        if chapter2_affection >= 6:
            "Ele quase parece encolher na sua frente, tentando se
            esconder."

            "Há uma vergonha claramente estampada em seu rosto por ter requerido tanto
            a sua assistência."
            jump chapter2_9

        if chapter2_affection >= 3:
            asterion "Embora, em minha defesa, minhas maneiras à mesa sejam
            excelentes quando tenho o benefício de não estar faminho."

            "Ele abre um meio sorriso."

            "Mesmo nu, e com um focinho desfigurado coberto de suco de uva, Astério
            olha para você com uma postura de nobreza: suas costas estão retas e seus
            ombros mudam ligeiramente para uma postura mais larga."

            "Há um toque de orgulho em seu sorriso quase imperceptível --
            a pequena alegria de ter mantido a dignidade, mesmo em circunstâncias
            incrivelmente difíceis."
            jump chapter2_9

    else:
        show Asterion:
            ease 1.0 zoom 1.05 yalign 1.05
        "Agora que Astério tem em suas mãos duas maçãs. Ele estende uma para você, seu olhar
        direcionado para baixo em uma reverência. Ele dá uma mordida apenas quando você prova a sua."
        show Asterion:
            ease 1.0 zoom 1.0 yalign 1.0
        asterion "O Mestre come primeiro. Sempre."

        "Assim que a primeira maçã vai embora, outra aparece em suas mãos. O
        processo se repete uma e mais uma vez, progressivamente mais rápido, até que
        Astério fica como um lobo rasgando uma carcaça."

label chapter2_9:
    "Talvez este seja um bom momento para deixar o minotauro ter um pouco de privacidade."

    you "Vou deixar você descansar. Eu volto para ver como você está mais tarde."

    show Asterion:
        ease 1.0 zoom 1.0 yalign 1.2 xalign 0.5
        ease 1.0 yalign 1.0

    "Astério interrompe seu frenesi de alimentação para se curvar a você -- digno, apesar
    dos sucos escorrendo por sua boca e peito."

    asterion "Eu estarei apresentável após o banho, Mestre. Não se preocupe comigo."

    menu:
        "Oferecer-se para ajudar com o banho?"
        "Sim.":
            you "Tem certeza que não quer ajuda com o banho? Eu não quero
            você caia e se machuque."

            "O minotauro se encolhe, sua fome dando lugar a um olhar mais frio."

            asterion "Eu falo a verdade, Mestre. Posso estar frágil agora, mas depois
            desta refeição e de um descanso estarei forte o suficiente. Há um banheiro
            bem aqui, na enfermaria."

            asterion "Eu compreendo sua preocupação, mas eu... eu posso fazer isso."

            "O ar fica tenso por um momento. A voz de Astério ressoa com uma
            firmeza inesperada."

            "Ele coloca as mãos sobre a virilha e fecha as pernas."

            asterion "O Mestre não precisa ter medo."

            asterion "Devo estar apresentável na próxima vez que nos encontrarmos."

            "Ele se curva para você e permanece assim até você sair da enfermaria."

        "Não.":
            you "Tudo bem. Se você precisar de ajuda, apenas... Grite, certo? Eu não
            quero que você se machuque. Mesmo que não possa morrer, como você diz."
            $ global_affection += 0.5

            if chapter2_affection >= 4:
                "Astério dá uma boa olhada em você. Seu olho escuro brilha suavemente
                sob a luz da enfermaria. Há quase uma umidade nele."

                "Ele respira tão lentamente enquanto olha para você, a cauda balançando de um
                lado para o outro. Ele observa cada característica de seu rosto, uma de cada vez."

                asterion "Obrigado por me libertar, Mestre."

                "Seu olho denuncia sua sonolência. Ele se curva para você e, ao fazê-lo,
                quase adormece. Você diz para ele descansar."

                asterion "Eu irei."

                "Você o deixa em sua privacidade."

            else:
                "O minotauro se curva para você, com uma elegância condizente à de um príncipe --
                e não um esqueleto coberto em polpa."

                "Ele permanece assim até você sair da enfermaria."

    scene bg black
    with Dissolve(1)
    pause 1

##############################################################################
#                       CHAPTER 2: GETTING THE WINE
##############################################################################
#PC finds the ledger of contracts.
#PC checks up on Asterion.
#They find the wine bottle at the lounge is broken.
#Asterion takes PC to the Master's Quarters. The bottle there is empty.
#PC goes to the underground.
label chapter3:
    $chapter = "Capítulo 2"
    define chapter3_affection = 0
    if chapter2_affection >= 4:
        $ global_affection += 0.5

    else:
        $ global_affection += 0

    play music "music/GreekFolkSong.ogg" fadeout 1.0 fadein 1.0

    call screen ChapterTransition("Capítulo 2", "Afogue suas mágoas")
    pause 0.5
    $save_name=output_save_name("Capítulo 2")

    scene bg oldlobby
    with Dissolve(1)

    "Você está de volta ao corredor em ruínas. Ele se estende até o saguão e
    mais adiante no Hotel."

    "Mais à frente, algo chama sua atenção. Um volume encadernado em couro, não muito
    diferente do livro de registros que você encontrou no escritório da recepção, foi
    jogado negligentemente ao chão."

    show image "gui/inventory/icons/big/item_Ledger.png":
        xalign 0.5
        yalign 0.4
    with Dissolve(.5)

    "Uma olhada rápida revela que a maioria de suas páginas foram arrancadas,
    mas o verso da capa contém algo escrito no mesmo estilo da escritura."

    "Os glifos se alteram e torcem sob seu olhar, marchando em posição quanto mais
    você olha. Depois de alguns minutos, no entanto, torna-se desconfortável, como se sua
    mente estivesse sendo perfurada pelo papel."

    "Você se senta no bar do salão, a apenas trinta centímetros de distância dos
    cacos de vidro verdes espalhados sobre a mancha roxa. Você redireciona toda a sua atenção
    para decifrar este manuscrito."

#To-do: Add the ledger of contracts.

    play sound "sfx/pageflip.ogg"

    contract "{i}Sentença de Astério"
    contract "{i}Por meio deste, os deuses do Olimpo sentenciam o Prisioneiro Astério à danação eterna por sua mansidão e covardia em face à adversidade."
    contract "{i}Com esta sentença, sua prisão é criada, um Labirinto nascido do icor dos deuses."
    contract "{i}O Labirinto deve acolher mortais perdidos sem nenhum lugar para ir. Entre eles, um Carcereiro será escolhido para comandar e reescrever o domínio."
    contract "{i}A missão do Carcereiro e do Labirinto é garantir a tortura eterna do Prisioneiro."
    contract "{i}O Carcereiro gozará de poder e liberdade para reescrever o Labirinto da forma que melhor enaltecer seu ponto de vista."
    contract "{i}Astério de Creta, filho adotivo do Rei Minos, e cada gota de seu sangue blasfemo é, por meio deste, condenado ao Labirinto."
    contract "{i}Por meio deste decreto, a vontade dos deuses é realizada."

    hide image "gui/inventory/icons/big/item_Ledger.png"
    with Dissolve(.5)

    $UI_permissions['ledger'] = True
    $inventory.add_item("Ledger")

    play sound "sfx/asterionchord.mp3"
    if renpy.variant("android"):
        "{i}Você obteve o {color=[UIColorOrange]}Livro de Registros{/color}."
    else:
        "{i}Você obteve o {color=[UIColorOrange]}Livro de Registros{/color}.
        \nO Livro de Registros lista os itens adquiridos, hóspedes e informação adicional.
        Clique no ícone no canto superior direito da tela para abri-lo."
    pause 1

    "Você é puxado de seu transe com a batida de uma porta fechando no corredor."

    "A luz ao seu redor oscilou. Você olha para trás, na direção do jardim, e vê que o sol
    já está se pondo. O tempo passou em um piscar de olhos, e agora o barulho de cascos batendo no piso
    de mármore ecoa pelo corredor."

    show Asterion:
        zoom 1.0 alpha 1.0 yalign 1.0 xalign 0.5
    with Dissolve(1)

    show Asterion:
        ease 1.0 yalign 1.2

    "O minotauro entra no salão, o vê, e se curva."

    menu:
        "Cumprimentá-lo.":
            $chapter3_affection += 1
            you "Oi, Astério. Você dormiu bem?"
            asterion "Sim, Mestre. Devo lhe agradecer por me permitir descansar."
            you "É bom ouvir isso. Presumo
            que você não teve problemas com o seu banho?"
            asterion "Não tive."
            show Asterion:
                ease 1.0 yalign 1.0
            "Astério se levanta e olha para você diretamente."

        "Permanecer em silêncio.":
            "O minotauro permanece curvado por um minuto inteiro. Ele não se moverá até que
            você o direcione a fazê-lo. Você o dá um aceno com a cabeça para prosseguir."
            show Asterion:
                ease 1.0 yalign 1.0

label chapter3_1:
    asterion "Eu deveria pedir seu perdão. O deixei esperando sem fornecer uma
    excursão no Hotel ou orientação sobre seu funcionamento interno. Isto foi terrivelmente
    inadequado de minha posição como Zelador do Hotel."

    asterion "Estou à sua disposição agora, entretanto."

    you "Tem algumas perguntas me corroendo, se você não se importa. Mas nós
    podemos deixar para depois se você não estiver se sentindo bem."

    asterion "Estou bem o suficiente para cumprir meu dever. O que o Mestre
    deseja saber?"

    you "Bem, para começar..."

    $myChoices = [ ("Como você está se sentindo?", "id1"), ("Como você fez a comida aparecer do nada?", "id2"), ("Que outras criaturas míticas existem?", "id3")]
    label after_nap_conversation:
        $narrator("O que você perguntará a Astério?", interact=False)
        $result = renpy.display_menu(myChoices)

        if result == "id1":
            you "Bem, admito que estou um pouco preocupado com você. Como você está se sentindo?
            O banho foi agradável?"

            "O minotauro altera o olhar, tentando decifrar seu tom e expressão.{w}
            Procurando por um toque de ironia, ou talvez malícia."

            asterion "Eu {w=0.2}-- Eu estou bem. Foi bastante peculiar tomar banho depois de todos
            esses anos.{w} Eu tinha esquecido como é a sensação da água."

            asterion "Tive sorte que minhas{w=0.2} -- minhas feridas estavam fechadas. Do contrário,
            poderia ter sido uma experiência dolorosa."

            asterion "Por um bom tempo, apenas fiquei ali parado, embaixo d'água.{w=0.2}
            Pensando e sentindo."

            asterion "Tudo isso é para dizer...{w=0.2} Sim, estou me sentindo bem.{w} É
            gentil de sua parte perguntar."

            asterion "Isso é tudo o que você gostaria de saber?"
            $ myChoices.remove(("Como você está se sentindo?", "id1"))

        if result == "id2":
            you "Então, sobre a comida...{w} Antes você simplesmente fez frutas aparecerem nas suas mãos. Foi
            como se o mundo inteiro tivesse \"piscado\" por um segundo."

            you "O que exatamente está acontecendo?"

            asterion "Lamento terrivelmente, meu senhor. Falhei em explicar a tempo.{w}
            Este domínio opera sob regras muito peculiares."

            asterion "Está{w=0.2} -- está relacionado ao juramento que fiz. Contratos,{w=0.2}
            juramentos,{w=0.2} promessas,{w=0.2} todas as manifestações de vontade do Mestre
            podem ter efeito obrigatório."

            asterion "Leis nesta terra são auto-impositivas, se marcadas pelo poder do senhor."

            asterion "O juramento que fiz refere-se a um antigo fragmento de lei, o
            Estatuto de José, o Misericordioso.{w} Em um de seus artigos, é permitido a mim
            invocar comida."

            asterion "Em circunstâncias comuns, o juramento teria sido um evento
            formal, onde eu teria lido o Estatuto por completo, mas nossa situação foi
            realmente péssima."

            asterion "Sinto muito, meu senhor. Apresentarei o Estatuto a você assim que possível,
            para que possa analisá-lo."

            you "Obrigado. Eu não gosto de assinar contratos que não li.{w} Mas não vá
            exigindo demais de si mesmo, suponho que isso não seja uma prioridade agora.
            Recuperar a sua saúde é mais importante."

            you "Ainda assim, não foi exatamente sobre isso que eu perguntei.{w} Você pode invocar
            comida por causa do juramento, mas como pode comida ser invocada assim em
            primeiro lugar?"

            you "Em outras palavras... que tipo de lugar é este?"

            pause 0.5

            "O olhar do minotauro redireciona para o chão. Seus cascos raspam contra
            ele."

            asterion "Este domínio foi criado para me aprisionar,{w=0.2} a missão
            do carcereiro é manter a vigília. E, para este propósito, os deuses julgaram
            adequado que matéria pudesse ser criada espontaneamente."

            asterion "...Assim, o trabalho do carcereiro não seria interrompido
            por \"coisas frívolas\" como limitações materiais."

            asterion "É, também, a compensação do Mestre.{w} Ser capaz
            de criar aquilo que seu coração desejar a partir do nada...{w=0.2}
            esta é uma baita recompensa, você não diria?"

            you "Realmente. Isso não é um poder pequeno, com um pouco de criatividade,
            qualquer um poderia fazer uma fortuna com esse lugar."

            asterion "Bem, existem algumas limitações...{w} Principalmente, o domínio se
            recusa a fazer metais como ouro e prata em grandes quantidades."

            asterion "Mas...{w=0.2} Mestres anteriores foram bastante criativos, e
            isso não os impediu de acumular suas próprias fortunas."

            asterion "Como zelador, é meu dever instruí-lo sobre este assunto.
            Eu posso mostrá-lo como invocar materiais."

            you "Eu agradeceria muito, mas nós podemos deixar isso para depois se for
            complicado. Eu tenho mais assuntos que gostaria de discutir com você."

            asterion "Muito bem.{w} O que o Mestre deseja saber?"
            $ myChoices.remove(("Como você fez a comida aparecer do nada?", "id2"))

        if result == "id3":
            you "Ainda estou um pouco abalado depois de saber que os deuses gregos são reais. Ou foram."

            you "Há muitas implicações nisso, sabe. Por exemplo... Posso presumir
            que existe uma vida após a morte, então?"

            pause 1.0

            asterion "Possivelmente."

            asterion "Fui enviado para uma vida após a morte após minha morte.{w} Chamava-se Hades."

            asterion "Mas isto foi naquela época, milhares de anos atrás. Eu não sei o que
            aconteceu com os deuses ou se o reino deles persiste até os dias de hoje."

            asterion "Também não sei se existem outros reinos de vida após a morte em primeiro
            lugar, embora eu acredite que este seja o caso."

            asterion "Estou ciente, no entanto, que a adoração aos olímpios há muito perdeu o
            favoritismo.{w} Se o Mestre pudesse alimentar minha curiosidade, ainda é assim?"

            you "Não, ninguém mais glorifica esses deuses. É uma religião morta, com certeza.{w} A maior parte
            do que você vai encontrar são pessoas estudando sobre eles durante as aulas de História, e alguns lugares
            usam os deuses como símbolos."

            you "É basicamente isso."

            asterion "Entendo. Então, a respeito disso, nada mudou desde que eu fui trancado."

            you "Tem uma coisa que eu quero saber, no entanto. Você me falou sobre os deuses
            e... outros seres míticos.{w} Eu quero saber mais sobre isso, se você não
            se importa."

            asterion "Ah, bem. Sim, esta é uma questão com a qual os Mestres de tempos anteriores
            também tiveram problemas."

            asterion "Apesar dos meus milhares de anos, devo admitir que não possuo
            conhecimento completo sobre a variedade de seres míticos que existem."

            asterion "Eu sei apenas daqueles que passaram por este Hotel, e do que eles
            tiveram gentileza o suficiente para compartilhar comigo."

            asterion "Eles usavam um amuleto encantado para passar despercebidos como humanos. {w}Mas não foi
            sempre assim, este costume começou há apenas alguns séculos."

            asterion "Quando eu era criança, não existia tal coisa...{w} Minha verdadeira
            forma estava à mostra para todos verem.{w} E o Pai Minos garantiu que eu
            fosse visto."

            asterion "De qualquer forma, os amuletos deles nunca funcionaram neste domínio. {w}Eu não sei o
            porquê, mas sempre foi uma constante."

            asterion "Era bastante peculiar, antigamente. Hóspedes humanos e sobrenaturais se
            misturavam."

            asterion "É sempre chocante no começo, mas depois de um tempo...{w=0.2}
            torna-se especial. {w}Humanos são ansiosos para aprender sobre o desconhecido,{w=0.2}
            e os seres míticos anseiam por viver sem um disfarce."

            asterion "Agora, de volta ao século 20...{w} Eles começaram a usar um...{w}
            Qual era o nome mesmo?"

            asterion "Era um livreto que eles carregavam..."

            you "Um passaporte?"

            asterion "Sim, um passaporte. Eles o encantavam e o mantinham por
            perto, sempre.{w} Era imperceptível."

            asterion "Mas eles carregavam vários amuletos com eles -- jóias, muitas vezes --
            no caso de serem separados de seus documentos."

            you "Eles faziam passaportes falsos, então? Como era isso?"

            asterion "Ah, eu acho que não. {w}Lamento não saber muito sobre isto,
            mas tive a impressão de que esses livretos eram emitidos por governos."

            asterion "Como se... Os governos fizessem os passaportes encantados."

            asterion "Algumas vezes me foi dito que eles precisavam ser registrados. Era bastante
            comum para seres míticos, até mesmo os funcionários, serem obrigados a retornar
            para seus países por causa de assuntos burocráticos."

            asterion "...{w}Ou para a guerra."

            asterion "... Mestre Jean-Marie não foi o único homem que perdemos para as
            Grandes Guerras."

            you "Eu não esperava que existisse...{w=0.2} burocracia em torno de seres
            míticos."

            asterion "De fato, é um pouco peculiar.{w} Mas gostaria de enfatizar que aprendi
            tudo isso de hóspedes anteriores. Nunca presenciei por conta própria."

            you "Ah, antes que eu me esqueça...{w=0.2} Encontrei esses dentro de um cofre, perto
            da recepção."

            $inventory.remove_item('Passaportes')

            "Você dá para Astério os {color=[UIColorOrange]}Passaportes{/color}."

            you "Esses são os passaportes encantados? Eles não parecem ter nada fora
            do comum."

            "O minotauro examina cada um dos passaportes. Franze a testa
            e, por um segundo, ele e seu lábio inferior estremecem."

            asterion "Sim, são estes.{w} Eu reconheço os nomes, estes são
            os passaportes."

            asterion "...Eles odiavam estas coisas. Elas eram suas algemas.{w}
            Foi por isso que eles estavam tão ansiosos para ficar e trabalhar aqui, em um lugar
            onde não precisavam esconder suas verdadeiras formas."

            asterion "Não se trata apenas de suas formas, também.{w} Há outra
            coisa que estes passaportes faziam:{w=0.2} eles os tornavam fáceis de se
            esquecer e passar despercebidos."

            asterion "Novamente, eu nunca testemunhei por conta própria,{w=0.2} mas frequentemente
            me diziam que era terrivelmente difícil fazer...{w=0.3} amigos,{w=0.3}
            estabelecer relações também, quando aqueles que você ama estão propensos
            a esquecer que você existiu."

            you "Isso soa difícil, para dizer o mínimo.{w} A existência deles deve
            ser bem solitária."

            "Astério mergulha em pensamentos enquanto folheia as páginas dos passaportes.
            Ele parece não ter ouvido você."

            "Quando ele fecha o último, seu olhar retorna para você com um ar melancólico {w=0.2}--
            isto é, mais melancólico que antes."

            asterion "O Mestre tem mais perguntas?"
            $ myChoices.remove(("Que outras criaturas míticas existem?", "id3"))

        $ long = len(myChoices)
        if long > 0:
            jump after_nap_conversation
        jump chapter3_1_2

label chapter3_1_2:

    you "Acho que é tudo o que tenho em mente, por enquanto.{w} É muita coisa para absorver."

    you "Que deuses e criaturas míticas existem, para começar, e que esse
    lugar pode simplesmente criar matéria a partir do nada."

    you "Obrigado por me contar tudo isso. Eu só vou precisar de algum tempo para
    processar a coisa toda."

    asterion "É um prazer servir.{w=0.2} Posso oferecer uma bebida ao
    Mestre?{w=0.2} Seria de seu agrado?"

    "Ele olha atrás de você, para a parede coberta com dezenas de garrafas de bebida."

    you "Bem, não acho que essas são seguras.{w=0.2} Eu verifiquei algumas delas,
    não estavam cheirando bem."

    asterion "Não será um problema. Posso invocar mais para o Mestre."

    you "Tudo bem, vá em frente."

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

    "O minotauro caminha atrás do balcão. O mundo pisca ao seu redor e, quando
    você olha de volta, ele segura uma garrafa de uísque."

    "Ele caminha com leveza nos passos, mas pausa quando se depara com a mancha roxa
    no chão."

    show Asterion:
        ease 1.0 yalign 1.4

    "Qualquer resquício de alegria que estava em seu rosto desaparece. Ele se abaixa até o
    chão e passa uma mão sobre o vinho seco."

    show Asterion:
        ease 1.0 xalign 0.52
        ease 1.0 xalign 0.5

    "Ele tenta tirar o pó do chão e, em seguida, esfregar a mão sobre
    ele, sem sucesso."

    you "O que tem em mente?"

    "O minotauro fala sem olhar para você."

    asterion "Ele foi até o fim, o Mestre anterior. Me trancar não foi o
    suficiente, ele teve que expulsar todos os hóspedes e ir tão longe
    a ponto de quebrar as garrafas."

    asterion "Ele sabia que o vinho podia me curar."

    asterion "Eu tinha um na enfermaria, para o caso de me machucar e precisar de
    ajuda, e um aqui para o meu prazer."

    asterion "Espero que ele não tenha quebrado os outros também. É impossível
    invocar mais deliberadamente."

    show Asterion:
        ease 1.0 yalign 1.2
        ease 1.0 yalign 1.0

    "O minotauro levanta e se apoia no balcão. Ele invoca um pano
    e o sacode."

    asterion "Não importa. Agora, o que o Mestre deseja? Devo dizer desde já,
    o licor do Hotel é bastante impressionante."

    menu:
        "Perguntar onde você pode encontrar o vinho.":
            $chapter3_affection += 1
            "Astério pode estar de pé e caminhando, mas ainda se encontra longe de estar bem.
            Ele pode aproveitar a ajuda."
            you "Você mencionou ter mais garrafas de vinho. Onde elas estão?{w=0.2} Tenho
            certeza que posso buscar elas para você."
            "Astério olha para o lado, aparentemente pensando sobre sua
            proposta."
            asterion "Não é adequado que o Zelador seja assistido pelo Mestre.
            {w=0.2}Eu suponho,{w=0.2} no entanto,{w=0.2} que seria meu dever levá-lo até lá,
            de qualquer maneira."
            asterion "Se não me falha a memória, deve haver uma garrafa nos
            aposentos do Mestre."
            jump chapter3_2

        "Pedir uma bebida.":
            "Você conta para Astério sobre sua bebida favorita. Ele escuta atentamente."

            show blackback:
                alpha 1.0
            with Dissolve(0.25)
            hide blackback
            with Dissolve(0.25)
            play sound "sfx/hum.ogg"

            "Enquanto você fala, o Hotel pisca ao seu redor. Um segundo após
            terminar sua descrição, a bebida está na sua frente."
            asterion "Espero que seja do agrado do Mestre."
            "Não é ruim, mas também não é bom. Tem um gosto um pouco estranho."

            "Astério percebe a decepção em seu rosto e a orelha dele abaixa."
            asterion "Suponho que o Hotel ainda esteja enferrujado. Pode demorar um pouco até
            que seja tão capaz quanto costumava ser."
            asterion "...Ou talvez eu seja o problema.{w} Devo dizer que sinto
            muito."
            "Ele murmura algo que você não consegue entender direito. Seu olho restante
            palpita."
            asterion "Talvez este seja o momento adequado para apresentar o Mestre
            a seus aposentos. Certamente você deve estar cansado, já está escurecendo."
            jump chapter3_2

#Goes to the Master's Quarters.
label chapter3_2:
    scene bg staircase
    with Dissolve(1.0)
    "Vocês dois retornam para o saguão do Hotel. A escada em espiral, agora tingida
    de laranja pela claraboia, continua tão acolhedora quanto antes."

    "O quarto andar não tem portas, no entanto."

    asterion "Aqui. Este andar é dedicado ao Mestre e àqueles que ele permite."
    asterion "O Hotel é moldado à vontade do Mestre. Deseje uma porta e ela
    será feita. Meu poder é semelhante ao seu, embora muito mais fraco."
    asterion "No devido tempo, o Hotel deverá estar em conformidade com seu ponto de vista
    de cima a baixo."

    "Quase não requer que você se concentre. Apenas um pensamento passageiro é o suficiente
    para fazer o Hotel piscar para dentro e fora da realidade."

    "A porta dá as boas-vindas para você. Ela desaparece depois que você e Astério cruzam seu limiar."

    scene bg oldquarters
    with Dissolve(1.0)

    show Asterion
    with Dissolve(1.0)

    "A sala de estar à sua frente parece ter resistido aos danos do tempo
    melhor que o resto do Hotel."

    "Está empoeirada e alguns pedaços da parede expõem o início de mofo,
    mas isto não é nada em comparação à devastação que você viu na cozinha."

    "Astério não fala nada a princípio. Seu olhar parece estar perdido na distância
    enquanto que ele anda em volta inspecionando a sala. Há fileiras de esculturas de
    madeira nas prateleiras."

    "Durante o silêncio do minotauro, você aproveita a oportunidade para explorá-la sozinho."

    "A sala de estar é um amplo salão pensado para receber os hóspedes, tanto em grande
    número como para encontros íntimos. Sob a luz do pôr do sol, o piso de madeira
    colore a sala com um toque caloroso e suave."

    "Há um quarto principal com um vasto armário ainda cheio de roupas --
    nenhuma que você usaria, no entanto. É um guarda-roupa saído direto dos anos 30,
    organizado com uma devoção incansável."

    "Há também um grande escritório, do tipo que você esperaria de um executivo importante.
    Sobre a mesa está uma seleção de canetas-tinteiro finamente decoradas e um conjunto de
    documentos, em sua maior parte escritos em delicada caligrafia."

    "A maioria dos documentos estão assinados por um \"Mestre Jean-Marie\", embora um punhado deles
    comporte um rabisco bastante ilegível para uma assinatura."

    "Há um banheiro finamente decorado em um espaço estreito ao lado da
    sala de estar. No final do corredor, depois de uma curva fechada, há uma câmara
    apertada e sem janelas."

    "Possui bastante calor residual da sala de estar, embora silencioso.
    A cor da madeira está desbotada, o teto é um metro mais baixo, há pouca ou
    nenhuma mobília."

    "Há, no entanto, uma áustera cama a qual parece maior que uma típica cama de
    solteiro. Ao lado dela encontra-se uma pequena cômoda com um punhado de livros de
    poesia empoeirados e empilhados em cima, com mais esculturas de madeira ao lado."

    "Este quarto oferece privacidade, mas pouco além disso."

    "Astério está examinando as coisas quando você chega. Ele segura com carinho cada escultura de madeira
    do quarto, checando-as uma a uma. Muitas delas retratam touros."

    "Ele abre um dos livros e um marcador de página cai dele. Ele olha para baixo,
    mas não se preocupa em pegá-lo."

    "O minotauro abre um pequeno armário em um canto e tira o que parece ser um longo
    pedaço de tecido. Ele o cheira, ou talvez o abraça contra o peito. Seu focinho ossudo deixa
    uma mancha de sangue sobre ele."

    "Ele suspira e estremece. O minotauro olha de volta para você, reconhecendo sua
    presença pela primeira vez desde que chegou aqui."

    asterion "Lamento terrivelmente, estava perdido em pensamentos."
    asterion "Neste andar ficam os aposentos do Mestre. Ele contém seu quarto,
    escritório, sala de estar e quaisquer outras instalações que você deseje adicionar."
    asterion "Este cômodo em que estamos, este... era o meu quarto. Eu sirvo ao Hotel, mas,
    acima de tudo, sirvo ao Mestre. Muitas vezes é considerado conveniente me ter
    por perto, pois posso cozinhar e ajudar o Mestre como ele achar adequado."
    asterion "Alguns mestres tiveram filhos, por exemplo. Eu ajudava a cuidar
    deles, proporcionando entretenimento e brincadeiras enquanto o Mestre descansava."
    asterion "Mestre Jean-Marie era um homem de cultura. Ele apreciava quando eu
    tocava minha lira para ele à noite."

    "O olhar do minotauro vagueia novamente. Suas mãos acariciam uma escultura de madeira."

    asterion "...O vinho deve estar na cozinha."

    "Vocês dois vão até lá. Desta vez, não há nenhuma mancha roxa no chão ou cacos de
    vidro espalhados. A garrafa vazia está delicadamente posicionada no balcão ao lado
    da pia."

    show Asterion:
        yalign 1.1

    "Astério se encolhe novamente."

    asterion "Pelo menos ele não danificou as esculturas do Mestre Jean-Marie."

    you "Essa era a última garrafa?"

    asterion "Não. Tenho uma última garrafa escondida e estou certo de que deve estar
    intacta. Não tinha como ele saber sobre esta."

    asterion "Está no térreo, lá embaixo, descendo as escadas."

    you "\"Lá embaixo\"?"

    asterion "...Cerca de trinta andares abaixo, sim."

    show Asterion:
        ease 1.0 yalign 1.0

    asterion "Não se preocupe, Mestre. Já está ficando tarde. Eu posso prepará-lo uma
    refeição apropriada e limpar a poeira de seus aposentos. Você pode descansar durante a noite, eu tratarei
    desse assunto depois que você for dormir."

    $chapter3_affection += 1
    jump chapter3_3

label chapter3_3:
    you "Não, não posso deixar você fazer isso. Você não está em condições de descer e subir
    trinta lances de escada."

    you "Me diga onde encontrar a garrafa. Enquanto eu vou até lá, você pode
    verificar os aposentos, se quiser examinar os pertences do Mestre
    anterior."

    show Asterion:
        ease 1.0 xalign 0.51
        ease 1.0 xalign 0.5

    "Por um único momento, você observa Astério olhando para o lado, ponderando antes
    de dar a resposta."

    asterion "...Muito bem. Eu obedeço."

    asterion "O vigésimo quinto andar subterrâneo é muito parecido com este,
    sem portas. Você pode comandar ao Hotel para revelar o caminho."

    asterion "É onde armazenamos as coisas ao longo dos séculos. No final do corredor,
    há uma pintura de parede, a garrafa deve estar em frente
    a ela."

    "Você responde com um polegar para cima enquanto invoca uma porta para o lado de fora."

    #"You don't waste any time. As you are leaving, however, Asterion speaks up.
    #There's an edge of anxiety in his voice, and a petulance in speaking to
    #you without being addressed first."

    #asterion "Master, if you would allow me to provide a warning, that floor is
    #where we keep the belongings of previous Masters."

    #asterion "Those are cherished, fragile heirlooms. I would plead with you to avoid
    #touching them."

    #"You answer with a thumbs-up as you summon a door out."

    scene bg staircase
    with Dissolve(1.0)

    "Mais uma vez, você é envolvido pela luz do sol passando através da
    claraboia. Seus passos ecoantes possuem uma sonoridade aderida, uma pontada
    de vida neste hotel abandonado."

    "Assim que você chega ao térreo, no entanto, seu caminho torna-se mais escuro. Seus passos
    agora soam tímidos em frente a um véu opressor."

    scene bg staircase2
    with Dissolve(1.0)

    "O vigésimo quinto andar não vê a hora de chegar. Uma placa em uma parede
    inexpressiva o cumprimenta. A porta pisca em sua frente com uma
    ansiedade semelhante."

    scene bg underground
    with Dissolve(1.0)

    "O corredor se estende para o longe, suas laterais revestidas com todo tipo
    de objetos."

    "Conjuntos de armaduras, móveis, estátuas, baús de tesouro cheios de bugigangas de todas as
    eras."

    menu:
        "O que você faz?"
        "Procurar pela garrafa de vinho.":
            jump chapter3_4
        "Examinar bugigangas.":

            "Você tira um momento para examinar seus arredores."

            if player_background == "humanities":
                "Um objeto chama sua atenção em um canto ao lado no corredor, em cima de uma
                pintura coberta por um lençol de linho."

                "É uma coroa feia e marrom de galhos entrelaçados. Duas dúzias de folhas
                secas estão espalhadas ao redor dela e no chão."

                "Você sabe o que é isto: uma guirlanda de oliveira, uma coroa tradicionalmente dada aos
                vencedores dos jogos olímpicos. Um símbolo de vitória."

                "Mas esta guirlanda aparentemente não comporta nenhuma glória. É uma coroa de espinhos seca
                deixada nas profundezas do solo, provavelmente para ser esquecida."

                "Você a deixa lá, intocada. É tão antiga que mesmo o manuseio poderia quebrá-la."

            if player_background == "tech":
                "Você caminha pelo corredor, fazendo algumas paradas ao longo do caminho para
                observar melhor alguns dos itens e artefatos ao seu redor."

                "Entre todos os artefatos antigos, você ocasionalmente vê alguns itens mais relativamente
                modernos. À sua esquerda, você vê prateleiras com uma série de pequenos modelos de motores
                a vapor que parecem ter saído diretamente de um museu."

                "Todos eles têm uma pequena placa de bronze com a mesma assinatura
                gravada em cima, que você vê passando por pequenas alterações conforme o ano
                aumenta ao lado e os modelos ficam mais elaborados."

                "Mais à frente, você avista equipamentos elétricos desmontados em expositores.
                O que parecem ser versões antigas de tubos de vácuo, cabos de cobre
                enrolados em um isolamento duro e o que deve ser uma bateria voltaica."

                "Você mal consegue acreditar no que está vendo ao passar por um trabuco em tamanho real
                parcialmente montado. Você não tem certeza se o corredor parecia tão espaçoso assim antes
                de chegar na frente dele."

                "Você continua andando para não desenvolver uma dor de cabeça tentando trabalhar sua
                mente em torno disso e continua procurando a garrafa."

            if player_background == "math":
                "Enquanto você observa com os olhos arregalados a coleção de artefatos e bugigangas, uma
                parte da parede direita chama sua atenção. Há uma sensação de ordem e cuidado meticuloso
                neste expositor que o faz se destacar da bagunça."

                "Uma escrivaninha elegante e antiquada de jacarandá encontra-se ao lado de fileiras de mesas e armários,
                contendo uma miríade de livros, documentos emoldurados e outros itens,
                alguns em recipientes de vidro para preservação."

                "Os documentos emoldurados na parede variam de pedaços de papel amassados a páginas
                elaboradamente decoradas, aparentemente arrancadas de livros. Muitos estão cobertos
                de diagramas e uma quantidade surpreendente está escrito em Árabe e Sânscrito."

                "Atrás das portas de vidro dos armários você vê o que pode dizer que são antigos
                instrumentos de medição e contagem, e alguns que você não consegue distinguir de forma alguma."

                "Está evidente que alguém dedicou bastante tempo e cuidado à curadoria desta parte
                do corredor. Mas você tem uma tarefa a cumprir e agora não é hora de continuar
                contemplando a coleção para o próprio lazer."

            if player_background == "leader":
                "Ao lado, você nota uma longa vitrine com o que parecem ser conjuntos
                de armadura em manequins."

                "Há cerca de uma dúzia de modelos diferentes. Embora todos variem muito
                entre si -- parecem ter sido feitos ao longo de vários séculos --
                todos parecem leves e sem intenção de serem usados em guerras de larga escala."

                "Uma pequena placa ao lado contém \"Armaduras de Guardas do Hotel\" escrito em cima,
                juntamente com os anos em que cada um dos conjuntos foi fabricado."

                "O mais antigo data do século XIV."

                "...Parece, no entanto, que a coleção não está completa: há um manequim
                cuja armadura está faltando parcialmente. Possui uma faixa roxa amarrada à cintura."

                "Não há muito mais para ver nas armaduras. Você prossegue pelo corredor."

            if player_background == "arts":
                "Há várias pinturas dispostas no canto lateral da sala e uma estante
                com o que parece ser uma coleção de cadernos."

                "A maioria das pinturas está coberta com lençóis de linho. Você reconhece que esta coleção
                possui obras que datam de séculos atrás."

                "Você dá uma olhada nos cadernos em cima da prateleira. O primeiro que você apanha o deixa
                perplexo na mesma hora: está repleto de desenhos que lembram muito o estilo de
                Picasso."

                "Possui dezenas de desenhos de minotauros. É inconfundível: este é o caderno de
                rascunhos de Picasso, possivelmente um que ele usou na preparação de sua Suíte Vollard."

                "Este é um achado incrível. Você pode apenas imaginar que outros tesouros podem estar escondidos
                aqui."

                "...Mas, no momento, você possui outra prioridade. Haverá muito tempo para
                explorar esta coleção. Você coloca o caderno de volta e prossegue."

            if player_background == "speedrunner":

                "É tudo lixo fedorento."

                "Nada disso é útil e, na verdade, você está perdendo seu tempo olhando
                em volta."

                "Você segue pelo corredor."


label chapter3_4:
    "Quando você chega ao final do corredor, os objetos fazem uma curva fechada para o que você
    esperaria de um museu sobre a Grécia Antiga."
    scene bg fresco
    with Dissolve(1.0)

    show image "gui/inventory/icons/big/item_Wine Bottle.png":
        xalign 0.5
        yalign 0.4
    with Dissolve(1)

    "Lá está a \"pintura de parede\" que Astério falou para você. Bem na frente dela encontra-se
    uma garrafa de vidro lacrada. Está coberta de poeira, seu rótulo está desbotado."

    $inventory.add_item("Wine Bottle")

    play sound "sfx/asterionchord.mp3"
    "Você obteve uma {color=[UIColorOrange]}garrafa de vinho{/color}."

    hide image "gui/inventory/icons/big/item_Wine Bottle.png"
    with Dissolve(1)

    pause 1

    show image "gui/inventory/icons/big/item_Blade.png":
        xalign 0.5
        yalign 0.4
    with Dissolve(1)

    "Ao lado, há uma caixa de vidro contendo uma pedra roxa
    esculpida no vago formato da cabeça de um machado de dois lados."

    "Goteja um líquido oleoso vermelho-escuro pela caixa. A gosma se acumulou no
    fundo do recipiente, exalando um fedor desagradável de sangue."

    "A caixa está trancada por um cadeado velho."

    hide image "gui/inventory/icons/big/item_Blade.png"
    with Dissolve(1)

    "Você conseguiu o que veio buscar aqui. Você segue o caminho
    de volta para cima."

    scene bg oldquarters
    with Dissolve(1.0)
    #Asterion and PC have a nice moment.
    #PC asks about Master Jean-Marie.
    #They talk about France, how the PC got the Deed.
    #Asterion asks if PC intends on remaining in the Hotel.

    #PC arrives at the Master's Quarters after finding the Wine Bottle in the basement.
    play music "music/seikilos.mp3" fadeout 4.0 fadein 4.0
    "Os tons laranjas do pôr do sol tingem o cômodo por inteiro. Eles transformam
    a poeira suspensa no ar em milhares de diamantes cintilantes."

    "As esculturas do Mestre anterior olham para você com os olhos arregalados e chamando
    para que vá adiante nos aposentos. O cheiro de poeira velha parece tão pequeno em comparação
    com quão docemente o quarto o recebe."

    "Se um lugar pudesse de alguma forma estar vivo e de alguma forma nu, seria este.
    O próprio Hotel abraça você, a intimidade dele sendo exposta."

    "Nada se move e Astério não está em lugar algum. O silêncio reina, exceto por um
    leve murmúrio de vida. Você deixa a garrafa de vinho em cima da mesa da sala de estar."

    "Você mergulha fundo em seus aposentos e o murmúrio fica mais alto e mais agudo.
    É como uma respiração, irregular e dolorida. A poeira visível sob a luz do
    sol estremece."

    "O som está vindo do escritório."

    "Astério está de pé em frente à mesa, de costas para você, soluçando."
    show Asterion:
        yalign 1.4 xalign 0.5
        pause 2.0
        ease 0.1 yalign 1.37
        ease 0.1 yalign 1.4
        pause 3.0
        ease 0.1 yalign 1.37
        ease 0.1 yalign 1.4
        ease 0.1 yalign 1.37
        ease 0.1 yalign 1.4
        repeat
    with Dissolve(.5)


    if chapter3_affection >= 2:
        $ global_affection += 0.5

    else:
        $ global_affection += 0

    if global_affection >= 1:
        "Seus passos não são suficientes para torná-lo ciente de sua presença. O
        minotauro soluça de novo e de novo, cada um vindo das partes mais profundas de seu ser."

        "Eles começam mansos, pouco mais que bufos. Mas ele coloca as mãos na mesa
        e se inclina para frente. Suas vértebras projetam-se nitidamente de sua pele terrivelmente fina,
        tornando-se mais óbvias pela maneira como ele se curva."

        "Ele cospe um soluço do fundo de seus pulmões. A represa estoura, ele quebra
        em onda após onda de grunhidos e gritos ligeiramente abafados."

        "Ele pressiona o rosto contra a mesa e a agarra, deixando suas marcas na
        madeira imaculada até que cai no chão, enrolado como uma criança."

        "Então, ele percebe sua presença e olha para você com o olho encharcado de lágrimas, mas ignora sua
        presença. Mestre ou não, você é muito pequeno."

        "Ele se enrola ainda mais em si mesmo, a boca coberta pelas mãos enquanto ele
        solta outro grito abafado. A voz do minotauro quebra no meio e ele fica em
        silêncio, mesmo que sua boca ainda esteja trancada em agonia."

        "Mas Astério olha para você, ciente de sua presença, e não faz nenhum esforço para se
        esconder ou encolher. Na verdade, ele tenta falar, mas você não consegue entender suas
        palavras arrastadas, apenas que a voz possui um tom de boas-vindas."

        menu:
            "Confortá-lo.":
                $ global_affection += 0.5
                "Você cruza a lacuna que separa vocês dois em um passo de cada vez.
                O olho de Astério não se desvia de você."

                "Você se senta ao lado dele, de costas para a mesa, e apenas então o olhar dele cai
                para o chão em mais soluços."

                "Você coloca um braço sobre o ombro dele e o puxa para você."

                "O minotauro dobra a intensidade do choro, agora abafado por sua camisa.
                Os dedos dele cavam em você -- eles machucariam se ele não estivesse tão emaciado."

                "Você acaricia atrás da cabeça dele e deixa o minotauro continuar em seu próprio
                ritmo. À medida que o sol se põe mais, escurecendo o quarto, seu choro fica mais
                silencioso e mais discreto também."

                show Asterion:
                    ease 2.0 yalign 1.5 xalign 0.55

                "Quando tudo está escuro, exceto pelas estrelas brilhando além da janela,
                as mãos de Astério relaxam e ele se apoia completamente em seu peito."

                "Ele quase parece estar dormindo, mas você percebe que ele está olhando para você."

                "Astério está apaziguado, mas você dá a ele mais alguns minutos para ter
                certeza. Os dedos dele cavam em você uma última vez enquanto ele suspira. Você
                dá um tapinha em suas costas e o ajuda a se levantar."

                show Asterion:
                    ease 2.0 yalign 1.3 xalign 0.5
                    ease 2.0 yalign 1.0

                "Ele não diz nada sobre o que acabou de acontecer, mas aceita sua
                mão. E quando você sai do escritório, ele permanece perto de você."

                "De volta à sala de estar, você guia Astério até o sofá. Ele se senta
                sem questionar, mas o acompanha com o olhar enquanto você abre a
                garrafa de vinho e a traz para ele."

                you "Estava exatamente onde você disse que estaria."

                "Astério acaricia a garrafa."
                jump chapter3_5

            #"Talk with him.":

    else:
        "A orelha dele sacode em resposta aos seus passos. A cabeça dele contorce para o lado,
        mal captando uma visão de você."

        "Astério segura a respiração, mas suas costas ainda convulsionam -- uma, duas, três
        vezes. Ele fecha as mãos em garras e as cava no peito,
        mantendo-se firme."

        "Há uma convulsão final à medida que ele se curva para frente, a boca
        trancada em um grito silencioso."

        "Você não consegue ouvir, mas qualquer um poderia sentir, sacudindo você até os ossos,
        a garganta ficando áspera com a vibração de gelar o sangue da dor de um prisioneiro."

        "Acaba tão rápido quanto começou. Como uma papoula despida em uma única
        brisa vermelha, suas pétalas se perdem para o mundo e seu grito morre."

        show Asterion:
            ease 3.0 yalign 1.0

        "Quando o minotauro se vira, para você, seu olho o perfura como os de uma estátua -- uma
        estátua almaldiçoando o mundo, que assistiu à sua rocha sendo arrancada do abraço da terra, cortada e
        trancada em uma tormenta a qual nunca pediu para estar."

        "Não há uma única lágrima em seu rosto."

        show Asterion:
            ease 3.0 yalign 1.4

        "Seu único olho rodopia em um turbilhão de pensamentos. Ele se curva apenas
        depois de passar seu doce tempo avaliando cada caraterística sua."

        you "Você está se sentindo bem?"

        asterion "Sim. A seu serviço, Mestre. Perdoe minha fraqueza."

        you "Tem certeza que está se sentindo bem? Podemos falar sobre isso."

        asterion "O Mestre não deve se preocupar. Eu não posso morrer, está tudo bem."

        "Há apenas um pingo de petulância em sua voz. O minotauro permanece curvado
        a você."

        you "Bem, eu tenho boas notícias. Encontrei o vinho que você queria."
        show Asterion:
            ease 2.0 yalign 1.0

label chapter3_5:

    asterion "Obrigado."

    asterion "Saúde."
    $inventory.remove_item('Garrafa de Vinho')

    "Astério renuncia inteiramente a usar uma taça. Ele inclina a cabeça para o lado,
    de forma que o vinho não escorra de sua mandíbula exposta, e bebe direto
    da garrafa."

    "Ele saboreia o primeiro gole e suspira, inclinando a cabeça para trás, e solta
    um gemido enquanto todo o seu corpo relaxa."

    "Em seguida, ele retorna para a garrafa, desta vez, bebendo com convicção."

    "Pelo canto do olho, ele olha para você. Uma pontada de vergonha espalha em seu rosto
    quando uma ou duas gotas de vinho pingam de sua mandíbula exposta."

    "No entanto, não demora muito para que seus braços comecem a tremer. Para sua
    musculatura emaciada, manter a posição por muito tempo é um desafio."

    menu:
        "Segurar a garrafa para ele.":
            "Você se levanta e o ajuda a segurar a garrafa."

            "É como alimentar um bezerro com mamadeira. Astério encara você
            com um olhar mordaz -- ele não recusa sua ajuda, mas a sobrancelha
            franze e o olho fixa em você com petulância."

            "Mal passa um minuto antes que ele pegue a garrafa e volte a segurá-la
            por conta própria."

            "Ele não perde tempo e bebe todo o conteúdo da garrafa sem
            parar, indo tão longe a ponto de balançar a garrafa
            para pegar as últimas gotas."

        "Sugerir que ele use uma taça.":
            "Você levanta uma taça. Astério entende a dica com um sorriso lateral."

            asterion "Mais uma vez, sinto muito, Mestre. Às vezes, a besta leva
            o melhor de mim."

            "Mesmo com a taça, ele não perde tempo e bebe todo o conteúdo da garrafa
            sem parar, indo tão longe a ponto de balançar a garrafa
            para pegar as últimas gotas."

label chapter3_6:
    show Asterion:
        ease 2.0 yalign 1.5 xalign 0.53
    "Astério se encosta no sofá, um meio sorriso pintado em seu rosto."

    asterion "Muito obrigado pelo vinho, Mestre. Eu já me sinto bem. Não
    vai demorar muito para começar a fazer efeito."

    you "Não precisa agradecer, não foi nada."

    asterion "É mesmo? Mestre, se não for impertinente de minha parte, você responderia
    a algumas perguntas?"

    you "Claro, não vejo como isso poderia ser um problema."

    asterion "Desejo saber sobre a guerra. Como ela terminou?"

    you "Guerra? Qual guerra?"

    asterion "A Segunda Guerra Mundial. O conflito entre os Aliados e o Eixo.
    A França foi ocupada. Como isto acabou? A França ainda existe?"

    you "Sim, existe, a França está indo bem, os Aliados venceram a Guerra. Muita coisa
    aconteceu desde então."

    "Você rapidamente conta para ele sobre a história da França depois da Segunda Guerra Mundial, especialmente
    as consequências da guerra."

    asterion "Ah, estou tão aliviado em ouvir isto. Passei todos esses anos trancado
    pensando no que aconteceu. O Mestre Jean-Marie falou tantas vezes sobre a
    França."

    asterion "Paris isso, Paris aquilo, mas também sobre a zona rural. Os campos
    de lavanda, as fragrâncias, os vinhedos. Todos os tipos de vinho. O Mestre
    Jean-Marie nunca poderia comer uma refeição sem uma taça."

    asterion "Ele cresceu em uma aldeia... Próxima a Bordéus, sim. Ele sempre disse
    que o vinho de sua aldeia era o melhor, ponto final."

    asterion "O Mestre Jean-Marie também lutou na Grande Guerra. Ele encontrou o caminho
    para o Hotel como um hóspede, um jovem traumatizado pela guerra recém-saído do campo de
    batalha."

    asterion "Ele herdou a escritura do Mestre anterior e seu comando sobre o Hotel
    foi um espetáculo para ser visto. Ele era muito gentil, tinha uma preferência por
    trazer vítimas da guerra."

    asterion "Não foi fácil cuidar de tantos amputados e homens em estado de choque,
    mas valeu a pena."

    asterion "Ele amava aqui, mas suponho que ele amava mais a França. Não
    consegui dissuadi-lo de voltar para casa para libertar seu país."

    asterion "Ele morreu em 1944. Eu senti no momento em que aconteceu. Senti a bala
    atravessando minha cabeça no meio da noite."

    asterion "Uma semana depois, o próximo Mestre chegou. Jean-Marie deixou um testamento
    entregando a escritura do Hotel a seu irmão, Mestre Clément."

    asterion "Clément não foi ruim no começo. Ele era bastante ansioso para agradar, para
    ser útil aos hóspedes. Mas havia algo nele..."

    asterion "Uma ganância, suponho. Ser meramente querido não era o suficiente. Ele
    e o Mestre Jean-Marie diferiam bastante."

    asterion "Jean-Marie tinha um ponto de vista, trazer conforto àqueles
    afetados pela guerra. Clément, por outro lado, não gostava de ser querido, mas adorado."

    asterion "Ele estava de olho em uma hóspede, uma mulher que dominava a mente dele como se segurasse na palma
    da mão."

    asterion "Posso apenas acreditar que correu mal. E então ele... bem, você viu o que
    ele fez comigo. Os hóspedes se foram e o Hotel foi largado para apodrecer."

    asterion "..."

    asterion "Eu tive um vislumbre do início da loucura em seus olhos. Eu não sou tolo.
    Estava claro que ele não era um homem são, mas eu esperava que ele fosse inofensivo."

    menu:
        "\"Acredito que eu tenha conhecido esse Clément de quem você fala.\"":
            you "Acredito que eu tenha conhecido esse Clément de quem você fala."
            you "Ele me deu a escritura do Hotel. Falou um pouco sobre si mesmo, disse
            que desperdiçou sua única chance de fazer algo bom."
            you "Ele está senil agora. Mal consegue falar direito. Estava procurando alguém
            para cuidar do lugar porque nenhum de seus filhos faria isso."
            you "Quando eu verifiquei a escritura, parecia um monte de rabiscos sem sentido, também.
            Eu só pude acreditar que ele não estava pensando direito e me deu um
            guardanapo usado."
            you "Ele disse que tinha feito coisas ruins durante a vida, mas eu nunca imaginei que
            fosse tão ruim como o que vi aqui."

            "A sobrancelha de Astério está franzida e seu olho vagueia. Ele brinca com os
            polegares enquanto você fala."

            asterion "Ele ainda está vivo, então."
            "Ele fecha o olho, franzindo o rosto em raiva."

        "Não falar nada.":
            "Você tem suas suspeitas, mas decide segurar sua língua."

label chapter3_7:
    "Astério olha para o teto. Sua voz está relaxada agora, quase calmante, mas
    carrega um toque de sobriedade."

    asterion "Mestre, se mais uma vez você aceitaria, posso fazer uma pergunta?
    Esta, entretanto, pode não ser condizente com a minha posição de Zelador."

    "Você o dá permissão."

    asterion "O Labirinto foi criado para me torturar, como punição pelo meu crime.
    Mas, com o passar dos anos, os Mestres humanos escolheram impor uma vontade diferente
    a este domínio."

    asterion "Começou com um jovem que teve pena de mim e, ao longo das gerações,
    tornou-se um refúgio para os perdidos. Cada Mestre teve um ponto de vista."

    asterion "Tivemos um bom percurso, alguns bons séculos desde que começamos.
    Até que, como você viu, Clément apareceu."

    asterion "Desejo saber suas intenções. Isto é terrivelmente inadequado para
    mim, como prisioneiro. Você é meu carcereiro, e obedecerei a qualquer que seja
    sua vontade."

    asterion "Ainda assim, desejo que minha pergunta impertinente seja respondida, se
    não for pedir muito. É de sua vontade continuar com a missão do Hotel?
    Oferecer santuário para aqueles perdidos e sem ter para onde ir."

    asterion "Devo avisar, antes que responda, que eu estou acostumado com o sofrimento.
    Já passei por coisas muito piores do que você viu hoje."

    asterion "Se sua vontade é me torturar, como Mestre Clément fez, então você
    não precisa fingir."

    asterion "No entanto, você aceitou meu juramento e me colocou a seu serviço, e agora
    você me tratou com gentileza. Eu acreditaria, então, que você não é como
    ele."

    asterion "Então, me diga, o seu desejo é manter a missão do Hotel de fornecer
    refúgio aos necessitados? Seja honesto, se quiser. Minha servidão a você
    permanece independentemente de sua escolha, já que eu não tenho nenhuma."

    menu:
        "Deseja cumprir a missão do Hotel?"

        "Desejo ser um bom Mestre para o Hotel e para você.":
            you "Eu não sabia no que estava me metendo quando aceitei a escritura do Clément.
            Muita coisa aconteceu em um único dia e eu não poderia imaginar nada disso a partir
            das divagações dele."
            you "Mas... sim. Eu tenho a intenção de cumprir a missão do Hotel agora. Eu quero ser um
            bom Mestre, para o Hotel e para você."
            you "Eu não estou tentando enganar você. Pelo que você me disse, eu não teria
            motivo para isso."
            you "Talvez seja difícil para você acreditar em mim agora, mas eu falo sério."

        "Eu quero o melhor para o Hotel. Mas eu não posso te libertar?":
            you "Eu quero fazer a coisa certa, Astério. Pode ser difícil para você
            enxergar isso agora, mas eu estou te falando a verdade."
            you "Eu gostaria de fazer o que for melhor para o Hotel e para você, por isso
            tenho que perguntar... Não posso libertar você? Sou seu Mestre,
            afinal."
            you "Não é correto manter ninguém como escravo. Se eu puder, eu quero te
            libertar."
            "Astério olha para o lado, roendo as unhas. Suas palavras
            não tiveram um efeito muito calmante sobre ele."
            asterion "É muita gentileza sua, Mestre, mas não pode ser feito. Minha
            sentença é para a eternidade e eu não posso escapar dela."
            asterion "Houve muitos Mestres que disseram palavras muito parecidas
            com as suas. Eles têm boas intenções, mas não pode ser
            feito. Eu não posso escapar da minha servidão."
            "O minotauro olha para você, roendo as ulhas. Seu olho mexe de um lado para o outro."
            you "Muito bem. Nesse caso, irei cumprir a missão do Hotel.
            Quero ser um bom Mestre, para o Hotel e para você."

label chapter3_8:
    if global_affection >= 1.5:
        "Astério não responde a princípio. Apenas sua respiração profunda corta
        o silêncio da sala."
        asterion "Faz tanto tempo."
        asterion "Eu não sei por quantos anos estive trancado.
        Devo admitir, o simples pensamento de perguntar me dá arrepios."
        asterion "Mestre, você consegue... imaginar? Por séculos eu venho
        cuidando deste hotel. Foi minha benção, o que me salvou da tortura
        e me deu propósito."
        asterion "Foi um trabalho árduo e nem todos os Mestres foram gentis
        ao longo dos séculos. Mas foi maravilhoso mesmo assim, eu
        aproveitei cada momento."
        asterion "E então... Mestre Jean-Marie morreu. Eu poderia ter feito mais
        para tentar impedi-lo. Eu deveria."
        asterion "Então ele veio, Clément. Estou acostumado com a dor, mas
        também tinha me acostumado a ter pessoas, uma missão, um propósito. Ser
        trancado e abandonado não causou metade da dor causada por ter meus hóspedes expulsos."
        asterion "Hoje você me libertou, me colocou a seu serviço e agora me
        diz que deseja ser um bom Mestre. Para o Hotel e para
        mim."
        asterion "Permita-me falar francamente. Eu tenho medo de você.
        Terrivelmente. Você é meu carcereiro. Ao longo dos séculos fui ficando confortável
        em prezar meus mestres, mas depois de Clément todo o receio voltou."
        asterion "Eu tenho tanto medo do que você pode fazer comigo e com o Hotel.
        Não há escolha a não ser obedecer a todos os seus comandos."
        asterion "Eu sinto muito por falar assim. É profundamente inadequado
        para o Zelador se dirigir ao Mestre desta forma."
        asterion "Suponho que, mesmo que eu tenha medo de você, perdi meu medo
        da dor e de ultrapassar os limites."
        asterion "Tudo isso dito... Apesar do meu medo, eu me encontro...
        querendo acreditar em você."

        show Asterion:
            ease 2.0 yalign 1.0 xalign 0.5

        "Astério se levanta do sofá e vai até você. Ele está claramente
        tonto, tropeçando enquanto se aproxima."
        "O minotauro se ajoelha diante de você."

        asterion "Desejo muito que suas palavras sejam verdadeiras."
        asterion "Não me é concedida a escolha sobre se devo obedecê-lo
        ou não. Eu sou um prisioneiro. Mas se de fato suas palavras são verdadeiras, se
        seu coração está realmente decidido a ser um bom Mestre..."
        asterion "Então eu o seguirei. Não por dever, mas por
        querer -- e se me fosse fornecida a verdadeira liberdade, eu permaneceria
        ao seu lado."
        asterion "Jurei servi-lo, e agora juro segui-lo --
        enquanto sua palavra for verdadeira."
        "Ele olha para você. A sala está escura, iluminada apenas pela luz da lua
        vindo através da janela, mas você consegue ver um brilho no olho do
        minotauro."

        menu:
            "Abraçar Astério.":
                show Asterion:
                    ease 1.0 yalign 1.05 zoom 1.05
                "Você o puxa de sua posição ajoelhada para um abraço.
                Ele é leve, pouco mais pesado que uma criança."
                "Em seus braços, ele fica rígido e frio, mas assim que suas mãos
                acariciam suas costas, ele retribui o gesto e descansa o focinho em
                seu ombro."
                "Ele funga uma, duas vezes e pressiona o rosto em seu pescoço."
                asterion "Obrigado, Mestre."
                "Ele respira profundamente, como se estivesse aprendendo seu cheiro."

    else:
        "O minotauro o encara de cima a baixo. Seu olho é afiado, pisca
        rapidamente como os de um gato, sem desfocar de você."
        "É como ser dissecado em busca de algo."
        show Asterion:
            ease 0.8 yalign 1.0 xalign 0.5
            ease 0.5 yalign 1.05 zoom 1.05
            ease 2.0 yalign 1.7

        "De repente, ele se levanta, rápido demais para se sentir confortável, e caminha até você.
        O minotauro se ajoelha."
        asterion "Muito bem. Obrigado, Mestre. Será uma honra
        servir."
        asterion "Não tenho outra escolha, naturalmente.
        Mas, se lhe traz satisfação, saiba que obedeço de bom grado àquele que tem em mente
        os melhores interesses para o Hotel."
        asterion "Isso me traz um propósito, e é a coisa certa a se fazer."
        asterion "Eu sou muito grato."


##############################################################################
#                      CHAPTER 4: REPAIRING THE HOTEL
##############################################################################
label chapter4:
    scene bg black
    with Dissolve(2)

    #Asterion falls asleep shortly after a simple meal.
    #Scene begins on the following morning.
    #Player wakes up. Asterion is already up and going. He prepared a simple meal
    #and he's wearing old-timey clothes. PC has the chance to make him wear
    #modern clothes.
    #
    "A noite cai rapidamente."

    "O Hotel não possui eletricidade, mas você consegue substituir por velas."

    "Sua sombra e a de Astério deslizam nas paredes, tremulando juntamente com as
    chamas oscilantes. Os aposentos do Mestre estão preenchidos com o som aveludado
    da vida -- respiração, passos, móveis rangendo diante de vocês."

    "Do lado de fora, um transeunte veria este hotel em ruínas com uma única janela à luz
    de velas. Se por acaso tentasse explorá-lo, encontraria apenas corredores intermináveis
    de ladrilhos de mármore preto e branco ecoando com o farfalhar de suas roupas."

    "Ele poderia buscar o conforto deste quarto iluminado por velas, mas nunca iria encontrá-lo,
    trancado como está, atrás de uma parede sem portas."

    "O silêncio volta a cair sobre vocês dois.
    Na maioria das vezes, Astério está voltado para você, seguindo-o com seu olhar."

    "Apenas quando você percebe quão faminto está, ele invoca um humilde banquete
    para você -- frutas, queijo, água e até mesmo uma garrafa de vinho comum."

    "Ele vira as costas para você para organizar a mesa. Ele tropeça um pouco e algumas
    maçãs rolam e caem no chão. Você o pega lhe dando um olhar de
    soslaio."

    "As narinas dele dilatam sob a respiração nervosa."
    if global_affection >= 1.5:
        "Astério estremece um pouco. Suas costas se alargam quando ele inspira, e então seus ombros
        se inclinam para frente com a expiração. Ele olha de volta para você, como se estivesse tentando
        dizer algo, depois de alguns segundos ele volta a organizar a mesa."

        "A cauda balança atrás dele, talvez até mesmo com um pouco de alegria."

        "Quando o jantar está pronto, ele o apresenta a você com um meio sorriso nos lábios."

    else:
        "Ele pega as maçãs e dá as costas para você, as mãos tremendo."

    "Seu jantar à luz de velas é simples e sem intercorrências. Qualquer oferta para que Astério
    coma ao seu lado é recusada com um balançar de cabeça. É um movimento longo e deliberado --
    sua única orelha chicoteia para frente e para trás ao lado de sua cabeça."

    "Você pergunta para ele se há alguma maneira de restaurar a eletricidade do hotel."

    asterion "Há uma maneira, sim. Devemos acender a lareira do hotel e, para isto, devemos usar um
    objeto especial."

    asterion "É um conjunto de espelhos de bronze que focalizam a luz do sol. Ele gera
    uma chama pura, trará todo o Hotel de volta à vida."

    "Pouco tempo depois, sem mais nada para fazer durante a noite, vocês dois encontram descanso
    em seus respectivos quartos."

    pause 2.5

#Wake up.
# Clothes
#Out
    $chapter = "Hades"
    call screen ChapterTransition("Hades", "Viagem", 'Hades')
    pause 0.5
    $save_name=output_save_name("Hades")

    play music "music/ariadne.ogg" fadeout 3.0 fadein 3.0
    pause 5.0
    "{i}O minotauro sonha."

    "{i}Antes de Atenas e Esparta, havia Creta, onde Zeus nasceu e foi criado.
    Cabras selvagens deixavam suas marcas de fenda nos declives, esculpidos do magma resfriado
    da era dos Titãs. Seu solo, rico e duro, erguia a promessa de prosperidade."

    "{i}Creta foi um berço -- seguro e fértil para a humanidade primitiva, como foi
    para Zeus, primeiro dos Olímpios. Seu filho, Minos, o Primeiro, até lá seguiu seu caminho
    e tornou-se o fundador e rei. Quando a morte veio para ele, Minos foi nomeado Juiz dos Mortos."

    "{i}Sua linhagem gerou muitos reis para Creta, o próspero berço do homem."

    "{i}Havia um outro que carregava o nome de Minos. Um homem que fez um pacto com
    Poseidon, deus dos mares. Das águas espumosas, o Olímpio enviou um touro branco
    para sinalizar sua preferência e, em troca, o homem prometeu sacrificá-lo."

    "{i}Mas Minos tomou para si aquilo que era destinado aos deuses. Por sua
    arrogância, Poseidon amaldiçoou sua família -- sua esposa, Pasífae, foi atingida com luxúria
    pela besta e ordenou que o lendário artesão, Dédalo, construísse uma novilha oca."

    "{i}Pasífae submeteu-se à estocada do touro e engravidou de seu filho. Assim
    nasceu o minotauro."

    "{i}A infâmia de Pasífae sobrevive. Creta caiu em favor de Atenas que, por sua vez,
    foi varrida por Roma, também consumida pelo tempo. Mas a desgraça de
    Pasífae permanece, assim como sobrevive a história do mestiço canibal a quem ela deu à luz."

    "{i}Mas, para o minotauro, ela era mãe. E ela o chamou de Astério, seu filho
    de olhos estrelados. Ele bebia de seu seio, como qualquer menino, e brincava com seus
    irmãos, mesmo que seu rosto denunciasse o pecado que o gerou."

    "{i}O minotauro sonha com o vasto campo florido de asfódelos brancos onde ele
    costumava ir com sua irmã, Ariadne, segurando seus dedos. Onde eles se sentariam perto de uma árvore
    e ele tiraria uma soneca com a cabeça descansando sobre as coxas dela."

    "{i}Astério sonha com Creta. O palácio de Cnossos, onde ele foi criado,
    e com seu destino inescapável: o labirinto construído por Dédalo, onde ele conheceu seu fim."

    "{i}Antes que os primeiros fios de cabelo de uma barba tivessem brotado se ele fosse
    completamente humano, ele foi carregado para um labirinto de pedra nas profundezas de um dos vales
    de Creta. A saída foi bloqueada e ele foi largado apenas com um machado que mal conseguia levantar."

    "{i}Uma década se passou antes que um visitante chegasse."

    "{i}Astério não conseguia mais pensar. A linguagem havia escapado de sua mente,
    de tão solitário que ele havia se tornado."

    "{i}Seu visitante, Teseu, cruzou o mar pela cabeça do minotauro. O
    herói esperava por uma batalha, mas encontrou apenas uma besta digna de misericórdia."

    "{i}Astério não rejeitou a pena do herói."

    "{i}Por fim, ele sonha com o Campo de Asfódelos. É uma benção. É o fim de
    seu sofrimento. Mas ele desperta para o labirinto novamente."

    $Asterion.change("stage","thin")
    if persistent.sfwMode:
        $Asterion.change("underwear", "loincloth")

    scene bg asterionbed
    show Asterion:
        yalign 2.0 zoom 1.0 xalign 0.6
    show blackback:
        alpha 0.7
    with Dissolve(2)

    "Ele salta de sonho para reflexão. Mestres Jean-Marie e Clément. A câmara fria.
    O novo Mestre. Liberdade da escuridão. Comida -- e vinho."

    "Astério agarra os lençóis empoeirados. Já se passaram décadas desde que ele dormiu em uma cama.
    ele não sente escaras em suas costas. Em vez do fedor da câmara fria, há apenas o cheiro ligeiramente
    mofado de seu antigo quarto."

    "Seus lábios -- metade touro, metade esqueleto -- ameaçam se curvar em um sorriso. Mas a dúvida
    o corrói, agita seu estômago."

    show Asterion:
        ease 2.0 yalign 1.0 xalign 0.5

    "O minotauro se levanta sem a menor cerimônia e abre o armário. Não importa o que
    venha a seguir, ele deve {i}trabalhar, trabalhar{/i} e então {i}trabalhar{/i} um pouco mais.
    Enquanto verifica suas roupas, ele murmura um antigo poema de memória."
    hide Asterion
    with Dissolve (1)

    asterion "Viestes. E fizestes bem em vir."

    asterion "Por ti ansiei e trouxestes fogo"

    asterion "ao meu coração, que por ti arde alto."
    $Asterion.change("clothes","40s")

    show Asterion behind blackback:
        yalign 1.0 xalign 0.5
    with Dissolve(1)

    "Essas roupas velhas não servem nele. O espelho deixa claro o quanto ele é
    uma desgraça. O buraco escancarado e sem carne em seu crânio faz seu icor borbulhar
    e ameaçar estourar de sua boca."

    "Porém... ele é uma desgraça menor do que era no dia anterior. E pelos últimos
    oitenta anos. Há alguma benção nisso."

    show Asterion:
        ease 3.0 xalign 0.3

    "Ele força um meio sorriso e sai."

    play sound "sfx/flute.ogg"

    "Assim que sai, entretanto, sua orelha sacode. Ele ouve uma melodia
    distante -- animada, pode-se dizer até alegre. É fraca, mas inconfundível.
    O sorriso desaparece de seu rosto."

    stop music fadeout 5.0
    scene bg black
    with Dissolve(3)


    $chapter = "Capítulo 3"

    call screen ChapterTransition("Capítulo 3", "O Capataz")
    pause 0.5
    $save_name=output_save_name("Capítulo 3")

    with Dissolve (3)

    play music "music/GreekFolkSong.ogg" fadeout 1.0 fadein 1.0

    scene bg oldquarters
    with Dissolve (3)

    "Diamantes de poeira flutuam pela sala, suspensos no tempo. A impiedosa luz do dia
    atravessa as janelas."

    "Sua boca está seca, seus olhos avermelhados. O quarto está úmido e ficando mais quente sob
    o sol do deserto."

    "Do lado de fora, você ouve o barulho de cascos -- muito fraco, porém perceptível,
    como se um certo minotauro estivesse tentando e falhando em ficar quieto."

    "Seu celular, agora quase sem bateria, mostra que são 6 da manhã. Você se levanta
    e sai para enfrentar o dia."

    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve(1)

    asterion "Bom dia, Mestre. Espero que tenha dormido bem."

    you "Astério, que roupas são essas que você está vestindo?"

    asterion "É o que eu costumava vestir. Elas podem estar um pouco grandes agora,
    mas isto não vai durar. Estarei de volta à minha antiga forma antes que perceba."

    asterion "Achei que foi inapropriado o suficiente passar um dia inteiro nu
    em sua presença. Então, esta manhã eu decidi me vestir."

    asterion "Você gostou?"

    you "..."
    menu:
        "Você gosta das roupas de Astério?"
        "Claro, você está ótimo.":
            $Asterion.setFavorite('40s')
            you "Com certeza, você está ótimo. Bem estiloso."
            asterion "Ah, você é muito gentil."

        "Que tal alguma coisa mais moderna?":
            $Asterion.setFavorite('vneck')
            you "Eu acho que você parece, é... Bem, claro. Mas essas roupas são um pouco
            antigas, que tal vestir algo mais moderno?"
            you "Quer dizer, podemos simplesmente invocar comida e água aqui, certo? Certamente
            posso conseguir algumas roupas para você também."
            asterion "É claro, Mestre. Basta comandar e o Hotel se submeterá à
            sua vontade."

            show blackback:
                alpha 0.0
                ease 0.5 alpha 1
                ease 0.5 alpha 0
            play sound "sfx/hum.ogg"
            "O Hotel pisca ao seu redor enquanto a realidade se reescreve."
            show blackback:
                alpha 0.0
                ease 0.5 alpha 1
                ease 0.5 alpha 0
            "Você imagina uma camisa que poderia se ver vestindo. É uma tarefa simples."
            if player_background == "humanities":
                "Algo clássico e minimalista..."

            if player_background == "tech":
                "Algo consciente de si mesmo e fascinante..."

            if player_background == "math":
                "Algo eterno e poderoso..."

            if player_background == "arts":
                "Algo estiloso e adequado para um minotauro..."

            if player_background == "leader":
                "Algo ousado, corajoso e que exale confiança..."

            if player_background == "speedrunner":
                "Algo {i}minimalista, fascinante, poderoso, estiloso e corajoso...
                Mas, acima de tudo: clássico.{/i}"

            show blackback:
                alpha 0.0
                ease 0.5 alpha 1
                ease 0.5 alpha 0
            pause 1.0
            "Do nada, uma trouxa de roupas aparece nas mãos de Astério. Ele sai por um minuto
            para experimentar."

            hide Asterion
            with Dissolve(1)
            $Asterion.change("clothes","vneck")
            if player_background == "speedrunner":
                asterion "...Isto é o que as pessoas usam hoje em dia?"
                show Asterion
                with Dissolve (1)
                asterion "Pelos deuses... Eu não quero ser rude, Mestre, mas
                isto é terrivelmente..."
                asterion "Me desculpe, eu não deveria questionar seu julgamento. Seu
                desejo é uma ordem... infelizmente."

            else:
                asterion "Então... Isto é o que as pessoas usam hoje em dia? Parece
                estranhamente casual para mim."
                asterion "Mas o desejo do Mestre é uma ordem."
                show Asterion
                with Dissolve (1)
                asterion "...É bastante confortável... Eu gostei. Não é
                tão elegante quanto a anterior, mas... Sim, eu realmente gostei. Obrigado."


label chapter4_1:
    pause 1
    "Pouco tempo depois, Astério invoca um café da manhã simples para você: pão, queijo e
    frutas. É tudo o que ele pode oferecer agora, tendo em vista que a cozinha ainda não possui
    equipamentos funcionando."

    "Você se senta enquanto Astério fica parado, de costas para a parede, olhando para você."

    you "Então, o que temos que fazer hoje? Alguma tarefa?"

    asterion "Há uma, mas não é algo com que o Mestre deva se preocupar.
    O item que mencionei noite passada, aquele que pode acender uma
    chama pura."

    asterion "Se o Mestre assim desejar, posso procurá-lo e então poderemos ser capazes
    de restaurar o Hotel."

    you "Mas eu posso ajudar, não tem problema. Não é como se eu tivesse qualquer outra coisa
    para fazer enquanto você está ocupado."

    asterion "..."

    asterion "Eu obedeço à vontade do Mestre."

    "O silêncio paira sobre vocês. O ar encontra-se pesado enquanto Astério dirige o olhar
    para você -- e para a comida na mesa."

    "Esta refeição de frutas, queijo e pão é simples -- pode-se dizer sem graça e
    entediante. Mas o minotauro olha para ela com um fervor condizente com o quão
    magro ele está."

    "Saliva escorre de sua mandíbula meio exposta. Ele não percebe quando as primeiras
    gotas caem no chão, mas assim que começa a escorrer no pelo de seu queixo, ele dá
    um tapa na própria bochecha para cobrir o ferimento."

    show Asterion:
        ease 2.0 yalign 1.2

    "Seu olho vai à loucura quando ele percebe o que acabou de acontecer. Astério olha para
    você, com medo de sua reação."

    "É uma visão lamentável. Seu olhar transmite uma sensação de pavor -- parece que ele espera
    que você fique irritado com este comportamento espantoso."

    you "Você parece estar com fome, Astério. Não vai comer? Eu não me importo
    em compartilhar uma refeição com você."

    asterion "É... É impróprio para o servo comer com o senhor. O Mestre não precisa
    se preocupar comigo, me alimentarei depois que você terminar."

    you "É assim que os Mestres anteriores tratavam você?"

    asterion "Sim. Esse tem sido nosso costume desde... por muitos séculos,
    digamos assim. Mestre Jean-Marie, em particular, era bastante rígido com isso. Ele
    apreciava ordem e hierarquia."

    asterion "...Na verdade, ele teria ficado chocado se tivesse visto meu comportamento
    ontem. Andando nu por aí, dependendo da assistência do Mestre..."

    asterion "Ele era gentil, mas rígido. E..."

    asterion "...Às vezes, ele punia minha insubordinação com bastante severidade. Afinal,
    de que outra maneira eu poderia saber se o que fiz foi errado? Mesmo assim, ele estava
    entre os Mestres mais gentis."

    you "Isso era mesmo necessário? Ele não poderia simplesmente conversar com você?"

    asterion "...Ele pensava de outra forma."

    asterion "De qualquer forma, ele não hesitou em me tratar bem quando eu superei
    suas expectativas."

    "O minotauro intercala a suspensão entre os cascos e olha para baixo. Seu olho fica mais entediado."

    asterion "...Ele me acariciava, às vezes. Coçava meu queixo e atrás das orelhas.
    Ele conseguia ser carinhoso."

    asterion "Eu aproveitei meu tempo com ele. Aproveitei sim. Ele foi um excelente Mestre para o
    Hotel, que floresceu sob seu domínio. É isto o que importa."


    if global_affection >= 1.5:
        asterion "Eu fico feliz enquanto o Hotel estiver indo bem, cumprindo seu
        propósito de fornecer refúgio a quem precisa. É como eu disse, ter sido
        trancado e largado para trás não doeu tanto quanto ver o lugar abandonado."

        asterion "Se o Mestre me trata bem ou não... Em última instância, não
        importa. Eu fui sentenciado ao sofrimento eterno e meramente existir como
        agora é melhor do que eu jamais poderia esperar."

        asterion "Então... Eu gostava do Mestre Jean-Marie. Ele era um bom homem."

        asterion "...Não é minha função dar palpite sobre as ações do Mestre. O
        Mestre Jean-Marie teria ficado furioso se ouvisse sobre esta conversa."

        asterion "... Suponho que tenho sido terrivelmente tagarela hoje, não é?
        Sinto muito por incomodar o Mestre."

        you "Você não está me incomodando. Eu quero saber mais sobre você e, bem,
        você é uma ótima companhia também."

        you "Eu gostaria que você se sentasse e compartilhasse a refeição comigo, mas já que isso não é
        algo que você está disposto a fazer... Gosto de ouvir você falar."

        asterion "Não é minha função dar palpite sobre suas ações, meu senhor.
        Mas, com sua permissão..."

        "Você acena com a cabeça para o minotauro."

        "Astério não fala mais nada."

        jump chapter4_2

    else:
        jump chapter4_2

label chapter4_2:
    show Asterion:
        ease 1.0 yalign 1.0
    "Quando você termina sua refeição, o minotauro vai à cozinha para
    lavar a louça. Resolvendo comer apenas depois -- ele se senta no chão, de pernas cruzadas,
    e come o que resta da comida invocada para você."

    "Mesmo que a cozinha não seja nada como a cela de pedra fria na qual vocês
    se conheceram, o ar de desânimo cercando Astério é tão contagiante que quase
    parece o mesmo."

    "Você o observa comer a refeição de pão e queijo -- lenta e meticulosamente,
    como se a própria sensação de comer fosse de alguma forma estranha para ele depois de
    inúmeras décadas largado para morrer de fome."

    "Como ele possui apenas metade de um rosto, você consegue ver um corte transversal de cada movimento
    enquanto ele morde, mastiga e engole a refeição escassa, tentando o melhor para encontrar um ângulo
    que o forneça a dignidade de não se expôr ainda mais."

    "Pego como está entre a vergonha de encontrar seus olhos, a impropriedade de se virar
    para evitá-lo e a vergonha de deixar você enxergar dentro da boca dele enquanto come, ele
    luta um pouco antes de se render à última opção."

    "Sem saber como despertá-lo para fora de sua melancolia, você simplesmente se permite
    compartilhar o silêncio, por mais embaraçoso que possa ser."

    "Por vários minutos, o único som que pode ser ouvido é o de sua própria
    respiração, bem como o ocasional respingo de quando o minotauro avalia mal quanto
    espaço ele tem disponível e um pouco de comida mastigada cai pelo lado esquelético
    de sua mandíbula."

    play sound "sfx/flute.ogg"
    stop music fadeout 2.0

    "Porém, pouco tempo após Astério engolir o último bocado de queijo, um som
    repentino tira vocês dois do isolamento compartilhado -- você pode ouvir uma
    flauta tocando do lado de fora dos aposentos, sibilando uma melodia alegre e animada."


    "A orelha de Astério sacode. Ele olha para você, percebe que você também ouviu
    e congela. A palidez rasteja sobre o rosto dele, gotas de suor caem de sua testa enquanto
    saliva vaza de sua boca semidestruída."

    you "O que é isso?"

    show Asterion:
        ease 0.05 xalign 0.501
        pause 0.05
        ease 0.05 xalign 0.499
        pause 0.05
        repeat

    "O minotauro começa a tremer."

    asterion "Por favor, não me mande para o vale. Eu imploro."

    asterion "Me desculpe por não ter mencionado isto antes, eu ia...
    mas estava com tanto medo."

    asterion "O torturador está no vale e tentará me trazer para
    fora. Por favor, não me mande para lá..."

    hide Asterion
    show bg black
    with Dissolve(1)

    "Leva um tempo para acalmar o minotauro, mas eventualmente ele o leva até a
    fonte da canção assustadoramente alegre: todo o caminho descendo a escada em espiral
    até as profundezas do Hotel."

    scene bg staircase2
    with Dissolve (1)

    "Astério segue você de perto -- mesmo que, em teoria, ele devesse ser aquele
    guiando o caminho."

    "A música fica mais alta à medida que você desce. É carregada para cima por uma corrente de ar
    vindo de baixo."

    scene bg valley_exit
    with Dissolve (1)

    "O piso da base é de rocha pura, uma galeria vagamente circular com uma única saída
    conduzindo ao vale."

    "Até agora, o Hotel inteiro, mesmo em ruínas, só lhe passou a impressão de que foi
    construído com amor. Não é o caso desta área em seu ponto mais baixo --
    foi precariamente escavada na rocha e deixada para trás com uma aversão e descuido deliberados."

    "A luz do sol derramando do lado de fora é severa para os seus olhos, acostumados como estão
    com a escuridão da escadaria em espiral. Em contraste, a música possui um toque alegre
    adicionado -- e continua a lançar Astério em um estado de quase pânico."

    asterion "Ele está aqui, o capataz do Labirinto. Ele se chama Argos. Ele irá me machucar
    se eu sair, mas ele não pode ferir o Mestre."

label chapter4_3:
    scene bg valley
    with Dissolve (1)

    "O vale está disposto diante de você, pintado em amplos traços de laranja vívido,
    equilibrados com tons de azul e dourado no céu."

    "É árido, mas há vegetação aqui -- é, na verdade, um cenário relaxante em comparação
    com o deserto completamente sem vida ao redor do Hotel. O vento até possui um toque
    de umidade matinal; não seria nenhuma surpresa encontrar algum orvalho
    persistindo nos arbustos."

    "É bastante peculiar -- o vale parecia desprovido de vida quando você olhou para ele
    a partir do mirante do Hotel, mas de perto é bem diferente."

    "Logo à frente encontram-se duas fileiras de estátuas de mármore, cada uma com
    quatro a cinco metros de altura e uma única estátua de uma mulher apontando a
    espada em sua mão na direção da entrada do Hotel."

    "A música vem da estátua. Você olha para trás, na direção de Astério --
    você mal consegue distinguir a chama azul na escuridão da caverna."

    play sound "sfx/flute.ogg"

    argos "Louvados sejam os Olímpios, os ossos mostraram a verdade!
    Um novo Mestre está de fato diante de nós!"

    play music "music/OneWitness.ogg"

    "Uma mão cinza agarra o ombro da estátua e, em seguida, uma forma serpentina
    emerge e se enrola em volta do pescoço da mulher."

    $ Argos.change ("pelt","True")
    $ Argos.change ("emotion","neutral")
    $ Argos.change ("pose","crossed")
    show Argos:
        xalign 0.5 zoom 0.6 alpha 0 yalign 1.0
        ease 0.4 xalign 0.53 zoom 0.7 alpha 0.5
        ease 0.4 xalign 0.47 zoom 0.8 alpha 1
        ease 0.4 xalign 0.53 zoom 0.9
        ease 0.4 xalign 0.5 zoom 1.0

    with Dissolve (1)

    argos "A espera foi longa, meu bom senhor. Ah, como eu antecipei este
    dia, quando um humano surgiria novamente para cumprir a missão concedida por Atena!"

    show Argos:
        alpha 1.0

    argos "Passei décadas esperando aqui, neste vale tão interessante quanto uma pilha de esterco,
    desde que Mestre Clément deixou este domínio. Todo em minha solidão."

    $ Argos.change ("emotion","smug")

    show Argos:
        ease 0.4 xalign 0.5 zoom 1.0

    argos "É como disse o épico -- \"Servos nunca fazem seu trabalho quando a mão de
    seu senhor não mais está sobre eles, pois Zeus leva metade da bondade de um homem
    embora quando o torna um escravo para si.\""

    argos "Sem um Mestre, o minotauro falhou em seus deveres: o poderoso
    Hotel está em mau estado e as entidades do vale desapareceram completamente.
    Não há trabalho a fazer se não há um Mestre por perto, você entende?"

    argos "Apenas eu permaneci, esperando. Mas isto deve mudar em breve -- Eu
    sinto a terra se mexendo sob as estátuas. Antes que você perceba, os antigos
    parentes dos deuses estarão entre nós mais uma vez."

    $ Argos.change ("emotion","cocky")

    argos "Ora, meu bom Mestre, você conhece o nome de seu seguidor mais fiel?
    O minotauro o informou sobre minha linhagem?"

    pause 1.0

    $ Argos.change ("emotion","smug")

    argos "O Mestre não me ofereceu uma saudação, nem uma palavra de apreciação,
    então posso apenas presumir que o velho touro negligencia seus deveres novamente."

    "Você está prestes a falar quando ele o interrompe e continua com o
    discurso."

    argos "Seu rosto diz tudo. Muito bem, permita-me apresentar-me."

    show Argos:
        zoom 1.0
        ease 0.8 yalign 1.3
        ease 1.0 yalign 1.0

    argos "Eu sou Argos Panoptes, sentinela do bezerro, adorador dos Olímpios.
    Minha linhagem é incomparável: nasci do próprio Labirinto e não há besta
    capaz de escapar do meu rastreamento."

    argos "...Nem qualquer relíquia, por falar nisso."

    "A cobra segura um objeto de metal sob o braço -- um conjunto de espelhos de bronze."

    $ Argos.change ("emotion","cocky")

    argos "Ora, Mestre, meus olhos estão aqui em cima. Seu olhar me faria acreditar que
    meu semblante chamou sua atenção. É verdade, sou um belo espécime, não sou?..."

    argos "Ou talvez você esteja interessado neste belo objeto que eu encontrei."

    argos "É uma relíquia de tempos antigos. Ela concentra a luz do sol em um
    único feixe, gerando uma chama pura, adequada para uma oferenda."

    argos "É o chamado Espelho de Héstia -- a qual é deusa da lareira.
    Mantenha-a apaziguada e sua bênção cuidará deste domínio."

    argos "Eu o encontrei aqui no vale há algum tempo, descartado, mas não destruído. Acredito
    que Mestre Clément o tenha jogado do penhasco antes de partir. Ele
    tinha conhecimento do valor do Espelho, certamente pretendia causar dano."

    argos "Eu sei que este objeto aqui tem toda uma importância lá em cima
    nesse seu Hotel. Veja bem, sem isto ele permanecerá em um estado
    de ruínas -- apenas estes pequenos pratos de bronze podem iluminar sua lareira sagrada."

    argos "Talvez... o Mestre deseje possuir tal coisa?"

    argos "Ora ora, seria um prazer ajudá-lo! Esta é minha função,
    servir ao senhor do domínio!"

    $ Argos.change ("emotion","neutral")

    argos "Terei o maior prazer em considerar oferecê-lo a você, se apenas o Mestre
    realizar um pedido meu muito simples."

    if player_background == "humanities":
        you "Você vai \"considerar\"?"
        argos "Sim, digo, eu o darei, sim... sob uma simples condição."
        jump chapter4_4

    if player_background == "leader":
        you "Você vai \"considerar\"?"
        argos "Sim, digo, eu o darei, sim... sob uma simples condição."
        jump chapter4_4

    else:
        jump chapter4_4


label chapter4_4:

    argos "É trivial, insignificante. Eu meramente desejo ter dois minutos com o
    minotauro, aqui mesmo no vale. Ordene que ele saia e fique por dois
    curtos minutos."

    argos "Não encostarei um dedo nele, prometo a você. Eu meramente desejo me
    familiarizar novamente com o prisioneiro."

    $ Chapter4_Terrorized_Asterion = "False"
    $ArgosContract = "Signed"
    menu:
        "Ordenar a saída de Astério.":
            "Bem... qual é o problema, então?"

            "Se isto resolverá toda a situação, talvez seja uma solução
            pragmática."

            pause 2

            you "Muito bem. Espere aqui enquanto eu busco ele."

            $ Chapter4_Terrorized_Asterion  = "True"
            $ArgosContract = "Terrorized"

            $ Argos.change ("emotion","cocky")
            argos "Maravilhoso!"
            argos "Vejo que você é um homem devoto de linhagem nobre, como os
            heróis de outrora. Devo manter minha palavra, Mestre; você não precisa se preocupar
            comigo encostando um dedo na criatura."

            scene bg valley_exit
            show Asterion:
                yalign 1.4
                ease 0.05 xalign 0.501
                pause 0.05
                ease 0.05 xalign 0.499
                pause 0.05
                repeat
            with Dissolve (1)

            "Você volta para dentro da caverna. Astério está sentado de costas para a
            parede, segurando os joelhos próximos ao peito."

            you "Ei..."

            "Ele está de olho arregalado, olhando para você com o lábio inferior trêmulo. A
            chama azul em sua cavidade ocular ondula como se soprada por um vendaval e a tremedeira
            cai de seus lábios, espalhando pelo corpo inteiro."

            you "Você não precisa se preocupar. Ele prometeu que não encostaria um dedo em você.
            Você só precisa ficar dois minutos lá fora, é só um pouco de conversa."

            "O minotauro não se mexe.{w} Seu olho permanece fixo nos seus,
            arregalado e em pânico."

            you "Você ouviu o que eu disse? Vá, fique dois minutos lá fora."

            show Asterion:
                ease 0.3 yalign 1.5
                ease 1.0 yalign 1.0

            "Astério abaixa a cabeça, solta um gemido de lamentação e, como se puxado por cordas,
            levanta e sai andando até o vale."

            $ Argos.change ("emotion","cocky")
            scene bg valley
            show Argos:
                xalign 0.9 yalign 1.0
            show Asterion:
                xalign 0.1 yalign 1.0
                ease 1.0 xalign 0.3
            with Dissolve (1)

            show Asterion:
                ease 0.05 xalign 0.301
                pause 0.05
                ease 0.05 xalign 0.299
                pause 0.05
                repeat

            "Astério sai como se resistisse a cada passo, às
            vezes tentando -- e falhando -- voltar para você."

            show Argos:
                ease 0.5 xalign 0.8 yalign 1.3
                ease 0.5 yalign 1.0 xalign 0.75

            show Asterion:
                ease 1.0 xalign 0.25

            show Asterion:
                ease 0.05 xalign 0.251
                pause 0.05
                ease 0.05 xalign 0.249
                pause 0.05
                repeat

            "Argos desliza para baixo, vindo da estátua, e se aproxima dele."

            argos "Sabe, sinto-me verdadeiramente honrado por estar em sua presença. Que
            privilégio -- estar a serviço dos próprios deuses, para testemunhar o
            prisioneiro eterno."

            argos "E para servir sob o domínio de um Mestre tão fiel, disposto a fazer o que é
            certo! É exatamente como os deuses ordenaram: o carcereiro entrega o prisioneiro à
            sua condenação."

            argos "Que esta seja minha apresentação formal.{w} Sou Argos Panoptes
            desta era, aqui para cumprir meu dever divino."

            argos "Infelizmente, não iniciarei os rituais hoje, bezerro. Seria terrivelmente
            rude de minha parte tirar sangue diante de nosso senhor."

            $ Argos.change ("pose","straight")

            show Argos behind Asterion:
                ease 0.4 xalign 0.35

            show Asterion:
                pause 0.2
                ease 0.6 xalign 0.15 yalign 1.4
            pause 1
            show Asterion:
                ease 0.05 xalign 0.151
                pause 0.05
                ease 0.05 xalign 0.149
                pause 0.05
                repeat

            "Em um piscar de olhos, Argos salta e se enrola em Astério -- o tempo todo
            mantendo ambas as mãos atrás das costas."

            "O emaciado minotauro se debate contra o aperto da cobra, mas Argos apenas ri.
            Astério levanta o rosto para os céus, gritando, naquele momento ele parece
            completamente bestial -- um touro berrando, o início de espuma escorrendo por sua
            boca e seu olho vermelho de sangue."

            $ Argos.change ("emotion","angry")

            argos "Suponho que uma mordidinha de amor não infringiria minha
            promessa, no entanto."

            show Argos:
                ease 0.5 xalign 0.32 yalign 1.1

            "Argos sibila e revela suas presas, arranhando o pescoço de Astério.
            O minotauro tenta lutar mas, em resposta, a cobra o aperta de novo
            e de novo, deixando sua vítima sem fôlego e tonta."

            show Asterion:
                ease 0.5 xalign 0.15

            "Astério para de lutar -- difícil dizer se por desistência ou por estar
            perdendo a consciência. Argos mantém as presas no pescoço do minotauro, aplicando
            tensão na pele e sentindo quão frágil é sua vítima."

            "Algum ar retorna para Astério -- e ele soluça, sem fôlego, soluços guturais,
            mais parecidos com um acesso de tosse de gelar o sangue."

            "Mas Argos não finaliza a mordida."

            $ Argos.change ("emotion","neutral")

            argos "Um humano pode viver mais de cem anos. Veja como nosso senhor
            é jovem, apenas pense quão longo será seu comando. Sessenta,
            setenta, oitenta anos a mais de diversão."

            $ Argos.change ("emotion","smug")

            argos "Quando eu tiver minha primeira noite com você aqui fora, será de sua
            vontade jamais ter deixado aquela cela, prisioneiro."

            $ Argos.change ("emotion","cocky")
            $ Argos.change ("pose","crossed")

            show Argos:
                ease 1.0 xalign 0.5 yalign 1.0
            show Asterion:
                ease 0.5 yalign 2.7

            "E então ele solta Astério, lentamente enfraquecendo o aperto."

            argos "Mantive minha promessa, touro. Nem um dedo encostado em você. Eu poderia
            ter injetado meu veneno com a mordida mais perfeita, também -- nenhuma gota de
            sangue teria saído."

            argos "Mas eu sou um cavalheiro, veja bem, seria vergonhoso para o carcereiro
            testemunhar seu sangue preto nojento, tanto quanto seria repugnante para mim
            prová-lo."

            argos "Você deve ir agora, besta. E leve o Espelho para seu Mestre
            {w}-- isto é uma ordem."

            show Asterion:
                ease 1.0 xalign 0.0 yalign 2.4 alpha 0.5
                ease 1.0 xalign -0.1 yalign 2.3 alpha 0.0

            "Astério rasteja de quatro para dentro, tropeçando enquanto segura o Espelho."

            hide Asterion

            "Ele está chorando contra a parede -- mas Argos chama você para
            conversar novamente."

            pause 2

            $ Argos.change ("emotion","smug")
            argos "Agora vejo do que o Mestre é feito. Você possui olhos de obsidiana,
            ferozes e ásperos, como um lorde bem deveria ter!"
            argos "Os próprios Olímpios devem ter enviado você aqui, escolhido a dedo
            entre os humanos mais capazes."
            argos "Sinto-me verdadeiramente realizado, que privilégio é testemunhar a sua
            glória! Certamente realizarei minha missão ao seu lado."
            jump chapter4_5


        "Recusar oferta.":
            you "Receio não poder fazer isso."

            $ Argos.change ("emotion","smug")
            argos "Ora, por que seria isso? O minotauro caluniou meu bom nome?"

            argos "Que baixo da parte dele. Dizem que o fígado de um covarde é pálido -- talvez um dia eu
            confirme isto com meus próprios olhos."

            $ Argos.change ("emotion","cocky")

            argos "Independentemente disso, gostaria que o Mestre soubesse que sou meramente um
            seguidor devoto dos velhos hábitos. Não há razão para duvidar de meu caráter --
            isto é, pressupondo que você preze muito pela palavra dos Doze Olímpios."
            jump chapter4_5

label chapter4_5:
    $ Argos.change ("emotion","neutral")

    argos "Meu dever é simples. Eu ajudo o Mestre a cumprir sua tarefa dada pelos
    deuses de decretar a punição do minotauro. Ele foi, afinal, sentenciado à
    danação eterna."

    argos "Os senhores da antiguidade eram verdadeiros heróis. Eles possuíam a mão de ferro
    para fazer o que os deuses exigiam! Mas então veio a linhagem posterior de degenerados de
    fraca vontade com ideias sacrílegas."

    argos "Fornecendo piedade aos condenados... Que tolice infantil."

    $ Argos.change ("emotion","cocky")

    argos "Aquele Mestre Clément, eu diria que ele foi um retorno bem-vindo às origens.
    Mas tão pouco criativo! Meramente trancar o prisioneiro em uma sala dificilmente
    se compara ao poder dos tempos antigos."

    $ Argos.change ("pose","straight")

    argos "Os humanos tornaram-se terrivelmente compassivos ao longo dos milênios -- é uma visão tão lamentável.
    Me dói pensar que a herança de Teseu, Héracles e Odisseu
    está desperdiçada."

    argos "Os heróis da antiguidade não hesitaram. A mira de Héracles foi certeira. Usando uma
    flecha coberta com o sangue da hidra, ele cortou o crânio de Gerião, o monstro
    do deserto vermelho."

    argos "Odisseu de língua prateada, herói de Ítaca, cegou o ciclope
    Polifemo com uma estaca e banhou seu palácio em sangue."

    argos "E por último, mas não menos importante, Teseu decapitou o minotauro com
    o lábris sagrado de Creta."

    argos "De novo e de novo os heróis de Atena prevaleceram sobre os descedentes bestiais
    de Poseidon, bom Mestre. O triunfo da civilização, da humanidade,
    sobre o caos."

    argos "Até hoje nós honramos o triunfo de Atena e da humanidade aqui neste
    glorioso domínio. O minotauro foi sentenciado à danação, entende,
    torturá-lo é um ato de adoração divina."

    if Chapter4_Terrorized_Asterion == "True":
        argos "Percebo, então, qual é a linhagem do Mestre -- heroísmo, a glória da
        humanidade! Não tenho dúvidas, deve ter sido a própria Atena quem o enviou aqui."

        argos "Com isto, Mestre, permita-me oferecer um conselho.
        Este domínio é regido por leis e contratos."

        argos "Minha promessa para você, lembra dela? Se o Mestre enviasse o prisioneiro para
        fora por dois minutos, eu \"teria o maior prazer em considerar oferecer o Espelho para você\". Há
        uma pegadinha, está vendo? Eu \"consideraria\". Não tenho a obrigação de
        lhe dar o espelho, de fato."

        argos "Mesmo assim, eu o entreguei. É um prazer ser útil a um Mestre
        como você! Se ainda manifestar o poder dos antigos heróis no futuro,
        então terei o maior prazer em segui-lo e servi-lo muito além do meu dever."

        argos "Por falar nisto... Tenho o que pode ser uma oferta atraente, Mestre.
        Tenho certeza que será de seu agrado, visto que compreende o
        propósito do Labirinto."

        argos "Eu tenho vasculhado este vale por muitos anos, bom Mestre, e estou
        cansado de viver nesta terra estéril."

        argos "Se o Mestre me legar um fragmento de seu poder... Meu senhor pode
        invocar comida, água e abrigo sempre que desejar, eu gostaria de ter
        a mesma capacidade."

        argos "Se me legar tal poder e permissão para entrar no Hotel, prometo
        ser útil para você. Como eu disse, sou um especialista quando
        se trata deste vale."

        argos "Posso obter todos os tipos de artefatos poderosos -- muito mais
        que aquela coisa velha que entreguei ao touro."

        argos "Garanto que será excepcionalmente lucrativo para você. O que
        diz, meu bom senhor?"

        "A serpente olha profundamente em seus olhos, lambendo os lábios."

        argos "Ou, talvez... sim."

        argos "Não tomarei mais de seu tempo, meu senhor. Não se preocupe, em alguns dias
        retornarei com uma oferta."

        argos "Não é adequado propor ao Mestre nada para o qual eu não
        tenha os termos definitivos."

        jump chapter5


    else:
        argos "Talvez seja difícil para você compreender, novato como é
        no Labirinto."
        argos "Basta dizer, toda essa... coisa, o Hotel, é uma perversão
        da vontade dos Olímpios. Não era desejo de Atena ter piedade
        com o minotauro. Nem era sua intenção que este domínio prisional
        fosse utilizado para lazer."
        argos "Vocês, humanos, são terrivelmente dotados de ingenuidade. Aqueles
        mestres de fraca vontade dos séculos anteriores corromperam esta bela terra em um covil
        de degeneração. Tudo realizado com o abuso das leis do domínio."
        argos "Mas dois podem jogar este jogo, veja bem. Se os humanos farão contratos para
        nos afastar dos deuses, então tenho propostas para o Mestre que nos aproximarão deles.
        Na verdade, tenho um contrato para você bem aqui."
        argos "Espero apenas que você veja, breve o suficiente, que o minotauro o qual
        protege é um covarde. Aquele que causou a queda de sua terra e o
        fim de sua linhagem. Ele não merece piedade, Mestre."

        play sound "sfx/flute.ogg"

        "Argos volta a tocar sua flauta e a música banha o vale como uma chuva
        refrescante. Ele fecha os olhos e leva o tempo que bem entende, como se estivesse
        insultando sua presença. A roupa de pele que ele veste balança com o vento."

        "Você fica onde está, olhando para a cobra no topo da estátua."

        $ myChoices = [ ("Não dizer nada", "opB") ]

        if player_background  == "humanities":
            "Você lidou com muitas pessoas orgulhosas e presunçosas como esta cobra em seu ramo de trabalho.
            Ele pensa muito alto sobre si mesmo -- talvez seja fácil fazê-lo cometer
            um erro."
            $ myChoices.insert(0, ("{color=[UIColorHumanities]}(HUMANAS) Tentar enganar Argos{/color}", "opA"))



        elif player_background  == "leader":
            "Esta cobra pensa muito alto sobre si mesma. Você gerenciou equipes cheias
            de pessoas similares, que acreditam ser um presente de Deus para a terra."
            "Você sabe exatamente como fazê-lo vacilar e cometer um erro."
            $ myChoices.insert(0, ("{color=[UIColorLeader]}(LÍDER) Tentar enganar Argos{/color}", "opA"))

        else:
            "Você não está acostumado a lidar com pessoas TÃO difíceis em seu ramo de trabalho.
            Ao menos não diretamente.
            Você sente que está fora de sua alçada tentar negociar com a cobra."

        $ narrator("O que você faz?", interact=False)
        $ result = renpy.display_menu(myChoices)
        if result == "opA":
            jump chapter4_Trick_Argos
        elif result == "opB":
            "Você segura sua língua."

    "Depois que termina a música, ele olha para você novamente."

    $ Argos.change ("emotion","angry")

    argos "Bem, o que foi? Você quer o Espelho? Eu fiz uma oferta,
    me dê dois minutos com o bezerro e considerarei fornecê-lo.
    Se não aceitar, não tenho motivos para negociar com você."

    argos "Posso servir à missão do Labirinto, mas não estou preso à sua
    vontade. Não preciso seguir suas demandas."

    $ Argos.change ("emotion","smug")

    argos "No entanto... Se o Mestre não aceitar minha primeira oferta, suponho que
    haja... uma coisa que eu quero que pode ser palatável para você."

    argos "Veja bem, meu bom Mestre, eu sou uma entidade do Labirinto. Esta
    terra me gerou. Eu nasci do divino, mas até mesmo eu tenho necessidades."

    argos "Tive ótimas negociações com os Mestres anteriores que acabaram
    tornando-se parcerias frutíferas -- mesmo que discordássemos sobre toda
    essa coisa de Hotel."

    $ Argos.change ("emotion","cocky")

    argos "...Talvez eu deva ir direto ao ponto, hein?"

    argos "Lhe oferecerei um contrato. É exatamente o que parece
    ser, um pedaço de pergaminho estabelecendo regras e efeitos."

    argos "Veja bem, Mestre, posso ser semidivino, mas preciso de comida e água.
    Há décadas tenho vasculhado esta terra, pois Mestre Clément foi embora sem
    negociar seus termos comigo."

    $ Argos.change ("emotion","neutral")

    argos "O contrato é claro. Você me legará um fragmento de seu poder para que
    eu possa invocar comida, água e abrigo. Estou cansado de viver nesta
    terra estéril."

    argos "Como pagamento por sua misericórdia, darei a você este artefato divino,
    usado para acender as chamas sagradas da lareira. Eu diria que é uma troca
    justa -- você terá sua toca confortável e eu também."

    argos "Exceto por Clément, cujo comando foi terrivelmente curto, todos os outros
    Mestres assinaram este termo. Tenho sido útil para todos eles, como eu serei
    para você e você para mim."

    argos "Podemos ser bons vizinhos cavalheirescos."

    argos "O contrato também possui uma cláusula de não agressão. Eu não o
    machucarei, você não me machucará. É um acordo auto-impositivo -- não conseguiremos quebrá-lo. As leis aqui, veja bem, se aplicam.
    Contratos são muito poderosos."

    argos "Na pouca chance de um de nós de alguma forma quebrar um dos termos, nosso
    pacto, então, é anulado. Eu perco os poderes que me foram legados e a lareira
    de seu Hotel se apagará. O objeto volta para a minha posse."

    argos "É um acordo muito justo, eu diria."

    if player_background  == "speedrunner":
        menu:
            "{color=[UIColorSpeedrunner]}(SPEEDRUNNER) Claro, por que não?{/color}":
                you "Ok. Onde eu assino?"
        $Argos.change ("emotion","surprised")
        argos "O que, o Mestre não lerá o contrato?"
        you "Pare de consumir meu tempo, cada símbolo que exibimos na tela é um
        quadro que eu perco. Estou tentando conseguir um recorde mundial aqui."
        argos "...Como é?"
        "Você arranca o contrato da mão dele e o assina."
        you "Tchau."
        "Você volta para dentro com um certo gingado, a cobra é deixada sem palavras após sua
        exibição de agilidade."
        $contestContract = "0"
        $ArgosContract = "Signed"
        jump chapter5


    "Argos entrega o pergaminho para você. Ele diz:"

label contract1:
    play sound "sfx/pageflip.ogg"

    contract "{i}Este documento compromete o Mestre do Labirinto e a cobra conhecida como
    Argos Panoptes, de agora em diante referido como \"o Capataz\", juntos em um acordo."

    contract "{i}Artigo Um.
    O Mestre aluga ao Capataz a autoridade para invocar comida, água,
    abrigo e mobília para uso como ele achar adequado, inclusive para
    o benefício do cultivo de safras e a criação de animais."

    contract "{i}Em retorno, o Capataz aluga o Espelho de Héstia para uso do Mestre como
    ele achar adequado, inclusive para o benefício e manutenção da estrutura conhecida
    como \"Hotel\", conforme estabelecido em contratos anteriores."

    contract "{i}Artigo Dois.
    O Mestre e o arrendatário devem abster-se de causar danos um ao outro,
    direta e indiretamente, por meios incluindo, mas não limitados à violência,
    incentivando ou recompensando terceiros à agressão mútua,
    sabotando estruturas, envenenando alimentos e água, entre outros."

    contract "{i}Artigo Três.
    O Mestre é proibido de interferir direta ou indiretamente no pleno
    gozo dos direitos do Capataz concedidos neste contrato.
    O Capataz é similarmente proibido de causar danos ao \"Hotel.\""

    contract "{i}Artigo Quatro.
    O Mestre está autorizado a fazer inspeções nas acomodações do Capataz,
    exceto em seus aposentos pessoais, cujo acesso é
    proibido."

    contract "{i}O Capataz está proibido de conspirar contra o Mestre e
    não deve usar os direitos garantidos por este Contrato para prejudicá-lo.
    O Mestre e o Capataz estão simetricamente comprometidos a este Artigo,
    incluindo, mas não limitando-se a não usar o Espelho de Héstia para causar danos ao Capataz."

    contract "{i}Artigo Cinco.
    Este contrato é auto-impositivo. Se qualquer um de seus artigos for quebrado,
    a posse do Espelho de Héstia reverte para o Capataz e qualquer chama acesa
    pelo Espelho é apagada."

    contract "{i}Ao mesmo tempo, o Capataz perde os direitos transferidos pelo
    contrato e toda e qualquer estrutura por ele invocada deixa de existir após
    um intervalo de 10 minutos para permitir a evacuação."

    contract "{i}Artigo Seis.
    Este artigo auto-impositivo entra em vigor no momento de sua assinatura
    e permanece válido durante o comando do Mestre e até que o Mestre
    posterior adquira a Escritura do Hotel."

    contract "{i}Pela vontade do Mestre, a quem o comando dos Olímpios sobre o domínio
    foi concedido, este contrato é estabelecido."

    play sound "sfx/pageflip.ogg"

    "Você assinará o Contrato?"
    menu:
        "Sim.":
            $contestContract = "0"
            you "Tudo parece estar em ordem."
            $ Argos.change ("emotion","cocky")
            argos "Estou feliz por meu contrato agradar ao Mestre."
            "Você assina o documento com sua caneta e Argos lhe entrega o espelho."
            argos "É um prazer negociar com você, Mestre. Espero que tenhamos
            mais oportunidades."
            "Você retorna para o Hotel."
            $ArgosContract = "Signed"
            jump chapter5

        "Contestar os termos.":
            "Há algo suspeito sobre este contrato."
            $ Argos.change ("emotion","angry")
            "O olhar de Argos está fixo em você, mudando sutilmente para seguir
            cada mudança em seus olhos."

            call screen ContractApproval('Argos1', ['1','2','3','4','5','6'])
            $contestContract = _return

label contest_contract:
    you "Sinto muito, mas eu não concordo com esses termos aqui."
    "Argos pega o contrato de suas mãos e o lê com atenção."
    $ Argos.change ("emotion","cocky")
    argos "Terá que me perdoar, Mestre. Não vejo nenhum problema..."
    argos "De qualquer forma... suponho que posso dar-lhe algum tempo para pensar sobre isso enquanto
    esboço outra oferta -- com sorte será de seu agrado."
    argos "Agora... Imagino que você deve estar ansioso para fazer esse seu Hotel
    voltar a funcionar. Que tal eu lhe emprestar o Espelho enquanto faço meu esboço?"
    argos "Você pode usá-lo até meu retorno. O chamarei com a minha flauta. Se
    não assinar o contrato quando chegar a hora, no entanto, esta pequena bugiganga voltará
    para mim."
    argos "O Mestre pode interpretar isto como um gesto de boa vontade de seu seguidor."
    "Você e Argos estabelecem um pacto e apertam as mãos."
    "Você retorna ao Hotel com o Espelho de Héstia em mãos."
    $ArgosContract = "Contested"
    jump chapter5


label chapter4_Trick_Argos:
    "Talvez você possa passar a perna nesta cobra presunçosa."

    you "Argos Panoptes, não é? Devo dizer que suas palavras soam bem em meus ouvidos. Fiquei
    em silêncio enquanto você falava, as pesando, mas na verdade eu entendo agora que o minotauro
    me informou mal."
    you "Ele de fato me contou que foi sentenciado a este domínio, mas não que suas
    torturas eram em homenagem aos antigos deuses."
    you "Devo admitir que, sabendo disso, teria agido de maneira bem diferente.
    Suponho que você esteja certo, os humanos ficaram compassivos demais. É chegada a hora,
    talvez, de retornarmos à devida adoração aos antigos deuses."
    $ Argos.change ("emotion","smug")

    argos "Ora ora, você é um dos iluminados, não é mesmo? Talvez eu também
    o tenha entendido mal, meu bom Mestre. Fui rude, então, por sugerir que
    você tinha uma disposição fraca."
    argos "Eu realmente devo pedir seu perdão por minha língua indisciplinada."

    you "Você está perdoado, Argos. Já que você é quem realmente está ligado aos deuses,
    é importante que comecemos com o pé direito. Por favor, desça para que eu possa apertar sua mão."

    $ Argos.change ("pose","straight")

    "Argos desliza para baixo, girando e virando com uma elegância brincalhona. Sua cabeça também
    se anima, como a de um cachorrinho."

    argos "Que dia alegre, o novo Mestre chega e me abençoa com a oportunidade
    de honrá-lo! Os deuses enviaram sua glória para o vale!"

    you "Esta é a nossa esperança, Argos. É uma honra conhecer um servo fiel dos deuses."

    $ Argos.change ("emotion","cocky")

    "Você aperta a mão de Argos e ele mal consegue conter a empolgação."

    you "Ontem aceitei oficialmente o minotauro ao meu serviço. Ele
    fez um juramento para mim. Presumo que o contrato o qual você deseja que eu assine seja semelhante."

    you "Que tal fazermos disso uma cerimônia apropriada? Ofereça-me o objeto e
    o contrato, boa cobra. Então você deve se curvar a mim e eu terei o prazer
    em considerar assiná-lo."

    "Sem dizer uma palavra, ele se curva para você e levanta as mãos, oferecendo-lhe
    o papel e o espelho."

    you "Você possui excelentes maneiras. Fico grato por sua oferta, Argos
    Panoptes."

    argos "Vivo para servir aos Olímpios e seu Mestre designado. É uma
    honra."

    "Argos entrega o pergaminho para você. Ele diz:"

    play sound "sfx/pageflip.ogg"

    contract "{i}Este documento compromete o Mestre do Labirinto e a cobra conhecida como
    Argos Panoptes, de agora em diante referido como \"o Capataz\", juntos em um acordo."

    contract "{i}Artigo Um.
    O Mestre aluga ao Capataz a autoridade para invocar comida, água,
    abrigo e mobília para uso como ele achar adequado, inclusive para
    o benefício do cultivo de safras e a criação de animais."

    contract "{i}Em retorno, o Capataz aluga o Espelho de Héstia para uso do Mestre como
    ele achar adequado, inclusive para o benefício e manutenção da estrutura conhecida
    como \"Hotel\", conforme estabelecido em contratos anteriores."

    contract "{i}Artigo Dois.
    O Mestre e o arrendatário devem abster-se de causar danos um ao outro,
    direta e indiretamente, por meios incluindo, mas não limitados à violência,
    incentivando ou recompensando terceiros à agressão mútua,
    sabotando estruturas, envenenando alimentos e água, entre outros."

    contract "{i}Artigo Três.
    O Mestre é proibido de interferir direta ou indiretamente no pleno
    gozo dos direitos do Capataz concedidos neste contrato.
    O Capataz é similarmente proibido de causar danos ao \"Hotel.\""

    contract "{i}Artigo Quatro.
    O Mestre está autorizado a fazer inspeções nas acomodações do Capataz,
    exceto em seus aposentos pessoais, cujo acesso é
    proibido."

    contract "{i}O Capataz está proibido de conspirar contra o Mestre e
    não deve usar os direitos garantidos por este Contrato para prejudicá-lo.
    O Mestre e o Capataz estão simetricamente comprometidos a este Artigo,
    incluindo, mas não limitando-se a não usar o Espelho de Héstia para causar danos ao Capataz."

    contract "{i}Artigo Cinco.
    Este contrato é auto-impositivo. Se qualquer um de seus artigos for quebrado,
    a posse do Espelho de Héstia reverte para o Capataz e qualquer chama acesa
    pelo Espelho é apagada."

    contract "{i}Ao mesmo tempo, o Capataz perde os direitos transferidos pelo
    contrato e toda e qualquer estrutura por ele invocada deixa de existir após
    um intervalo de 10 minutos para permitir a evacuação."

    contract "{i}Artigo Seis.
    Este artigo auto-impositivo entra em vigor no momento de sua assinatura
    e permanece válido durante o comando do Mestre e até que o Mestre
    posterior adquira a Escritura do Hotel."

    contract "{i}Pela vontade do Mestre, a quem o comando dos Olímpios sobre o domínio
    foi concedido, este contrato é estabelecido."

    play sound "sfx/pageflip.ogg"

    you "Ora, o que é isso? Aqui diz que, ao assinar este contrato, eu permito que você
    entre nos limites do Hotel -- que, assim como eu posso inspecionar suas acomodações, você poderá inspecionar o Hotel.
    Não foi isso que você descreveu para mim há apenas um minuto, Argos."

    you "Eu sei que você não tem permissão para entrar."

    $ Argos.change ("emotion","surprised")

    "A postura de Argos muda, de uma reverência graciosa para uma rígida e trêmula."

    you "Você estava tentando me enganar? Isto é terrivelmente dissimulado de sua
    parte. Achei que você fosse um honorável seguidor dos deuses."

    you "Sinto muito, mas não posso assinar este contrato."
    you "Infelizmente, é uma pena. Bem, você me ofereceu o objeto em troca de minha
    consideração, então ele pertence a mim agora."

    you "Desejo-lhe um bom dia, Argos. Talvez da próxima vez você não tente passar a perna no seu
    senhor."

    "Sem pensar duas vezes, focando apenas em conter o grande sorriso pretensioso
    estampado em seu rosto, você se vira para voltar para dentro."

    argos "Espere, Mestre! Isto é um engano, eu o ofereci o pergaminho errado!
    Aqui, este é o correto, por favor, reconsidere!"

    argos "Não vá, eu realmente sou seu seguidor, estou honrado! Por favor... Estou com tanta fome..."

    you "Você deixou um gosto amargo na minha boca, Argos. Faça-se útil para
    mim e volte mais tarde com um acordo de verdade. Talvez eu
    reconsidere -- sem promessas, no entanto."
    $ArgosContract = "Tricked"
    jump chapter5
    #PC returns with the trinket, Asterion is overjoyed.


##############################################################################
#                      CHAPTER 5: HESTIA'S MIRROR
##############################################################################
label chapter5:
    scene bg black
    with Dissolve (2)

    $chapter = "Capítulo 4"

    call screen ChapterTransition("Capítulo 4", "Ignição para a chama sagrada")
    pause 0.5
    $save_name=output_save_name("Capítulo 4")

    scene bg valley_exit
    with Dissolve (1)
    $ global_affection += 1.0
    play music "music/seikilos.mp3" fadeout 4.0 fadein 4.0

    if Chapter4_Terrorized_Asterion  == "True":
        $ global_affection = 0
        "A caverna engole você de volta às profundezas do Hotel -- uma escuridão aveludada
        a qual seus olhos lutam para se adaptar. Sua respiração e seus passos ecoam por todo o
        caminho até a escada em espiral."

        "Sua sombra se estende através da câmara, tornando-se desfigurada sobre as pedras
        irregulares. Enquanto seus olhos se acomodam, você olha para ela -- olha para como é gigantesca,
        a sombra de um homem."

        show Asterion:
            xalign 0.4 yalign 1.7 alpha 1.0
        with Dissolve(1)

        "Astério está sentado contra uma das paredes da câmara, olhando para você e para
        esta besta se estendendo de seus pés. O olhar dele vagueia, mas o queixo está pingando suor."

        you "Astério, me desculpe...{w=0.2} Eu não sabia que ele ia fazer aquilo.{w}
        Achei que ele só queria conversar, e que era a única maneira de conseguir o espelho."

        "Você se ajoelha na frente dele, mas o olhar dele não se altera."

        you "Astério?"

        "A chama em sua cavidade ocular pisca para você.{w}
        Ele fala, mas sua voz está diferente -- afetada, quebrada, mais quieta."

        asterion "Não.{w=0.2} A culpa é minha.{w} Eu deveria ter --"

        show Asterion:
            ease 0.2 yalign 1.6
            ease 0.3 yalign 1.7
            ease 0.2 yalign 1.6
            ease 0.3 yalign 1.7

        "Ele parece engasgar com as próprias palavras e tem um violento acesso de tosse,
        quase como se estivesse prestes a vomitar os pulmões."

        "Ele se inclina -- e então você ouve.{w}
        Um assobio vindo da garganta do minotauro enquanto ela se fecha."

        "Ele luta para respirar. Com uma mão ele agarra a própria garganta,
        com a outra, sustenta o próprio peso."

        show Asterion:
            ease 0.5 xalign 0.35 yalign 1.8

        "Você se move para tocá-lo, mas assim que sua sombra cobre a cabeça dele, ele olha para você
        e quase cai na sua direção contrária."

        show Asterion:
            ease 1.0 xalign 0.45 yalign 1.3

        "Mas algo chama a atenção dele, o Espelho que você está segurando."

        "Em um piscar de olhos, a aversão dele se transforma em fome. Ele estende a mão para o espelho."

        "Você mal tem tempo suficiente para pensar -- simplesmente o deixa removê-lo de suas mãos."

        show Asterion:
            ease 1.0 xalign 0.4 yalign 1.9

        "Ele abraça o Espelho e desaba para o lado.{w} O minotauro ainda luta para respirar,
        mas há uma paz em seu ser, enquanto ele acaricia o bronze gelado com os dedos."

        "Sua sombra, longa e terrível, o cobre."

        "Você se agacha para esfregar as costas dele, mas sente a tensão sob seu toque.{w}
        Astério não olha para você -- seu olho está fechado enquanto ele abraça seu precioso Espelho."

        "Você se senta com as costas contra a parede para esperar.{w}
        Demora alguns minutos antes que a respiração do minotauro volte
        ao normal e ele abra o olho."

        you "Me desculpe. Eu não sabia que ele ia fazer isso, ele prometeu que não machuraria você."

        asterion "Não, isso é tudo culpa minha.{w} Eu deveria ter contado ao Mestre sobre o Capataz."

        asterion "Ele é uma coisa antiga do Labirinto. Sua forma se altera volta e meia,
        ele desaparece por alguns anos de cada vez, até mesmo décadas."

        asterion "Mas o Capataz já existe há alguns milênios.
        Seu papel também é me torturar."

        you "Então é por isso que você tem medo dele, ele te machucou."

        "Ele solta um suspiro longo e prolongado."

        asterion "Há coisas piores no vale.{w}
        O que ele fez comigo não é tão aterrorizante quanto o que aqueles monstros podem fazer."

        asterion "...Há coisas horríveis lá fora, criaturas feitas pelos próprios
        deuses. Suspeito que Argos seja um deles, apenas dotado de mais
        inteligência que sede de sangue."

        "Ele se enrola ainda mais em torno de seu precioso espelho."

        asterion "...O vale é lindo, não é, Mestre? É um espetáculo para ser visto."

        asterion "Mas para mim é aterrorizante -- um lugar lindo também pode ser um inferno.
        Por milênios eu fui torturado lá. O simples fato de estar aqui embaixo me faz mal."

        $ Promise_Valley = "Unasked"

        "A chama cintilante no crânio dele está voltada para você."

        asterion "Podemos retornar agora? Já somos capazes de iniciar a restauração do Hotel."

        you "Claro. Quer ajuda para se levantar?"

        asterion "Isto não será necessário."

        show Asterion:
            ease 1.0 xalign 0.45 yalign 1.5
            ease 1.0 xalign 0.5 yalign 1.0

        "O minotauro rola e se levanta sozinho."

        jump chapter5_2b


    "A caverna engole você de volta às profundezas do Hotel -- uma escuridão aveludada
    a qual seus olhos lutam para se adaptar. Sua respiração e seus passos ecoam por todo o
    caminho até a escada em espiral."

    "Sua sombra se estende através da câmara, tornando-se desfigurada sobre as pedras
    irregulares. Enquanto seus olhos se acomodam, você olha para ela -- observa como é gigantesca,
    a sombra de um homem."

    show Asterion:
        yalign 1.8 xalign 0.5
    with Dissolve(1)

    "Astério está sentado contra uma das paredes da câmara, olhando para você e para
    esta besta se estendendo de seus pés. A chama do olho dele pisca
    para você."

    you "Consegui o Espelho. Agora podemos fazer o Hotel voltar a funcionar, certo?"

    "Você o passa para Astério. Os dedos dele roçam e enrolam suavemente sobre o
    bronze, e então ele o tira de sua mão com uma elegância cerimonial e o embala
    contra o peito."

    "Você dá uma boa olhada em Astério. Seu pelo e camisa estão molhados de suor,
    apesar da temperatura um tanto fria da câmara. A cauda balança atrás
    dele como um mar turbulento."

    asterion "Sinto muito por não lhe informar antes sobre o Capataz. Eu
    realmente sinto muito. Não sei o que deu em mim, Mestre."

    you "Não se preocupe com isso, não foi nenhum problema. Ele queria que eu
    mandasse você para fora, mas eu não ia fazer isso. Então, tivemos que
    descobrir outra maneira de resolver o problema."
    if player_background  == "speedrunner":
        you "Eu não sou muito bom com toda essa coisa de \"leitura\", então eu fui
        em frente e assinei, pareceu uma boa ideia no momento."
        pause 2
        "Você consegue sentir a decepção de Astério fervendo dentro dele."
        asterion "Entendi. Eu deveria saber."
    else:
        if ArgosContract == "Signed":
            you "Ele queria comida, água e abrigo. Assinei um contrato permitindo que ele
            invocasse os itens. Em troca, ganhamos o Espelho."

        if ArgosContract == "Contested":
            you "Ele queria comida, água e abrigo. Me ofereceu um contrato, mas
            acho que percebi alguma coisa estranha nele. Ele me emprestou o Espelho
            enquanto conserta o contrato."

        if ArgosContract == "Tricked":
            you "Ele queria comida, água e abrigo... mas eu consegui passar a perna nele.
            Fiz com que ele me entregasse o espelho em troca de nada. Se ele quer que eu
            assine esse contrato, vai ter que se mostrar útil."

        asterion "Sim... isso é normalmente o que ele pede."

    asterion "A cobra, ela é uma coisa antiga do Labirinto. Sua forma
    se altera volta e meia, ele desaparece por alguns anos de cada vez,
    até mesmo décadas."

    asterion "Mas o Capataz já existe há alguns milênios.
    Seu papel também é me torturar."

    asterion "...Obrigado."

    "Astério abraça o Espelho. Seus dedos esfregam contra a superfície,
    provocando o frio cortante do metal. Ele o segura contra seu peito
    como algo bastante precioso."

    you "Tudo bem, então, vamos voltar?"

    asterion "...Sim, senhor. Perdoe minha lentidão, estou me sentindo um pouco enjoado.
    Isso tudo me deixou...em um estado de pânico."

    you "Ah. Eu posso esperar."

    "Você se senta ao lado de Astério, assumindo uma posição bem distinta à dele
    -- sentado de pernas cruzadas em contraste com os joelhos dele para cima."

    you "Então... ele machucou você antigamente? É por isso que você tem medo dele?"

    asterion "Ele não me {i}machuca{/i} geralmente. Faz jogos para me aterrorizar,
    na maioria das vezes, e manda coisas piores para me pegar."

    asterion "...Há coisas horríveis lá fora, criaturas feitas pelos próprios
    deuses. Argos deve ser um deles, apenas dotado de mais
    inteligência que sede de sangue."

    asterion "...O vale é lindo, não é, Mestre?
    É um espetáculo para ser visto."

    asterion "Mas para mim é aterrorizante -- um lindo lugar também pode ser um inferno.
    Por milênios eu fui torturado lá. O simples fato de estar aqui embaixo me faz mal."

    asterion "Mestre, você me permite falar francamente?"

    you "Você não tem que pedir minha permissão assim.
    Se você quer falar, simplesmente fale."

    you "Estou te dando permissão para falar comigo livremente,
    sempre que quiser."

    play sound "sfx/hum.ogg"

    "Suas palavras cortam através da galeria ao seu redor, e você ouve o zumbido
    agora familiar vindo da escadaria."

    "O próprio mundo estremece em resposta -- como se suas palavras criassem raízes e o
    alterassem à força."

    if global_affection >= 2.5:
        "O minotauro percebe esta mudança arrepiante em torno
        de vocês dois."

        asterion "...Você é bastante tolerante, no que diz respeito aos Mestres.
        Não houve muitos que me permitiram tal liberdade. Ironicamente,
        Mestre Clément foi um dos poucos que permitiram."

        asterion "Mas não foi isso que eu quis dizer."

    "O minotauro respira fundo e desvia o olhar de você."

    asterion "Por favor, nunca me mande para o vale. Eu farei qualquer coisa
    por você, qualquer coisa, apenas não me peça para fazer isto em particular."

    asterion "Você pode me punir como quiser se eu fizer algo errado, mesmo se
    eu fizer tudo certo também. Eu aguento qualquer coisa.
    Apenas, por favor, não me faça sair."

    menu:
        "Mudar de assunto.":
            "Você fica em silêncio, pensando no que o minotauro acabou de dizer."
            "Talvez esta seja uma decisão que você não está pronto para tomar, por enquanto.
            Você muda de assunto, então permite que os dois fiquem em silêncio."
            $ Promise_Valley = "False"
            jump chapter5_2

        "Prometer nunca mandar Astério para o vale.":
            $ global_affection += 0.5
            $ Promise_Valley = "True"
            jump chapter5_1

label chapter5_1:
    you "Astério... olhe para mim."

    you "Eu prometo que nunca vou mandar você para lá."

    you "Não posso dizer que sei exatamente o que fizeram com você lá fora. Eu
    entendo se você não quiser falar sobre isso. Mas eu vou aceitar seu pedido,
    e não vou mandar você para lá."

    you "Eu estava falando sério ontem à noite: Eu quero ser um bom mestre para você
    e para o Hotel. Eu não vou machucar você, e prometo que nunca vou te mandar para lá."

    "Astério olha para você com o olho entreaberto. A náusea ainda se contorce dentro
    dele, e ele balança para frente e para trás como se empurrado e puxado pelas ondas do mar."

    "Suas palavras são doces como mel. Um véu de chumbo cai sobre o minotauro."

    "As costas dele cedem e ele se curva para frente, ainda segurando o Espelho contra
    o peito. Ele descansa seus chifres nos joelhos e solta um suspiro estrondoso
    do fundo de seus pulmões."

    you "Você está se sentindo bem?"

    asterion "Uhum. Só bastante... cansado."

    you "Podemos ficar aqui mais um pouco. Leve o tempo que precisar."

    "Astério suspira outra vez."

    menu:
        "Confortá-lo.":
            "Você coloca um braço sobre os ombros de Astério."

            if global_affection >= 3:
                "Astério fica tenso quando você o toca, mas dura apenas um momento."

                "Você o pega virando a cabeça ligeiramente para a direita, em sua
                direção. Ele responde com uma piscada longa e deliberada, seguida pelos
                ombros relaxando sob seu braço."

                "Astério está surpreendentemente quente. Seu pelo bagunçado não faz muito
                para conter o calor do corpo."

                "Ele inclina a cabeça em seu braço, tomando cuidado para não deitar o chifre
                em você."

                "Há quinze centímetros separando vocês dois. Você chega mais
                perto dele -- ele olha para você novamente e algo faísca em
                seu olho."

                "É fome de toque humano. Astério passou décadas trancado
                em um quarto escuro, passando fome e sede, tornando-se
                emaciado ano após ano."

                "Você o alimentou, vestiu e cuidou de suas feridas. Mas uma nova
                forma de fome surge em sua cabeça agora, e não há como ele
                ele esconder isso."

                "Agora que você está perto, ele apoia o peso em seu ombro e fecha
                o olho. Você o puxa para mais perto, aceitando toda a exaustão
                acumulada nos ossos dele."

                "Às vezes, você sente o olho dele se abrindo novamente, movendo-se para os lados.
                Ele quer seu calor, mas luta para ceder totalmente.
                A batalha continua feroz dentro dele, e o lado de permanecer
                perto de você vence."

                "Astério mencionou que Mestre Jean-Marie costumava acariciá-lo atrás
                das orelhas. Agora ele tem apenas uma, mas a forma como ele a sacode
                para você possui uma qualidade convidativa."

                "Você o acaricia e ele derrete em você, aninhando-se como uma criança. O peito
                dele ronca com o suspiro profundo que escorre de sua garganta."

                "Você o deixa cochilar em seu ombro pelo tempo que ele quiser."

                jump chapter5_2


            else:
                "O minotauro congela assim que você o toca."

                "A tensão em sua postura é um sinal de que seu toque não é muito
                bem-vindo. Você dá um tapinha nas costas dele e deixa por isso mesmo."
                jump chapter5_2

        "Deixá-lo em paz.":
            "Talvez fosse ultrapassar os limites tocá-lo agora."
            jump chapter5_2

label chapter5_2:
    show Asterion:
        ease 2.0 yalign 1.0
    "Eventualmente, Astério sinaliza para você que ele está pronto para seguir o caminho de volta para cima."

    scene bg staircase
    jump chapter5_2b

label chapter5_2b:
    "Você tem que parar algumas vezes para deixar Astério descansar, mas, eventualmente, vocês
    conseguem chegar ao andar térreo e ao salão."

    scene bg lounge
    show blackback:
        alpha 0.7
    with Dissolve(1)

    "Dentro do antigo salão, glorioso e consumido pelo tempo, você e Astério
    encontram uma lareira coberta de fuligem em frente ao bar. É cercada por um
    conjunto de poltronas. O couro delas rachou e secou, mas nenhum dano
    pode esconder o talento com que foram feitas."

    "A luz do sol cai em frente à lareira, entrando pelas altas janelas de vidro
    do salão."

    "Astério se ajoelha diante da lareira em uma posição parecida com uma oração. Ele
    deixa o Espelho de lado por um momento e invoca toras de madeira e feno seco e saudável.
    Em seguida, coloca o feno no ponto focal do Espelho."

    "O feixe de luz solar focalizado aquece o feno."

    "Você e Astério esperam."

    show Asterion behind blackback:
        xalign 0.5 yalign 1.0 zoom 1.0
    with Dissolve(1)

    asterion "Décadas atrás, se o fogo cessasse, eu teria sido punido.
    Cuidar dele era uma de minhas muitas funções e falhar em fazer isto era um
    dos erros mais graves que eu poderia cometer."

    asterion "Assim que acender novamente, o Hotel voltará à vida."

    asterion "...Este domínio é bem diferente do mundo exterior, não é? É
    difícil para mim até mesmo lembrar como era lá fora quando eu estava vivo."

    asterion "Lá em casa, quando eu era apenas um menino, saí para caçar cabras selvagens
    com um de meus irmãos. Encontrando nossa própria comida e trazendo-a de volta para casa..."

    asterion "Nosso pai me levava para o campo. As pessoas acreditavam que eu lhes traria
    boa sorte e boa colheita."

    asterion "...A comida é colhida ou caçada, a madeira é cortada, casas são construídas
    com suor e pedra. Mas este mundo opera sob regras diferentes."

    asterion "Os deuses construíram o mundo onde nascemos sabendo bem que estávamos
    destinados a trabalhar duro e sofrer.{w} Tal é o destino do homem."

    asterion "\"Enquanto viveres,{w=0.2} brilha,{w=0.2} de todo não te aflijas.{w} Pois curta é a
    vida{w=0.2} e o tempo cobra seu tributo.\""

    asterion "Os deuses apreciam o sofrimento dos mortais. Então, eles optaram
    por não ligar este domínio às mesmas regras."

    asterion "Se alguém deseja infligir dor, este deve derrubar uma árvore e confeccionar
    uma lança a partir da madeira, depois minerar e refinar o metal para o topo.{w} Aqui, porém,
    meu carcereiro poderia invocar quantas lanças quisesse."

    asterion "Por que perder tempo trabalhando na terra quando ele poderia facilmente invocar toda
    a comida que seu corpo deseja?"

    asterion "Da mesma forma, ele poderia quebrar as regras da vida e do próprio espaço. A
    arquitetura da realidade. A vontade do Mestre é soberana."

    "À medida que Astério fala, o feno se contorce conforme fica mais seco, e então escurece
    e emite uma fina fumaça. A pura chama logo estará presente."

    asterion "Os deuses, no entanto, raramente compreendem a engenhosidade humana. A mudança os
    confunde. Com prazer, eles passariam séculos sem mudar, repetindo os mesmos
    dias para todo o sempre."

    asterion "Eu vi isso com meus próprios olhos."

    asterion "Eu posso ser um monstro,{w=0.2} mas sou meio humano.
    A mudança também é fácil para mim. Eu mudei a cada século,
    adaptando-me à vontade do meu Mestre, fazendo o que fosse necessário."

    "Uma lasca de fogo sobe a partir do feno. Astério o pega, sem se importar
    se vai se queimar ou não, e coloca entre as toras."

    if Chapter4_Terrorized_Asterion  == "True":
        asterion "Ainda assim, não é dito que os humanos possuem uma fagulha do divino?{w}
        É o que os separa das bestas, eu presumo."

        asterion "Eu também tenho o divino em mim.{w} E eu o temo,{w=0.2} temo sim."

        asterion "Nem uma besta, nem humano, muito menos um deus.{w} E morto,
        é claro.{w} Para sempre morto."

        asterion "...Dito isso, eu preferiria ter sido um humano.{w} Viver
        meus dias, trabalhar duro, perecer sabendo que fui abençoado com aquilo que é essencialmente
        humano."

    else:
        asterion "...Você possui bondade em si."

    asterion "..."

    asterion "Mas a engenhosidade humana, às vezes, vai longe demais. Há coisas que o
    Hotel não consegue realizar, não importa o quanto se tente."

    asterion "O homem não pode se tornar imortal, para começar. Os deuses não teriam sido
    tão clementes. Nem os mortos podem ser trazidos de volta."

    asterion "O Hotel não produzirá ouro ou prata em grandes quantidades e
    nunca imprimirá moeda."

    asterion "Mais importante de tudo, o domínio precisa de instruções precisas sobre
    o que se pretende fabricar."

    asterion "Por mais poderoso que o Mestre possa ser aqui, ele nunca pode ser transformado
    em um deus. Esta é uma regra fundamental do Labirinto."

    asterion "..."

    scene bg hearth
    with Dissolve (2)

    asterion "Uma chama pura, adequada para os deuses."

    asterion "Os deuses se foram. Pelas histórias que os hóspedes contaram ao longo
    dos séculos, pareceu para mim que o mundo lá fora estava bem a caminho de deixar
    o mito e a magia para trás."

    asterion "Mas o poder deles perdura. Uma oferenda ainda pode ser ouvida
    e o Labirinto nunca abandonará estas regras fundamentais.{w} Um homem permanece um homem."

    asterion "\"Enquanto viveres,{w=0.2} brilha,{w=0.2} de todo não te aflijas.{w} Pois curta é a
    vida{w=0.2} e o tempo cobra seu tributo.\""

    asterion "Você já ouviu esta música antes, Mestre? Eu ouvi uma mulher de
    Éfeso cantá-la. Ela disse que seu marido a escreveu quando ela morreu.
    Muitas pessoas começaram a cantá-la lá embaixo, seja em Elísio ou Tártaro."

    asterion "A vida é curta -- mais para alguns que para outros. Deve ser apreciada."

    asterion "...Quem o legou a Escritura do Hotel deu-lhe um presente maior do que
    qualquer fortuna. Este lugar, e eu, atenderemos às suas necessidades."

    asterion "Você pode viver uma vida abençoada e, se permitir que este lugar cumpra seu propósito
    criado pelo homem -- fornecer refúgio àqueles perdidos e vagando por aí
    -- dará sentido à sua vida também."

    asterion "Mesmo uma existência tão miserável quanto a minha pode ter beleza, meu senhor."

    if Chapter4_Terrorized_Asterion  == "True":

        asterion "É meu dever informá-lo de tais assuntos.{w} Embora eu deva dizer
        que sinto muito por estar divagando."

    else:
        asterion "Não sei bem por que estou lhe contando tudo isso. Suponho que senti
        saudades de conversar, e eu me sinto tão nervoso de repente."

    you "Não se preocupe com isso, eu gosto de ouvir você."

    you "Isso é ótimo, sabe? Conversar desse jeito em frente ao fogo. Não posso dizer
    que entendi completamente como esse Hotel funciona e o que está acontecendo, mas..."

    you "Esse é um ótimo momento, você não acha?"

    if Chapter4_Terrorized_Asterion  == "True":
        "O minotauro resmunga baixinho."

    else:
        asterion "...Sim, de fato."

    "A chama se parece com qualquer fogo comum, mas algo atrai sua
    atenção para ela. Por um longo tempo -- horas, talvez -- você e Astério olham para ela."

    "No fundo de sua mente, você pode ouvir o Hotel rangendo e torcendo,
    móveis se arrastando aqui e ali, tecido rasgando e costurando-se
    de volta."

    "Você consegue, bem nos cantos de sua visão, perceber o salão
    se refazendo."

    "O sol se arrasta pelo céu. Em algum momento, uma vaga forma se
    materializa entre você e Astério -- uma garrafa de vinho."

    "O minotauro encontra-se tão lerdo quanto você, mas ele consegue pegá-la e
    abri-la."

    if global_affection >= 3.0:
        "Ele oferece a garrafa para você antes de ele mesmo tomar um gole,
        mas você o deixa beber tudo."

    "Assim como na noite anterior, ele bebe diretamente da garrafa -- embora
    desta vez ele demonstre melhoria em lidar com a metade esquelética de sua boca."

    "Mas sua atenção é puxada de volta para o fogo. As chamas diminuem quanto mais
    você olha, até se estabelecerem em brasas quase apagadas."

    "Talvez sejam seus olhos enganando você, mas nas chamas da lareira uma cena se
    desenrola.{w} Lá está você, Astério e o salão."

    "Ela se altera e oscila.{w} Às vezes, reverte-se para uma taverna arcaica,
    o piso revestido de ladrilhos de cerâmica e paredes cobertas de barris de vinho envelhecido."

    "Em seguida, ela salta para frente, para o que você só pode acreditar que é o futuro,{w=0.2}
    mas é como se o fogo estivesse indeciso."

    show image "images/Kota/Kota.webp":
        alpha 0.4 xalign 0.1 yalign 1.0
    with Dissolve(1)

    "Às vezes você vê um restaurante elegante e clientes bem vestidos, com
    uma larga silhueta atrás do bar. É um espaço cênico, mas com uma rigidez
    subjacente que alguns poderiam considerar sufocante."

    hide image "images/Kota/Kota.webp"
    with Dissolve(1)

    "Mas existe outra possibilidade..."

    show image "images/Luke/Luke.webp":
        alpha 0.4 xalign 0.9 yalign 1.0
    with Dissolve(1)

    "Um lugar turbulento, possivelmente até lascivo, com um homem seminu o administrando.
    O tipo de lugar onde se poderia viver travessuras inesquecíveis,
    vergonhosas e revigorantes."

    hide image "images/Luke/Luke.webp"
    with Dissolve(1)

    "Estes dois pontos de vista para o salão parecem lutar um contra o outro."

    "Um peso cai sobre seus ombros. As chamas repetem a visão, de novo e
    de novo, forçando-lhe a tomar uma decisão.{w} O Hotel exige uma resposta."

    "Qual é a sua vontade?"

    menu:
        "Que tipo de salão você deseja?"
        "Elegante e cênico, mas rigoroso.":
            $first_guest = "Kota"
            jump chapter5_3

        "Divertido e turbulento... talvez até excitante.":
            $first_guest = "Luke"
            jump chapter5_3

label chapter5_3:
    "Conforme você faz sua escolha, uma sensação de finalidade descende -- como se você
    tivesse quebrado um selo, ou talvez assinado um contrato."

    "Você é puxado para fora de sua meditação. Astério também olha para
    o fogo, imperturbado pelo que aconteceu."

    asterion "Estava com medo de ficar trancado lá para sempre."

    asterion "Isto continuava voltando para mim... este foi o destino dos deuses? Eles
    foram trancados em algum lugar, presos e esquecidos? Foi por isso que eles desapareceram?"

    asterion "Se ao menos eu pudesse desobecer às ordens do Mestre Clément, teria
    derrubado aquela porta no mesmo dia em que ele me jogou lá dentro. Mas eu não podia.
    Eu não posso desobedecer ao Mestre."

    asterion "...Nem posso desobedecer a você."

    asterion "Por todos esses anos eu pensei, e pensei, e pensei. Não havia
    nada mais que eu pudesse fazer, e meu corpo estava apodrecendo."

    asterion "Pensei em tudo o que poderia acontecer, cada pequena possibilidade.
    Gostaria de poder dizer a você que eu sonhei, e, de fato, às vezes me permitia
    ter esperança."

    asterion "Mas, na maioria das vezes, eu pensava sobre todas as coisas ruins que poderiam
    vir em seguida, cada possibilidade."

    if Chapter4_Terrorized_Asterion == "True":
        asterion "...Porém, nada disso importa.{w} O Hotel está voltando à
        vida. É quase como se eu estivesse enlouquecendo, pensei que nunca mais veria outra
        alma viva."

    else:
        asterion "É difícil para mim acreditar que estou...{w=0.2} \"livre.\"{w} Às vezes me
        pego pensando que isso deve ser um dos meus devaneios."

        asterion "Eu estava certo de que você me mandaria lá fora para o Capataz, e tudo se transformaria
        em um pesadelo. Meu estômago estava se revirando, me sentei porque não conseguia ficar
        de pé."

    $Asterion.change ("stage", "dyel")
    $Asterion.change ("fur", "brown")
    $Asterion.change ("emotion", "tired")
    $Asterion.change ("leftarm", "loose")
    $Asterion.change ("rightarm", "hips")
    if persistent.sfwMode:
        $Asterion.change("underwear", "loincloth")
    $Asterion.wearFavorite()

    scene bg lounge
    with Dissolve (1)
    "Quando você se vira, é saudado com uma nova vista -- um salão reconstruído,
    um sol de fim de tarde lá fora e um Astério completamente diferente."
    show Asterion
    with Dissolve (1)

    asterion "Mas não é um sonho. Nós {i}estamos{/i} aqui."

    $Asterion.change ("rightarm", "loose")

    asterion "...Eu só quero voltar para a minha vida. Meu hotel, meus hóspedes.
    Vozes ecoando pelos corredores, comida e bebida para todos, ouvindo suas
    histórias noite adentro."

    $Asterion.change ("emotion", "sad")

    asterion "Às vezes eu saía escondido durante a noite, enquanto o Mestre Jean-Marie
    dormia. Lá fora, eu me encontrava com um amigo -- um matemático do
    Novo Mundo."

    asterion "E conversávamos sem parar sobre o {i}infinito{/i}, sobre a arquitetura do
    Hotel. Trazíamos vinho e..."

    $Asterion.change ("rightarm", "hips")
    $Asterion.change ("emotion", "smiling")

    asterion "...ficávamos muito bêbados e barulhentos."

    asterion "Em seguida, a equipe da cozinha juntava-se a nós e, mais tarde,
    o recepcionista noturno."

    asterion "Ficávamos na porta dos fundos da cozinha, do lado de fora, com um rádio
    tocando lá dentro... Ouvíamos músicas da França a noite inteira."

    asterion "Eu invocava cigarros para eles. Eu não fumava, mas voltava
    fedendo a tabaco, sempre precisava tomar um banho antes do
    Mestre acordar."

    asterion "E, por sua vez, eles pediam ao Mestre Jean-Marie para me colocar em suas
    equipes -- e eu apenas... eu não fazia muito, apenas desfrutava da companhia deles."

    asterion "Passar um dia com amigos. Conversando, rindo, nenhuma preocupação
    com o mundo."
    $Asterion.change ("rightarm", "loose")

    asterion "Isto era {i}vida.{/i} Eu acordava todos os dias sabendo que minha existência tinha significado."

    $Asterion.change ("emotion", "tired")

    asterion "Eu tinha um propósito -- era tudo o que eu tinha -- e aquele demônio tirou isso
    de mim."

    asterion "Era como um sonho. Era como se todo o meu passado nunca tivesse acontecido e
    eu pudesse viver a fantasia de fazer algo bom. Cada dia
    era uma maravilha. Foi ótimo e me manteve longe dos pesadelos."

    $Asterion.change ("emotion", "sad")

    asterion "Não importava se os Mestres me tratavam bem ou não, pois
    minha vida não se resumia a eles. Eu tinha amigos e uma razão para existir."

    asterion "Eu não era o minotauro de Creta ou algum prisioneiro torturado. Eu
    era {i}Astério{/i}, simples assim, e as chances eram de que eles não soubessem o que
    me fez estar aqui em primeiro lugar."

    asterion "Mas o sonho tinha que acabar. Tinha que acabar."

    asterion "Eu morri uma vez, em Creta, e de novo quando Clément
    expulsou meus hóspedes. Todas as minhas outras mortes, torturado por Mestres de
    séculos atrás, foram pequenas em comparação a estas."

    asterion "...Não é justo."

    asterion "Eu sou um monstro, eu conheço meus crimes, mas o que meus hóspedes fizeram?
    Nada para merecerem ser expulsos de sua casa."

    asterion "Nós tínhamos veteranos se recuperando do trauma, soldados ainda se
    curando de seus ferimentos, refugiados das frentes."

    $Asterion.change ("emotion", "angry")

    asterion "Construímos um propósito para este lugar -- não graças aos deuses -- e aquele
    demônio egoísta o destruiu."

    if Chapter4_Terrorized_Asterion == "True":
        asterion "Eu sei como sou indigno, que meu nascimento foi uma atrocidade
        por si só.{w} Mas os hóspedes...{w} meus hóspedes, o que eles fizeram?"

        asterion "Eu teria suportado tudo de novo uma dúzia de vezes se isso
        significasse que eles teriam um lar.{w} Porque então, pelo menos,
        eu poderia descansar sabendo que minha dor era por alguma coisa."

    asterion "..."

    $Asterion.change ("emotion", "sad")

    asterion "..."

    $Asterion.change ("emotion", "bowing")
    $Asterion.change ("rightarm", "loose")
    $Asterion.change ("leftarm", "raised")

    asterion "Sinto muito. Eu esqueço meu lugar quando bebo, Mestre. Isto não
    acontecerá novamente. Foi terrivelmente inadequado."

    you "Mas está tudo bem. Eu te dei permissão para falar livremente comigo,
    não dei? E eu falei sério."

    $Asterion.change ("emotion", "sad")

    you "Se você estivesse me incomodando, eu já teria dito para parar. Então você pode
    relaxar. Acho que eu quero aprender mais sobre o que você passou."

    asterion "..."
    if Chapter4_Terrorized_Asterion == "False":

        asterion "Eu posso apenas presumir que os tempos mudaram. Você não é como os outros
        Mestres. Eu já teria sido posto em meu lugar por causa dessa insolência a essa altura."

    $Asterion.change ("leftarm", "loose")

    asterion "...Eu continuo pensando que tudo isso vai acabar a qualquer momento agora, e que eu
    acordarei naquela câmara outra vez."

    asterion "..."

    "O olhar de Astério vagueia -- e parece que apenas agora ele percebe a vasta mudança
    no salão."

    "O Hotel está vivo de novo."

    you "Mas não é um sonho. Você vai ver. Pode demorar um pouco para você acreditar
    em mim, mas é verdade."

    you "E eu falei sério. Eu quero ser um bom mestre para o Hotel --
    e para {i}você.{/i}"

    if Chapter4_Terrorized_Asterion == "True":
        "O minotauro suspira e desvia o olhar."

    else:
        "O olho de Astério desvia para o lado, depois volta para você. O minotauro morde os lábios."

        "O menor dos suspiros escapa de seus lábios, seguido por ele fechando o olho.
        A lateral de seu rosto faz dobras."

    #"Asterion’s smile lights up his newly healed face."

    $Asterion.change ("emotion", "bowing")

    "Ele está prestes a dizer algo. Seu rosto fica frio em uma solenidade quase profissional,
    mas ele se impede novamente."

    $Asterion.change ("emotion", "sad")

    "Ele olha para você uma última vez."

    $Asterion.change ("emotion", "neutral")

    asterion "Estou certo de que o Mestre será..."

    asterion "..."

    if Chapter4_Terrorized_Asterion == "True":
        "Seus lábios tremem, seu olho se estreita."
        pause 1.0
        $Asterion.change ("emotion", "angry")

        pause 3.0

        "As narinas de Astério dilatam quando ele inspira..."
        pause 1.0
        $Asterion.change ("emotion", "neutral")
        "...e expira."

        "Seu olhar retorna, frio como gelo."

        $Asterion.change("leftarm", "raised")

        asterion "É claro, Mestre.{w} É claro que você quer."

        pause 0.5

        $Asterion.change ("emotion", "angry")

        pause 1.0

        asterion "Vida longa ao grande senhor do Hotel."

        asterion "Poderia {w=0.2}este servo{w=0.2} persuadi-lo a desfrutar de uma bebida?"

        scene bg black
        with Dissolve (3)
    else:
        "Os lábios dele tremem por um momento antes de um sorriso aparecer em seu rosto."

        "Sua voz sai distorcida. A curva de seu sorriso dá a suas palavras um toque
        caloroso, mas suas palavras saem abaladas. Sua voz falha e o minotauro
        enuncia vagarosamente."

        "Há também um fundo de ansiedade à medida que seu olho move de um lado para o outro."

        $Asterion.change ("emotion", "smiling")

        asterion "Fico feliz que, de todas as pessoas que existem, {i}você{/i}
        esteja aqui, Mestre %(player_name)s."

        $Asterion.change ("emotion", "tired")

        "Ele olha para baixo, e então de volta para você. Algo parece piscar em frente a seu olho,
        o que tira sua atenção. Ele mergulha em pensamentos..."

        "E é como se ele estivesse fantasiando sobre uma ideia. Seja lá o que for que toma conta de sua
        mente, parece esperançoso."

        $Asterion.change ("emotion", "neutral")

        "Ele morde os lábios em desejo, e continua a se perder em querer acreditar."

        $Asterion.change ("emotion", "smiling")

        "O sorriso conquista o rosto primeiro e depois se espalha para todo o corpo."

        $Asterion.change ("rightarm", "hips")

        "Desta vez sua voz sai mais firme em meio ao sorriso."

        asterion "Então eu repito meus votos. Se você está determinado a cuidar do Hotel
        e seus hóspedes, e cumprir sua missão determinada pelo homem, então eu irei servi-lo por minha
        própria vontade."

        asterion "Será um prazer servi-lo, Mestre %(player_name)s."

        asterion "Há muitas coisas sobre as quais deveríamos... sobre as quais eu gostaria
        de conversar com você. Poderia eu persuadi-lo a desfrutar de uma bebida?"

        scene bg black
        with Dissolve (3)

    jump chapter6
