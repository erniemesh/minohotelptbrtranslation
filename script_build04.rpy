label build04:
    $build=4
    $new_build_update()
    $obtain_reward('Build3', 'RD', subtract=False)

    if guests.get_guest_status('Asterion') == 'unavailable':
        $guests.free_guest('Asterion')

    #throwaway1 is true if asterion was wearing the vneck so if we restore it into
    #a sleeveless shirt keep that in mind
    #if Build3Ending == 'bad' -> then the greta internet scene may not have happened.
    #we can either add it here or just carry on the ruthless route with no internet.

    if Build3Ending == 'bad':
        jump ruthlessEnding

    $chapter = "Capítulo 13"

    call screen ChapterTransition("Capítulo 13", "Estrelinhas")
    pause 0.5
    $save_name=output_save_name("Capítulo 13")

    $LoungeBlobs =[True, 2]

    scene Lounge
    show Asterion:
        yalign 1.1 zoom 0.85 xalign 0.75 xzoom -1

    play music "music/Lullaby.ogg" fadeout 1.0 fadein 1.0

    if first_guest == "Luke":
        show LoungeLight
    with Dissolve(3.0)

    $Asterion.change('emotion', 'contemplative')

    "Uma noite esbravece e saúda apenas por um breve momento, o tempo sempre cobra seu preço."

    "Ainda assim, eles não sentiram dor alguma. Dançaram e beberam, riram e cantaram até
    suas vozes ficarem roucas e os olhos turvos."

    "E continuaram celebrando, como se de alguma forma uma vitória pudesse tornar-se eterna
    caso brilhasse o suficiente."

    "Sentado na periferia do salão, cercado pela humanidade, mas
    preso dentro de sua mente, o minotauro perdeu-se em pensamentos."

    $Asterion.change('emotion', 'relieved')

    "Uma coisa tão humana. Será que os hóspedes e o mestre talvez o conheçam, o
    ritual arcaico ensinado por seu velho amigo?"

    "Celebre e viva por uma noite inteira, não cesse até que suas costas queimem todo
    o combustível e, sob nenhuma circunstância, permita que a fogueira se apague;"

    "Em seguida, pegue um punhado de brasas, acinzentadas e esfarelando por fora,
    mas ainda abrigando um coração vermelho. Despeje um fio líquido de seu melhor vinho, reservado das
    festividades, para apagar o fogo da noite."

    show blackback behind Asterion:
        alpha 0.7
    with Dissolve(3)

    "O velho Froneu jurou que ouviu sobre ele sem querer durante a iniciação de uma sacerdotisa quando
    ela foi instruída sobre os mistérios da antiga deusa de Creta."

    "Aquele ritual, ele disse, poderia fazer um momento tornar-se eterno. Deixaria os daemones
    para trás — uma memória da noite gravada na terra e alojada na mente de suas testemunhas."

    "Ele disse que o último fio de fumaça da brasa seria recolhido pelas Orações, pelas
    filhas de Zeus, e levado às Graças, ou aos Destinos, ou às Horas, para sua tecelagem."

    $Asterion.change('emotion', 'tired')

    "Quanto mais ele explicava, mais solta sua concepção da cerimônia se tornava."

    $Asterion.change('emotion', 'relieved')

    "Que tola bobagem, Astério pensou, quando em Creta. Ele está dizendo isso apenas para me animar novamente."

    "Mas o minotauro realmente roubou uma taça do vinho de seu pai e, juntos, eles afogaram
    as brasas, coletado da bacia no pátio onde a fogueira havia se enfurecido."

    "Ele nunca acreditou que tal ritual pudesse funcionar. Ele mesmo conhecia vários mistérios
    e nenhum era tão simples e inocente como aquele."

    "Mesmo em seus momentos mais gentis, os deuses antigos cobravam em sangue."

    "Mas ainda assim ele o fez porque, independentemente dos deuses, tornava as
    noites inesquecíveis em sua mente."

    "Às vezes, a crença bruta, desprovida de qualquer forma de magia vinculativa, é o suficiente para tornar algo verdadeiro."

    "Isso foi há muito tempo. Ele testemunhou tantas festividades em todos esses séculos como zelador do hotel."

    "Cada uma o atraiu para mais perto de acreditar que o ritual de Froneu era
    meramente uma manifestação do desejo da humanidade de encontrar a imortalidade."

    "É apenas humano buscar a eternidade. A primorosa mentira de que o fluxo do tempo
    pode ser interrompido, prendendo este alguém em uma bolha que nenhuma tragédia pode estourar."

    "Froneu desejava esta benção em Creta, milhares de anos atrás, e a humanidade ainda anseia por ela."

    "Acreditar em rituais tão antigos, de uma época na qual os próprios deuses desapareceram...
    Tola bobagem, branda indulgência."

    hide Asterion
    with Dissolve(0.5)

    scene bg asterionbed
    $Asterion.change('emotion', 'tired')
    $Asterion.getNude()
    $Asterion.change('underwear', 'loincloth')
    show Asterion:
        yalign 1.0 zoom 1.0 xalign 0.5 xzoom 1
    show blackback:
        alpha 0.7
    with Dissolve(2)

    "Mesmo assim, naquela noite após o concerto, o minotauro foi para a cama com as mãos cobertas de cinzas."

    "Que momentos maravilhosos eles passaram juntos... O cansaço da situação o estava dominando."

    show Asterion:
        ease 2.0 yalign 3.3 xalign 0.8
    "Uma tensão em seu peito fez o quarto girar ao seu redor. As pontas de seus dedos estavam congelando."

    "Ele não percebeu quando aconteceu, mas uma única respiração profunda tornou-se uma tarefa trabalhosa."

    $Asterion.change('emotion', 'sad')

    "Astério sabia disso muito bem. O tempo, afinal, cobra seu preço e, para cada alegria,
    uma dor maior certamente virá. {w=2}Ele respirou fundo."

    "Para um prisioneiro como ele, a felicidade não era permitida. Sua mente o dizia isto mesmo
    enquanto ele lembrava da alegria da noite. {w=2}Ele respirou fundo."

    "Ele esqueceu que tinha a intenção de dormir; esqueceu de fechar os olhos. O minotauro
    encarava o teto enquanto os pensamentos transformavam-se em noções e o aperto
    em seu peito tornava-se um peso em seus ombros e uma tensão em suas mãos."

    "Ele respirou fundo. {w=2}Um preço deve ser pago. Sempre há uma pegadinha."

    "Os lençóis ao redor dele amontoaram-se em vales e picos. A inquietação lutou
    contra o cansaço. {w=2}Ele respirou fundo."

    show blackback:
        ease 1.0 alpha 0.85

    "Um sono agitado o dominou ao mesmo tempo em que ele se sentia pesado demais para se mover, um taciturno cansaço
    em sua mente, mais profundo que o sono, o puxou para o vale de seus lençóis."

    "Sussurros sobre sua natureza — palavras que ele não se permitiu reproduzir por quase um século agora."

    if Build3Ending == 'neutral':

        "Mesmo assim, ele se lembrava das brasas e do vinho de vez em quando. Ele poderia
        se forçar a lembrar das coisas boas, porém, sua mente as fazia de notas de rodapé."

    if Build3Ending == 'good':
        "Mas outra memória vibrava, aquela do abraço de [player_name]."

        "O nariz do minotauro em sua cabeça, aquele calor tranquilizante que eles compartilharam."

        "Mesmo isto, no entanto, está coberto com as preocupações de...{w}
        Ele deveria, ele tinha o direito...{w=0.2} Cedo demais ou repentinamente, de ultrapassar os limites?"

        "Ele, sempre indesejado, agora..."

    scene bg black
    with Dissolve(2)

    pause 2.0

    scene bg asterionbed
    $Asterion.change('emotion', 'sad')
    show Asterion:
        yalign 6.3 xalign 0.8 xzoom -1
    with Dissolve(0.5)

    "A manhã abriu seu crânio, mas nenhum sonho bateu em retirada."

    "O quarto parecia o mesmo de sempre — tão apertado que ameaçava
    esmagá-lo, paredes tão brancas que queimavam seus olhos e prateleiras
    decoradas com as esculturas de olhos esbugalhados de Jean-Marie."

    $Asterion.change('emotion', 'tired')

    "Ele se lembrou de respirar, depois mordeu sua língua. A dor veio sem pressa, maçante e latejante."

    "Mas os olhos do minotauro tinham uma sensação diferente, como se durante a noite tivessem pulado o outono e mergulhado no inverno."

    "Se a mente fosse um músculo, a dele estaria mancando por aí, doendo de tanto uso."

    "Astério disse a si mesmo para olhar na direção da porta, mas não o fez. Olhou para cima,
    disse a si mesmo para olhar na direção do batente da porta."

    "\"Lembre-se de respirar,\" rezou o híbrido. Ele respirou fundo. Disse a si mesmo
    para levantar, mas não o fez. Ele fechou as mãos, sentiu as unhas cravando-se na palma."

    "Havia pedaços de obisidiana amarrados a seus membros, cintura, olhos — até mesmo cada dobra
    de seu cérebro estava sendo puxada para baixo por ganchos."

    "Se os deuses tivessem enviado a ele um pingo de misericórdia, tal peso poderia tê-lo esmagado
    completamente e acabado com sua existência. Mas eles o fizeram forte e resiliente para suportar o peso."

    "Este vassalo não foi feito para quebrar, ele sabia, mesmo que as criaturas deste domínio
    estivessem tão ansiosas para tentar. O único movimento realizado quando ele finalmente
    direcionou os olhos para o lado foi um abrir e fechar de mãos sem objetivo."

    "Em muitas vezes ao longo de sua existência eterna, o espírito de Astério sentiu-se
    esvaziado de vigor ou substância como agora."

    "Pelo menos algumas vezes por ano nos últimos dois milênios, sem
    falta, embora o tempo tenha se tornado mais inconsistente dentro da câmara fria."

    "Mas nem sempre foi o caso. Ele não podia se permitir tal branda indulgência quando os monstros o perseguiam."

    "Talvez tenha sido uma brincadeira dos próprios deuses.{w} Ele se lembrou de respirar.{w}
    Quando chegou um humano em busca de encerrar suas provações, mais uma punição veio,
    desta vez de sua própria mente."

    pause 2.0
    $Asterion.change('emotion', 'mooing')
    pause 1.0

    $Asterion.change('emotion', 'tired')
    "Mas chega de demora, estrelinha. Independente disso, você deve se levantar novamente."

    show Asterion:
        ease 3.0 xalign 0.5 yalign 2.0

    "Há um atraso entre ordenar que seu corpo se mova e fazer com que ele reúna a
    vontade de obedecer. Ele se empurra para cima com a falta de jeito de uma marionete,
    lutando contra uma inércia em seu cérebro."

    show Asterion:
        ease 1.0 yalign 2.3
        ease 1.0 yalign 2.0
        repeat

    "Há um pouco de espaço para respirar entre o movimento de cada membro para
    levantar-se, como se toda a força adquirida em uma noite de sono fosse necessária."

    hide Asterion
    with Dissolve(0.4)
    scene bg black
    $Asterion.change('emotion', 'sad')
    show bg asterionbed:
        xzoom -1
    show Asterion:
        xalign 0.5 xzoom 1 yalign -0.5 zoom 1.3
    show image "cg/cg6_mirror.png"
    with Dissolve(1.0)

    "Ele encara o espelho."

    asterion "Bem-vindo de volta ao seu antigo eu, estrelinha."

    play music "music/GreekFolkSong.ogg" fadein 1.0 fadeout 1.0

    pause 1

    scene bg black
    show Asterion:
        xalign 0.5 xzoom 1 yalign -0.5 zoom 1.3
    show image "images/Asterion/clothing_front_vneck_[player_background].webp":
        xalign 0.5 xzoom 1 yalign -0.5 zoom 1.3
    show backtitle:
        alpha 0.8
    show image "CG6Tablet"
    with Dissolve(2)

    pause 1

    hide image "images/Asterion/clothing_front_vneck_[player_background].webp"
    $Asterion.change('clothes', 'vneck')
    $Asterion.change('underwear', 'jeans')

    you "Você está pronto para ver a Internet?"

    "Testemunhar a última criação da engenhosidade humana."

    "Eles nunca pararam, esses humanos perspicazes. Que criações complexas seus formidáveis dedos produzem."

    "Astério olhou para sua própria mão, para as proeminentes articulações e unhas grossas.
    Cada nó de articulação amarrado com uma corda áspera e irregular."

    asterion "Sim, é claro."

    you "Ótimo.{w=0.2} {i}Isso{/i} é um tablet, é um tipo de computador que usa controles de toque."

    you "...Com isso eu quero dizer que você só precisa tocar na tela, é bem intuitivo."

    asterion "Está... Eu não consigo ver nada, estou fazendo errado?"

    you "Não, está tudo bem, ainda não desbloqueei."

    you "Aqui, basta pressionar esse botão e..."
    play sound "sfx/itemget.ogg"
    show image "images/cg/cg6_screen.png" behind backtitle
    hide backtitle
    with Dissolve (0.5)

    you "Tomei a liberdade de configurar. Sabendo que você tem dificuldade com
    movimentos delicados, tive certeza de deixar as coisas grandes e fáceis de tocar."

    you "Você acha que eles estão grandes o suficiente? Posso expandir os ícones ainda mais se você quiser."

    asterion "Obrigado, senhor. Está adequado."

    scene bg oldquarters
    show Asterion:
        xalign 0.5 yalign 1.0 xzoom 1 zoom 1
    $Asterion.change ("emotion", "tired")
    with Dissolve (1.0)
    pause 1.0

    asterion "No entanto... Espero não ter imposto uma tarefa a você. \"Configurar\" foi difícil?"

    you "De forma alguma, todos os tablets vêm com configurações de acessibilidade. Adaptá-lo às
    suas necessidades é uma questão trivial."

    "\"Acessibilidade.\" Apenas humanos poderiam imaginar tal coisa. Os deuses não amavam
    nem se importavam com Hefesto e suas imperfeições."

    $Asterion.change ("emotion", "relieved")

    asterion "Ah. É muito gentil da parte deles pensarem nos desgraçadamente descoordenados como eu."

    "O homem olha para baixo na direção do híbrido."

    "Astério encara seus olhos. Ele nunca entendeu por que as pessoas
    tinham tanto fascínio pela cor da íris umas das outras; para ele, o branco
    em torno delas era muito mais cativante."

    "A natureza foi gentil com ele neste aspecto, pelo menos. Ao invés da escuridão dos
    olhos de uma vaca, ele foi abençoado com um belo par de olhos
    bastante humanos, brancos e tudo."

    "Talvez fosse algo na maneira como os olhos de [player_name] hesitavam enquanto ele
    procurava por palavras. Ou talvez fosse o cérebro do minotauro escorregando por um segundo."

    $Asterion.change ("emotion", "tired")

    "Mas antes que [player_name] pudesse falar, o minotauro sentiu alguns séculos de idade
    erguendo-se de suas costas."

    you "Eu não diria assim. Muitas pessoas têm deficiências ou necessidades especiais e,
    independentemente disso, todo mundo envelhece um dia. Todos nós vamos precisar da ajuda."

    "Ele pensou um pouco. O tom era gentil, o mestre falou quase como se estivesse cantando.
    Mas, à medida que as palavras eram costuradas, tornavam-se espinhosas."

    $Asterion.change ("emotion", "sad")

    "Astério mordeu a língua. Ele era velho — ou, talvez, velho no mesmo sentido em que um humano poderia ser?"

    "Seu corpo estava no melhor estado dos últimos oitenta anos, mas todo aquele tempo passado
    na câmara fria nunca o deixou tão cansado quanto agora."

    "Era o tipo de exaustão que tornava até mesmo abrir os olhos uma tarefa intransponível."

    "Velho ou aleijado, o minotauro precisava desta invenção de \"acessibilidade\"."

    $Asterion.change ("emotion", "tired")

    asterion "Eu tenho necessidades especiais ou sou apenas velho?"

    "Astério resmungou. Sua língua parecia inchada hoje, ele teve que cerrar os dentes para
    impedir que saísse de sua boca. O Mestre não conseguiu distinguir o que ele disse."

    you "Desculpa, o que você disse?"

    pause 2.0

    $Asterion.change ("emotion", "mooing")

    asterion "Muu."

    $Asterion.change ("emotion", "tired")

    "Os olhos do Mestre o examinam. Eles apreciam cada característica de seu rosto,
    como se estivessem tentando vislumbrar a mente do minotauro."

    "Seu coração bate forte. Ele vai perceber como Astério pode ser um brinquedo descartável?"

    "O híbrido não consegue dizer o que virá a seguir, mas deve ser melhor que esta sensação
    de estar suspenso e aguardando julgamento."

    you "Você está se sentindo bem, Astério? Parece um pouco angustiado hoje."

    stop music fadeout 2.0
    show blackback behind Asterion:
        alpha 0.5
    with Dissolve(2)

    "Astério desvia o olhar e respira fundo. Seu peito aperta e ele abre a boca —
    a deixa pendurada, na verdade, pois o que ele queria dizer lhe escapa."

    "Ele pisca, deixa suas pálpebras caírem conforme exala. É tão difícil pensar com todos aqueles ganchos em seu cérebro."

    "Ele precisa amarrar junto cada palavra, e então dividir tudo em movimentos
    bucais, respirações, olhares e gestos com as mãos."

    "E lá está o atraso, tornando tudo pior. Uma lacuna tão profunda e escura quanto o oceano."

    $Asterion.change ("emotion", "mooing")

    "Mas quando ele fecha os olhos e se permite sonhar, imagens fluem como a água de uma nascente."

    show blackback:
        ease 2.0 alpha 0.9

    if Build3Ending == 'good':

        "Dava para sentir o calor do Mestre ontem à noite. Abraçá-lo não era a prova que o minotauro
        esperava — sua mente ficou em silêncio enquanto eles permaneceram trancados um ao outro no escuro."

        "Astério esfregou seu nariz no topo da cabeça de [player_name]. Ele não recuou."

        "Enquanto durou, Astério não pensou no quão desajeitadas suas mãos poderiam estar,
        com todos os dedos fechados. Deixou de ser uma garra descoordenada, tornou-se apenas uma mão."

        "Quando ele reajustou suas pernas, nem ouviu o {i}clop{/i} de seus cascos.
        Todos os ruídos corroendo nos arredores se acalmaram, abafados pelo veludo."

    if Build3Ending == 'good':

        "O Mestre foi generoso. Ele caminhou grandes distâncias para conseguir o vinho — e o que ele ganhou com isto?"

        "Astério morde a língua. Talvez um pouco mais de confiança seja a justificativa."

    "O minotauro abriu a boca e respirou fundo. As imagens brotaram e as palavras
    acorrentaram a si mesmas."

    "Pelos deuses, eu deveria contar para ele que parece como se eu estivesse virando pedra. [player_name]
    deve saber o que significa e o que eu deveria fazer."

    you "Asterion?"

    "Mas deve haver uma pegadinha com ele. Sempre tem uma."

    you "Você está bem?"

    "Mas, de qualquer forma, ele não é cruel. Se é para servi-lo e cumprir bem este dever,
    talvez ele saiba como eu posso melhorar."

    "Eu deveria contá-lo..."

    show Asterion:
        ease 1.0 yalign 1.05 zoom 1.05

    "Uma mão aquece o antebraço do minotauro."

    $Asterion.change ("emotion", "tired")

    play music "music/GreekFolkSong.ogg" fadeout 1.0 fadein 1.0

    hide blackback
    with Dissolve (1.0)

    you "Você não parece muito bem."

    "O minotauro olha para o humano. Seus olhos estão imóveis — sem medo ou tristeza,
    mas olhando através do Mestre, como se tentar focar em seu rosto fosse uma ação muito difícil."

    "O minotauro respira fundo e fala antes que uma parte mais gentil de sua mente possa assumir o controle."

    $Asterion.change ("emotion", "relieved")

    asterion "Estou apenas tendo dificuldade para acordar."

    you "Ah. É verdade, ainda não comemos nada. Que tal eu te ensinar um pouco do
    básico e depois descer para pegar as sobras da noite passada? Escondi alguns
    dos aperitivos na geladeira do salão."

    $Asterion.change ("emotion", "tired")

    "Astério grunhe — sem ouvir de verdade, apenas reafirmando sua vaga e sempre
    presente concordância com tudo o que o Mestre tem a dizer."

    you "Ok. Então, só recapitulando... Com um computador nós podemos acessar \"a Internet\"
    e encontrar todo tipo de coisas legais. Você lembra o que é a Internet?"

    $Asterion.change ("emotion", "contemplative")

    "Uma pergunta. Os olhos de Astério mudam de posição. A Internet."

    $Asterion.change ("emotion", "tired")
    if player_background == 'tech':

        "Sim. Ele anotou sobre isto, não foi? Ele ordenou que seu braço movesse em direção
        às suas pernas e, em seguida, que seus dedos se alinhassem para que ele pudesse colocar a mão no bolso."

        "Ele puxou aquele pedaço de papel. E então abriu a mão, pegou o papel, o desdobrou."

        asterion "S-sim, é claro."

        $Asterion.change ("emotion", "mooing")
        asterion "\"A internet é uma rede de redes operando sob um conjunto de
        protocolos abertos e públicos através de cabos, satélites, rádio e muitas
        outras tecnologias de comunicação."

    else:
        "Sim. Puxe a corda, puxe as palavras de sua mente e fale."

        asterion "É uma maneira de, hum...{w=0.2} é uma maneira de obter conhecimento muito rapidamente."

        $Asterion.change ("emotion", "mooing")
        asterion "Demoraria meses para um livro ou carta serem entregues, mas
        com a Internet não demorará muito."

    $Asterion.change ("emotion", "tired")

    pause 2.0

    $Asterion.change ("emotion", "neutral")

    asterion "Eu entendi corretamente?"

    you "Sim! Vamos começar, então. Agora eu quero que você toque naquele ícone no canto
    superior esquerdo, pode fazer isso para mim?"

    $Asterion.change ("emotion", "contemplative")

    asterion "Basta... basta tocá-lo? Com um dedo?"

    you "Isso mesmo. Sem mistério, só tocar."

    asterion "Ok... Assim?"

    $Asterion.change ("emotion", "surprise")
    show Asterion:
        ease 0.5 yalign 1.0 zoom 1.0
    play sound "sfx/click.ogg"

    pause 2.0

    $Asterion.change ("emotion", "neutral")

    you "Então, o que você quer procurar primeiro?"

    $Asterion.change ("emotion", "relieved")

    asterion "Eu não sei... C-como posso contar para isto o que quero saber?"

    you "Basta tocar aqui, nessa pequena barra branca... E agora o teclado vai aparecer..."

    pause 1.0

    $Asterion.change ("emotion", "sad")

    asterion "Esses símbolos... Eles são normais?"

    you "Como assim? O teclado tem que mostrar o alfabeto, não é nada fora do comum."

    $Asterion.change ("emotion", "tired")

    asterion "Ah... Ah não, eu acho que quebrei."

    you "O que? De jeito nenhum, você não fez nada de errado..."

    scene blackback
    show image "images/cg/cg6_browser.png"
    show image "CG6Tablet"
    with Dissolve(1.0)

    asterion "Eu... Meu dedo é ruim? Eu toquei errado?"

    you "A tela parece normal para mim."

    "O minotauro olha para a tela, tentando fazer sentido de todos os símbolos.
    Que linhas estranhas eles são... Mas realmente despertam um senso de familiaridade."

    "Seu cérebro coça enquanto luta para conectar uma mente antiga a conhecimentos mais recentes."

    "Suas orelhas sacodem. Ele ouve um barulho de mecanismos fazendo tique-taque e
    soltando ruídos no alicerce apertado."

    "Estava vindo para ele. O nome de uma máquina, um escritor... Uma \"máquina de escrever.\""

    "Elas tinham sido um grande problema. As letras em si não tinham significado, nenhuma
    alma por trás delas. A tradução do hotel não podia fazer nada para impor a ordem."

    "Durante todos os milênios, o minotauro falara a língua de seu povo,
    sem se importar em aprender qualquer nova língua que fosse moda na época."

    "Embora, para ser mais preciso, por alguns séculos ele tinha adquirido o hábito
    de fazer novas palavras, tanto que seu velho Minóico tornou-se
    bastante diferente do que ele falava quando criança."

    "Mas tudo mudou quando as máquinas de escrever foram inventadas. As letras sozinhas o frustraram."

    "Ele teve que aprender outras línguas e alfabetos na época."

    asterion "Ah, isto é uma máquina de escrever. O hotel não gosta delas."

    you "Hã. Por que isso?"

    asterion "Ele só entende significado e palavras, não do que elas são feitas. Tudo desmorona."

    you "Ah. Existe algo que eu possa fazer, então? Eu posso ler e digitar para você, não seria um problema."

    "Ele respirou fundo. Quanto mais ele olhava para o alfabeto — quão parecido
    era ao que os gregos inventaram — menos ele sentia os ganchos em seu cérebro."

    asterion "Eu consigo lembrar das letras. Das palavras também."

    "Ele tocou na tela. Tinha a intenção de pressionar o \"O\", mas tocou no \"P\" em vez disso."

    "Um velho aborrecimento. Dias mais simples voltaram à sua mente, quando Jean-Marie ainda
    estava vivo e eles estavam redigindo contratos no alicerce."

    "Ele nunca dominou a máquina de escrever. Mas a utilizava de forma decente o suficiente — lentamente."

    "Ele poderia conquistá-la novamente."

    asterion "Eu posso encarar isto."

    "[player_name] continua olhando para o minotauro. Seria isto uma pontada de preocupação?"

    "E então suaviza. Sua voz, assim que sai, soa como veludo."

    you "É claro que você pode. Você manteve este hotel funcionando por tanto tempo, memorizar um
    alfabeto não vai ser difícil para você."

    scene bg oldquarters
    $Asterion.change ("emotion", "neutral")
    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve(1.0)


    asterion "Desculpe, o que disse?"

    you "Você manteve esse lugar em pé e funcionando, certo? Mestres iam e vinham, mas
    você foi a constante. Você é muito competente e trabalhador, isso é claro para mim."

    $Asterion.change ("emotion", "tired")

    "Trabalhador. Os deuses o {i}fizeram{/i} forte para ser capaz de carregar uma carga que nenhum homem normal poderia."

    "Ele era uma besta de carga. Sim, Astério poderia se orgulhar disto."

    you "Você lida com os hóspedes, administra as entradas e saídas, conserta os quartos,
    até cozinha se necessário. E ontem à noite você foi tão longe a ponto de entreter."

    you "Acabamos de reabrir o hotel e ele já está indo tão bem, em grande parte graças a você."

    you "Memorizar um alfabeto é uma tarefa difícil para alguém tão perspicaz como você?"

    $Asterion.change ("emotion", "relieved")

    "O hotel está indo bem, pensou o minotauro."

    "Em qualquer outro contexto, pensamentos amargos surgiriam em sua mente — não,
    o hotel ainda é um fragmento do que costumava ser, estamos hospedando apenas
    uma ou duas dúzias de hóspedes, quase não temos funcionários."

    "Mas quando se tratava deste assunto, sua mente desanuviava..."

    $Asterion.change ("emotion", "contemplative")

    "Sim, o hotel estava indo bem. Consertar um lugar tão grande em menos de duas
    semanas foi quase um milagre."

    "Os hóspedes chegando agora nem imaginam que o lugar ficou em ruínas por oitenta anos."

    "Era sua única coisa boa. A cada violência e desgraça que os deuses consideraram
    adequado impor a ele, bênçãos para sua casa vinham em dobro."

    "Ele serviria bem se isto significasse a prosperidade de sua única coisa boa."

    $Asterion.change ("emotion", "determined")

    asterion "Eu tenho orgulho do hotel."

    "A voz do minotauro retumbou, seguida por um áspero bufo e sacudir de suas orelhas."

    you "Como você bem deveria."

    $Asterion.change ("emotion", "contemplative")

    asterion "Isto é uma ordem?"

    you "Considere como uma sugestão de um amigo, e recomendação de um parceiro."

    $Asterion.change ("emotion", "contemplative")

    asterion "Parceiro?"

    pause 1.0
    $renpy.music.set_volume(0.2, delay=1, channel='music')

    show blackback behind Asterion:
        alpha 0.6
    with Dissolve (1)

    $Asterion.change ("emotion", "tired")

    pause 1

    "Parceiro. Que palavra peculiar."

    "Astério olhou para o lado. Ele precisou amarrar cada comando junto —
    ele podia sentir seus globos oculares arrastando dentro de suas cavidades."

    "Ele respirou fundo e, em seguida, cravou as unhas nas palmas das mãos."

    "Parceiro. Froneu costumava chamá-lo assim em Creta, até aquela noite."

    "Um pássaro branco voando sob a luz do luar. O minotauro mirou seu arco
    e puxou a corda. Não era muito diferente de tocar sua lira.
    Aquela última tensão antes de soltar."

    "Para Froneu, para aquele eterno amigo, mas antes de tudo por seu irmão,
    o intrépido Androgeu, ele disparou a flecha."

    "Parceiro. Eles estavam caçando juntos naquela noite. Mas, no final, Froneu
    o chamou de outra coisa. E esta foi a última vez que eles se viram."

    $renpy.music.set_volume(1.0, delay=1, channel='music')
    hide blackback
    with Dissolve(1)

    "Mas às vezes parecia que este Mestre era o espírito de Froneu, ou Androgeu encarnado.
    Todos eles tinham línguas tão doces..."

    you "Nós {i}somos{/i} parceiros de negócios, não somos? Estamos nessa juntos."

    $Asterion.change ("emotion", "neutral")

    "Astério retornou de seu devaneio."

    asterion "Receio que não seja algo que o hotel, ou o vale, estariam dispostos a reconhecer."

    asterion "Minha sentença, afinal... Contratos que se afastem muito de me tratar como
    prisioneiro seriam ineficazes."

    you "O que você quer dizer com isso, exatamente?"

    asterion "O Mestre pode ordenar o domínio a realizar sua vontade, mas há regras
    e princípios que estão acima."

    asterion "Se você tenta passar um contrato ou comando que os desconsidere, sua
    ordem não será realizada."

    asterion "Da mesma forma que você não pode invocar dinheiro, você não pode assinar um contrato
    dizendo que sou {i}igual a você.{/i} Isto iria contra os princípios do labirinto."

    $Asterion.change ("emotion", "tired")

    asterion "Então... Eu não posso ser seu parceiro de negócios. No que diz respeito ao labirinto,
    isto simplesmente não é possível."

    "[player_name] olha para o lado, perdido em pensamentos."

    menu:
        "\"Poderia haver uma brecha?\"":
            you "Quem sabe, talvez eu consiga encontrar um jeito de contornar isso.
            Acho que estou pegando o jeito sobre como esse domínio funciona."

            you "Poderíamos tentar encontrar uma brecha que podemos usar para alcançar o mesmo efeito."

            you "Talvez algo no sentido de proibir o mestre de fazer mal a você."

        "\"Realmente precisamos de um contrato para isso?\"":

            you "Bem, isso é um baita enigma..."

            you "Mas realmente importa o que o labirinto pensa ou quer?"

            you "Se eu digo às pessoas que você é meu parceiro, e objetivamente é assim
            que trabalhamos juntos... Isso não {i}faz{/i} de nós parceiros?"

    "Que ideias absurdas. O minotauro sente os beija-flores bicando na parte de trás de seu crânio.
    Ele range os dentes e [player_name] percebe."

    you "Mas parece que nos desviamos do assunto, eu deveria te mostrar a Internet."

    $Asterion.change ("emotion", "neutral")

    asterion "Sim, senhor."

    you "Então, toque aqui... Podemos começar com algumas pesquisas. Tenho certeza que existe muita
    coisa que você quer saber sobre o mundo exterior."

    "Mais uma vez, o alfabeto peculiar apareceu na tela — desta vez, no entanto, foi
    transformado em palavras teimosas que não se curvaram à tradução do domínio."

    "Mas elas não eram desconhecidas. A memória despertou. Cordas soltas amarradas em nós."

    $Asterion.change ("emotion", "tired")

    asterion "A tradução do hotel não está funcionando."

    you "Isso é estranho, eu consigo ler normalmente... Mas acho que é porque
    eu já falo português, não notaria nada de errado."

    you "Isso é um problema?"

    $Asterion.change ("emotion", "relieved")

    asterion "Português? Não, consigo ler nesta língua... aprendi depois que começamos a usar máquinas
    de escrever... apenas precisarei de um minuto para me familiarizar."

    you "Sim... Que língua você tem falado até agora?"

    $Asterion.change ("emotion", "neutral")

    asterion "Minha língua."

    pause 1.0

    you "Como assim?"

    $Asterion.change ("emotion", "contemplative")

    asterion "É... É {i}minha{/i} língua. Era cretense, costumava ser,
    mas com o tempo eu simplesmente... Se tudo é traduzido, então eu poderia consertá-la e torná-la minha."

    asterion "Eu tinha dificuldade com certos sons. Então, simplesmente a mudei, deixava de um jeito que parecesse certo."

    asterion "Então... Costumava ser minóico, mas não é mais. É minha língua."

    pause 1.0
    $renpy.music.set_volume(0.2, delay=1, channel='music')

    show blackback behind Asterion:
        alpha 0.6
    with Dissolve (1)

    $Asterion.change ("emotion", "neutral")

    pause 1

    "Minha língua. Lábios ásperos de touro curvados em ângulos estranhos, uma língua muito longa e grossa."

    "Durante o dia, sua ama-de-leite ensinava-lhe as palavras, repetindo cada uma cem vezes.
    Um príncipe deve falar bem, ela dizia."

    "A cada duas semanas, sua mãe passava uma noite com ele. Os olhos dela vagavam,
    rastejavam até o teto, e suas pequenas mãos de pulsos moles agarravam o ar como as de um bebê."

    "Ela falava como se sua boca estivesse cheia de seixos. Suas sílabas
    borravam juntas. As vogais tartamudeavam e eram lavadas por seu sotaque."

    "Papai disse que era a loucura dela falando. A ama de leite disse que ela veio de um lugar
    sagrado além do mar e esse era seu sotaque."

    "Astério saboreou cada precioso momento com sua mãe. Incluindo sua música arrastada."

    "Ele nunca poderia dizer se seu sotaque vinha de sua forma bestial ou da influência dela."

    "Mas aqui no labirinto ele o deixou ir embora. Pegou pedaços de pessoas ao longo
    dos séculos. Costurou algo áspero, feito de trapos e perfeito."

    $renpy.music.set_volume(1.0, delay=1, channel='music')
    hide blackback
    with Dissolve(1)

    pause 1

    asterion "Eu fiz minha própria língua."

    you "Entendo. Não estava esperando por isso. Mas você consegue ler bem em português? Se não, posso te ajudar."

    $Asterion.change ("emotion", "contemplative")

    asterion "O Mestre não deve se preocupar. Sim, estou me lembrando... Agora, o que devo fazer a seguir?"

    you "Podemos começar pesquisando por algo que você quer saber. Tente digitar — sobre o que você está curioso."

    asterion "Sim, senhor. Hum..."

    "Dar uma olhada no mundo exterior. Algumas coisas vem à mente, ele pensou
    tanto sobre elas nessas últimas décadas."

    $myChoices = [ ("Minha terra natal, Creta.", "crete"), ("Local de nascimento do Mestre Jean-Marie.", "bordeaux")]

    if player_background == 'tech':
        $ myChoices.insert(0, ("{color=[UIColorTech]}(TECNOLOGIA) Como fazer um website.{/color}", "tech"))

    if player_background == 'math':
        $ myChoices.insert(0, ("{color=[UIColorMath]}(MATEMÁTICA) Curso online.{/color}", "math"))

    if player_background == 'leader':
        $ myChoices.insert(0, ("{color=[UIColorLeader]}(LÍDER) Conhecer pessoas.{/color}", "leader"))

    if player_background == 'arts':
        $ myChoices.insert(0, ("{color=[UIColorArts]}(ARTES) Catedral de Notre Dame.{/color}", "arts"))

    if player_background == 'speedrunner':
        $ myChoices.insert(0, ("{color=[UIColorSpeedrunner]}(SPEEDRUNNER) Filmes.{/color}", "speedrunner"))

    if player_background == 'humanities':
        $ myChoices.insert(0, ("{color=[UIColorHumanities]}(HUMANAS) Livros.{/color}", "humanities"))


    label chapter13_internet:
        $narrator("O que pesquisamos?", interact=False)
        $result = renpy.display_menu(myChoices)

    if result == "crete":

        $Asterion.change ("emotion", "contemplative")

        asterion "Me pergunto como está Creta hoje em dia..."

        asterion "\"O Palácio de Cnossos foi descoberto no final do século XIX e escavado
        no início do século XX.\""

        asterion "Então... eles encontraram. Resta tão pouco, mas é lá mesmo, é onde eu cresci."

        $Asterion.change ("emotion", "smiling")

        asterion "Este pátio... Quando eu era criança, costumava brincar aqui com meu irmão, Androgeu."

        you "Como era viver naquela época?"

        $Asterion.change ("emotion", "contemplative")

        asterion "Era... agradável, suponho. Se você está se perguntando sobre todos os
        confortos modernos — água corrente, eletricidade — não tínhamos nada disso."

        asterion "Mas vivíamos bem, melhor do que a maioria. Eu até tinha um quarto só meu,
        sei que poucas crianças daquela época podiam dizer o mesmo."

        asterion "Eu tinha um guarda-costas para me proteger, sempre ficávamos juntos..."

        pause 1.0

        $Asterion.change ("emotion", "relieved")

        asterion "Embora esta possa não ser a melhor maneira de descrevê-lo. Ele era apenas
        uns sete anos mais velho do que eu quando se tornou meu, digamos, guardião.
        Eu devia ter quatro anos."

        asterion "Meu tempo no palácio foi bastante agradável, em grande parte
        graças a ele. Seu nome era Froneu."

        asterion "Mas não se engane, eu tinha responsabilidades... Desempenhava
        funções cerimoniais com bastante frequência."

        asterion "Froneu sempre me deu companhia, e Androgeu também, quando suas obrigações permitiam."

        $Asterion.change ("emotion", "contemplative")

        pause 2.0

        asterion "Me pergunto o que mais posso encontrar nessa Internet."

        $ myChoices.remove(("Minha terra natal, Creta.", "crete"))

    if result == "bordeaux":
        $Asterion.change ("emotion", "contemplative")

        asterion "Tem um lugar que estive bastante curioso para saber como é há algum tempo...
        Talvez você já tenha ouvido falar, a região de \"Bordeaux\"."

        you "Esse nome não me é estranho, sim. É uma região da França?"

        asterion "Sim, acredito que seja. Agora, o que sua Internet vai me dizer sobre isto..."

        asterion "\"A mais proeminente região vinícola da França.\" Hm, suponho que o Mestre
        Jean-Marie não estava se gabando, o vinho de sua família deve ter sido notável."

        $Asterion.change ("emotion", "tired")

        asterion "\"Foi capturada pelos alemães durante a Segunda Guerra Mundial...\" Ah, acho que faz sentido."

        $Asterion.change ("emotion", "relieved")

        asterion "Mas parece estar indo muito bem agora. É um alívio."

        you "Hum... Jean-Marie veio dessa região?"

        $Asterion.change ("emotion", "neutral")

        asterion "Sim, é como ele chamava sua pátria ancestral. Ele
        era uma patriota, nenhum lugar na Terra era tão bonito e nobre como sua casa."

        $Asterion.change ("emotion", "sad")

        asterion "Ele não suportava ouvir falar da situação da França na guerra.
        Nenhuma quantidade de súplica poderia impedi-lo de ir."

        "O minotauro ainda podia sentir, o zunido em sua cabeça quando Jean-Marie morreu."

        asterion "E o resto, suponho, é história."

        pause 1.0

        $Asterion.change ("emotion", "tired")

        asterion "Me pergunto como deve ser a sensação de caminhar por um desses vinhedos."

        you "Deve ser refrescante. O sol nas suas costas, talvez um vento frio
        passando através das videiras, folhas roçando nos braços..."

        $Asterion.change ("emotion", "tired")

        asterion "Eu gostaria disso."

        you "Poderiamos fazer um, então. Que tal, nosso próprio vinhedo?"

        $Asterion.change ("emotion", "neutral")

        asterion "O-o que? Mas por que?"

        you "Por que eu posso simplesmente fazer as coisas surgirem do nada, por que não usar isso
        para fazer algo divertido e agradável assim?"

        $Asterion.change ("emotion", "tired")

        asterion "Ah, meu bom senhor... Se ao menos as coisas fossem tão simples. Seria um
        assunto bastante complicado, receio."

        you "Por que? O que está nos impedindo?"

        asterion "Contratos, para começar. Esta terra não é própria para a vida.
        Além disso, isso nos distrairia demais de nossa missão e do hotel, não?"

        you "Suponho que esteja certo..."

        pause 1.0

        $Asterion.change ("emotion", "contemplative")

        asterion "Bem... eu não deveria mentir, um vinhedo {i}seria{/i} ótimo.
        Quem sabe, talvez um dia, se ainda for de sua vontade."

        asterion "É uma invenção bacana, essa coisa de Internet..."


        $ myChoices.remove(("Local de nascimento do Mestre Jean-Marie.", "bordeaux"))

    if result == "tech":

        $Asterion.change ("emotion", "neutral")

        "O minotauro tira os dedos da tela por um momento e fica brincando com eles enquanto desvia o olhar."

        asterion "...Mestre, posso perguntar uma coisa?"

        you "Claro, vá em frente."

        $Asterion.change ("emotion", "contemplative")

        asterion "Você mencionou no salão que as pessoas usam a Internet para trabalhar, certo?
        Como conectar pessoas e vender coisas..."

        you "Sim."

        asterion "E fazer...{w=0.2} estações, para mostrar a outras pessoas?"

        you "Se você quer dizer páginas da web, sim, você pode fazer isso."

        $Asterion.change ("emotion", "neutral")

        asterion "Como se faz sua própria \"página da web\"?"

        you "Hm, essa é uma pergunta complicada. Existem páginas e serviços que tornam isso
        mais fácil, mas acho que você se beneficiaria com um pouco mais de experiência com
        computadores antes de tentar."

        you "Por que pergunta? Que página você tem em mente?"

        $Asterion.change ("emotion", "surprise")
        pause 1
        $Asterion.change ("emotion", "sad")
        pause 1

        "Astério brinca com os dedos em seu assento antes de responder."

        asterion "Não tenho nenhuma ideia concreta, apenas queria saber como uma é feita."

        $Asterion.change ("emotion", "neutral")

        asterion "Quando usei uma máquina de escrever pela primeira vez, não tinha realmente algo em mente,
        apenas queria experimentar e ver como funcionava. Sinto o mesmo agora."

        you "Não acho que você esteja pronto para HTML no momento. Passos de bebê, Astério."

        $Asterion.change ("emotion", "tired")

        asterion "Passos de bebê?"

        you "Quer dizer, vá com calma, você vai aprender com o tempo. Vamos manter simples por enquanto
        — tem mais alguma coisa que você gostaria de pesquisar?"


        $ myChoices.remove(("{color=[UIColorTech]}(TECNOLOGIA) Como fazer um website.{/color}", "tech"))

    if result == "math":

        $Asterion.change ("emotion", "neutral")

        asterion "Acredito que você tenha mencionado algo no salão outro dia.
        É possível procurar aulas online, sim?"

        you "Acho que sim...{w=0.2} Ah, lembrei agora. Essa conversa tomou um rumo estranho."

        show Asterion:
            ease 1.0 yalign 1.5

        $Asterion.change ("emotion", "embarrassed")
        pause 2

        you "Bem, deixa para lá. Em que tipo de aula você estava interessado?"

        $Asterion.change ("emotion", "neutral")

        asterion "...Há tantas opções, Mestre."

        you "Deixa eu pensar em alguma coisa rápida e simples que ilustra bem como usar
        a Internet para aprender coisas novas…{w} Existe alguma comida que você realmente gosta,
        mas não sabe como cozinhar?"

        $Asterion.change ("emotion", "contemplative")

        asterion "... Eu tive um Mestre uma vez, isto foi há muito, muito tempo. Ele era
        do Reino de Leão, que então se tornou a Espanha… A Espanha ainda existe, Mestre?"

        you "Bem, por que você não pergunta à Internet?"

        $Asterion.change ("emotion", "neutral")

        "Astério digita, uma por uma e lentamente, as letras H, I, S, P, A, N, I, A, M."

        $Asterion.change ("emotion", "tired")

        "Os resultados da pesquisa não são exatamente o que ele está procurando. O Mestre o impede de
        clicar em um link para um tesauro em latim, e digita \"Espanha\" ele mesmo."

        $Asterion.change ("emotion", "relieved")

        asterion "O-obrigado, Mestre. Parece que eles saíram ilesos da Segunda Guerra Mundial, como a França."

        you "Eu não colocaria exatamente dessa maneira — mas quer saber, melhor não se aprofundar nisso.
        Por que pergunta?"

        asterion "Há uma sobremesa que o Mestre pedia."

        asterion "Não me era permitido cozinhar para ele, o Mestre era um cristão muito dedicado,
        apesar de não ser exatamente o mais complacente que conheci. Mas eu me lembro muito bem do cheiro daquele bolo."

        you "Hmm… Qualquer coisa mais específica?"

        $Asterion.change ("emotion", "contemplative")

        asterion "...Eu me lembro de ter que carregar sacos cheios de amêndoas sempre que ele pedia."

        you "Tente digitar: Espanha, amêndoas, bolo."

        $Asterion.change ("emotion", "smiling")
        show Asterion:
            ease 0.1 yalign 1.0
            ease 0.15 yalign 1.5
            ease 0.1 yalign 1.0
            ease 0.15 yalign 1.5

        "Astério segue a ordem, desta vez perguntando se ele está escrevendo o nome do país
        corretamente. Seus olhos se iluminam assim que a primeira imagem aparece na tela."

        you "Acho que encontramos o que queríamos. Tarta de Santiago."

        $Asterion.change ("emotion", "contemplative")

        show Asterion:
            ease 1.0 yalign 1.0

        asterion "Sim, acredito que era assim que ele a chamava."

        "O Mestre diz ao minotauro para digitar 'Tarta de Santiago', seguido de 'receita'.
        Ele se apressa e clica no primeiro resultado."

        "Ele lê as instruções com calma. O Mestre o interrompe antes que ele clique
        em um link para um tutorial em vídeo."

        $Asterion.change ("emotion", "neutral")

        you "Quer saber, posso salvar essa página nos favoritos e podemos conferir mais tarde."

        you "Mas sim, você pode encontrar instruções detalhadas sobre como cozinhar praticamente
        qualquer coisa na internet — e isso nem envolve cursos online detalhados..."

        $Asterion.change ("emotion", "contemplative")

        asterion "Eu gostaria de conferir isto mais tarde, Mestre. Obrigado."

        you "O que mais você gostaria de pesquisar?"


        $ myChoices.remove(("{color=[UIColorMath]}(MATEMÁTICA) Curso online.{/color}", "math"))

    if result == "leader":

        $Asterion.change ("emotion", "contemplative")

        "O Mestre observa, o sorriso se espalhando em seu rosto enquanto Astério digita as palavras 'conhecer' e 'pessoas'."

        you "Ah, então é assim."

        $Asterion.change ("emotion", "surprise")

        asterion "O-o que?"

        you "Os hóspedes e eu não somos suficientes para você?"

        $Asterion.change ("emotion", "relieved")

        asterion "N-não, não é nada disso! Apenas fiquei curioso sobre o que você
        mencionou no salão ontem, Mestre. Como você pode usar a internet para conhecer
        pessoas, como amigos por correspondência?"

        "O Mestre dá uma risadinha."

        you "Sim, mas não é tão simples quanto digitar \"conhecer pessoas\". Existem sites
        para isso e você geralmente precisa fazer um perfil antes de poder falar com alguém."

        $Asterion.change ("emotion", "neutral")

        asterion "Um perfil?"

        you "Sim, geralmente são informações bem básicas sobre você."

        $Asterion.change ("emotion", "sad")

        asterion "Não acho que quero divulgar isto tão cedo."

        you "... Bem, configurar um perfil preciso seria difícil, não acho que
        a maioria dos sites aceitaria 1000 a.C. como uma data de nascimento válida."

        you "Mas existem sites que você pode usar como anônimo. Ou você poderia usar um pseudônimo."

        $Asterion.change ("emotion", "neutral")

        asterion "Seria preferível, sim."

        you "Sabe, existem pessoas que fazem perfis fingindo ser personagens fictícios ou
        figuras históricas por diversão — você pode fazer algo assim."

        pause 2

        $Asterion.change ("emotion", "tired")

        asterion "Por que as pessoas fingiriam ser personagens fictícios por diversão?"

        pause 2

        "O Mestre hesita antes de responder."

        you "Acho que estamos desviando do objetivo. Podemos lidar com isso mais tarde, tudo bem?
        Mais alguma coisa que você quer pesquisar?"


        $ myChoices.remove(("{color=[UIColorLeader]}(LÍDER) Conhecer pessoas.{/color}", "leader"))

    if result == "arts":

        $Asterion.change ("emotion", "contemplative")

        "Antes que o Mestre consiga detê-lo, o minotauro digita \"Catedral de Notre Dame\"."

        $Asterion.change ("emotion", "tired")

        "Um arrepio percorre a espinha do homem ao mesmo tempo que o estômago do minotauro embrulha."

        you "Sinto muito. Eu deveria ter te avisado sobre isso."

        $Asterion.change ("emotion", "sad")

        "As orelhas de Astério caem conforme ele lê."

        asterion "Isto é uma tragédia."

        you "É sim. Eles vão restaurar, mas ainda é horrível."

        you "Mas você ainda pode ver muitas filmagens e fotos arquivadas de Notre Dame.
        A maioria dos edifícios históricos como ela são bem preservados e documentados digitalmente."

        "O Mestre mostra a ele os resultados da pesquisa de imagens."

        you "Você mencionou que Jean-Marie fez desenhos da catedral de memória,
        eles fazem justiça à real?"

        "Mais imagens da catedral são reveladas, mas todos os outros resultados
        são imagens de notícias da catedral em chamas."

        $Asterion.change ("emotion", "tired")

        asterion "É estranho. Você esperaria que eu não me importasse muito com algo que está
        completamente fora do meu alcance. Mesmo se não tivesse queimado, continua fora dos limites para mim."

        $Asterion.change ("emotion", "mooing")

        asterion "De certa forma, se está fora dos limites para outras pessoas também, estou compartilhando
        uma pequena parte do meu fardo com elas, e isto não é algo de que gosto."

        $Asterion.change ("emotion", "tired")

        pause 3

        "O minotauro fica amuado em silêncio por um ou dois minutos, e o Mestre lhe dá espaço."

        "Ele considera se mostrar um tour virtual a Astério o faria mudar de ideia,
        mas decide não continuar mexendo na ferida."

        $Asterion.change ("emotion", "sad")

        asterion "Sinto muito por deixar o clima para baixo, Mestre. Prefiro não
        insistir mais neste assunto."

        you "Não se preocupe com isso. E sim, é uma boa ideia. Tem mais alguma coisa que você quer pesquisar?"

        $ myChoices.remove(("{color=[UIColorArts]}(ARTES) Catedral de Notre Dame.{/color}", "arts"))

    if result == "speedrunner":

        $Asterion.change ("emotion", "contemplative")

        "Astério digita \"filmes\"."

        you "Ah, o que você tem em mente?"

        asterion "Bem, durante a gestão de Jean Marie, um de nossos hóspedes tinha um amigo
        projecionista que lhe devia dinheiro, então ele trazia rolos de filme para o hotel."

        asterion "Me pergunto se você pode assistir a filmes como esses na internet."


        "Você gosta de para onde isso está indo."

        you "Você quer vídeos? Ah, eu vou te mostrar vídeos, Astério."

        $Asterion.change ("emotion", "neutral")

        "Você pega o tablet das mãos dele e abre tantas abas quanto o tablet consegue suportar."

        $Asterion.change ("emotion", "tired")

        "Os quinze minutos seguintes voam para você enquanto você mostra a Astério
        os vídeos mais engraçados que a internet tem a oferecer para fazê-lo rir."

        "Vídeos de gato, compilações de \"os melhores\" de seus resenhistas de internet favoritos,
        playlists de vergonha alheia e clipes de anime."

        "Sem você saber, aqueles quinze minutos duram uma eternidade para o minotauro,
        faltando-lhe o contexto para entender seu humor."

        $Asterion.change ("emotion", "annoyed")

        "Earrape, em particular, estressa Astério bastante, mas você não parece
        notar, encantado com a tela e preenchendo um vazio que estava lá há semanas."

        $Asterion.change ("emotion", "tired")

        "Você começa a ficar cada vez mais nervoso à medida que Astério falha em rir de
        qualquer um dos vídeos que você mostra a ele."

        $Asterion.change ("emotion", "relieved")

        "Por mais fugaz que seja seu momento de autoconsciência, Astério suspira de alívio à medida que
        você fecha todas as abas, abre a barra de pesquisa mais uma vez e entrega o dispositivo de volta para ele."


        $ myChoices.remove(("{color=[UIColorSpeedrunner]}(SPEEDRUNNER) Filmes.{/color}", "speedrunner"))

    if result == "humanities":

        $Asterion.change ("emotion", "contemplative")

        "O dedo indicador direito de Astério digita: L, I, V, R, O, S."

        you "Você quer alguma coisa para ler?"

        $Asterion.change ("emotion", "neutral")

        asterion "Sim. Lembro que você mencionou que eu poderia obter muitos livros da Internet
        rapidamente. Como exatamente isto é feito?"

        "Você o instrui a tocar em uma das lojas de e-books exibidos nos resultados da pesquisa."

        you "Aqui. Navegue um pouco e me diga quais livros você quer, eu consigo eles para você."

        $Asterion.change ("emotion", "smiling")

        asterion "Quer dizer que eu posso escolher mais de um?"

        you "É claro. Quantos você quiser."

        $Asterion.change ("emotion", "contemplative")

        "O minotauro olha para a tela. Suas orelhas sacodem como se moscas zumbissem ao seu redor."

        asterion "Mas se eu escolher mais de um, estarei negligenciando os outros? Se
        pegar vários, talvez acabe gastando de forma tola."

        you "Talvez, mas você nunca teve um pouco de excesso?"

        $Asterion.change ("emotion", "neutral")

        asterion "Como?"

        you "Um pouco de conforto, é o que eu estou dizendo. Você trabalhou tão duro ultimamente, ganhar
        alguns livros é uma recompensa bem merecida."

        $Asterion.change ("emotion", "contemplative")

        asterion "A-ah. O Mestre realmente acha isso, que eu mereço uma recompensa?"

        you "É claro. Agora vá em frente, dê uma explorada e veja o que você gosta."

        "O minotauro obedece e sua pesquisa dá frutos em abundância."

        "Durante o século 20, ele ouviu histórias da poesia de Walt Whitman — uma curiosidade que
        nenhum Mestre jamais achou por bem aprovar. Ele seleciona uma coleção de seus trabalhos e,
        em seguida, recebe recomendações das obras de Robert Frost."

        "Mais algumas opções do início do século 20 são exibidas, mas o minotauro é inspirado
        por um toque de aventura. Ele busca uma perspectiva do mundo atual."

        "Ele abre um livro despretensioso cuja capa mostra um desenho granulado de um vulcão.
        \"Autobiografia do Vermelho\" de Anne Carson."

        "O resumo por si só o cativa. Ele olha para a tela como se uma onda de nostalgia
        tomasse conta de seus sentidos."

        $Asterion.change ("emotion", "smiling")

        asterion "Este é sobre Gerião."

        you "Quem?"

        $Asterion.change ("emotion", "contemplative")

        asterion "Ele era meu primo, parente distante. Nos conhecemos em Hades, vivíamos juntos como colegas de quarto."

        asterion "Ah, Gerião. Uma história sobre você, que presente...{w} Posso escolher este também, Mestre?"

        you "É claro, quantos livros você quiser."

        $Asterion.change ("emotion", "relieved")

        asterion "É o suficiente. Se eu escolher mais, com certeza esquecerei do valor deles."

        asterion "Obrigado, Mestre."

        you "De nada. Me dê o tablet por um minuto, vou finalizar as coisas."

        "Depois de comprar os livros e baixá-los, você devolve o dispositivo para o minotauro."

        $Asterion.change ("emotion", "contemplative")

        you "Agora, tem mais alguma coisa que você gostaria de pesquisar na internet?"


        $ myChoices.remove(("{color=[UIColorHumanities]}(HUMANAS) Livros.{/color}", "humanities"))

    if len(myChoices) > 0:
        jump chapter13_internet

    $Asterion.change ("emotion", "contemplative")

    asterion "Será que... A ideia mais boba me ocorreu, talvez seja arrogância de minha parte sequer considerá-la..."

    "As orelhas do minotauro sacodem e seu focinho assume um tom mais vivo de rosa."

    $Asterion.change ("emotion", "embarrassed")

    you "A Internet poderia ter algo sobre... mim?"

    you "É claro. Existe toda uma lenda sobre você, datando de quem sabe quando.
    Podemos encontrar várias coisas."

    you "Embora..."

    menu:
        "\"Existem muitos conceitos errados sobre você.\"":
            you "Olha, já vou te dizendo logo, as pessoas têm muitas ideias erradas sobre você."

        "\"Você pode não gostar do que vai ver.\"":
            you "A história pintou uma imagem muito cruel de você. Eu iria tão longe a ponto de classificar como difamatório."

    $Asterion.change ("emotion", "tired")

    asterion "Entendo... Sim, não posso dizer que estou surpreso. Os Atenienses
    não eram gentis em sua maneira de contar o que aconteceu, sei disso há muito tempo."

    asterion "Vamos ver...\"Astério de Creta\"..."

    pause 2.0

    $Asterion.change ("emotion", "neutral")

    asterion "Ah, há algo aqui... mesmo que não seja sobre {i}mim{/i}.
    Astério, o Primeiro, tornou-se rei de Creta após a morte de seu pai, Rei Téctamo."

    asterion "Depois que Europa foi sequestrada e levada por Zeus, ele se casou com ela
    e tornou-se o padrasto dos filhos de Zeus..."

    $Asterion.change ("emotion", "contemplative")

    asterion "Hã. Não é o que eu queria, mas... isso é legal. Um fragmento da história da minha família ainda vive."

    you "Esse é o seu avô?"

    $Asterion.change ("emotion", "neutral")

    asterion "Não exatamente... Ele viveu muito tempo antes de mim, não consigo nem
    lembrar quantas gerações tínhamos de diferença."

    asterion "Não há muito aqui, suponho que a maior parte seria esquecida. Mas..."

    $Asterion.change ("emotion", "contemplative")

    asterion "Mais abaixo está escrito \"Astério, o Segundo, o Minotauro\"..."

    $Asterion.change ("emotion", "smiling")

    asterion "Vamos ver o que eles têm sobre mim..."

    "Os olhos do minotauro saltam de frase em frase."

    show blackback behind Asterion:
        alpha 0
        ease 1 alpha 0.2

    $Asterion.change ("emotion", "neutral")

    "\"Pasífae, atingida pela loucura de Poseidon, recrutou o artesão Dédalo para
    criar uma vaca oca na qual ela recebeu a estocada do touro.\""

    "\"A criança híbrida, dita ter o corpo de homem e cabeça de touro,
    não tinha lugar na ordem natural e nada para sustentá-la.
    Como tal, ele se tornou violento e começou a consumir carne humana.\""

    $renpy.music.set_volume(0.7, delay=1, channel='music')
    show blackback:
        ease 1 alpha 0.35

    $Asterion.change ("emotion", "tired")

    "\"O rei Minos ordenou a Atenas que enviasse jovens como tributo para alimentá-lo.
    Sete jovens, entre os quais Teseu, herdeiro do trono de Atenas.\""

    "\"Ariadne, a irmã do minotauro, encantou-se com o herói ateniense e lhe confiou
    o segredo de que o labirinto poderia ser solucionado com um novelo de lã."

    $renpy.music.set_volume(0.4, delay=1, channel='music')
    show blackback:
        ease 1 alpha 0.5

    "\"Com a ajuda de Ariadne, Teseu o solucionou e derrotou o minotauro.\""

    "\"Ele escapou de Creta com a princesa, mas a abandonou na ilha de Naxos,
    onde acredita-se que ela encontrou seu fim, ou foi sequestrada por Dionísio.\""

    $renpy.music.set_volume(0.1, delay=1, channel='music')
    show blackback:
        ease 1 alpha 0.65

    $Asterion.change ("emotion", "sad")
    "\"Por consequência da morte do minotauro, Creta caiu de sua posição hegemônica
    sobre o Mediterrâneo.\""

    "\"O rei Minos saiu em busca de Dédalo, procurando por vingança, pois
    acreditava que foi o artesão quem revelou a Ariadne a solução secreta para o labirinto.\""

    show blackback:
        ease 1 alpha 0.8

    "\"Isto, por sua vez, levou à morte de Minos, fervido vivo em uma corte estrangeira.\""

    "\"A morte do minotauro marca a queda de Creta e a ascensão de Atenas como a principal
    potência do Mediterrâneo.\""

    "\"A perda de uma figura dirigente centralizada levou à fragmentação, por sua vez,
    permitindo que fosse conquistada por diferentes civilizações ao longo da história.\""

    hide blackback
    with Dissolve (2.0)

    $renpy.music.set_volume(1, delay=1, channel='music')

    $Asterion.change ("emotion", "tired")

    pause 3

    menu:
        "Consolar Astério.":
            you "Se quer ouvir um conselho sobre cautela, nem tudo o que você vai encontrar online é verdade."

            you "Eu imagino que possa ser doloroso, ver uma má representação de si mesmo."

            you "Você não é nem um pouco como diz a lenda. É uma calúnia total."

            you "Mas nós dois sabemos coisa melhor. Você é gentil, trabalha duro e é muito importante
            para o hotel e para as pessoas daqui. Essa é a verdade que importa."

            you "Dito isso, pode ser melhor se você não focar muito no que a Internet
            diz sobre você. Existem coisas melhores para você pesquisar sobre."

            $Asterion.change ("emotion", "mooing")

            "O minotauro respira fundo, segurando-se para não tossir."

            $Asterion.change ("emotion", "tired")

            asterion "Está tudo bem. Nada que eu já não soubesse."

            asterion "Os atenienses não foram lá muito gentis na forma com que contaram a história."

            you "Temos nossa própria versão da história agora. Isso não vai importar."
            $global_affection += 1

        "Permanecer em silêncio.":

            "Os olhos do Mestre continuam examinando o rosto do minotauro, talvez em busca de pistas sobre o que ele está pensando."

            "Astério pode apenas esperar que ele não note suas costas encharcadas de suor."

            "Mas os doze são misericordiosos hoje, pelo menos por um segundo. A fome do
            senhor aumenta e sua atenção é desviada."

    pause 3

    you "Bem, eu estava pensando em descer para o salão, se bem me lembro,
    tem algumas sobras de ontem que poderíamos comer."

    you "Se quiser, pode ficar aqui e continuar navegando na Internet. Parece bom para você?"

    "As pontas dos dedos do minotauro estavam geladas, seus cascos irradiavam uma
    dor maçante que subia até o topo de seus chifres."

    $Asterion.change ("emotion", "mooing")

    "Ele respirou fundo. Seus dedos se curvaram na superfície do dispositivo, suas orelhas
    ficaram dormentes à medida que um fio de suor frio escorria por suas costas."

    $Asterion.change ("emotion", "tired")

    asterion "Sim. Ficarei bem. Obrigado, senhor."

    you "Te vejo depois, Astério."

    $Asterion.change ("emotion", "mooing")

    "O minotauro fechou os olhos e se lembrou de tudo — as dezenas, talvez
    centenas de recontagens da história que ouvira ao longo dos séculos."

    "Cada uma mais horrível que a anterior, tantas vezes girando em torno
    daquela fundamental informação errada de que ele tinha sido um canibal."

    "Uma mentira que muda vidas."

    $Asterion.change ("emotion", "tired")

    "E, no entanto, havia algo reconfortante no simples fato de que, canibalismo
    à parte, o que ele leu foi exatamente o que esperava."

    $Asterion.change ("emotion", "sad")

    asterion "Vejo você em breve, meu senhor."

    stop music fadeout 2.0

    scene bg black
    with Dissolve(2)

    pause 2

    scene bg staircase
    with Dissolve (1)

    "Mais uma vez, o som de seus passos ecoa para cima e para baixo na escadaria, da
    claraboia acima até as profundezas abaixo."

    "Cada um soa de certa forma solitário sem o barulho familiar dos cascos de Astério
    mantendo o ritmo com eles."

    "Não há voz grave, cantarolante e sussurante logo acima e atrás de seu ombro."

    "Nenhum corpo enorme roçando contra sua lateral, e então se afastando depois de permanecer
    pelo mais breve dos momentos. Não há conversa, nem mesmo silêncio amistoso."

    "Há apenas você e a escada."

    "À medida que você desce os degraus, sua mente desliza para a noite anterior.
    Para a celebração do renascimento do hotel."

    "Para o concerto de Astério."

    if Build3Ending == 'good':


        "Para o abraço que você compartilhou com o minotauro antes que ele subisse ao palco e
        para as brincadeiras entre vocês dois enquanto voltavam para seus aposentos quando
        já era tarde da noite."

    if Build3Ending == 'neutral':

        "Para Astério incluindo você em suas orações e o compromisso compartilhado
        de continuar a missão do hotel."

        "Quanta diferença uma única noite faz. E, ainda assim, quão pouco em face
        de anos de experiências passadas; séculos, no caso de Astério."

    "Você enfia a cabeça no saguão, verificando por qualquer chegada matinal.
    Ao se deparar apenas com silêncio e solidão, você segue o caminho até
    a luz e a vida — por mais que estejam transmitindo uma aura de ressaca e cabeça pesada — do salão."

    $LoungeBlobs = [False, 1]

    if first_guest == "Luke":
        play music "music/AberdeenDoneIt.ogg" fadeout 1.0 fadein 1.0
        $Luke.change("clothes", "uniform")
        $Luke.change("arm", "pointing")
        $Luke.change("emotion", "laughing")
        $Kota.change("clothes", "kimono")
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "relaxed")

    else:
        play music "music/TheSorrow.ogg" fadeout 4.0 fadein 4.0
        $Luke.change("clothes", "tankpants")
        $Kota.change("clothes", "barman")
        $Luke.change("arm", "hip")
        $Luke.change("emotion", "neutral")
        $Kota.change("emotion", "happy")
        $Kota.change("leftarm", "mug")

    scene Lounge
    show Luke:
        xalign 1.0 yalign 1.0 xzoom 1
    show Kota:
        xalign 0.0 yalign 1.0 xzoom 1
    with Dissolve(1)

    pause 1

    if first_guest == "Luke":

        "O par de trabalhadores sul-americanos estão amontoados sobre a mesma mesa no canto
        que ocuparam na noite anterior, ambos {i}bebendo{/i} para diminuir os efeitos da ressaca."

        "Alguns dos recém-chegados estão espalhados aqui e ali, ainda ocasionalmente lançando
        olhares de soslaio na direção do grifo escandaloso administrando o balcão do bar."

        "E o próprio Luke conversa com Kota enquanto o dragão belisca seu café da manhã
        com delicada precisão."

    else:

        "O grupo de estudantes do Oriente Médio está reunido ao redor da mesma mesa
        perto da lareira que ocuparam na noite anterior, compartilhando uma animada
        conversa diante de suas xícaras de café fumegantes."

        "Alguns dos recém-chegados estão espalhados aqui e ali, ainda ocasionalmente lançando
        olhares de soslaio na direção do dragão sereno administrando o balcão do bar."

        "E o próprio Kota concorda com a cabeça na conversa com Luke enquanto o grifo põe para dentro seu café da manhã."


    $Luke.change("emotion", "neutral")
    luke "...então, o que é que cê acha?{w=0.2} Pode ser bem divertido, né?"

    $Kota.change("emotion", "neutral")
    kota "Mm, talvez."

    $Luke.change("arm", "pointing")
    luke "Vamo lá, Azulzinho! Um pouquinho de música,{w=0.2} observar as estrelas,{w=0.2} eu posso fazer uns lanches pra gente..."

    $Luke.change("emotion", "cocky")
    $Luke.change("arm", "hip")
    luke "Aah! Cê já experimentou um picolé de picles?{w} Se fizer eles grandes o suficiente dá
    pra ficar chupando praticamente a noite toda."

    $Kota.change("emotion", "angry")
    pause 1.0

    $Kota.change("rightarm", "raised")
    $Kota.change("leftarm", "relaxed")
    kota "...Isto foi uma sugestão?"

    show Luke:
        ease 1.0 xalign 0.75
    $Luke.change("emotion", "hornier")
    luke "Você quer que seja?"

    pause 1.0

    $Luke.change("emotion", "laughing")
    show Luke:
        ease 0.6 xalign 1.0
    pause 0.6
    show Luke:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.0
        repeat

    $Kota.change("emotion", "puzzled")
    $Kota.change("rightarm", "relaxed")
    "O grifo tenta manter uma expressão séria, mas tem dificuldade conforme os segundos
    se passam. Ele finalmente explode em um ataque de risadinhas enquanto Kota revira os olhos."

    show Luke:
        ease 0.3 yalign 1.0
    $Luke.change("emotion", "happy")
    $Luke.change("arm", "pointing")
    luke "Mas sério, quase tudo fica mais divertido quando você faz com outra
    pessoa.{w} Sem gracinha, eu prometo. Só dois homens curtindo a
    beleza do céu noturno juntos."

    $Kota.change("emotion", "sad")
    kota "Você não prefere passar o tempo com uma de suas paqueras?"

    $Luke.change("emotion", "annoyed")
    $Luke.change("arm", "hip")
    luke "Nem, coisas assim nunca duram tanto quanto você quer."
    $Luke.change("emotion", "sad")

    if first_guest == "Luke":
        "O olhar de Luke se dirige para os trabalhadores sul-americanos no canto
        e um suspiro melancólico escapa de seu bico."
    else:
        "O olhar de Luke fica distante e um suspiro melancólico escapa de seu bico."


    $Luke.change("emotion", "neutral")
    luke "Vamos, porfavorzinho?{w} Prometo fazer seu tempo valer a pena."

    $Luke.change("emotion", "cocky")
    luke "A gente podia até trazer [player_name] e Ang- digo, Astério, juntos pro passeio, fazer disso um rolê de verdade."

    you "Do que vocês estão falando?"

    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "neutral")
    "A dupla olha para você quando você fala."


    if first_guest == "Luke":
        show Kota:
            ease 1.0 xalign -0.2
        "Você se move para pegar o banquinho ao lado de Kota. O dragão limpa a boca
        com o guardanapo e lhe dá um pequeno aceno de saudação."

        $Luke.change("emotion", "laughing")
        $Luke.change("arm", "hip")
        luke "Ah! Bom dia, chefinho!{w=0.2} Tava só contando pro Kota aqui
        sobre uma ideia que eu tive de sair pra observar as estrelas."

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")
        you "Hm. O que te fez ter essa ideia?"

        $Luke.change("emotion", "wink")
        "O grifo esfrega a nuca."

        luke "Sei lá. É uma coisa que eu costumava fazer o tempo todo quando era criança, acho que só andei ansioso por isso esses dias."

        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "point")
        luke "Não me entenda mal, dirigir essa joça tem sido a maior diversão que eu já tive em anos.{w}
        Mas eu não sou de ferro, então até eu preciso fazer uma pausa às vezes, sabe?"

        $Luke.change("emotion", "annoyed")
        $Kota.change("emotion", "puzzled")
        $Luke.change("arm", "hip")
        luke "Entre cozinhar, limpar e tentar descobrir pra onde as coisas tão
        desaparecendo, um cara pode ficar muito cansado."

        you "Desaparecendo?"

        luke "Sim, é estranho pra caramba. {w=0.2} Às vezes eu tô preparando um belo
        prato de hambúrgueres, saio pra limpar e, quando me viro,
        metade deles sumiu."

        $Luke.change("arm", "pointing")
        luke "Ou então entro na câmara fria pra pegar umas latas de feijão e vejo
        que estamos sem, quando sei que estoquei algumas na última vez que entrei lá."

        you "Isso é… muito estranho. Não acho que algum dos hóspedes estaria entrando sorrateiramente
        na cozinha para pegar comida quando eles podem simplesmente pedir para que seja servida."

        you "Será que o hotel poderia estar fazendo isso de alguma forma?"

        $Kota.change("emotion", "neutral")
        $Luke.change("emotion", "wink")
        $Luke.change("arm", "hip")
        luke "Você e Astério deveriam saber sobre como esse negócio doido de voodoo funciona melhor do que eu, chefinho."

        you "Acho que posso perguntar a ele."

        $Luke.change("emotion", "neutral")
        you "Mas sim, se você precisar de uma pausa, então isso poderia ser legal. Depois
        de tudo o que aconteceu nos últimos dias, acho que todos nós poderíamos aproveitar."

        kota "Mm."

        "Você e Luke olham para Kota. O dragão continua a mastigar sua
        comida, sua expressão pensativa. Então ele engole e fala."

        kota "Algumas noites atrás, me encontrei com Astério no alpendre do hotel."

        $Kota.change("emotion", "sad")
        kota "Isso foi um pouco depois de eu chegar,{w=0.2} e…"

        "Ele olha para Luke e depois para longe. Antes que o silêncio torne-se muito estranho,
        ele pigarreia e continua."

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        kota "Acabamos tendo uma conversa esclarecedora enquanto ele tocava
        sua lira.{w=0.2} E o céu noturno era realmente de tirar o fôlego."

        $Kota.change("emotion", "happy")
        $Kota.change("leftarm", "relaxed")
        kota "Suponho que seria ótimo fazer algo assim novamente."

        $Luke.change("emotion", "laughing")
        luke "Beleza! É um plano, então!"

        $Luke.change("emotion", "happy")
        "O grifo sorri e seus olhos brilham como as estrelas que ele parece tanto amar."

    else:
        show Luke:
            ease 1.0 xalign 1.2

        $Luke.change("arm", "salute")
        "Você move para se sentar no banco ao lado de Luke, o grifo limpa o bico com
        o antebraço e o cumprimenta com um largo sorriso."

        $Kota.change("emotion", "laughing")
        $Kota.change("rightarm", "raised")
        $Luke.change("arm", "hip")
        kota "Bom dia, [player_name].{w=0.2} Luke estava me contando sobre
        sua ideia de observar as estrelas e desejou que eu me juntasse a ele."

        $Kota.change("emotion", "neutral")
        $Kota.change("rightarm", "relaxed")
        you "Ah? Como surgiu essa ideia?"

        $Luke.change("emotion", "wink")
        luke "Bem, isso vem sacudido na minha mente já tem um tempo."

        $Luke.change("emotion", "horny")
        luke "Sabe, umas noites atrás eu tava pensando sobre as coisas.{w=0.2} Foi logo
        depois que eu cheguei aqui, e, bem, cê sabe."

        $Luke.change("emotion", "annoyed")
        $Kota.change("emotion", "sad")
        "Ele olha para Kota e, em seguida, pigarreia e continua."

        $Luke.change("emotion", "neutral")
        luke "Enfim, eu vi Astério no alpendre tocando aquela harpa dele.
        A gente acabou jogando a merda no ventilador e ele me disse umas coisas que eu precisava ouvir."

        $Luke.change("emotion", "happy")
        $Kota.change("emotion", "neutral")
        luke "Mas as estrelas, cara…{w=0.2} era como olhar no rosto de Deus."

        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "pointing")
        luke "Eu sempre amei olhar pras estrelas. Aí eu pensei, bem,
        o que é melhor do que fazer isso com alguns amigos?"

        $Kota.change("emotion", "puzzled")
        $Kota.change("leftarm", "raised")
        kota "Ah, então somos amigos, não é?"

        $Luke.change("emotion", "wink")
        "O grifo fica inquieto e se contorce em seu banquinho com uma risadinha acanhada."

        $Luke.change("arm", "hip")
        luke "Bem, quer dizer…{w=0.2} Eu só achei que…{w=0.2} cê sabe."

        $Kota.change("emotion", "happy")
        $Kota.change("rightarm", "mug")
        "Kota murmura de forma grave e estrondosa enquanto cruza os braços e fecha os olhos. Pensando. Considerando."

        kota "Suponho que eu poderia aproveitar algo assim. Algo para tirar minha mente das coisas."

        $Kota.change("emotion", "puzzled")
        $Luke.change("emotion", "neutral")
        kota "Não me entenda mal, [player_name], fico grato pelo trabalho.{w}
        Mas correr por aí servindo aos hóspedes enquanto tento descobrir para onde
        as coisas estão desaparecendo é mais cansativo do que eu esperava."

        you "Espera, o que está desaparecendo?"

        $Kota.change("emotion", "sad")
        $Kota.change("rightarm", "raised")
        $Kota.change("leftarm", "raised")
        "Kota dá de ombros."

        kota "É muito estranho. Geralmente é comida, mas até os utensílios não estão totalmente seguros."

        $Kota.change("emotion", "puzzled")
        $Kota.change("leftarm", "relaxed")
        kota "Eu preparo algumas bandejas e me viro, depois não as encontro no momento em
        que olho de volta.{w=0.2} Até mesmo a câmara fria tem uma ocasional jarra ou lata faltando."

        $Kota.change("rightarm", "relaxed")
        you "Isso é… muito estranho. Não acho que algum dos hóspedes estaria entrando sorrateiramente
        na cozinha para pegar comida quando eles podem simplesmente pedir para que seja servida."

        you "Será que o hotel poderia estar fazendo isso de alguma forma?"

        $Kota.change("leftarm", "raised")
        kota "Acredito que não. Mas admito que você ou Astério saberiam mais do
        que eu como tudo isso funciona."

        you "Acho que posso perguntar a ele."

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        you "Mas sim, se você precisar de uma pausa, então isso poderia ser legal. Depois
        de tudo o que aconteceu nos últimos dias, acho que todos nós poderíamos aproveitar."

        $Luke.change("emotion", "laughing")
        luke "Beleza! É um plano, então!"

        $Luke.change("emotion", "happy")
        "O grifo salta de seu banquinho, alongando o corpo e chicoteando o rabo com entusiasmo."

    show Luke:
        ease 0.5 xalign 0.8

    $Kota.change("emotion", "neutral")
    $Luke.change("arm", "hip")
    luke "Ah, cara, isso vai ser ótimo!{w} A gente pode levar umas caixas de cerveja,{w=0.2}
    arranjar umas cadeiras de jardim,{w=0.2} e-"

    $Luke.change("emotion", "horny")
    "Luke faz uma pausa, sorri pretensiosamente, e olha para você."

    $Luke.change("emotion", "cocky")
    $Luke.change("arm", "pointing")
    luke "Ei, acha que a mágica doida do seu hotel consegue fazer um telescópio pra gente?"

    you "Hã… hm."

    $Luke.change("arm", "hip")
    you "É difícil fazer objetos complicados. Você precisa ser capaz de dizer ao hotel como."

    $Luke.change("emotion", "neutral")
    you "Mas acho que existem alguns esquemas para diferentes máquinas, telefones, coisas
    assim lá no Alicerce. Astério me disse que tinha tudo organizado em uma das mesas."

    you "Você poderia dar uma olhada lá e ver se consegue encontrar algo para um telescópio.
    Se não, podemos tentar elaborar algo."

    $Luke.change("emotion", "annoyed")
    $Kota.change("emotion", "sad")
    luke "No alicerce, né?"

    "Luke enrola por um longo momento. Ele coça a parte de baixo de seu bico.
    Sua cauda balança atrás dele."

    $Luke.change("emotion", "cocky")
    $Luke.change("arm", "pointing")
    $Kota.change("emotion", "surprise")
    show Kota:
        ease 1.0 xalign -0.3
    show Luke:
        ease 1.2 xalign 0.3
    pause 1.2
    show Kota:
        ease 2.0 xalign 0.2
    show Luke:
        ease 2.2 xalign 0.8

    luke "Beleza!{w} Você abre o caminho e eu e o Azulzinho encontramos aqueles esquemas de máquina num instante."

    $Kota.change("emotion", "puzzled")
    $Kota.change("rightarm", "raised")
    $Kota.change("leftarm", "raised")

    show Kota:
        ease 1.0 xalign 0.0
    kota "Desculpe, mas, eu?"

    show Luke:
        ease 1.0 xalign 0.6
    pause 1.0
    show Kota:
        ease 2.0 xalign 0.2
    show Luke:
        ease 2.0 xalign 0.8
    $Luke.change("emotion", "horny")
    luke "É, ué. Dois pares de olhos vão encontrar o que a gente procura mais rápido do que um, não é?"

    $Kota.change("rightarm", "relaxed")
    $Kota.change("leftarm", "relaxed")
    "O dragão olha para você e você faz um dar de ombros impotente na direção dele. Luke está certo,
    e mesmo que Kota não queira admitir, vocês três sabem disso."

    $Kota.change("emotion", "sad")
    kota "Você vai me importunar até eu dizer sim,{w=0.2} não vai?"
    show Kota:
        ease 1.0 xalign 0.15
    show Luke:
        ease 1.0 xalign 0.75
    $Luke.change("emotion", "laughing")
    luke "Isso aí!"

    "Diante do sorriso sem vergonha do grifo, Kota pode apenas suspirar, balançar a cabeça
    e render-se ao seu destino."

    $Kota.change("emotion", "neutral")
    $Kota.change("rightarm", "raised")
    $Kota.change("leftarm", "raised")
    kota "Muito bem. Suponho que devamos descer mais cedo ou mais tarde, certo?"

    $Luke.change("emotion", "neutral")
    you "Ei, escutem… antes de vocês irem, posso contar algo a vocês dois?"

    show Kota:
        ease 1.0 xalign 0.0
    $Luke.change("arm", "hip")
    $Kota.change("rightarm", "relaxed")
    $Kota.change("leftarm", "relaxed")
    pause 1.0
    show Kota:
        ease 1.0 yalign 1.2 zoom 1.05
    show Luke:
        ease 1.0 yalign 1.05 zoom 1.05
    "Você olha ao redor e, em seguida, gesticula para o dragão e o grifo se aproximando."

    you "É sobre o Astério."

    $Kota.change("emotion", "puzzled")
    kota "Está tudo bem?"

    you "Acho que sim. É só que…"

    "Kota e Luke esperam que você organize seus pensamentos. Você pesa cada palavra
    antes de falar, tentando decidir o quanto contar para eles."

    "O quanto você tem o direito de contar a eles."

    you "Ele passou por muita coisa. Vocês se lembram de como o hotel estava quando acabamos de reabrir, certo?"

    if first_guest == "Luke":
        $Luke.change("emotion", "sad")
        "O grifo acena com a cabeça. Sua expressão cai para algo que quase poderia ser chamado de sério."
    else:
        "O dragão acena com a cabeça. Sua expressão fica séria conforme ele espera, paciente e plácido, que você continue."

    $Luke.change("emotion", "sad")
    you "Bem, ele… a família dele não tem sido capaz de manter o hotel em boas condições
    desde que o último Mestre o abandonou. Quando eu cheguei, só Astério estava aqui."

    you "Ele já passou por muito sufoco e as coisas podem ficar difíceis para ele às vezes.
    Eu sei que nos divertimos ontem à noite, mas hoje de manhã, ele…"

    you "Ele pode precisar de um tempinho."

    $Luke.change("emotion", "neutral")
    "Luke acena com a cabeça. E então fala em um tom baixo e uniforme que chega a ser surpreendente vindo do grifo."

    $Luke.change("emotion", "happy")
    luke "Ele pode levar todo o tempo que precisar. Não vamos forçar ele a sair com a gente."

    $Luke.change("arm", "pointing")
    luke "Mas se ele já estiver se sentindo melhor de noite,{w=0.2} você e ele são bem-vindos pra se juntar à diversão."

    $Luke.change("arm", "hip")
    you "Obrigado, Luke."

    $Luke.change("emotion", "wink")
    "O grifo dá uma piscadela para você e sua pata pesada bate em seu ombro."

    luke "É claro. É o mínimo que eu posso fazer por ele e você."

    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "neutral")
    luke "Então!{w} Bora?"

    kota "Sim…"

    you "Certo."

    "Com isso dito e feito, vocês três quebram a aproximação."

    play sound "sfx/hum.ogg"
    hide Luke
    hide Kota
    with Dissolve(1)

    "Você abre a passagem para o Alicerce para eles, cantarolando exatamente como Astério lhe ensinou.
    Depois de ver o grifo e o dragão indo, você decide verificar o que mais precisa ser feito."

    "O hotel está vivo mais uma vez, e é dever do Mestre cuidar dos hóspedes que
    passam por suas portas abertas."

    pause 2.0

    "Mas primeiro, café da manhã."

    stop music fadeout 2.0
    scene bg black
    with Dissolve(2)

    play music "music/CrossingTheAstralBridge.ogg" fadein 1.0 fadeout 1.0

    pause 2

    "O grifo e o dragão seguem pelo sinuoso corredor de pedra.
    Seus passos ecoam no silêncio que os cerca, avançando para as profundezas
    labirínticas que aguardam a dupla."

    luke "...Então."

    kota "Mm."

    luke "De volta aqui outra vez."

    kota "Mmhm."

    "O silêncio cai novamente, um cobertor sufocante que engole a dupla. Assim que
    começa a ficar insuportável, é interrompido por um som agudo e choramingante."

    kota "Quer parar com isto?"

    luke "Qual é o problema? Não gosta do meu assobio?"

    kota "Para ser honesto, parece que alguém está estrangulando um gato."

    luke "Hmph.{w=0.2} Grosso."

    pause 1.0

    luke "Não tô com medo, tá legal?"

    luke "Quer dizer, o que tem aqui pra se ter medo?{w} É só um porão assustador."

    luke "Em um{w=0.2} hotel estranho,{w=0.2} e mágico."

    kota "Sim. Nada para se ter medo."

    pause 1.0

    kota "...Será que você pode soltar o meu braço?{w=0.2} Acho que estou começando a perder a circulação."

    luke "Ah, desculpa."

    "As mãos de Luke se afastam, levantando-se com as palmas à mostra enquanto ele dá um sorriso tímido para Kota."

    "Os dois continuam andando pela passagem; e embora nenhum dos dois perceba,
    seus ombros continuam a se roçar, como se confirmando a presença um do outro."

    "E então eles dobram uma última curva e param no limiar de seu destino."

    scene Bedrock
    with Dissolve(2)

    if first_guest == "Luke":

        "Na época em que ele, Angus e os outros estavam lá embaixo tentando fazer o wi-fi funcionar,
        Luke foi capaz de se distrair da opressiva sensação de algo errado que preenchia a sala."

        "Mas agora não há ninguém para quem servir o almoço. Nenhum homem atraente para
        cobiçar enquanto eles grunhem, suam e curvam. E a sensação roça sua nuca e desliza como um
        sincelo em suas costas."

        if 'Kota' in rd_team_names():
            "O grifo se depara com os olhos do dragão e encontra um reflexo de seus pensamentos
            escrito claramente no rosto de Kota."

    else:
        "Quando ele estava lá embaixo ajudando--tanto quanto podia, pelo menos--a fazer o
        wi-fi funcionar, Kota tinha sido capaz de encontrar distrações para
        a opressiva sensação de algo errado que preenchia a sala."

        "Mas agora não há ninguém para quem servir lanches ou chá. Nenhuma tagarelice de
        uma certa jovem entusiasmada demais. E o sentimento aperta como um punho
        em torno de seu velho e palpitante coração."

        if 'Luke' in rd_team_names():
            "O dragão encontra os olhos do grifo e encontra um reflexo de seus pensamentos
            escrito claramente no rosto de Luke."


    luke "...Depois de você."

    kota "Não, por favor, eu insisto.{w=0.2} Depois de você."

    luke "Nah, tudo bem.{w=0.2} Primeiro as damas, não é?"

    kota "Francamente, eu... eu-{w=0.2} como é?"

    pause 1.0

    luke "...No três?"

    kota "Isto seria aceitável."

    luke "Beleza.{w=0.2} Lá vai."

    luke "...Um."

    kota "...Dois."

    luke "...Três!{nw}"

    kota "Três!{nw}"

    if first_guest == "Luke":

        $Kota.change("emotion", "surprise")

        show Kota:
            xalign 0.5 yalign 1.0 xzoom 1 zoom 1
        with Dissolve(0.5)

        pause 1

        "Com uma respiração profunda sibilando por entre os dentes cerrados, o dragão avança para dentro
        da sala. Ele faz uma pausa, esperando, e então uma risadinha suave atrás dele o faz piscar."

        "Ele olha de volta para a entrada da sala e pega Luke tentando--e falhando--abafar
        outra explosão de risadas."

        $Kota.change("emotion", "angry")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        kota "...Não foi engraçado."

        $Luke.change("emotion", "laughing")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "relaxed")

        show Kota:
            ease 1.0 xalign 0.1
        pause 1
        show Luke:
            xalign 0.9 yalign 1.0 xzoom 1.0
        with Dissolve(1.0)
        luke "Qual é, foi um pouquinho sim."

        $Luke.change("emotion", "horny")
        $Kota.change("emotion", "neutral")
        pause 1
        $Kota.change("emotion", "happy")
        "Kota solta um suspiro pesado e cruza os braços. Mesmo enquanto tenta bufar e encarar
        seu companheiro de outrora, os cantos de sua boca se contraem para cima."

        "Talvez tenha sido um pouquinho engraçado."

        $Kota.change("emotion", "neutral")
        kota "Bem, então, se você já terminou de brincar?"

    else:

        $Luke.change("emotion", "surprise")

        show Luke:
            xalign 0.5 yalign 1.0 xzoom 1 zoom 1
        with Dissolve(0.5)

        pause 1

        "O grifo solta um grito involuntário enquanto corre para dentro da sala.
        Ele estremece e levanta os punhos quando ouve um estrondo baixo e profundo,
        mas então percebe que o som está vindo de trás."

        "Kota ainda está parado na entrada da sala, escondendo um pequeno sorriso atrás da mão."

        $Luke.change("emotion", "annoyed")
        luke "Babaca."

        $Kota.change("emotion", "laughing")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")

        show Luke:
            ease 1.0 xalign 0.9
        pause 1
        show Kota:
            xalign 0.1 yalign 1.0 xzoom 1.0
        with Dissolve(1.0)

        pause 1
        $Kota.change("rightarm", "relaxed")
        kota "Ora, Sr. Walker. Não é você quem está sempre me dizendo para relaxar?"

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        $Luke.change("emotion", "surprise")
        pause 1
        $Luke.change("emotion", "wink")
        "O bico de Luke abre, e então fecha. Abre, e então fecha.
        O grifo esfrega a nuca e solta uma risada silenciosa."

        "Ele não pode argumentar contra isto."

        $Luke.change("emotion", "neutral")
        kota "Bem, agora, e o telescópio?"

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "pointing")
    luke "Sim, sim..."

    $Luke.change("arm", "hip")

    show Luke:
        xzoom -1
        ease 3.0 xalign 2.0

    "O grifo move em direção a uma das mesas e começa a procurar nas pilhas de documentos."

    luke "[player_name] disse que aqueles esquemas deveriam estar aqui, certo?"

    kota "Correto."

    $Kota.change("emotion", "sad")
    "Kota observa Luke vasculhar os papéis, retraindo quando alguns deles caem da mesa
    e se espalham no chão. Enquanto o grifo bagunça o trabalho de Astério,
    o olhar do dragão começa a vagar."

    "Para a parede de obisidiana enchendo metade da sala."

    "Para a bacia sem fundo no centro da câmara massiva."

    $Kota.change("emotion", "puzzled")
    show Kota:
        xzoom -1
        pause 1
        xzoom 1
    pause 1
    "Para os instrumentos empilhados ao longo de uma parede e, em seguida, para as pastas alinhadas em outra mesa próxima."

    "Contratos."

    $Kota.change("rightarm", "raised")
    show Kota:
        xzoom -1
        ease 2.0 xalign -0.2

    "Kota não tem certeza a princípio o que o leva a se aproximar e começar a folhear
    aquelas pastas. Mas enquanto cantarola para si mesmo, ele procura
    nomes. Descrições. Qualquer coisa que possa despertar um único indício de familiaridade."

    $Kota.change("rightarm", "relaxed")

    "Quando ele perguntou a [player_name] e Astério, os dois disseram que não sabiam de
    nenhum hóspede parecido com o homem que ele estava procurando. Não era como se ele não acreditasse
    neles, mas talvez…"

    $Kota.change("leftarm", "raised")
    $Kota.change("rightarm", "relaxed")

    "Talvez fosse ainda mais no passado do que a família de Astério conseguiria se lembrar.
    Talvez [player_name], sendo novo e inexperiente, sequer saberia onde procurar
    nos registros."

    $Kota.change("emotion", "sad")

    "Talvez não fosse o dragão vermelho, mas um dos nomes que Kota havia procurado
    quando sua jornada começou, escondendo-se em algum lugar dentro daquelas páginas."

    "Talvez. Talvez. Talvez."

    $Kota.change("leftarm", "relaxed")
    "Era pouco provável, mas a mera possibilidade era como uma coceita insistente.
    E Kota há muito tempo havia perdido a capacidade de resistir coçar."

    stop music fadeout 1.0

    $Kota.change("emotion", "puzzled")
    kota "..."

    kota "..."

    kota "...hm?"

    kota "Espere um momento…{w=0.2} Isto é{nw}"

    $Kota.change("emotion", "surprise")
    $Kota.change("leftarm", "raised")
    $Kota.change("rightarm", "raised")
    luke "AAAAAHH!"

    $Luke.change("emotion", "surprise")
    $Luke.change("arm", "pointing")

    show Luke behind Kota:
        xzoom 1
        ease 2.0 xalign 0.2

    "O grito agudo desvia a linha de pensamento de Kota. E então algo quente,
    penífero e cheirando a gordura de bacon e almíscar bate em sua lateral e envolve
    os braços com força ao redor dele."

    kota "GAH!"

    $Luke.change("arm", "hip")
    $Kota.change("emotion", "angry")
    $Kota.change("leftarm", "relaxed")

    show Kota:
        xzoom 1

    kota "Luke, o que você…?!{w=0.2} Me solte…!"
    show Kota:
        ease 1.0 xalign 0.1
    show Luke:
        xzoom -1
        ease 2.0 xalign -0.2

    $Kota.change("rightarm", "relaxed")
    $Luke.change("arm", "pointing")
    luke "Tem alguma coisa ali!"

    "Os olhos do dragão seguem o dedo trêmulo de Luke em direção a uma pilha de lixo próxima.
    Ele está prestes a falar quando o som de passos o interrompe."

    $Kota.change("emotion", "surprise")

    "Uma sombra se move atrás de uma das mesas. Algo respira no silêncio pesado."

    "Kota olha para Luke. Luke olha para Kota."

    $Kota.change("emotion", "puzzled")
    show Kota:
        ease 1.0 xalign 0.3
    kota "...Bem, vamos então. Vamos ver o que é."

    $Luke.change("arm", "hip")
    show Kota:
        ease 1.0 xalign 0.6
    show Luke:
        ease 1.0 xalign 0.1
    "Kota se aproxima da fonte desses sons. Luke, enquanto isso, leva um
    momento para pegar um peso pesado de papel antes de seguir."

    show Kota:
        ease 1.0 xalign 0.9
        ease 1.0 xalign 1.0
        ease 1.0 xalign 1.3
        ease 1.0 xalign 1.4
        ease 1.0 xalign 1.7
        ease 1.0 xalign 1.8
        ease 1.0 xalign 2.1
    show Luke:
        ease 1.0 xalign 0.4
        ease 1.0 xalign 0.5
        ease 1.0 xalign 0.8
        ease 1.0 xalign 0.9
        ease 1.0 xalign 1.2
        ease 1.0 xalign 1.3
        ease 1.0 xalign 1.4
        ease 1.0 xalign 1.7
        ease 1.0 xalign 2.0
    pause 5

    "Devagar. Com cautela. Quietos. Eles avançam em direção ao que quer que esteja lá com eles."

    show Kota:
        ease 1.0 xalign 2.0
    show Luke:
        ease 1.0 xalign 2.0
    pause 1
    hide Kota
    hide Luke

    "Luke olha para Kota. Kota olha para Luke. O dragão acena com a cabeça e uma contagem silenciosa começa."

    "Um."

    "Dois."

    "Três!"

    play sound "sfx/chair.ogg"

    "Kota agarra a mesa e a joga para longe da parede com um alto rugido
    enquanto Luke avança com um guincho de predador e sua arma erguida."

    luke "Hiyaa!"

    pause 1.0
    play music "music/Obviously.ogg"

    cobaltq "EEP!"

    show cobalt_left:
        xalign 1.6 yalign 1.05
        ease 1.0 xalign 0.5


    "A criaturinha recua e grita quando seu esconderijo é arrancado.
    Com um grito de medo, ela tenta se arrastar de volta para o abrigo da mesa."

    show cobalt_left:
        ease 0.15 yalign 1.0
        ease 0.2 yalign 1.05

    cobaltq "Cai fora!"

    show cobalt_left:
        ease 1.0 xalign -0.4

    "Algo bate nas costas de Luke, envolvendo os braços finos em volta do pescoço
    do grifo com um grito de guerra agudo. E então a pilha de lixo explode
    e outra criaturinha se joga em Kota."

    $Luke.change("arm", "pointing")
    show Luke:
        xzoom 1 xalign 2.0 yalign 1.0
        ease 1.0 xalign 0.7
        xzoom -1
        ease 1.0 xalign 2.0
    show cobalt_middle behind Luke:
        xzoom -1 xalign 1.5 yalign 1.0
        pause 0.3
        ease 1.0 xalign 0.5
        xzoom 1
        ease 1.0 xalign 1.5

    "O pandemônio preenche a sala. Grunhidos e gritos. Raspadas e arranhões.
    Kota tropeça e cai sobre um corpo de membros finos, e Luke cambaleia e grunhe
    a cada golpe de minúsculos punhos no topo de sua cabeça."

    "Mas, por mais que os dois tenham sido surpreendidos por seus agressores, eles são maiores e
    mais fortes."

    "Luke estende a mão para agarrar a coisa presa em suas costas e, mesmo enquanto a criatura
    se contorce e rosna em suas mãos, o grifo consegue tirá-la."

    $Kota.change("emotion", "angry")
    $Kota.change("rightarm", "raised")
    show Kota:
        xalign 2.0 xzoom -1 yalign 1.0
        ease 3.0 xalign -0.9
    show cobalt_right:
        xzoom -1 xalign 1.5 yalign 1.0
        ease 3.0 xalign -1.5

    "Kota, enquanto isso, rola no chão para agarrar a coisinha encolhida que o fez tropeçar
    com a dobra de um braço. A criatura que bateu na lateral do dragão
    tenta fugir mas, apesar de seu tamanho, Kota é rápido."

    show cobalt_left:
        xzoom -1
        ease 1.0 xalign 0.4
        ease 0.2 yalign 1.2 xalign 0.45
        ease 0.4 yalign 1.0 xalign 0.5
        pause 0.5
        xzoom 1

    "Ele surge como uma maré para engolfar o inimigo em fuga."

    show cobalt_middle:
        xzoom -1
        ease 2.0 xalign 0.5
        xzoom 1
    show cobalt_left:
        xzoom 1
        ease 0.5 xalign 0.3
    show cobalt_right:
        xzoom 1
        ease 2.0 xalign 0.7

    pause 2.0
    $Luke.change("arm", "hip")
    $Luke.change("emotion", "annoyed")
    $Kota.change("rightarm", "relaxed")

    show Kota:
        xzoom 1
        ease 2.0 xalign -0.4
    show Luke:
        xzoom 1
        ease 2.0 xalign 1.4


    "A dupla finalmente se levanta, machucada e despenteada, mas vitoriosa. Seus oponentes se contorcendo
    soltam guinchos estridentes de pânico enquanto são carregados e dispostos próximos à parede de obisidiana."

    show cobalt_middle:
        ease 0.1 yalign 1.01
        ease 0.1 yalign 1.0
        repeat
    show cobalt_left:
        ease 0.1 yalign 1.01
        ease 0.1 yalign 1.0
        repeat
    show cobalt_right:
        ease 0.1 yalign 1.01
        ease 0.1 yalign 1.0
        repeat

    "Quando as criaturinhas olham em volta procurando por uma rota de fuga e veem o dragão e o grifo
    as encurralando, elas choram e se amontoam enquanto acovardam-se no chão."

    show cobalt_left:
        ease 0.3 yalign 1.04

    cobaltq "D-deixa a gente ir!"

    show cobalt_right:
        ease 0.3 yalign 1.04

    cobaltq "A-a gente não fez por mal!"

    show cobalt_middle:
        ease 0.3 yalign 1.04

    cobaltq "Por favor,{w=0.2} n-não nos machuque!"

    show cobalt_middle:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.04
        repeat
    show cobalt_left:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.04
        repeat
    show cobalt_right:
        ease 0.1 yalign 1.05
        ease 0.1 yalign 1.04
        repeat
    $Kota.change("emotion", "puzzled")

    "O dragão e o grifo olham para os diminutos seres reptilianos."

    "Luke observa os trapos de roupa que o trio está vestindo — pegos do lixo,
    sem dúvida — enquanto Kota se irrita com a visão das escamas pálidas e feições retraídas."







    if first_guest == "Luke":


        $Luke.change("emotion", "wink")
        "É o grifo quem finalmente suspira e se agacha para se aproximar dos lagartos trêmulos."

        show Luke:
            ease 2.0 xalign 1.2 yalign 2.0

        show cobalt_middle:
            ease 2.0 xalign 0.4
        show cobalt_left:
            xzoom -1
            ease 2.0 xalign 0.2
        show cobalt_right:
            ease 2.0 xalign 0.55

        luke "Ei, relaxem, carinhas. A gente não vai machucar vocês."

        $Kota.change("leftarm", "raised")

        "Kota resmunga, mas acena com a cabeça enquanto se limpa e ajeita a roupa."

        $Kota.change("leftarm", "relaxed")
        $Luke.change("arm", "pointing")

        "O grifo, enquanto isso, estende uma das mãos em direção ao trio de lagartos.
        Eles recuam e choramingam, mas não se movem quando ele coloca a palma da mão sobre a cabeça do que está no meio."

        $Luke.change("emotion", "happy")
        luke "Isso, aqui, tá vendo?"

        luke "Tadinhos.{w} Vocês tão só pele e osso!"

        show cobalt_middle:
            ease 0.6 yalign 1.03
        show cobalt_left:
            ease 0.6 yalign 1.03
        show cobalt_right:
            ease 0.6 yalign 1.03

        "Enquanto a mão do grifo acaricia e afaga os lagartos um de cada vez,
        seus corpos rígidos relaxam e param de tremer."

        $Luke.change("emotion", "sad")
        luke "...Ei, pensando bem agora,{w=0.2} vocês provavelmente são as criaturas roubando
        coisas da cozinha, não é?"

        "Um guincho de culpa escapa do lagarto gordinho."

        show cobalt_left:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "A-a gente precisava.{w=0.2} Faz muito tempo que a gente não via tanta comida."

        show cobalt_middle:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "Passamos fome por tanto tempo, e..."

        show cobalt_middle:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "Não vamos fazer de novo,{w=0.2} de verdade!{w=0.2} Só deixa a gente ir, e —"

        $Luke.change("emotion", "surprise")
        luke "Epa, calma aí. Eu não sou de deixar alguém em necessidade passar fome."

        $Luke.change("emotion", "happy")
        luke "Vocês venham comigo e eu vou encher essas barrigas mais rápido que um balde
        em temporada de furacão."

        show cobalt_right:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "M-mesmo…?"

        show cobalt_middle:
            ease 2.0 xalign 0.6
        show cobalt_left:
            xzoom -1
            ease 2.0 xalign 0.4
        show cobalt_right:
            ease 2.0 xalign 0.75

        "Por fim, o trio ergue os olhos para o grifo, tentando avaliar a sinceridade
        de suas palavras. O prospecto de comida--comida que eles nem precisam roubar--parece
        acalmá-los quase tanto quanto os dedos de afago de Luke."

        $Luke.change("emotion", "wink")
        $Luke.change("arm", "hip")
        show Luke:
            ease 2.0 yalign 1.0 xalign 1.3
        "Luke lança um olhar para Kota. Uma expressão tímida cruza seu rosto e ele rapidamente
        pigarreia e abaixa o olhar em constrangimento."

        $Luke.change("emotion", "neutral")

    else:

        $Kota.change("emotion", "sad")
        "É o dragão quem finalmente suspira e cruza os braços, olhando para os lagartos trêmulos."

        $Kota.change("rightarm", "raised")
        $Kota.change("leftarm", "raised")
        show Kota behind cobalt_left, cobalt_middle, cobalt_right:
            ease 2.0 xalign -0.2 yalign 2.0

        show cobalt_middle:
            xzoom -1
            ease 2.0 xalign 0.55
        show cobalt_left:
            xzoom 1
            ease 2.0 xalign 0.45
        show cobalt_right:
            xzoom -1
            ease 2.0 xalign 0.75

        kota "Silêncio agora, pequeninos.{w=0.2} Não vamos machucar vocês, eu prometo."

        $Kota.change("arm", "pointing")
        $Luke.change("emotion", "annoyed")
        luke "Diz isso pra minha cabeça dolorida."

        $Kota.change("arm", "hip")
        $Kota.change("emotion", "angry")
        $Kota.change("rightarm", "relaxed")
        $Kota.change("leftarm", "relaxed")
        "Kota atira um olhar em Luke e o grifo volta a ficar de mal humor enquanto esfrega sua cabeça machucada."

        $Kota.change("leftarm", "raised")
        kota "Eu sou Kota, um funcionário deste hotel.{w} Digam-me, são vocês que andam roubando comida lá de cima?"

        show cobalt_middle:
            ease 0.6 yalign 1.03
        show cobalt_left:
            ease 0.6 yalign 1.03
        show cobalt_right:
            ease 0.6 yalign 1.03

        $Kota.change("leftarm", "relaxed")
        "Depois de fungar e limpar o focinho, o lagarto de escamas mais escuras fala."

        show cobalt_middle:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "A-a gente precisava.{w=0.2} A gente passou fome por tanto tempo,{w=0.2} e…"

        show cobalt_middle:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "Não vamos fazer de novo,{w=0.2} de verdade!{w=0.2} Só deixa a gente ir embora, e…{w=0.2} e…"

        "O lagarto olha para Kota e vagueia. Seus olhos amarelos examinam o
        homem ameaçador por um longo momento, depois se arregalam."

        show cobalt_middle:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "Ah…{w=0.2} a-ah…"

        show cobalt_middle:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "Um{w=0.2} dragão…!"

        $Kota.change("emotion", "surprise")
        $Luke.change("emotion", "surprise")
        "Os outros dois lagartos ficam em silêncio, como se a palavra fosse um gatilho.
        Eles também erguem a cabeça para olhar na direção de Kota e a mesma expressão de espanto
        que se espalha no rosto de seu companheiro de escamas mais escuras também se espalha nos rostos deles."

        show cobalt_left:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "Dragão?{w=0.2} É um dragão mesmo?"

        show cobalt_right:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "É sim! É um dragão!"

        $Luke.change("emotion", "annoyed")
        $Kota.change("emotion", "puzzled")
        "Os três lagartos piam de alegria e seus focinhos se abrem em sorrisos largos, dentuços e radiantes."

        show cobalt_right:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "Um dragão! Um dragão! A gente finalmente encontrou um dragão!"

        show cobalt_left:
            ease 0.2 yalign 1.0
            ease 0.3 yalign 1.03
        cobaltq "...Espera. Isso significa…{w=0.2} que a gente…"

        show cobalt_left:
            ease 0.5 xalign 0.2
        show cobalt_middle:
            ease 0.5 xalign 0.35
        show cobalt_right:
            ease 0.5 xalign 0.5

        show Kota:
            ease 1.0 yalign 1.0 xalign -0.25
        $Kota.change("emotion", "surprise")
        "Os olhos piscando se arregalam em realização, e então horror. O trio se joga no chão
        aos pés de Kota e se agarra aos tornozelos do dragão."

        cobaltq "Desculpa! A gente não sabia!"

        $Kota.change("emotion", "sad")
        kota "De verdade, está tudo bem. Calma, pequeninos, calma…"

        "Kota olha dos lagartos choramingando para Luke, sua própria expressão perplexa.
        Ele murmura uma vaga consolação para o trio enquanto se inclina para dar-lhes tapinhas suaves
        entre seus chifres."

    luke "Então, é…{w=0.2} o que são esses caras?"

    kota "Acredito ter uma ideia. Independentemente disso, eles não são uma ameaça."

    $Kota.change("emotion", "neutral")
    kota "Na verdade, parece que eles precisam de abrigo tanto quanto qualquer outro hóspede do hotel."

    luke "É."

    $Luke.change("emotion", "cocky")
    luke "Nesse caso, acho que a gente devia contar ao [player_name] e ao Astério sobre eles."

    "Com a menção do nome do minotauro, o olhar de Kota cai para o chão."

    $Kota.change("emotion", "sad")
    kota "De fato…"

    $Luke.change("emotion", "annoyed")
    luke "Qual o problema agora, Azulzinho?"

    kota "Não é nada. Embora…"

    if first_guest == "Luke":

        show Kota:
            xzoom -1
            ease 1.0 xalign -0.4

        "Kota retorna para a mesa no outro lado da sala, pegando o arquivo da pasta
        que estava folheando antes da interrupção."

    else:
        "Kota se retira dos suplicantes lagartos, dando-lhes instruções
        silenciosas para ficarem onde estão por um momento."

        show cobalt_middle:
            ease 2.0 xalign 0.6
        show cobalt_left:
            ease 2.0 xalign 0.4
        show cobalt_right:
            ease 2.0 xalign 0.75

        "Eles gorjeiam em reconhecimento obediente, observando junto com Luke enquanto
        o dragão retorna para a mesa."

        show Kota:
            xzoom -1
            ease 1.0 xalign -0.4

        "Kota pega o arquivo da pasta que estava folheando antes da interrupção."

    show Kota:
        xzoom 1
        ease 1.0 xalign -0.1

    $Kota.change("emotion", "puzzled")
    kota "Se importaria de confirmar algo para mim, Sr. Walker?"

    $Kota.change("rightarm", "raised")
    $Luke.change("emotion", "surprise")
    "Ele estende a pasta para o grifo."

    luke "Hã, claro?{w} Do que cê tá precisando agora?"

    kota "Apenas leia, e acho que entenderá."

    show Luke:
        ease 2.0 xalign 0.6

    show cobalt_middle:
        ease 2.0 xalign 1.0
        xzoom -1
    show cobalt_left:
        ease 2.0 xalign 0.9
        xzoom 1
    show cobalt_right:
        ease 2.0 xalign 1.15
        xzoom -1

    $Luke.change("emotion", "wink")
    luke "Beleza…"

    "Quando o dragão entrega os documentos, Luke começa a folheá-los."

    scene bg black
    with Dissolve(1)

    luke "..."

    luke "..."

    luke "...ãhn?"

    luke "Que…{w=0.2} o que diabos é isso?"

    pause 2.0

    play music "music/IslandJourney.ogg" fadeout 1.0 fadein 1.0
    scene bg oldquarters
    with Dissolve(2.0)

    "Ao descobrir a falta das cobiçadas sobras, um homem deve ascender frente ao desafio.
    Depois de um lanche improvisado para você e Astério, você começa a trabalhar no mais divino dos alimentos: pão."

    "Passe o dedo sobre uma xícara cheia de farinha para se livrar do excesso. Menos que uma colher
    de sal, água e fermento misturados para trazê-lo de volta à vida."

    "Cada ingrediente na quantidade certa e no lugar adequado."

    "Misture tudo. Primeiro bolinhas desiguais, depois cordas meio misturadas. Pegajosas o suficiente para formar
    uma teia do indicador ao polegar, firme o suficiente para ser arrancada."

    "Continue misturando, ficará entre seus dedos como uma memória dos tempos em que nossos
    ancestrais ficaram com as mãos grudentas."

    "O suor escorre de sua testa. Lute com uma toalha para enxugar, deixe um fio de massa sobre ela."

    "Espere, deixe o pão crescer, amasse. Pegue suas bordas e dobre-o sobre si mesmo
    quatro, oito, doze, dezesseis vezes."

    "Deixe dormir dentro de uma bacia. Demora um tempo para o pão crescer o suficiente
    para empurrar a tampa, mas eventualmente a hora chega. Um forte cheiro de álcool deve subir."

    "Sove-o, sinta como ele resiste ao seu aperto até que seja dobrado sobre si mesmo
    em uma bola elegante e lisa, quase explodindo nas partes amarradas."

    "Sove e descanse até que esteja pronto. Quantas vezes for preciso."

    "Há algo divino em todas as etapas do cozimento. A suavidade da farinha,
    o calor diminuto da levedura ativada, o cheiro de lacrimejar os olhos da fermentação alcoólica."

    "A principal delas é o aroma do pão no forno e a alegria de compartilhá-lo."

    $Asterion.change("emotion", "tired")
    show Asterion:
        xzoom 1 xalign 0.5 yalign 0.5 zoom 1
    with Dissolve(2)

    "Olhe para cima. Há alguém no sofá — seu servo, colega de quarto, parceiro de negócios,
    querido hóspede. A mente de um homem no corpo de um híbrido."

    "Há algo divino nos olhos. Nos seus, nos dele, nos olhos da humanidade e de todas
    as belas feras humanoides com as quais nosso império foi construído."

    "Não faz muito tempo que você conhece este homem chamado Astério. Mas a cadência de sua voz,
    a reverência em suas palavras, as alterações em seu rosto, agora pode haver familiaridade."

    "Os humores dele são mais claros em sua mente. Às vezes você até se pega antecipando
    o próximo passo da dança dele."

    "Que ritual pagão, cozinhar para o minotauro da lenda enquanto ele medita.
    Seus dedos brutos roçam e batem no tablet até que ele encontra um problema que não consegue resolver."

    $Asterion.change("emotion", "sad")

    "A postura dele fica rígida e você sabe bem como abordá-lo — acontece a cada vinte minutos,
    combina bem com os tempos de descanso da massa."

    "Ele está quieto agora, mais do que quando você o deixou. Qualquer tentativa de extrair alguma verdade
    é recebida com um grunhido desorientado."

    $Asterion.change("emotion", "tired")

    "Dê-lhe tempo — vocês dois o têm de sobra, afinal. Volte ao seu ritual
    pagão de sovar massa para o homem taciturno."

    "Leve o dever a sério. Há algo divino em jogo, na culinária, nos olhos e nas mãos da humanidade.
    Tendo a sorte posta a sorrir, você também carregará essa divindade em si mesmo."

    "Deixe o tempo passar, coma e beba. Deixe o homem descansar, seu coração dança em seu próprio ritmo estranho."

    "É isso o que você estava procurando, eu me pergunto? Por que você, mestre dos mestres, veio a este deserto lamentável?"

    "Aqui o senhor pode invocar diamantes na ponta dos dedos, mas não é por isso que você foi
    seduzido a possuir esta terra."

    "Talvez fosse isso que você estava procurando — um domínio onde um homem pode conduzir o ritual
    pagão de encontrar uma alma gêmea."

    "Há algo de divino em conceder graça a uma alma enferma. E então você deve cozinhar enquanto
    ele descansa. Você é o mestre e, por esta tarde silenciosa, ele é seu hóspede."

    "Escravize-se no forno, abra o vinho, derrame seu conteúdo em sua melhor taça,
    chame o homem para a festa mesmo que ele esteja sem apetite."

    show Asterion:
        ease 1.0 yalign 1.6
    pause 1
    show quartertable
    with Dissolve(1)

    pause 1

    "Ele come em silêncio, você cantarola e bate os pés em um ritmo que apenas Deus conhece.
    Você troca olhares e pondera como os olhos dele sempre parecem muito úmidos."

    "As narinas de Astério dilatam conforme ele deixa sair todo o ar velho e estagnado acumulado em seus pulmões.
    Seus ombros caem enquanto um arrepio sobe por sua espinha, deixando uma trilha de cabelos em pé."

    "Seu peito vibra um estrondo inaudível, os cascos arranham contra o chão.
    Você sente uma batida cinco vezes antes da voz dele chegar."

    pause 1.0

    $Asterion.change("emotion", "sad")

    asterion "Eu não aguento mais{w=0.3}, não consigo mais fingir."

    pause 1.0

    you "O que você quer dizer?"

    asterion "Eu não mereço nada...{w=0.3} disso."

    $Asterion.change("emotion", "tired")

    "O minotauro olha através de você. Olhos turvos, cansados e sem medo."

    you "Desculpe, não entendi."

    $Asterion.change("emotion", "mooing")

    "Ele abre a boca e respira fundo. De seu lugar na mesa de jantar,
    você consegue ouvir um chiado."

    $Asterion.change("emotion", "tired")

    "Ele lambe os lábios, mas a língua está igualmente seca. Junta as mãos em concha e as esfrega para aquecê-las."

    "Hoje sua voz não está tão tensa como de costume. Cada sílaba flui sem ritmo ou dança."

    asterion "Eu sou um miserável, [player_name]. Nascido e morto como um. Sentenciado pelos deuses por minha covardia."

    "O minotauro aperta seu antebraço e gira. Ele morde a bochecha, deformando-a para dentro,
    e então sua mandíbula fica tensa enquanto ele testa seus próprios limites."

    asterion "Quando você saiu, continuei lendo sobre mim. Minha própria história.
    Nada que eu não soubesse, mas foi interessante ver tudo exposto."

    asterion "Se importaria em ouvir? Tudo vindo da própria besta."

    $Asterion.change("emotion", "mooing")

    "O minotauro respira fundo com dificuldade. Ele aperta o antebraço com mais força,
    o torce, e isto destrava sua garganta mais uma vez."

    $Asterion.change("emotion", "tired")

    "Uma gota de suor escorre de sua testa até o queixo, depois goteja para suas roupas.
    Suas orelhas e cauda balançam para frente e para trás, como se vespas estivessem flutuando em torno delas."

    "Entre vocês dois, há apenas uma pequena mesa de madeira, com cerca de um braço de comprimento.
    Seus cantos já foram afiados um dia, agora estão atenuados pelo tempo e desgaste."

    "Você ignora a pergunta dele; em vez disso, questões mais urgentes vêm à tona.
    O torcer de seu braço, o chiado de sua garganta, o medo sombrio como a morte o consumindo."

    "Ele está ao alcance de seu braço, mas a distância é intransponível. E sua pergunta,
    ele podendo prosseguir ou não, é de todas as formas a errada."

    "Você acena com a cabeça e ele começa."

    $Asterion.change("emotion", "sad")

    asterion "Fui condenado a esta terra por causa de minha covardia, permiti que um homem me matasse."

    asterion "Minha mãe perdeu a si mesma durante o meu nascimento. Dar vida a um monstro é razão
    suficiente para perder a cabeça."

    asterion "Eu tinha irmãos, demais para conseguir contar, como você pode imaginar, o corpo da minha mãe
    não pôde suportar outro depois do meu nascimento."

    asterion "Meu guarda, ele era meu amigo. Seu nome era Froneu."

    asterion "Não me era permitido trabalhar, mas eu me fazia útil. Meu pai, rei e sacerdote supremo
    de nossa fé, tirava meu sangue para trazer fertilidade às colheitas do meu povo."

    asterion "Nas histórias que li sobre mim, eles me chamaram de canibal. E aqui está a verdade,
    [player_name]: de fato eu era."

    asterion "Um dia minhas três irmãs me enganaram para comer carne bovina. Eu sou meio touro,
    afinal. Fazer isto é tanto canibalismo quanto comer um humano."

    asterion "Fui ensinado a evitar, mas eles me enganaram. Daquele momento em
    diante minha vida foi à ruína."

    asterion "Fui enviado para o labirinto ondi vivi o resto de meus dias.
    Era uma punição, sim, mas também uma medida de segurança para quaisquer medos que eles tivessem."

    asterion "Também era um dever, fui enviado lá para cuidar de um templo e manter uma relíquia segura."

    asterion "Eu cuidei da chama, [player_name], por anos. Apenas uma vez ela se apagou
    e não foi por negligência, embora, em retrospecto, eu desejaria que tivesse sido assim."

    $Asterion.change("emotion", "tired")

    asterion "Eu matei um homem sagrado. Seu filho o trouxe até mim na esperança de que eu pudesse
    acabar com sua miséria. E eu o fiz. Mas foi um crime imperdoável."

    asterion "Eu estava manchado com isto. Tirei uma vida que o próprio Zeus havia marcado
    como eterna. O que eu poderia ter feito depois disso?"

    asterion "Mas o filho do homem me disse palavras doces. Um redentor viria, ele disse.
    Então eu esperei, e ele chegou."

    asterion "Eu dei minha vida. Covardia, é como foi marcada. Uma desgraça ignóbil,
    na melhor das hipóteses, para um príncipe dar as costas a uma lâmina sem lutar com bravura."

    $Asterion.change("emotion", "relieved")

    asterion "Mas em Hades eu encontrei paz. Meu irmão, Androgeu, me defendeu e os juízes
    dos mortos me inocentaram de todas as acusações."

    $Asterion.change("emotion", "tired")

    asterion "Desfrutei de três anos de liberdade em Hades antes de ser sequestrado para este domínio
    para cumprir a sentença que os deuses consideravam adequada."

    asterion "Durante séculos, os mestres fizeram o que bem entendiam, até que alguém achou por bem encerrar minhas provações."

    $Asterion.change("emotion", "sad")

    asterion "Eu estou podre, [player_name]. Quando fico ferido, é isto que sai de mim, podridão e decadência. Eu estou morto."

    asterion "Eu sei o que vai acontecer. Você não tem que mentir para si mesmo sobre quem ou o que eu sou.
    Tampouco precisa me enganar ou prolongar. Por... bondade..."

    asterion "Você vai se cansar de mim. Como todos se cansam, eventualmente. Não tenho disposição para isso —
    ser um brinquedo abordado como se fosse um homem."

    asterion "Você se mostrou gentil. Mais do que a maioria dos mestres.
    Mas eu sei que é apenas uma questão de tempo até você ficar entediado e ver que
    é tolice cuidar de um escravo para si."

    asterion "Esta antecipação, a tensão, eu não consigo suportar."

    pause 1
    $Asterion.change("emotion", "tired")

    asterion "A dor, por outro lado, eu dominei."

    asterion "Então, por favor. Vamos acabar com esse jogo, eu não aguento mais."

    $Asterion.change("emotion", "sad")

    asterion "Faça o que quiser comigo."

    pause 2.0

    if Build3Ending == 'neutral':
        "Você percorreu um longo caminho em sua jornada, bom mestre."
    else:
        "Você percorreu um longo caminho em sua jornada, gentil mestre."

    "Herdou um antigo tesouro da humanidade, investigou seu funcionamento interno, curou
    o zelador, superou a pretensão da cobra, deu as boas-vindas a errantes virtuosos e disformes."

    "E ainda assim, não lhe custou muito. Suas ações foram pequenas e corriqueiras.
    Você não sangrou ou se exauriu com isto."

    "Mas a bondade nem sempre vem de sangue ou suor. Às vezes, fazer a coisa certa
    quando confrontado com tentações infinitas é digno de nota o suficiente para ser heróico."

    menu:
        "Você poderia ter cedido aos seus impulsos mais básicos.":
            "Havia um momento, não muito tempo atrás, em que você poderia ter cedido aos seus impulsos mais básicos."

            "De fato o potencial para a violência existe em todos os humanos, ele se espreita e salta em
            momentos inesperados. Pode agarrar os olhos de uma pessoa e levar alguém a machucar, torcer,
            matar por mera curiosidade."

            "Mas esse período acabou. Suas escolhas o protegem contra tais pensamentos."


        "Para se tornar um homem, um menino sacrifica parte de seu potencial para causar danos.":
            "Um recém-nascido carrega possibilidades infinitas para o bem e o mal."

            "Mas o menino sacrifica potencial em seu caminho para a vida adulta, afinal.
            Como um homem, seu potencial para o mal é cortado por todas as escolhas que o pesam."

        "Essas pequenas ideias espontâneas que rangem seus dentes.":

            "Deve-se estar ciente de sua própria coleção particular de demônios nascidos
            dos excessos concedidos a você."

            "E, no seu caso, esses pensamentos sombrios — a emoção de impor sua vontade
            a uma vítima relutante, de tomar sem cuidado ou preocupação,
            de deixar a natureza mais selvagem tomar conta — foram relíquias que você sacrificou com prazer."

        "Decisões...":

            "Decisões. Todas as escolhas que você fez levaram a este exato momento,
            onde apenas um caminho é possível — não porque você não tem o poder, mas porque algumas
            algemas do certo e errado se apoderaram."

            "Mas, será que carregar este peso adicional não o deterá, e sim apenas lhe dará força
            para carregá-lo em diante?"

    if Build3Ending == 'neutral':
        "Então levante-se, bom mestre, e revele-se."
    else:
        "Então levante-se, gentil mestre, e revele-se."

    you "Receio que você não tenha entendido quem eu sou."

    pause 1.0

    $Asterion.change("emotion", "tired")

    asterion "Você é humano."

    you "Você também. Já não discutimos isso antes?"

    pause 1.0

    you "O que você está me pedindo, eu me recuso a fazer.{w} Não é uma questão de o que eu sou,
    o que um humano é. É sobre {i}quem{/i} eu sou."

    you "Eu tenho sido gentil com você, Astério. Não nos conhecemos há muito tempo,
    mas eu não estou só te colocando para cima ou brincando com você para te chamar de meu amigo."

    you "Bem, você quer que eu acabe com a sua dúvida e te machuque. Eu não sei o que os mestres anteriores
    podem ter feito ou como eles agiram, mas se tratanto de mim... Eu simplesmente não vou fazer isso."

    you "Eu não vou te machucar. E eu não digo isso como um ato de gentileza ou caridade — é simplesmente quem eu sou."

    you "Então, se fosse para eu ser firme com você sobre qualquer coisa, deveria ser isso. Não. Eu não vou."

    you "Talvez você esteja certo no sentido de que a dor que posso infligir a você seja mais suportável
    do que a angústia que você sente."

    you "Mas eu não sou esse homem. Eu não vou desistir do que acredito ser certo."

    you "Ser gentil com você não é um jogo. É simplesmente... básico. É decente. Apenas isso."

    pause 1.5

    $Asterion.change("emotion", "sad")
    pause 1.0

    you "Você me considera um amigo, Astério?"

    pause 2.0

    you "Eu percebo que essa é uma pergunta complicada. O poder que eu tenho sobre você não é nada
    senão absoluto, mas escute o que eu disse."

    you "Eu não vou te machucar. Isso não é caridade ou piedade. É a coisa certa e vai continuar
    assim nem que eu tenha que me algemar para que isso aconteça."

    $Asterion.change("emotion", "tired")

    "A respiração dele engata com a menção de \"algema\"."

    you "Mas eu tenho que te fazer uma pergunta. Tudo pelo que passamos até agora, tudo isso foi
    uma fachada de mestre e servo..."

    you "...ou fomos eu e você, Astério e [player_name]?"

    "O minotauro pisca e sente o veludo ao redor deles na noite passada, quando eles
    se abraçaram. Como ele esqueceu o som de seus próprios passos."

    you "Você me contou sobre a missão do hotel: dar lugar a quem não tem para onde ir."

    you "Estou lhe dizendo aqui e agora, de forma inequivocada que juro por isso. Eu
    vou manter a missão."

    you "E você... Você também não tem para onde ir. Portanto, esse lugar deve ser um
    lugar para você também. Eu não vou te machucar."

    "A bochecha do minotauro se deforma quando ele a morde. Ele afunda as unhas no próprio antebraço e as
    arrasta como se estivesse torcendo a pele."

    show blackback behind Asterion:
        alpha 0.6
    with Dissolve(2)
    $Asterion.change("emotion", "mooing")

    "Ele respira fundo."

    $Asterion.change("emotion", "tired")

    "\"Ó Senhor dos Hóspedes,\" ele pensa, \"que invenção enviou este homem até mim?\""

    "\"Destino, seria ele mais uma das provações planejadas para me destruir? Ou, Dama Héstia,
    você teve pena de mim uma última vez?\""

    "\"Ou foi sua graça, Arrasador Poseidon? Por favor, dê-me um sinal de que
    isto é verdade e não mais um sofrimento que devo suportar.\""

    hide blackback
    with Dissolve(2)

    you "Podemos fazer isso juntos. Mas devo pedir algo de você. Me veja como eu mesmo,
    [player_name], e não como \"Mestre\"."

    you "Eu não estava falando sobre nos tornar parceiros de negócios? O que foi que você me disse,
    que o labirinto não tornaria isso oficial?"

    you "Algumas vezes você se referiu a toda essa terra como \"o labirinto,\" certo?
    Suponho que era assim que deveria ser chamado."

    you "Mas eu não vejo um labirinto, isso é claramente um hotel. Essa é a verdade
    que você construiu e mesmo que haja contratos e leis por trás disso, não vai deixar de ser um hotel."

    you "Então, importa como é chamado, que palavra damos a ele? Os fatos não têm precedência?"

    you "Então que se foda o labirinto e suas regras. Vamos ordenar os fatos e isso faz a realidade.
    Não precisamos de um contrato para fazer as coisas funcionarem."

    you "Podemos simplesmente considerar como verdade. Diga que você é meu parceiro de negócios, vá em frente, e em pouco tempo
    todo mundo vai acreditar nisso — porque é a verdade, mais do que qualquer pedaço de papel jamais será."

    you "Se minha palavra significar algo, se eu puder cumprir minha promessa, então você pode e será meu parceiro."

    $renpy.music.set_volume(0.0, delay=2.0, channel='music')

    scene bg black
    with Dissolve(0.1)

    "O silêncio estrondoso e avassalador aperta o coração do minotauro, esmaga seus pulmões
    e lava tudo o que [player_name] poderia dizer."

    "Ele tosse, mas não percebe, e quando abre os olhos..."

    scene bg oldquarters
    show Androgeos_serious:
        xalign 0.5 yalign 1.0
    with Dissolve(1.0)

    androgeos "Você não deveria chorar tão cedo, nem ouviu meu discurso."

    androgeos "Teremos todo o tempo para colocar a conversa em dia assim que eu salvar você, Estrelinha."

    hide Androgeos_serious

    show Androgeos_smile:
        xalign 0.5 yalign 1.0

    androgeos "Agora, não se preocupe, você fez uma grande bagunça, mas eu o conheço melhor do que você mesmo.
    Mostrarei a Suas Excelências exatamente que tipo de pessoa você é e foi."

    androgeos "Pelo peso de minhas palavras e valor de minhas promessas, não demorará
    muito para que estejamos saindo daqui, meu irmão."

    androgeos "Suas Excelências, devo começar?"

    hide Androgeos_smile
    with Dissolve(3)

    scene bg black
    with Dissolve(1)

    "Não, ele não chorou.{w} Ele não irritou os deuses.{w} Ele não foi enviado a cem
    labirintos diferentes."

    "E, durante aquela noite quando seu guarda o visitou, ele não rejeitou seu pedido."

    "Froneu" "Abandone o labirinto. Podemos adorar aos deuses da mesma forma, prestar o devido
    respeito em nosso próprio lar e construir um santuário ao redor."

    "Froneu" "Se minhas palavras e promessas alguma vez tiveram peso, então venha, Astério,
    e eu o acompanharei como meu irmão."

    scene bg oldquarters
    $Asterion.change("emotion", "crying")
    show Asterion:
        xalign 0.5 yalign 1.2
    show quartertable
    with Dissolve(2)

    pause 2.0

    $renpy.music.set_volume(1.0, delay=2.0, channel='music')

    asterion "Sim."

    $Asterion.change("emotion", "surprise")
    show Asterion:
        ease 0.4 yalign 1.0

    "O minotauro olha para você como se seu rosto o pegasse desprevinido, assim como a própria realidade
    volta a rugir em sua mente."

    $Asterion.change("emotion", "mooing")

    "Ele respira fundo, mas desta vez não engata — na verdade, ele supera todo o ar estagnado.
    Um encher de pulmões tão fresco que traz umidade aos olhos."

    $Asterion.change("emotion", "sad")

    pause 1.5

    asterion "Sinto muito por meu desrespeito. Eu fui...{w=0.2} imprudente durante nossa conversa,
    [player_name]."

    you "Não tem motivo para pedir desculpas. Eu agradeceria se você falasse comigo com essa franqueza com
    mais frequência."

    $Asterion.change("emotion", "tired")

    asterion "Receio não poder ter outra conversa como esta tão cedo, [player_name].
    Esta foi a coisa mais difícil que fiz desde..."

    pause 1.0

    $Asterion.change("emotion", "sad")

    asterion "Melhor não ir até lá."

    you "Sim. Não tem por que cutucar essas velhas memórias."

    pause 1.5

    asterion "Vou precisar de algum tempo."

    you "Não tem problema. Nós temos todo o tempo do mundo, certo?"

    $Asterion.change("emotion", "horny")

    asterion "Temos."

    pause 2.0

    you "Lembro de você mencionando que eu te lembrava de um amigo. É aquele tal de \"Froneu\"
    de quem você falou mais cedo?"

    $Asterion.change("emotion", "sad")

    "O minotauro olha para suas mãos. A direita se acomoda em cima da esquerda e a coça,
    suas unhas cravando-se como se tentasse desenterrar as veias."

    you "Posso perguntar por que te lembro dele?"

    asterion "Você é o Mestre, claro que é..."

    you "Por favor, pare com isso. Eu sou uma pessoa, só me trate como uma."

    $Asterion.change("emotion", "neutral")
    pause 1.0

    you "Nada disso é sobre ordens isso, Mestre aquilo. Se você não quer responder, tudo bem,
    fim da história."

    $Asterion.change("emotion", "sad")

    asterion "É por causa de coisas assim que você me lembra dele."

    asterion "Ele era meu guarda, esta era sua função oficial. Mas na verdade ele foi meu amigo
    e parceiro de brincadeiras primeiro. Ele foi designado para mim quando éramos crianças."

    asterion "A maneira como você fala, as coisas que você diz.{w} Seu desprezo pela hierarquia."

    asterion "A maneira como você olha para mim... Eu me peguei pensando como se você fosse ele."

    you "Se Froneu fosse um Mestre, ele seria como os outros? Ele teria te machucado?"

    $Asterion.change("emotion", "annoyed")

    asterion "Não. Não há nada nesse mundo que eu tenha mais certeza do que isso."

    you "Por que você tem tanta certeza de que ele não faria isso?"

    asterion "Ele não era esse tipo de homem. Jamais passaria por sua mente."

    pause 2.0

    $Asterion.change("emotion", "surprise")

    pause 1.0

    $Asterion.change("emotion", "sad")

    "Astério bate as juntas dos dedos na mesa de madeira. Ele lambe os lábios e, desta vez,
    sua língua deixa um brilho de saliva."

    "Os olhos dele alternam entre olhar para você e piscar deliberadamente."

    $Asterion.change("emotion", "mooing")

    "Ele respira fundo e coloca as duas mãos sobre a mesa. Ele expira e
    seus braços avançam um pouco mais."

    $Asterion.change("emotion", "tired")

    "É uma distância tão pequena, não mais que o comprimento de um braço. Na verdade, é quase apertado,
    como se você tivesse que se limitar a um canto da sala."

    menu:
        "Segurar as mãos e confortá-lo.":

            "Você levanta a mão alguns centímetros da mesa — parece leve, nem um pouco estranho.
            O minotauro a lança um breve olhar, uma piscada deliberada, uma longa expiração."

            show Asterion:
                ease 1.0 yalign 1.15 zoom 1.05

            "Você a coloca sobre a dele. As veias saltam nas costas das mãos — você poderia traçá-las
            com seus dedos seguindo a direção do pelo curto."

            "Está fria e suada, mas não muito. Seu calor não deve ser indesejado — na
            verdade, o minotauro fecha os olhos, inspira, expira e solta os ombros."

            $Asterion.change("emotion", "neutral")

            "O toque dura apenas por um curto momento, o tempo cobra seu preço. Você solta antes
            de ultrapassar o limite das boas-vindas."

            pause 2.0

            $global_affection += 1

        "Insistir no argumento.":
            you "Lamento se essa conversa não serviu para acalmar você. Mas às vezes a vida
            {i}é{/i} anticlimática."

            you "Podemos esperar grandes histórias como nas lendas. Esse é o mito que as pessoas
            contam sobre você, certo?"

            you "Eles pintaram você como o vilão, Teseu como o herói, e foi isso que
            passou adiante. Mas a verdade é pequena e tranquila."

            you "Já se passaram milhares de anos, mas hoje é a mesma coisa. Você esperava
            que eu me virasse e mostrasse minha verdadeira natureza sendo que estive mostrando
            a você esse tempo todo."

            you "Eu sou só um cara. Nem um herói, nem um vilão, e tudo o que estou fazendo é a coisa certa."

            you "E o mesmo vale para você. Por que você não matou Teseu? É porque esse não é
            você."

            $Asterion.change("emotion", "relieved")

            you "Humanos são assim."

            "Você abre um sorriso."

            pause 2.0

            $Asterion.change("emotion", "contemplative")

            asterion "Você e sua lábia."

            "Ele fecha os olhos e se afunda na cadeira. Suas mãos trêmulas cobrem a mancha
            de suor em seu estômago."

            $Asterion.change("emotion", "neutral")

            asterion "Me permite um tempo para pensar?"

            you "Você nem precisa perguntar esse tipo de coisa, a resposta é sempre sim."

            asterion "Eu sei."

            "Ele esfrega as mãos, como se estivesse tentando se aquecer."

            asterion "Eu sei disso."

            $global_affection += 0.5

        "Dá-lo espaço.":
            hide Asterion
            hide quarterstable
            with Dissolve(1)

            "Você se levanta e volta para a cozinha. Ainda há um punhado de pequenas tarefas a se fazer —
            lavar pratos, limpar a bancada, guardar os ingredientes."

    hide Asterion
    hide quartertable
    with Dissolve(1)

    "Não muito tempo depois, o minotauro se retira para seu quarto."

    "Você se abstém de interromper a paz dele pelo maior tempo possível, mas horas depois você se lembra
    da oferta de Luke para observar as estrelas."

    "Talvez fosse melhor permitir a Astério algum tempo sozinho. Ele não precisa
    sair se não quiser."

    "Enquanto você está se arrumando, no entanto, ele sai do quarto."

    $Asterion.change("emotion", "neutral")
    show Asterion:
        xalign 0.5 yalign 1.0
    with Dissolve(1.0)

    asterion "Você está saindo?"

    you "Sim, Luke nos convidou para observar as estrelas hoje, lembra? Você não precisa vir
    se não quiser."

    asterion "Ah, sim. Eu estava querendo perguntar algo sobre isto."

    $Asterion.change("emotion", "tired")

    asterion "Será que você, ou talvez Luke, se importariam se eu trouxesse minha lira junto?"

    you "Tenho certeza que todos nós vamos apreciar as suas músicas."

    $Asterion.change("emotion", "contemplative")

    you "Uma noite com amigos."

    pause 1.0

    asterion "Sim. Precisarei apenas de um minuto para ficar pronto."

    you "Eu te espero."

    scene bg black
    with Dissolve(2)

    play music "music/Obviously.ogg" fadeout 2.0 fadein 2.0

    scene stargaze

    $Asterion.change("emotion", "contemplative")
    $Luke.change("emotion", "happy")
    $Luke.change("arm", "pointing")
    $Kota.change("emotion", "neutral")
    $Kota.change("rightarm", "relaxed")
    $Kota.change("leftarm", "relaxed")
    show Cobalts:
        zoom 1.0 yalign 1.1 xalign 0.3
    show Luke behind Cobalts:
        zoom 0.6 xalign 0.1 xzoom -1 yalign 1.0
    show Asterion behind Cobalts:
        xzoom 1 zoom 0.65 yalign 1.0 xalign 0.6
    show Kota behind Cobalts:
        xzoom -1 zoom 0.8 yalign 1.0 xalign 1.1
    show quartertable:
        yalign 1.0 xpos -950

    with Dissolve (2)

    show Cobalts:
        ease 2.0 xalign 1.1
        ease 0.2 yalign 1.0
        ease 0.2 yalign 1.1
        ease 2.0 xalign 0.3
        ease 0.2 yalign 1.0
        ease 0.2 yalign 1.1
        repeat

    "Antes do pôr do sol, o grifo levou algumas cadeiras para o estacionamento."

    "As estrelas acima brilham como um veio de minério."

    "Luke é banhado pela luz vermelha de uma série de lâmpadas movidas a bateria que trouxe consigo.
    Ele derrama sobre os papéis espalhados na mesa suas anotações e um livro maltratado tão grande quanto seu braço."

    "É um atlas do céu estrelado. O vento ameaça soprá-lo, mas o grifo usa
    uma lâmpada como peso."

    "Você o viu tirando todas essas coisas do porta-malas do carro."

    "O minotauro acaricia sua lira — uma sequência dedilhada, uma palheta roçando nas cordas e, em seguida,
    mudando notas enquanto ele afina tudo."

    "Você e Kota olham um para o outro, depois para o lado."

    show Cobalts:
        ease 0.5 xalign 0.65 yalign 1.0
    pause 0.5
    show Cobalts:
        ease 1.0 xalign 0.2 zoom 0.6 yalign 1.0
        pause 3
        ease 2.0 xalign 1.1 zoom 0.75
        pause 3
        ease 1.0 xalign 0.65 zoom 1.0 yalign 1.1
        pause 1.5
        ease 0.2 yalign 1.0
        ease 0.2 yalign 1.1
        pause 3
        repeat

    "Três pequenos lagartos correm ao seu redor. Eles se aproximam para olhar mais de perto, os olhos
    brilhando no escuro."

    "Suas pequenas garras clicam contra qualquer bugiganga que pegam para examinar.
    Chaveiros, canetas, latas de cerveja vazias sendo passadas ao redor por meio minuto
    antes de serem colocadas de volta onde estavam."

    "Após o menor dos movimentos, eles correm um ou dois metros para o deserto e se escondem
    atrás de uma rocha. Eles gorjeiam como pássaros, depois ficam em silêncio até que o topo
    de suas cabeças espreite da rocha."

    "Você dá a eles alguns petiscos — alguns pedaços de frango grelhado, um sanduíche de atum, algumas maçãs.{w}
    Seus dedos estão sujos e são tão finos."

    you "Você poderia me esclarecer sobre o que exatamente eles são?"

    $Kota.change("rightarm", "raised")
    kota "A resposta é simples, {w=1} eles —{nw}"

    #he gets interrupted by Luke

    $Kota.change("rightarm", "relaxed")
    $Kota.change("emotion", "sad")
    $Luke.change("emotion", "cocky")
    show Asterion:
        xzoom -1
    luke "Esse céu é como nada eu já tenha visto, Astério."

    $Luke.change("emotion", "happy")
    pause 1
    show Asterion:
        xzoom 1
    "O minotauro ergue os olhos para o grifo, pisca, e volta sua atenção para a lira."

    $Kota.change("emotion", "angry")
    $Kota.change("rightarm", "raised")
    kota "Como eu estava dizendo, isso é fácil de responder."

    kota "Anos atrás, ouvi falar de uma raça brincalhona de seres diminutos semelhantes a répteis,
    dito viverem e trabalharem no subsolo."

    $Kota.change("emotion", "neutral")
    kota "Os vi várias vezes em minhas viagens, principalmente no Velho Mundo e cerca de um século
    ou mais atrás. Esses meninos ficaram terrivelmente escassos nas últimas décadas."

    show Cobalts:
        ease 2.0 xalign -1.0 zoom 1 yalign 1.0

    kota "Se não me falha a memória, eles são chamados de \"cobaltos\"."

    you "Cobaltos? Que nem o metal?"

    $Kota.change("leftarm", "raised")
    $Kota.change("emotion", "happy")
    kota "Isso mesmo! Suponho que deva estar relacionado a eles serem criaturas subterrâneas."

    $Kota.change("emotion", "neutral")
    $Kota.change("leftarm", "relaxed")
    $Kota.change("rightarm", "relaxed")

    show cobalt_left behind Luke, Kota, Asterion:
        xalign -0.6 zoom 0.6 yalign 1.0 xzoom -1
        ease 2.0 xalign 0.3
    show cobalt_middle behind Luke, Kota, Asterion:
        xalign -0.6 zoom 0.6 yalign 1.0 xzoom -1
        ease 2.0 xalign 0.4
    show cobalt_right behind Luke, Kota, Asterion:
        xalign -0.6 zoom 0.6 yalign 1.0 xzoom -1
        ease 2.0 xalign 0.5

    pause 2.0
    "A um metro de vocês quatro, os cobaltos brigam de luta no chão."

    show cobalt_left:
        ease 1.0 xalign 0.3
        pause 1
        ease 1.0 xalign 0.4
        ease 1.0 xalign 0.5
        repeat
    show cobalt_middle:
        ease 1.0 xalign 0.4
        pause 1
        ease 1.0 xalign 0.5
        ease 1.0 xalign 0.3
        repeat
    show cobalt_right:
        ease 1.0 xalign 0.5
        pause 1
        ease 1.0 xalign 0.3
        ease 1.0 xalign 0.4
        repeat


    "O lagarto gordinho rasteja de quatro e avança em direção ao cobalto mais escuro,
    que se esquiva e o imobiliza. O perdedor geme — não muito diferente de um \"muu\" estridente."

    "O gordinho se joga no chão, como gado abatido, e se finge de morto."

    "Sobre seu cadáver, os dois outros lagartos, o escuro e o claro, lutam.
    Quando um deles tropeça no menino gordinho, ele rapidamente se afasta e
    fica à margem se remexendo e se abraçando."

    "O mais escuro vence, mas uma revanche começa. Uma nuvem de poeira sobe, grunhidos e
    guinchos a perfuram. O menino gordinho geme algo, mas nenhum dos dois o escuta."

    you "E tem certeza de que é seguro manter eles por perto? E se eles forem raivosos?"

    $Kota.change("rightarm", "raised")
    kota "Se eu estiver correto em minha avaliação, sim, eu diria. Algumas pessoas veem
    esses pequeninos como pestes, mas eles são trabalhadores diligentes, presumindo que sejam bem tratados."

    kota "E devo lhe informar que eles são bastante resistentes a praticamente qualquer doença que você possa imaginar.
    Além disso, eles possuem sangue frio, não há como pegarem raiva. Eles são {i}muito{/i} difíceis de matar."

    you "Entendo. E, só para ter certeza, o que exatamente \"tratar eles bem\" significa?"

    $Kota.change("emotion", "happy")
    $Kota.change("leftarm", "raised")
    kota "Ah, eles não precisam de muito. Comida, água, um buraco para dormir. Rochas e metais brilhantes
    caso queira recompensá-los, quando mais brilhantes, melhor. Eles amam pirita."

    kota "Você pode contar com eles para trabalhar duro, embora ocasionalmente eles possam se distrair e brincar."

    $Kota.change("emotion", "neutral")
    $Kota.change("leftarm", "relaxed")
    $Kota.change("rightarm", "relaxed")
    kota "Dê uma olhada, tenho certeza que eles estão prestes a fazer algo."

    "A luta corpo-a-corpo dos cobaltos chega ao fim. Parece que o lagarto mais escuro
    ganhou de novo e de novo, mas desta vez o mais claro quebrou uma regra anciã puxando
    a cauda do outro."

    "Ele monta no perdedor e solta um grunhido de vitória, tornado gutural e áspero
    com a promessa de violência em si."

    show cobalt_left:
        ease 1.0 xalign 0.1
    show cobalt_middle:
        xzoom 1
        ease 1.0 xalign 0.2
    show cobalt_right:
        ease 1.0 xalign 0.5

    "Ele está cansado da humilhação — perdendo de novo e de novo e, como consequência,
    largado para passar pela desgraça de comer as maçãs mais verdes."

    "Pelos deuses, quantas vezes pode um homem comer a borda queimada de uma fatia de pão
    antes de perder sua fé na justiça?"

    show cobalt_middle:
        ease 1.0 xalign 0.5
    "Ele puxa uma arma — uma lata de cerveja amassada. É hora da violência."

    show cobalt_left:
        ease 1.0 xalign 0.4
    "O cobalto gordinho se atira para impedi-lo, bufando e gritando enquanto ranho escorre pelo nariz."

    "Mas seus destinos estão selados. Caim e Abel não podem evitar a tragédia na qual foram colocados por Deus."

    show cobalt_left:
        ease 1.0 yalign 1.2
    "No último segundo, o cobalto mais escuro pondera sobre a vida — como não há grande epifania antes
    que alguém encontre seu fim, nenhuma iluminação, tudo acaba tão abruptamente quanto
    as primeiras memórias começam."

    "O cobalto mais claro desce a lata sobre o crânio do outro. Provoca um baque surdo e,
    em seguida, quica a um ou dois metros de distância."

    "O perdedor solta uma lamúria dramática — cheia de maldições aos daemones e apelos
    aos deuses — enquanto o vencedor grita em glória enlouquecida."

    "O gordinho chora e lamenta. O vencedor leva os itens conquistados — a maçã mais madura,
    o pedaço de frango mais grosso e o meio do sanduiche transbordando de atum."

    "Que mundo doentio e distorcido é este. O menino gordinho pode apenas chorar, gemendo
    seu característico \"muu\" estridente e invocando as Erínias para trazer retribuição."

    "O vencedor solta um guincho final de glória."

    "O segura e deixa ressoar pelo vale até que desapareça por completo."

    "Fim."

    show cobalt_left:
        ease 1.0 xalign 0.25 yalign 1.0
    show cobalt_middle:
        ease 1.0 xalign 0.35
    show cobalt_right:
        ease 1.0 xalign 0.45

    "Os três meninos se levantam, se dão as mãos e comemoram."

    "Que performance maravilhosa! A trupe se curva enquanto o público invisível os aplaude de pé."

    $Kota.change("emotion", "laughing")
    kota "Eles são muito brincalhões, como você pode ver. Não concorda, Luke?"

    $Luke.change("emotion", "neutral")
    luke "O que?"

    $Kota.change("emotion", "happy")
    kota "Os cobaltos, não são a coisa mais engraçada que você já viu?"

    $Luke.change("emotion", "annoyed")
    luke "Sim, claro. Os patifes engraçadinhos comeram o meu almoço, mas beleza."

    $Kota.change("emotion", "puzzled")
    kota "Você não pode culpá-los, eles estão tão magros! Quem sabe quando foi a última vez que eles tiveram uma refeição de verdade."

    luke "Ah-ham."

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "hip")
    show Luke:
        ease 2.0 xalign 0.0 zoom 0.85

    $Kota.change("emotion", "neutral")
    "O grifo volta a examinar seus papéis avermelhados. Você se levanta para verificar como ele está."

    "Há um atlas celestial sobre a mesa — suas páginas estão minuciosamente rabiscadas com
    marcas de lápis bem fracas, nas margens há listas de nomes e datas."

    you "Então, Luke, como vai? A estrelas estão boas esta noite?"

    $Luke.change("emotion", "happy")
    luke "Com certeza, o céu noturno aqui é simplesmente incrível. Olhe com seus próprios olhos,
    você já viu estrelas tão nítidas assim, [player_name]?"

    you "Não posso dizer que sim. Acho que nem o lugar mais isolado que já visitei era assim."

    luke "Sim, sim. Nem um tiquinho de poluição luminosa. Se a gente tivesse perto de uma cidade — com prédios
    e casas, postes de luz, o que você pensar — seria difícil ver as estrelas com todo aquele lixo."

    luke "Mas nem um tiquinho disso aqui... E eu não reconheço essas estrelas de jeito nenhum. Nem umazinha..."

    $Luke.change("emotion", "neutral")
    luke "A não ser, {i}talvez...{/i} Uma cadeia de estrelas que me lembra Hydra,
    mas pode ser só uma parecida."

    show cobalt_left:
        ease 4.0 xalign -0.7
    show cobalt_middle:
        ease 4.0 xalign -0.6
    show cobalt_right:
        ease 4.0 xalign -0.5

    $Kota.change("rightarm", "raised")
    kota "Eu posso ter uma resposta para isso, Luke. Já passou pela sua cabeça que podemos não estar
    no hemisfério norte? Talvez você esteja familiarizado apenas com aquela parte!"

    $Luke.change("emotion", "annoyed")
    $Kota.change("rightarm", "relaxed")
    luke "Passou sim, mas não é isso. Além do mais, fique você sabendo que eu conheço
    o hemisfério celestial sul!"

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "salute")
    luke "Se tem uma coisa que esse cérebro de passarinho aqui conhece, são as estrelas."

    $Luke.change("arm", "hip")
    luke "Como você pode esperar, não tem sinal de celular ou GPS aqui também.
    Então não tem como saber com certeza onde a gente tá na Terra..."

    luke "Mas nenhum lugar na Terra teria um céu assim. Então minha... é... minha {i}hipótese{/i}
    é que a gente nem tá na Terra sequer."

    pause 1.0

    $Kota.change("emotion", "laughing")
    kota "Hah! Esta é sua primeira vez encarando algo profundamente sobrenatural, Luke?
    Pensei que estaria mais familiarizado com tais circunstâncias!"

    $Luke.change("emotion", "annoyed")
    $Luke.change("arm", "pointing")
    luke "Me desculpa se eu não venho do místico Extremo Oriente, senhor deus dragão!
    Lá em casa a gente não tem nenhuma merda dessas."

    $Luke.change("arm", "hip")
    luke "Então porque você não esclarece a gente sobre o que tá acontecendo?"

    $Kota.change("emotion", "happy")
    kota "A-ah. Bem... Você está enxergando isto da maneira errada, entende?
    A magia não deve ser averiguada com a ciência humana, Luke. Ela apenas é o que é."

    $Luke.change("emotion", "laughing")
    luke "Foi mal, chefão, mas isso não vai rolar pra mim. Eu tô apaixonado por esse céu e quero fazer dele todo meu."

    $Luke.change("emotion", "happy")
    "Ele olha para cima. Com uma coroa de estrelas sobre a cabeça, poderia-se esquecer a
    natureza lasciva e as piadas grosseiras do homem. Durante esta noite, ele carrega bem a
    magnificência da águia careca americana."
    luke "Pode imaginar se todo esse lugar estiver em outro planeta?
    O que isso pode significar pra humanidade..."

    luke "Talvez eu possa... Seria um pé no saco, mas talvez eu possa encontrar uma estrela
    em comum com o céu da Terra... Mas eu nem sei por onde começar com isso
    se eu estiver errado sobre Hydra."

    pause 1.5

    $Luke.change("emotion", "neutral")
    luke "...Talvez se eu..."

    pause 1.0
    show Luke:
        xzoom 1
        ease 2.0 xalign -0.2
    #luke is lost in thought again. he goes to a table nearby where there's a red
    #lamp and start scribbling around
    #asterion becomes a bit interested
    pause 1.0
    $Asterion.change("emotion", "neutral")
    show Asterion:
        xzoom -1
        ease 1.0 xalign 0.5 zoom 0.7

    you "O que você está fazendo, Luke?"

    $Luke.change("arm", "salute")
    luke "Mapeando esse céu, chefe. Não posso desperdiçar essa oportunidade."

    $Luke.change("arm", "hip")
    if first_guest == 'Kota':
        luke "Eu tava conversando com o Astério umas noites atrás e ele me disse que ninguém mapeou o céu,
        ou pelo menos ele acha que ninguém fez isso. Então eu tô fazendo."

    else:
        luke "Eu puxei nosso menino Astério de lado ontem e ele me disse que não tem registros
        de ninguém que tenha mapeado esse céu, então eu tô fazendo isso."

    $Luke.change("emotion", "cocky")
    luke "Se importa se eu inventar constelações e dar nome a elas?"

    pause 1.0

    you "Se estiver tudo bem para o Astério, então tudo bem para mim."

    $Asterion.change("emotion", "smiling")
    show Asterion:
        ease 0.6 yalign 1.1
        ease 1.0 yalign 1.0
    pause 1.6
    $Asterion.change("emotion", "contemplative")

    pause 1.0
    #luke has something sharp in his eyes

    $Luke.change("emotion", "neutral")
    luke "Entendo. Bem, nesse caso... Bem, só pra ter certeza, tudo bem se eu batizasse uma com
    o nome do meu irmão?"

    you "Não vejo por que não."

    $Luke.change("emotion", "happy")
    luke "Obrigado. Isso é um sonho que se tornou realidade, chefe."

    show Luke:
        xzoom -1
        ease 2.0 zoom 0.6 xalign 0.1
    $Kota.change("emotion", "puzzled")
    kota "Irmão, é?"

    luke "Isso mesmo. O nome dele era Pedro, a gente costumava observar as estrelas quando crianças e ele
    inventava as constelações mais estranhas que você poderia imaginar."

    $renpy.music.set_volume(0.1, delay=1, channel='music')

    $Kota.change("emotion", "neutral")
    $Asterion.change("emotion", "contemplative")
    show Asterion:
        xzoom 1
    pause 0.5
    #the screen focuses on Asterion while the background goes black
    show Luke behind Asterion
    show Kota behind Asterion
    show blackback behind Asterion:
        alpha 0.6
    with Dissolve(2)

    "Irmão."

    "A mão de Androgeu cobriu a do minotauro — uma luva áspera e calejada na ponta de seus dedos,
    coberta apenas por uma pequena camada de pelo."

    "Por duas semanas, ele ensinou seu irmão mais novo como puxar uma flecha de uma aljava,
    como encaixar seu entalhe na corda do arco, como puxá-la com as costas e não com os braços."

    "Adquirir a força para puxar a corda foi fácil para o bezerro.
    \"Astério de Costas Largas como as Estepes\", era como Androgeu o chamava. \"O Filho do Arqueiro.\""

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "pointing")
    "A destreza para encaixar as flechas e mirar o iludiram, no entanto, e se passaram anos antes
    que o jovem híbrido pudesse efetivamente disparar uma sequência de flechas."

    "Mas um dia os ensinamentos de Androgeu entraram em colapso interno. Talvez algo tenha
    mudado nos olhos do minotauro, ou uma benção criou raízes em suas mãos."

    "Tudo o que ele aprendeu se transformou em carne e, a partir de então, seu progresso não foi nada além de prodigioso."

    "Daquele dia em diante, uma vez a cada duas semanas ou mais, seu pai se levantava cedo
    para assistir suas práticas."

    "Tinha sua atenção total com a queda de alvo após alvo. Até que tudo acabou."

    "Androgeu. Quão curto foi nosso tempo juntos e, ainda assim, poucos deixaram uma impressão tão duradoura em mim."

    $Asterion.change("emotion", "sad")

    "Se ao menos eu tivesse permanecido em Hades..."

    hide blackback
    with Dissolve(2)

    $renpy.music.set_volume(1.0, delay=1, channel='music')

    show Luke:
        xzoom -1

    $Luke.change("emotion", "happy")
    $Luke.change("arm", "hip")
    luke "Pedro era um filho da puta tão atrevido... Eu até errei uma questão numa
    prova uma vez, sabe? Acontece que não existe uma constelação de \"Argos\",
    por mais que exista uma \"Argo Navis\"."

    $Luke.change("emotion", "laughing")
    luke "E o desgraçado acertou essa também! Quando eu cheguei, ele tava rindo
    pra caramba de mim, ele sabia só de olhar pra minha cara que eu tinha errado."

    $Luke.change("emotion", "neutral")
    luke "Em minha defesa, essa é do hemisfério sul, então não é como se, naquela época,
    eu tivesse a chance de ver por conta própria."

    $Kota.change("rightarm", "raised")
    kota "Entendo. Então vocês tinham uma boa relação."

    $Kota.change("rightarm", "relaxed")
    $Luke.change("emotion", "cocky")
    luke "Isso aí!"

    $Luke.change("arm", "pointing")
    luke "E você, Azulzinho? Tem algum irmão em casa, seja lá onde isso for?"

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "hip")
    $Kota.change("emotion", "happy")
    kota "Sim, em uma época. Um irmão, de escamas vermelhas e mais apto nas artes marciais
    do que eu. {w=0.2} Eu, por outro lado, descobri minha aptidão no sacerdócio e na erudição."

    kota "Ainda assim, nos dávamos bem um com o outro. Como duas metades de um todo,
    como diriam os sacerdotes do santuário."

    $Kota.change("emotion", "neutral")
    kota "E, de fato, tínhamos nossas divergências e discussões, mas elas nunca importaram
    muito no final.{w} Onsen e eu, nós..."

    $Kota.change("emotion", "sad")
    "O dragão se perde na reminiscência por um momento. Em seguida, o sorriso desaparece de seu rosto."

    kota "É claro, as circunstâncias nos fizeram seguir caminhos diferentes no final."

    $Luke.change("emotion", "sad")
    luke "Ah."

    $Luke.change("emotion", "neutral")
    luke "Hã… você sabe onde ele tá? Como ele vai?"

    pause 1.0
    kota "Quem sabe."

    $renpy.music.set_volume(0.1, delay=1, channel='music')

    show blackback behind Asterion:
        alpha 0.6
    with Dissolve(2)
    #screen goes back to Asterion, background goes black
    "Androgeu. Nunca perguntei se você gostou das penas. Aquela noite foi muito parecida com esta.
    Eu apontei meu arco para uma estrela, como se de alguma forma minha flecha pudesse alcançá-la, e soltei."

    "Três vezes disparei uma flecha, e então ela caiu."

    "Froneu e eu preparamos o fogo. Nosso sacrifício para você, penas de um pássaro sagrado."

    "Quanto a Froneu... Não compartilhávamos o mesmo sangue, mas éramos irmãos da mesma forma."

    "Naquela noite, festejamos e afogamos as brasas com vinho, e você me disse para..."

    "Froneu" "Abandone o labirinto. Podemos adorar aos deuses da mesma forma, prestar o
    devido respeito em nossa própria lareira e construir um santuário ao redor dela."

    $Kota.change("emotion", "puzzled")
    kota "Asterion?"

    "Froneu" "Você pode ter sua liberdade se construirmos nossa fé."

    kota "Asterion? Você está me ouvindo?"

    stop music fadeout 2.0

    hide blackback
    with Dissolve(1)

    $Asterion.change("emotion", "tired")
    $Kota.change("emotion", "sad")
    "O minotauro olha para o dragão, lábios selados enquanto as palavras cortam seus pensamentos."

    "Ele toma um gole de sua garrafa de vinho."

    $Asterion.change("emotion", "neutral")
    asterion "Perdoe-me. O que você disse?"

    $Kota.change("rightarm", "raised")
    kota "Eu estava perguntando, você tem irmãos?"

    $Kota.change("rightarm", "relaxed")
    asterion "Sim. Irmãos e irmãs."

    kota "Se importa se eu perguntar onde eles estão agora?"

    $Asterion.change("emotion", "tired")
    asterion "Eles não estão mais por perto. Já faz um bom tempo desde a última vez que conversamos."

    $Kota.change("rightarm", "raised")
    kota "Entendo. Isto é bastante peculiar para mim. Eu viajei muito, vi o mundo, e ainda assim...
    Nunca tinha visto um minotauro com meus próprios olhos."

    kota "Na verdade, de todos os mitos e lendas, é amplamente aceito que os minotauros não existiram,
    ou pelo menos não existem mais."

    $Kota.change("rightarm", "relaxed")

    pause 2.0

    #kota stops
    #asterion keeps quiet
    #luke is seemingly focused on mapping the stars
    #the player is tense
    #maybe we can show this with the visuals


    kota "Você... Você se importaria em me dizer os nomes dos seus irmãos?"

    $renpy.music.set_volume(1.0, delay=1, channel='music')

    pause 1.0

    $Asterion.change("emotion", "neutral")

    show Asterion:
        ease 3.0 xalign 0.47
    pause 4.0

    play music "music/Calliopeia.ogg" fadeout 2.0 fadein 2.0

    "O minotauro levanta os olhos da lira."

    "O grifo e o dragão já tinham visto muitos dos mistérios do labirinto até então.
    Mas ele não contou para eles — e nem o Mestre, ele presumiu — sobre sua verdadeira natureza."

    "Será que o dragão descobriu de alguma forma?"

    asterion "Froneu era meu irmão."

    $Kota.change("rightarm", "raised")
    kota "Mesmo?"

    pause 1.0

    $Kota.change("rightarm", "relaxed")
    kota "Um nome bem grego, assim como o seu. É uma tradição familiar?"

    pause 1.0

    asterion "É nossa cultura."

    $Kota.change("emotion", "puzzled")
    kota "Cultura grega. {w=0.5}Ou talvez,{w=0.5} seja mais próxima de Cre—{nw}"


    $Luke.change("arm", "hip")
    show Luke:
        linear 0.5 zoom 0.7 xalign 0.0

    $Luke.change("emotion", "laughing")
    show Asterion behind Luke:
        xzoom -1
        ease 2.0 xalign 0.55
    show Luke:
        linear 0.5 zoom 0.8 xalign 0.0

    #luke interjects, he's smiling to defuse the situation
    luke "Sabe... Foi meu irmão quem me chamou de Luke pela primeira vez."

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "pointing")
    luke "Os seus já te deram algum apelido, Astério?"

    pause 0.5

    $Asterion.change("emotion", "contemplative")
    asterion "Sim. Ele costumava me chamar de \"Estrelinha\"."

    $Luke.change("emotion", "laughing")
    luke "Estrelinha, hein? Esse é o nome de um hino que a minha mãe costumava cantar pra mim!"

    $Luke.change("arm", "hip")
    luke "Quer ouvir?"

    $Asterion.change("emotion", "neutral")
    asterion "Se você gostaria de compartilhar, sim."

    $Kota.change("emotion", "angry")
    luke "Quão sábia você parece, estrelinha, lá longe\nLá encima no céu;"
    luke "Por quantos anos você brilhou aí\nAcima do mundo, tão alto?"
    $Luke.change("emotion", "happy")
    luke "Estrelinha, lá encima no céu,\nDiga-me, você estava brilhando antes?"
    luke "Você ouviu os anjos cantando,\n\“Paz! Boa vontade aos homens\”?"

    $Luke.change("arm", "salute")
    luke "Muitas vezes me pergunto se você estava lá\nQuando Cristo estava no celeiro,"
    luke "E se você viu, de sua altura estonteante,\nO infante Senhor de todos."

    $Kota.change("emotion", "puzzled")
    $Luke.change("arm", "pointing")
    luke "Se você ouviu naquela noite,\nPoderia ter escutado a música"
    luke "Que flutuou no ar da meia noite\nDaquela multidão angelical?"
    luke "Ah, sim, você é uma estrelinha sábia,\nMesmo sem nenhuma palavra para dizer;"
    $Luke.change("emotion", "laughing")
    $Luke.change("arm", "salute")
    luke "Você observa a terra sonolenta a noite toda,\nE dorme durante o dia inteiro."

    pause 2.0

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "pointing")
    luke "Bonito, hein?"

    pause 1.0

    asterion "Sim. É legal."

    pause 2.0

    show Kota:
        ease 1.0 xalign 1.0

    show Asterion:
        xzoom 1
        ease 2.0 xalign 0.45

    $Kota.change("emotion", "angry")
    $Kota.change("leftarm", "raised")
    $Kota.change("rightarm", "raised")
    kota "Agora que este pequeno desvio foi resolvido..."

    $Luke.change("emotion", "sad")
    $Luke.change("arm", "hip")
    $Kota.change("leftarm", "relaxed")
    kota "[player_name], Astério. Hoje, Luke e eu descemos para o alicerce.
    Foi onde encontramos os cobaltos."

    $Kota.change("emotion", "puzzled")
    kota "Espero que não se importe, mas examinei alguns dos contratos e documentos armazenados lá."

    $Kota.change("emotion", "sad")
    $Kota.change("rightarm", "relaxed")
    kota "O que encontramos foi..."

    pause 2.0

    $Asterion.change("emotion", "annoyed")
    asterion "Sim. O que vocês encontraram foi?"

    pause 2.0

    show Kota:
        ease 1.0 xalign 1.1
    show Luke:
        ease 1.0 xalign -0.1
    show Asterion:
        ease 1.0 zoom 0.75 xalign 0.5

    asterion "Vá em frente. Diga."

    pause 2.0

    asterion "Agora vocês conhecem a verdade. Eu sou Astério. {i}O{/i} minotauro."

    $Kota.change("leftarm", "raised")
    $Kota.change("rightarm", "raised")
    show Kota:
        ease 1.0 xalign 1.2
    kota "Sim, mas... O que você fez para merecer isso?"

    $Kota.change("leftarm", "relaxed")
    $Kota.change("rightarm", "relaxed")
    $Asterion.change("emotion", "neutral")
    #asterion's expression is cold, emotionless
    pause 1.0

    asterion "Eu desagradei os deuses. Apenas isto já justifica punição."

    asterion "Você deveria saber disso muito bem, considerando sua idade e procedência."

    $Kota.change("emotion", "puzzled")

    kota "Não, isso não está nem arranhando a superfície. Tem que haver mais nessa história."

    $Asterion.change("emotion", "tired")
    kota "Há milhões de mortais que foram muito além de \"desagradar\"
    os deuses que eles adoram e não posso acreditar que algum recebeu uma punição tão severa como a sua."

    $Asterion.change("emotion", "sad")
    show Asterion:
        ease 3.0 zoom 0.7

    kota "Foi assassinato, canibalismo? Esta é a lenda, afinal, de que você —"

    you "Kota. Pare. Ele não quer falar sobre isso."

    $Kota.change("emotion", "sad")
    kota "Isto eu vejo, mas temos o direito de saber do que se trata e..."

    $Luke.change("arm", "pointing")
    show Luke:
        ease 1.0 xalign 0.0

    luke "Seja lá o que ele tenha feito, não importa o quão grande ou pequeno, já foi pago centenas de vezes."

    $Luke.change("arm", "hip")
    $Kota.change("emotion", "angry")

    kota "Suponho que você esteja correto nisso. Ainda assim, não responde o que exatamente está acontecendo aqui."

    kota "Por exemplo, você, [player_name], se entendi corretamente, seu papel em tudo
    isso é ser o {i}torturador{/i} dele."

    if TimesSent == 0:
        $Kota.change("emotion", "puzzled")
        kota "Houve momentos difíceis em nossas interações, mas em meu breve tempo aqui não
        vi razão para questionar sua moral."
    else:
        $Kota.change("emotion", "sad")
        kota "Não vi nada muito chocante em nossas interações, mas você
        realmente enviou Astério para aquele vale."
        kota "Nenhum ferimento grave saiu disso, mas..."

    $Kota.change("emotion", "angry")
    $Kota.change("rightarm", "raised")
    $Kota.change("leftarm", "raised")
    show Kota:
        ease 1.0 xalign 1.0
    kota "Mas, por favor, você precisa entender. Eu não posso, eu não vou trabalhar em um lugar assim... que tortura alguém!"

    kota "Não há magia, nem quantidade de ouro, nada que me convença a fazer isso.
    Então, por favor, eu preciso saber o que está acontecendo aqui."

    $Kota.change("rightarm", "relaxed")
    $Kota.change("leftarm", "relaxed")
    pause 1.0

    luke "[player_name]..."

    $Luke.change("emotion", "annoyed")
    $Luke.change("arm", "pointing")

    luke "Olha, eu não queria tocar no assunto essa noite. Ainda tô apavorado e tentando
    me controlar, e não tenho certeza se falar assim de cara como Kota fez é o que eu faria."

    luke "Mas, caramba, eu tô com ele aqui."

    luke "Eu já fiz um monte de coisa fodida na minha vida, não sou santo,
    mas isso tudo ficou pra trás. Eu tenho que saber o que é toda essa coisa de labirinto."

    luke "Então... Agora que a merda foi jogada no ventilador, se importa?"

    $Luke.change("arm", "hip")
    "Você reúne seus pensamentos — desde a noite em que recebeu a escritura até
    encontrar Astério na câmara fria e tudo o que veio depois."

    "Que história absurda, e já se passaram menos de duas semanas desde que você chegou aqui."

    "Conforme você junta os fatos, fica claro o quão absurda é — e
    que a mera ideia de ter poder absoluto sobre este domínio e Astério é
    questionável o suficiente..."

    if TimesSent == 0:
        "...mesmo que você não o tenha usado mal."
    else:
        "...ainda mais considerando que você enviou Astério para o vale."

    $Luke.change("emotion", "sad")
    $Kota.change("emotion", "sad")
    "Ainda assim, você conta a eles sua versão até encontrar Astério na câmara fria..."

    $Asterion.change("emotion", "tired")
    show Asterion:
        ease 1.0 zoom 0.8 xalign 0.5
    show Luke:
        ease 1.0 xalign -0.1
    show Kota:
        ease 1.0 xalign 1.1

    "...que é quando o minotauro entra e começa a corroborar a história,
    se não contando sua própria versão."

    if ArgosContract == "Terrorized":
        "Ele omite, entretanto, como você o enviou para fora a pedido de Argos."

    "Não leva mais de quinze minutos para atualizá-los."

    kota "Astério, [player_name], eu não sei o que dizer..."

    luke "Então é por isso que você tava diferente na noite passada..."

    pause 1.5

    luke "Mas por que você não contou pra gente?"

    pause 1.0

    $Asterion.change("emotion", "sad")
    asterion "Quanto menos pessoas souberem disso, mais posso simplesmente viver. Ignorar tudo e aproveitar o que tenho."

    asterion "É apenas porque vocês foram ao vale e viram o que ele possui que estou disposto
    a falar. De qualquer forma, esta era uma história a qual eu não tinha interesse em compartilhar."

    $Luke.change("arm", "pointing")
    show Luke behind Asterion:
        ease 1.0 xalign 0.1
    luke "Não tem como libertar você? Tem que ter..."

    kota "Se houvesse uma maneira, presumo que ele já teria descoberto."

    asterion "De fato. Ainda não encontrei uma pista sequer de como me libertar."

    $Luke.change("arm", "hip")
    pause 1.5
    show Luke:
        xzoom 1
        ease 2.0 xalign -0.2
    show Kota:
        xzoom 1
        ease 2.0 xalign 1.2


    "Luke vira de volta para seus mapas celestes, mas mantém o olhar nos próprios pés. Kota
    desvia o olhar para a estrada e passa uma mão pela barba."

    $Asterion.change("emotion", "mooing")

    "Astério puxa o ar, segura, e solta em um chiado áspero."

    $Asterion.change("emotion", "tired")

    "Até os cobaltos interromperam sua briga, agora eles se sentam perto
    de uma rocha não muito longe e observam Astério."

    pause 1

    "Nenhum deles direciona tanto quanto um olhar para você, mas a presença deles o afeta independentemente."

    "Você é o chefe, afinal. Se qualquer um tem legitimidade para falar e tomar as rédeas, esse alguém é você."

    "Os eventos desta tarde ainda estão frescos. É um bom começo."

    show Luke:
        xzoom -1
    show Kota:
        xzoom -1

    you "Independentemente de haver ou não um jeito, eu posso fazer minha parte. Estávamos conversando sobre isso mais cedo."

    you "Para todos os efeitos e propósitos, Astério é meu {i}parceiro.{/i} Nós trabalhamos
    juntos, tomamos decisões depois de consultar um ao outro, até vivemos sob o mesmo teto."

    you "Astério disse que não tinha como eu oficializar isso aqui. E, de fato,
    o labirinto pode ter seus contratos e leis, pode me impedir de assinar um documento sobre isso..."

    you "Mas não precisamos de papelada para fazer isso acontecer. A verdade fala por si só."

    you "Se todos nós reconhecermos o {i}fato{/i} de que Astério e eu somos
    iguais, se todos souberem disso..."

    you "Então essa é a verdade."

    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "neutral")
    #Change their expressions to show what the MC is saying is connecting.
    #That said Asterion is still a bit skeptical.
    pause 1.5

    you "E vocês podem me responsabilizar por isso, certo? Agora que vocês sabem a verdade
    sobre o vale, o que vão fazer se eu mandar Astério para fora outra vez?"

    $Kota.change("emotion", "sad")
    $Kota.change("rightarm", "raised")
    kota "Nós... Isso não está certo, nós impediríamos você."

    $Kota.change("rightarm", "relaxed")
    you "Exatamente. Mesmo que não me restrinjam completamente, vocês poderiam me desobedecer,
    digamos, fazendo uma greve."

    you "Nenhum de vocês precisa confiar em mim para fazer a coisa certa a partir da bondade
    do meu coração. Vocês {i}podem{/i} me impedir ou me pressionar."

    $Kota.change("emotion", "neutral")
    you "E se continuarmos assim por tempo suficiente, durante as décadas que serei o gerente do
    hotel, então... Quando o próximo chegar, ele também não terá escolha, não é?"

    you "Todos vão esperar que Astério seja tratado como um parceiro, isso é tudo o que
    eles terão conhecido. Todas essas restrições passarão para ele, as pessoas vão exigir isso."

    you "Não podemos saber exatamente o que o futuro nos reserva, mas isso pode ser o suficiente para manter
    você seguro, Astério. Pode até ser um impedimento para outras pessoas como Clément no futuro."

    pause 1.5

    $Kota.change("emotion", "sad")
    $Luke.change("emotion", "sad")
    #Everyone's thinking, Asterion is still apprehensive
    #Let the tension linger.

    pause 2.0

    kota "Não tenho certeza de que isso resolverá todas as formas de problemas futuros, mas, independentemente disto,
    parece uma boa ideia."

    luke "Sim, realmente parece bom, mas se alguém {i}quisesse{/i} fazer alguma coisa
    fodida, isso não iria realmente impedir."

    $Luke.change("emotion", "annoyed")
    $Luke.change("arm", "pointing")
    luke "Quer dizer, até você... Se você quisesse fazer alguma coisa ruim ainda poderia atrás de portas fechadas."

    $Luke.change("arm", "hip")
    luke "Caramba, se eu e Kota não estivermos prestando atenção, você ainda pode mandar o
    Astério pro vale assustador."

    $Luke.change("emotion", "sad")
    $Kota.change("rightarm", "raised")
    kota "Astério, há uma maneira de usarmos um pouco da magia do hotel para lidar com isso?"

    $Kota.change("rightarm", "relaxed")
    $Asterion.change("emotion", "sad")
    pause 2.0
    #Asterion is a bit overwhelmed, thinking.
    #Player also thinks, and thinks about the contracts, the Argos stuff.

    "Poderia haver algo que você pudesse usar?"


    if player_background != "speedrunner" and (ArgosContract in ['Signed', 'Contested']):

        pause 2.0

        show blackback:
            alpha 0.8

        $Argos.change("pose", "crossed")
        $Argos.change("emotion", "smug")

        show Argos:
            xalign 0.5 yalign 1.0 xzoom 1 zoom 1
        with Dissolve(2)

        argos "O contrato também possui uma cláusula de não agressão. Eu não machucarei
        você, você não me machucará. É um acordo auto-impositivo -- nós dois
        não conseguiremos quebrá-lo. As leis aqui, veja bem, são
        auto-impositivas. Contratos são muito poderosos."

        argos "Na eventualidade de um de nós quebrar um dos termos de alguma forma,
        nosso pacto é encerrado. Eu perco os poderes que me foram legados, e a lareira
        de seu Hotel se apagará. O objeto volta para minha posse."

        $Argos.change("emotion", "cocky")

        argos "É um acordo muito justo, eu diria."

        pause 1.0

        hide Argos
        hide blackback
        with Dissolve(2)

        pause 2.0

        #Flashback to Argos' contract where it says that the mirror will revert to Argos if the MC harms him

        you "Eu tenho uma ideia, mas não tenho certeza se pode funcionar."

        $Asterion.change("emotion", "tired")

        you "Astério, me lembro que você disse algo sobre eu não poder me proibir de mandar você para fora.
        Mas eu estava pensando..."

        you "O contrato proposto por Argos, se bem me lembro, dizia algo sobre o Espelho de Héstia
        revertendo para sua posse caso certas condições fossem atendidas, como eu o machucando."

        you "Se eu machucar ele, então algo que não gosto acontece. Não poderíamos aplicar o mesmo princípio aqui?"

    else:

        you "Eu tenho uma ideia, mas não tenho certeza se pode funcionar."

        $Asterion.change("emotion", "tired")

        you "Astério, me lembro que você disse algo sobre eu não poder me proibir de mandar você para fora.
        Mas eu estava pensando..."

        you "Poderíamos definir algo que faria uma coisa que eu prefira evitar se mandar você para fora?"

    pause 1
    $Asterion.change("emotion", "sad")
    pause 1

    show blackback behind Asterion:
        alpha 0.7
    with Dissolve(3)

    "Um pedido simples, na verdade; se uma condição for realizada, então uma consequência desagradável é acionada."

    "Muitos contratos foram elaborados ao longo dos milênios, tantos que agora existem
    dezenas no Alicerce."

    "Ainda assim, poucos ou nenhum para restringir o Mestre todo-poderoso."

    "Há um contrato que ele poderia usar, um que o minotauro está bem familiarizado."

    "No entanto, seu pescoço arrepia. Ele cerra os dentes e morde a língua. Que arrogância sequer
    considerar colocar um Mestre através de tal infâmia."

    "Ou um amigo, por assim dizer."

    "Não há como alguém aceitar isso. [player_name] recusará — mas então, pelo menos,
    o minotauro poderá respirar sem dúvidas."

    "A farsa acabará."

    hide blackback
    with Dissolve(3)

    $Asterion.change("emotion", "tired")
    pause 1

    asterion "Há algo que podemos fazer, mas temo que você não vai gostar, {i}meu Senhor.{/i}"

    asterion "Estou ciente de um contrato antigo que pode criar um par de artefatos vinculados.
    Foi usado algumas vezes por senhores do passado."

    you "O que ele faz?"

    pause 1.0

    $Asterion.change("emotion", "neutral")

    asterion "Tem certeza que é isso o que você quer? Você realmente iria tão longe a ponto
    de se restringir para conseguir isso?"

    pause 2
    #ominous tension rises

    asterion "O contrato cria duas braçadeiras — uma no formato de uma coroa de louros,
    a outra em um simples anel de chumbo."

    asterion "Nós estabelecemos cláusulas — as condições que desejamos impedir de se
    concretizarem — digamos, pretendemos impedir que você me envie para o vale."

    asterion "Então você colocaria o anel de chumbo, eu pegaria a coroa de louros
    e nós assinaríamos o contrato com duas testemunhas oculares."

    you "Então isso me impediria de te mandar para o vale?"

    pause 1.5

    $Asterion.change("emotion", "tired")
    asterion "Estritamente falando, não. O que isso faria seria infligir uma punição a você caso um dia se tornasse realidade."

    pause 1.5

    you "Qual é a punição?"

    pause 2.0

    $Luke.change("emotion", "surprise")
    $Kota.change("emotion", "surprise")
    asterion "Amputaria seu braço."

    pause 1.0

    you "É uma baita punição."

    $Luke.change("emotion", "sad")
    $Kota.change("emotion", "sad")
    $Asterion.change("emotion", "mooing")
    asterion "Sim. O anel de chumbo também não pode ser removido, a menos que o contrato seja
    revogado com o consentimento de ambas as partes e testemunhas oculares."

    $Asterion.change("emotion", "tired")

    asterion "Mas se você quiser me provar que não tem má índole, então esta é sua chance."

    asterion "Eu posso arranjar o contrato agora, esta noite. Já sei os termos que gostaria."

    pause 1.0

    you "Ok. O que você tem em mente?"

    asterion "Que não serei forçado ou coagido a ir para o vale. É tudo o que quero."

    asterion "Se você está dizendo a verdade, se não quer me machucar e deseja realizar
    a missão do hotel, então esta condição não deve ser controversa."

    asterion "Não tenho assuntos a resolver no vale. Por séculos antes de Clément, nunca
    tive uma razão para ir lá, e nenhum mestre viu motivo para isto também."

    asterion "Esta cláusula não especifica quem me força ou me coage a ir para o vale,
    veja bem. Se este termo for assinado, será de seu interesse me proteger de qualquer
    pessoa que faria isso."

    $Asterion.change("emotion", "neutral")

    asterion "Também não quero que você seja machucado. Você tem sido um bom mestre.
    Então, você pode esperar que eu o defenda de qualquer um que tente forçá-lo a fazer isso."

    asterion "Se o que você disse esta noite for verdade, se você realmente quer me tornar
    seu parceiro de negócios, está é a única coisa que me convencerá de uma vez por todas."

    asterion "Eu nunca mais quero voltar para o vale novamente. É tudo o que quero."

    asterion "Me conceda este único pedido e eu..."

    pause 2.0

    $Asterion.change("emotion", "tired")

    asterion "E eu o seguirei. Não porque você é meu mestre, mas porque então
    eu saberei quem você é... que você realmente quis dizer tudo o que falou."

    menu:

        "Vamos nessa.":

            $Asterion.change("emotion", "relieved")
            $Luke.change("emotion", "neutral")
            $Kota.change("emotion", "neutral")
            you "Sim, vamos nessa, prepare o contrato."

        "Não tenho tanta certeza disso.":

            you "Eu não tenho tanta certeza. Não me oponho à cláusula, mas a ameaça de amputação
            não é pouca coisa."


            asterion "Sim, mas você deve reconhecer que não será difícil para você respeitar
            esta cláusula. Nunca haverá um motivo real para me mandar ao vale,
            a não ser que você queira me torturar."

            asterion "E se houver a necessidade de fazer isso — o que jamais acontecerá —
            eu ainda posso escolher ir para lá por vontade própria."

            asterion "Devo acrescentar que se você assinar e aceitar minha proposta, há
            algo que você ganhará."

            you "O que?"

            $Asterion.change("emotion", "neutral")
            $Luke.change("emotion", "neutral")
            $Kota.change("emotion", "neutral")
            asterion "Kota, Luke. Vocês estão ouvindo tudo isso."

            asterion "Vocês ouviram meu pedido. Vocês sabem o que eu quero, e o poder que [player_name] possui."

            asterion "Se ele realmente assinar o contrato, o que isto significaria para vocês?"

            $Kota.change("emotion", "laughing")
            $Kota.change("leftarm", "raised")
            $Kota.change("rightarm", "raised")
            kota "Ah, Astério, você é um demônio!"

            $Luke.change("emotion", "annoyed")
            $Luke.change("arm", "pointing")
            luke "O que? Como assim?"

            $Kota.change("emotion", "happy")
            $Luke.change("arm", "hip")
            $Kota.change("leftarm", "relaxed")
            kota "Luke, se [player_name] assinar isso, então nosso pequeno problema também está resolvido.
            Nós dois poderemos saber com certeza que [player_name] não abusará de seus poderes."

            $Luke.change("emotion", "horny")
            luke "Ah. Ah sim, isso mesmo."

            $Kota.change("rightarm", "relaxed")
            $Luke.change("emotion", "cocky")
            $Luke.change("arm", "pointing")
            luke "[player_name], esse é um acordo muito bom! Só assina o bagulho aí, vai ser ótimo."

            $Asterion.change("emotion", "tired")
            $Luke.change("arm", "hip")
            you "Mas não é o seu braço que pode ser amputado!"

            $Kota.change("emotion", "neutral")
            kota "Mas lembre-se que existe um sistema à prova de falhas, também podemos revogar o contrato se todos concordarmos."

            $Kota.change("emotion", "puzzled")
            kota "Além disso, e deixe-me ser franco com você, já não lucrou o suficiente com
            toda essa provação? Você pode fazer chover diamantes de suas mãos, possui a magia
            de todo um domínio na ponta dos dedos."

            if player_background  == "speedrunner":

                $Luke.change("emotion", "laughing")
                luke "Ei, se o pior acontecer, já que você tem tudo mesmo,
                o que é um conjunto de dedos a menos?"

            $Luke.change("emotion", "neutral")
            $Kota.change("emotion", "neutral")
            kota "E tudo o que estamos pedindo é uma, apenas uma única restrição. Então Luke e eu também
            poderemos confiar em você."

            luke "Olha, eu tô um pouco perdido, mas se tô entendendo a ideia geral... Sim,
            eu tô com o bafo de lagarto aqui."

            you "E o que acontece se eu {i}não{/i} assinar?"

            $Kota.change("emotion", "happy")
            kota "Entramos em greve!"

            $Luke.change("emotion", "surprise")
            luke "Entramos?"

            kota "Apenas confie em mim nessa."

            $Luke.change("emotion", "neutral")
            $Kota.change("emotion", "neutral")
            "O acordo parece sólido — é compreensível que Astério pedisse por isso."

            "Mas a ideia de ter seu braço amputado — a mera sensação de imaginar —
            é o suficiente para se fazer o ácido estomacal bater no fundo da garganta."

            "Assinar este contrato pode ser a coisa certa a se fazer, mas isto não torna a ação nem um pouco mais fácil."

            "Você respira fundo e range os dentes. Seu estômago continua girando e se contorcendo,
            mas este é o caminho a se seguir. É sim, e você não pode negar."

            "Você engole o nó em sua garganta e olha para cima — para todos olhando em sua direção,
            esperando por sua escolha fatídica."

            show Asterion:
                ease 0.1 xalign 0.503
                ease 0.1 xalign 0.5
                repeat
            "E então, há Astério."

            #show Asterion, he's ultra nervous
            #show him for two or three seconds, shaking in anxiety

            pause 2.0

            you "Vou estar contando com você se fizermos isso. Serei tanto seu refém quanto você é meu."

            you "Não mandar você para o vale é fácil, e farei tudo ao meu alcance para te
            manter protegido de qualquer um que possa coagir você. Mas vou precisar da sua ajuda
            para que assim possamos evitar um desastre."

            pause 1.0

            show Asterion:
                ease 0.1 xalign 0.5
            $Asterion.change("emotion", "relieved")
            asterion "Você... Você vai assinar?"

            you "Sim. E conto com você."

            you "Prepare o contrato."

    play music "music/seikilos.mp3" fadeout 2.0 fadein 2.0

    show blackback:
        alpha 1.0
    with Dissolve(2.0)

    "Quatro sombras banhadas por luz vermelha, amontoadas ao redor de uma mesa com vista para o céu estrelado."

    "Um pedaço de pergaminho seco e grosso, um manuscrito rabiscado, cláusulas e termos murmurados
    entre acessos de tosse. Ideias crescendo como teias de aranha até se tocarem e serem tecidas juntas."

    "O minotauro desenha uma escrita com a qual você não está familiarizado — algo mais antigo que o próprio
    alfabeto. Ele se mistura, desaparece e reaparece, e então se reconstrói em palavras e frases."

    "Cada parágrafo vinculado e trancado ao outro. Cada cláusula é cortada, estudada e
    refeita uma dúzia de vezes."

    $Luke.change("arm", "hip")
    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "puzzled")
    $Asterion.change("emotion", "sad")
    show Luke behind blackback:
        zoom 0.85 xalign -0.1 xzoom -1 yalign 1.0
    show Kota behind blackback:
        zoom 0.85 xalign 1.1 xzoom -1 yalign 1.0
    show Asterion behind blackback:
        zoom 0.9 xalign 0.5 xzoom 1 yalign 1.0
    hide quartertable
    "Até tornar-se uma teia assustadora de causa e consequência — se Astério algum dia for
    para o vale como resultado de força ou coerção, você terá um destino terrível."

    hide blackback
    with Dissolve(1.0)
    "O suor escorre da testa do minotauro. Ele a enxuga com a mão trêmula,
    olha para você e, em seguida, desvia o olhar."

    "O primeiro rascunho está feito. É deixado para dormir e envelhecer enquanto todos vocês
    olham para as estrelas e compartilham um momento de silêncio."

    "Kota esfrega as têmporas enquanto se esforça para captar as frases em meio à luz vermelha.
    Luke olha para as estrelas; sua concentração se foi. Os cobaltos estão dobrando alguns pedaços de papel."

    $Asterion.change("emotion", "tired")
    "Você e Astério ficam a trinta centímetros um do outro. Você desvia o olhar, o momento persistindo
    antes de vocês olharem nos olhos um do outro. Depois a lua, as estrelas e, por fim, as mãos do minotauro."

    "Volte para o contrato. Leia-o em voz alta, pese cada palavra uma contra a outra,
    o fardo e a bênção de cada parte."

    "Então comece de novo — um novo pergaminho para pintar o quadro novamente: desta vez com uma
    vírgula aqui, um ponto ali."

    "Uma coisa tão humana, atribuir grande valor à precisão de cada frase. Deuses, em sua época,
    não conseguiam se importar com as dores e tristezas dos meros mortais — quaisquer promessas
    que os Olimpianos faziam eram vagas e descuidadas."

    "Mas os humanos têm tanto a perder e pouco a ganhar."

    "Mesmo este minotauro imortal, homem em tudo, exceto na forma."

    "Mas você, bom mestre. O que o trouxe a esta terra feia, a este hotel vazio e abandonado?"

    "Existem caminhos sombrios e nada auspiciosos que você poderia ter trilhado, e outros de grande glória também.
    É aqui que você está, no entanto."

    "Nós, sentados à margem, podemos apenas esperar que tenha sido este momento que você buscou."

    "Ah... Seria um exagero presumir que você veio aqui para desfazer as algemas do híbrido?"

    "Que mestre estranho você é... Centenas vieram antes, mas nenhum foi tão tolo
    a ponto de fazer o que você está prestes a fazer."

    "A humanidade é de fato peculiar. Perdoe-nos se vagarmos, mas a questão nos atormenta.
    A humanidade mudou com o tempo, ou você é talvez um espécime raro e excelente?"

    "Ah, o minotauro se agita. É chegada a hora, nosso bom senhor."

    $Asterion.change("emotion", "tired")

    asterion "O contrato está pronto, [player_name]."

    show Kota:
        ease 1.0 zoom 1.0
    pause 2.0
    #kota reads the contract out loud

    $Kota.change("rightarm", "raised")
    $Kota.change("emotion", "neutral")

    "Kota dá um passo à fremte e lê o contrato em voz alta."

    contract "Pela vontade do Mestre do Labirinto este contrato vinculativo é estabelecido,
    para que possa impor seu conteúdo ao mundo e seu povo."

    contract "Por meio deste, o Mestre comanda à existência dois objetos interligados: um anel de chumbo
    para ajustar-se ao redor do bíceps de um homem e uma guirlanda de louros da largura do braço do prisioneiro."

    contract "Estes dois objetos devem estar ligados em causa e efeito, assim como seus portadores."

    contract "Aquele que vestir o anel de chumbo se encontrará em uma situação onde removê-lo será impossível, exceto
    mediante à revogação deste contrato."

    contract "Quem primeiro vestir a coroa de louros se tornará seu proprietário permanente e imutável."

    contract "Se o dono da coroa de louros alguma vez for levado para o vale do Labirinto
    —seja por coerção, ordem, ou força— então o anel de chumbo virá a contrair e fechar de
    forma a amputar o braço de seu portador."

    contract "Pela vontade do Mestre, este contrato poderá ser revogado apenas se todas as suas partes —
    portador do anel de chumbo, dono da coroa de louros, e as duas testemunhas presentes durante
    a sua assinatura — o consentirem."

    contract "Tal é a vontade do Mestre."

    $Kota.change("rightarm", "relaxed")
    show Kota:
        ease 1.0 zoom 0.85
    pause 2.0
    show Kota behind Asterion
    $Asterion.change("emotion", "sad")

    asterion "Mestre, é realmente isso que você quer?"

    you "Sim. Eu te disse mais cedo hoje, e falei sério, Astério."

    you "Você esperava que eu voltasse atrás com a minha palavra agora que estamos colocando consequências na mesa?"

    pause 2.0

    asterion "Sim, eu esperava. Eu {w=0.2} — Eu não posso, não poderia, imaginar um Mestre aceitando condições tão absurdas."

    you "Suponho que você esteja errado, então. Mas não tem por que se sentir mal, às vezes isso é uma coisa boa."

    $Asterion.change("emotion", "tired")

    "Você pega a caneta e assina o contrato."

    play sound "sfx/hum.ogg"
    #play the distant sound of the labyrinth groaning, but no light changing this
    #time since they are outside and in nighttime

    "O contrato estremece em sua mão. Seu papel fica mais grosso, quase com textura de couro."

    pause 1.0

    $Asterion.change("emotion", "neutral")
    $Kota.change("emotion", "happy")
    $Luke.change("emotion", "happy")


    $add_file('Contract', "Rings")

    $global_affection += 2

    play sound "sfx/asterionchord.mp3"
    "{i}Você assinou o {color=[UIColorOrange]}Juramento dos Anéis Vinculativos{/color}.\n
    Você pode reler os termos no menu de arquivos."

    pause 1.0

    show Asterion:
        ease 1.0 yalign 1.2
        ease 1.0 yalign 1.0

    "Os dois anéis materializam na mesa. Astério pega o de chumbo, você pega
    a guirlanda de louros, e então vocês se voltam um para o outro."

    you "Asterion. Eu prometo não te mandar para o vale sob nenhuma circunstância,
    e juro que te protegerei de qualquer um que tente fazer isso."

    you "Juro pelo meu braço, sabendo bem das consequências de quebrar minha palavra.
    Mas faço isso com a consciência tranquila; não há razão para eu violar essa regra."

    you "Eu prometo ser o bom mestre que você e esse hotel merecem."

    pause 2.0

    #Asterion is speechless for a while

    $Asterion.change("emotion", "contemplative")

    pause 3.0

    asterion "Mestre [player_name], sua bondade e piedade são incomparáveis."

    asterion "Este contrato não pede nada de mim. Apesar disto, oferecerei minha palavra vinculativa em seu favor."

    asterion "Eu prometo protegê-lo, como é meu dever, e manter longe desta terra
    qualquer um que possa ameaçá-lo por meio de nosso juramento."

    $Asterion.change("emotion", "smiling")

    asterion "Eu juro que farei todo o possível, dentro ou fora de meu alcance,
    para que você nunca se arrependa de sua misericórdia."

    $Asterion.change("emotion", "contemplative")

    pause 1.0

    $Kota.change("rightarm", "raised")
    kota "Muito bem então, agora —"

    $Kota.change("emotion", "surprise")
    $Kota.change("rightarm", "relaxed")
    you "Com licença, Kota, tem uma coisa que eu gostaria de acrescentar."

    $Luke.change("emotion", "neutral")
    $Kota.change("emotion", "neutral")
    $Asterion.change("emotion", "neutral")

    you "De fato, Astério, o contrato não exige nada de você. É por isso que vou exigir uma coisa agora."

    you "Não me importo em registrar isso na papelada, ou se pode ser transformado em um
    contrato em primeiro lugar. Ainda assim, quero que você atenda a esse pedido simples."

    asterion "O que é, meu senhor?"

    you "Efetivamente agora, você aceitará seu lugar como meu parceiro de negócios e, de agora em diante,
    me chamará pelo meu nome."

    $Kota.change("emotion", "happy")
    $Luke.change("emotion", "happy")
    pause 2.0

    $Asterion.change("emotion", "relieved")

    asterion "Sim, [player_name], eu irei. Eu aceito seu pedido."

    pause 1.5

    $Asterion.change("emotion", "contemplative")

    $Kota.change("emotion", "neutral")
    $Kota.change("rightarm", "raised")
    kota "Caso não haja mais objeções, então... Astério, [player_name]..."

    $Kota.change("rightarm", "relaxed")
    show Asterion:
        ease 1.0 zoom 1.05 yalign 1.1

    "Você estende seu braço esquerdo e o minotauro desliza cuidadosamente o anel até que ele se ajuste ao seu bíceps."

    "Ele não contrai ou incomoda, entretanto — mal parece que está roçando sua pele,
    mesmo que esteja firme e imóvel."

    "O minotauro estende o braço e você faz o mesmo — desliza a guirlanda de louros,
    com suas folhas acariciando o pelo de Astério, até que ela se ajuste ao seu bíceps."

    hide Asterion
    with Dissolve(0.5)

    $Asterion.change("emotion", "smiling")
    $Asterion.change("armwear", "laurel")
    $wardrobe.add("armwear", "laurel")

    show Asterion:
        zoom 1.05 yalign 1.1 xalign 0.5
    with Dissolve(0.5)
    pause 1.0
    show Asterion:
        ease 2.0 zoom 1.0 yalign 1.0

    pause 2.0

    "Está feito, bom mestre: sua pequena cerimônia, este rito peculiar. Vincula você
    a aliviar o fardo do prisioneiro."

    $Kota.change("emotion", "happy")
    kota "Que dupla singular. Esses anéis combinam com vocês, e que nobre cerimônia!"

    $Luke.change("emotion", "cocky")
    $Luke.change("arm", "pointing")
    luke "E agora{w=0.5}, você pode beijar a noiva."

    $Kota.change("emotion", "angry")
    kota "E agora {w=0.5}você abre a boca para estragar o momento, seu camponês inculto."

    $Luke.change("emotion", "laughing")
    luke "Sempre!"

    $Luke.change("emotion", "neutral")
    $Luke.change("arm", "hip")
    $Kota.change("emotion", "neutral")
    pause 2.0

    show Asterion:
        xzoom -1
    $Asterion.change("emotion", "contemplative")
    "Algo puxa sua calça."

    show Luke behind cobalt_right
    show Kota behind cobalt_right
    show Asterion behind cobalt_right

    show cobalt_right:
        xalign -0.5 yalign 2.0 xzoom 1 zoom 1
        ease 2.0 xalign 0.1 yalign 1.0
    #show one of the cobalts

    "O garotinho encara você a trinta centímetros de distância, e então estende
    o braço rapidamente para lhe oferecer algo."

    "É uma pequena rosa de papel."

    "Você só tem tempo para pegá-la antes dele fugir para se esconder atrás de uma pedra."

    show Asterion:
        pause 0.5
        xzoom 1

    show cobalt_right:
        ease 1.5 xalign 1.4
    #show kota and Luke again

    $Kota.change("emotion", "happy")
    $Luke.change("emotion", "laughing")
    kota "Aww, [player_name], ele queria te dar um presente!"

    $Luke.change("emotion", "neutral")
    luke "É. Acho que você tá certo: eles podem ser fofos."

    $Kota.change("emotion", "neutral")
    kota "É claro que estou certo, por que você duvidou de mim?"

    pause 1
    show Luke behind Asterion:
        xzoom 1
        pause 1
        ease 2.0 xalign -1.0 zoom 0.6
    show Kota behind Asterion:
        ease 4.0 xalign -1.0 zoom 0.6

    "Os dois começam a brigar, como de costume. Você observa, com Astério ao seu
    lado, ambos banhados pela luz vermelha da lamparina de baixo e pela branca luz do luar de cima."

    "Atrás está o hotel, alto e majestoso, uma parede entre vocês e o horrível vale."

    "O braço de Astério aquece contra o seu. Desta vez, não há recuo assustado ou tenso estremecimento."

    "O vento passa em torno e através de vocês e, desta vez, vocês dois se inclinam juntos
    — aquele que começou, você não consegue dizer."

    asterion "[player_name], não diria que isso pede uma bebida?"

    you "Sim. Mas Luke só comprou a cerveja aguada dele, poderíamos dividir uma garrafa de vinho no hotel."

    asterion "Eu gostaria disso. Seria um final memorável para esta noite."

    "Uma brasa tão pequena, mas seu coração bate vermelho mesmo assim."

    scene bg black
    with Dissolve (2.0)
    pause 2.0

    "Vocês dois voltam para casa, batendo os ombros enquanto caminham."

    "Naquela noite, o minotauro é recebido com um sono pesado e reparador.
    E, no dia seguinte, pela primeira vez desde a Segunda Guerra Mundial,
    ele se permite um dia de paz sem intercorrências."

    pause 3.0

    play music "music/asterion.ogg" fadeout 2.0 fadein 2.0

    $chapter = "Hades"
    call screen ChapterTransition("Hades", "O tribunal", 'Hades')
    pause 0.5
    $save_name=output_save_name("Hades IV")

    "O minotauro e Caronte, barqueiro dos mortos, navegaram através do rio Estige.
    A jornada foi breve, mas não desagradável."

    "Para a esquerda e direita o recém-morto olhava, para torres de rocha bruta projetando-se do
    chão em formas familiares — templos, casas, palácios — e incompreensíveis
    — edifícios que desafiavam a geometria e a lógica."

    "O mundo dos mortos carecia de luz solar, mas seus objetos também careciam de sombra.
    Tudo brilhava com uma humilde luz interna."

    "Até mesmo as águas do Estige brilhavam. Tão claras eram que o príncipe cretense podia
    contemplar suas profundezas, o depósito de areia repousante salpicado de pedras preciosas e prata."

    "Astério cantarolava acompanhando o remo do barqueiro e, quando uma gota de tédio
    caiu em sua mente, ele começou a cantar. Primeiro todas as músicas que lhe ensinaram,
    depois as novas que serpenteavam junto com o barco."

    "Ele cantou até o nó de sua garganta se desfazer, e então eles chegaram."

    "Adiante estava um império de rocha, pedras preciosas e metal, o qual se erguia do solo na forma
    de um templo, mas com a grandeza de um palácio."

    "\"Menor que o palácio de Cnossos,\" pensou o minotauro — ignorando que suas
    lembranças do lugar vinham dos olhos de uma criança."

    "À esquerda e à direita havia altos muros de pedra que haviam sido esculpidos em barras.
    Ele podia ver o reino de Hades além, campos de açafrão e uvas, pastagens
    onde cabras e vacas com chifres altos pastavam."

    "Os guardas de Hades aproximaram-se com lanças ao alto como se esperassem uma luta,
    já que os recém-mortos não eram conhecidos por sua obediência, mas, ao verem a fisionomia dele,
    pararam onde estavam."

    "O príncipe híbrido curvou-se e falou com uma voz tão clara, tão melodiosa,
    que sentiram como se um velho amigo e senhor estivesse se dirigindo a eles."

    "Ele pediu instruções para chegar a seu destino e eles o ofereceram, indicaram-lhe ao
    palácio onde os mortos eram julgados."

    "Eles o guiaram durante a primeira metade, passando pelas multidões de almas enfermas
    ainda no processo de aceitarem suas próprias passagens, antes que se tornasse claro que este assunto não exigia supervisão."

    "Na segunda metade da jornada, portanto, eles o seguiram e conversaram.
    Perguntaram sobre Creta, berço da civilização, e Astério se gabou de seus campos
    de açafrão e como eles balançavam ao vento."

    "O príncipe perguntou sobre a vida em Hades, que provações o Senhor do Bom Conselho
    considerava adequado impor a seus súditos. A resposta deles vieram em vozes efervescentes e destemidas."

    "Guarda" "Se você for considerado um herói, como sua fisionomia implicaria, os Campos
    Elísios esperam por você, onde você encontrará uma existência desprovida de tragédia."

    "Guarda" "Quanto a nós, homens de pouca glória, é nos Campos de Asfódelos
    que vivemos. Aqui existimos como se ainda estivéssemos vivos, trabalhando duro, mas não sofrendo,
    não desfrutando de privilégios nem de maldição."

    asterion "Meu amigo, suas palavras são gentis e você não precisa me bajular. Minha fisionomia está
    tão longe de ser heróica quanto possível e tenho vivido sem mérito digno de louvor."

    "Guarda" "É mesmo? Mas não se engane, não digo bajulação alguma.
    Você carrega uma semelhança familiar a nós, guardas de Hades, embora invertida."

    "Guarda" "Se sua língua for honesta e você não possuir nenhuma glória digna de louvor,
    então oro que considere meu conselho — alguém como você seria uma adição bem-vinda à nossa categoria."

    "Perguntas nadam na mente do príncipe, tantas delas, mas poderia-se escolher apenas uma de cada vez."

    "Por mais que ele desejasse saber sobre seu futuro, o passado ainda tinha um fascínio ao qual ele não podia resistir."

    asterion "Amigo, por favor, fale sem medo; o que você quis dizer com minha aparência
    ser familiar? Será que você viu aqui gente como eu, amaldiçoada com a aparência de um touro?"

    "Guarda" "Não como você, mas entre a elite de Hades você encontrará homens com olhos de boi
    da linhagem de Creta, suas vozes meandram tanto quanto a sua."

    "Guarda" "Sua grandeza é bem conhecida e incomparável. Por isso não posso acreditar que você seja uma alma
    humilde e medíocre — a grandeza flui em seu sangue tanto quanto cai em seus chifres."

    "Eles chegam em um corredor tão alto quanto o Palácio de Cnossos, pedra polida
    de cima a baixo com pedras preciosas incrustadas onde nasceram."

    "No final do corredor havia três pódios, cada um com um juíz — homens com olhos de touro,
    pele bronzeada e roupas bastante familiares às do príncipe cretense."

    "Com seus ombros largos como as estepes erguidos com orgulho, o minotauro encontrou seu destino de cabeça."

    stop music fadeout 3.0

    pause 2.0

    $chapter = "Sertão I"

    call screen ChapterTransition("O Sertão I", "O amuleto", 'Hinterlands')
    pause 0.5
    $save_name=output_save_name("Sertão I")

    play music "music/CrossingTheAstralBridge.ogg" fadeout 1.0 fadein 1.0

    "O minotauro sonha. Visões instantâneas ao seu redor, mexendo para frente e para trás."

    image cg7base = "images/cg/cg7_base.png"
    image cg7storm1 = "images/cg/cg7_storm1.png"
    image cg7storm2 = "images/cg/cg7_storm2.png"
    image cg7storm3 = "images/cg/cg7_storm3.png"
    image cg7p1 = "images/cg/cg7_p1.png"
    image cg7p2 = "images/cg/cg7_p2.png"
    image cg7top = "images/cg/cg7_top.png"

    scene cg7base
    show cg7storm1
    show cg7top
    with Dissolve (2)

    pause 2

    "O sol batendo em suas costas. O pelo estava sempre úmido de usar capuz,
    um fio de suor escorrendo pela testa. Argila seca endureceu o tecido, ele cheirava azedo."

    "Pano macio sobre seus chifres desabrochados, um pouco de sombra sobre seus olhos. Cauda dobrada dentro do short."

    "E então, capuzes rasgados de quando seus chifres não puderam ser escondidos."

    "Hematomas antes da aula, escondidos sob o pelo preto.
    Depois, uma ou duas horas de números — pequenos blocos frios e suaves."

    "Ele estava segurando um lápis agora, não mais do que um centímetro de comprimento depois de ser usado até o final."

    "Ele anotou os números com amor. Cada sete cruzado no meio,
    linhas simétricas de seis e noves, uma curva perfeita para cada dois."

    "Demorou um tempo, mas ele dominou o oito.
    As duas bolas tinham que estar espelhadas. Então a aula acabou."

    $renpy.music.set_volume(2.0, delay=1, channel='sound')

    play sound "sfx/footsteps_dirt.ogg"

    "Anos depois, sintaxe e gramática. Verbos, adjetivos, substantivos."

    "\"Aproxime-se das mulheres delicadas\" disse a professora.{w} \"Atravesse o mar incansável\".{w}
    Frases estendendo-se indefinidamente, tijolinhos elegantes."

    "\"Touro de casco oco,\" disse ele. Risinhos. O menino não gostava destas palavras."

    "Depois vieram as interpretações, textos. Ele gostava das histórias, mas as regras de sua mente
    eram diferentes daquelas que os livros prezavam."

    "História e Geografia eram enigmáticas. Muito macias e flexíveis, elas escaparam
    por entre seus dedos."

    "Filosofa era aprazível, contanto que fosse parecida com Matemática, mas Biologia era um insulto."

    "Hematomas após reprovar em Biologia. Punido por revidar; obrigado a usar rolhas de garrafa nos chifres na escola.
    Abandonou a escola, mas manteve os números e todos os tijolinhos que pôde carregar."

    $renpy.music.set_volume(4.0, delay=1, channel='sound')

    play sound "sfx/footsteps_dirt.ogg"

    "Caminhando para a loja com a mãe. Os homens zombam e cospem insultos na direção deles.
    Ele finge que não sabe o que \"zoófila\" significa."

    "Ela puxa o braço dele, talvez desta vez ela o desloque.{w}
    Ela nunca disse quem é o pai dele. Talvez ela não saiba. Mas \"ele é humano,\"
    ela o assegura entre tragadas de fumaça de cigarro."

    stop sound fadeout 1.0
    hide textbox
    pause 1.0

    show cg7p1 behind cg7top
    with Dissolve(2)
    pause 2.0

    "Há uma bondade na família. As únicas pessoas que consideram adequado ignorá-lo."

    "Mas isto não basta. Fugiu. Passou um tempo no mundo selvagem, depois na cidade.
    Procurou um emprego. Voltou para casa."

    "Tentou novamente, desta vez roubou dinheiro suficiente para pegar um ônibus para algum lugar mais distante."

    "Dormiu debaixo de uma ponte, sempre durante o dia. A noite esconde seus chifres e focinho."

    "O corredor se esvazia quando ele vai para a loja. Pedem-no para sair da lanchonete
    com um bilhete na sacola para não comer lá dentro. Bom o suficiente para seu dinheiro roubado, mas não para sua presença."

    "Falhar. Tentar novamente. Falhar pior. Ir para casa."

    $renpy.music.set_volume(1.0, delay=1, channel='sound')

    pause 1.0

    "???" "Ah, eaí. Estou te incomodando?"

    hide cg7storm1
    show cg7storm2 behind cg7top
    with Dissolve (1)

    "Antes mesmo de sua consciência despertar, o minotauro já plantou seus cascos no solo
    e se enfiou mais fundo na alcova."

    "Suas orelhas sacodem. Os olhos saltam ao redor até focar no homem bloqueando o sol.
    Ele não consegue detectar nenhuma característica — e, na verdade, uma coceira na parte de trás de sua cabeça
    torna impossível dizer para o que ele está olhando."

    "Palavras cruzam sua mente. Seus lábios se contraem. O homem está falando com ele ou há
    mais alguém fora de vista?"

    "Talvez ele não tenha me visto, o minotauro pensa. Ele separa os lábios e respira
    fundo, lentamente entre os dentes, para não fazer nenhum som."

    "???" "Ah, cheguei numa hora ruim, não é? Sinto muito por incomodar você."

    "???" "Mas eu estava de passagem, vim aqui para resolver um problema pessoal, e um amigo de família
    fez questão de dizer que eu deveria encontrar você."

    play sound "sfx/pageflip.ogg"

    "O homem tira um bloco de notas do bolso de trás. Cada virada de página é acompanhada por um
    quebradiço barulho de papel. Ele o verifica antes de continuar."

    "???" "Mais uma vez, desculpe incomodar. E eu sei que o que eu estou prestes a dizer vai soar estranho,
    mas por acaso você é o proprietário ou mora em um hotel?"

    pause 1

    stormq "É o que? Que pergunta besta. Tu acha que eu ia tá
    dormindo aqui se fosse dono de um hotel?"

    "???" "Sim, sim. Me desculpe, eu tinha que ter certeza. Não posso descartar nenhuma possibilidade."

    play sound "sfx/pageflip.ogg"

    "O homem dá mais uma olhada em seu bloco de notas, seguido por um suspiro enquanto ele passa a mão
    pelo cabelo, alisando-o para trás."

    "???" "Quando eu passei pela aldeia, me disseram que você estava procurando emprego.
    Acontece que eu preciso de ajuda e pode ser um bom uso do seu tempo."

    "O minotauro range os dentes enquanto procura por malícia na voz do estranho."

    "Cada palavra dissecada, cada movimento julgado."

    hide cg7storm2
    show cg7storm1 behind cg7top
    with Dissolve (1)

    pause 2.0

    stormq "Cê deve ter achado o cara errado."

    "O estranho intercala o peso entre as pernas. Possivelmente franze a testa, mas o minotauro não
    consegue dizer com certeza — é como se houvesse um buraco onde o rosto do homem deveria estar."

    "???" "Não, tenho certeza de que você é exatamente quem eu estou procurando. Me disseram que eu poderia encontrar um..."

    hide cg7storm1
    show cg7storm2 behind cg7top
    with Dissolve (0.5)

    pause 1.0

    "Aí está. Aquela mesma coisa em todos os homens e mulheres."

    "O minotauro aperta os punhos e deixa a cabeça cair um pouco, apontando os chifres na direção do homem."

    stormq "Um o que?"

    pause 1.0

    "???" "Alguém parecido comigo. Que possa se identificar com a minha situação. \"Farinha do mesmo saco\" e tudo mais."

    "A coceira no fundo de sua mente fica enlouquecedora. A voz do homem soa entrecortada, ou talvez os ouvidos do minotauro estejam falhando."

    "???" "Ah, deixa eu ir direto ao ponto. Vai fazer muito mais sentido se eu simplesmente mostrar a você."

    play sound "sfx/pageflip.ogg"

    "O homem tira um livreto do bolso, o abre e passa o dedo sobre uma página."

    pause 1.0

    show cg7p1:
        ease 2.0 alpha 0.5
    show cg7p2:
        alpha 0
        ease 2.0 alpha 0.5

    pause 1.0

    "A coceira na parte de trás da mente do minotauro morre, mas, em contrapartida, sua visão
    começa a parecer errada. Ele continua encarando as feições borradas e ilegíveis do homem."

    hide cg7storm2
    show cg7storm3 behind cg7top
    with Dissolve (0.5)

    "Por um momento, elas até parecem..."

    pause 1.0

    show cg7p1:
        ease 2.0 alpha 0.0
    show cg7p2:
        ease 2.0 alpha 1.0

    pause 1.0
    pq "Pronto. Melhor assim."

    "O sol desaparece atrás do horizonte e, finalmente, o minotauro consegue ver o rosto da criatura.
    Seu coração bate forte enquanto ele levanta com rapidez."

    $P.change('tail', 'low')
    $P.change('emotion', 'content')
    $P.change('leftarm', 'loose')
    $P.change('rightarm', 'palm')
    $P.change('clothes', 'dressshirt')
    $Storm.change("emotion", "embarrassed")
    $Storm.change("clothes", "football")
    $Storm.change("wheat", "False")

    scene image "images/bg/bg acude.jpg"

    show P:
        xalign 0.9 yalign 1.0

    show Storm:
        xalign 0.1 yalign 4.0
        ease 2.0 yalign 1.0

    with Dissolve (1.0)


    stormq "{i}Que porra é você?{/i}"

    $P.change('leftarm', 'hip')

    pq "Um homem!{w} Ou assim pareceria para a maioria.{w=0.2} Mas, na verdade, eu sou como você,
    só um pouco... diferente aqui e ali."

    $P.change('rightarm', 'pointing')
    $P.change('emotion', 'dominant')

    p "As pessoas me chamam só de P, então... Prazer em conhecê-lo, senhor...?"

    pause 1.0

    show Storm:
        yalign 1.0
        ease 1.0 xalign -0.1

    pause 1.0

    "\"Sonho,\" o minotauro pensa. \"Isso tem que ser um sonho.\""

    "Ele dá um suspiro que fica preso em sua garganta. Bile e fogo borbulham no topo de seu estômago."

    pause 1.0

    $P.change('rightarm', 'palm')

    p "Bem, não importa por enquanto. Agora que você pode me ver como eu sou, me deixe explicar a minha situação."


    play music "music/WhenDarknessTakesFlight.ogg" fadeout 1.0 fadein 1.0

    $P.change('emotion', 'deepthinking')
    $P.change('rightarm', 'hip')

    p "Eu estou aqui no sertão para tratar de um certo assunto de família. Meu avô,
    que Deus o tenha, passou boa parte da vida dele atrás de um lugar muito especial."

    p "Ele o chamava de \"hotel minotauro\". Deveria estar perto dessa área,
    mas ele nunca conseguiu encontrar."

    p "E sim, como você pode ver... Eu não sou realmente um humano, sou? Nem meu avô, é claro.
    As chances são de que esse hotel que eu estou procurando seja bastante peculiar, também."

    p "Então, eu quero provar que o meu querido velho estava certo. E, por sorte,
    ouvi uma história sobre um \"minotauro\", entre todas as coisas, aqui no vale."

    $P.change('emotion', 'thinking')

    p "Isso não pode ser uma coincidência, certo? Então vim aqui para ver com os meus próprios olhos e
    com certeza você se parece com um."

    $P.change('emotion', 'dominant')
    $P.change('rightarm', 'pointing')

    p "E deixa eu te contar, encontrar você não foi uma tarefa fácil. Quanto mais perto eu chegava dessa lagoa,
    menos sentido as estradas faziam. Tem alguma coisa estranha acontecendo aqui."

    $Storm.change("emotion", "neutral")
    $P.change('rightarm', 'palm')

    p "Mesmo que você não tenha informações sobre o hotel minotauro, ainda tenho um trabalho para você."

    p "Eu simplesmente não posso acreditar que isso seja uma coincidência. Uma parte de mim quer acreditar
    que Os Destinos conspiraram para fazer isso acontecer."

    $P.change('emotion', 'content')
    p "Então, eu quero contratar você. Acredito que você possa me ajudar a encontrar o que procuro."

    $P.change('rightarm', 'hip')
    p "Parece bom para você?"

    $P.change('emotion', 'neutral')
    $Storm.change("emotion", "sad")

    pause 2.0

    "Os últimos resquícios de sono fogem da mente do minotauro... Seus cascos raspam
    a argila seca e seus dentes rangem enquanto seu coração queima."

    "\"Se isso não é um sonho, então eu devo estar amaldiçoado ou enlouquecendo...{w=0.3} ou isso é
    um monstro tentando me enganar\"."

    $Storm.change("emotion", "neutral")

    stormq "Como eu sei que tu não tá querendo me enganar? Que... que você não é um demônio ou algo assim."

    $P.change('emotion', 'thinking')

    p "Demônio? Isso é...{w=0.2} Você já viu um antes?"

    "Ele não viu. Nunca em todos os seus anos de existência ele testemunhou algo que,
    sem sombra de dúvida, rompeu o véu da vida mundana. Mas ele ouviu as histórias."

    $Storm.change("emotion", "angry")
    stormq "Tem um monte de coisa estranha por aqui. Nunca se sabe."

    $P.change('rightarm', 'thinking')

    p "Entendo.{w=0.2} Bem, eu {i}posso{/i} te dizer que não sou um demônio, mas não vou poder
    te dar muitas provas disso."

    p "Quer dizer, como alguém pode provar que não é um demônio? Eu não saberia de um teste para verificar isso."

    pause 1.0

    $P.change('emotion', 'dominant')
    $P.change('rightarm', 'hip')
    $Storm.change("emotion", "neutral")

    p "Dito isso, visto que você não parece convencido, posso adoçar um pouco o nosso acordo."

    $P.change('leftarm', 'notepad')
    $P.change('rightarm', 'pointing')

    p "Você viu meu truque, certo? Meu próprio disfarce humano, com o qual ninguém pode ver
    o que eu realmente sou. Tudo graças a esse livrinho aqui — que chamamos de \"amuleto\"."

    $Storm.change("emotion", "embarrassed")
    $P.change('rightarm', 'palm')

    p "Com certeza é difícil não ser humano, não é? Mais ainda quando você não
    tem como se misturar. Julgando pelo que eu ouvi sobre você na aldeia,
    parece que você nunca teve um desses..."

    "Em qualquer outra noite, dizer tais coisas para o minotauro provocaria uma briga.
    Especialmente quando falado no tom de alegre condescendência do pavão."

    "Mas não aqui, não agora. O minotauro olha para o livreto e, apesar
    da neblina de seu medo, visões o dominam."

    $Storm.change("emotion", "sad")
    "Para tornar-se um homem. E assim que as palavras penetram em seus pensamentos, tudo se destrava."

    "Sonhos surgem, uma fonte de possibilidades que ele selou em um vaso
    e se recusou a pensar sobre."

    $P.change('emotion', 'content')
    $P.change('leftarm', 'hip')
    $P.change('rightarm', 'hip')

    $Storm.change("emotion", "neutral")
    p "Antes de você ter qualquer ideia, lamento dizer que pegar o meu não vai
    lhe servir de nada — em sua maioria, eles só funcionam com a pessoa para a qual foram feitos."

    $P.change('emotion', 'dominant')

    p "Mas isso não é problema. Posso fazer um para você, aqui e agora."

    "E com isso, o minotauro percebe exatamente por que as pessoas vendem suas almas."

    $Storm.change("emotion", "angry")
    $P.change('emotion', 'neutral')

    stormq "Tu tá falando cada vez mais parecido com um demônio, sabia?"

    stormq "Um estranho aparecendo do nada, não é nem humano, e agora tá falando
    desses negócio estranho aí..."

    stormq "Se eu não tô sonhando então tu deve ser o tinhoso, com certeza."

    $P.change('rightarm', 'pointing')
    p "Não é um sonho, não senhor. E eu também não sou um demônio, isso é cristão demais para o meu gosto.
    Eu sou muito mais, digamos, o tipo de cara antiquado — bem parecido com você, imagino."

    $P.change('rightarm', 'hip')
    p "Embora... suponho que o que eu tenho a dizer não vai melhorar muito minha situação."

    $Storm.change("emotion", "neutral")
    stormq "Como assim?"

    $P.change('emotion', 'deepthinking')
    p "Como posso dizer... Vou ser franco com você."

    $P.change('rightarm', 'pointing')
    p "Eu quero uma coisa sua e estou disposto a pagar pelo seu tempo. Dito isso...
    a situação em que você se encontra, está {i}errada.{/i}"

    p "Pessoas como nós não devem andar por aí mostrando quem são de verdade.
    Essa é a lei, e podemos ser punidos por isso."

    $P.change('emotion', 'thinking')
    $P.change('rightarm', 'hip')
    p "Você é sortudo, de certa forma — esse lugar é um fim de mundo, então os boatos
    sobre você nunca foram muito longe."

    p "Ou talvez seja azar, visto que você teria conseguido ajuda há muito tempo
    se morasse em algum lugar decente."

    $P.change('emotion', 'dominant')
    $Storm.change("emotion", "embarrassed")
    p "Eu posso fazer um amuleto para você — aqui e agora. Quando esse dia acabar,
    você já vai ter seu próprio disfarce humano."

    p "Tudo que eu quero é que você considere aceitar a minha oferta. Vou te pagar para me ajudar a
    encontrar esse lugar, o \"hotel minotauro.\""

    p "Não deve demorar muito. Só vou ficar aqui por duas semanas no máximo."

    $P.change('emotion', 'content')
    p "E para adoçar ainda mais, enquanto trabalhamos juntos,
    vou te ensinar tudo o que tem para saber sobre... bem, não ser humano."

    show P:
        ease 1.0 xalign 0.7
    $P.change('emotion', 'neutral')
    $P.change('rightarm', 'palm')
    $Storm.change("emotion", "neutral")

    show Storm:
        ease 0.5 xalign -0.2
    p "Temos um trato?"

    pause 1.5

    "Sons saltam do outro lado da lagoa — gafanhotos e cigarras cantando, pássaros
    soltando gritos distantes enquanto voltam para seus ninhos."

    "Ondulações emergem do centro da próprio lagoa para dançar em sua superfície
    plácida. As ondas concêntricas seguem seu caminho até a costa, deslocando finas nuvens
    de sedimentos com seu movimento."

    "Um som de colisão líquida, como um mar distante dentro da própria cabeça."

    show Storm:
        ease 3.0 xalign 0.0 yalign 1.4

    "O minotauro respira fundo e se inclina. Beija-flores bicam sua
    nuca, levantando cada fio de pelo, um de cada vez."

    $Storm.change("emotion", "sad")

    show blackback:
        alpha 0.2
    with Dissolve(3.0)

    "É como um sonho de visões costuradas. Ir ao mercadinho
    da aldeia, onde todos os produtos têm uma fina camada de poeira da estrada.
    Onde as pessoas levantam as orelhas para ouvir seus passos."

    "A humilhação interminável que vem com a compra de algo tão simples como uma barra de chocolate."

    $P.change('rightarm', 'hip')
    "Cerrando os dentes contra os olhares deles. Ignorando sua repulsa por ele, como se ele carregasse alguma terrível deformidade. Sendo ignorado em resposta; melhor não interagir com o \"amaldiçoado\"."

    "Sua mente volta para quando ele era mais jovem. Quando ele usava um capuz para cobrir o rosto. O pânico de quando seus chifres ficaram largos demais para serem escondidos."

    pause 1.0
    "Os beija-flores cavam seus bicos em sua pele enquanto mais visões surgem."

    "Estar nas ruas como qualquer outro transeunte despretensioso. Andar por aí, sem se esconder do medo e do ódio. Aqueles que antes o encaravam agora ignorantes de sua identidade."

    $P.change('emotion', 'tired')
    "Ele pode criar um novo nome para si mesmo, renascer."

    "Isto é sua salvação."

    pause 1.0
    "E este homem, ele deve ser um demônio. Deve haver uma pegadinha."

    "Porém, recapitulando, ele já está condenado. Se não estava fadado ao inferno desde o dia em que nasceu, então as circunstâncias com certeza não o deixaram escolha."

    "Qualquer preço vale a pena para se tornar um humano. Até sua alma."

    $Storm.change("emotion", "neutral")
    show Storm:
        ease 2.0 yalign 1.0
    stormq "Cê não precisa mentir. Nada disso pode ser verdade, e se for, eu sei que você
    deve querer alguma coisa a mais."

    stormq "Ainda não me convenci que você não é um demônio, senhor, ou se você tá atrás de mais alguma coisa."

    stormq "Mas mesmo que você seja, e tem a intenção de levar a minha alma, considere
    o trato feito. Eu vou fazer o trabalho e qualquer outra coisa que você pedir."

    $Storm.change("emotion", "sad")

    stormq "Só me transforma em humano, não importa o preço."

    show blackback:
        ease 3.0 alpha 0.3

    pause 1.5

    $P.change('emotion', 'dominant')
    $P.change('rightarm', 'palm')
    p "Você é engraçado, rapaz. Muito bem, nosso pacto está selado."

    $P.change('rightarm', 'pointing')
    p "Melhor não perder tempo, hein? Me diz, como está a água naquela lagoa?"

    stormq "Salgada e morta. Lá não cresce nada, é melhor você não beber."

    $P.change('emotion', 'deepthinking')
    $P.change('rightarm', 'thinking')
    p "Não vai servir, então. Precisamos de um lugar adequado para fazer isso...{w=0.2} Acredito ter visto
    uma encruzilhada no meu caminho para cá."

    $P.change('emotion', 'thinking')
    p "O amuleto vai ser mais forte se criarmos ele lá. Vamos indo. E comece a recolher
    lenha seca no caminho, vamos precisar fazer uma fogueira."

    scene blackback
    with Dissolve(1)


    $Storm.change("wheat", "True")
    $Storm.change('emotion', 'smile')
    $P.change('emotion', 'content')
    $P.change('rightarm', 'hip')

    scene image "images/bg/bg crossroads.jpg"
    show Storm:
        xalign 0.1 yalign 1.0
    show P:
        xalign 0.9 yalign 1.0
    show blackback:
        alpha 0.3
    with Dissolve(2)

    pause 3.0

    $P.change('emotion', 'neutral')
    $P.change('rightarm', 'palm')
    p "Antes de prosseguirmos, você não me disse seu nome. Como eu disse, você pode me chamar de P."

    $Storm.change('emotion', 'neutral')
    stormq "P? Esse é teu nome mesmo?"

    $P.change('rightarm', 'hip')
    p "Minha família tem algumas tradições peculiares. Meu pai, avô, todos os homens
    compartilham um nome muito complicado."

    $P.change('emotion', 'dominant')
    p "Todo mundo que eu conheço me chama só de \"P\". É mais fácil."

    $P.change('emotion', 'neutral')
    pause 1.0
    $Storm.change('emotion', 'smile')

    "O minotauro não pode deixar de sentir a animação disparando em seu peito.
    Por um momento, ele se permite cair na fantasia de realizar um ritual
    misterioso com este homem inescrutável."

    $Storm.change('emotion', 'proud')
    "Seu peito incha quando ele se lembra de um apelido do qual se orgulhava — e como ele se sentia poderoso
    quando as pessoas o falavam."

    storm "Então... pode me chamar de Tempestade. É como as pessoas me chamavam."

    $P.change('emotion', 'content')
    p "Tempestade? Muito bem. Prazer em conhecê-lo."

    pause 1

    $P.change('emotion', 'neutral')
    p "Agora, antes de começarmos, se importa de me contar um pouco sobre você?"

    $Storm.change('emotion', 'neutral')
    "O potro debandando em seu peito fica imóvel e se esconde na grama alta.
    Seus lábios estão tensos."

    $Storm.change('emotion', 'sad')
    "Tempestade bufa e desvia o olhar."

    "P nem mesmo levanta uma sobrancelha. Ele analisa o rapaz — roupas, sotaque,
    emoções — em busca de um ponto saliente que possa explorar."

    "Algo vulnerável, mas não tão dolorido a ponto de provocar uma reação hostil."

    $P.change('rightarm', 'pointing')
    p "Você é daqui, certo?"

    $P.change('rightarm', 'hip')
    "Uma pergunta inofensiva o suficiente para o jovem temperamental. Melhor que perguntar sobre suas roupas."

    $Storm.change('emotion', 'neutral')
    storm "Sim. Nascido e criado aqui no sertão."

    pause 2.0

    "P permanece quieto. O silêncio gera o desconforto que os incautos costumam preencher."

    $Storm.change('emotion', 'sad')
    "O coração do minotauro deve estar batendo forte, ou talvez ele se sinta pequeno
    e vulnerável contra o pavão. Ele bufa, depois fala."

    $Storm.change('emotion', 'neutral')
    storm "Mas a família de mainha é do norte, perto da praia."

    p "Entendo. É um lugar difícil de viver, não é?"

    $Storm.change('emotion', 'angry')
    storm "Não mais que esse lugar empestado dos infernos."

    pause 2.0

    $Storm.change('emotion', 'neutral')
    storm "Mas é bom pra pescar. A água é fria que só a mulesta, e com vento igual um tornado."

    pause 2.3

    "A voz do pavão sai monótona, como se estivesse respondendo a algo que o
    minotauro revelou sem perceber."

    p "Sim."

    $Storm.change('emotion', 'embarrassed')
    pause 0.5
    show Storm:
        xzoom -1
        ease 1.0 xalign 0.08
        pause 1
        xzoom 1
        ease 1.0 xalign 0.1
    "Um arrepio percorre a espinha do minotauro conforme ele se sente observado por uma dúzia de pares de olhos.
    Ele olha em volta, mas não encontra mais ninguém lá com eles."

    pause 1.0

    $P.change('rightarm', 'pointing')

    p "Você vem de uma família de pescadores?"

    $P.change('rightarm', 'hip')
    "O medo de ser observado afrouxa os lábios do minotauro."

    storm "Mais ou menos. Meu avô por parte de mãe é um."

    pause 0.5
    show Storm:
        xzoom -1
        pause 1
        xzoom 1
    "Ele olha para trás novamente e, nada."

    storm "Meus, hã... Os pais dos meus irmãos são pescadores também."

    show Storm:
        ease 0.8 xalign 0.08

    $P.change('emotion', 'deepthinking')
    "O olhar do pavão fica mais severo."

    p "Ah. Quantos irmãos você tem?"

    storm "Seis, nenhuma irmã. Eu sou o caçula.{w} Mainha não quis ter mais nenhum filho depois de mim."

    $P.change('emotion', 'thinking')
    p "Entendi. Então você é o sétimo..."

    $Storm.change('emotion', 'neutral')
    "Petulância retorna ao minotauro."

    storm "Isso importa pra alguma coisa?"

    $Storm.change('emotion', 'neutral')
    p "Não tenho certeza. Existe uma lenda local...{w} O sétimo filho do sétimo filho
    nasce... especial, digamos assim. O folclore diz que ele vai ser um lobisomem."

    $P.change('emotion', 'neutral')
    p "Alguma possibilidade do seu pai também ter sido um sétimo filho?"

    $Storm.change('emotion', 'sad')
    storm "Não dá pra responder essa pergunta. Nunca conheci ele."

    pause 1.5

    p "Entendo."

    pause 2.0

    storm "Mainha sempre disse que ele era um homem."

    $P.change('emotion', 'deepthinking')
    "As peças do quebra-cabeça flutuam na mente do pavão.{w} Ele fala sem perceber que
    já deseja partir o rapaz em pedaços e observar cada parte de seu passado."

    "A ideia de encontrar o hotel dá lugar ao fascínio da investigação."

    $P.change('emotion', 'thinking')

    p "Talvez. Talvez ele fosse, sim."

    $Storm.change('emotion', 'angry')
    show Storm:
        xzoom 1
        ease 0.5 xalign 0.15

    storm "O que tu quer dizer com isso?"

    $P.change('emotion', 'neutral')

    p "Ele pode ter sido humano, sim, e você pode simplesmente ter nascido um minotauro
    por causa de um evento anormal da natureza. É raro, mas pode acontecer."

    p "Ou ele poderia ser alguém como eu, carregando um amuleto para parecer humano."

    pause 1.5

    $Storm.change('emotion', 'embarrassed')
    $P.change('emotion', 'dominant')
    p "Talvez seu painho esteja te esperando nesse hotel minotauro que eu estou procurando."

    "O pavão espera que o minotauro morda a isca, mas seu rosto continua tão difícil de ler como sempre."


    $P.change('emotion', 'tired')
    $Storm.change('emotion', 'pissed')
    show Storm:
        ease 0.5 xalign 0.2

    storm "Aí dento!"

    storm "Me responde uma pergunta, moço da cidade. Se tivesse {i}outra{/i} desgraça de
    minotauro por aqui, tu não acha que todo mundo ia saber disso?"

    storm "Olha, posso até parecer um tabacudo falando isso, mas pode ser que o teu avô tava falando arisia e
    {i}não tem{/i} nenhum \”hotel minotauro\” ou sei lá."

    $P.change('emotion', 'tired')
    p "Tudo bem, isso significa que você está rejeitando a minha oferta? Vá se foder, então."

    $Storm.change('emotion', 'embarrassed')
    show Storm:
        ease 2.0 xalign 0.1

    pause 2.0

    $P.change('rightarm', 'pointing')
    p "Ué, já morgou? Olha, eu disse que valeria a pena o seu tempo. Você vai
    ser pago independente de qualquer coisa, mesmo que esse hotel nem exista."

    $P.change('rightarm', 'palm')

    p "Você vai pegar a desgraça do seu amuleto hoje e seu dinheiro quando terminarmos.
    Mas agora, vamos ser honestos aqui por um minuto."

    $P.change('rightarm', 'pointing')
    p "Olha, rapaz, supondo por um momento que o seu pai seja alguém como eu você,
    estou fazendo o que ele deveria ter feito há vinte anos."

    p "Então, aqui estão suas opções. Você pode ficar aqui, se comportar, e eu vou te ensinar tudo
    sobre como se passar por um humano. Ou você pode ir embora e voltar a ser um morador de rua."

    $P.change('rightarm', 'hip')
    pause 2.0

    "Um lampejo de clareza atravessa a mente do minotauro conforme a hierarquia do pavão é estabelecida."

    "Ele rastejaria e imploraria?{w} Sim,{w=0.3} sem pensar duas vezes."

    $Storm.change('emotion', 'sad')
    pause 1.0

    storm "Me ensina. Eu quero ser humano."

    $P.change('rightarm', 'pointing')

    $P.change('emotion', 'dominant')

    p "Melhor assim, rapaz."

    $P.change('rightarm', 'palm')

    p "Primeiramente, não podemos {i}virar{/i} humanos. No máximo, podemos {i}nos passar{/i} por um.
    Essa é a primeira coisa, só para você não ficar com expectativas muito altas."

    $Storm.change('emotion', 'neutral')
    storm "Qual a diferença?"

    $P.change('emotion', 'thinking')
    p "Você ainda vai ser, bem, você... mas os outros não vão notar. É exclusivamente uma questão
    de percepção. Você carrega um amuleto que faz todo mundo pensar que você é humano."

    $Storm.change('emotion', 'sad')
    storm "Se eles me tocarem, vão saber?"

    $P.change('emotion', 'content')
    p "Depende. Se o seu amuleto for muito, muito bom, eles não vão encontrar nada de errado.
    Vão sentir você como uma pessoa normal."

    $Storm.change('emotion', 'neutral')
    $P.change('emotion', 'neutral')
    $P.change('rightarm', 'hip')
    p "Mas esse nível de qualidade geralmente é tão caro que você terá que passar uma vida inteira trabalhando
    para pagar por isso. Ou você pode trabalhar como funcionário público, isso te renderia umas coisas legais."

    p "Mas a maioria das pessoas não pode exatamente fazer isso, então, optamos por algo mais
    acessível. Hoje em dia, você pode conseguir um efeito \"dá pro gasto\" com um passaporte."

    $Storm.change('emotion', 'angry')

    storm "Um... um passaporte? Tás viçando é?"

    p "Não, é exatamente o que parece. Você faz um passaporte — tem que ser um
    daqueles passaportes eletrônicos, com um pequeno chip dentro — e eles transformam o chip em um amuleto."

    p "Isto é, contanto que você sempre carregue seu passaporte com você."

    $Storm.change('emotion', 'sad')
    storm "Tu tá de brincadeira né. Esse tempo todo eu podia só... carregar um passaporte?"

    "Toda a humilhação de uma vida — uma aberração na escola, uma desgraça em casa,
    uma abominação nas ruas — tudo isso poderia ter sido evitado.{w} Se apenas ele tivesse um livreto."

    "Não é nada menos que um insulto."

    $P.change('emotion', 'sad')

    p "Eu sinto muito. Não posso imaginar pelo que você passou."

    storm "Não, você não pode{w=0.5}, seu...{nw}"

    $P.change('emotion', 'neutral')
    pause 0.5
    $Storm.change('emotion', 'embarrassed')
    show Storm:
        ease 0.1 xalign 0.097
        ease 0.1 xalign 0.1
        repeat

    "O pavão se prepara para outra explosão, mas o rapaz respira fundo. Cerra os dentes. Chacoalha-se, e..."

    pause 1.0

    $Storm.change('emotion', 'sad')
    show Storm:
        ease 0.1 xalign 0.1
        ease 2.0 yalign 1.4
    "Expira."

    storm "Então, a gente só, hã...{w=0.2} Onde eu consigo um passaporte?
    É só entrar e pedir?"

    $P.change('emotion', 'thinking')

    p "Bem, sim. Em teoria, mas é ilegal para nós andar por aí sem um amuleto em
    primeiro lugar. Você seria preso."

    storm "Então como eu faço pra... Se o passaporte é o amuleto, mas eu não posso {i}conseguir{/i}
    um passaporte sem um amuleto..."

    $P.change('emotion', 'dominant')
    p "Sim, um baita paradoxo, né? Mas não se preocupe, rapaz.
    Vamos consertar isso hoje, aqui mesmo."

    p "Também existem amuletos caseiros. Eles não são tão bons quanto o passaporte,
    mas ei, vão servir."

    $Storm.change('emotion', 'neutral')
    show Storm:
        ease 1.0 yalign 1.0
    storm "Então... Ele é bom quanto? Qual é a desvantagem? Tem que ter uma, eu não sou besta."

    $P.change('emotion', 'neutral')
    p "A desvantagem é que amuletos de baixa qualidade têm efeitos colaterais — os detalhes
    dependem de como foram criados e qual processo foi usado. Na maioria das vezes,
    eles tornam difícil para as pessoas... lembrarem de você."

    $P.change('rightarm', 'palm')
    p "Por outro lado, os passaportes costumam ter esse problema também, mas é bem ruim
    se tratando dos caseiros."

    $Storm.change('emotion', 'embarrassed')
    storm "As pessoas vão simplesmente esquecer que eu existi?"

    p "Não, é mais tipo... Com um amuleto caseiro, as pessoas que te conhecem
    enquanto você está disfarçado vão esquecer que te viram depois de uma ou duas horas mais ou menos."

    p "Isso torna muito difícil manter um emprego, sabe? Ou fazer amigos, namorar..."

    pause 2.0

    $Storm.change('emotion', 'neutral')
    storm "Não."

    $P.change('rightarm', 'hip')
    $P.change('emotion', 'deepthinking')
    p "...Não?"

    $Storm.change('emotion', 'smile')
    $P.change('emotion', 'neutral')
    storm "Isso não é uma coisa ruim. Parece ótimo."

    $Storm.change('emotion', 'sad')
    storm "Me trataram igual merda a minha vida toda. Eu não podia nem ir no mercadinho
    sem as pessoas me olharem como se eu tivesse doente ou algo assim."

    storm "Toda minha vida eu fui lembrado, e eu odeio isso. Eu {i}odeio{/i}."

    storm "Ser esquecido parece a melhor coisa do mundo pra mim.
    Não quero saber o que custa, eu mataria por isso."

    $Storm.change('emotion', 'neutral')
    storm "Bora. Faz o amuleto pra mim...{w=0.3} por favor."

    $P.change('emotion', 'deepthinking')

    p "Bom, então eu vou explicar o processo. Existem muitas formas de se fazer um amuleto."

    $Storm.change('emotion', 'embarrassed')
    p "Na Grécia e Roma antigas, envolveria sacrificar um animal para os deuses
    visando imbuir os ossos com propriedades mágicas."

    p "Os cristãos não gostavam desses rituais pagãos. Em vez disso, eles fizeram
    um sacramento com o qual as cruzes viravam amuletos."

    $Storm.change('emotion', 'neutral')
    p "Há apenas um século, você precisaria de um padre para fazer um amuleto.
    No entanto, os tempos mudaram e agora é tudo um assunto para o estado."

    p "Se você souber quem e o que procurar, pode conseguir um amuleto emitido pelo governo.
    Mas isso geralmente exige que você já tenha um com você, pelo menos para que possa pegar discretamente."

    p "Portanto, cada método pode ser mais difícil ou mais fácil de realizar, dependendo das nossas circunstâncias.
    Evidentemente, nós não temos gado para sacrificar e duvido que haja um padre por perto que
    conheça o sacramento."

    $P.change('emotion', 'thinking')
    $P.change('rightarm', 'thinking')
    p "Mas {i}existe{/i} o tradicional jeitinho brasileiro de se fazer isso. Requer muito
    pouco se tratando de materiais, e já tenho o que precisamos."

    p "Vai levar um tempo e os amuletos que dá para produzir são bastante específicos.
    Mas isso não deve ser um problema. Você também vai ter que seguir minhas instruções."

    $Storm.change('emotion', 'proud')
    storm "Só diz o que eu preciso fazer. Pode ser o que for, eu faço."

    $P.change('emotion', 'dominant')
    $P.change('rightarm', 'pointing')
    p "Ótimo. É simples, sério. Nós vamos acender uma fogueira e cada um conta uma história.
    Vamos ter que ficar amarrando uma na outra para fazer o seu amuleto ter um poder duradouro."

    p "Depois que terminarmos nossas histórias, eu vou te dar uma pena e você vai jogar
    ela na fogueira junto com aquilo que quiser para o seu amuleto."

    $P.change('rightarm', 'palm')
    p "Esse é o jeitinho brasileiro. Nós contamos histórias, entrelaçamos elas em um contrato."

    p "Você vai fazer um juramento com a própria humanidade, construída como uma extensão da minha própria, que, hã..."

    pause 1.5

    $P.change('emotion', 'thinking')
    $P.change('rightarm', 'hip')
    p "Enfim. Isso já é preâmbulo suficiente, rapaz. Você já está pronto e
    de boa com isso para que possamos começar?"

    storm "Eu seria um abestalhado se não tivesse."

    $P.change('emotion', 'dominant')

    p "Fico feliz em ouvir isso. Então..."

    $P.change('emotion', 'dominant')
    $P.change('rightarm', 'palm')
    pause 1

    show P:
        ease 2.0 xalign 0.7
        ease 0.5 yalign 1.1
        ease 0.5 yalign 1.0
    show Storm:
        ease 2.0 xalign 0.3
        ease 0.5 yalign 1.1
        ease 0.5 yalign 1.0

    pause 2

    p "Você tem um aperto de mão forte, rapaz."
    $P.change('rightarm', 'hip')
    show P:
        ease 2.0 xalign 0.8
    show Storm:
        ease 2.0 xalign 0.2

    storm "Você também… pra um moço da cidade."

    $P.change('emotion', 'dominant')
    $P.change('rightarm', 'palm')

    p "Não me provoque; você não tem ideia do que esse moço da cidade é capaz."

    $Storm.change('emotion', 'happy')
    storm "Tá… então,{w=0.3} belo aperto pra um coroa."

    $P.change('rightarm', 'pointing')

    p "Você é um merdinha mesmo, não é?"

    $Storm.change('emotion', 'proud')
    storm "É. Se acostuma aí, eu sei que tu precisa de mim pra achar o teu hotel."

    $P.change('emotion', 'neutral')
    $P.change('rightarm', 'palm')
    p "Ok, vou deixar você ganhar essa. Agora, podemos começar com o amuleto?"

    $P.change('rightarm', 'hip')
    storm "Achei que tu nunca ia perguntar."

    scene blackback
    with Dissolve(1)

    image bonfire = "images/bg/crossroads_fire.png"

    $Storm.change('emotion', 'smile')
    scene image "images/bg/bg crossroads.jpg"
    show Storm:
        xalign 0.1 yalign 1.0
    show P:
        xalign 0.9 yalign 1.0
    show bonfire
    show blackback behind bonfire:
        alpha 0.4
    with Dissolve (2)

    pause 2.0

    "O pavão sabe que um juramento é algo tênue, dado poder pela relação
    de uma coisa com outra."

    "Um pensamento completo para sua cláusula dependente. Um sujeito para um objeto. Um pássaro para um minotauro."

    "Que conversa fiada e inconsequente ele pode revelar para se conectar com esse Tempestade,
    esse garoto que guarda o segredo de seu desejo mais profundo a sete chaves?"

    "Um súbito movimento autoritário de uma asa é suficiente para chamar a atenção do touro,
    para fazer as rodas na cabeça da dupla chiarem até parar."

    pause 2.0

    p "Já que você vai trabalhar para mim, vou começar com a história que você precisa saber."

    $P.change('emotion', 'thinking')
    $P.change('rightarm', 'thinking')
    p "Por{w=0.3} onde{w=0.3} começar...{w=1} Você já viu alguma coisa sobrenatural por aqui, Tempestade?"

    $Storm.change("emotion", "neutral")
    show Storm:
        xzoom -1

    "O minotauro desvia o olhar — para as estradas além da vista.{w}
    Isto diz ao pavão o que ele realmente deseja saber."
    show Storm:
        xzoom 1
    storm "Muita coisa estranha acontece por aqui, mas eu não sei se é mágica ou sei lá o quê."

    $P.change("emotion", "tired")
    $Storm.change("emotion", "embarrassed")
    $P.change('rightarm', 'hip')
    "O pavão revira os olhos. O rapaz fica tenso, como se andasse em uma corda bamba e
    debatesse para se equilibrar."

    "Naquele momento, ele entende melhor do que nunca o que é estar sob uma hierarquia."

    "Ele sabe que deve tomar cuidado para não ofender seu novo benfeitor, ou correr o risco de perder sua
    chance de tornar-se humano. Quaisquer que sejam seus sentimentos, ele deve concordar com qualquer coisa que o pavão dizer."

    $Storm.change("emotion", "neutral")
    p "Sim, sim. Esse lugar deveria ser o último buraco onde alguém encontraria magia
    nesse lado do país."

    p "Rádio, televisão, a Internet — onde quer que eles vão, mais fraca a magia se torna.
    Não sabemos bem por quê, mas é o que é."

    p "E esse lugar, o sertão, em virtude do grande{w=0.2} cu do mundo{w=0.2}
    que é, manteve-se livre de todo tipo tipo de progresso e {w=0.2}civilização básica."

    $P.change("emotion", "neutral")
    p "Ah, desculpa. Espero não ter te ofendido por..."

    $Storm.change("emotion", "angry")

    storm "Nah, eu odeio isso aqui. Sempre me trataram igual merda. Não tem emprego
    a não ser minerar sal, e eles não me aceitam nem pra isso..."

    $Storm.change("emotion", "neutral")
    storm "Nada pra fazer, nada pra ver, nada que valha a pena salvar nesse buraco."

    pause 1.5

    $P.change("emotion", "dominant")
    "O pavão sorri pela curvatura natural de seu bico. A tácita admissão de Tempestade
    agita a brisa em seus pulmões até que emerge como um bufo orgulhoso e ondulante."

    $Storm.change("emotion", "smile")
    p "Fico feliz que concordamos um com o outro."

    $Storm.change("emotion", "neutral")
    p "Bem, com isso em mente, nossa história começa...{w=0.2} cerca de oitenta anos atrás."

    p "Suponho que tenha sido uma noite muito parecida com essa quando alguém muito parecido comigo — meu
    avô — fugiu desse lugar."

    $P.change("emotion", "neutral")
    p "Ele viveu a maior parte da vida dele aqui, e... Não conheço os detalhes, mas as
    coisas deram errado e ele se viu tendo que correr para salvar sua vida."

    $P.change("rightarm", "palm")
    p "Ele correu o mais longe que pôde e, depois, passou três dias no mato,
    se escondendo durante o dia e caminhando em direção à costa durante a noite."

    p "Na quarta noite, ele encontrou um viajante que lhe deu comida e água."

    $P.change("rightarm", "hip")
    p "Cara legal, eu imagino. Vê alguém fugindo e não faz perguntas,
    simplesmente oferece ajuda. Devia saber que era melhor não enfiar o nariz."

    p "O andarilho, porém, sabia como ler as estrelas e deu ao meu avô algumas palavras
    de conselho — vá para o noroeste, estará seguro lá."

    p "Mas ele não seguiu o conselho. Ele ouviu cavalos em disparada naquela
    direção, então ele foi para o leste, e lá ele encontrou..."

    pause 1.5

    $Storm.change("emotion", "embarrassed")
    $P.change("emotion", "thinking")
    p "Uma estação de ônibus."

    $P.change("rightarm", "palm")
    p "Era madrugada e não havia ninguém lá. Ele verificou o cronograma
    — talvez um ônibus viesse, o levasse para o noroeste."

    $Storm.change("emotion", "neutral")
    p "Nem cinco minutos depois, um apareceu."

    p "O motorista era uma criatura disfarçada de humano. Ele não falava português e suas
    roupas tinham letras estranhas."

    p "Meu avô embarcou, eles partiram para o leste e ele foi levado para um lugar estranho que chamou
    de \"hotel minotauro.\""

    $P.change("rightarm", "hip")
    p "Ele me disse que foi criado antes da Torre de Babel ser destruída, que um
    fragmento de sua antiga magia humana sobreviveu lá, fazendo com que todos pudessem se entender,
    independentemente da língua."

    $P.change("emotion", "neutral")
    p "O lugar era governado por um minotauro que tinha o poder de fazer diamantes aparecerem
    na palma da mão."

    p "Ninguém passava fome lá. Até mesmo a pessoa mais miserável poderia encontrar uma casa e um emprego."

    pause 2.0

    $P.change("emotion", "tired")

    p "Mas, como você pode imaginar, algo aconteceu."

    p "Meu avô voltou para casa todo bagunçado um dia, e então partiu para encontrar aquele hotel de novo.{w}
    Mas ele nunca encontrou."

    $P.change("emotion", "sad")
    p "Ele passou anos procurando. Voltou ao trabalho, conheceu sua esposa, teve seu filho, mas nunca parou
    de sair, às vezes por dias, para tentar encontrar o lugar."

    p "Meu pai achava que ele estava louco, que esse hotel nunca existiu. Minha avó ainda está viva,
    e ainda se ressente de todas as noites que o vovô gastou na busca."

    $Storm.change("emotion", "sad")
    p "Quanto ao ele, já se passaram algumas semanas desde que ele faleceu."

    $P.change("rightarm", "palm")
    p "Eu gostaria de dizer que ele me contou a história outra vez em seu leito de morte e me pediu para encontrar.
    Aquele hotel. Não seria ótimo?"

    $P.change("emotion", "neutral")
    p "Mas isso seria uma mentira — uma doce, mas uma mentira, de qualquer forma."

    $P.change("rightarm", "hip")
    p "Eu não estava lá quando ele morreu, e naquela época a mente dele já tinha sumido há muito tempo.
    Gosto de pensar que ele sentiu um pouco de liberdade quando chegou a hora dele."

    p "Mas suponho que ninguém pode se libertar sem passar um fardo para outro.
    Agora que ele se foi, aquele velho desejo de viajar me dominou."

    $Storm.change("emotion", "neutral")
    $P.change("emotion", "angry")
    p "Eu quero encontrar aquele hotel. Limpar o nome do meu avô, provar que ele estava certo o tempo todo."

    "Uma aparência resoluta passa através das feições da ave. Se havia vulnerabilidade em seu
    discurso, foi dobrada três vezes e escondida no canto de sua mente."

    "De onde ele está, Tempestade não pode deixar de notar como tudo sobre o pavão é
    organizado e apropriado."

    $P.change("emotion", "neutral")
    p "Além disso, tem uma coisa lá que é minha. Minha herança, você poderia dizer."

    p "Tenho sonhado com esse lugar desde que o vovô faleceu.
    Tenho certeza de que tudo o que ele disse era verdade."

    pause 2.0

    $P.change("rightarm", "palm")
    p "Agora é sua vez. Me conte uma história."

    $Storm.change("emotion", "embarrassed")
    "Os olhos do minotauro ficam finos como facas."

    $P.change("rightarm", "hip")
    storm "Eu tenho que fazer isso mesmo?"

    $P.change("emotion", "content")
    p "Sem história, sem amuleto, sem humanidade."

    storm "E se eu inventar? Tem que ser de verdade?"

    $P.change("rightarm", "palm")
    $P.change("emotion", "tired")
    p "Claro, vá em frente e perca nosso tempo.{w} Mas eu não vou fazer isso de novo."

    pause 1
    $P.change("rightarm", "hip")
    $Storm.change("emotion", "sad")

    pause 1
    show Storm:
        xzoom -1
    pause 1
    "O minotauro desvia o olhar, desta vez em direção à lagoa e seu buraco."

    "Ele sabe que não há escolha. Mas ele não consegue falar — não enquanto os beija-flores
    bicam sua nuca, levantando cada fio de pelo."

    "Ele coça o pescoço com as duas mãos — cavando para deixar a pele em carne viva.
    Mas o pavão ignora. Sua paciência está se esgotando."

    $P.change("rightarm", "pointing")
    p "Você realmente vai me forçar a te interrogar, rapaz?"

    show Storm:
        xzoom 1
        ease 2.0 yalign 1.3
    "O minotauro balança a cabeça, tentando afastar todas as criaturinhas que voam
    ao seu redor. Um grave muu escapa de sua garganta."

    p "Quantos anos você tem?"

    pause 1.0

    storm "21."

    pause 2.0

    $P.change("emotion", "deepthinking")
    $P.change("rightarm", "hip")

    pause 2.0

    storm "Só... Me dá um tempo, eu tô pensando, ok?"

    "O pavão conta os segundos enquanto o minotauro perde a noção do tempo.
    Ele continua se coçando até que seja lá o que lhe estava afetando desaparece."

    "Ele respira fundo, estremece e fala."

    show Storm:
        ease 1.0 yalign 1.0

    storm "Mainha disse que painho era um homem.{w}
    Eu não cheguei a conhecer ele, mas ela sempre, sempre deixou isso claro. Então não fique com a ideia errada."

    $P.change("emotion", "neutral")

    p "Mais uma vez, de jeito nenhum era um touro — isso não faz sentido — e se ele fosse alguém como eu,
    teria te arranjado um amuleto.{w} A não ser que algo tenha acontecido com ele, ou
    ele não sabe que você existe."

    $Storm.change("emotion", "neutral")

    "O minotauro não gosta da nitidez na voz do pássado. Estridente e
    oscilando no limiar da raiva."

    "Mas ele dá o primeiro suspiro de verdadeiro alívio em toda sua vida, sabendo que há
    alguém neste mundo que não pensa que ele é produto de bestialidade."

    "Talvez haja umidade nos olhos do minotauro, brilhando com o fogo.
    Mas o pavão de olhos afiados confunde isto com outra coisa."

    $P.change("emotion", "deepthinking")

    p "Desculpe por interromper. Continue."

    storm "Ah, sim...{w=0.2} o que eu tava dizendo?"

    $P.change("emotion", "neutral")
    $P.change("rightarm", "pointing")

    p "Você não conheceu seu pai. Sua mãe te criou, eu presumo."

    $P.change("rightarm", "hip")
    storm "Sim, criou eu e os meus seis irmãos.{w} Eu sou o caçula e, é...
    ela não podia ter mais depois que eu, hã, saí."

    $Storm.change("emotion", "sad")

    pause 2.0
    "\"Arruinou,\" foi o que ela disse.{w} \"Você me arruinou.\""

    "Nem uma gota de raiva em sua voz, embora seu rosto estivesse coberto por duas
    décadas de humilhação."

    "Ela soprou fumaça no rosto dele, apagou a guimba do cigarro na mesa de jantar
    de plástico e depois jogou na fruteira vazia."

    "Apenas afirmando um fato simples. Inescapável."

    "Ele não deveria ter nascido."

    storm "Eu nunca me dei com ela, nem com qualquer um dos meus irmãos, aliás.
    Eles botavam a culpa em mim por coisas que eu não tinha feito."

    "Tudo começou de forma simples — culpando-o por quebrar o único copo de vidro deles.
    Aquele laranja que mainha costumava tomar café. Ele tinha quatro anos."

    "Como um vício, criou raízes e cresceu. Se alguma coisa sumia da geladeira,
    tinha sido ele. Ou se alguma desgraça acontecesse, como se sua existência trouxesse azar.
    Eles apontariam para seus chifres e se recusariam a dizer seu nome."

    "Apenas \"ele\" — sem nome. Mais um conceito do que uma pessoa. Olhos bem abertos e mente
    silenciosa, entorpecida, enquanto continuava acontecendo."

    "Tornou-se a droga deles. A razão pela qual eles não conseguiram empregos e tiveram que viver da previdência."

    "Estar com raiva dele era o suficiente para justificar bater em suas namoradas. Ou abandonar
    suas crianças e fugir da cidade."

    "\"Ele.\" Seu nome era tão não usado que poderia muito bem não existir."

    "Tempestade era um título melhor. E assim o rapaz reúne as memórias, as dores, a mente em si mesma."

    storm "Todo mundo pensava besteira de mainha. Sobre o que ela devia ter feito pra ter um filho igual a mim."

    storm "Até olhar pra mim deixava ela com raiva."

    storm "A escola também me tratou que nem merda.{w} Então eu desisti e fugi."

    storm "Eu achei que podia ganhar a vida lá na cidade. Ou em uma fazenda."

    "Não durou muito. O dono da fazenda podia apreciar sua força e dedicação,
    mas os fazendeiros não gostavam muito de dividir os aposentos com ele."

    "Melhor largar o trabalho que ser massacrado no meio da noite, ele pensou."

    storm "Mas eu voltei, não tive sorte. As pessoas aqui pelo menos não entram em pânico quando me veem."

    "Sem juízo demais pra se importarem."

    storm "Tentei voltar pra casa de mainha. Ela me deixou entrar, mas depois me acordou de noite pra gritar."

    "Faltava o juízo pra ter alguma consciência dos próprios atos."

    storm "Então eu tentei ir embora de novo, também não funcionou."

    "Fui mais longe, mas a polícia começou a ficar curiosa sobre o morador de rua chifrudo
    debaixo da ponte."

    storm "É por isso que eu moro aqui perto da lagoa."

    storm "É seguro. Ninguém me incomoda de noite. Consigo fazer uns bicos aqui e ali pra comprar comida."

    play music "music/CrossingTheAstralBridge.ogg" fadein 1.0 fadeout 1.0

    pause 1.5
    $Storm.change("emotion", "neutral")
    pause 1
    #At first show Storm looking a little bitter about having to open up — then after a small pause, the pleading desperation for the charm returns
    $Storm.change("emotion", "sad")
    pause 1
    storm "Essa é minha história.{w} É o suficiente pro seu ritual?"

    $Storm.change("emotion", "embarrassed")
    $P.change("emotion", "deepthinking")

    show blackback:
        ease 1.0 alpha 0.8
    show blackback:
        ease 0.6 alpha 0.6
        ease 0.5 alpha 0.8
        repeat


    #P and Storm both feel migraines, if possible show something on-screen to indicate it

    "Um arrepio sobe pelas costas do pavão. O ar ao redor deles fica mais denso."

    "Uma enxaqueca desliza sobre sua cabeça e penetra em seu olho esquerdo.
    Suas pernas ficam dormentes e seu cérebro se pega esquecendo as palavras."

    "O minotauro, enquanto isso, desvia o olhar da fogueira. A luz queima seus olhos."

    "Os beija-flores bicam seu pescoço novamente enquanto o canto das cigarras toma conta de sua audição."

    "Ele está prestes a pedir ajuda quando, em um piscar de olhos, tudo acaba."

    show blackback:
        ease 3.0 alpha 0.4
    pause 4.0

    $Storm.change("emotion", "neutral")
    $P.change("emotion", "neutral")
    p "Sim, é o suficiente.{w} Vamos ver agora, uma pena... Essa está prestes a cair."

    show P:
        ease 1.0 xalign 0.7
    pause 1.0
    show blackback:
        ease 1.0 alpha 0.7
    show P:
        ease 1.0 xalign 0.9

    p "Vou fazer o juramento agora, você só precisa aceitar."

    show Storm:
        ease 0.5 xalign 0.0
    show P:
        xalign 1.23

    $Storm.change("emotion", "embarrassed")
    $P.change("tail", "raised")
    $P.change("emotion", "content")
    "O pavão fecha os olhos. Suas penas se eriçam como se um arrepio percorresse sua espinha."


    p "És o sal da terra, eterno e implacável.
    \nPor que, então, não deverias ser nosso irmão?"

    p "És a lua da noite, uma cidade soterrada pelas cinzas.
    \nUm segredo escrito em seu peito não pode ser visto.
    \nÉs o sal da terra, e o que é a humanidade sem ti?"

    p "Oculto, não perderás teu valor.
    \nNão serás pisoteado.
    \nNão morrerás novamente."

    p "Abençoado és tu quando te tornas nosso irmão.
    \nPelo presente da humanidade ninguém te perseguirá,
    \nnem te acusará de atos desagradáveis."

    p "És a luz do mundo,
    \nescondido da vista e brilhando ainda assim.
    \nNão verão tua origem, mas contemplarão tua oferenda."

    p "Não serás posto de lado, e a glória seguirá teus passos.
    \n\nPelo sal e pelo mar, pegue meu fio de vida,
    \nvamos fazer um juramento de parentesco."

    p "Que a humanidade receba o portador desta promessa de proteção em seu seio,
    \nbem como hoje à noite trocamos nossos fios de longa duração."

    p "Deves festejar e viver como um dos nossos, portador de parentesco,
    \ne enquanto carregares a prova deste juramento, ninguém verá teu mito."

    p "Pelo sal e pelo mar, pelas terras ocidentais, desamarre meu feixe de humanidade
    \ne estique seu fio até este diante de mim, para que ele possa desfrutar de liberdade não menor que a minha."

    p "Portador da humanidade, fazes este honesto juramento à raça humana
    \nenquanto funcionarem teus pulmões?"

    pause 2.0

    $Storm.change("emotion", "sad")
    "\"Isso deve ser um sonho,\" pensa o minotauro. \"Ou um demônio agindo.\""

    "E qual poderia ser a pegadinha inevitável? Um presente como este não vem
    sem um preço angustiante."

label build4_safe_end:

    hide bonfire
    with Dissolve(1)

    show blackback:
        ease 1.0 alpha 1.0


    pause 1.0

    $Storm.change("emotion", "neutral")
    "Mas nada disso importa. As consequências que se danem, ele aceitará."

    pause 1.0

    $Storm.change("emotion", "proud")
    storm "Sim."

    $P.change("emotion", "neutral")
    p "Jogue a pena e seu objeto na chama. Minha oferenda vai queimar, então a sua não deve."

    $Storm.change("emotion", "neutral")
    #show Storm:
    #    ease 1.0 xalign 0.3
    #    ease 1.0 xalign 0.1
    "O híbrido remove seu alargador, coloca a pena através dele e os joga no fogo."

    #Raise the tension — maybe increase the volume of the fire crackling, add noise, until it dies suddenly and fades to black.

    pause 2.0
    hide bonfire
    with Dissolve(1)

    #show blackback:
    #    ease 1.0 alpha 0.4
    pause 2.0
    #show P:
    #    xalign 0.9
    $P.change("tail", "low")

    #show Storm:
    #    ease 1.0 xalign 0.3 yalign 1.6
    #    ease 1.0 xalign 0.1 yalign 1.0
    $P.change("rightarm", "palm")
    p "Aqui. Experimente."

    pause 2.0

    $Storm.change("emotion", "proud")
    $P.change("emotion", "content")
    $P.change("rightarm", "pointing")
    p "Bem-vindo à sua primeira noite como humano, Tempestade."

    stop music fadeout 3
    scene bg black
    with Dissolve(3)








#end of build

    jump build05

    #play music "music/PersonalElegy.ogg" fadein 1.0 fadeout 1.0

    pause 3.0
    $Cobalts.change ("clothes","waiter")
    show cobalt_left:
        xzoom 1 xalign 0.5 yalign 1.0 zoom 1
    with Dissolve(3)

    gruggy "...E é isso!"

    gruggy "Essa foi a Atualização 0.4 de Hotel Minotauro. Espero que tenha gostado."

    gruggy "Em primeiro lugar, nos desculpamos pelo longo hiato entre as atualizações.
    Depois de terminar a 0.3, demos uma pausa antes de começar a trabalhar na 0.4 e definir
    tudo o que queríamos fazer para a atualização."

    gruggy "Sem falar que, se você vem acompanhando o desenvolvimento desta VN,
    mordemos um pouco mais do que conseguíamos mastigar. Fizemos um progresso considerável — tínhamos
    cerca de 75k palavras na atualização, mas ainda tínhamos um longo caminho a percorrer..."

    gruggy "...e mantivemos as pessoas esperando por quase meio ano sem
    atualizações, em uma época onde elas realmente poderiam aproveitar um pouco de conteúdo que melhore o humor."

    gruggy "Portanto, decidimos colocar esta atualização como um compromisso. Esperamos que o
    Capítulo 13 e a introdução à seção do Sertão no jogo
    tenham entregado uma quantidade satisfatória de conteúdo."

    gruggy "Desta vez, não tiraremos nosso tempo de folga habitual após o lançamento.
    Nossa escrita está seguindo em um ritmo muito bom e saudável."

    gruggy "Se o conteúdo desta vez pareceu um pouco curto, sentimos muito.
    Se serve de consolo, teve que ser mais curto aqui para que o próximo conteúdo seja
    o melhor possível."

    gruggy "Este capítulo ainda tem um pouco de rejogabilidade — Astério visita diferentes
    sites com base em sua recomendação e os cobaltos gostam de Kota ou Luke
    dependendo de quem está administrando o salão."

    gruggy "E, é claro, as escolhas sobre como você trata o Astério. Então, como sempre, recomendamos
    tentar diferentes salvamentos."

    pause 2.0

    gruggy "Como de costume, aqui está sua classificação atual!"

    call screen RankBar(global_affection)

    gruggy "Deve ter subido, considerando que você melhorou bastante sua relação
    com Astério nesta atualização."

    gruggy "Como de costume, gostaríamos de perguntar a você: O que você está achando de Hotel Minotauro até agora?"

    menu:
        "O que você está achando de Hotel Minotauro até agora?"
        "O jogo é excelente.":

            gruggy "Ótimo, ficamos felizes em ouvir isso.{w=0.2} É o que queremos,
            criar uma experiência bastante notável."

            gruggy "Se você quer nos ajudar a continuar nesse caminho e está disposto
            a nos dar dois ou três minutos do seu tempo, há duas coisas que você pode fazer para nos ajudar."

            gruggy "Primeiro, ajuda imensamente quando as pessoas avaliam nosso jogo no Itch.io.{w=0.2}
            Cada avaliação de 5 estrelas que obtemos faz com que Hotel Minotauro apareça com mais frequência para mais pessoas."

            gruggy "Também nos mostra o quanto as pessoas estão gostando do nosso jogo.{w=0.2}
            Quer dizer, a vida não é fácil, não é?{w=0.2} Queríamos fazer um jogo
            que fizesse as pessoas se sentirem bem."

            gruggy "Então, ver essa confirmação significa muito para nós.{w=0.2}
            Significa que estamos realizando exatamente o que nos propusemos a fazer."

            gruggy "Além disso, muito do sucesso que encontramos se deve às pessoas que separaram
            um tempo para avaliar nosso jogo.{w=0.2} Não posso superestimar o quanto
            isso ajuda quando se trata de atrair mais jogadores."

            gruggy "Deixar uma classificação leva apenas alguns segundos, devo adicionar."

            if permaSFW:
                gruggy "{a=https://minoh.itch.io/minotaur-hotel-sfw/rate?source=game}Você pode clicar aqui
                para avaliar o Hotel Minotauro: Modo SFW no Itch.{/a} Escrever uma resenha também ajuda, mas não é necessário."
            else:
                gruggy "{a=https://minoh.itch.io/minotaur-hotel/rate?source=game}Você pode clicar aqui para
                avaliar o Hotel Minotauro no Itch.{/a} Escrever uma resenha também ajuda, mas não é necessário."

                gruggy "{a=https://minoh.itch.io/minotaur-hotel-sfw/rate?source=game}E se você estiver disposto
                a nos dar alguma ajuda extra, pode dar uma boa avalização a Hotel Minotauro: Modo SFW também.{/a}"

            gruggy "Se você já escreveu uma resenha...{w=0.2} Muito obrigado."

            gruggy "Se ainda tiver mais um pouco de tempo, também pode preencher nossa pesquisa anônima."

            gruggy "Cada uma das pesquisas que fizemos nos deram informações valiosas sobre como
            melhorar o jogo, e queremos continuar verificando com vocês como a experiência está indo."

            gruggy "Não deve levar mais que dois minutos do seu tempo...{w=0.2}
            São só algumas perguntas de múltipla escolha."

            gruggy "{a=https://forms.gle/CEzQ3LaHJnDeA75U8}Você pode acessar a pesquisa clicando aqui.{/a}"

        "É muito bom.":

            gruggy "Fico feliz em ouvir isso! Se você tiver alguma sugestão sobre como melhorá-lo,
            gostaríamos de ouvir."

            gruggy "Temos uma pesquisa para isso e tudo."

            gruggy "Cada uma das pesquisas que fizemos nos deram informações valiosas sobre como
            melhorar o jogo, e queremos continuar verificando com vocês como a experiência está indo."

            gruggy "Não deve levar mais que dois minutos do seu tempo...{w=0.2}
            São só algumas perguntas de múltipla escolha."

            gruggy "{a=https://forms.gle/CEzQ3LaHJnDeA75U8}Você pode acessar a pesquisa clicando aqui.{/a}"

        "É ok, meio razoável.":
            gruggy "Entendo, entendo. Nesse caso, você teria um ou dois minutos para nos dizer como podemos
            melhorá-lo?"

            gruggy "Sempre fazemos uma pesquisa para colher informações, desta vez não é diferente."

            gruggy "Cada uma das pesquisas que fizemos nos deram informações valiosas sobre como
            melhorar o jogo, e queremos continuar verificando com vocês como a experiência está indo."

            gruggy "Não deve levar mais que dois minutos do seu tempo...{w=0.2}
            São só algumas perguntas de múltipla escolha."

            gruggy "{a=https://forms.gle/CEzQ3LaHJnDeA75U8}Você pode acessar a pesquisa clicando aqui.{/a}"

        "Desculpa, é meio ruim.":
            gruggy "Ah, sinto muito ouvir isso."

            gruggy "Se quiser nos dizer o porquê, adoraríamos ouvir. Temos uma pesquisa exatamente para isso, para descobrir como melhorar o jogo."

            gruggy "{a=https://forms.gle/CEzQ3LaHJnDeA75U8}Se você tiver dois ou três minutos, pode preenchê-la aqui.{/a}"

        "Eu realmente não gostei nem um pouco.":
            gruggy "Ah, sinto muito ouvir isso."

            gruggy "Bem, você seguiu todo o caminho até aqui, não é? Se quiser nos dizer o porquê,
            adoraríamos ouvir. Temos uma pesquisa exatamente para isso,
            descobrir como melhorar o jogo."

            gruggy "{a=https://forms.gle/CEzQ3LaHJnDeA75U8}Se você tiver dois ou três minutos,
            pode preenchê-la aqui.{/a}"

    gruggy "Também criamos um tópico para as pessoas discutirem o jogo. É o melhor lugar para
    ir se você quiser entrar em detalhes sobre como devemos melhorar.
    {a=https://itch.io/t/1069812/build-04-general-discussion}Aqui está.{/a}"

    gruggy "{a=https://itch.io/t/681416/nsfw-general-art-fan-content-thread}Temos um lugar para
    as pessoas postarem fan art, também.{/a}"

    gruggy "Agora, para concluir..."

    gruggy "Muito obrigado por jogar. E, sobre quando a próxima atualização vai sair..."

    gruggy "Muito do trabalho para a 0.5 já está feito! Ainda precisaremos de alguns meses,
    mas achamos que vai valer muito a pena quando finalmente for lançada."

    gruggy "Como de costume, sugerimos que você rejogue o jogo.
    Lançamos um passo a passo em nossa página do itch para o conteúdo da 0.3 há algum tempo, para dar
    sugestões sobre coisas que você pode ter perdido."

    gruggy "Você agora será levado de volta a um local seguro para salvar o jogo para a próxima atualização.
    Até lá, tchauzin!"

    jump build4_safe_end
