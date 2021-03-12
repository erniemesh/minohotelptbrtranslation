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
                            text "Na tábua se lê:"
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
                            text "Na tábua se lê:"
                            text ""
                            text "{i}Titono era meu pai, sua era a mão a qual me ensinou a navegar nestas águas abundantes."
                            text "{i}Juntos, perseguimos e lançamos flechas contra auroques no solo avermelhado e úmido o qual fizemos nosso banquete."
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
                            text "Colunas carmesim ainda se encontram nos locais antigos de Creta, uma memória duraroura de uma época derradeira. O labiríntico Palácio de Cnossos, embora consumido e apodrecido, durou mais tempo que reis e deuses."
                            text "Esta tábua é decorada com padrões repetitivos de colunas, mas um exame minucioso revela traços de um raro e precioso tesouro pulverizado sobre ela: açafrão."
                            text "Na tábua se lê:"
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
                            text "Os tempos antigos eram governados pelo princípio de que a força faz o certo. Mulheres que desejavam impor sua vontade ao mundo tiveram que contar com subterfúgios e inteligência."
                            text "Esta tábua é decorada com uma única linha em sua parte inferior, a silhueta do Monte Egeão; o local onde, diz a lenda, Zeus foi criado."
                            text "Na tábua se lê:"
                            text ""
                            text "{i}Quando o verão chegou e o Rei Minos ainda não havia nos concedido sua bênção"
                            text "{i}uma jovem mulher entrou sorrateiramente em nossa tenda e me contou sobre o labirinto"
                            text "{i}— no pé de uma montanha, a mesma onde Zeus passou sua juventude —"
                            text "{i}onde encontraríamos um temível híbrido, um demônio nascido do caso da rainha com uma fera."
                            text ""
                            text "{i}Durante minhas tardes de colheita de açafrão, as esposas falaram-me de tal besta,"
                            text "{i}outrora conhecida como uma divindade da prosperidade exibida pelo Rei Minos,"
                            text "{i}trancado nos confins do labirinto depois de experimentar o canibalismo."
                            text "{i}Ele, disse a jovem, guarda o Lábris de Creta,"
                            text "{i}presente de Zeus para seu local de nascimento, bem no centro do labirinto."
                            text ""
                            text "{i}\"Busque o demônio almaldiçoado no coração do mundo,"
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
                            text "{i}{size=+2}Quinta Tábua: Demônio" xalign 0.5
                            text ""
                            text "Uma tábua de argila narrando o encontro de um homem com outro de natureza divina."
                            text "Para os gregos, ser um híbrido é ser um monstro. Os dois são indissociáveis."
                            text "Divino ou não, um híbrido é um ser abominável e repulsivo que boas pessoas fariam bem ao ostracizar."
                            text "Esta tábua é decorada com linhas labirínticas em suas margens."
                            text "Uma tábua de argila narrando uma intervenção de um jovem preocupado."
                            text "Na tábua se lê:"
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
                            text "{i}O demônio brincou conosco, nunca dando as caras."
                            text "{i}Eu temia que a fome tirasse minha vida e chorei pela de meu pai."
                            text ""
                            text "{i}No quarto dia, a criatura apareceu, o monstro híbrido de Pasífae."
                            text "{i}Não era o temível titã o qual me disseram que comia a carne de homens —"
                            text "{i}seu focinho rosa, tímidos chifres e olhos brilhantes eram os de um bezerro amamentado."
                            text ""
                            text "{i}Eu o desafiei para o combate, certo de que finalmente"
                            text "{i}teria um fim para este escárnio,"
                            text "{i}mas ele disparou por seus corredores intermináveis,"
                            text "{i}deixando para trás apenas o bater de cascos entrando em silêncio."

                    if Memento == "Tablet6":
                        vbox spacing 10:
                            text "{i}{size=+2}Sexta Tábua: Criança" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando a hospitalidade de uma criança."
                            text "Os gregos tinham muitos costumes e normas as quais ditavam como um hóspede deveria ser tratado. Naqueles tempos antigos, deuses disfarçados andavam entre os homens, então era esperado que um anfitrião tratasse seus convidados com o respeito que o divino merecia."
                            text "Trazer desgraça para a casa de um anfitrião era uma atrocidade imperdoável que certamente inspiraria maldições sobre a linhagem de uma pessoa."
                            text "Esta tábua é adornada com representações de um templo, ou talvez um santuário. Um touro massacrado encontra-se em sua entrada."
                            text "Na tábua se lê:"
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
                            text "{i}Eu te receberia carinhosamente — não fosse pelas armas em teu punho."
                            text "{i}Diga-me, por que levantarias teu braço contra os deuses?\""
                            text ""
                            text "{i}Com a pouca voz que restou em minha rouca garganta, eu respondi:"
                            text "{i}\"É contra a insensatez divina que me volto, não aos próprios deuses."
                            text "{i}Eu sou Laomedonte, filho de Titono, por sua vez, marido da deusa Eos;"
                            text "{i}esta casca que carregou é o que ela deixou para trás. Ela implorou a Zeus para torná-lo imortal"
                            text "{i}mas em seu tolo torpor, não pediu por juventude eterna."
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
                            text "Na tábua se lê:"
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
                            text "Na tábua se lê:"
                            text ""
                            text "{i}Por três dias e três noites, me recuperei de minhas queimaduras."
                            text "{i}O híbrido voluntariamente assumiu o papel de cuidador de meu pai e de mim."
                            text "{i}Que hospitalidade ele mostrou, minhas feridas ele limpou,"
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
                            text "{i}Que direito tenho eu de retirar o que os Crônidas deram?\""
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
                            text "Na tábua se lê:"
                            text ""
                            text "{i}Muitas noites passamos naquele santuário carmesim,"
                            text "{i}confortados pela lira do menino e pela chama da bacia."
                            text "{i}Antes e depois de cada refeição, Astério pagaria a Héstia seu tributo e além,"
                            text "{i}às vezes passando fome por uma glória maior da deusa."
                            text ""
                            text "{i}Noite após noite eu implorei por sua ajuda, mas ele não aceitou."
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
                            text "{i}que você cumprimentou os pescadores para comprar sua pesca fresca?\""
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
                            text "{i}Eu encontro companheirismo entre elas, traçando-as com um dedo,"
                            text "{i}e dentro de minha própria mente da qual ninguém pode me despojar."
                            text "{i}Antes de sua chegada, eu pensei; do amanhecer ao anoitecer,"
                            text "{i}minha mente correu com histórias e possibilidades."
                            text "{i}O mar eu não verei até que meu pai me alivie de meu dever,"
                            text "{i}mas sua espuma posso para sempre manter na palma de minha mente.\""

                    if Memento == "Tablet10":
                        vbox spacing 10:
                            text "{i}{size=+2}Décima Tábua: Espuma do Mar" xalign 0.5
                            text ""
                            text "Uma tábua de argila revelando um bastardo tentando um jovem devoto a se afastar para longe de seu dever."
                            text "Creta não é conhecida por suas cobras venenosas. Não é nenhuma surpresa, então, que aquele que tentaria um príncipe a se afastar de seu dever veio do outro lado do mar."
                            text "Esta tábua é adornada com padrões parecidos com ondas."
                            text "Na tábua se lê:"
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
                            text "Esta tábua de argila é adornada com padrões decorativos de flores, que racharam e se deformaram durante o processo de cozimento."
                            text "Na tábua se lê:"
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
                            text "{i}um único dia de alegria enquanto vasculhamos estas praias."
                            text "{i}Mas este não é o caso; seu dever é muito grande."
                            text "{i}Então é com pesar que devo anunciar:"
                            text "{i}ao amanhecer, eu e meu pai deixaremos"
                            text "{i}o labirinto e os solos de Creta, para algum lugar,"
                            text "{i}além destas águas turvas deve haver uma outra,"
                            text "{i}inspirado pelos Olímpios, os quais podem encerrar nossa jornada.\""
                            text ""
                            text "{i}Astério expectante do amanhecer interrompeu sua música e fechou os olhos."
                            text "{i}O pesar parecia consumi-lo; um nó se formou em sua garganta."
                            text "{i}Quando as palavras o deixaram, elas estavam roucas e vacilantes."
                            text "{i}\"Você conhece as artes do combate, não?"
                            text "{i}Seu pai, em seu auge, lhe ensinou sobre o afiamento de uma lâmina."
                            text "{i}Quanto tempo levaria para eu reunir o poder"
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
                            text "Na tábua se lê:"
                            text ""
                            text "{i}Pristine-horned Asterion kept his word; our afternoons were spent sparring"
                            text "{i}much like my own father taught me the balance and slashes of each weapon."
                            text "{i}For three winters Daedalus' labyrinth became my home."
                            text "{i}The hybrid grew before my eyes, his once fine features"
                            text "{i}acquired a bull's might — fear he would strike among foes"
                            text "{i}were it not for his forever childish pink snout."
                            text "{i}Asterion of Steppe-Wide Back, that is how I came to call him"
                            text "{i}in his brilliant warrior's glory."
                            text ""
                            text "{i}Still, there was not a night in which his lyre went unplucked,"
                            text "{i}nor one when Hestia's fire on the basin starved for what little meat we had"
                            text "{i}and much less a night when our blood went unspilled as we clashed armaments."
                            text "{i}And so did I learn of Asterion's foul blood — a fetid concoction,"
                            text "{i}both blood-red and ichor-black, proof of the hybrid's profane origins."
                            text "{i}It bellowed when set aflame, and what great fire it begat."
                            text "{i}T'was fine sacrifice for the basin, more so for Hestia with her taste for oxen meat."
                            text "{i}Once spilt it hardened into a brittle, foul stone, much like a wound's clot"
                            text "{i}but firm enough to pass off as stone spilled from a volcano."
                            text "{i}Its scent brought revulsion, but fine kindling it was for the flame."
                            text "{i}The labyrinth's unending, shifting hallways were our training grounds"
                            text "{i}for the boy would not taint the shrine with his fetid nature."

                    if Memento == "Tablet13":
                        vbox spacing 10:
                            text "{i}{size=+2}Thirteenth Tablet: Dying Embers" xalign 0.5
                            text ""
                            text "A clay tablet revealing the hybrid's despondency."
                            text "One must not lock the door if the prisoner's spirit is broken."
                            text "This clay tablet bears no decorations."
                            text "The tablet reads:"
                            text ""
                            text "{i}After Asterion played father's lullaby we would talk in whispers well into the night."
                            text "{i}We would swap heroes's tales and constellations, exchanging legends from our lands."
                            text "{i}\"Tell me, boy, did you hear tales of the villages beyond this sea?"
                            text "{i}My father was once a prince to a fine city-state, before the gods' folly plucked his mind."
                            text "{i}Does it please you the thought of leaving this labyrinth and journeying north,"
                            text "{i}should your father ever relieve you of this shrine-tending duty?\""
                            text ""
                            text "{i}The boy dallied before answering, when he did his voice cracked like the embers."
                            text "{i}\"To see beyond these walls and sea? Nay, the stories I heard very few,"
                            text "{i}but the thought, to cross the ocean, how could I find it pleasing?"
                            text "{i}Crete is the cradle of man, it stands tall above all others and shall outlive them all,"
                            text "{i}what reason would one have to abandon its bosom?"
                            text "{i}Alas, the thought alone is foolish, for never will father relieve me of duty."
                            text "{i}I may leave these walls, but there shall be another labyrinth for me"
                            text "{i}once I prove myself capable of wielding the labrys.\""
                            text ""
                            text "{i}\"Forget Crete, then, does the thought of freedom entice you?"
                            text "{i}There may be no land like this, where the snakes know no ill words"
                            text "{i}and the wild goats have such rich flesh, but think of a place where freedom is yours.\""
                            text ""
                            text "{i}And like dried wood, abandoned for years, his voice cracked among the embers."
                            text "{i}\"Banish the thought, my lord. See you not that I am a beast?"
                            text "{i}My will scarcely matters in this affair, whether or not I wish for freedom"
                            text "{i}how would I cross the raging sea? If I knew how to sail, still I have no means to do it."
                            text "{i}Had I the crew and ship, would they not vanquish me for the sin I am?"
                            text "{i}And if I ever did cross the sea, what awaits me there? At least here"
                            text "{i}I have the hope of seeing my family once more, for their next visit."
                            text "{i}Surely they will soon arrive, my siblings and I shall hunt together."
                            text "{i}There is no future anywhere else for me, my lord,"
                            text "{i}even if I fear this land too bears nothing for me except dying embers.\""

                    if Memento == "Tablet14":
                        vbox spacing 10:
                            text "{i}{size=+2}Fourteenth Tablet: Redeemer" xalign 0.5
                            text ""
                            text "A clay tablet revealing one of many tragedies leading to a boy's demise."
                            text "What awaits the sacrificed beyond his mortal coil? One can only wonder."
                            text "This clay tablet is adorned with flower motifs, which cracked and warped during the cooking process."
                            text "The tablet reads:"
                            text ""
                            text "{i}One day the boy found a flower growing through a crack on the stone floor,"
                            text "{i}the first he had seen in all those winters since his banishment."
                            text "{i}What pain was in his eyes, knowing it should not be plucked"
                            text "{i}and having to journey the hallways merely to glance upon it!"
                            text "{i}Endless was his sorrow when harsh rain rotted its roots"
                            text "{i}but he found solace in offering it to Hestia as sacrifice."
                            text ""
                            text "{i}It had been three winters since my arrival at this island,"
                            text "{i}the hybrid had grown into a fine, capable warrior under my tutelage."
                            text "{i}It would not be long before he would be able to raise the labrys"
                            text "{i}and put an end to my father's suffering."
                            text ""
                            text "{i}During one of the chilly nights when we huddled against the basin"
                            text "{i}when the wood let out a foul, darkened smoke that brought tears to one's eyes"
                            text "{i}he asked me if a flower felt joy upon being plucked and offered to the gods."
                            text "{i}At times this grown creature spoke with the innocence of a child,"
                            text "{i}that soft voice which we all learned to abandon perhaps too early."
                            text "{i}I spoke then with the pain and pity of a father consoling his son upon a dog's death:"
                            text "{i}\"There is no greater honor than to be offered to the twelve, child."
                            text "{i}For whatever weakness it or any being ever showed is redeemed"
                            text "{i}when one's life is thus plucked and made sacred."
                            text "{i}Soon we shall put an end to my father's pain, then you must see it"
                            text "{i}as a liberation from heavy shackles, and see yourself as his cherished redeemer.\""
                            text ""
                            text "{i}That was the last night in which the hybrid played his lyre; a string snapped then."
                            text "{i}Asterion Thread-Cutter cradled the instrument against his chest"
                            text "{i}and hummed instead until drowsiness fell upon our eyes."
                            text "{i}Before we retreated to our straw mats, however, he said"
                            text "{i}\"Is there warmth in your heart to believe that I, too,"
                            text "{i}shall one day be blessed with a redeemer? One crossing the sea to liberate me"
                            text "{i}from these oh so familiar shackles that bear the signs of gods?"
                            text "{i}Will one day I be redeemed from my birth, shall I fly free"
                            text "{i}like Ikaros and Daedalus did, away from this wretched land?\""
                            text ""
                            text "{i}I felt then the knife hidden among his words, about to slit my own throat as well."
                            text "{i}What could I say? I gathered my embers, all I could muster, and said:"
                            text "{i}\"You shall be redeemed no doubt, and then you will see the flowers"
                            text "{i}growing outside these crimson walls of Daedalus."
                            text "{i}No sea is too great, no curse too foul, to stop one from achieving salvation,"
                            text "{i}above all else one who would have the mercy to free an ailing, accursed man.\""
                            text ""
                            text "{i}And those words, today I regret them most,"
                            text "{i}for what wretched nightmare did I plant in him?"

                    if Memento == "Tablet15":
                        vbox spacing 10:
                            text "{i}{size=+2}Fifteenth Tablet: Folly" xalign 0.5
                            text ""
                            text "A clay tablet revealing a prisoner's last shred of hope."
                            text "One must snuff the flames of those around him to realize his will. A prisoner must be kept shackled to fulfill his mission."
                            text "And yet, some embers have a second life, revealed when the layer of soot flies away to reveal a still red heart."
                            text "This tablet bearns no ornaments."
                            text "The tablet reads:"
                            text ""
                            text "{i}Spring arrived, but winter persisted in the hybrid's heart."
                            text "{i}His breath grew shorter and a cough took root in his lungs,"
                            text "{i}still I pulled him from his bedroll everyday to learn warcraft"
                            text "{i}so he may release father from his accursed existence."
                            text "{i}A fire simmered on my lungs and I too grew short of breath,"
                            text "{i}although mine was not of malaise; it was my despair."
                            text "{i}Despite my want for silence, the hybrid did speak between our matches."
                            text ""
                            text "{i}\"When the day comes for my redeemer to liberate me, how will he know"
                            text "{i}to turn left three times after the patio with the bull-leaping mural?"
                            text "{i}Will the gods bless his mind with the eyesight of a hawk flying above?"
                            text "{i}Will Hera send snakes to guide him down to the shrine I protect?"
                            text "{i}Perhaps my savior will follow the same footsteps as thee,"
                            text "{i}first seeking the house of my birth to learn of the labyrinth's heart.\""
                            text ""
                            text "{i}I motioned for us to restart our combat, but he did not budge."
                            text "{i}I proceeded then to speak the honeyed words he so wished to hear."
                            text "{i}\"Whatever you will, whatever you wish, for such a pious youth"
                            text "{i}I know the gods shall realize your request; for few are those"
                            text "{i}with their ichor flowing through his veins and with such a loyal disposition."
                            text "{i}Upon the completion of our ritual, when my father's thread is ruptured,"
                            text "{i}surely they will send Nike herself to guide a redeemer to thee.\""
                            text ""
                            text "{i}\"The ritual, indeed,\" mumbled the fiend and I noticed again the cracking of embers."
                            text "{i}\"Iron-willed Tithonus, would you hear my plea? There is one wish"
                            text "{i}my heart yearns for. When you leave Daedalus' home"
                            text "{i}would you return to my birthplace and tell my family a secret?"
                            text "{i}Tell them the labyrinth's pathways yield gently if one lays behind"
                            text "{i}a strand of wool yarn as they brave it."
                            text "{i}With this knowledge my savior will surely find his way"
                            text "{i}to the heart where I await him."
                            text "{i}Although, if too would you listen to my shameful confession,"
                            text "{i}as soon as the wish for my redeemer's arrival took hold so did"
                            text "{i}a silly idea I cannot shake. In my dreams I see myself leaving"
                            text "{i}Daedalus' home, seeing for myself the fields of crocuses"
                            text "{i}and the sea's foamy water, the same from which my progenitor came."
                            text "{i}My heart races when I think of a redeemer's arrival,"
                            text "{i}but painfully so, as if somehow I am meant to avert the idea."
                            text "{i}For the first time in all these years, my friend, I wish"
                            text "{i}to abandon my post and leave this labyrinth."
                            text "{i}Mount Aegaeon's caves would provide me safe haven,"
                            text "{i}there are many unknown glades in this island"
                            text "{i}where I could find comfort, and perhaps I could barter what little I have"
                            text "{i}in exchange for safe passage across the sea to lands unknown."
                            text "{i}Tell me, Tithonus, is this idea not shameful and rotten?"
                            text "{i}To abandon my duty to the gods, leave these crimson walls"
                            text "{i}at this very instant. Merely saying so quickens my heart."
                            text "{i}And as cowardly as I know it is, tonight I believe I could and should do it."
                            text "{i}Tell me, friend, should I? Abandon duty and grasp"
                            text "{i}this cowardly salvation with my own two hands?\""
                            text ""
                            text "{i}That night the basin's flame died for the first time since my arrival winters before."
                            text "{i}My father awoke at midnight and called my name, amidst his fog of senility he asked"
                            text "{i}\"Who is this sobbing young man I hear, and why are his pleas so desperate?"
                            text "{i}Son, where are we and what cursed fate fell on this boy"
                            text "{i}for his wails to inspire such sorrow in me?"
                            text "{i}Is there not a thing we can do to grant him comfort?\""
                            text ""
                            text "{i}And to father I said \"Nay, vanquish the memory from your mind, father,"
                            text "{i}the hybrid shall soon fulfill his duty and peace will come to thee.\""
                            text ""
                            text "{i}A price must be paid to do what is right, all men know."
                            text "{i}To bring death unto a defenseless, willing victim leaves a stain on"
                            text "{i}one's soul, an indelible weight like the one which crushes Atlas."
                            text "{i}The hybrid bore the weight of my father's end and I of his."
                            text "{i}A man must be ready to lead others unto death to do what is right."
                            text "{i}I know this old wisdom, and yet why can I not contain my racing heart?"
                            text "{i}How much wood must I lay under his pyre to atone for my impiety?"

                    if Memento == "Tablet16":
                        vbox spacing 10:
                            text "{i}{size=+2}Sixteenth Tablet: Ritual" xalign 0.5
                            text ""
                            text "A clay tablet depicting a crime against divine order."
                            text "To no mortal is given the right to remove the eternity which the Olympians granted. He who rises against divine order is cursed with a fate most foul."
                            text "The tablet is adorned with the depiction of an old man's face. The artist tried to make his eyes peaceful, but the process of cooking the tablets gave him a horrified expression, befitting of the curse unleashed by his killing."
                            text "The tablet reads:"
                            text ""
                            text "{i}His name was Tithonus, he was my father."
                            text "{i}At the apex of his life, when I was at the cusp of my manhood,"
                            text "{i}father was spirited away by Eos, witless goddess of dawn."
                            text "{i}Zeus made him undying, but not forever youthful."
                            text "{i}His mind withered, his body dried into a husk,"
                            text "{i}yet Thanatos would not embrace him, nor would"
                            text "{i}Hermes Psychopompos lead him to the shores of Styx."
                            text ""
                            text "{i}With his husk strapped to my back I crossed the sea to the land of Crete"
                            text "{i}where a crescent moon even the Fates feared was hidden."
                            text "{i}The labrys' guardian found us inside the home of Daedalus,"
                            text "{i}he nursed us back to health despite his fear of the axe."
                            text "{i}I persuaded him into granting my father mercy"
                            text "{i}for only those with a touch of the divine may wield the Thread-Cutter."
                            text ""
                            text "{i}At the heart of the labyrinth was a shrine to the gods and"
                            text "{i}for over seven winters a fire burned inside it, on a wide basin."
                            text "{i}The flame I vanquished with my words, and seven nights later"
                            text "{i}we placed father's neck at the basin's rim."
                            text "{i}The labrys cracked the stone like thunder shakes the mind"
                            text "{i}and so it cut my father's thread, the one which the Fates would not touch."
                            text "{i}His abandoned vessel leaned sideways, like a child seeking a mother's shoulder"
                            text "{i}to drift off into sleep during a long carriage journey."
                            text ""
                            text "{i}In his old age my father loved the scent of saffron, even if his appetite had nearly ceased."
                            text "{i}Honey would make him smile, at times laugh. When I held his hand"
                            text "{i}his fingers would intertwine with mine even if his mind was gone."
                            text ""
                            text "{i}A black ichor flowed from his wound to the basin. There we made his pyre."
                            text "{i}As the flame licked and kissed father's abandoned vessel"
                            text "{i}the hybrid hummed for his lyre no longer had the strings to sing."
                            text ""
                            text "{i}The fire did not cleanse the basin, nor did it heal its cracks."
                            text "{i}The shrine took on an indelibly fetid stench, inside it nightmarish shadows"
                            text "{i}would crawl at night, moaning and laughing."
                            text ""
                            text "{i}\"The shrine is profaned,\" said Asterion while I made preparations for my departure."
                            text "{i}\"It is no longer a place for worship or sacrifice. And the labrys,"
                            text "{i}that which I was sworn to protect, Tithonus blood washes not from it."
                            text "{i}What shall I do, Laomedon, how may I wash this blasphemy from my hands?\""
                            text ""
                            text "{i}I had no answer for him, and no sweet words of mine could distract him."
                            text "{i}When I left the labyrinth's heart he stayed behind,"
                            text "{i}\"I shall await my redeemer then, as the Fates have woven."
                            text "{i}Still, will you visit me, Laomedon, to keep my loneliness at bay?\""

                    if Memento == "Tablet17":
                        vbox spacing 10:
                            text "{i}{size=+2}Seventeenth Tablet: Pyre" xalign 0.5
                            text ""
                            text "A clay tablet revealing a prisoner's liberation."
                            text "In face of death one would do well to spare the words."
                            text "A flame, burning on a basin, adorns this tablet's bottom. The margins are lined with circles, presumably representing coins."
                            text "The tablet reads:"
                            text ""
                            text "{i}He was Asterion, son of Queen Pasiphae and raised by King Minos."
                            text "{i}He was sired by Poseidon's white bull with the aid of crafty Daedalus."
                            text "{i}He who was seafoam-haired, pristine-horned, blessed with Hera's gaze,"
                            text "{i}of steppe-wide back and forever dawn-awaiting,"
                            text "{i}liberated my father from unbearable shackles"
                            text "{i}and in so doing took the weight of his curse."
                            text "{i}Together we bled ichor on the god's basin and"
                            text "{i}for our infinite hubris incurred their wrath, forever more."
                            text "{i}I remained in Crete but did not see the labyrinth's crimson walls"
                            text "{i}until word came of an Athenian warrior favored by Ariadne,"
                            text "{i}Loud-Bellowing Asterion's sibling. She told him of the secret"
                            text "{i}I delivered, according to the hybrid's wishes"
                            text "{i}— but in truth she knew it already, for Daedalus left her the knowledge."
                            text "{i}The Athenian ventured the labyrinth with a ball of yarn,"
                            text "{i}there he found his mark, the supposed fearsome beast."
                            text ""
                            text "{i}The Palace of Knossos will have you believe torrid-born Asterion"
                            text "{i}fought for his life against the invader's might."
                            text "{i}But I ran to the labyrinth as soon as I heard word"
                            text "{i}and found once more the cracked basin filled with dark and red."
                            text "{i}His body lay on his side, in a headless slumber,"
                            text "{i}with the Thread-cutter labrys at his hooves."
                            text "{i}Indeed, his redeemer had arrived and liberated him"
                            text "{i}as, I tell myself, the Fates themselves wished."
                            text ""
                            text "{i}I should believe he is now freed from his torrid lot in life,"
                            text "{i}that he shall find peace among his adoptive descendant,"
                            text "{i}virtuous King Minos of Crete who founded this very country."
                            text "{i}But why am I consumed by sorrow and an ineffable weight?"
                            text "{i}I look at his remains and what wrath fills me to see"
                            text "{i}that the Athenian took my friend's horn as trophy."
                            text "{i}The cursed labrys, Hephaistos' crescent moons, he left behind"
                            text "{i}now stained with godly and mortal fluid alike."
                            text ""
                            text "{i}King Minos' guards arrived as I completed his pyre."
                            text "{i}They did not stop me, in fact gathered wood they did"
                            text "{i}but the pristine-horned one's last shred of ivory they took back to the king."
                            text "{i}A gold coin I left under my friend's tongue, to appease Charon."
                            text "{i}On the basin he faithfully tended he departed from this land."

                    if Memento == "Tablet18":
                        vbox spacing 10:
                            text "{i}{size=+2}Eighteenth Tablet: Skyros" xalign 0.5
                            text ""
                            text "A clay tablet revealing an ominous fate."
                            text "A redeemer takes on the shackles of those he liberates. That unbroken chain extends from the birth of mankind to this very day."
                            text "None are spared."
                            text "This tablet bears no ornaments."
                            text "The tablet reads:"
                            text ""
                            text "{i}I continue with my journey, now that my heart belongs to no land."
                            text "{i}Crete I shall leave behind to seek a place which soothes"
                            text "{i}this unyielding wrath in my bosom."
                            text "{i}I look to the northern sea and remember then my father's legacy,"
                            text "{i}that he was close indeed to the monarch of Skyros."
                            text "{i}It is as if the Fates themselves call me there"
                            text "{i}and I have no doubt their intention is for me to find my redeemer"
                            text "{i}or perhaps to become one myself."
                            text ""
                            text "{i}This world's starry sky survived all the star-vanquishing dawns"
                            text "{i}and shall withstand them for ages more."
                            text "{i}The starry sky and sins of men went on,"
                            text "{i}Asterion did not."

                    if Memento == "TypewriterScrap":
                        vbox spacing 10:
                            text "{i}{size=+2}Typewriter scrap" xalign 0.5
                            text ""
                            text "A crumpled up piece of paper found by your exploration team."
                            text "It reads:"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}AqpqpqpqQPQPQP qaZxswed W4ITINGS WRITings nineteen eightee nnnnnnnn"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}asteriup ASTERION"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}TYPERITE minotaUR labyrint enclosu plsklmdv skwjekmw"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}services"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}continue"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}lonelier"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}violence"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}sleepier"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}progress"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}receding"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}peerless"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}mysquare"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}S E R V I C E S"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}L E N C E S L C"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}O S R E C E E O"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I S R L E D E N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}V E E S S I P T"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}R R E P G N I I"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}E G O R P R E N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I L E N O L E U"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}S E R V I C E S ·"
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
                            text "Showing this to the minotaur makes his ears droop and his shoulders shrink."
                            text "He explains that a previous master had brought some publications and \"the thing with the buttons to imprint letters\"."
                            text "Upon seeing that all the letters were the same size, he tried, in his own words, to \"make a square of words\"."
                            text "He wishes not to be reminded."

                    if Memento == "PoemNotebook":
                        vbox spacing 10:
                            text "{i}{size=+2}Goatskin-bound notebook" xalign 0.5
                            text ""
                            text "A tiny notebook, a tad smaller than a human's hand."
                            text "The same poem is written in its pages a dozen times, with diminutive variations over each version. At the end there is one final scrawl, different from all others."
                            text "The handwriting is poor and cramped."
                            text ""
                            text "{u}CHOREGOS"
                            text "{i}        A grain of sand has led my mind far back"
                            text "{i}wherever memory could choke my throat"
                            text "{i}or blind my sight. I'm helpless before her."
                            text "{i}        Too open a mind, too keen to recall,"
                            text "{i}and trouble imprints eidetically there"
                            text "{i}wherever it can. A hug can be held"
                            text "{i}in mind, but blows leave tender bruises, scars,"
                            text "{i}the ugliest scars of distrusting friends:"
                            text "{i}Of ulterior suspicion all based"
                            text "{i}on off-hand ribs, ignorant sleights and jolts"
                            text "{i}the other half forgot. If only I"
                            text "{i}had not this stone-sure trap between my horns."
                            text "{i}I can't help but hate my position, 'blest'"
                            text "{i}lone patriot of tense Mnemosyne."
                            text ""
                            text "{u}CHORUS"
                            text "{i}        \"What nonsense: bland indulgence, whining, and--\""
                            text "{i}        It's all cemented in; what's light just froths"
                            text "{i}and floats up over top, bottom stagnant"
                            text "{i}and suffocating: Still. This caustic rot"
                            text "{i}bears not a use: it raises none like yeast"
                            text "{i}nor delights like drunkenness. Why keep on?"
                            text "{i}        \"Just stop. This endeavor just escapes you.\""
                            text ""
                            text "{u}CHOREGOS"
                            text "{i}        A thicker skin is necessary, but"
                            text "{i}perhaps with fewer gatekeepers to track"
                            text "{i}who earned their self-esteem already, then"
                            text "{i}more would get strength and grit and earnest self"
                            text "{i}sufficiency. It takes only one time:"
                            text "{i}one rightly placed blow hobbles the balance."
                            text "{i}        No strength is gained from craven exposé"
                            text "{i}and testing jabs when wounds are open, sore,"
                            text "{i}and bleeding still. A coagulant, or"
                            text "{i}astringent tonic needed — not friction,"
                            text "{i}blood-letting, bones re-set and bound, toxic"
                            text "{i}applied in 'therapeutic' doses. The hope"
                            text "{i}is hypertrophy — but not yet — but soon—!—? ..."
                            text ""
                            text "{u}CHORUS"
                            text "{i}        \"What nonsense: bland indulgence, whining, and —\""
                            text "{i}        A pace that functions, lasts and grows more strong"
                            text "{i}elusive is. That's all that's simple here."
                            text "{i}What growth not stymied tortures by, is razed"
                            text "{i}by just as close as possible a source."
                            text "{i}A mother's madness inherited here?"
                            text "{i}        \"Just stop. This endeavor just escapes you.\""
                            text ""
                            text ""
                            text "{i}        \"I know I offer precious little, but"
                            text "{i}what little offered: precious is, I hope.\""

                    if Memento == "RockCarving":
                        vbox spacing 10:
                            text "{i}{size=+2}Petroglyph" xalign 0.5
                            text ""
                            text "A slab of rock with writing engraved on it found in the Valley."
                            text "Some parts of the rock are missing, so it's impossible to read the full poem."
                            text ""
                            text "{i}\"Cry, oh great Allmother, sorrow so deep that no Parnassan Muse would prepare ere a thought to this plea made so ----"
                            text "{i}Call, oh Poseidon, a Muse much more hardy and tougher than ----"
                            text "{i}Please, oh Melpomene, chant weary lines through red Knossos halls, rich ----"
                            text "{i}Thalia, come not, ----\""

                    if Memento == "Agape":
                        vbox spacing 10:
                            text "{i}{size=+2}Agape, Eros, Phileos" xalign 0.5
                            text ""
                            text "An epigram written to a Roman Pagan or gnostic, pontificating on their conquest of the Greeks."
                            text "As usual with all foreign written language in the labyrinth, the letters shift as you focus your eyes on them, making the piece of parchment legible."
                            text "However, you could swear that some of the glyphs that all now refer to the same words looked different to you a moment ago."
                            text ""
                            text "{i}\"    'But love's not love it's more like love,' he told"
                            text "{i}me, using words from my own tongue, from us"
                            text "{i}imported. What compartmentalizing"
                            text "{i}these Romans do! They speak as if the dusk"
                            text "{i}was not yet still the sun!"
                            text ""
                            text "{i}    They took our gods,"
                            text "{i}remade, refashioned, mixed up meanings, names —"
                            text "{i}a pantheon of mush. This first, but then"
                            text "{i}these men with garum doused and drowned our food."
                            text "{i}And now, they lecture me on our own words…\""

                    if Memento == "FieldWork":
                        vbox spacing 10:
                            text "{i}{size=+2}Torn illustrated page" xalign 0.5
                            text ""
                            text "An old, yellowed sheet of paper with one of its edges ripped off. You assume it's a page torn off an old book."
                            text "The page is adorned with an illustration of a minotaur ploughing a field, in colorful blue and gold ink."
                            if not main_menu:
                                if player_background in ['humanities', 'arts']:
                                    text "An poem is written in red ink below the illustration. You recognize it is written using the Greek alphabet; this, compounded with the style and framing of the illustration, would date this page around the Bizantine era."
                                else:
                                    text "An poem is written in red ink below the illustration. It is written in a language foreign to you, but the letters shift as you focus your eyes, making the piece of parchment legible."
                            else:
                                text "An poem is written in red ink below the illustration. It is written in a language foreign to you, but the letters shift as you focus your eyes, making the piece of parchment legible."
                            text "It's an ode to field work, rather than carousing:"
                            text ""
                            text "{i}    \"Wild oats! What use is there in that? What makes"
                            text "{i}a man himself is well worked usefulness"
                            text "{i}in fields of help and aid and produce made."
                            text "{i}    Well tended, these halls maybe rows become"
                            text "{i}at whim of Master. Fertile fields extend"
                            text "{i}with hoof-trod handiwork, well-roofed with sky,"
                            text "{i}    through halls of wheat and corn and oat that not"
                            text "{i}a Perses, dull, could stand to leave untilled."
                            text "{i}The readied field willed good, not wild, by hand.\""

                    if Memento == "FoldedNote":
                        vbox spacing 10:
                            text "{i}{size=+2}Folded Note" xalign 0.5
                            text ""
                            text "An epigram written to a wordy, forward, active, and mercurial former master."
                            text "When asking Asterion about the note, he sadly explains that he recalls having said the last line after not being able to keep up with the master, which delighted him. He demanded a poem out of it."
                            text ""
                            text "{i}\"Stop, please, oh Lord of mine —"
                            text "{i}Fast speaker, mover bold,"
                            text "{i}Deft organizer — slow:"
                            text "{i}I listen far too fast.\""

                    if Memento == "Selene":
                        vbox spacing 10:
                            text "{i}{size=+2}Handwritten scrawl" xalign 0.5
                            text ""
                            text "An epigram written to Selene with crude handwriting."
                            text ""
                            text "{i}\"The Moon is pallid, out-of-focus, hook'd."
                            text "{i}The city clouds the stars, while vapour veils the moon,"
                            text "{i}I rush under its side-long smile.\""


                if FileType == 'Artifacts':
                    if Artifact == "Wine":
                        vbox spacing 10:
                            text "{i}{size=+2}Wine bottle" xalign 0.5
                            text ""
                            text "A bottle containing magical wine that speeds up Asterion's recovery after injuries."
                            text "Neither the Master nor the prisoner are capable of summoning this special wine through regular means, the exact way to do so is currently unknown."
                            text "What would anyone but Asterion drinking the wine do is also unknown."
                            text ""
                            if not main_menu:
                                if BundleSacrifice == 'Hestia':
                                    text "Argos reluctantly gave up the wine bottle in exchange for making a sacrifice to Hestia, goddess of hearth and home, at the fireplace inside the hotel."
                                elif BundleSacrifice == 'Hades':
                                    text "Argos reluctantly gave up the wine bottle in exchange for making a sacrifice to Hades, lord of the dead, at his statue in the hotel gardens."
                                elif BundleSacrifice == 'Hermes':
                                    text "Argos reluctantly gave up the wine bottle in exchange for making a sacrifice to Hermes, messenger of the gods, at the basin in the hotel's bedrock."
                                elif BundleSacrifice == 'Zeus':
                                    text "Argos handed the wine bottle over in exchange for arranging an expedition to make a sacrifice to Zeus, king of the gods, at a statue in his honor atop a plateau in the valley."
                                elif BundleSacrifice == 'Athena':
                                    text "Argos handed the wine bottle over in exchange for arranging an expedition to make a sacrifice to Athena, goddess of wisdom, at a statue in her honor atop a plateau in the valley."
                                else:
                                    text "The bottle was taken by force from Argos."
                if FileType == 'Techs':
                    if Tech == "WiFi":
                        vbox spacing 10:
                            text "{i}{size=+2}Internet Access" xalign 0.5
                            text ""
                            text "Through a combination of contracts and schematics, you have managed to establish an internet connection inside the hotel."
                            text "This is all made possible by repurposing a shrine of Hermes in the Bedrock of the labyrinth that establishes a connection to the outside world."
                            text "You are currently using a rather slow Uruguayan ISP and will have to pay them a fee, but that should not be an issue."
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
