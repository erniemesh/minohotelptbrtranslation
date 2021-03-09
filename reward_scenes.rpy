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
        "Let's check in on the R&D team."
        if len(rd_team_names())==0:
            "Oh? It looks like no one is here.
            Your R&D team didn't make any progress."
        else:
            $reward=determine_rd_reward(rewards, inventory, guests, relationships)
            $accumulate_rd_stats()
            if reward == 'none':
                "Your R&D team made some progress, but no project was completed."
            else:
                if build < 4 or is_essential(reward):
                    $pose_team(rd_team_names(), 'victory')
                    "Oh? It looks like you completed a project!"
                    $ renpy.jump('RDReward_' + reward)
                else:
                    $pose_team(rd_team_names(), 'victory')
                    "Your current team can complete a project!
                    Do you want to complete your research, or continue working towards something else?"
                    $myChoices = rewards.get_reward_choices(inventory.accumulated_stats['RD'] + calculate_rd_team_stats(), inventory.raw_materials)
                    $narrator("Spend your research?", interact=False)
                    $result = renpy.display_menu(myChoices)
                    if result == 'none':
                        $pose_team(rd_team_names(), 'neutral')
                        "The team will keep its progress and work on other projects."
                    else:
                        $ renpy.jump('RDReward_' + result)

    #we return here after the scene with the reward we just claimed
    label RDrewardcheck:

    if UI_permissions['exploration']:
        scene bg valley
        $show_team(exploration_team_names())
        $pose_team(exploration_team_names(), 'neutral')
        with Dissolve(1.0)
        "Let's check in on the exploration team."
        if len(exploration_team_names())==0:
            "Well... no one was sent into the labyrinth."
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
                        "Other than that, your exploration team didn't make any big discoveries."
                    else:
                        "Your exploration team didn't find anything."
                else:
                    $pose_team(exploration_team_names(), 'victory')
                    if calculate_exploration_team_stats().get_value("Surveying") >=1:
                        "Oh? It looks like you found something else!"
                    else:
                        "Looks like your team found something!"
                    $ renpy.jump('EXReward_' + reward)
        #we return here after the scene with the reward we just claimed
    label EXrewardcheck:
    $hide_team(rd_team_names())
    #both teams are done. we return to the day the team processing was called from.
    $ renpy.jump(nextLabel)


label danger:
    #Your team fucked up and is in danger.
    $pose_team(exploration_team_names(), 'defeat')
    "The exploration team reports their findings.\n
    They were attacked by a creature in the depths of the Labyrinth."
    $RNJesus = renpy.random.randint(1, 100)
    if player_background == "speedrunner" and RNJesus <= 40:
        $loot = calculate_exploration_team_stats().get_value("Surveying")
        $pose_team(exploration_team_names(), 'victory')
        "However... somehow, your team pulled through unscathed.
        Not only that, they managed to loot [loot] raw materials from the creature!"
        "Some people would attribute this to sheer luck, or divine intervention.
        In your mind, your years spent perfecting resource management and your
        epic gamer skills and instincts were the true key to success."
        $inventory.raw_materials +=loot
    else:
        if danger_attack():
            #if you got attacked but avoided it successfully you can still claim a reward
            #if someone got injured you jump straight to the end
            jump EXrewardcheck
    jump EXreward

#survey extra rewards
label survey_Cool:
    "This is an example of an extra scene that happens when you get really lucky during surveys."
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

    "Greta" "[player_name]!{w=0.2} [player_name]! It's wonderful, everyone's having a blast!"

    you "Oh, hey Greta. What's going on, is the Internet working?"

    pause 1.0

    show Greta:
        ease 1.0 xalign 0.45

    "Greta" "...Internet?"

    pause 1.0
    show Greta:
        ease 0.5 xalign 0.5

    "Greta" "Oh, yes!{w=0.2} The Internet, silly me, how could I forget.{w=0.2}
    It is working, we did it, but that's not even the best thing."

    "Greta" "This whole experience here has given me so many amazing ideas,
    such incredible visions for research!{w=0.2} I wrote a document outlining a few
    of them and showed it to everyone!"

    show Greta:
        ease 0.3 yalign 1.0
        ease 0.3 yalign 1.1
    "Greta" "They are all so blown away by it,{w=0.2} they can't even take more than
    one idea or two before needing a break!"

    "Greta" "Oh, it's beautiful, [player_name]!{w=0.2} Everyone back at the
    Engineering department will be so jealous!"

    you "That's...{w=0.3} that's great, Greta.{w=0.2} I'm happy to hear that.{w}
    I'm sure everyone will love your...{w=0.3} ideas."

    you "So, I take it everything is set up and well?"

    show Greta:
        ease 0.3 yalign 1.0
        ease 0.3 yalign 1.1
    "Greta" "Yes, absolutely!{w=0.5}... More or less."

    "Greta" "We... we got the wi-fi to work,{w=0.2} but there was a whole mess about
    getting an Internet service provider and..."

    show Greta:
        xzoom -1
        ease 1.0 xalign 0.4

    "Greta" "We might be...{w=0.5}ha ha...{w=0.5} we might be using the Internet service
    provider the Uruguayans work for,{w=0.2} ok?"

    show Greta:
        xzoom 1
        ease 1.0 xalign 0.5
    "Greta" "So, things are very makeshift on that end, you see.{w=0.2}
    The broadband is very limited.{w} But it works!{w=0.2} Everything is in order."

    "Greta" "...But if something goes wrong, I'm afraid I have no idea how to fix it,{w=0.2} haha."

    "Greta" "I'm not a networks engineer.{w=0.2} Give me a break, ok?"

    "Greta" "You might want to send their central an e-mail every once in a while,{w=0.2}
    and you'll have to pay the bills too.{w} But I'm sure that will be easy for you,{w=0.2}
    with a magic hotel and all."

    "Greta" "Give me one minute,{w=0.2} we’re doing a stress test here,{w=0.2} be right back with you."

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
        luke "Hell yeah!{w=0.2} Check this shit out, [player_name]!"

        $Luke.change("emotion", "cocky")
        show Luke:
            ease 1.0

        "Luke borderline shoves his phone to your face. It has seen better days: its sides are
        dented and the screen is cracked and scratched all over, making it hard for you to read."

        "In fact, right now Luke's talons are adding new scratches just by gripping it."

        "However, you can make out a {i}lot{/i} of notifications on the top of the screen,
        and an all-caps conversation Luke is having with a contact nicknamed \"Ma\", followed
        by a healthy amount of heart emojis."

        $Luke.change("arm", "hip")
        show Luke:
            ease 1.0

    if 'Kota' in rd_team_names():
        $Kota.change("emotion", "happy")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "relaxed")

        kota "Isn’t this exciting news, Mister [player_name]?"

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        if 'Kota' == first_guest:
            kota "I do not use my phone a lot, but being able to look up recipes to cater to
            guests the world over is definitely a boon to any restaurant."
        else:
            kota "I do not use my phone a lot, but I am certain that this will make the
            guests’ stay more pleasant."

    if 'Asterion' in rd_team_names():
        $ global_affection += 1
        $Asterion.change("emotion", "laughing")

        asterion "We did it, Master."

        $Asterion.change("emotion", "contemplative")
        asterion "Well... I didn’t do much other than explain how to write contracts
        and make sure everything was in order, the others did the heavy lifting.{w=0.2}
        But I’m happy to have been able to help."

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
        asterion "Greta has been most helpful explaining these concepts to me throughout
        these sessions.{w=0.2} I feel like I caught up with some of the advancements I missed
        these last decades."
        $Asterion.change("emotion", "contemplative")
        asterion "I... still feel like I will need your help with learning the ropes, Master,
        but I feel more confident in my ability to do so."

    elif myList == 'Kota':
        $Kota.change("emotion", "happy")
        kota "Ah, and of course, Miss Greta has been most attentive."

        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        $Kota.change("emotion", "neutral")
        kota "I insisted it was not necessary, but since I was the least knowledgeable
        person in the room, she put me up to speed in a lot of these matters."

        $Kota.change("rightarm", "relaxed")
        kota "I hope I will be more helpful in the future."

    elif myList == 'Luke':
        $Luke.change("emotion", "laughing")
        luke "Also,{w=0.2} dang it,{w=0.2} I’m taking back everything I’ve said about
        the Germans. Greta’s been a doll this whole afternoon explaining all this mumbo
        jumbo to me,{w=0.2} it {i}almost{/i} makes sense now."

        $Luke.change("emotion", "wink")
        luke "If you need a hand tinkering with this stuff down the line,
        I think I might be able to help out a bit here and there."

    play sound "sfx/asterionchord.mp3"
    $guests.increase_guest_stat(myList, "Tech", 1)
    "[myList]'s {color=[UIColorTech]}Tech{/color} stat went up by 1!"

    you "This is incredible news.{w=0.2} So, should I try logging in?"

    #one of the team at random shows you how to log in
    $throwaway2 = rd_team_names()[renpy.random.randint(1, len(rd_team_names()))-1]

    if throwaway2 == 'Asterion':
        $Asterion.change("emotion", "smiling")
        asterion "Yes,{w=0.2} uh,{w=0.2} let me see if I recall the instructions..."

        asterion "The \"network\" is {i}’Minotaur Hotel’{/i}."
        $Asterion.change("emotion", "tired")
        asterion "And the password is..."

        "Asterion thinks for a couple of seconds with a strained expression,
        but then just points towards a strip of paper on the table."

        "You pick it up and it says:"

        contract "Password: Netzwerkdurchsetzungsgesetz"

        you "Ok,{w=0.2} we’re going to have to change that."

        asterion "That would be for the best.{w=0.2} She carefully detailed how to do it in
        one of these documents."

    elif throwaway2 == 'Luke':
        $Luke.change("emotion", "annoyed")
        luke "Well, you’re welcome to try.{w=0.2} The network is {i}\"Minotaur Hotel\"{/i},{w=0.2}
        but the password is some stupid German shit word that’s impossible to remember."

        $Luke.change("arm", "pointing")
        "Luke shows you the password in a memo on his phone.{w=0.2} You manage to read it,
        despite the claw marks and cracks in the screen making it almost impossible to do so."

        contract "Password: Netzwerkdurchsetzungsgesetz"

        you "Ok,{w=0.2} we’re going to have to change that."

        $Luke.change("arm", "hip")
        $Luke.change("emotion", "neutral")
        luke "I know, right?{w=0.2} She left some instructions on how to do it, thankfully."

    elif throwaway2 == 'Kota':
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        $Kota.change("emotion", "happy")
        kota "Why yes. You shouldn’t have a problem finding the network, since it’s the only one.
        It's called {i}\"Minotaur Hotel\"{/i}."

        $Kota.change("rightarm", "relaxed")
        kota "As for the password, well, it’s...{w=0.3} I hope I’m saying this right...
        {w=0.3} Netzwerkdurchsetzungsgesetz."

        you "Excuse me,{w=0.2} what?"

        $Kota.change("emotion", "sad")
        "Kota sighs, and hands you a slip of paper. It’s written in bright purple ink,
        in what you assume to be Greta’s handwriting."

        contract "Password: Netzwerkdurchsetzungsgesetz"

        you "Ok,{w=0.2} we’re going to have to change that."

        $Kota.change("emotion", "neutral")
        kota "Yes, it would seem prudent to do so.{w=0.2} She was nice enough to leave
        instructions on how to do it."

    you "So, Minotaur Hotel.{w} Ok, that’s memorable and to the point, I suppose."
    play sound "sfx/vibratephone.mp3"
    "You login and, for the first time in a long while, your wi-fi icon lights up."
    stop sound
    $obtain_reward('WiFi', 'RD')
    $add_file('Tech', "WiFi")

    play sound "sfx/asterionchord.mp3"
    "You managed to establish {color=[UIColorOrange]}internet access{/color} in the hotel.
    You can see your completed tech projects under the tech tab in
    the {color=[UIColorOrange]}Files{/color} screen in the pause menu."

    if len(exploration_team_names()) > 0:
        "The excitement in the room is palpable, but you have other responsibilities to attend to.
        You congratulate the team on a job well done, and go check on the exploration team."
    else:
        "The excitement in the room is palpable. You congratulate the team on a job well done,
        and stay with them for a while to celebrate."

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
    "You found a clay tablet narrating a dutiful son's journey to Crete.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet1', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet2:
    $add_file('Memento', "Tablet2")
    "You found a clay tablet narrating a cursed family's arrival to Crete.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet2', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet3:
    $add_file('Memento', "Tablet3")
    "You obtained a clay tablet narrating a rare audience with an ancient king.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet3', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet4:
    $add_file('Memento', "Tablet4")
    "You obtained a clay tablet narrating an intervention from a concerned youth.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet4', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet5:
    $add_file('Memento', "Tablet5")
    "You obtained a clay tablet narrating a man's encounter with one of divine nature.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet5', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet6:
    $add_file('Memento', "Tablet6")
    "You obtained a clay tablet revealing a child's hospitality.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet6', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet7:
    $add_file('Memento', "Tablet7")
    "You obtained a clay tablet narrating a small tragedy of human folly.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet7', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet8:
    $add_file('Memento', "Tablet8")
    "You obtained a clay tablet depicting a scene of treachery.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet8', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet9:
    $add_file('Memento', "Tablet9")
    "You obtained a clay tablet narrating a small tragedy of human folly.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet9', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet10:
    $add_file('Memento', "Tablet10")
    "You obtained a clay tablet revealing a bastard tempting a pious youth away from his duty.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet10', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet11:
    $add_file('Memento', "Tablet11")
    "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet11', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet12:
    $add_file('Memento', "Tablet12")
    "You obtained a clay tablet revealing a hybrid's foul nature.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet12', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet13:
    $add_file('Memento', "Tablet13")
    "You obtained a clay tablet revealing the hybrid's despondency.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet13', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet14:
    $add_file('Memento', "Tablet14")
    "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet14', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet15:
    $add_file('Memento', "Tablet15")
    "You obtained a clay tablet revealing a prisoner's last shred of hope.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet15', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet16:
    $add_file('Memento', "Tablet16")
    "You obtained a clay tablet depicting a crime against divine order.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet16', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet17:
    $add_file('Memento', "Tablet17")
    "You obtained a clay tablet revealing a prisoner's liberation.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet17', 'Exploration')
    jump EXrewardcheck

label EXReward_Tablet18:
    $add_file('Memento', "Tablet18")
    "You obtained a clay tablet revealing an ominous fate.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Tablet18', 'Exploration')
    jump EXrewardcheck

label EXReward_TypewriterScrap:
    $add_file('Memento', "TypewriterScrap")
    "You encountered a very old crumpled piece of paper: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('TypewriterScrap', 'Exploration')
    jump EXrewardcheck

label EXReward_PoemNotebook:
    $add_file('Memento', "PoemNotebook")
    "You encountered a tiny, goatskin-bound notebook, containing handwritten poetry.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('PoemNotebook', 'Exploration')
    jump EXrewardcheck

label EXReward_RockCarving:
    $add_file('Memento', "RockCarving")
    "You found a petroglyph: writing engraved into a slab of rock.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('RockCarving', 'Exploration')
    jump EXrewardcheck

label EXReward_Agape:
    $add_file('Memento', "Agape")
    "You found a poem written in very old parchment: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Agape', 'Exploration')
    jump EXrewardcheck

label EXReward_FieldWork:
    $add_file('Memento', "FieldWork")
    "You found an old page torn off a book: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('FieldWork', 'Exploration')
    jump EXrewardcheck

label EXReward_FoldedNote:
    $add_file('Memento', "FoldedNote")
    "You found an old page torn off a book: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('FoldedNote', 'Exploration')
    jump EXrewardcheck

label EXReward_Selene:
    $add_file('Memento', "Selene")
    "You found a handwritten poem: a small memento of Asterion's past.\n
    You can read it by opening the Files in the menu."
    $obtain_reward('Selene', 'Exploration')
    jump EXrewardcheck





label EXReward_Wine:
    $inventory.remove_item('Bundle')
    you "So... how’d that go?"

    if 'Luke' in exploration_team_names() and 'Kota' not in exploration_team_names():
        $throwaway1 = 'we' if 'Asterion' in exploration_team_names() else 'I'
        luke "[player_name],{w=0.2} [throwaway1] fucking did it.{w=0.2} Mission accomplished, pardner!"

        you "Really?{w} You sure you did it right?"

        $Luke.change("arm", "pointing")

        luke "Oh, you can bet the farm on it.{w=0.2} Just followed the instructions:
        walked south and saw the plateau with a couple statues on top. It was impossible to miss, really!"

        $Luke.change("arm", "hip")
        $Luke.change("emotion", "neutral")

        if 'Asterion' in exploration_team_names():
            $Asterion.change("emotion", "sad")
            luke "Now, when we got to the top, there were two statues:{w=0.2} a buff dude on a throne
            and a chick with a spear, shield and funny helmet on it."

            luke "Y’see I was gonna go with the spear lady,{w=0.2} because she looked like those old
            timey propaganda posters with the chick draped in the flag and shit.{w} Very vintage, you know?"

            $Luke.change("emotion", "annoyed")
            luke "But Asterion convinced me otherwise and,{w=0.2} hey,{w=0.2} I’ll trust what he says
            on these matters.{w} Besides, I had to throw the guy a bone, boss,{w=0.2}
            he looked fucking miserable the entire way there."
            $BundleSacrifice = 'Zeus'

            $Asterion.change("emotion", "tired")
            luke "Not to mention the legless crawling lady things didn’t leave him alone."

            you "You mean like the one that jumped at me?"
            $Luke.change("arm", "pointing")

            $Asterion.change("emotion", "sad")
            luke "Bingo.{w=0.2} Now, I was doing fine, you know,{w=0.2} half bird and all.{w}
            I’m light on my feet{w=0.2} — but, man, Asterion just had the worst fucking time.{w=0.2}
            Those things went ballistic whenever they saw him. "

            $Luke.change("arm", "hip")
            luke "I know we’re kinda tight on time for that bottle thing, but please,{w=0.2}
            next time spare the guy."

        else:
            luke "Now, when I got to the top, there were two statues:{w=0.2} a buff dude on a throne
            and a chick with a spear, shield and funny helmet on it."

            luke "The dude on the throne looked {i}good{/i},{w=0.2} let me tell you,{w=0.2} so I was
            gonna burn the thingy at his feet like a good boy."

            $Luke.change("emotion", "horny")
            luke "But...{w=0.2} I don’t know,{w=0.2} call me a softy, but the chick got me nostalgic,
            you know?{w} She looked like those old timey propaganda posters with the lady draped in
            the flag and shit."

            $Luke.change("arm", "salute")
            luke "It’s cheesy, I know, but I...{w=0.2} well, I put the bundle in front of her, lit it on fire,
            and did a little salute."
            $BundleSacrifice = 'Athena'

            $Luke.change("emotion", "surprise")
            luke "It was fucking scary, though.{w=0.2} On my way back the place was crawling with these weird
            legless lady things."

            you "You mean like the one that jumped at me?"

            $Luke.change("arm", "pointing")
            $Luke.change("emotion", "neutral")
            luke "Bingo.{w=0.2} Thankfully I’m light on my feet — you know,{w=0.2} half bird and all,{w=0.2}
            so I’m here in one piece."

        $Luke.change("arm", "pointing")
        $Luke.change("emotion", "cocky")
        luke "But what’s important is, go show that snake who’s boss, will ya?"

    elif 'Luke' not in exploration_team_names() and 'Kota' in exploration_team_names():
        $throwaway1 = 'We' if 'Asterion' in exploration_team_names() else 'I'

        kota "Mister [player_name], I’ll have you know that the task at hand is complete."

        you "That’s fantastic! Did you burn it in the right place?"
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "relaxed")
        $Kota.change("rightarm", "raised")
        kota "Well, there wasn’t much of a margin for error.{w=0.2} The instructions were very clear."

        $Kota.change("rightarm", "relaxed")
        $Asterion.change("emotion", "sad")
        kota "[throwaway1] walked south until we saw a small plateau with some large statues
        on top of it,{w=0.2} then followed the path to the top."

        if 'Asterion' in exploration_team_names():
            kota "So, atop the plateau there were two statues.
            According to Asterion they represent Zeus and Athena."

            $Kota.change("emotion", "puzzled")
            $Kota.change("leftarm", "raised")
            kota "Now, I have heard quite a lot of outrageous stories about Zeus,{w=0.2} so I first
            thought about doing a sacrifice to Athena.{w} But Asterion convinced me we should go
            with Zeus instead,{w=0.2} and I will trust his judgement before mine in these matters."
            $BundleSacrifice = 'Zeus'
            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "tired")
            kota "Sadly,{w=0.2} our return was more complicated than our arrival.{w} These...{w=0.3}
            legless,{w=0.2} wailing,{w=0.2} crawling creatures started approaching us."

            $Kota.change("leftarm", "relaxed")
            you "Oh right, one of those jumped at me yesterday."

            $Kota.change("emotion", "puzzled")
            kota "Yes, very unpleasant things.{w=0.2} Thankfully they didn’t come at me all at once."

            kota "Although I should say...{w=0.2} I may not look like it, but I can handle myself in
            a physical altercation, so regardless I wasn't under any peril.{w}
            But I don’t think I can say the same about Mister Asterion."

            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "sad")
            kota "[player_name]...{w=0.2} I must implore you, please refrain from sending
            Asterion to the valley again.{w} It felt like everything there — and I do not just
            refer to just the creatures — was out to get him."

            $Kota.change("emotion", "neutral")
            kota "Thankfully we are both here in one piece and the sacrifice to the Gods is fulfilled.{w=0.2}
            That is what matters."

        else:
            kota "So, atop the plateau there were two statues which...{w=0.2} based on my knowledge on Greek
            deities should represent Zeus and Athena."

            $Kota.change("emotion", "puzzled")
            $Kota.change("leftarm", "raised")
            kota "Now, I have heard quite a lot of outrageous stories about Zeus, so I
            put the bundle at Athena’s feet.{w=0.2} I burned it, recited a small prayer,
            and went on my merry way."
            $BundleSacrifice = 'Athena'
            $Kota.change("emotion", "sad")
            kota "...Which is what I would like to say but there was nothing merry about my return at all.{w}
            On my way back these...{w=0.2} legless,{w=0.2} wailing,{w=0.2}
            crawling creatures started approaching me."

            $Kota.change("leftarm", "relaxed")
            you "Oh right, one of those jumped at me yesterday."

            $Kota.change("emotion", "happy")
            kota "Thankfully they didn’t come at me all at once.{w=0.2} I may not look like it,
            but I can handle myself in a physical altercation — still, avoiding conflict is always good."

            kota "Regardless, what matters is: I am here in one piece,
            and the sacrifice to the Gods is fulfilled."

        you "Thank you,{w=0.2} Kota."

        $Kota.change("emotion", "laughing")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        kota "Please, it was the least I could do.{w=0.2} Now, enough chit-chat,
        I believe you have a reward to claim with a certain snake, do you not?"

    elif 'Luke' in exploration_team_names() and 'Kota' in exploration_team_names():
        luke "Actually, boss, not bad. Not bad at all."
        kota "Yes. I… we are happy to inform that the task is done."

        you "That’s great! Did you guys run into any issues?"

        $Luke.change("emotion", "neutral")
        $Luke.change("arm", "hip")
        $Asterion.change("emotion", "sad")
        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "relaxed")
        kota "Well, not at first."
        $Kota.change("leftarm", "relaxed")
        luke "See, getting to the plateau was the easy part. All we did was walk south and after
        a while we did see the plateau in the distance, you couldn’t miss it."
        $Luke.change("emotion", "annoyed")
        luke "I was expecting the snake to be lying and sending us on a wild goose chase
        but we had no problem getting there."

        if 'Asterion' not in exploration_team_names():
            $Luke.change("emotion", "neutral")
            kota "Atop the plateau there were two statues, which based on my knowledge of Greek
            deities represented Zeus and Athena."
            $Kota.change("emotion", "happy")
            $Luke.change("emotion", "horny")
            luke "It was funny, we just stopped for a second, looked at each other and decided to
            go with the big dude in the throne."
            $BundleSacrifice = 'Zeus'
            you "Well, I’m happy to see you’re both getting along better."
            $Luke.change("emotion", "annoyed")
            $Kota.change("emotion", "sad")
            kota "Well, I would say cooperation became a necessity, because of what happened next."
            $Luke.change("arm", "pointing")
            luke "Yeah, I think that fucking asshole sent us to an ambush, because when we started
            walking back these legless screaming things started crawling toward us."
            you "Oh, yes, I think one of those jumped at me yesterday."
            luke "Yeah, it was spooky shit."
            $Luke.change("arm", "hip")
            kota "Well, thankfully, they didn’t come at us all at once. I am… let’s just say, not
            a good runner, so we had to kick some of those out of our way."
            $Luke.change("emotion", "cocky")
            luke "I’ll be honest, I’m impressed with dragon boy here. Wouldn’t mind going a round
            or two with him."
            pause 1.0
            $Kota.change("emotion", "angry")
            kota "I {i}hope{/i} you mean a fight."
            $Luke.change("emotion", "horny")
            $Luke.change("arm", "pointing")
            luke "Whatever you want to call it."
            $Luke.change("arm", "hip")
            pause 1.0

        else:
            $Luke.change("emotion", "neutral")
            kota "Atop the plateau there were two statues, which Asterion explained represent Zeus
            and Athena. He suggested burning the bundle at the bottom of Zeus’ throne and we all agreed.
            It was a simple task."
            $BundleSacrifice = 'Zeus'
            $Luke.change("emotion", "annoyed")
            $Kota.change("emotion", "sad")
            $Asterion.change("emotion", "tired")
            luke "Now the hard part was getting back, because let me tell you, I think that fucking
            asshole sent us to an ambush, because when we started walking back these legless
            screaming things started crawling toward us."
            you "Oh, yes, I think one of those jumped at me yesterday."
            $Luke.change("arm", "pointing")
            luke "Yeah it was spooky shit."
            $Luke.change("arm", "hip")
            $Kota.change("rightarm", "raised")
            kota "Alas, they all went straight for Asterion. Mister [player_name], I know it was
            imperative to get all the help we could get this one time, but please,
            unless it is absolutely necessary, refrain from doing it in the future."

            $Kota.change("rightarm", "relaxed")
            $Asterion.change("emotion", "sad")
            luke "It wasn’t just the creatures, boss. The soil, the grass, the roots, the insects;
            everything was out to get him. He had a miserable time."
            $Luke.change("emotion", "neutral")

        $Kota.change("emotion", "neutral")
        $Kota.change("leftarm", "raised")
        $Kota.change("rightarm", "raised")
        kota "We’re back in one piece, which is what’s important."
        $Luke.change("emotion", "cocky")
        $Luke.change("arm", "pointing")
        luke "Yeah, now go show that snake who’s boss, will ya?"

    else:
        $Asterion.change("emotion", "sad")
        $Asterion.change("leftarm", "loose")
        $Asterion.change("rightarm", "loose")
        show Asterion:
            ease 0.05 xalign 0.503
            ease 0.05 xalign 0.5
            repeat
        pause 2.0
        asterion "I- I…"
        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")
        asterion "I completed the task, Master."
        pause 1.0
        show Asterion:
            ease 0.05 xalign 0.5
        you "I’m sorry for sending you out. It was the only way to get the bottle."
        $Asterion.change("leftarm", "loose")
        pause 3.0
        $Asterion.change("emotion", "sad")
        "Asterion doesn’t respond. He has a hard time maintaining eye contact with you."
        pause 1.0
        you "I’m sorry."
        pause 2.0
        "After a while, Asterion regains his composure, and slowly bows to you."
        $Asterion.change("emotion", "bowing")
        $Asterion.change("leftarm", "raised")
        asterion "Please, Master, don’t be. What matters is that the sacrifice is complete.
        I put the bundle next to a statue of Zeus at the shrine and set it on fire,
        and made it back. That is what matters."
        $BundleSacrifice = 'Zeus'
        pause 1.0
        $Asterion.change("emotion", "tired")
        $Asterion.change("leftarm", "loose")
        asterion "I-I do believe Argos is waiting for you, Master."
        you "Yes, I’ll go meet him right away."

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
        "You obtained a clay tablet narrating a dutiful son's journey to Crete.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet1', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet2':
        $add_file('Memento', "Tablet2")
        "You obtained a clay tablet narrating a cursed family's arrival to Crete.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet2', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet3':
        $add_file('Memento', "Tablet3")
        "You obtained a clay tablet narrating a rare audience with an ancient king.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet3', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet4':
        $add_file('Memento', "Tablet4")
        "You obtained a clay tablet narrating an intervention from a concerned youth.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet4', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet5':
        $add_file('Memento', "Tablet5")
        "You obtained a clay tablet narrating a man's encounter with one of divine nature.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet5', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet6':
        $add_file('Memento', "Tablet6")
        "You obtained a clay tablet revealing a child's hospitality.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet6', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet7':
        $add_file('Memento', "Tablet7")
        "You obtained a clay tablet narrating a small tragedy of human folly.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet7', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet8':
        $add_file('Memento', "Tablet8")
        "You obtained a clay tablet depicting a scene of treachery.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet8', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet9':
        $add_file('Memento', "Tablet9")
        "You obtained a clay tablet narrating a small tragedy of human folly.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet9', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet10':
        $add_file('Memento', "Tablet10")
        "You obtained a clay tablet revealing a bastard tempting a pious youth away from his duty.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet10', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet11':
        $add_file('Memento', "Tablet11")
        "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet11', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet12':
        $add_file('Memento', "Tablet12")
        "You obtained a clay tablet revealing a hybrid's foul nature.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet12', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet13':
        $add_file('Memento', "Tablet13")
        "You obtained a clay tablet revealing the hybrid's despondency.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet13', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet14':
        $add_file('Memento', "Tablet14")
        "You obtained a clay tablet revealing one of many tragedies leading to a boy's demise.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet14', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet15':
        $add_file('Memento', "Tablet15")
        "You obtained a clay tablet revealing a prisoner's last shred of hope.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet15', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet16':
        $add_file('Memento', "Tablet16")
        "You obtained a clay tablet depicting a crime against divine order.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet16', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet17':
        $add_file('Memento', "Tablet17")
        "You obtained a clay tablet revealing a prisoner's liberation.\n
        You can read it by opening the Files in the menu."
        $obtain_reward('Tablet17', 'Exploration', subtract=False)
    elif throwaway3 == 'Tablet18':
        $add_file('Memento', "Tablet18")
        "You obtained a clay tablet revealing an ominous fate.\n
        You can read it by opening the Files in the menu."
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
