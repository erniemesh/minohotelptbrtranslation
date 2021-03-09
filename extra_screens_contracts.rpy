screen ContractApproval(contract, choices):
    $Size = "A" if renpy.variant("android") else "D"
    image "gui/contractbg.png" xalign 0.5 yalign 0.5 alpha 0.8

    side "c r":
        area (150, 120, 980, 400)

        viewport id "vp":
            draggable True
            mousewheel True

            if contract == 'Argos1':
                vbox spacing 20:
                    text "{color=[UIColorContract]}{i}Este documento compromete o Mestre do Labirinto e a cobra conhecida como Argos Panoptes, de agora em diante referido como \"o Capataz\", juntos em um acordo."
                    vbox spacing 5:
                        text "{color=[UIColorContract]}{size=+2}Artigo Um" xalign 0.1
                        text "{color=[UIColorContract]}{i}O Mestre aluga ao Capataz a autoridade para invocar comida, água, abrigo e mobília para uso como ele achar adequado, inclusive para o benefício do cultivo de safras e a criação de animais."
                        text "{color=[UIColorContract]}{i}Em retorno, o Capataz aluga o Espelho de Héstia para uso do Mestre como ele achar adequado, inclusive para o benefício e manutenção da estrutura conhecida como \"Hotel\", conforme estabelecido em contratos anteriores."
                    vbox spacing 5:
                        text "{color=[UIColorContract]}{size=+2}Artigo Dois" xalign 0.1
                        text "{color=[UIColorContract]}{i}O Mestre e o arrendatário devem abster-se de causar danos um ao outro, direta e indiretamente, por meios incluindo, mas não limitados à violência, incentivando ou recompensando terceiros à agressão mútua, sabotando estruturas, envenenando alimentos e água, entre outros."
                    vbox spacing 5:
                        text "{color=[UIColorContract]}{size=+2}Artigo Três" xalign 0.1
                        text "{color=[UIColorContract]}{i}O Mestre é proibido de interferir direta ou indiretamente no pleno gozo dos direitos do Capataz concedidos neste contrato. O Capataz é similarmente proibido de causar danos ao \"Hotel.\""
                    vbox spacing 5:
                        text "{color=[UIColorContract]}{size=+2}Artigo Quatro" xalign 0.1
                        text "{color=[UIColorContract]}{i}O Mestre está autorizado a fazer inspeções nas acomodações do Capataz, exceto em seus aposentos pessoais, cujo acesso é proibido."
                        text "{color=[UIColorContract]}{i}O Capataz está proibido de conspirar contra o Mestre e não deve usar os direitos garantidos por este Contrato para prejudicá-lo. O Mestre e o Capataz estão simetricamente comprometidos a este Artigo, incluindo, mas não limitando-se a não usar o Espelho de Héstia para causar danos ao Capataz."
                    vbox spacing 5:
                        text "{color=[UIColorContract]}{size=+2}Artigo Cinco" xalign 0.1
                        text "{color=[UIColorContract]}{i}Este contrato é auto-impositivo. Se qualquer um de seus artigos for quebrado, a posse do Espelho de Héstia reverte para o Capataz e qualquer chama acesa pelo Espelho é apagada."
                        text "{color=[UIColorContract]}{i}Ao mesmo tempo, o Capataz perde os direitos transferidos pelo contrato e toda e qualquer estrutura por ele invocada deixa de existir após um intervalo de 10 minutos para permitir a evacuação."
                    vbox spacing 5:
                        text "{color=[UIColorContract]}{size=+2}Artigo Seis" xalign 0.1
                        text "{color=[UIColorContract]}{i}Este artigo auto-impositivo entra em vigor no momento de sua assinatura e permanece válido durante o comando do Mestre e até que o Mestre posterior adquira a Escritura do Hotel."
                    text "{color=[UIColorContract]}{i}Pela vontade do Mestre, a quem o comando dos Olímpios sobre o domínio foi concedido, este contrato é estabelecido."

        vbar value YScrollValue("vp")

    vbox xalign 0.5 yalign 0.85 spacing 10:
        text "{color=[UIColorContract]}{i}Qual artigo você quer disputar?" xalign 0.5
        hbox xalign 0.5 spacing 20:
            for choose in choices:
                hbox spacing 10:
                    if renpy.variant("android"):
                        imagebutton auto "gui/A_ContractBlock_%s.png":
                            action Return(choose)
                    else:
                        imagebutton auto "gui/D_ContractBlock_%s.png":
                            action Return(choose)
                    text "{color=[UIColorContract]}{i}[choose]" yalign 0.5
