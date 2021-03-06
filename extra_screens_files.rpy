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
                            text "{i}{size=+2}Senten??a de Asterion" xalign 0.5
                            text ""
                            text "{i}Por meio deste, os deuses do Olimpo sentenciam o Prisioneiro Ast??rio ?? dana????o eterna por sua mansid??o e covardia em face ?? adversidade."
                            text "{i}Com esta senten??a, sua pris??o ?? criada, um Labirinto nascido do icor dos deuses."
                            text "{i}O Labirinto deve acolher mortais perdidos sem nenhum lugar para ir. Entre eles, um Carcereiro ser?? escolhido para comandar e reescrever o dom??nio."
                            text "{i}A miss??o do Carcereiro e do Labirinto ?? garantir a tortura eterna do Prisioneiro."
                            text "{i}O Carcereiro gozar?? de poder e liberdade para reescrever o Labirinto da forma que melhor enaltecer seu ponto de vista."
                            text "{i}Ast??rio de Creta, filho adotivo do Rei Minos, e cada gota de seu sangue blasfemo ??, por meio deste, condenado ao Labirinto."
                            text "{i}Por meio deste decreto, a vontade dos deuses ?? realizada."
                    elif Contract == "Servitude":
                        vbox spacing 10:
                            text "{i}{size=+2}Juramento de Servid??o de Ast??rio" xalign 0.5
                            text ""
                            text "{i}Pelas provis??es sob o Estatuto de Jos??, o Misericordioso, o Prisioneiro Ast??rio promete lealdade e servid??o ao Mestre do Labirinto."
                            text "{i}O Prisioneiro ?? institu??do Zelador do Hotel acima do vale e lhe ?? legado o poder de realizar a vontade do Mestre."
                            text "{i}O Mestre, por sua vez, restringe o Labirinto, proibindo suas entidades maliciosas de deixarem dito vale."
                            text "{i}O dom??nio foi projetado para torturar o Prisioneiro e, de fato, sua miss??o deve ser cumprida. O Prisioneiro carregar?? o fardo da servid??o, mas n??o sofrer?? a ira do Labirinto dentro do territ??rio do Hotel."
                            text "{i}O Prisioneiro, amparado pela vontade de seu Mestre, fica seguro desde que cumpra seu dever, sob os termos do Estatuto"

                    elif Contract == "ArgosContract":
                        vbox spacing 10:
                            text "{i}{size=+2}Contrato de Argos" xalign 0.5
                            text ""
                            text "{i}Este documento compromete o Mestre do Labirinto e a cobra conhecida como Argos Panoptes, de agora em diante referido como \"o Capataz\", juntos em um acordo."
                            text "{color=[UIColorOrange]}{i}Artigo Um."
                            text "{i}O Mestre aluga ao Capataz a autoridade para invocar comida, ??gua, abrigo e mob??lia para uso como ele achar adequado, inclusive para o benef??cio do cultivo de safras e a cria????o de animais."
                            text "{i}Em retorno, o Capataz aluga o Espelho de H??stia para uso do Mestre como ele achar adequado, inclusive para o benef??cio e manuten????o da estrutura conhecida como \"Hotel\", conforme estabelecido em contratos anteriores."
                            text "{color=[UIColorOrange]}{i}Artigo Dois."
                            text "{i}O Mestre e o arrendat??rio devem abster-se de causar danos um ao outro, direta e indiretamente, por meios incluindo, mas n??o limitados ?? viol??ncia, incentivando ou recompensando terceiros ?? agress??o m??tua, sabotando estruturas, envenenando alimentos e ??gua, entre outros."
                            text "{color=[UIColorOrange]}{i}Artigo Tr??s."
                            text "{i}O Mestre ?? proibido de interferir direta ou indiretamente no pleno gozo dos direitos do Capataz concedidos neste contrato. O Capataz ?? similarmente proibido de causar danos ao \"Hotel.\""
                            text "{color=[UIColorOrange]}{i}Artigo Quatro."
                            text "{i}O Mestre est?? autorizado a fazer inspe????es nas acomoda????es do Capataz, exceto em seus aposentos pessoais, cujo acesso ?? proibido."
                            text "{i}O Capataz est?? proibido de conspirar contra o Mestre e n??o deve usar os direitos garantidos por este Contrato para prejudic??-lo. O Mestre e o Capataz est??o simetricamente comprometidos a este Artigo, incluindo, mas n??o limitando-se a n??o usar o Espelho de H??stia para causar danos ao Capataz."
                            text "{color=[UIColorOrange]}{i}Artigo Cinco."
                            text "{i}Este contrato ?? auto-impositivo. Se qualquer um de seus artigos for quebrado, a posse do Espelho de H??stia reverte para o Capataz e qualquer chama acesa pelo Espelho ?? apagada."
                            text "{i}Ao mesmo tempo, o Capataz perde os direitos transferidos pelo contrato e toda e qualquer estrutura por ele invocada deixa de existir ap??s um intervalo de 10 minutos para permitir a evacua????o."
                            text "{color=[UIColorOrange]}{i}Artigo Seis."
                            text "{i}Este artigo auto-impositivo entra em vigor no momento de sua assinatura e permanece v??lido durante o comando do Mestre e at?? que o Mestre posterior adquira a Escritura do Hotel."
                            text "{i}Pela vontade do Mestre, a quem o comando dos Ol??mpios sobre o dom??nio foi concedido, este contrato ?? estabelecido."

                    elif Contract == "Rings":
                        vbox spacing 10:
                            text "{i}{size=+2}Juramento dos An??is Vinculativos" xalign 0.5
                            text ""
                            text "Um contrato blasfemo que desafia a vontade dos deuses, proposto pelo prisioneiro na tentativa de revelar as verdadeiras inten????es do Mestre."
                            text "Em sua primeira encarna????o, o anel de chumbo foi feito para ativar se condi????es imposs??veis n??o fossem atendidas. Mas, assim como o pr??prio dom??nio onde o hotel foi constru??do, seu prop??sito foi corrompido e subvertido pela humanidade."
                            text "Talvez haja sabedoria na mem??ria antiga de que um redentor assume as algemas daqueles que ele liberta. A humanidade contempor??nea, no entanto, encontraria virtude em um senhor que voluntariamente limita seu pr??prio poder."
                            text ""
                            text "{i}Pela vontade do Mestre do Labirinto este contrato vinculativo ?? estabelecido, para que possa impor seu conte??do ao mundo e seu povo."
                            text "{i}Por meio deste, o Mestre comanda ?? exist??ncia dois objetos interligados: um anel de chumbo para ajustar-se ao redor do b??ceps de um homem e uma guirlanda de louros da largura do bra??o do prisioneiro."
                            text "{i}Estes dois objetos devem estar ligados em causa e efeito, assim como seus portadores."
                            text "{i}Aquele que vestir o anel de chumbo se encontrar?? em uma situa????o onde remov??-lo ser?? imposs??vel, exceto mediante ?? revoga????o deste contrato."
                            text "{i}Quem primeiro vestir a coroa de louros se tornar?? seu propriet??rio permanente e imut??vel."
                            text "{i}Se o dono da coroa de louros alguma vez for levado para o vale do Labirinto ???seja por coer????o, ordem, ou for??a??? ent??o o anel de chumbo vir?? a contrair e fechar de forma a amputar o bra??o de seu portador."
                            text "{i}Pela vontade do Mestre, este contrato poder?? ser revogado apenas se todas as suas partes ??? portador do anel de chumbo, dono da coroa de louros, e as duas testemunhas presentes durante a sua assinatura ??? o consentirem."
                            text "{i}Tal ?? a vontade do Mestre."
                            
                if FileType == 'Mementos':
                    if Memento == "Tablet1":
                        vbox spacing 10:
                            text "{i}{size=+2}Primeira T??bua: Lua Crescente" xalign 0.5
                            text ""
                            text "Uma t??bua de argila narrando a jornada de um filho cordial a Creta."
                            text "Em tempos antigos, mesmo uma viagem curta levaria anos. Enfrentar o oceano sempre carregou a amea??a de morte, portanto, a viagem era reservada para guerreiros sedentos por sangue, mercadores ambiciosos e miser??veis desesperados."
                            text "Esta t??bua ?? decorada com padr??es de lua crescente imperfeitos. Aquele que os esculpiu desprovia do talento do artes??o, mas n??o de seu carinho."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Cortou atrav??s do pesco??o de meu pai como o a??afr??o colhido a foice destas margens rochosas,"
                            text "{i}aquela lua crescente despretensiosa, nascida do brilho de Hefesto e da turbul??ncia de Zeus."
                            text ""
                            text "{i}Da ??sia Menor eu vim, carregando o peso de meu pai nas costas como ele uma vez me carregou."
                            text "{i}Durante a primavera de minha vida e o inverno da dele, cruzamos o mar para a Creta do Rei Minos."
                            text "{i}Enquanto meu pai enfermo navegava em seus pesadelos de velhice, eu trabalhava nos remos"
                            text "{i}e orava ao trapaceiro da corte do Rei Lica??o, cuja sabedoria nos colocou neste curso."
                            text ""
                            text "{i}Atrav??s do curto mar, fizemos nosso caminho at?? Creta, saudados pelos chifres de ??bex selvagens."
                            text "{i}L?? eu encontraria o mais belo trabalho de Hefesto, as luas crescentes do Olimpo ???"
                            text "{i}aquelas que trazem a noite at?? mesmo para o aspecto incans??vel de um imortal."
                            text "{i}Eu sou Laomedonte, filho bastardo de Titono, uma vez pr??ncipe de Troia."
                            text "{i}O mar que atravessei e o labirinto que percorri, eu faria tudo pelo meu pai,"
                            text "{i}nenhum custo muito alto, nenhuma carga pesada demais, nenhum truque n??o utilizado."
                            text "{i}Ou??a a hist??ria de liberta????o do pai nas m??os do solit??rio guardi??o do labirinto"
                            text "{i}e a morte do h??brido pelo enviado dos deuses."

                    if Memento == "Tablet2":
                        vbox spacing 10:
                            text "{i}{size=+2}Segunda T??bua: Chegada" xalign 0.5
                            text ""
                            text "Uma t??bua de argila narrando a chegada de uma fam??lia amaldi??oada a Creta."
                            text "Era uma vez um homem chamado Minos, filho de Zeus e Europa. Ele fundou Creta, o estado-ilha do qual a cultura grega descende. As lendas falam muito bem sobre a virtude do monarca, dito ter conquistado seu lugar entre os ju??zes de Hades ap??s a morte."
                            text "Gera????es mais tarde, no entanto, outro Minos assumiria o trono, um com uma disposi????o que irritava os deuses e homens de modo parecido."
                            text "Esta t??bua ?? decorada com desenhos simples da cabe??a de uma cabra selvagem. Seus chifres erguem-se orgulhosos, emoldurando uma ??nica estrela solit??ria."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Titono era meu pai, sua era a m??o a qual me ensinou a navegar nestas ??guas abundantes."
                            text "{i}Juntos, perseguimos e lan??amos flechas contra auroques no solo avermelhado e ??mido a partir dos quais fizemos nosso banquete."
                            text "{i}Pastoreamos e ordenhamos ovelhas, fizemos o queijo e o compartilhamos com nossos vizinhos,"
                            text "{i}mas meu pai foi roubado de mim pela est??pida deusa do amanhecer, Eos."
                            text "{i}Ela o tomou por marido e ele, mortal, que escolha ele tinha?"
                            text ""
                            text "{i}O tolo amanhecer pressionou Zeus para torn??-lo imortal, para que ela nunca perdesse seu animal de estima????o."
                            text "{i}Como um rei que n??o conhece o peso do ouro, ele tornou meu pai imortal"
                            text "{i}mas, como disse o trapaceiro de Lica??o, n??o se lembrou da natureza ef??mera de envelhecimento dos mortais."
                            text "{i}Agora sua mente est?? devastada pela idade, mesmo que seu corpo magro e enfermo n??o cesse."
                            text ""
                            text "{i}Naquele dia, quando atraquei meu navio na costa de Creta, carreguei-o nas costas de volta a Cnossos."
                            text "{i}Ele bamboleou como um beb?? em sua primeira primavera, eu aguentei seu peso como uma vez ele fez com o meu."
                            text "{i}Para Creta eu trouxe meu pai, para libert??-lo desta miser??vel b??n????o divina."
                            text "{i}Durante o outono e o inverno, implorei aos p??s do pal??cio de Cnossos pela miseric??rdia do Rei Minos."

                    if Memento == "Tablet3":
                        vbox spacing 10:
                            text "{i}{size=+2}Terceira T??bua: Audi??ncia" xalign 0.5
                            text ""
                            text "Uma t??bua de argila narrando uma rara audi??ncia com um antigo rei."
                            text "Colunas carmesim ainda se encontram nos locais antigos de Creta, uma mem??ria duraroura de uma ??poca derradeira. O labir??ntico Pal??cio de Cnossos, embora consumido e apodrecido, durou mais tempo que os reis e deuses."
                            text "Esta t??bua ?? decorada com padr??es repetitivos de colunas, mas um exame minucioso revela tra??os de um raro e precioso tesouro pulverizado sobre ela: a??afr??o."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}O Rei Minos, no topo de seu pal??cio carmesim, se recusou a nos conceder uma audi??ncia,"
                            text "{i}mas a passos r??pidos eu cacei os ??bex selvagem de sua costa e celebrei com seu povo."
                            text "{i}O couro eu transformei em roupas, primeiro para o meu pai e posteriormente para os cretenses."
                            text "{i}Eu colhi o a??afr??o e os gr??os, eu era um h??spede entre cada uma das fam??lias de Cnossos,"
                            text "{i}at?? que todos ouviram a lament??vel hist??ria de meu pai e foram ati??ados a enfurecer-se contra os deuses."
                            text ""
                            text "{i}O Rei Minos temia nossa hist??ria e a dissemina????o da impiedade entre a popula????o."
                            text "{i}Sob o manto da noite, fomos levados para sua corte, empurrados por entre as fileiras de colunas carmesim."
                            text "{i}Fomos alimentados e vestidos com trajes tradicionais de Creta, e meu pai eu dei banho,"
                            text "{i}pois apenas eu sei como lidar com sua pele, mais delicada que p??talas de asf??delos."
                            text ""
                            text "{i}Enfim chegamos em sua corte, carreguei meu pai contra meu peito como um rec??m-nascido."
                            text "{i}Sobre um tapete de palha eu o deitei para o Rei ver o infort??nio nascido da b??n????o de Zeus"
                            text "{i}e implorei pelas luas crescentes de Hefesto, sua mais bela cria????o,"
                            text "{i}que partiram o cr??nio de Zeus e, assim, deram ?? luz Atenas, sempre mais s??bia que seu pai."
                            text ""
                            text "{i}Pois ?? dever de um filho cuidar de seus pais durante a velhice,"
                            text "{i}e ?? meu dever libertar meu pai de sua enfermidade eterna."
                            text "{i}Eu sou Laomedonte, filho do imortal Titono, marido abandonado da est??pida Eos,"
                            text "{i}e procuro o L??bris de Creta, t??o afiado a ponto de cortar seu fio de vida imortal tecido pelos Destinos."
                            text "{i}Para um par t??o miser??vel e amaldi??oado, nenhum custo ?? muito alto, nenhuma carga ?? terr??vel demais."

                    if Memento == "Tablet4":
                        vbox spacing 10:
                            text "{i}{size=+2}Quarta T??bua: Jovem Mulher" xalign 0.5
                            text ""
                            text "Uma t??bua de argila narrando a interven????o de uma jovem preocupada."
                            text "Os tempos antigos eram governados pelo princ??pio de que a for??a faz o correto. Mulheres que desejavam impor sua vontade ao mundo tiveram que contar com subterf??gios e intelig??ncia."
                            text "Esta t??bua ?? decorada com uma ??nica linha em sua parte inferior, a silhueta do Monte Ege??o; o local onde, diz a lenda, Zeus foi criado."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Quando o ver??o chegou e o Rei Minos ainda n??o havia nos concedido sua b??n????o,"
                            text "{i}uma jovem mulher entrou sorrateiramente em nossa tenda e me contou sobre o labirinto"
                            text "{i}??? no p?? de uma montanha, a mesma onde Zeus passou sua juventude ???"
                            text "{i}onde encontrar??amos um tem??vel h??brido, um monstro nascido do caso da rainha com uma fera."
                            text ""
                            text "{i}Durante minhas tardes de colheita de a??afr??o, as esposas falaram-me de tal besta,"
                            text "{i}outrora conhecida como uma divindade da prosperidade exibida pelo Rei Minos,"
                            text "{i}trancado nos confins do labirinto depois de experimentar o canibalismo."
                            text "{i}Ele, disse a jovem, guarda o L??bris de Creta,"
                            text "{i}presente de Zeus para seu local de nascimento, bem no centro do labirinto."
                            text ""
                            text "{i}\"Busque o monstro amaldi??oado no cora????o do mundo,"
                            text "{i}no santu??rio carmesim ele guarda o machado capaz de cortar a linha vital."
                            text "{i}Mas saiba, bastardo de Troia, que somente aqueles inspirados pelo divino"
                            text "{i}podem levant??-lo ??? ore pela b??n????o de Atena."
                            text "{i}N??o o toque; ele ?? revestido com o icor de Zeus."
                            text "{i}N??o ?? destino de um homem tocar mat??ria divina.\""
                            text ""
                            text "{i}Eu parti com meu pai naquela mesma noite,"
                            text "{i}?? dist??ncia, avistei a montanha de Zeus."
                            text "{i}Ficava mais perto a cada dia,"
                            text "{i}assim como o sofrimento de meu pai chegou ao fim."

                    if Memento == "Tablet5":
                        vbox spacing 10:
                            text "{i}{size=+2}Quinta T??bua: Monstro" xalign 0.5
                            text ""
                            text "Uma t??bua de argila narrando o encontro de um homem com outro de natureza divina."
                            text "Para os gregos, ser um h??brido ?? ser um monstro. Os dois s??o indissoci??veis."
                            text "Divino ou n??o, um h??brido ?? um ser abomin??vel e repulsivo que boas pessoas fariam bem ao ostracizar."
                            text "Esta t??bua ?? decorada com linhas labir??nticas em suas margens."
                            text "Uma t??bua de argila narrando uma interven????o de um jovem preocupado."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}No sop?? do Monte Ege??o, no planalto Lasiti, eu encontrei o labirinto,"
                            text "{i}uma antiga estrutura pintada com o mesmo carmesim do Pal??cio de Cnossos,"
                            text "{i}constru??do e esculpido com o amor e carinho de um artes??o especialista."
                            text "{i}Por mais que tentasse, do topo da montanha n??o consegui aprender suas curvas,"
                            text "{i}pois sua forma alterava-se a cada piscar de meus olhos."
                            text ""
                            text "{i}Um porrete em minha m??o, pai nas minhas costas, nos aventuramos juntos"
                            text "{i}com o conforto de saber que, mesmo se eu falhasse, sua dor ainda cessaria."
                            text "{i}Por tr??s dias e tr??s noites n??s vagamos, ouvindo apenas o canto das cigarras"
                            text "{i}e o bater de cascos distantes, sempre fora de alcance."
                            text "{i}O monstro brincou conosco, nunca dando as caras."
                            text "{i}Eu temia que a fome tirasse minha vida e chorei pela de meu pai."
                            text ""
                            text "{i}No quarto dia, a criatura apareceu, o monstro h??brido de Pas??fae."
                            text "{i}N??o era o tem??vel tit?? o qual me disseram que comia a carne de homens ???"
                            text "{i}seu focinho rosa, t??midos chifres e olhos brilhantes eram os de um bezerro amamentado."
                            text ""
                            text "{i}Eu o desafiei para um combate, certo de que finalmente"
                            text "{i}teria um fim para este esc??rnio,"
                            text "{i}mas ele disparou por seus corredores intermin??veis,"
                            text "{i}deixando para tr??s apenas o bater de cascos entrando em sil??ncio."

                    if Memento == "Tablet6":
                        vbox spacing 10:
                            text "{i}{size=+2}Sexta T??bua: Crian??a" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando a hospitalidade de uma crian??a."
                            text "Os gregos tinham muitos costumes e normas as quais ditavam como um h??spede deveria ser tratado. Naqueles tempos antigos, deuses disfar??ados andavam entre os homens, ent??o era esperado que um anfitri??o tratasse seus convidados com o respeito que o divino merecia."
                            text "Trazer desgra??a ?? casa de um anfitri??o era uma atrocidade imperdo??vel que certamente inspiraria maldi????es sobre a linhagem de uma pessoa."
                            text "Esta t??bua ?? adornada com representa????es de um templo, ou talvez um santu??rio. Um touro massacrado encontra-se em sua entrada."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Eu cacei a panturrilha do arqueiro, mas na verdade fui feito uma presa."
                            text "{i}Na quarta noite, eu desabei. Apenas ent??o o menino revelou-se"
                            text "{i}de uma curva ?? frente."
                            text ""
                            text "{i}\"Eu sou Ast??rio, filho adotivo do Rei Minos e guardi??o da casa de D??dalo."
                            text "{i}Este ?? um solo sagrado; em seu cora????o h?? um santu??rio, em seu centro jaz uma bacia"
                            text "{i}na qual queima um fogo sagrado presenteado pelos pr??prios deuses."
                            text "{i}Aprendi a arte da hospitalidade, lavar os p??s dos h??spedes"
                            text "{i}e fornecer dois ter??os de minha refei????o a ti."
                            text "{i}Eu lhe receberia carinhosamente ??? n??o fosse pelas armas em teu punho."
                            text "{i}Diga-me, por que levantarias teu bra??o contra os deuses?\""
                            text ""
                            text "{i}Com a pouca voz que restou em minha rouca garganta, eu respondi:"
                            text "{i}\"?? contra a insensatez divina que me volto, n??o aos pr??prios deuses."
                            text "{i}Eu sou Laomedonte, filho de Titono, por sua vez, marido da deusa Eos;"
                            text "{i}esta casca que carregou ?? o que ela deixou para tr??s. Ela implorou a Zeus para torn??-lo imortal"
                            text "{i}mas em seu tolo torpor, n??o requisitou juventude eterna."
                            text "{i}A velhice sequestrou sua mente, seus ossos agora est??o fr??geis"
                            text "{i}e sua pele est?? t??o delicada quanto as asas de uma mariposa."
                            text "{i}Eu ouvi um conto que em Creta, no cora????o do labirinto, pode-se encontrar"
                            text "{i}uma arma de lua crescente, um l??bris fabricado por Hefesto,"
                            text "{i}capaz de cortar o fio vital de um imortal.\""
                            text ""
                            text "{i}Talvez um guerreiro experiente tivesse jogado de lado minha hist??ria"
                            text "{i}e me deixado para morrer de fome e apodrecer nestes corredores intermin??veis."
                            text "{i}Mas as crian??as n??o sabem que um mendigo pode esconder uma faca sob o manto."

                    if Memento == "Tablet7":
                        vbox spacing 10:
                            text "{i}{size=+2}S??tima T??bua: Icor" xalign 0.5
                            text ""
                            text "Uma t??bua de argila narrando uma pequena trag??dia da loucura humana."
                            text "O corpo ?? um recipiente dado pelos deuses, sabendo muito bem que ?? o destino humano ser destro??ado, quebrado e mutilado. Deixe a dor lev??-lo embora, para que serve o sofrimento humano sen??o um pequeno desvio na exist??ncia de um deus?"
                            text "Esta t??bua n??o possui adornos."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}O h??brido guiou eu e meu pai a um santu??rio carmesim ???"
                            text "{i}uma morada de pedra abrigando uma piscina rasa de ??guas claras,"
                            text "{i}em seu centro encontra-se uma bacia de pedra na qual arde a chama sagrada."
                            text "{i}?? sua esquerda, h?? um santu??rio menor, no centro h?? uma ampla chapa"
                            text "{i}de pedra polida na qual o machado de duas cabe??as de Creta est?? cravado."
                            text ""
                            text "{i}Lembrei-me ent??o das palavras da jovem mo??a, que apenas algu??m"
                            text "{i}favorecido pelo divino poderia empunhar o machado."
                            text "{i}O menino h??brido alertou-me contra isto, mas a arrog??ncia da masculinidade"
                            text "{i}me deixou surdo ?? todas as palavras de cautela."
                            text ""
                            text "{i}At?? os dias de hoje carrego as marcas de queimadura em minhas m??os;"
                            text "{i}at?? os dias de hoje o machado est?? imbu??do com o icor de Zeus,"
                            text "{i}ele rebelou-se contra o toque mortal e revidou."

                    if Memento == "Tablet8":
                        vbox spacing 10:
                            text "{i}{size=+2}Oitava T??bua: Guardi??o do L??bris" xalign 0.5
                            text ""
                            text "Uma t??bua de argila retratando uma cena de trai????o."
                            text "M??es frequentemente alertam seus filhos para que n??o falem com estranhos. A m??e deste pr??ncipe, no entanto, h?? muito desistiu das palavras e caiu em uma loucura de lamenta????es. Largado sozinho, muitas li????es importantes nunca foram ensinadas a ele."
                            text "Esta t??bua ?? adornada com um padr??o decorativo tradicional de Creta, o machado de duas cabe??as."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Por tr??s dias e tr??s noites, me recuperei de minhas queimaduras."
                            text "{i}O h??brido voluntariamente assumiu o papel de meu cuidador e de meu pai."
                            text "{i}Que hospitalidade ele demonstrou, minhas feridas ele limpou,"
                            text "{i}meu pai ele reajustava duas d??zias de vezes por dia para que nenhuma escara o afligisse."
                            text ""
                            text "{i}O tempo todo, implorei por sua ajuda; \"Voc?? n??o tem divindade interior?"
                            text "{i}Pois seu pai ?? o touro de Poseidon, sua m??e ?? Pas??fae, a ninfa."
                            text "{i}Certamente o l??bris se render?? a ti; corte ent??o o fio vital de meu pai"
                            text "{i}e o liberte desta maldi????o divina.\""
                            text ""
                            text "{i}O h??brido de chifres imaculados olhou para mim com olhos lustrosos."
                            text "{i}\"De fato, o machado n??o queima minha pele, mas seu peso ?? imenso,"
                            text "{i}nunca o desalojei de sua pedra. Ai de mim, meu bom pr??ncipe,"
                            text "{i}n??o dissestes que o pr??prio Zeus concedeu a teu pai a d??diva da eternidade?"
                            text "{i}Que direito tenho eu de retirar o que os Cr??nidas concederam?\""
                            text ""
                            text "{i}\"Todos os deuses nos deram vida e os Destinos nos tiram dela."
                            text "{i}?? apenas natural para um homem trazer a morte ao outro ???"
                            text "{i}os deuses n??o derramaram icor em sua titanomaquia?"
                            text "{i}O homem apenas imita o que os Ol??mpios ensinaram."
                            text "{i}Ser?? que algu??m como voc??, com caracter??sticas desumanas,"
                            text "{i}acredita-se estar acima do dever de derramamento de sangue?"
                            text "{i}N??o se preocupe, uma natureza peculiar n??o o isenta do dever."
                            text "{i}H?? miseric??rdia em acabar com o sofrimento de algu??m,"
                            text "{i}e ainda mais gra??a em ser subjugado pela arte de Hefesto."
                            text "{i}Por favor, hospitaleiro senhor do labirinto, ajude este filho em sua justa miss??o;"
                            text "{i}n??o tema o peso do machado, pois irei trein??-lo."
                            text "{i}Sua fisionomia calejar?? com a maturidade,"
                            text "{i}suas costas crescer??o e ficar??o t??o largas quanto as estepes,"
                            text "{i}seu rugido estrondoso deve rachar as paredes."
                            text "{i}O treinarei da mesma forma que meu pai me ensinou."
                            text "{i}Pelo tempo que for necess??rio, estarei ao seu lado, at?? o dia"
                            text "{i}que seu poder elevar-se sobre o peso das luas crescentes de Hefesto.\""

                    if Memento == "Tablet9":
                        vbox spacing 10:
                            text "{i}{size=+2}Nona T??bua: Lira" xalign 0.5
                            text ""
                            text "Uma t??bua de argila narrando uma pequena trag??dia da loucura humana."
                            text "A m??sica dura por apenas um momento, mas pode ser guardada para sempre na mente de algu??m."
                            text "Esta t??bua ?? adornada com o desenho de uma lira. O processo de cozimento, por??m, fez com que os fios se rompessem."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Muitas noites passamos naquele santu??rio carmesim,"
                            text "{i}confortados pela lira do menino e pela chama da bacia."
                            text "{i}Antes e depois de cada refei????o, Ast??rio pagaria a H??stia seu tributo e al??m,"
                            text "{i}??s vezes passando fome por uma gl??ria maior da deusa."
                            text ""
                            text "{i}Noite ap??s noite eu implorei por sua ajuda, mas ele n??o cedeu."
                            text "{i}Ent??o usei de minha intelig??ncia para persuadi-lo, eu o convenceria com minha l??bia."
                            text "{i}Entre os gemidos de meu pai eu perguntaria,"
                            text "{i}ele responderia sem parar sua m??sica, os dedos ro??ando nos fios."
                            text ""
                            text "{i}\"Por que voc?? fica aqui, crian??a?"
                            text "{i}O planalto que nos rodeia ?? vasto e bonito."
                            text "{i}N??o ??s um pr??ncipe, descendente de uma rainha aben??oada?"
                            text "{i}Muitas s??o as alegrias que a realeza bem merece desfrutar."
                            text "{i}Quando foi a ??ltima vez que colheu a??afr??o"
                            text "{i}e ro??ou teus dedos na suavidade oculta de suas p??talas?"
                            text "{i}Quando foi a ??ltima vez que se banhou na costa de Creta?"
                            text "{i}N??o est?? em sua riqueza vestir-se de roxos e vermelhos vibrantes?"
                            text "{i}Quantas luas se passaram desde o amanhecer"
                            text "{i}no qual voc?? cumprimentou os pescadores para comprar sua pesca fresca?\""
                            text ""
                            text "{i}\"N??o sei ao certo, senhor,\" respondeu a crian??a, os olhos brilhando contra o fogo."
                            text "{i}Suas orelhas sacudiram junto com o vento frio."
                            text "{i}\"Passaram-se talvez sete invernos desde que negociei com os pescadores,"
                            text "{i}seis desde a ??ltima vez que meus cascos sentiram o abra??o frio do mar,"
                            text "{i}cinco desde a ??ltima vez que segurei a m??o de minha irm?? em nosso caminho at?? os campos para colher flores,"
                            text "{i}quatro desde que n??o usei nada al??m de tecidos duros"
                            text "{i}e tive algu??m com quem trocar palavras pela ??ltima vez."
                            text "{i}Mas nem uma noite se passou sem que eu puxasse as cordas de minha lira"
                            text "{i}nem um dia em que as d??vidas dos deuses n??o foram pagas."
                            text "{i}Por mais solit??rio que seja o labirinto, n??o fui eu batizado com o nome das estrelas?"
                            text "{i}Eu encontro companheirismo entre elas, tra??ando-as com um dedo"
                            text "{i}e dentro de minha pr??pria mente, da qual ningu??m pode me despojar."
                            text "{i}Antes de sua chegada, eu pensei; do amanhecer ao anoitecer,"
                            text "{i}minha mente correu com hist??rias e possibilidades."
                            text "{i}O mar eu n??o verei at?? que meu pai me alivie de meu dever,"
                            text "{i}mas sua espuma posso para sempre manter na palma de minha mente.\""

                    if Memento == "Tablet10":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima T??bua: Espuma do Mar" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando um bastardo tentando um jovem devoto a se afastar para longe de seu dever."
                            text "Creta n??o ?? conhecida por suas cobras venenosas. N??o ?? nenhuma surpresa, ent??o, que aquele que tentaria um pr??ncipe a se afastar de seu dever tenha vindo do outro lado do mar."
                            text "Esta t??bua ?? adornada com padr??es parecidos com ondas."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}\"A costa n??o est?? longe, muito menos os a??afr??es pelos quais esta ilha ?? conhecida."
                            text "{i}Deixe-nos partir amanh?? ao romper da madrugada, eu segurarei sua m??o"
                            text "{i}enquanto cruzamos este planalto e deleitamos nossos olhos com suas cores."
                            text "{i}Deixe o carmesim deste santu??rio ser esquecido, passe seus dedos sobre as p??talas roxas"
                            text "{i}e afunde seus cascos nas praias arenosas e ??guas turvas."
                            text "{i}Amanh??, voc?? e eu, ao amanhecer,"
                            text "{i}vamos deixar este cativeiro para tr??s e nos encher de contentamento.\""
                            text ""
                            text "{i}Mas o filho de Minos n??o acolheria ideias t??o ??mpias."
                            text "{i}\"Isto n??o devo fazer, pois dei minha palavra a meu pai, que n??o iria embora"
                            text "{i}da casa que D??dalo construiu. Devo cuidar do santu??rio e guardar o l??bris"
                            text "{i}para que a ru??na n??o caia sobre nossa terra e todo o seu povo."
                            text "{i}Voc?? ?? um pr??ncipe tanto quanto eu ??? um bastardo tamb??m."
                            text "{i}Por mais que seja nosso direito tomar parte dos prazeres da realeza,"
                            text "{i}o dever sozinho me acorrenta.\""
                            text ""
                            text "{i}\"Devemos retornar antes do anoitecer, Ast??rio. O santu??rio n??o ficar?? sem manuten????o,"
                            text "{i}nem o tributo a H??stia deixar?? de ser pago. Vamos colher uma pitada de a??afr??o e oferecer a ela,"
                            text "{i}nossa aventura trar?? alegria ao seu rosto caseiro."
                            text "{i}Nenhum homem saber?? de nossa transgress??o, apenas as ??guas espumosas do mar.\""
                            text ""
                            text "{i}Ele acariciou as cordas de sua lira, puxando aqui e ali."
                            text "{i}\"Mas eu saberia, e isto ?? ruim o suficiente."
                            text "{i}Voc?? faria bem em gravar minha frase em sua mente."
                            text "{i}N??o te esque??as que os Destinos n??o acharam por bem que eu fosse homem,"
                            text "{i}nem teceram a espuma do mar ou o a??afr??o da flor em meu tapete."
                            text "{i}Dentro do labirinto devo permanecer, pois esta ?? minha promessa.\""

                    if Memento == "Tablet11":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima Primeira T??bua: Permuta" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando uma das muitas trag??dias que levaram ?? morte de um menino."
                            text "Esta t??bua de argila ?? adornada com padr??es decorativos de flores que racharam e se deformaram durante o processo de cozimento."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}A noite se estendia em diante, um v??u de medo e escurid??o nos cobriu."
                            text "{i}Um fogo transbordou em meu peito, talvez no dele tamb??m."
                            text "{i}Nenhuma oferta de prazeres poderia convenc??-lo a partir"
                            text "{i}ou levantar o machado para libertar meu pai."
                            text "{i}Um estalo agudo me despertou do pensamento ???"
                            text "{i}uma ??nica brasa saltou da bacia para a piscina rasa."
                            text "{i}Eu a vi fracassar e morrer, sozinha e com frio ???"
                            text "{i}que nitidez ela trouxe aos meus olhos!"
                            text "{i}Uma ideia saltou de mim antes que minha pr??pria prud??ncia tomasse conta."
                            text "{i}\"Pr??ncipe de Creta expectante do amanhecer, por uma d??zia de dias"
                            text "{i}meu pai e eu nos abrigamos em sua morada,"
                            text "{i}comendo de sua comida e ??gua."
                            text "{i}Como eu disse, era minha miss??o libertar meu pai da dor,"
                            text "{i}entreg??-lo ??s margens da Nix, nas m??os de Caronte."
                            text "{i}Sou grato por sua hospitalidade ??? igualmente grato estaria Titono,"
                            text "{i}tivesse ele ju??zo o suficiente para gastar."
                            text "{i}Queria compartilhar com voc?? uma ??ltima mem??ria de alegria,"
                            text "{i}um ??nico dia de felicidade quando vasculhamos estas praias."
                            text "{i}Mas este n??o ?? o caso; seu dever ?? muito grande."
                            text "{i}Ent??o ?? com pesar que devo anunciar:"
                            text "{i}ao amanhecer, eu e meu pai deixaremos"
                            text "{i}o labirinto e os solos de Creta, para algum lugar,"
                            text "{i}al??m destas ??guas turvas deve haver um outro"
                            text "{i}inspirado pelos Ol??mpios, os quais podem encerrar nossa jornada.\""
                            text ""
                            text "{i}Ast??rio expectante do amanhecer interrompeu sua m??sica e fechou os olhos."
                            text "{i}O pesar parecia consumi-lo; um n?? se formou em sua garganta."
                            text "{i}Quando as palavras o deixaram, elas estavam roucas e vacilantes."
                            text "{i}\"Voc?? conhece as artes do combate, n??o?"
                            text "{i}Seu pai, em seu auge, lhe ensinou sobre o afiamento de uma l??mina."
                            text "{i}Quanto tempo levaria para eu reunir o poder necess??rio"
                            text "{i}para empunhar o tesouro de Hefesto, o machado capaz de cortar o fio de vida?"
                            text "{i}Suas palavras talvez carregassem sabedoria, afinal;"
                            text "{i}deve-se ascender para conceder miseric??rdia e liberta????o"
                            text "{i}para um prisioneiro acorrentado pela desgra??a e infort??nio."
                            text "{i}Eu o farei, pr??ncipe de Troia, dominarei o l??bris"
                            text "{i}se voc?? me conceder um pedido simples e humilde:"
                            text "{i}n??o me deixe sozinho.\""

                    if Memento == "Tablet12":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima Segunda T??bua: Oferenda" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando a natureza suja de um h??brido."
                            text "Ser um h??brido ?? ser amaldi??oado com uma vida de infort??nios muito maiores que os de qualquer mortal."
                            text "Esta t??bua de argila ?? adornada com padr??es decorativos de fogo, embora o processo de cozimento os tenha deformado e distorcido."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Ast??rio de chifres imaculados manteve sua palavra; nossas tardes foram gastas treinando"
                            text "{i}bem como meu pr??prio pai me ensinou o equil??brio e os golpes de cada arma."
                            text "{i}Por tr??s invernos, o labirinto de D??dalo tornou-se minha casa."
                            text "{i}O h??brido cresceu diante dos meus olhos, seus tra??os outrora finos"
                            text "{i}adquiriram o poder de um touro ??? medo ele provocaria entre os inimigos"
                            text "{i}n??o fosse por seu focinho rosa sempre infantil."
                            text "{i}Ast??rio de costas largas como as estepes, foi assim que passei a cham??-lo"
                            text "{i}em sua brilhante gl??ria de guerreiro."
                            text ""
                            text "{i}Ainda assim, n??o houve uma noite em que sua lira n??o tenha sido tocada,"
                            text "{i}nem uma onde o fogo de H??stia na bacia implorou pela pouca carne que t??nhamos,"
                            text "{i}e muito menos uma noite em que nosso sangue n??o derramasse conforme choc??vamos armamentos."
                            text "{i}E assim aprendi sobre o sangue sujo de Ast??rio ??? uma mistura f??tida,"
                            text "{i}tanto vermelho sangue quanto preto icor, prova das origens profanas do h??brido."
                            text "{i}Retumbou quando incendiado, e que grande chama ele gerou."
                            text "{i}Foi um ??timo sacrif??cio para a bacia, mais ainda para H??stia com seu gosto por carne de boi."
                            text "{i}Uma vez derramado, endurecia em uma pedra quebradi??a e imunda, bem como o co??gulo de uma ferida,"
                            text "{i}mas firme o suficiente para se passar como pedra cuspida de um vulc??o."
                            text "{i}Seu cheiro trazia repulsa, mas que bela igni????o era para a chama."
                            text "{i}Os corredores intermin??veis e mut??veis do labirinto eram nossos campos de treinamento"
                            text "{i}pois o menino n??o contaminaria o santu??rio com sua natureza f??tida."

                    if Memento == "Tablet13":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima Terceira T??bua: Brasas a Morrer" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando o des??nimo do h??brido."
                            text "N??o se deve trancar a porta se o esp??rito do prisioneiro estiver quebrado."
                            text "Esta t??bua de argila n??o possui decora????es."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Depois que Ast??rio tocou a can????o de ninar do pai, conversamos em sussurros at?? tarde da noite."
                            text "{i}Trocar??amos contos de her??is e constela????es, compartilhando lendas de nossas terras."
                            text "{i}\"Diga-me, garoto, voc?? ouviu hist??rias das aldeias al??m deste mar?"
                            text "{i}Meu pai j?? foi pr??ncipe de uma bela cidade-estado antes de a insensatez dos deuses tomar conta de sua mente."
                            text "{i}Lhe agrada a ideia de deixar este labirinto e viajar para o norte,"
                            text "{i}caso seu pai algum dia o liberte do dever de cuidar deste santu??rio?\""
                            text ""
                            text "{i}O menino hesitou antes de responder, quando o fez, sua voz estalou como as brasas."
                            text "{i}\"Para ver al??m destas paredes e do mar? De forma alguma, ouvi pouqu??ssimas hist??rias,"
                            text "{i}mas o pensamento, cruzar o mar, como eu poderia achar isto agrad??vel?"
                            text "{i}Creta ?? o ber??o do homem, est?? acima de todas as outras na????es e sobreviver?? a todas elas,"
                            text "{i}que raz??o teria algu??m para abandonar seu seio?"
                            text "{i}Ai de mim, apenas o pensamento ?? tolice, pois meu pai jamais me dispensar?? de meu dever."
                            text "{i}Posso deixar estas paredes, mas haver?? outro labirinto para mim"
                            text "{i}assim que provar que sou capaz de empunhar o l??bris.\""
                            text ""
                            text "{i}\"Esque??a Creta, ent??o, o pensamento da liberdade o ati??a?"
                            text "{i}Pode n??o haver terra como esta, onde as cobras n??o conhecem palavras venenosas"
                            text "{i}e as cabras selvagens t??m uma carne t??o rica, mas pense em um lugar onde a liberdade ?? sua.\""
                            text ""
                            text "{i}E como madeira seca, abandonada por anos, sua voz estalou entre as brasas."
                            text "{i}\"Elimine o pensamento, meu senhor. N??o v?? que sou uma besta?"
                            text "{i}Minha vontade dificilmente importa nesse caso, independente de eu desejar ou n??o a liberdade,"
                            text "{i}como cruzaria o mar revolto? Se soubesse como velejar, ainda assim n??o teria como faz??-lo."
                            text "{i}Tivesse eu a tripula????o e o barco, eles n??o me subjugariam pelo pecado que sou?"
                            text "{i}E se eu de fato conseguir cruzar o mar, o que me espera do outro lado? Ao menos aqui"
                            text "{i}tenho a esperan??a de ver minha fam??lia mais uma vez, de sua pr??xima visita."
                            text "{i}Certamente eles chegar??o em breve, meus irm??os e eu ca??aremos juntos."
                            text "{i}N??o h?? futuro em nenhum outro lugar para mim, meu senhor,"
                            text "{i}mesmo que eu tema que esta terra tamb??m n??o comporte nada para mim, exceto brasas a morrer.\""

                    if Memento == "Tablet14":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima Quarta T??bua: Redentor" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando uma das muitas trag??dias que levaram ?? morte de um menino."
                            text "O que aguarda o sacrificado al??m de sua tormenta? Pode-se apenas imaginar."
                            text "Esta t??bua de argila ?? adornada com padr??es decorativos de flores, os quais racharam e se deformaram durante o processo de cozimento."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Um dia o menino encontrou uma flor crescendo atrav??s de uma rachadura no ch??o de pedra,"
                            text "{i}a primeira que ele viu em todos aqueles invernos desde seu banimento."
                            text "{i}Que dor havia em seus olhos, sabendo que n??o deveria ser arrancada"
                            text "{i}e ter que percorrer os corredores apenas para dar uma olhada!"
                            text "{i}Intermin??vel foi sua tristeza quando a chuva forte apodreceu suas ra??zes,"
                            text "{i}mas ele encontrou consolo em oferec??-la a H??stia como sacrif??cio."
                            text ""
                            text "{i}J?? se passaram tr??s invernos desde minha chegada a esta ilha,"
                            text "{i}o h??brido tornou-se um guerreiro excelente e capaz sob minha tutela."
                            text "{i}N??o demoraria muito para ele ser capaz de levantar o l??bris"
                            text "{i}e p??r um fim ao sofrimento de meu pai."
                            text ""
                            text "{i}Durante uma das noites frias, quando nos amontoamos contra a bacia,"
                            text "{i}quando a madeira soltou uma fuma??a f??tida e escura capaz de trazer l??grimas aos olhos,"
                            text "{i}ele me perguntou se uma flor sentia alegria ao ser arrancada e oferecida aos deuses."
                            text "{i}??s vezes, esta criatura adulta falava com a inoc??ncia de uma crian??a,"
                            text "{i}aquela voz suave que todos n??s aprendemos a abandonar talvez muito cedo."
                            text "{i}Falei ent??o com a dor e a pena de um pai consolando seu filho com a morte de um cachorro:"
                            text "{i}\"N??o h?? maior honra que ser oferecido aos doze, crian??a."
                            text "{i}Pois qualquer fraqueza que ela ou qualquer ser j?? tenha mostrado ?? redimida"
                            text "{i}quando a vida de uma pessoa ?? assim arrancada e tornada sagrada."
                            text "{i}Em breve acabaremos com a dor de meu pai, e ent??o voc?? enxergar??"
                            text "{i}como uma liberta????o de pesadas algemas, e ver?? a si mesmo como seu querido redentor.\""
                            text ""
                            text "{i}Aquela foi a ??ltima noite na qual o h??brido tocou sua lira; uma corda estourou."
                            text "{i}Ast??rio Cortador de Fios embalou o instrumento contra seu peito"
                            text "{i}e cantarolou at?? a sonol??ncia cair sobre seus olhos."
                            text "{i}Antes de nos retirarmos para nossas esteiras de palha, no entanto, ele disse:"
                            text "{i}\"Existe calor em seu cora????o para acreditar que eu, tamb??m,"
                            text "{i}um dia serei aben??oado com um redentor? Um cruzando o mar para me libertar"
                            text "{i}destas algemas t??o familiares que carregam os s??mbolos dos deuses?"
                            text "{i}Ser?? que um dia serei redimido de meu nascimento, voarei livre"
                            text "{i}como ??caro e D??dalo voaram, para longe desta terra miser??vel?\""
                            text ""
                            text "{i}Eu senti ent??o a faca escondida entre suas palavras, prestes a cortar minha pr??pria garganta tamb??m."
                            text "{i}O que eu poderia dizer? Juntei minhas brasas, todas que pude reunir, e disse:"
                            text "{i}\"Voc?? ser?? redimido, sem d??vida, e ent??o ver?? as flores"
                            text "{i}crescendo fora destas paredes carmesim de D??dalo."
                            text "{i}Nenhum mar ?? grande demais, nenhuma maldi????o ?? ruim o suficiente, para impedir algu??m de alcan??ar a salva????o,"
                            text "{i}acima de tudo, aquele que teria a miseric??rdia de libertar um homem enfermo e amaldi??oado.\""
                            text ""
                            text "{i}E estas palavras, hoje s??o as que mais me arrependo,"
                            text "{i}que pesadelo miser??vel depositei nele?"

                    if Memento == "Tablet15":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima Quinta T??bua: Insensatez" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando o ??ltimo resqu??cio de esperan??a de um prisioneiro."
                            text "?? preciso apagar as chamas ao redor para realizar sua vontade. Um prisioneiro deve ser mantido acorrentado para cumprir sua miss??o."
                            text "Ainda assim, algumas brasas possuem uma segunda vida, revelada quando a camada de fuligem voa para expor um cora????o ainda vermelho."
                            text "Esta t??bua n??o possui enfeites."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}A primavera chegou, mas o inverno persistiu no cora????o do h??brido."
                            text "{i}Sua respira????o ficou mais curta e uma tosse criou ra??zes em seus pulm??es,"
                            text "{i}ainda assim, eu o puxava de seu saco de dormir todos os dias para aprender a arte da guerra,"
                            text "{i}para que ele pudesse libertar meu pai de sua exist??ncia amaldi??oada."
                            text "{i}Um fogo fervia em meus pulm??es e eu tamb??m fiquei sem f??lego,"
                            text "{i}embora em mim n??o fosse de mal-estar; e sim de desespero."
                            text "{i}Apesar de minha necessidade por sil??ncio, o h??brido falou entre nossas partidas."
                            text ""
                            text "{i}\"Quando chegar o dia em que meu redentor me libertar??, como ele saber??"
                            text "{i}virar ?? esquerda tr??s vezes depois do p??tio com o mural de touro em alto relevo?"
                            text "{i}Os deuses aben??oar??o sua mente com a vis??o de um falc??o voando acima?"
                            text "{i}Hera enviar?? cobras para gui??-lo at?? o santu??rio que eu protejo?"
                            text "{i}Talvez meu salvador seguir?? os mesmos passos de ti,"
                            text "{i}primeiro procurando a casa onde nasci para aprender sobre o cora????o do labirinto.\""
                            text ""
                            text "{i}Fiz sinal para reiniciarmos nosso combate, mas ele n??o se mexeu."
                            text "{i}Comecei ent??o a falar as palavras doces que ele tanto desejava ouvir."
                            text "{i}\"O que voc?? desejar, aquilo que quiser, para um jovem t??o devoto,"
                            text "{i}Sei que os deuses atender??o ao seu pedido; poucos s??o aqueles"
                            text "{i}com o icor correndo em suas veias e com uma disposi????o t??o leal."
                            text "{i}Ap??s a conclus??o de nosso ritual, quando o fio vital de meu pai for rompido,"
                            text "{i}certamente eles enviar??o a pr??pria Nice para guiar um redentor at?? voc??.\""
                            text ""
                            text "{i}\"O ritual, de fato,\" murmurou o monstro e percebi novamente o estalar das brasas."
                            text "{i}\"Obstinado Titono, voc?? ouviria meu apelo? H?? um desejo pelo qual"
                            text "{i}meu cora????o anseia. Quando deixares a cada de D??dalo,"
                            text "{i}retornaria para minha terra natal e contaria um segredo para minha fam??lia?"
                            text "{i}Diga-os que os caminhos do labirinto rendem-se gentilmente se algu??m deixar para tr??s"
                            text "{i}um fio de l?? enquanto o enfrentam."
                            text "{i}Com este conhecimento, meu salvador certamente encontrar?? seu caminho"
                            text "{i}para o cora????o onde o espero."
                            text "{i}Embora, se tamb??m ouviria minha vergonhosa confiss??o,"
                            text "{i}assim que o desejo pela chegada de meu redentor se apoderou de mim,"
                            text "{i}uma ideia boba a qual n??o consigo me livrar tamb??m apareceu. Em meus sonhos, me enxergo saindo"
                            text "{i}da casa de D??dalo, vendo por conta pr??pria os campos de a??afr??o"
                            text "{i}e a ??gua espumosa do mar, o mesmo de onde veio meu progenitor."
                            text "{i}Meu cora????o dispara quando penso na chegada de um redentor,"
                            text "{i}mas dolorosamente, como se de alguma forma eu tivesse que evitar a ideia."
                            text "{i}Pela primeira vez em todos esses anos, meu amigo, eu desejo"
                            text "{i}abandonar meu posto e deixar este labirinto."
                            text "{i}As cavernas do Monte Ege??o me forneceriam um porto seguro,"
                            text "{i}existem muitas clareiras desconhecidas nesta ilha"
                            text "{i}onde eu poderia encontrar conforto, e talvez eu pudesse negociar o pouco que tenho"
                            text "{i}em troca de uma passagem segura atrav??s do mar para terras desconhecidas."
                            text "{i}Diga-me, Titono, esta ideia n??o ?? podre e vergonhosa?"
                            text "{i}Abandonar meu dever para com os deuses, deixar estas paredes carmesim"
                            text "{i}neste exato instante. Meramente dizer isto acelera meu cora????o."
                            text "{i}E por mais covarde que eu saiba que isto ??, esta noite acredito que poderia e deveria faz??-lo."
                            text "{i}Diga-me, amigo, eu deveria? Abandonar o dever e agarrar"
                            text "{i}esta covarde salva????o com minhas pr??prias m??os?\""
                            text ""
                            text "{i}Naquela noite, a chama da bacia morreu pela primeira vez desde minha chegada, invernos atr??s."
                            text "{i}Meu pai acordou ?? meia-noite e chamou meu nome, em meio a sua n??voa de senilidade ele perguntou"
                            text "{i}\"Quem ?? este jovem a solu??ar que ou??o, e por que seus apelos s??o t??o desesperados?"
                            text "{i}Filho, onde estamos e que destino amaldi??oado caiu sobre este menino"
                            text "{i}para seus lamentos inspirarem tanta tristeza em mim?"
                            text "{i}N??o h?? nada que possamos fazer para confort??-lo?\""
                            text ""
                            text "{i}E para meu pai eu disse \"N??o, elimine a mem??ria de sua mente, pai,"
                            text "{i}o h??brido logo cumprir?? seu dever e a paz vir?? para ti.\""
                            text ""
                            text "{i}Um pre??o deve ser pago para fazer o que ?? certo, todos sabem."
                            text "{i}Trazer a morte a uma v??tima indefesa e volunt??ria deixa uma mancha na"
                            text "{i}alma de uma pessoa, um peso indel??vel, como aquele que esmaga Atlas."
                            text "{i}O h??brido suportou o peso do fim de meu pai e eu do dele."
                            text "{i}Um homem deve estar pronto para levar outros ?? morte para fazer o que ?? certo."
                            text "{i}Eu conhe??o esta velha sabedoria, ainda assim, por que n??o consigo conter meu cora????o acelerado?"
                            text "{i}Quanta madeira devo colocar sob sua pira para compensar minha irrever??ncia?"

                    if Memento == "Tablet16":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima Sexta T??bua: Ritual" xalign 0.5
                            text ""
                            text "Uma t??bua de argila retratando um crime contra a ordem divina."
                            text "A nenhum mortal ?? dado o direito de remover a eternidade concedida pelos Ol??mpios. Aquele que se levanta contra a ordem divina ?? amaldi??oado com o destino mais imundo."
                            text "A t??bua ?? adornada com a representa????o do rosto de um homem. O artista tentou esculpir olhos calmos, mas o processo de cozimento da t??bua deu-lhe uma express??o de horror, condizente com a maldi????o desencadeada por sua morte."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Seu nome era Titono, ele era meu pai."
                            text "{i}No ??pice de sua vida, quando eu estava no auge de minha masculinidade,"
                            text "{i}meu pai foi levado embora por Eos, tola deusa do amanhecer."
                            text "{i}Zeus o fez imortal, mas n??o jovem para sempre."
                            text "{i}Sua mente definhou, seu corpo secou em uma casca,"
                            text "{i}ainda assim, T??nato n??o o abra??ou, nem"
                            text "{i}Hermes Psicopompo o guiaria at?? as margens do Estige."
                            text ""
                            text "{i}Com sua casca amarrada ??s minhas costas, cruzei o mar at?? a terra de Creta"
                            text "{i}onde uma lua crescente que at?? mesmo os Destinos temiam estava escondida."
                            text "{i}O guardi??o do l??bris nos encontrou dentro da casa de D??dalo,"
                            text "{i}ele nos trouxe de volta ?? sa??de, apesar de seu medo do machado."
                            text "{i}Eu o persuadi a conceder miseric??rdia ao meu pai,"
                            text "{i}pois apenas aqueles com um toque do divino podem empunhar o Cortador de Fios."
                            text ""
                            text "{i}No cora????o do labirinto havia um santu??rio para os deuses e,"
                            text "{i}por sete invernos, um fogo ardeu dentro dele em uma ampla bacia."
                            text "{i}A chama eu subjuguei com minhas palavras e, sete noites depois,"
                            text "{i}colocamos o pesco??o de meu pai na borda da bacia."
                            text "{i}O l??bris rachou a pedra como um trov??o chacoalha a mente,"
                            text "{i}e assim cortou o fio de meu pai, aquele que os Destinos n??o tocariam."
                            text "{i}Seu recept??culo abandonado inclinou-se para o lado, como uma crian??a procurando o ombro da m??e"
                            text "{i}para cair no sono durante uma longa jornada de carruagem."
                            text ""
                            text "{i}Em sua velhice, meu pai adorava o cheiro de a??afr??o, embora seu apetite tenha quase cessado."
                            text "{i}Mel o fazia sorrir, ??s vezes rir. Quando segurava sua m??o,"
                            text "{i}seus dedos se entrela??avam com os meus, mesmo que sua mente tivesse ido embora."
                            text ""
                            text "{i}Um icor negro fluiu de seu ferimento para a bacia. Nela fizemos sua pira."
                            text "{i}?? medida que a chama lambia e beijava o recept??culo abandonado de meu pai,"
                            text "{i}o h??brido cantarolava no lugar de sua lira, a qual n??o mais tinha cordas para cantar."
                            text ""
                            text "{i}O fogo n??o limpou a bacia, nem sarou suas rachaduras."
                            text "{i}O santu??rio adquiriu um fedor indelevelmente f??tido, dentro dele, pesadelos sombrios"
                            text "{i}rastejariam ?? noite, gemendo e rindo."
                            text ""
                            text "{i}\"O santu??rio est?? profanado,\" disse Ast??rio enquanto eu fazia os preparativos para minha partida."
                            text "{i}\"N??o ?? mais um lugar de adora????o ou sacrif??cio. E o l??bris,"
                            text "{i}o qual jurei proteger, o sangue de Titono n??o sai dele."
                            text "{i}O que devo fazer, Laomedonte, como posso lavar esta blasf??mia de minhas m??os?\""
                            text ""
                            text "{i}Eu n??o tinha resposta para ele, e nenhuma palavra doce minha poderia distrai-lo."
                            text "{i}Quando deixei o cora????o do labirinto, ele ficou para tr??s,"
                            text "{i}\"Aguardarei meu redentor, ent??o, como os Destinos teceram."
                            text "{i}Ainda assim, voc?? me visitar??, Laomedonte, para manter minha solid??o sob controle?\""

                    if Memento == "Tablet17":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima S??tima T??bua: Pira" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando a liberta????o de um prisioneiro."
                            text "Diante da morte, faz-se bem em poupar as palavras."
                            text "Uma chama queimando em uma bacia adorna a parte inferior desta t??bua. As margens est??o alinhadas com c??rculos, provavelmente representando moedas."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Ele era Ast??rio, filho da Rainha Pas??fae e criado pelo Rei Minos."
                            text "{i}Ele foi gerado pelo touro branco de Poseidon com a ajuda do astuto D??dalo."
                            text "{i}Ele, o qual tinha cabelos de espuma do mar, chifres imaculados, aben??oados com o olhar de Hera,"
                            text "{i}de costas largas como as estepes e eternamente ?? espera do amanhecer,"
                            text "{i}libertou meu pai de algemas insuport??veis e,"
                            text "{i}ao fazer isto, tomou o peso de sua maldi????o."
                            text "{i}Juntos, sangramos icor na bacia da deusa e,"
                            text "{i}por nossa infinita arrog??ncia, incorreu sua ira para sempre e al??m."
                            text "{i}Eu permaneci em Creta, mas n??o vi as paredes carmesim do labirinto,"
                            text "{i}at?? que chegou a not??cia de um guerreiro ateniense favorecido por Ariadne,"
                            text "{i}O irm??o de berro alto de Ast??rio. Ela contou para ele o segredo"
                            text "{i}que eu trouxe, de acordo com os desejos do h??brido"
                            text "{i}??? mas, na verdade, ela j?? sabia, pois D??dalo lhe deixou o conhecimento."
                            text "{i}O ateniense aventurou-se no labirinto com um novelo de l??,"
                            text "{i}l?? ele encontrou seu alvo, a suposta besta tem??vel."
                            text ""
                            text "{i}O Pal??cio de Cnossos far?? voc?? acreditar que o Ast??rio nascido da brasa"
                            text "{i}lutou por sua vida contra a for??a do invasor."
                            text "{i}Mas eu corri para o labirinto assim que ouvi a palavra"
                            text "{i}e encontrei mais uma vez a bacia rachada cheia de preto e vermelho."
                            text "{i}Seu corpo estava deitado ao lado, em uma sonol??ncia sem cabe??a,"
                            text "{i}com o l??bris cortador de fios em seus cascos."
                            text "{i}De fato, seu redentor havia chegado e o libertado,"
                            text "{i}assim como, digo a mim mesmo, os pr??prios Destinos desejavam."
                            text ""
                            text "{i}Eu deveria acreditar que agora ele est?? livre de sua vida t??rrida,"
                            text "{i}que ele encontrar?? paz na companhia de seu descendente adotivo,"
                            text "{i}o virtuoso Rei Minos de Creta, que fundou este pa??s."
                            text "{i}Mas por que estou consumido pela m??goa e um peso inef??vel?"
                            text "{i}Eu olho para seus restos mortais e que f??ria me enche de ver"
                            text "{i}que o ateniense levou o chifre de meu amigo como trof??u."
                            text "{i}O l??bris amaldi??oado, as luas crescentes de Hefesto, ele deixou para tr??s,"
                            text "{i}agora manchados com fl??ido divino e mortal."
                            text ""
                            text "{i}Os guardas do Rei Minos chegaram quando eu completei sua pira."
                            text "{i}Eles n??o me pararam, na verdade, coletaram mais madeira,"
                            text "{i}mas o ??ltimo resqu??cio de osso do chifre imaculado eles levaram de volta ao rei."
                            text "{i}Uma moeda de ouro eu deixei debaixo da l??ngua de meu amigo, para apaziguar Caronte."
                            text "{i}Na bacia da qual ele fielmente cuidou, partiu desta terra."

                    if Memento == "Tablet18":
                        vbox spacing 10:
                            text "{i}{size=+2}D??cima Oitava T??bua: Esquiro" xalign 0.5
                            text ""
                            text "Uma t??bua de argila revelando um destino sinistro."
                            text "Um redentor assume as algemas daqueles que ele liberta. Esta cadeia ininterrupta se estende desde o nascimento da humanidade at?? os dias de hoje."
                            text "Nenhum ?? poupado."
                            text "Esta t??bua n??o possui enfeites."
                            text "Na t??bua est?? contido:"
                            text ""
                            text "{i}Eu continuo com minha jornada, agora que meu cora????o n??o pertence a nenhuma terra."
                            text "{i}Deixarei Creta para tr??s em busca de um lugar que acalme"
                            text "{i}esta f??ria implac??vel em meu peito."
                            text "{i}Eu olho para o mar do norte e me lembro do legado de meu pai,"
                            text "{i}que ele era realmente pr??ximo do monarca de Esquiro."
                            text "{i}?? como se os pr??prios Destinos me chamassem para l??,"
                            text "{i}e eu n??o tenho d??vidas de que a inten????o deles ?? que eu encontre meu redentor,"
                            text "{i}ou talvez torne-me um eu mesmo."
                            text ""
                            text "{i}O c??u estrelado deste mundo sobreviveu a todos os amanheceres destruidores de estrelas"
                            text "{i}e deve suport??-los por muito mais tempo."
                            text "{i}O c??u estrelado e os pecados dos homens continuaram,"
                            text "{i}Ast??rio n??o."

                    if Memento == "TypewriterScrap":
                        vbox spacing 10:
                            text "{i}{size=+2}Descarte de m??quina de escrever" xalign 0.5
                            text ""
                            text "Um peda??o de papel amassado encontrado por sua equipe de explora????o."
                            text "Est?? contido:"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}AqpqpqpqQPQPQP qaZxswed S3RVi??os ESCRIturas dezenove dezoiit oooooooo"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}ast??riup AST??RIO"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}DATIROGRAFIA minotaURO labirinto anexo plsklmdv skwjekmw"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}servi??os"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}continue"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}sozinhos"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}agress??o"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}dormindo"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}evolu????o"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}regresso"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}singular"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}quadrado"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}S E R V I ?? O S"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}L E N C E S L C"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}O S R E C E E O"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I S R L E D E N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}V E E S S I P T"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}R R E P G N I I"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}E G O R P R E N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I L E N O L E U"
                            text ""
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}S E R V I ?? O S ??"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}E N C E ?? S L E C"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}L E C E D I N E O"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}O R ??       G P N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}I ?? S       ?? I T"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}V S S       P E I"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}?? S E L R E E R N"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}R E R G O R P ?? U"
                            text "{size=-2}{font=fonts/LucidaConsole.ttf}E I L E N O L ?? E"
                            text ""
                            text ""
                            text "Mostrar isto ao minotauro faz suas orelhas ca??rem e seus ombros encolherem."
                            text "Ele explica que um mestre anterior havia trazido algumas publica????es e \"a coisa com os bot??es para imprimir letras\"."
                            text "Ao ver que todas as letras eram do mesmo tamanho, ele tentou, em suas pr??prias palavras, \"fazer um quadrado de palavras\"."
                            text "Ele n??o deseja ser lembrado disso."

                    if Memento == "PoemNotebook":
                        vbox spacing 10:
                            text "{i}{size=+2}Caderno encadernado em pele de cabra" xalign 0.5
                            text ""
                            text "Um pequeno caderno, um pouco menor que a m??o de um humano."
                            text "O mesmo poema ?? escrito em suas p??ginas uma d??zia de vezes, com varia????es diminutas a cada vers??o. Nas ??ltimas p??ginas, h?? um rabisco final, diferente de todos os outros."
                            text "A caligrafia ?? pobre e espasm??dica."
                            text ""
                            text "{u}COREGO"
                            text "{i}        Um gr??o de areia conduziu minha mente para muito tempo atr??s,"
                            text "{i}onde quer que a mem??ria pudesse sufocar minha garganta"
                            text "{i}ou cegar minha vis??o. Estou indefeso diante dela."
                            text "{i}        Uma mente muito aberta, muito ansiosa para lembrar,"
                            text "{i}e l??, problemas impressos eideticamente"
                            text "{i}onde pudessem estar. Um abra??o pode ser mantido"
                            text "{i}na mente, mas os golpes deixam contus??es sens??veis, cicatrizes,"
                            text "{i}as cicatrizes mais feias de amigos desconfiados:"
                            text "{i}Tudo baseado em suspeitas ocultas"
                            text "{i}sobre m??os de nervos salientes, truques e arrancadas ignorantes"
                            text "{i}a outra metade esqueceu. Se apenas eu"
                            text "{i}n??o tivesse esta armadilha certeira como pedra entre meus chifres."
                            text "{i}N??o posso evitar odiar minha posi????o, 'aben??oado'"
                            text "{i}solit??rio patriota da tensa Mnemosine."
                            text ""
                            text "{u}CORO"
                            text "{i}        \"Que tolice: branda indulg??ncia, lam??ria, e--\""
                            text "{i}        Est?? tudo cimentado; o que ?? luz apenas espuma"
                            text "{i}e flutua sobre o topo, fundo estagnado"
                            text "{i}e sufocante: Parado. Esta podrid??o c??ustica"
                            text "{i}n??o tem uso: n??o levanta nada como o fermento"
                            text "{i}nem delicia como a embriaguez. Por que continuar?"
                            text "{i}        \"Apenas pare. Este empreendimento simplesmente escapa de voc??.\""
                            text ""
                            text "{u}COREGO"
                            text "{i}        Uma pele mais grossa ?? necess??ria, mas"
                            text "{i}talvez com menos portas de entrada para rastrear"
                            text "{i}quem j?? conquistou sua autoestima, ent??o,"
                            text "{i}mais obteriam for??a, coragem e garantida"
                            text "{i}autossufici??ncia. Leva apenas uma vez:"
                            text "{i}um golpe bem posicionado manqueja o equil??brio."
                            text "{i}        Nenhuma for??a ?? obtida com exposi????o covarde"
                            text "{i}e cutucadas de teste quando as feridas est??o abertas, doloridas"
                            text "{i}e ainda sangrando. Um coagulante, ou"
                            text "{i}t??nico adstringente ?? necess??rio ??? sem atrito,"
                            text "{i}sangria, ossos realocados e ligados, toxinas"
                            text "{i}aplicadas em doses 'terap??uticas'. A esperan??a"
                            text "{i}?? a hipertrofia ??? mas ainda n??o ??? mas em breve???!???? ..."
                            text ""
                            text "{u}CORO"
                            text "{i}        \"Que tolice: branda indulg??ncia, lam??ria, e ???\""
                            text "{i}        Um ritmo que funciona, dura e cresce mais forte"
                            text "{i}evasivo ??. ?? tudo o que ?? simples aqui."
                            text "{i}O que o crescimento ??, n??o ?? impedido por torturas, ?? destru??do"
                            text "{i}por uma fonte o mais pr??xima poss??vel."
                            text "{i}A loucura de uma m??e herdou aqui?"
                            text "{i}        \"Apenas pare. Este empreendimento simplesmente escapa de voc??.\""
                            text ""
                            text ""
                            text "{i}        \"Eu sei que ofere??o muito pouco, mas"
                            text "{i}o pouco oferecido: precioso ??, eu espero.\""

                    if Memento == "RockCarving":
                        vbox spacing 10:
                            text "{i}{size=+2}Petr??glifo" xalign 0.5
                            text ""
                            text "Uma placa de rocha com inscri????es gravadas encontrada no Vale."
                            text "Algumas partes da rocha est??o faltando, ent??o ?? imposs??vel ler o poema completo."
                            text ""
                            text "{i}\"Chore, ??, grande m??e, pesar t??o profundo que nenhuma Musa Parnassana se prepararia antes que um pensamento sobre este apelo fizesse ----"
                            text "{i}Chame, ??, Poseidon, uma Musa muito mais resistente e destemida que ----"
                            text "{i}Por favor, ??, Melp??mene, cante versos cansados pelos corredores vermelhos de Cnossos, ricos ----"
                            text "{i}T??lia, n??o venha, ----\""

                    if Memento == "Agape":
                        vbox spacing 10:
                            text "{i}{size=+2}??gape, Eros, Filia" xalign 0.5
                            text ""
                            text "Um epigrama escrito para um pag??o romano ou gn??stico, pontificando sua conquista dos gregos."
                            text "Como de costume com todas as l??nguas estrangeiras escritas no labirinto, as letras mudam conforme voc?? focaliza seus olhos nelas, tornando o peda??o de pergaminho leg??vel."
                            text "No entanto, voc?? poderia jurar que alguns dos glifos que agora se referem ??s mesmas palavras pareciam diferentes para voc?? um momento atr??s."
                            text ""
                            text "{i}\"    'Mas amor n??o ?? amor, ?? mais como amor, ele me"
                            text "{i}disse, usando palavras da minha pr??pria l??ngua, de n??s"
                            text "{i}importado. Que compartimentaliza????o"
                            text "{i}esses romanos fazem! Eles falam como se o crep??sculo"
                            text "{i}n??o fosse ainda assim o sol!"
                            text ""
                            text "{i}    Eles levaram nossos deuses,"
                            text "{i}refizeram, remodelaram, misturaram os significados, nomes ???"
                            text "{i}um pante??o de desordem. Isto primeiro, mas ent??o"
                            text "{i}esses homens, com garo, encharcaram e afogaram nossa comida."
                            text "{i}E agora, eles me d??o serm??o usando nossas pr??prias palavras???\""

                    if Memento == "FieldWork":
                        vbox spacing 10:
                            text "{i}{size=+2}P??gina ilustrada rasgada" xalign 0.5
                            text ""
                            text "Um peda??o de papel antigo e amarelado com uma das pontas arrancadas. Voc?? presume que seja uma p??gina arrancada de um livro antigo."
                            text "A p??gina ?? adornada com uma ilustra????o de um minotauro arando um campo em tinta colorida azul e dourada."
                            if not main_menu:
                                if player_background in ['humanities', 'arts']:
                                    text "Um poema est?? escrito em tinta vermelha abaixo da ilustra????o. Voc?? reconhece que foi escrito usando o alfabeto grego; isto, combinado com o estilo e moldura da ilustra????o, dataria esta p??gina por volta da era Bizantina."
                                else:
                                    text "Um poema est?? escrito em tinta vermelha abaixo da ilustra????o. ?? escrito em um idioma estranho para voc??, mas as letras se alteram ?? medida que voc?? foca seus olhos, tornando o peda??o de papel leg??vel."
                            else:
                                text "Um poema est?? escrito em tinta vermelha abaixo da ilustra????o. ?? escrito em um idioma estranho para voc??, mas as letras se alteram ?? medida que voc?? foca seus olhos, tornando o peda??o de papel leg??vel."
                            text "?? uma ode ao trabalho no campo, ao inv??s de farra:"
                            text ""
                            text "{i}    \"Aveia selvagem! Qual a utilidade disto? O que faz"
                            text "{i}o pr??prio homem ?? a utilidade bem trabalhada"
                            text "{i}nos campos de ajuda e assist??ncia e dos produtos feitos."
                            text "{i}    Bem cuidados, estes corredores talvez tornem-se filas"
                            text "{i}por capricho do Mestre. Campos f??rteis estendem-se"
                            text "{i}com trabalhos manuais pisoteados, bem cobertos com c??u,"
                            text "{i}    atrav??s de corredores de trigo, milho e aveia os quais"
                            text "{i}nenhum Perses, est??pido, poderia deixar sem cultivar."
                            text "{i}O campo preparado legava bondade, n??o selvageria, pela m??o.\""

                    if Memento == "FoldedNote":
                        vbox spacing 10:
                            text "{i}{size=+2}Nota Dobrada" xalign 0.5
                            text ""
                            text "Um epigrama escrito para um ex-mestre prolixo, direto, ativo e vol??til."
                            text "Ao perguntar a Ast??rio sobre a nota, com pesar, ele explica que se lembra de ter dito o ??ltimo verso depois de n??o conseguir acompanhar o mestre, o que o deixou encantado. Ele exigiu um poema disso."
                            text ""
                            text "{i}\"Pare, por favor, ??, meu senhor ???"
                            text "{i}Rapido falante, movente audacioso,"
                            text "{i}Organizador h??bil ??? lento:"
                            text "{i}Eu ou??o r??pido demais.\""

                    if Memento == "Selene":
                        vbox spacing 10:
                            text "{i}{size=+2}Rabisco de caligrafia" xalign 0.5
                            text ""
                            text "Um epigrama escrito para Selena com uma caligrafia grosseira."
                            text ""
                            text "{i}\"A Lua est?? p??lida, fora de foco, fisgada."
                            text "{i}A cidade anuvia as estrelas, enquanto o vapor cobre a lua,"
                            text "{i}Eu corro sob seu largo sorriso.\""


                if FileType == 'Artifacts':
                    if Artifact == "Wine":
                        vbox spacing 10:
                            text "{i}{size=+2}Garrafa de Vinho" xalign 0.5
                            text ""
                            text "Uma garrafa contendo vinho m??gico que acelera a recupera????o de Ast??rio ap??s ferimentos."
                            text "Nem o Mestre nem o prisioneiro s??o capazes de invocar este vinho especial por meios convencionais, a maneira exata de faz??-lo ?? atualmente desconhecida."
                            text "Em que ocasionaria algu??m al??m de Ast??rio bebendo o vinho tamb??m ?? desconhecido."
                            text ""
                            if not main_menu:
                                if BundleSacrifice == 'Hestia':
                                    text "Argos relutantemente entregou a garrafa de vinho em troca de um sacrif??cio para H??stia, a deusa da lareira e do lar, feito na lareira dentro do hotel."
                                elif BundleSacrifice == 'Hades':
                                    text "Argos relutantemente entregou a garrafa de vinho em troca de um sacrif??cio para Hades, senhor dos mortos, feito em sua est??tua nos jardins do hotel."
                                elif BundleSacrifice == 'Hermes':
                                    text "Argos relutantemente entregou a garrafa de vinho em troca de um sacrif??cio para Hermes, mensageiro dos deuses, feito na bacia do alicerce do hotel."
                                elif BundleSacrifice == 'Zeus':
                                    text "Argos entregou a garrafa de vinho em troca de uma expedi????o para fazer um sacrif??cio a Zeus, rei dos deuses, na est??tua em sua homenagem no topo de um planalto no vale."
                                elif BundleSacrifice == 'Athena':
                                    text "Argos entregou a garrafa de vinho em troca de uma expedi????o para fazer um sacrif??cio a Atena, deusa da sabedoria, na est??tua em sua homenagem no todo de um planalto no vale."
                                else:
                                    text "A garrafa foi tirada de Argos ?? for??a."
                if FileType == 'Techs':
                    if Tech == "WiFi":
                        vbox spacing 10:
                            text "{i}{size=+2}Acesso ?? Internet" xalign 0.5
                            text ""
                            text "Atrav??s de uma combina????o de contratos e esquemas, voc?? conseguiu estabelecer uma conex??o ?? internet dentro do hotel."
                            text "Tudo isso ?? poss??vel pelo reaproveitamento de um santu??rio de Hermes no Alicerce do labirinto que estabelece uma conex??o com o mundo exterior."
                            text "Voc?? est?? atualmente usando um PSI uruguaio bastante lento e ter?? que pag??-los uma taxa, mas isto n??o deve ser um problema."
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
