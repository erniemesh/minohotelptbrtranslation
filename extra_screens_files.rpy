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
                            text "{i}{size=+2}Asterion's Sentence" xalign 0.5
                            text ""
                            text "{i}Hereby the gods of Olympus sentence the Prisoner Asterion to eternal damnation for his meekness and cowardice in the face of adversity."
                            text "{i}With this sentence his prison is created, a Labyrinth born out of the gods' ichor."
                            text "{i}The Labyrinth shall welcome lost mortals with nowhere to go. Among them, a Jailer will be picked to command and rewrite the realm."
                            text "{i}The Jailer and the Labyrinth's mission is to secure the Prisoner's eternal torture."
                            text "{i}The Jailer shall enjoy power and freedom to rewrite the Labyrinth as to better enact his vision."
                            text "{i}Asterion of Crete, adopted son to King Minos, and every drop of his blasphemous blood is hereby sentenced to the Labyrinth."
                            text "{i}By this decree the gods' will is done."
                    elif Contract == "Servitude":
                        vbox spacing 10:
                            text "{i}{size=+2}Asterion's Oath of Servitude" xalign 0.5
                            text ""
                            text "{i}By the provisions under the Statute of Joseph the Merciful, the Prisoner Asterion pledges loyalty and servitude to the Labyrinth's Master."
                            text "{i}The Prisoner is made Keeper of the Hotel above the valley, and is bequeathed the power to realize the Master's will."
                            text "{i}The Master in turn binds the Labyrinth, forbidding its malicious entities from leaving said valley."
                            text "{i}The realm was engineered to torture the Prisoner, and indeed its mission shall be accomplished. The Prisoner will carry the burden of servitude, but shall not suffer the Labyrinth's wrath within the Hotel's territory."
                            text "{i}The Prisoner, shielded by his Master's will, is made safe as long as his duty is fulfilled, under the terms of the Statute."

                    elif Contract == "ArgosContract":
                        vbox spacing 10:
                            text "{i}{size=+2}Contrato de Argos" xalign 0.5
                            text ""
                            text "{i}This document binds the Master of the Labyrinth and the snake known as Argos Panoptes, henceforth referred to as \"the Foreman\", together in an agreement."
                            text "{color=[UIColorOrange]}{i}Article One."
                            text "{i}The Master leases to the Foreman the authority to summon food, water, shelter, and furniture for use however he sees fit, including for the benefit of the cultivation of crops and raising of animals."
                            text "{i}In return, the Foreman leases the Mirror of Hestia for the Master's use however he sees fit, including for the benefit and maintenance of the structure known as \"The Hotel\" as established in previous contracts."
                            text "{color=[UIColorOrange]}{i}Article Two."
                            text "{i}The Master and the lessee shall refrain from bringing harm to the other, directly and indirectly, by means including but not limited to violence, incentivizing or rewarding third parties towards aggression against the other, sabotaging structures, poisoning food and water, among others."
                            text "{color=[UIColorOrange]}{i}Article Three."
                            text "{i}The Master is forbidden from directly and indirectly interfering with the the full enjoyment of the Foreman's rights granted under this contract. The Foreman is similarly forbidden from bringing harm to \"The Hotel.\""
                            text "{color=[UIColorOrange]}{i}Article Four."
                            text "{i}The Master is allowed to conduct inspections on the Foreman's accommodations, save for the Foreman's personal quarters, whose access is forbidden."
                            text "{i}The Foreman is forbidden from conspiring against the Master and shall not use the rights granted by this Contract to bring him harm. The Master and Foreman are symmetrically bound this Article, including but not limited to not using Hestia's Mirror to bring harm to the Foreman."
                            text "{color=[UIColorOrange]}{i}Article Five."
                            text "{i}This contract is self-enforcing. If any of its articles are broken then possession of Hestia's Mirror reverts to the Foreman and any flame lit by the Mirror is put out."
                            text "{i}At the same time the Foreman loses the rights transferred by the contract and any and all structures summoned by him cease to exist after a 10 minute interval to allow for evacuation."
                            text "{color=[UIColorOrange]}{i}Article Six."
                            text "{i}This self-enforcing contract is made effective at the moment of its signing, and remains valid during the Master's reign and until the following Master acquires the Hotel's Deed."
                            text "{i}By the will of the Master, to whom the Olympians' reign over the realmwas granted, this contract is established."

                    elif Contract == "Rings":
                        vbox spacing 10:
                            text "{i}{size=+2}Oath of the Binding Rings" xalign 0.5
                            text ""
                            text "A blasphemous contract that defies the gods' will, proposed by the prisoner in an attempt to reveal the Master's truest intentions."
                            text "In its first incarnation the lead ring was imposed on the prisoner and set to trigger if impossible conditions were not met. But, much like the very realm where the hotel was built, its purpose has been corrupted and subverted by humanity."
                            text "Perhaps there is wisdom in that ancient memory that a redeemer takes on the shackles of those he liberates. Contemporary humanity, however, would instead find virtue in a lord who willfully limits himself from using his power."
                            text ""
                            text "{i}By the will of the Labyrinth's Master this binding contract is established, so it may enforce its contents upon the world and its people."
                            text "{i}Hereby the Master commands into existence two linked objects: a lead ring to fit around a man's bicep, and a laurel wreath as wide as the prisoner's arm."
                            text "{i}These two objects shall be linked in cause and effect, as will their wearers."
                            text "{i}Whoever dons the lead ring will find it impossible to be removed, except through the revoking of this contract."
                            text "{i}Whoever first dons the laurel wreath shall become its permanent and unchangeable owner."
                            text "{i}If the owner of the laurel wreath is ever made to go to the Labyrinth's valley —either by coercion, command, or forcing— then the lead ring shall constrict and close as to amputate its bearer’s arm."
                            text "{i}By the Master's will, this contract may only be revoked if all its parties — bearer of the lead ring, owner of the laurel wreath, and the two eyewitnesses present during its signing — consent to it."
                            text "{i}Such is the Master's will."

                if FileType == 'Mementos':
                    if Memento == "Tablet1":
                        vbox spacing 10:
                            text "{i}{size=+2}First Tablet: Crescent Moon" xalign 0.5
                            text ""
                            text "A clay tablet narrating a dutiful son's journey to Crete."
                            text "In Ancient times even a short trip would take years. Braving the sea always held the threat of death, so travel was reserved for blood-thirsty warriors, ambitious merchants and desperate wretches."
                            text "This tablet is decorated with crude crescent moon motifs. He who created them lacked the artisan's talent but not his care."
                            text "The tablet reads:"
                            text ""
                            text "{i}It cut through my father's neck like the sickle-harvested saffron from these rocky shores,"
                            text "{i}that unassuming crescent moon born of Hephaistos' brilliance and Zeus' turbulence."
                            text ""
                            text "{i}From Asia Minor I came, bearing my father's weight on my back as he once carried me."
                            text "{i}During the spring of my life, and winter of his, we crossed the sea to King Minos' Crete."
                            text "{i}While my ailing father sailed his nightmares of old age I worked the oars"
                            text "{i}and prayed to the trickster from King Lycaon's court, whose wisdom set us in this course."
                            text ""
                            text "{i}Over the short sea we made our way to Crete, greeted by the wild ibex's horns."
                            text "{i}There I would find Hephaistos' finest work, the crescent moons of Olympus —"
                            text "{i}those which bring night even to an immortal's restless visage."
                            text "{i}I am Laomedon, bastard son of Tithonus, once prince of Troy."
                            text "{i}The sea I crossed and the labyrinth I roamed, for my father I would do it all,"
                            text "{i}no cost too high, no load too great, no trick unused."
                            text "{i}Hear the tale of father's liberation at the hands of the lonesome keeper of labyrinth"
                            text "{i}and the hybrid's demise under the envoy of the gods."

                    if Memento == "Tablet2":
                        vbox spacing 10:
                            text "{i}{size=+2}Second Tablet: Arrival" xalign 0.5
                            text ""
                            text "A clay tablet narrating a cursed family's arrival to Crete."
                            text "There was once a man named Minos, son of Zeus and Europa. He founded Crete, the island-state from which Greek culture descends. Legends speak highly of the monarch's virtue, after death said to have earned his place among Hades' judges."
                            text "Generations later, however, another Minos would take on the throne, one with a disposition that angered gods and men alike."
                            text "This tablet is decorated with simple drawings of a wild goat's head. Its horns stand proud, framing a single, lonesome star."
                            text "The tablet reads:"
                            text ""
                            text "{i}Tithonus was my father, his was the hand which taught me to sail these bountiful waters."
                            text "{i}Together we stalked and flew arrows at aurochs, on the reddened, wet soil made our feast."
                            text "{i}We herded and milked sheep, made the cheese, and shared it with our neighbors,"
                            text "{i}but my father was robbed from me by the witless goddess of dawn, Eos."
                            text "{i}She took him as husband and he, mortal, what choice did he have?"
                            text ""
                            text "{i}Witless dawn lobbied Zeus to make him immortal, so she would never lose her pet."
                            text "{i}Like a king who knows not the weight of gold he made my father undying"
                            text "{i}but, as the trickster of Lycaon said, did not remember mortals' aging, ephemeral nature."
                            text "{i}Now his mind is ravaged by age, even if his sickly-thin body will still not cease."
                            text ""
                            text "{i}That day when I docked my vessel on Crete's shore I carried him on my back to Knossos."
                            text "{i}He bumbled like a baby past in his first spring, I bore his weight as he once did mine."
                            text "{i}To Crete I brought my father, to release him of this wretched, god-given blessing."
                            text "{i}During autumn and winter I pleaded at the foot of Knossos' palace for King Minos' mercy."

                    if Memento == "Tablet3":
                        vbox spacing 10:
                            text "{i}{size=+2}Third Tablet: Audience" xalign 0.5
                            text ""
                            text "A clay tablet narrating a rare audience with an ancient king."
                            text "Crimson columns still stand on Crete's ancient sites, a lasting memory of a bygone era. The labyrinthine Palace of Knossos, albeit consumed and rotted, outlived kings and gods."
                            text "This tablet is decorated with repetitive column motifs, but close scrutiny reveals trace amounts of a rare, precious treasure powdered over it: saffron."
                            text "The tablet reads:"
                            text ""
                            text "{i}King Minos' atop his crimson palace refused to grant us audience,"
                            text "{i}but swift-footed I hunted the wild ibex's of his coast and feasted with his people."
                            text "{i}The leather I fashioned into clothes, for my father first and for Cretans second."
                            text "{i}I harvested the saffron and grains, a guest was I among each of Knossos' families"
                            text "{i}until they all heard of my father's woeful tale and were incited to rage against the gods."
                            text ""
                            text "{i}King Minos feared our tale and the spread of impiety among the populace."
                            text "{i}Under cover of night we were taken to his court, pushed across the rows of crimson columns."
                            text "{i}We were fed and clothed with Cretes' traditional attires, and my father I bathed"
                            text "{i}for only I know how to handle his skin, more delicate than the asphodel's petals."
                            text ""
                            text "{i}At long last we arrived at his court, then I carried father against my chest like a newborn."
                            text "{i}Over a straw mat I laid him for the King to see the woe born from Zeus' blessing"
                            text "{i}and pleaded for Hephaistos' crescent moons, his finest creation"
                            text "{i}which cleaved Zeus' skull and so gave birth to Athena, ever wiser than her father."
                            text ""
                            text "{i}For it's a son's duty to care for his parents during their old age,"
                            text "{i}And 'tis my duty to release father from his everlasting ailment."
                            text "{i}I am Laomedon, son of undying Tithonus, abandoned husband to witless Eos"
                            text "{i}and I seek Crete's Labrys, so sharp as to cut his immortal Fates-woven thread."
                            text "{i}For such a wretched, accursed pair no cost is too great, no load too terrible."

                    if Memento == "Tablet4":
                        vbox spacing 10:
                            text "{i}{size=+2}Fourth Tablet: Young Woman" xalign 0.5
                            text ""
                            text "A clay tablet narrating an intervention from a concerned youth."
                            text "Ancient times were ruled by the principle that might makes right. Women who wished to impose their will unto the world had to rely on subterfuge and wits."
                            text "This tablet is decorated with a single line at its bottom, the silhouette of Mount Aegaeon; the location where, legend tells, Zeus was raised."
                            text "The tablet reads:"
                            text ""
                            text "{i}When summer arrived and King Minos had not yet granted us his blessing"
                            text "{i}a young woman sneaked her way into our tent and told me of the labyrinth"
                            text "{i}— at the foot of a mountain, the very same where Zeus spent his youth —"
                            text "{i}where we would find a fearsome hybrid, a fiend born from the queen's affair with a beast."
                            text ""
                            text "{i}During my saffron-harvesting afternoons the wives told me of such a beast,"
                            text "{i}once known as a deity of prosperity paraded by King Minos,"
                            text "{i}locked away to the labyrinth's confines after taking to cannibalism."
                            text "{i}He, the young woman said, guards the Labrys of Crete,"
                            text "{i}gift of Zeus to his birthplace, at the very center of the labyrinth."
                            text ""
                            text "{i}\"Seek the cursed fiend at the world's heart,"
                            text "{i}in the crimson shrine he keeps the thread-cutting axe."
                            text "{i}But know, bastard of Troy, that only those inspired by the divine "
                            text "{i}may raise it — pray for Athena's blessing."
                            text "{i}Touch it not; it is coated with Zeus' ichor."
                            text "{i}'Tis not a man's lot to grasp divine matter.\""
                            text ""
                            text "{i}I departed with my father that same night,"
                            text "{i}from the distance I glimpsed Zeus' mountain."
                            text "{i}It grew closer with each passing day,"
                            text "{i}much like my father's suffering came to a close."

                    if Memento == "Tablet5":
                        vbox spacing 10:
                            text "{i}{size=+2}Fifth Tablet: Fiend" xalign 0.5
                            text ""
                            text "A clay tablet narrating a man's encounter with one of divine nature."
                            text "For the Greeks, to be a hybrid is to be a monster. The two are indissociable."
                            text "Divine or not, a hybrid is an accursed, repulsive being which good people would do well to ostracize."
                            text "This tablet is decorated with labyrinthine lines at its margins."
                            text "A clay tablet narrating an intervention from a concerned youth."
                            text "The tablet reads:"
                            text ""
                            text "{i}At the foot of Mount Aegaeon, on the Lasithi Plateau, I found the labyrinth,"
                            text "{i}an old structure painted with the same crimson from Knossos' Palace,"
                            text "{i}built and carved with an expert artisan's loving care."
                            text "{i}Try as I might, from atop the mountain I could not learn its twists,"
                            text "{i}for its shape shifted with each blink of my eyes."
                            text ""
                            text "{i}A club on my hand, father on my back, we ventured together"
                            text "{i}with the comfort of knowing that, even if I failed, his pain still would cease."
                            text "{i}For three days and nights we wandered, hearing only the song of cicadas"
                            text "{i}and the clopping of distant hooves, always just out of reach."
                            text "{i}The fiend toyed with us, never once showing its visage."
                            text "{i}I feared starvation would take my life, and cried for father's."
                            text ""
                            text "{i}On the fourth day the creature showed itself, Pasiphae's hybrid monster."
                            text "{i}It was not the fearsome titan I was told ate the flesh of men —"
                            text "{i}its pink snout, shy horns and glimmering eyes were that of a nursing calf."
                            text ""
                            text "{i}I challenged it to combat, certain that at long last"
                            text "{i}I would have an end to this charade,"
                            text "{i}but he bolted down his unending hallways,"
                            text "{i}leaving behind only the silencing clops of hooves."

                    if Memento == "Tablet6":
                        vbox spacing 10:
                            text "{i}{size=+2}Sixth Tablet: Child" xalign 0.5
                            text ""
                            text "A clay tablet revealing a child's hospitality."
                            text "The Greeks had extensive customs and norms dictating how a guest ought to be treated. In those ancient times gods in disguise walked among men, so it was expected that a host treat his guests with the respect the divine deserved."
                            text "To bring woe into a host's home was an unforgivable atrocity which would surely inspire curses upon one's bloodline."
                            text "This tablet is adorned with depictions of a temple, or perhaps a shrine. A butchered bull lies at its entrance."
                            text "The tablet reads:"
                            text ""
                            text "{i}I hunted the archer's calf but in truth I was made prey."
                            text "{i}By the fourth night I had collapsed. Only then did the boy"
                            text "{i}reveal himself from a bend up ahead."
                            text ""
                            text "{i}\"I am Asterion, adopted son of King Minos, and guardian to Daedalus' home."
                            text "{i}This is a holy ground; at its heart there is a shrine, at its center lies a basin"
                            text "{i}on which burns a holy fire gifted by the gods themselves."
                            text "{i}I was taught the art of hospitality, to wash a guests' feet"
                            text "{i}and provide two thirds of my meal to thee."
                            text "{i}I would welcome thee dearly — were there not weapons on your grasp."
                            text "{i}Tell me, why would you raise your arm against the gods?\""
                            text ""
                            text "{i}With what little voice was left in my cracked throat I responded:"
                            text "{i}\"It is against divine folly I turn, not the gods themselves."
                            text "{i}I am Laomedon, son of Tithonus, in turn husband to the goddess Eos;"
                            text "{i}this husk I carry is what she left behind. She pleaded Zeus to make him undying"
                            text "{i}but in her witless daze did not ask for eternal youth."
                            text "{i}Old age kidnapped his mind, his bones are now brittle"
                            text "{i}and his skin is as delicate as a moth's wings."
                            text "{i}I heard tale that in Crete, at the labyrinth's heart, one can find"
                            text "{i}a crescent moon weapon, a labrys of Hephaistos' making,"
                            text "{i}capable of severing an immortal's thread.\""
                            text ""
                            text "{i}Perhaps a seasoned warrior would have thrown aside my tale"
                            text "{i}and left me to starve and rot in these endless hallways."
                            text "{i}But children know not that a beggar may hide a knife under his cloak."

                    if Memento == "Tablet7":
                        vbox spacing 10:
                            text "{i}{size=+2}Seventh Tablet: Ichor" xalign 0.5
                            text ""
                            text "A clay tablet narrating a small tragedy of human folly."
                            text "One's body is a vessel given by the gods, knowing full well that it is human fate to be mangled, broken and maimed. Let pain take you away, for what is human suffering but a blip on a god's existence?"
                            text "This tablet bears no adornments."
                            text "The tablet reads:"
                            text ""
                            text "{i}The hybrid guided my father and I to a crimson shrine —"
                            text "{i}a stone abode housing a shallow pool of clear waters,"
                            text "{i}at its center lies a stone basin on which burns the holy flame."
                            text "{i}To its west there is a smaller shrine, at its center there is a wide slab"
                            text "{i}of polished stone on which Crete's two-headed axe is stuck."
                            text ""
                            text "{i}I remembered then the young lady's words, that only one"
                            text "{i}favored by the divine could wield the thread-cutting axe."
                            text "{i}The hybrid boy warned me against it, but the brashness of manhood"
                            text "{i}rendered me deaf to all words of caution."
                            text ""
                            text "{i}To this day I carry the burn marks in my hands;"
                            text "{i}to this day the axe is imbued with Zeus' ichor,"
                            text "{i}it rebelled against mortal touch and striked back."

                    if Memento == "Tablet8":
                        vbox spacing 10:
                            text "{i}{size=+2}Eighth Tablet: Labryskeeper" xalign 0.5
                            text ""
                            text "A clay tablet depicting a scene of treachery."
                            text "Mothers often warn their children from speaking to strangers. This prince's mother, however, had long ago given up on words and fallen into a wailing madness. Left to his own devices, many important lessons were never taught to him."
                            text "This tablet is adorned with a traditionally Cretan motif, the two-headed axe."
                            text "The tablet reads:"
                            text ""
                            text "{i}For three days and nights I recovered from my burns."
                            text "{i}The hybrid willfully assumed the role of caretaker for my father and I."
                            text "{i}What hospitality he showed, my wounds he cleaned,"
                            text "{i}my father he readjusted two dozen times per day so no bedsores would ail him."
                            text ""
                            text "{i}All the while, I pleaded for his help; \"Have you not divinity within?"
                            text "{i}For your sire is Poseidon's bull, your mother is Pasiphae the nymph."
                            text "{i}Surely the labrys shall yield to thee; cut then my father's thread"
                            text "{i}and release him from this gods-given curse.\""
                            text ""
                            text "{i}The pristine-horned hybrid looked at me with beady eyes."
                            text "{i}\"Indeed, the axe burns not my skin but its weight is immense,"
                            text "{i}never have I dislodged it from its stone. Alas, my good prince,"
                            text "{i}did you not say Zeus himself granted your father the gift of eternity?"
                            text "{i}What right have I to strip away that which the Cronides gave?\""
                            text ""
                            text "{i}\"The gods all granted us life and the Fates strip us from it."
                            text "{i}It is only natural for man to give death unto other —"
                            text "{i}did the gods not spill ichor in their Titanomachy?"
                            text "{i}Man only mimics that which the Olympians taught."
                            text "{i}Wouldst one such as thee, with inhuman features,"
                            text "{i}believe yourself above the duty of bloodshed?"
                            text "{i}Fret not, a peculiar nature exempts you not from duty."
                            text "{i}There is mercy in ending one's suffering,"
                            text "{i}and yet more grace in being vanquished by the craft of Hephaistos."
                            text "{i}Please, hospitable lord of the labyrinth, assist this son in his just mission;"
                            text "{i}fear not the axe's weight for I shall train you."
                            text "{i}Your visage will harden with maturity,"
                            text "{i}your back shall grow to be as wide as the steppes,"
                            text "{i}your thunderous bellow shall split the walls."
                            text "{i}I shall train you much the same way my father taught me."
                            text "{i}For as long as necessary I shall stand by your side, until the day"
                            text "{i}your might towers over the weight of Hephaistos' crescent moons.\""

                    if Memento == "Tablet9":
                        vbox spacing 10:
                            text "{i}{size=+2}Ninth Tablet: Lyre" xalign 0.5
                            text ""
                            text "A clay tablet narrating a small tragedy of human folly."
                            text "Music lasts only a moment, but it can be forever held in one's mind."
                            text "This tablet is adorned with the drawing of a lyre. The cooking process, however, made the strings tear."
                            text "The tablet reads:"
                            text ""
                            text "{i}Many a night we spent in that crimson shrine,"
                            text "{i}comforted by the boy's lyre and the basin's flame."
                            text "{i}Before and after every meal Asterion would pay Hestia her due and beyond,"
                            text "{i}sometimes going hungry for her greater glory."
                            text ""
                            text "{i}Night after night I pleaded for his help but he would not have it."
                            text "{i}So I employed my wit, persuade him I would with honeyed tongue."
                            text "{i}In-between my father's moans I would ask,"
                            text "{i}he would answer without ceasing his song, fingers grazing the threads."
                            text ""
                            text "{i}\"Why is it that you stay here, child?"
                            text "{i}The plateau around us is vast and beautiful."
                            text "{i}Are thou not a prince, descended from a blessed queen?"
                            text "{i}Many are the joys royalty well deserves to enjoy."
                            text "{i}When was the last time you picked crocuses"
                            text "{i}and grazed your fingers on their petal-hidden softness?"
                            text "{i}When did you last bathe on Crete's coast?"
                            text "{i}Is it not in your wealth to robe yourself in vibrant purples and reds?"
                            text "{i}How many moons has it been since at dawn"
                            text "{i}you greeted the fishermen to buy their fresh catch?\""
                            text ""
                            text "{i}\"I do not know for sure, sir,\" answered the child, eyes glimmering against fire."
                            text "{i}His ears flickered along with the chilly wind."
                            text "{i}\"Perhaps seven winters it has been since I bartered with the fishermen,"
                            text "{i}six since my hooves last felt the sea's cold embrace,"
                            text "{i}five since I last held my sister's hand on our way to the fields to gather flowers,"
                            text "{i}four since I have worn nothing but rough fabrics"
                            text "{i}and last had someone to exchange words with."
                            text "{i}But not a night has gone by when I did not pluck my lyre's strings"
                            text "{i}nor a day in which the gods' dues went unpaid."
                            text "{i}Lonely as the labyrinth may be, am I not named after the stars?"
                            text "{i}I find companionship among them, tracing them with a finger,"
                            text "{i}and inside my own mind of which none can strip me."
                            text "{i}Before your arrival I thought; from dawn to dusk,"
                            text "{i}my mind raced with stories and possibilities."
                            text "{i}The sea I shan't see until father relieves me of duty"
                            text "{i}but its foam I can forever hold in the palm of my mind.\""

                    if Memento == "Tablet10":
                        vbox spacing 10:
                            text "{i}{size=+2}Tenth Tablet: Seafoam" xalign 0.5
                            text ""
                            text "A clay tablet revealing a bastard tempting a pious youth away from his duty."
                            text "Crete is not known for its venomous snakes. It is of no surprise, then, that the one who would tempt a prince away from his duty came from across the sea."
                            text "This tablet is adorned with wave-like motifs."
                            text "The tablet reads:"
                            text ""
                            text "{i}\"The coast is not far, much less the crocuses for which this island is known."
                            text "{i}Let us depart tomorrow upon the break of dawn, I shall take your hand"
                            text "{i}as we cross this plateau and feast our eyes upon its colors."
                            text "{i}Let this shrine's crimson be forgotten, run your fingers over the purple petals"
                            text "{i}and sink your hooves on the sandy shores and murky waters."
                            text "{i}Tomorrow, you and I, upon the break of dawn,"
                            text "{i}let us leave this captivity behind and rejoice.\""
                            text ""
                            text "{i}But the son of Minos would not entertain such impious ideas."
                            text "{i}\"That I must not do, for I gave my word to father, that I would not leave"
                            text "{i}the home Daedalus built. I must tend to the shrine and guard the labrys,"
                            text "{i}lest ruin befall our land and all its people."
                            text "{i}You are a prince as much as I — a bastard too."
                            text "{i}As much as it is our right to partake in royalty's pleasures,"
                            text "{i}duty shackles myself alone.\""
                            text ""
                            text "{i}\"We shall return before nightfall, Asterion.The shrine will not go unmaintained,"
                            text "{i}nor will Hestia's tribute go unoffered. Let us harvest a dash of saffron and offer it to her,"
                            text "{i}our adventure will bring joy to her homely visage."
                            text "{i}No man will know of our transgression, only the sea's foamy waters.\""
                            text ""
                            text "{i}He caressed his lyre's strings, plucking here and there."
                            text "{i}\"But I would know, and that is bad enough."
                            text "{i}You would do well to etch my sentence on your mind."
                            text "{i}Forget not the Fates did not see fit for I to be man,"
                            text "{i}nor did they weave the sea's foam or the flower's saffron on my tapestry."
                            text "{i}Inside the labyrinth I shall remain, for that is my promise.\""

                    if Memento == "Tablet11":
                        vbox spacing 10:
                            text "{i}{size=+2}Eleventh Tablet: Barter" xalign 0.5
                            text ""
                            text "A clay tablet revealing one of many tragedies leading to a boy's demise."
                            text "This clay tablet is adorned with flower motifs, which cracked and warped during the cooking process."
                            text "The tablet reads:"
                            text ""
                            text "{i}The night stretched ahead, a veil of fear and darkness covered us."
                            text "{i}A fire brimmed in my chest, perhaps in his as well."
                            text "{i}No offer of pleasures could convince him to leave,"
                            text "{i}or to take up the thread-cutting axe to release my father."
                            text "{i}A sharp crack awakened me from thought —"
                            text "{i}a single ember jumped from the basin down to the shallow pool."
                            text "{i}I saw it fizzle and die, alone and cold —"
                            text "{i}what sharpness it brought to my eyes!"
                            text "{i}An idea leaped out from me before my own prudence took hold."
                            text "{i}\"Dawn-awaiting prince of Crete, for a dozen days"
                            text "{i}has my father and I taken shelter in your abode,"
                            text "{i}eating from your food and water."
                            text "{i}As I said it was my mission to release father from pain,"
                            text "{i}to deliver him to the shores of Nyx, to the hands of Charon."
                            text "{i}I am grateful for your hospitality — so would Tithonus,"
                            text "{i}had he mind enough to spare."
                            text "{i}I wished to share with you a final memory of joy,"
                            text "{i}a single day of joy as we comb these beaches."
                            text "{i}But that is not the case; your duty is too great."
                            text "{i}Then it is with sorrow that I must announce:"
                            text "{i}at the break of dawn father and I shall leave"
                            text "{i}the labyrinth and the soils of Crete, for somewhere"
                            text "{i}beyond these cloudy waters must there be another one,"
                            text "{i}inspired by the Olympians, who can end our journey.\""
                            text ""
                            text "{i}Dawn-awaiting Asterion ceased his song and closed his eyes."
                            text "{i}Grief seemed to consume him; a knot formed in his throat."
                            text "{i}When words left him they were cracked and faltering."
                            text "{i}\"You know the arts of combat, do you not?"
                            text "{i}Your father, in his prime, taught you of a blade's sharpness."
                            text "{i}How long would it take for I to muster the might"
                            text "{i}to wield Hephaistos' treasure, the thread-cutting axe?"
                            text "{i}Perhaps your words held wisdom, after all;"
                            text "{i}one must rise up to grant mercy and liberation"
                            text "{i}to a prisoner shackled by misfortune and disgrace."
                            text "{i}I will do it, prince of Troy, I shall master the labrys"
                            text "{i}if you would grant me a simple, humble request:"
                            text "{i}do not leave me alone.\""

                    if Memento == "Tablet12":
                        vbox spacing 10:
                            text "{i}{size=+2}Twelfth Tablet: Offering" xalign 0.5
                            text ""
                            text "A clay tablet revealing a hybrid's foul nature."
                            text "To be a hybrid is to be cursed to a life of misfortune much greater than any mortal's."
                            text "This clay tablet is adorned with fire motifs, although the cooking process warped and distorted it."
                            text "The tablet reads:"
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
