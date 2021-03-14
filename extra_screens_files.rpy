init python:
    def resetFileType(fType, newType, fVar):
        fType = newType
        fVar = 'none'

screen mobileFilesMenu():
    $PlatAlign = 0.25 if renpy.variant("android") else 0.2
    $PlatAlign2 = 25 if renpy.variant("android") else 0
    default FileType = 'none'
    default Contract = 'none'
    default Profile = 'none'
    default Memento = 'none'
    default Artifact = 'none'
    default Tech = 'none'
    #source files
    if main_menu:
        default showContracts = persistent.main_menu_files_contract
        default showTechs = persistent.main_menu_files_tech
        default showMementos = persistent.main_menu_files_memento
        default showArtifacts = persistent.main_menu_files_artifact
        default showProfiles = persistent.main_menu_files_profile
        default contractsList = persistent.persistent_files['Contract']
        default techsList = persistent.persistent_files['Tech']
        default mementosList = sort_file_list_by_key(persistent.persistent_files['Memento'], preset_memento_id_key)
        default artifactsList = persistent.persistent_files['Artifact']
        default profilesList = persistent.persistent_files['Profile']
    else:
        default showContracts = UI_permissions['file_contracts']
        default showTechs = UI_permissions['file_tech']
        default showMementos = UI_permissions['file_mementos']
        default showArtifacts = UI_permissions['file_artifacts']
        default showProfiles = UI_permissions['file_profile']
        default contractsList = inventory.files.get_files('contract')
        default techsList = inventory.files.get_files('tech')
        default mementosList = sort_file_list_by_key(inventory.files.get_files('memento'), preset_memento_id_key)
        default artifactsList = inventory.files.get_files('artifact')
        default profilesList = inventory.files.get_files('profile')

    tag menu
    #display BG
    add "images/backtitle.png"
    use navigation
    #add scrolls
    add "scrollsMobileTeams"

    if not renpy.variant("android"):
        vbox xalign 0.5 ypos 0 yminimum ButtonBarHeight:
            text "{size=+10}Files{/size}" yalign 0.5

    hbox spacing 50 yalign PlatAlign xalign 0.5:
        if showContracts:
            if FileType == 'Contracts':
                image "gui/filesIcons/contracts_hover.png"
            else:
                imagebutton auto "gui/filesIcons/contracts_%s.png":
                    action SetLocalVariable("FileType", "Contracts")
        else:
            image "gui/filesIcons/contracts_blue.png"
        if showTechs:
            if FileType == 'Techs':
                image "gui/filesIcons/techs_hover.png"
            else:
                imagebutton auto "gui/filesIcons/techs_%s.png":
                    action SetLocalVariable("FileType", "Techs")
        else:
            image "gui/filesIcons/techs_blue.png"
        if showMementos:
            if FileType == 'Mementos':
                image "gui/filesIcons/mementos_hover.png"
            else:
                imagebutton auto "gui/filesIcons/mementos_%s.png":
                    action SetLocalVariable("FileType", "Mementos")
        else:
            image "gui/filesIcons/mementos_blue.png"
        if showArtifacts:
            if FileType == 'Artifacts':
                image "gui/filesIcons/artifacts_hover.png"
            else:
                imagebutton auto "gui/filesIcons/artifacts_%s.png":
                    action SetLocalVariable("FileType", "Artifacts")
        else:
            image "gui/filesIcons/artifacts_blue.png"
        if showProfiles:
            if FileType == 'Profiles':
                image "gui/filesIcons/profiles_hover.png"
            else:
                imagebutton auto "gui/filesIcons/profiles_%s.png":
                    action SetLocalVariable("FileType", "Profiles")
        else:
            image "gui/filesIcons/profiles_blue.png"


    if FileType != 'none' and current_file_type_value(FileType, Contract, Tech, Profile, Memento, Artifact) != 'none':
        side "c r":
            area (360, 220+PlatAlign2, 870, 420)
            viewport id "ct":
                draggable True
                mousewheel True
                if FileType == 'Contracts':
                    if Contract == "AsterionSentence":
                        vbox spacing 10:
                            text "{i}{size=+2}Sentença de Asterion" xalign 0.5
                            text ""
                            text "{i}Por meio deste, os deuses do Olimpo sentenciam o Prisioneiro Astério à danação eterna por sua mansidão e covardia em face à adversidade."
                            text "{i}Com esta sentença, sua prisão é criada, um Labirinto nascido do icor dos deuses."
                            text "{i}O Labirinto deve acolher mortais perdidos sem nenhum lugar para ir. Entre eles, um Carcereiro será escolhido para comandar e reescrever o domínio."
                            text "{i}A missão do Carcereiro e do Labirinto é garantir a tortura eterna do Prisioneiro."
                            text "{i}O Carcereiro gozará de poder e liberdade para reescrever o Labirinto da forma que melhor enaltecer seu ponto de vista."
                            text "{i}Astério de Creta, filho adotivo do Rei Minos, e cada gota de seu sangue blasfemo é, por meio deste, condenado ao Labirinto."
                            text "{i}Por meio deste decreto, a vontade dos deuses é realizada."
                    elif Contract == "Servitude":
                        vbox spacing 10:
                            text "{i}{size=+2}Juramento de Servidão de Astério" xalign 0.5
                            text ""
                            text "{i}Pelas provisões sob o Estatuto de José, o Misericordioso, o Prisioneiro Astério promete lealdade e servidão ao Mestre do Labirinto."
                            text "{i}O Prisioneiro é instituído Zelador do Hotel acima do vale e lhe é legado o poder de realizar a vontade do Mestre."
                            text "{i}O Mestre, por sua vez, restringe o Labirinto, proibindo suas entidades maliciosas de deixarem dito vale."
                            text "{i}O domínio foi projetado para torturar o Prisioneiro e, de fato, sua missão deve ser cumprida. O Prisioneiro carregará o fardo da servidão, mas não sofrerá a ira do Labirinto dentro do território do Hotel."
                            text "{i}O Prisioneiro, amparado pela vontade de seu Mestre, fica seguro desde que cumpra seu dever, sob os termos do Estatuto"

                    elif Contract == "ArgosContract":
                        vbox spacing 10:
                            text "{i}{size=+2}Contrato de Argos" xalign 0.5
                            text ""
                            text "{i}Este documento compromete o Mestre do Labirinto e a cobra conhecida como Argos Panoptes, de agora em diante referido como \"o Capataz\", juntos em um acordo."
                            text "{color=[UIColorOrange]}{i}Artigo Um."
                            text "{i}O Mestre aluga ao Capataz a autoridade para invocar comida, água, abrigo e mobília para uso como ele achar adequado, inclusive para o benefício do cultivo de safras e a criação de animais."
                            text "{i}Em retorno, o Capataz aluga o Espelho de Héstia para uso do Mestre como ele achar adequado, inclusive para o benefício e manutenção da estrutura conhecida como \"Hotel\", conforme estabelecido em contratos anteriores."
                            text "{color=[UIColorOrange]}{i}Artigo Dois."
                            text "{i}O Mestre e o arrendatário devem abster-se de causar danos um ao outro, direta e indiretamente, por meios incluindo, mas não limitados à violência, incentivando ou recompensando terceiros à agressão mútua, sabotando estruturas, envenenando alimentos e água, entre outros."
                            text "{color=[UIColorOrange]}{i}Artigo Três."
                            text "{i}O Mestre é proibido de interferir direta ou indiretamente no pleno gozo dos direitos do Capataz concedidos neste contrato. O Capataz é similarmente proibido de causar danos ao \"Hotel.\""
                            text "{color=[UIColorOrange]}{i}Artigo Quatro."
                            text "{i}O Mestre está autorizado a fazer inspeções nas acomodações do Capataz, exceto em seus aposentos pessoais, cujo acesso é proibido."
                            text "{i}O Capataz está proibido de conspirar contra o Mestre e não deve usar os direitos garantidos por este Contrato para prejudicá-lo. O Mestre e o Capataz estão simetricamente comprometidos a este Artigo, incluindo, mas não limitando-se a não usar o Espelho de Héstia para causar danos ao Capataz."
                            text "{color=[UIColorOrange]}{i}Artigo Cinco."
                            text "{i}Este contrato é auto-impositivo. Se qualquer um de seus artigos for quebrado, a posse do Espelho de Héstia reverte para o Capataz e qualquer chama acesa pelo Espelho é apagada."
                            text "{i}Ao mesmo tempo, o Capataz perde os direitos transferidos pelo contrato e toda e qualquer estrutura por ele invocada deixa de existir após um intervalo de 10 minutos para permitir a evacuação."
                            text "{color=[UIColorOrange]}{i}Artigo Seis."
                            text "{i}Este artigo auto-impositivo entra em vigor no momento de sua assinatura e permanece válido durante o comando do Mestre e até que o Mestre posterior adquira a Escritura do Hotel."
                            text "{i}Pela vontade do Mestre, a quem o comando dos Olímpios sobre o domínio foi concedido, este contrato é estabelecido."

                    elif Contract == "Rings":
                        vbox spacing 10:
                            text "{i}{size=+2}Juramento dos Anéis Vinculativos" xalign 0.5
                            text ""
                            text "Um contrato blasfemo que desafia a vontade dos deuses, proposto pelo prisioneiro na tentativa de revelar as verdadeiras intenções do Mestre."
                            text "Em sua primeira encarnação, o anel de chumbo foi feito para ativar se condições impossíveis não fossem atendidas. Mas, assim como o próprio domínio onde o hotel foi construído, seu propósito foi corrompido e subvertido pela humanidade."
                            text "Talvez haja sabedoria na memória antiga de que um redentor assume as algemas daqueles que ele liberta. A humanidade contemporânea, no entanto, encontraria virtude em um senhor que voluntariamente limita seu próprio poder."
                            text ""
                            text "{i}Pela vontade do Mestre do Labirinto este contrato vinculativo é estabelecido, para que possa impor seu conteúdo ao mundo e seu povo."
                            text "{i}Por meio deste, o Mestre comanda à existência dois objetos interligados: um anel de chumbo para ajustar-se ao redor do bíceps de um homem e uma guirlanda de louros da largura do braço do prisioneiro."
                            text "{i}Estes dois objetos devem estar ligados em causa e efeito, assim como seus portadores."
                            text "{i}Aquele que vestir o anel de chumbo se encontrará em uma situação onde removê-lo será impossível, exceto mediante à revogação deste contrato."
                            text "{i}Quem primeiro vestir a coroa de louros se tornará seu proprietário permanente e imutável."
                            text "{i}Se o dono da coroa de louros alguma vez for levado para o vale do Labirinto —seja por coerção, ordem, ou força— então o anel de chumbo virá a contrair e fechar de forma a amputar o braço de seu portador."
                            text "{i}Pela vontade do Mestre, este contrato poderá ser revogado apenas se todas as suas partes — portador do anel de chumbo, dono da coroa de louros, e as duas testemunhas presentes durante a sua assinatura — o consentirem."
                            text "{i}Tal é a vontade do Mestre."
                            
                if FileType == 'Mementos':
                    if Memento == "Tablet1":
                        vbox spacing 10:
                            text "{i}{size=+2}Primeira Tábua: Lua Crescente" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando a jornada de um filho cordial a Creta."
                            text "Em tempos antigos, mesmo uma viagem curta levaria anos. Enfrentar o oceano sempre carregou a ameaça de morte, portanto, a viagem era reservada para guerreiros sedentos por sangue, mercadores ambiciosos e miseráveis desesperados."
                            text "Esta tábua é decorada com padrões de lua crescente imperfeitos. Aquele que os esculpiu desprovia do talento do artesão, mas não de seu carinho."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Cortou através do pescoço de meu pai como o açafrão colhido a foice destas margens rochosas,"
                            text "{i}aquela lua crescente despretensiosa, nascida do brilho de Hefesto e da turbulência de Zeus."
                            text ""
                            text "{i}Da Ásia Menor eu vim, carregando o peso de meu pai nas costas como ele uma vez me carregou."
                            text "{i}Durante a primavera de minha vida e o inverno da dele, cruzamos o mar para a Creta do Rei Minos."
                            text "{i}Enquanto meu pai enfermo navegava em seus pesadelos de velhice, eu trabalhava nos remos"
                            text "{i}e orava ao trapaceiro da corte do Rei Licaão, cuja sabedoria nos colocou neste curso."
                            text ""
                            text "{i}Através do curto mar, fizemos nosso caminho até Creta, saudados pelos chifres de íbex selvagens."
                            text "{i}Lá eu encontraria o mais belo trabalho de Hefesto, as luas crescentes do Olimpo —"
                            text "{i}aquelas que trazem a noite até mesmo para o aspecto incansável de um imortal."
                            text "{i}Eu sou Laomedonte, filho bastardo de Titono, uma vez príncipe de Troia."
                            text "{i}O mar que atravessei e o labirinto que percorri, eu faria tudo pelo meu pai,"
                            text "{i}nenhum custo muito alto, nenhuma carga pesada demais, nenhum truque não utilizado."
                            text "{i}Ouça a história de libertação do pai nas mãos do solitário guardião do labirinto"
                            text "{i}e a morte do híbrido pelo enviado dos deuses."

                    if Memento == "Tablet2":
                        vbox spacing 10:
                            text "{i}{size=+2}Segunda Tábua: Chegada" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando a chegada de uma família amaldiçoada a Creta."
                            text "Era uma vez um homem chamado Minos, filho de Zeus e Europa. Ele fundou Creta, o estado-ilha do qual a cultura grega descende. As lendas falam muito bem sobre a virtude do monarca, dito ter conquistado seu lugar entre os juízes de Hades após a morte."
                            text "Gerações mais tarde, no entanto, outro Minos assumiria o trono, um com uma disposição que irritava os deuses e homens de modo parecido."
                            text "Esta tábua é decorada com desenhos simples da cabeça de uma cabra selvagem. Seus chifres erguem-se orgulhosos, emoldurando uma única estrela solitária."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Titono era meu pai, sua era a mão a qual me ensinou a navegar nestas águas abundantes."
                            text "{i}Juntos, perseguimos e lançamos flechas contra auroques no solo avermelhado e úmido a partir dos quais fizemos nosso banquete."
                            text "{i}Pastoreamos e ordenhamos ovelhas, fizemos o queijo e o compartilhamos com nossos vizinhos,"
                            text "{i}mas meu pai foi roubado de mim pela estúpida deusa do amanhecer, Eos."
                            text "{i}Ela o tomou por marido e ele, mortal, que escolha ele tinha?"
                            text ""
                            text "{i}O tolo amanhecer pressionou Zeus para torná-lo imortal, para que ela nunca perdesse seu animal de estimação."
                            text "{i}Como um rei que não conhece o peso do ouro, ele tornou meu pai imortal"
                            text "{i}mas, como disse o trapaceiro de Licaão, não se lembrou da natureza efêmera de envelhecimento dos mortais."
                            text "{i}Agora sua mente está devastada pela idade, mesmo que seu corpo magro e enfermo não cesse."
                            text ""
                            text "{i}Naquele dia, quando atraquei meu navio na costa de Creta, carreguei-o nas costas de volta a Cnossos."
                            text "{i}Ele bamboleou como um bebê em sua primeira primavera, eu aguentei seu peso como uma vez ele fez com o meu."
                            text "{i}Para Creta eu trouxe meu pai, para libertá-lo desta miserável bênção divina."
                            text "{i}Durante o outono e o inverno, implorei aos pés do palácio de Cnossos pela misericórdia do Rei Minos."

                    if Memento == "Tablet3":
                        vbox spacing 10:
                            text "{i}{size=+2}Terceira Tábua: Audiência" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando uma rara audiência com um antigo rei."
                            text "Colunas carmesim ainda se encontram nos locais antigos de Creta, uma memória duraroura de uma época derradeira. O labiríntico Palácio de Cnossos, embora consumido e apodrecido, durou mais tempo que os reis e deuses."
                            text "Esta tábua é decorada com padrões repetitivos de colunas, mas um exame minucioso revela traços de um raro e precioso tesouro pulverizado sobre ela: açafrão."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}O Rei Minos, no topo de seu palácio carmesim, se recusou a nos conceder uma audiência,"
                            text "{i}mas a passos rápidos eu cacei os íbex selvagem de sua costa e celebrei com seu povo."
                            text "{i}O couro eu transformei em roupas, primeiro para o meu pai e posteriormente para os cretenses."
                            text "{i}Eu colhi o açafrão e os grãos, eu era um hóspede entre cada uma das famílias de Cnossos,"
                            text "{i}até que todos ouviram a lamentável história de meu pai e foram atiçados a enfurecer-se contra os deuses."
                            text ""
                            text "{i}O Rei Minos temia nossa história e a disseminação da impiedade entre a população."
                            text "{i}Sob o manto da noite, fomos levados para sua corte, empurrados por entre as fileiras de colunas carmesim."
                            text "{i}Fomos alimentados e vestidos com trajes tradicionais de Creta, e meu pai eu dei banho,"
                            text "{i}pois apenas eu sei como lidar com sua pele, mais delicada que pétalas de asfódelos."
                            text ""
                            text "{i}Enfim chegamos em sua corte, carreguei meu pai contra meu peito como um recém-nascido."
                            text "{i}Sobre um tapete de palha eu o deitei para o Rei ver o infortúnio nascido da bênção de Zeus"
                            text "{i}e implorei pelas luas crescentes de Hefesto, sua mais bela criação,"
                            text "{i}que partiram o crânio de Zeus e, assim, deram à luz Atenas, sempre mais sábia que seu pai."
                            text ""
                            text "{i}Pois é dever de um filho cuidar de seus pais durante a velhice,"
                            text "{i}e é meu dever libertar meu pai de sua enfermidade eterna."
                            text "{i}Eu sou Laomedonte, filho do imortal Titono, marido abandonado da estúpida Eos,"
                            text "{i}e procuro o Lábris de Creta, tão afiado a ponto de cortar seu fio de vida imortal tecido pelos Destinos."
                            text "{i}Para um par tão miserável e amaldiçoado, nenhum custo é muito alto, nenhuma carga é terrível demais."

                    if Memento == "Tablet4":
                        vbox spacing 10:
                            text "{i}{size=+2}Quarta Tábua: Jovem Mulher" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando a intervenção de uma jovem preocupada."
                            text "Os tempos antigos eram governados pelo princípio de que a força faz o correto. Mulheres que desejavam impor sua vontade ao mundo tiveram que contar com subterfúgios e inteligência."
                            text "Esta tábua é decorada com uma única linha em sua parte inferior, a silhueta do Monte Egeão; o local onde, diz a lenda, Zeus foi criado."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Quando o verão chegou e o Rei Minos ainda não havia nos concedido sua bênção,"
                            text "{i}uma jovem mulher entrou sorrateiramente em nossa tenda e me contou sobre o labirinto"
                            text "{i}— no pé de uma montanha, a mesma onde Zeus passou sua juventude —"
                            text "{i}onde encontraríamos um temível híbrido, um monstro nascido do caso da rainha com uma fera."
                            text ""
                            text "{i}Durante minhas tardes de colheita de açafrão, as esposas falaram-me de tal besta,"
                            text "{i}outrora conhecida como uma divindade da prosperidade exibida pelo Rei Minos,"
                            text "{i}trancado nos confins do labirinto depois de experimentar o canibalismo."
                            text "{i}Ele, disse a jovem, guarda o Lábris de Creta,"
                            text "{i}presente de Zeus para seu local de nascimento, bem no centro do labirinto."
                            text ""
                            text "{i}\"Busque o monstro amaldiçoado no coração do mundo,"
                            text "{i}no santuário carmesim ele guarda o machado capaz de cortar a linha vital."
                            text "{i}Mas saiba, bastardo de Troia, que somente aqueles inspirados pelo divino"
                            text "{i}podem levantá-lo — ore pela bênção de Atena."
                            text "{i}Não o toque; ele é revestido com o icor de Zeus."
                            text "{i}Não é destino de um homem tocar matéria divina.\""
                            text ""
                            text "{i}Eu parti com meu pai naquela mesma noite,"
                            text "{i}à distância, avistei a montanha de Zeus."
                            text "{i}Ficava mais perto a cada dia,"
                            text "{i}assim como o sofrimento de meu pai chegou ao fim."

                    if Memento == "Tablet5":
                        vbox spacing 10:
                            text "{i}{size=+2}Quinta Tábua: Monstro" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando o encontro de um homem com outro de natureza divina."
                            text "Para os gregos, ser um híbrido é ser um monstro. Os dois são indissociáveis."
                            text "Divino ou não, um híbrido é um ser abominável e repulsivo que boas pessoas fariam bem ao ostracizar."
                            text "Esta tábua é decorada com linhas labirínticas em suas margens."
                            text "Uma tábua de argila narrando uma intervenção de um jovem preocupado."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}No sopé do Monte Egeão, no planalto Lasiti, eu encontrei o labirinto,"
                            text "{i}uma antiga estrutura pintada com o mesmo carmesim do Palácio de Cnossos,"
                            text "{i}construído e esculpido com o amor e carinho de um artesão especialista."
                            text "{i}Por mais que tentasse, do topo da montanha não consegui aprender suas curvas,"
                            text "{i}pois sua forma alterava-se a cada piscar de meus olhos."
                            text ""
                            text "{i}Um porrete em minha mão, pai nas minhas costas, nos aventuramos juntos"
                            text "{i}com o conforto de saber que, mesmo se eu falhasse, sua dor ainda cessaria."
                            text "{i}Por três dias e três noites nós vagamos, ouvindo apenas o canto das cigarras"
                            text "{i}e o bater de cascos distantes, sempre fora de alcance."
                            text "{i}O monstro brincou conosco, nunca dando as caras."
                            text "{i}Eu temia que a fome tirasse minha vida e chorei pela de meu pai."
                            text ""
                            text "{i}No quarto dia, a criatura apareceu, o monstro híbrido de Pasífae."
                            text "{i}Não era o temível titã o qual me disseram que comia a carne de homens —"
                            text "{i}seu focinho rosa, tímidos chifres e olhos brilhantes eram os de um bezerro amamentado."
                            text ""
                            text "{i}Eu o desafiei para um combate, certo de que finalmente"
                            text "{i}teria um fim para este escárnio,"
                            text "{i}mas ele disparou por seus corredores intermináveis,"
                            text "{i}deixando para trás apenas o bater de cascos entrando em silêncio."

                    if Memento == "Tablet6":
                        vbox spacing 10:
                            text "{i}{size=+2}Sexta Tábua: Criança" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando a hospitalidade de uma criança."
                            text "Os gregos tinham muitos costumes e normas as quais ditavam como um hóspede deveria ser tratado. Naqueles tempos antigos, deuses disfarçados andavam entre os homens, então era esperado que um anfitrião tratasse seus convidados com o respeito que o divino merecia."
                            text "Trazer desgraça à casa de um anfitrião era uma atrocidade imperdoável que certamente inspiraria maldições sobre a linhagem de uma pessoa."
                            text "Esta tábua é adornada com representações de um templo, ou talvez um santuário. Um touro massacrado encontra-se em sua entrada."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Eu cacei a panturrilha do arqueiro, mas na verdade fui feito uma presa."
                            text "{i}Na quarta noite, eu desabei. Apenas então o menino revelou-se"
                            text "{i}de uma curva à frente."
                            text ""
                            text "{i}\"Eu sou Astério, filho adotivo do Rei Minos e guardião da casa de Dédalo."
                            text "{i}Este é um solo sagrado; em seu coração há um santuário, em seu centro jaz uma bacia"
                            text "{i}na qual queima um fogo sagrado presenteado pelos próprios deuses."
                            text "{i}Aprendi a arte da hospitalidade, lavar os pés dos hóspedes"
                            text "{i}e fornecer dois terços de minha refeição a ti."
                            text "{i}Eu lhe receberia carinhosamente — não fosse pelas armas em teu punho."
                            text "{i}Diga-me, por que levantarias teu braço contra os deuses?\""
                            text ""
                            text "{i}Com a pouca voz que restou em minha rouca garganta, eu respondi:"
                            text "{i}\"É contra a insensatez divina que me volto, não aos próprios deuses."
                            text "{i}Eu sou Laomedonte, filho de Titono, por sua vez, marido da deusa Eos;"
                            text "{i}esta casca que carregou é o que ela deixou para trás. Ela implorou a Zeus para torná-lo imortal"
                            text "{i}mas em seu tolo torpor, não requisitou juventude eterna."
                            text "{i}A velhice sequestrou sua mente, seus ossos agora estão frágeis"
                            text "{i}e sua pele está tão delicada quanto as asas de uma mariposa."
                            text "{i}Eu ouvi um conto que em Creta, no coração do labirinto, pode-se encontrar"
                            text "{i}uma arma de lua crescente, um lábris fabricado por Hefesto,"
                            text "{i}capaz de cortar o fio vital de um imortal.\""
                            text ""
                            text "{i}Talvez um guerreiro experiente tivesse jogado de lado minha história"
                            text "{i}e me deixado para morrer de fome e apodrecer nestes corredores intermináveis."
                            text "{i}Mas as crianças não sabem que um mendigo pode esconder uma faca sob o manto."

                    if Memento == "Tablet7":
                        vbox spacing 10:
                            text "{i}{size=+2}Sétima Tábua: Icor" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando uma pequena tragédia da loucura humana."
                            text "O corpo é um recipiente dado pelos deuses, sabendo muito bem que é o destino humano ser destroçado, quebrado e mutilado. Deixe a dor levá-lo embora, para que serve o sofrimento humano senão um pequeno desvio na existência de um deus?"
                            text "Esta tábua não possui adornos."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}O híbrido guiou eu e meu pai a um santuário carmesim —"
                            text "{i}uma morada de pedra abrigando uma piscina rasa de águas claras,"
                            text "{i}em seu centro encontra-se uma bacia de pedra na qual arde a chama sagrada."
                            text "{i}À sua esquerda, há um santuário menor, no centro há uma ampla chapa"
                            text "{i}de pedra polida na qual o machado de duas cabeças de Creta está cravado."
                            text ""
                            text "{i}Lembrei-me então das palavras da jovem moça, que apenas alguém"
                            text "{i}favorecido pelo divino poderia empunhar o machado."
                            text "{i}O menino híbrido alertou-me contra isto, mas a arrogância da masculinidade"
                            text "{i}me deixou surdo à todas as palavras de cautela."
                            text ""
                            text "{i}Até os dias de hoje carrego as marcas de queimadura em minhas mãos;"
                            text "{i}até os dias de hoje o machado está imbuído com o icor de Zeus,"
                            text "{i}ele rebelou-se contra o toque mortal e revidou."

                    if Memento == "Tablet8":
                        vbox spacing 10:
                            text "{i}{size=+2}Oitava Tábua: Guardião do Lábris" xalign 0.5
                            text ""
                            text "Uma tábua de argila retratando uma cena de traição."
                            text "Mães frequentemente alertam seus filhos para que não falem com estranhos. A mãe deste príncipe, no entanto, há muito desistiu das palavras e caiu em uma loucura de lamentações. Largado sozinho, muitas lições importantes nunca foram ensinadas a ele."
                            text "Esta tábua é adornada com um padrão decorativo tradicional de Creta, o machado de duas cabeças."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Por três dias e três noites, me recuperei de minhas queimaduras."
                            text "{i}O híbrido voluntariamente assumiu o papel de meu cuidador e de meu pai."
                            text "{i}Que hospitalidade ele demonstrou, minhas feridas ele limpou,"
                            text "{i}meu pai ele reajustava duas dúzias de vezes por dia para que nenhuma escara o afligisse."
                            text ""
                            text "{i}O tempo todo, implorei por sua ajuda; \"Você não tem divindade interior?"
                            text "{i}Pois seu pai é o touro de Poseidon, sua mãe é Pasífae, a ninfa."
                            text "{i}Certamente o lábris se renderá a ti; corte então o fio vital de meu pai"
                            text "{i}e o liberte desta maldição divina.\""
                            text ""
                            text "{i}O híbrido de chifres imaculados olhou para mim com olhos lustrosos."
                            text "{i}\"De fato, o machado não queima minha pele, mas seu peso é imenso,"
                            text "{i}nunca o desalojei de sua pedra. Ai de mim, meu bom príncipe,"
                            text "{i}não dissestes que o próprio Zeus concedeu a teu pai a dádiva da eternidade?"
                            text "{i}Que direito tenho eu de retirar o que os Crônidas concederam?\""
                            text ""
                            text "{i}\"Todos os deuses nos deram vida e os Destinos nos tiram dela."
                            text "{i}É apenas natural para um homem trazer a morte ao outro —"
                            text "{i}os deuses não derramaram icor em sua titanomaquia?"
                            text "{i}O homem apenas imita o que os Olímpios ensinaram."
                            text "{i}Será que alguém como você, com características desumanas,"
                            text "{i}acredita-se estar acima do dever de derramamento de sangue?"
                            text "{i}Não se preocupe, uma natureza peculiar não o isenta do dever."
                            text "{i}Há misericórdia em acabar com o sofrimento de alguém,"
                            text "{i}e ainda mais graça em ser subjugado pela arte de Hefesto."
                            text "{i}Por favor, hospitaleiro senhor do labirinto, ajude este filho em sua justa missão;"
                            text "{i}não tema o peso do machado, pois irei treiná-lo."
                            text "{i}Sua fisionomia calejará com a maturidade,"
                            text "{i}suas costas crescerão e ficarão tão largas quanto as estepes,"
                            text "{i}seu rugido estrondoso deve rachar as paredes."
                            text "{i}O treinarei da mesma forma que meu pai me ensinou."
                            text "{i}Pelo tempo que for necessário, estarei ao seu lado, até o dia"
                            text "{i}que seu poder elevar-se sobre o peso das luas crescentes de Hefesto.\""

                    if Memento == "Tablet9":
                        vbox spacing 10:
                            text "{i}{size=+2}Nona Tábua: Lira" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando uma pequena tragédia da loucura humana."
                            text "A música dura por apenas um momento, mas pode ser guardada para sempre na mente de alguém."
                            text "Esta tábua é adornada com o desenho de uma lira. O processo de cozimento, porém, fez com que os fios se rompessem."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Muitas noites passamos naquele santuário carmesim,"
                            text "{i}confortados pela lira do menino e pela chama da bacia."
                            text "{i}Antes e depois de cada refeição, Astério pagaria a Héstia seu tributo e além,"
                            text "{i}às vezes passando fome por uma glória maior da deusa."
                            text ""
                            text "{i}Noite após noite eu implorei por sua ajuda, mas ele não cedeu."
                            text "{i}Então usei de minha inteligência para persuadi-lo, eu o convenceria com minha lábia."
                            text "{i}Entre os gemidos de meu pai eu perguntaria,"
                            text "{i}ele responderia sem parar sua música, os dedos roçando nos fios."
                            text ""
                            text "{i}\"Por que você fica aqui, criança?"
                            text "{i}O planalto que nos rodeia é vasto e bonito."
                            text "{i}Não és um príncipe, descendente de uma rainha abençoada?"
                            text "{i}Muitas são as alegrias que a realeza bem merece desfrutar."
                            text "{i}Quando foi a última vez que colheu açafrão"
                            text "{i}e roçou teus dedos na suavidade oculta de suas pétalas?"
                            text "{i}Quando foi a última vez que se banhou na costa de Creta?"
                            text "{i}Não está em sua riqueza vestir-se de roxos e vermelhos vibrantes?"
                            text "{i}Quantas luas se passaram desde o amanhecer"
                            text "{i}no qual você cumprimentou os pescadores para comprar sua pesca fresca?\""
                            text ""
                            text "{i}\"Não sei ao certo, senhor,\" respondeu a criança, os olhos brilhando contra o fogo."
                            text "{i}Suas orelhas sacudiram junto com o vento frio."
                            text "{i}\"Passaram-se talvez sete invernos desde que negociei com os pescadores,"
                            text "{i}seis desde a última vez que meus cascos sentiram o abraço frio do mar,"
                            text "{i}cinco desde a última vez que segurei a mão de minha irmã em nosso caminho até os campos para colher flores,"
                            text "{i}quatro desde que não usei nada além de tecidos duros"
                            text "{i}e tive alguém com quem trocar palavras pela última vez."
                            text "{i}Mas nem uma noite se passou sem que eu puxasse as cordas de minha lira"
                            text "{i}nem um dia em que as dívidas dos deuses não foram pagas."
                            text "{i}Por mais solitário que seja o labirinto, não fui eu batizado com o nome das estrelas?"
                            text "{i}Eu encontro companheirismo entre elas, traçando-as com um dedo"
                            text "{i}e dentro de minha própria mente, da qual ninguém pode me despojar."
                            text "{i}Antes de sua chegada, eu pensei; do amanhecer ao anoitecer,"
                            text "{i}minha mente correu com histórias e possibilidades."
                            text "{i}O mar eu não verei até que meu pai me alivie de meu dever,"
                            text "{i}mas sua espuma posso para sempre manter na palma de minha mente.\""

                    if Memento == "Tablet10":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Tábua: Espuma do Mar" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando um bastardo tentando um jovem devoto a se afastar para longe de seu dever."
                            text "Creta não é conhecida por suas cobras venenosas. Não é nenhuma surpresa, então, que aquele que tentaria um príncipe a se afastar de seu dever tenha vindo do outro lado do mar."
                            text "Esta tábua é adornada com padrões parecidos com ondas."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}\"A costa não está longe, muito menos os açafrões pelos quais esta ilha é conhecida."
                            text "{i}Deixe-nos partir amanhã ao romper da madrugada, eu segurarei sua mão"
                            text "{i}enquanto cruzamos este planalto e deleitamos nossos olhos com suas cores."
                            text "{i}Deixe o carmesim deste santuário ser esquecido, passe seus dedos sobre as pétalas roxas"
                            text "{i}e afunde seus cascos nas praias arenosas e águas turvas."
                            text "{i}Amanhã, você e eu, ao amanhecer,"
                            text "{i}vamos deixar este cativeiro para trás e nos encher de contentamento.\""
                            text ""
                            text "{i}Mas o filho de Minos não acolheria ideias tão ímpias."
                            text "{i}\"Isto não devo fazer, pois dei minha palavra a meu pai, que não iria embora"
                            text "{i}da casa que Dédalo construiu. Devo cuidar do santuário e guardar o lábris"
                            text "{i}para que a ruína não caia sobre nossa terra e todo o seu povo."
                            text "{i}Você é um príncipe tanto quanto eu — um bastardo também."
                            text "{i}Por mais que seja nosso direito tomar parte dos prazeres da realeza,"
                            text "{i}o dever sozinho me acorrenta.\""
                            text ""
                            text "{i}\"Devemos retornar antes do anoitecer, Astério. O santuário não ficará sem manutenção,"
                            text "{i}nem o tributo a Héstia deixará de ser pago. Vamos colher uma pitada de açafrão e oferecer a ela,"
                            text "{i}nossa aventura trará alegria ao seu rosto caseiro."
                            text "{i}Nenhum homem saberá de nossa transgressão, apenas as águas espumosas do mar.\""
                            text ""
                            text "{i}Ele acariciou as cordas de sua lira, puxando aqui e ali."
                            text "{i}\"Mas eu saberia, e isto é ruim o suficiente."
                            text "{i}Você faria bem em gravar minha frase em sua mente."
                            text "{i}Não te esqueças que os Destinos não acharam por bem que eu fosse homem,"
                            text "{i}nem teceram a espuma do mar ou o açafrão da flor em meu tapete."
                            text "{i}Dentro do labirinto devo permanecer, pois esta é minha promessa.\""

                    if Memento == "Tablet11":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Primeira Tábua: Permuta" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando uma das muitas tragédias que levaram à morte do menino."
                            text "Esta tábua de argila é adornada com padrões decorativos de flores que racharam e se deformaram durante o processo de cozimento."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}A noite se estendia em diante, um véu de medo e escuridão nos cobriu."
                            text "{i}Um fogo transbordou em meu peito, talvez no dele também."
                            text "{i}Nenhuma oferta de prazeres poderia convencê-lo a partir"
                            text "{i}ou levantar o machado para libertar meu pai."
                            text "{i}Um estalo agudo me despertou do pensamento —"
                            text "{i}uma única brasa saltou da bacia para a piscina rasa."
                            text "{i}Eu a vi fracassar e morrer, sozinha e com frio —"
                            text "{i}que nitidez ela trouxe aos meus olhos!"
                            text "{i}Uma ideia saltou de mim antes que minha própria prudência tomasse conta."
                            text "{i}\"Príncipe de Creta expectante do amanhecer, por uma dúzia de dias"
                            text "{i}meu pai e eu nos abrigamos em sua morada,"
                            text "{i}comendo de sua comida e água."
                            text "{i}Como eu disse, era minha missão libertar meu pai da dor,"
                            text "{i}entregá-lo às margens da Nix, nas mãos de Caronte."
                            text "{i}Sou grato por sua hospitalidade — igualmente grato estaria Titono,"
                            text "{i}tivesse ele juízo o suficiente para gastar."
                            text "{i}Queria compartilhar com você uma última memória de alegria,"
                            text "{i}um único dia de felicidade quando vasculhamos estas praias."
                            text "{i}Mas este não é o caso; seu dever é muito grande."
                            text "{i}Então é com pesar que devo anunciar:"
                            text "{i}ao amanhecer, eu e meu pai deixaremos"
                            text "{i}o labirinto e os solos de Creta, para algum lugar,"
                            text "{i}além destas águas turvas deve haver um outro"
                            text "{i}inspirado pelos Olímpios, os quais podem encerrar nossa jornada.\""
                            text ""
                            text "{i}Astério expectante do amanhecer interrompeu sua música e fechou os olhos."
                            text "{i}O pesar parecia consumi-lo; um nó se formou em sua garganta."
                            text "{i}Quando as palavras o deixaram, elas estavam roucas e vacilantes."
                            text "{i}\"Você conhece as artes do combate, não?"
                            text "{i}Seu pai, em seu auge, lhe ensinou sobre o afiamento de uma lâmina."
                            text "{i}Quanto tempo levaria para eu reunir o poder necessário"
                            text "{i}para empunhar o tesouro de Hefesto, o machado capaz de cortar o fio de vida?"
                            text "{i}Suas palavras talvez carregassem sabedoria, afinal;"
                            text "{i}deve-se ascender para conceder misericórdia e libertação"
                            text "{i}para um prisioneiro acorrentado pela desgraça e infortúnio."
                            text "{i}Eu o farei, príncipe de Troia, dominarei o lábris"
                            text "{i}se você me conceder um pedido simples e humilde:"
                            text "{i}não me deixe sozinho.\""

                    if Memento == "Tablet12":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Segunda Tábua: Oferenda" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando a natureza suja de um híbrido."
                            text "Ser um híbrido é ser amaldiçoado com uma vida de infortúnios muito maiores que os de qualquer mortal."
                            text "Esta tábua de argila é adornada com padrões decorativos de fogo, embora o processo de cozimento os tenha deformado e distorcido."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Astério de chifres imaculados manteve sua palavra; nossas tardes foram gastas treinando"
                            text "{i}bem como meu próprio pai me ensinou o equilíbrio e os golpes de cada arma."
                            text "{i}Por três invernos, o labirinto de Dédalo tornou-se minha casa."
                            text "{i}O híbrido cresceu diante dos meus olhos, seus traços outrora finos"
                            text "{i}adquiriram o poder de um touro — medo ele provocaria entre os inimigos"
                            text "{i}não fosse por seu focinho rosa sempre infantil."
                            text "{i}Astério de costas largas como as estepes, foi assim que passei a chamá-lo"
                            text "{i}em sua brilhante glória de guerreiro."
                            text ""
                            text "{i}Ainda assim, não houve uma noite em que sua lira não tenha sido tocada,"
                            text "{i}nem uma onde o fogo de Héstia na bacia implorou pela pouca carne que tínhamos,"
                            text "{i}e muito menos uma noite em que nosso sangue não derramasse conforme chocávamos armamentos."
                            text "{i}E assim aprendi sobre o sangue sujo de Astério — uma mistura fétida,"
                            text "{i}tanto vermelho sangue quanto preto icor, prova das origens profanas do híbrido."
                            text "{i}Retumbou quando incendiado, e que grande chama ele gerou."
                            text "{i}Foi um ótimo sacrifício para a bacia, mais ainda para Héstia com seu gosto por carne de boi."
                            text "{i}Uma vez derramado, endurecia em uma pedra quebradiça e imunda, bem como o coágulo de uma ferida,"
                            text "{i}mas firme o suficiente para se passar como pedra cuspida de um vulcão."
                            text "{i}Seu cheiro trazia repulsa, mas que bela ignição era para a chama."
                            text "{i}Os corredores intermináveis e mutáveis do labirinto eram nossos campos de treinamento"
                            text "{i}pois o menino não contaminaria o santuário com sua natureza fétida."

                    if Memento == "Tablet13":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Terceira Tábua: Brasas a Morrer" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando o desânimo do híbrido."
                            text "Não se deve trancar a porta se o espírito do prisioneiro estiver quebrado."
                            text "Esta tábua de argila não possui decorações."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Depois que Astério tocou a canção de ninar do pai, conversamos em sussurros até tarde da noite."
                            text "{i}Trocaríamos contos de heróis e constelações, compartilhando lendas de nossas terras."
                            text "{i}\"Diga-me, garoto, você ouviu histórias das aldeias além deste mar?"
                            text "{i}Meu pai já foi príncipe de uma bela cidade-estado antes de a insensatez dos deuses tomar conta de sua mente."
                            text "{i}Lhe agrada a ideia de deixar este labirinto e viajar para o norte,"
                            text "{i}caso seu pai algum dia o liberte do dever de cuidar deste santuário?\""
                            text ""
                            text "{i}O menino hesitou antes de responder, quando o fez, sua voz estalou como as brasas."
                            text "{i}\"Para ver além destas paredes e do mar? De forma alguma, ouvi pouquíssimas histórias,"
                            text "{i}mas o pensamento, cruzar o mar, como eu poderia achar isto agradável?"
                            text "{i}Creta é o berço do homem, está acima de todas as outras nações e sobreviverá a todas elas,"
                            text "{i}que razão teria alguém para abandonar seu seio?"
                            text "{i}Ai de mim, apenas o pensamento é tolice, pois meu pai jamais me dispensará de meu dever."
                            text "{i}Posso deixar estas paredes, mas haverá outro labirinto para mim"
                            text "{i}assim que provar que sou capaz de empunhar o lábris.\""
                            text ""
                            text "{i}\"Esqueça Creta, então, o pensamento da liberdade o atiça?"
                            text "{i}Pode não haver terra como esta, onde as cobras não conhecem palavras venenosas"
                            text "{i}e as cabras selvagens têm uma carne tão rica, mas pense em um lugar onde a liberdade é sua.\""
                            text ""
                            text "{i}E como madeira seca, abandonada por anos, sua voz estalou entre as brasas."
                            text "{i}\"Elimine o pensamento, meu senhor. Não vê que sou uma besta?"
                            text "{i}Minha vontade dificilmente importa nesse caso, independente de eu desejar ou não a liberdade,"
                            text "{i}como cruzaria o mar revolto? Se soubesse como velejar, ainda assim não teria como fazê-lo."
                            text "{i}Tivesse eu a tripulação e o barco, eles não me subjugariam pelo pecado que sou?"
                            text "{i}E se eu de fato conseguir cruzar o mar, o que me espera do outro lado? Ao menos aqui"
                            text "{i}tenho a esperança de ver minha família mais uma vez, de sua próxima visita."
                            text "{i}Certamente eles chegarão em breve, meus irmãos e eu caçaremos juntos."
                            text "{i}Não há futuro em nenhum outro lugar para mim, meu senhor,"
                            text "{i}mesmo que eu tema que esta terra também não comporte nada para mim, exceto brasas a morrer.\""

                    if Memento == "Tablet14":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Quarta Tábua: Redentor" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando uma das muitas tragédias que levaram à morte de um menino."
                            text "O que aguarda o sacrificado além de sua tormenta? Pode-se apenas imaginar."
                            text "Esta tábua de argila é adornada com padrões decorativos de flores, os quais racharam e se deformaram durante o processo de cozimento."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Um dia o menino encontrou uma flor crescendo através de uma rachadura no chão de pedra,"
                            text "{i}a primeira que ele viu em todos aqueles invernos desde seu banimento."
                            text "{i}Que dor havia em seus olhos, sabendo que não deveria ser arrancada"
                            text "{i}e ter que percorrer os corredores apenas para dar uma olhada!"
                            text "{i}Interminável foi sua tristeza quando a chuva forte apodreceu suas raízes,"
                            text "{i}mas ele encontrou consolo em oferecê-la a Héstia como sacrifício."
                            text ""
                            text "{i}Já se passaram três invernos desde minha chegada a esta ilha,"
                            text "{i}o híbrido tornou-se um guerreiro excelente e capaz sob minha tutela."
                            text "{i}Não demoraria muito para ele ser capaz de levantar o lábris"
                            text "{i}e pôr um fim ao sofrimento de meu pai."
                            text ""
                            text "{i}Durante uma das noites frias, quando nos amontoamos contra a bacia,"
                            text "{i}quando a madeira soltou uma fumaça fétida e escura capaz de trazer lágrimas aos olhos,"
                            text "{i}ele me perguntou se uma flor sentia alegria ao ser arrancada e oferecida aos deuses."
                            text "{i}Às vezes, esta criatura adulta falava com a inocência de uma criança,"
                            text "{i}aquela voz suave que todos nós aprendemos a abandonar talvez muito cedo."
                            text "{i}Falei então com a dor e a pena de um pai consolando seu filho com a morte de um cachorro:"
                            text "{i}\"Não há maior honra que ser oferecido aos doze, criança."
                            text "{i}Pois qualquer fraqueza que ela ou qualquer ser já tenha mostrado é redimida"
                            text "{i}quando a vida de uma pessoa é assim arrancada e tornada sagrada."
                            text "{i}Em breve acabaremos com a dor de meu pai, e então você enxergará"
                            text "{i}como uma libertação de pesadas algemas, e verá a si mesmo como seu querido redentor.\""
                            text ""
                            text "{i}Aquela foi a última noite na qual o híbrido tocou sua lira; uma corda estourou."
                            text "{i}Astério Cortador de Fios embalou o instrumento contra seu peito"
                            text "{i}e cantarolou até a sonolência cair sobre seus olhos."
                            text "{i}Antes de nos retirarmos para nossas esteiras de palha, no entanto, ele disse:"
                            text "{i}\"Existe calor em seu coração para acreditar que eu, também,"
                            text "{i}um dia serei abençoado com um redentor? Um cruzando o mar para me libertar"
                            text "{i}destas algemas tão familiares que carregam os símbolos dos deuses?"
                            text "{i}Será que um dia serei redimido de meu nascimento, voarei livre"
                            text "{i}como Ícaro e Dédalo voaram, para longe desta terra miserável?\""
                            text ""
                            text "{i}Eu senti então a faca escondida entre suas palavras, prestes a cortar minha própria garganta também."
                            text "{i}O que eu poderia dizer? Juntei minhas brasas, todas que pude reunir, e disse:"
                            text "{i}\"Você será redimido, sem dúvida, e então verá as flores"
                            text "{i}crescendo fora destas paredes carmesim de Dédalo."
                            text "{i}Nenhum mar é grande demais, nenhuma maldição é ruim o suficiente, para impedir alguém de alcançar a salvação,"
                            text "{i}acima de tudo, aquele que teria a misericórdia de libertar um homem enfermo e amaldiçoado.\""
                            text ""
                            text "{i}E estas palavras, hoje são as que mais me arrependo,"
                            text "{i}que pesadelo miserável depositei nele?"

                    if Memento == "Tablet15":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Quinta Tábua: Insensatez" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando o último resquício de esperança de um prisioneiro."
                            text "É preciso apagar as chamas ao redor para realizar sua vontade. Um prisioneiro deve ser mantido acorrentado para cumprir sua missão."
                            text "Ainda assim, algumas brasas possuem uma segunda vida, revelada quando a camada de fuligem voa para expor um coração ainda vermelho."
                            text "Esta tábua não possui enfeites."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}A primavera chegou, mas o inverno persistiu no coração do híbrido."
                            text "{i}Sua respiração ficou mais curta e uma tosse criou raízes em seus pulmões,"
                            text "{i}ainda assim, eu o puxava de seu saco de dormir todos os dias para aprender a arte da guerra,"
                            text "{i}para que ele pudesse libertar meu pai de sua existência amaldiçoada."
                            text "{i}Um fogo fervia em meus pulmões e eu também fiquei sem fôlego,"
                            text "{i}embora em mim não fosse de mal-estar; e sim de desespero."
                            text "{i}Apesar de minha necessidade por silêncio, o híbrido falou entre nossas partidas."
                            text ""
                            text "{i}\"Quando chegar o dia em que meu redentor me libertará, como ele saberá"
                            text "{i}virar à esquerda três vezes depois do pátio com o mural de touro em alto relevo?"
                            text "{i}Os deuses abençoarão sua mente com a visão de um falcão voando acima?"
                            text "{i}Hera enviará cobras para guiá-lo até o santuário que eu protejo?"
                            text "{i}Talvez meu salvador seguirá os mesmos passos de ti,"
                            text "{i}primeiro procurando a casa onde nasci para aprender sobre o coração do labirinto.\""
                            text ""
                            text "{i}Fiz sinal para reiniciarmos nosso combate, mas ele não se mexeu."
                            text "{i}Comecei então a falar as palavras doces que ele tanto desejava ouvir."
                            text "{i}\"O que você desejar, aquilo que quiser, para um jovem tão devoto,"
                            text "{i}Sei que os deuses atenderão ao seu pedido; poucos são aqueles"
                            text "{i}com o icor correndo em suas veias e com uma disposição tão leal."
                            text "{i}Após a conclusão de nosso ritual, quando o fio vital de meu pai for rompido,"
                            text "{i}certamente eles enviarão a própria Nice para guiar um redentor até você.\""
                            text ""
                            text "{i}\"O ritual, de fato,\" murmurou o monstro e percebi novamente o estalar das brasas."
                            text "{i}\"Obstinado Titono, você ouviria meu apelo? Há um desejo pelo qual"
                            text "{i}meu coração anseia. Quando deixares a cada de Dédalo,"
                            text "{i}retornaria para minha terra natal e contaria um segredo para minha família?"
                            text "{i}Diga-os que os caminhos do labirinto rendem-se gentilmente se alguém deixar para trás"
                            text "{i}um fio de lã enquanto o enfrentam."
                            text "{i}Com este conhecimento, meu salvador certamente encontrará seu caminho"
                            text "{i}para o coração onde o espero."
                            text "{i}Embora, se também ouviria minha vergonhosa confissão,"
                            text "{i}assim que o desejo pela chegada de meu redentor se apoderou de mim,"
                            text "{i}uma ideia boba a qual não consigo me livrar também apareceu. Em meus sonhos, me enxergo saindo"
                            text "{i}da casa de Dédalo, vendo por conta própria os campos de açafrão"
                            text "{i}e a água espumosa do mar, o mesmo de onde veio meu progenitor."
                            text "{i}Meu coração dispara quando penso na chegada de um redentor,"
                            text "{i}mas dolorosamente, como se de alguma forma eu tivesse que evitar a ideia."
                            text "{i}Pela primeira vez em todos esses anos, meu amigo, eu desejo"
                            text "{i}abandonar meu posto e deixar este labirinto."
                            text "{i}As cavernas do Monte Egeão me forneceriam um porto seguro,"
                            text "{i}existem muitas clareiras desconhecidas nesta ilha"
                            text "{i}onde eu poderia encontrar conforto, e talvez eu pudesse negociar o pouco que tenho"
                            text "{i}em troca de uma passagem segura através do mar para terras desconhecidas."
                            text "{i}Diga-me, Titono, esta ideia não é podre e vergonhosa?"
                            text "{i}Abandonar meu dever para com os deuses, deixar estas paredes carmesim"
                            text "{i}neste exato instante. Meramente dizer isto acelera meu coração."
                            text "{i}E por mais covarde que eu saiba que isto é, esta noite acredito que poderia e deveria fazê-lo."
                            text "{i}Diga-me, amigo, eu deveria? Abandonar o dever e agarrar"
                            text "{i}esta covarde salvação com minhas próprias mãos?\""
                            text ""
                            text "{i}Naquela noite, a chama da bacia morreu pela primeira vez desde minha chegada, invernos atrás."
                            text "{i}Meu pai acordou à meia-noite e chamou meu nome, em meio a sua névoa de senilidade ele perguntou"
                            text "{i}\"Quem é este jovem a soluçar que ouço, e por que seus apelos são tão desesperados?"
                            text "{i}Filho, onde estamos e que destino amaldiçoado caiu sobre este menino"
                            text "{i}para seus lamentos inspirarem tanta tristeza em mim?"
                            text "{i}Não há nada que possamos fazer para confortá-lo?\""
                            text ""
                            text "{i}E para meu pai eu disse \"Não, elimine a memória de sua mente, pai,"
                            text "{i}o híbrido logo cumprirá seu dever e a paz virá para ti.\""
                            text ""
                            text "{i}Um preço deve ser pago para fazer o que é certo, todos sabem."
                            text "{i}Trazer a morte a uma vítima indefesa e voluntária deixa uma mancha na"
                            text "{i}alma de uma pessoa, um peso indelével, como aquele que esmaga Atlas."
                            text "{i}O híbrido suportou o peso do fim de meu pai e eu do dele."
                            text "{i}Um homem deve estar pronto para levar outros à morte para fazer o que é certo."
                            text "{i}Eu conheço esta velha sabedoria, ainda assim, por que não consigo conter meu coração acelerado?"
                            text "{i}Quanta madeira devo colocar sob sua pira para compensar minha irreverência?"

                    if Memento == "Tablet16":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Sexta Tábua: Ritual" xalign 0.5
                            text ""
                            text "Uma tábua de argila retratando um crime contra a ordem divina."
                            text "A nenhum mortal é dado o direito de remover a eternidade concedida pelos Olímpios. Aquele que se levanta contra a ordem divina é amaldiçoado com o destino mais imundo."
                            text "A tábua é adornada com a representação do rosto de um homem. O artista tentou esculpir olhos calmos, mas o processo de cozimento da tábua deu-lhe uma expressão de horror, condizente com a maldição desencadeada por sua morte."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Seu nome era Titono, ele era meu pai."
                            text "{i}No ápice de sua vida, quando eu estava no auge de minha masculinidade,"
                            text "{i}meu pai foi levado embora por Eos, tola deusa do amanhecer."
                            text "{i}Zeus o fez imortal, mas não jovem para sempre."
                            text "{i}Sua mente definhou, seu corpo secou em uma casca,"
                            text "{i}ainda assim, Tânato não o abraçou, nem"
                            text "{i}Hermes Psicopompo o guiaria até as margens do Estige."
                            text ""
                            text "{i}Com sua casca amarrada às minhas costas, cruzei o mar até a terra de Creta"
                            text "{i}onde uma lua crescente que até mesmo os Destinos temiam estava escondida."
                            text "{i}O guardião do lábris nos encontrou dentro da casa de Dédalo,"
                            text "{i}ele nos trouxe de volta à saúde, apesar de seu medo do machado."
                            text "{i}Eu o persuadi a conceder misericórdia ao meu pai,"
                            text "{i}pois apenas aqueles com um toque do divino podem empunhar o Cortador de Fios."
                            text ""
                            text "{i}No coração do labirinto havia um santuário para os deuses e,"
                            text "{i}por sete invernos, um fogo ardeu dentro dele em uma ampla bacia."
                            text "{i}A chama eu subjuguei com minhas palavras e, sete noites depois,"
                            text "{i}colocamos o pescoço de meu pai na borda da bacia."
                            text "{i}O lábris rachou a pedra como um trovão chacoalha a mente,"
                            text "{i}e assim cortou o fio de meu pai, aquele que os Destinos não tocariam."
                            text "{i}Seu receptáculo abandonado inclinou-se para o lado, como uma criança procurando o ombro da mãe"
                            text "{i}para cair no sono durante uma longa jornada de carruagem."
                            text ""
                            text "{i}Em sua velhice, meu pai adorava o cheiro de açafrão, embora seu apetite tenha quase cessado."
                            text "{i}Mel o fazia sorrir, às vezes rir. Quando segurava sua mão,"
                            text "{i}seus dedos se entrelaçavam com os meus, mesmo que sua mente tivesse ido embora."
                            text ""
                            text "{i}Um icor negro fluiu de seu ferimento para a bacia. Nela fizemos sua pira."
                            text "{i}À medida que a chama lambia e beijava o receptáculo abandonado de meu pai,"
                            text "{i}o híbrido cantarolava no lugar de sua lira, a qual não mais tinha cordas para cantar."
                            text ""
                            text "{i}O fogo não limpou a bacia, nem sarou suas rachaduras."
                            text "{i}O santuário adquiriu um fedor indelevelmente fétido, dentro dele, pesadelos sombrios"
                            text "{i}rastejariam à noite, gemendo e rindo."
                            text ""
                            text "{i}\"O santuário está profanado,\" disse Astério enquanto eu fazia os preparativos para minha partida."
                            text "{i}\"Não é mais um lugar de adoração ou sacrifício. E o lábris,"
                            text "{i}o qual jurei proteger, o sangue de Titono não sai dele."
                            text "{i}O que devo fazer, Laomedonte, como posso lavar esta blasfêmia de minhas mãos?\""
                            text ""
                            text "{i}Eu não tinha resposta para ele, e nenhuma palavra doce minha poderia distrai-lo."
                            text "{i}Quando deixei o coração do labirinto, ele ficou para trás,"
                            text "{i}\"Aguardarei meu redentor, então, como os Destinos teceram."
                            text "{i}Ainda assim, você me visitará, Laomedonte, para manter minha solidão sob controle?\""

                    if Memento == "Tablet17":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Sétima Tábua: Pira" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando a libertação de um prisioneiro."
                            text "Diante da morte, faz-se bem em poupar as palavras."
                            text "Uma chama queimando em uma bacia adorna a parte inferior desta tábua. As margens estão alinhadas com círculos, provavelmente representando moedas."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Ele era Astério, filho da Rainha Pasífae e criado pelo Rei Minos."
                            text "{i}Ele foi gerado pelo touro branco de Poseidon com a ajuda do astuto Dédalo."
                            text "{i}Ele, o qual tinha cabelos de espuma do mar, chifres imaculados, abençoados com o olhar de Hera,"
                            text "{i}de costas largas como as estepes e eternamente à espera do amanhecer,"
                            text "{i}libertou meu pai de algemas insuportáveis e,"
                            text "{i}ao fazer isto, tomou o peso de sua maldição."
                            text "{i}Juntos, sangramos icor na bacia da deusa e,"
                            text "{i}por nossa infinita arrogância, incorreu sua ira para sempre e além."
                            text "{i}Eu permaneci em Creta, mas não vi as paredes carmesim do labirinto,"
                            text "{i}até que chegou a notícia de um guerreiro ateniense favorecido por Ariadne,"
                            text "{i}O irmão de berro alto de Astério. Ela contou para ele o segredo"
                            text "{i}que eu trouxe, de acordo com os desejos do híbrido"
                            text "{i}— mas, na verdade, ela já sabia, pois Dédalo lhe deixou o conhecimento."
                            text "{i}O ateniense aventurou-se no labirinto com um novelo de lã,"
                            text "{i}lá ele encontrou seu alvo, a suposta besta temível."
                            text ""
                            text "{i}O Palácio de Cnossos fará você acreditar que o Astério nascido da brasa"
                            text "{i}lutou por sua vida contra a força do invasor."
                            text "{i}Mas eu corri para o labirinto assim que ouvi a palavra"
                            text "{i}e encontrei mais uma vez a bacia rachada cheia de preto e vermelho."
                            text "{i}Seu corpo estava deitado ao lado, em uma sonolência sem cabeça,"
                            text "{i}com o lábris cortador de fios em seus cascos."
                            text "{i}De fato, seu redentor havia chegado e o libertado,"
                            text "{i}assim como, digo a mim mesmo, os próprios Destinos desejavam."
                            text ""
                            text "{i}Eu deveria acreditar que agora ele está livre de sua vida tórrida,"
                            text "{i}que ele encontrará paz na companhia de seu descendente adotivo,"
                            text "{i}o virtuoso Rei Minos de Creta, que fundou este país."
                            text "{i}Mas por que estou consumido pela mágoa e um peso inefável?"
                            text "{i}Eu olho para seus restos mortais e que fúria me enche de ver"
                            text "{i}que o ateniense levou o chifre de meu amigo como troféu."
                            text "{i}O lábris amaldiçoado, as luas crescentes de Hefesto, ele deixou para trás,"
                            text "{i}agora manchados com flúido divino e mortal."
                            text ""
                            text "{i}Os guardas do Rei Minos chegaram quando eu completei sua pira."
                            text "{i}Eles não me pararam, na verdade, coletaram mais madeira,"
                            text "{i}mas o último resquício de osso do chifre imaculado eles levaram de volta ao rei."
                            text "{i}Uma moeda de ouro eu deixei debaixo da língua de meu amigo, para apaziguar Caronte."
                            text "{i}Na bacia da qual ele fielmente cuidou, partiu desta terra."

                    if Memento == "Tablet18":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Oitava Tábua: Esquiro" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando um destino sinistro."
                            text "Um redentor assume as algemas daqueles que ele liberta. Esta cadeia ininterrupta se estende desde o nascimento da humanidade até os dias de hoje."
                            text "Nenhum é poupado."
                            text "Esta tábua não possui enfeites."
                            text "Na tábua está contido:"
                            text ""
                            text "{i}Eu continuo com minha jornada, agora que meu coração não pertence a nenhuma terra."
                            text "{i}Deixarei Creta para trás em busca de um lugar que acalme"
                            text "{i}esta fúria implacável em meu peito."
                            text "{i}Eu olho para o mar do norte e me lembro do legado de meu pai,"
                            text "{i}que ele era realmente próximo do monarca de Esquiro."
                            text "{i}É como se os próprios Destinos me chamassem para lá,"
                            text "{i}e eu não tenho dúvidas de que a intenção deles é que eu encontre meu redentor,"
                            text "{i}ou talvez torne-me um eu mesmo."
                            text ""
                            text "{i}O céu estrelado deste mundo sobreviveu a todos os amanheceres destruidores de estrelas"
                            text "{i}e deve suportá-los por muito mais tempo."
                            text "{i}O céu estrelado e os pecados dos homens continuaram,"
                            text "{i}Astério não."

                    if Memento == "TypewriterScrap":
                        vbox spacing 10:
                            text "{i}{size=+2}Descarte de máquina de escrever" xalign 0.5
                            text ""
                            text "Um pedaço de papel amassado encontrado por sua equipe de exploração."
                            text "Está contido:"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}AqpqpqpqQPQPQP qaZxswed S3RViços ESCRIturas dezenove dezoiit oooooooo"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}astériup ASTÉRIO"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}DATIROGRAFIA minotaURO labirinto anexo plsklmdv skwjekmw"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}serviços"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}continue"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}sozinhos"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}agressão"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}dormindo"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}evolução"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}regresso"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}singular"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}quadrado"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}S E R V I Ç O S"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}L E N C E S L C"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}O S R E C E E O"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I S R L E D E N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}V E E S S I P T"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}R R E P G N I I"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}E G O R P R E N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I L E N O L E U"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}S E R V I Ç O S ·"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}E N C E · S L E C"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}L E C E D I N E O"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}O R ·       G P N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I · S       · I T"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}V S S       P E I"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}· S E L R E E R N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}R E R G O R P · U"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}E I L E N O L · E"
                            text ""
                            text ""
                            text "Mostrar isto ao minotauro faz suas orelhas caírem e seus ombros encolherem."
                            text "Ele explica que um mestre anterior havia trazido algumas publicações e \"a coisa com os botões para imprimir letras\"."
                            text "Ao ver que todas as letras eram do mesmo tamanho, ele tentou, em suas próprias palavras, \"fazer um quadrado de palavras\"."
                            text "Ele não deseja ser lembrado disso."

                    if Memento == "PoemNotebook":
                        vbox spacing 10:
                            text "{i}{size=+2}Caderno encadernado em pele de cabra" xalign 0.5
                            text ""
                            text "Um pequeno caderno, um pouco menor que a mão de um humano."
                            text "O mesmo poema é escrito em suas páginas uma dúzia de vezes, com variações diminutas a cada versão. Nas últimas páginas, há um rabisco final, diferente de todos os outros."
                            text "A caligrafia é pobre e espasmódica."
                            text ""
                            text "{u}COREGO"
                            text "{i}        Um grão de areia conduziu minha mente para muito tempo atrás,"
                            text "{i}onde quer que a memória pudesse sufocar minha garganta"
                            text "{i}ou cegar minha visão. Estou indefeso diante dela."
                            text "{i}        Uma mente muito aberta, muito ansiosa para lembrar,"
                            text "{i}e lá, problemas impressos eideticamente"
                            text "{i}onde pudessem estar. Um abraço pode ser mantido"
                            text "{i}na mente, mas os golpes deixam contusões sensíveis, cicatrizes,"
                            text "{i}as cicatrizes mais feias de amigos desconfiados:"
                            text "{i}Tudo baseado em suspeitas ocultas"
                            text "{i}sobre mãos de nervos salientes, truques e arrancadas ignorantes"
                            text "{i}a outra metade esqueceu. Se apenas eu"
                            text "{i}não tivesse esta armadilha certeira como pedra entre meus chifres."
                            text "{i}Não posso evitar odiar minha posição, 'abençoado'"
                            text "{i}solitário patriota da tensa Mnemosine."
                            text ""
                            text "{u}CORO"
                            text "{i}        \"Que tolice: branda indulgência, lamúria, e--\""
                            text "{i}        Está tudo cimentado; o que é luz apenas espuma"
                            text "{i}e flutua sobre o topo, fundo estagnado"
                            text "{i}e sufocante: Parado. Esta podridão cáustica"
                            text "{i}não tem uso: não levanta nada como o fermento"
                            text "{i}nem delicia como a embriaguez. Por que continuar?"
                            text "{i}        \"Apenas pare. Este empreendimento simplesmente escapa de você.\""
                            text ""
                            text "{u}COREGO"
                            text "{i}        Uma pele mais grossa é necessária, mas"
                            text "{i}talvez com menos portas de entrada para rastrear"
                            text "{i}quem já conquistou sua autoestima, então,"
                            text "{i}mais obteriam força, coragem e garantida"
                            text "{i}autossuficiência. Leva apenas uma vez:"
                            text "{i}um golpe bem posicionado manqueja o equilíbrio."
                            text "{i}        Nenhuma força é obtida com exposição covarde"
                            text "{i}e cutucadas de teste quando as feridas estão abertas, doloridas"
                            text "{i}e ainda sangrando. Um coagulante, ou"
                            text "{i}tônico adstringente é necessário — sem atrito,"
                            text "{i}sangria, ossos realocados e ligados, toxinas"
                            text "{i}aplicadas em doses 'terapêuticas'. A esperança"
                            text "{i}é a hipertrofia — mas ainda não — mas em breve—!—? ..."
                            text ""
                            text "{u}CORO"
                            text "{i}        \"Que tolice: branda indulgência, lamúria, e —\""
                            text "{i}        Um ritmo que funciona, dura e cresce mais forte"
                            text "{i}evasivo é. É tudo o que é simples aqui."
                            text "{i}O que o crescimento é, não é impedido por torturas, é destruído"
                            text "{i}por uma fonte o mais próxima possível."
                            text "{i}A loucura de uma mãe herdou aqui?"
                            text "{i}        \"Apenas pare. Este empreendimento simplesmente escapa de você.\""
                            text ""
                            text ""
                            text "{i}        \"Eu sei que ofereço muito pouco, mas"
                            text "{i}o pouco oferecido: precioso é, eu espero.\""

                    if Memento == "RockCarving":
                        vbox spacing 10:
                            text "{i}{size=+2}Petróglifo" xalign 0.5
                            text ""
                            text "Uma placa de rocha com inscrições gravadas encontrada no Vale."
                            text "Algumas partes da rocha estão faltando, então é impossível ler o poema completo."
                            text ""
                            text "{i}\"Chore, ó, grande mãe, pesar tão profundo que nenhuma Musa Parnassana se prepararia antes que um pensamento sobre este apelo fizesse ----"
                            text "{i}Chame, ó, Poseidon, uma Musa muito mais resistente e destemida que ----"
                            text "{i}Por favor, ó, Melpômene, cante versos cansados pelos corredores vermelhos de Cnossos, ricos ----"
                            text "{i}Tália, não venha, ----\""

                    if Memento == "Agape":
                        vbox spacing 10:
                            text "{i}{size=+2}Ágape, Eros, Filia" xalign 0.5
                            text ""
                            text "Um epigrama escrito para um pagão romano ou gnóstico, pontificando sua conquista dos gregos."
                            text "Como de costume com todas as línguas estrangeiras escritas no labirinto, as letras mudam conforme você focaliza seus olhos nelas, tornando o pedaço de pergaminho legível."
                            text "No entanto, você poderia jurar que alguns dos glifos que agora se referem às mesmas palavras pareciam diferentes para você um momento atrás."
                            text ""
                            text "{i}\"    'Mas amor não é amor, é mais como amor, ele me"
                            text "{i}disse, usando palavras da minha própria língua, de nós"
                            text "{i}importado. Que compartimentalização"
                            text "{i}esses romanos fazem! Eles falam como se o crepúsculo"
                            text "{i}não fosse ainda assim o sol!"
                            text ""
                            text "{i}    Eles levaram nossos deuses,"
                            text "{i}refizeram, remodelaram, misturaram os significados, nomes —"
                            text "{i}um panteão de desordem. Isto primeiro, mas então"
                            text "{i}esses homens, com garo, encharcaram e afogaram nossa comida."
                            text "{i}E agora, eles me dão sermão usando nossas próprias palavras…\""

                    if Memento == "FieldWork":
                        vbox spacing 10:
                            text "{i}{size=+2}Página ilustrada rasgada" xalign 0.5
                            text ""
                            text "Um pedaço de papel antigo e amarelado com uma das pontas arrancadas. Você presume que seja uma página arrancada de um livro antigo."
                            text "A página é adornada com uma ilustração de um minotauro arando um campo em tinta colorida azul e dourada."
                            if not main_menu:
                                if player_background in ['humanities', 'arts']:
                                    text "Um poema está escrito em tinta vermelha abaixo da ilustração. Você reconhece que foi escrito usando o alfabeto grego; isto, combinado com o estilo e moldura da ilustração, dataria esta página por volta da era Bizantina."
                                else:
                                    text "Um poema está escrito em tinta vermelha abaixo da ilustração. É escrito em um idioma estranho para você, mas as letras se alteram à medida que você foca seus olhos, tornando o pedaço de papel legível."
                            else:
                                text "Um poema está escrito em tinta vermelha abaixo da ilustração. É escrito em um idioma estranho para você, mas as letras se alteram à medida que você foca seus olhos, tornando o pedaço de papel legível."
                            text "É uma ode ao trabalho no campo, ao invés de farra:"
                            text ""
                            text "{i}    \"Aveia selvagem! Qual a utilidade disto? O que faz"
                            text "{i}o próprio homem é a utilidade bem trabalhada"
                            text "{i}nos campos de ajuda e assistência e dos produtos feitos."
                            text "{i}    Bem cuidados, estes corredores talvez tornem-se filas"
                            text "{i}por capricho do Mestre. Campos férteis estendem-se"
                            text "{i}com trabalhos manuais pisoteados, bem cobertos com céu,"
                            text "{i}    através de corredores de trigo, milho e aveia os quais"
                            text "{i}nenhum Perses, estúpido, poderia deixar sem cultivar."
                            text "{i}O campo preparado legava bondade, não selvageria, pela mão.\""

                    if Memento == "FoldedNote":
                        vbox spacing 10:
                            text "{i}{size=+2}Nota Dobrada" xalign 0.5
                            text ""
                            text "Um epigrama escrito para um ex-mestre prolixo, direto, ativo e volátil."
                            text "Ao perguntar a Astério sobre a nota, com pesar, ele explica que se lembra de ter dito o último verso depois de não conseguir acompanhar o mestre, o que o deixou encantado. Ele exigiu um poema disso."
                            text ""
                            text "{i}\"Pare, por favor, ó, meu senhor —"
                            text "{i}Rapido falante, movente audacioso,"
                            text "{i}Organizador hábil — lento:"
                            text "{i}Eu ouço rápido demais.\""

                    if Memento == "Selene":
                        vbox spacing 10:
                            text "{i}{size=+2}Rabisco de caligrafia" xalign 0.5
                            text ""
                            text "Um epigrama escrito para Selena com uma caligrafia grosseira."
                            text ""
                            text "{i}\"A Lua está pálida, fora de foco, fisgada."
                            text "{i}A cidade anuvia as estrelas, enquanto o vapor cobre a lua,"
                            text "{i}Eu corro sob seu largo sorriso.\""


                if FileType == 'Artifacts':
                    if Artifact == "Wine":
                        vbox spacing 10:
                            text "{i}{size=+2}Garrafa de Vinho" xalign 0.5
                            text ""
                            text "Uma garrafa contendo vinho mágico que acelera a recuperação de Astério após ferimentos."
                            text "Nem o Mestre nem o prisioneiro são capazes de invocar este vinho especial por meios convencionais, a maneira exata de fazê-lo é atualmente desconhecida."
                            text "Em que ocasionaria alguém além de Astério bebendo o vinho também é desconhecido."
                            text ""
                            if not main_menu:
                                if BundleSacrifice == 'Hestia':
                                    text "Argos relutantemente entregou a garrafa de vinho em troca de um sacrifício para Héstia, a deusa da lareira e do lar, feito na lareira dentro do hotel."
                                elif BundleSacrifice == 'Hades':
                                    text "Argos relutantemente entregou a garrafa de vinho em troca de um sacrifício para Hades, senhor dos mortos, feito em sua estátua nos jardins do hotel."
                                elif BundleSacrifice == 'Hermes':
                                    text "Argos relutantemente entregou a garrafa de vinho em troca de um sacrifício para Hermes, mensageiro dos deuses, feito na bacia do alicerce do hotel."
                                elif BundleSacrifice == 'Zeus':
                                    text "Argos entregou a garrafa de vinho em troca de uma expedição para fazer um sacrifício a Zeus, rei dos deuses, na estátua em sua homenagem no topo de um planalto no vale."
                                elif BundleSacrifice == 'Athena':
                                    text "Argos entregou a garrafa de vinho em troca de uma expedição para fazer um sacrifício a Atena, deusa da sabedoria, na estátua em sua homenagem no todo de um planalto no vale."
                                else:
                                    text "A garrafa foi tirada de Argos à força."
                if FileType == 'Techs':
                    if Tech == "WiFi":
                        vbox spacing 10:
                            text "{i}{size=+2}Acesso à Internet" xalign 0.5
                            text ""
                            text "Através de uma combinação de contratos e esquemas, você conseguiu estabelecer uma conexão à internet dentro do hotel."
                            text "Tudo isso é possível pelo reaproveitamento de um santuário de Hermes no Alicerce do labirinto que estabelece uma conexão com o mundo exterior."
                            text "Você está atualmente usando um PSI uruguaio bastante lento e terá que pagá-los uma taxa, mas isto não deve ser um problema."
            vbar value YScrollValue("ct")
            
    if FileType != 'none':
        side "c r":
            area (40, 220+PlatAlign2 , 260, 420)
            viewport id "ctside":
                draggable True
                mousewheel True
                vbox spacing 20 xminimum 220:
                    if FileType == 'Contracts':
                        for contract in contractsList:
                            $displayName = contract['name']
                            $id = contract['id']
                            textbutton "{size=+4}[displayName]" action SetLocalVariable("Contract", id) xalign 0.5
                    elif FileType == 'Techs':
                        for tech in techsList:
                            $displayName = tech['name']
                            $id = tech['id']
                            textbutton "{size=+4}[displayName]" action SetLocalVariable("Tech", id) xalign 0.5
                    elif FileType == 'Mementos':
                        for memento in mementosList:
                            $displayName = memento['name']
                            $id = memento['id']
                            textbutton "{size=+4}[displayName]" action SetLocalVariable("Memento", id) xalign 0.5
                    elif FileType == 'Artifacts':
                        for artifact in artifactsList:
                            $displayName = artifact['name']
                            $id = artifact['id']
                            textbutton "{size=+4}[displayName]" action SetLocalVariable("Artifact", id) xalign 0.5
                    elif FileType == 'Profiles':
                        for profile in profilesList:
                            $displayName = profile['name']
                            $id = profile['id']
                            textbutton "{size=+4}[displayName]" action SetLocalVariable("Profile", id) xalign 0.5

            vbar value YScrollValue("ctside")
