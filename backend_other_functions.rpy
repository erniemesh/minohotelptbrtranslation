init python:

    def is_essential(reward):
        if reward in preset_rewards.keys():
            if "essential" in preset_rewards[reward]:
                return preset_rewards[reward]['essential']
        return False

    def list_into_text(my_list):
        output = ""
        if len(my_list) == 1:
            return str(my_list[0])
        else:
            for i, j in enumerate(my_list):
                if i+1 == len(my_list):
                    output = output + 'and ' + str(my_list[i])
                elif i+2 == len(my_list):
                    output = output + str(my_list[i]) + ' '
                else:
                    output = output + str(my_list[i]) + ', '
            return output


    def encrypt_rank(affection):
        affection = float(affection)
        if affection > 0:
            if affection.is_integer():
                word1 = "Great"
            else:
                word1 = "Grand"
        else:
            if affection.is_integer():
                word1 = "Fearsome"
            else:
                word1 = "Ruthless"

        if int(abs(affection)/4) not in preset_animal_ranks.keys():
            word2 = 'Auroch'
        else:
            word2 = preset_animal_ranks[int(abs(affection) / 4)]

        word3 = preset_metal_ranks[int(affection) % 4]

        return word1 + " " + word3 + " " + word2


    def decrypt_rank(rank):
        words = rank.split()
        metals_inverted = {v: k for k, v in preset_metal_ranks.items()}
        animals_inverted = {v: k for k, v in preset_animal_ranks.items()}

        if words[0] == "Great":
            num0 = 1
            num1 = 0
        elif words[0] == "Grand":
            num0 = 1
            num1 = 0.5
        elif words[0] == "Fearsome":
            num0 = -1
            num1 = 0
        elif words[0] == "Ruthless":
            num0 = -1
            num1 = 0.5

        num2 = metals_inverted[words[1]]

        if words[2] == 'Auroch':
            num3 = 8
        else:
            num3 = animals_inverted[words[2]]

        return ((num3 * 4) + num2 + num1) * num0


    def output_save_name(chapter_title):
        colors = {"math": "{color=[UIColorMath]}Math{/color}",
                  "tech": "{color=[UIColorTech]}Tech{/color}",
                  "leader": "{color=[UIColorLeader]}Leader{/color}",
                  "speedrunner": "{color=[UIColorSpeedrunner]}Speedrunner{/color}",
                  "humanities": "{color=[UIColorHumanities]}Humanities{/color}",
                  "arts": "{color=[UIColorArts]}Arts{/color}"}
        color = colors[player_background] if player_background in colors.keys() else ''
        return chapter_title + ', ' + color


    def scroll_speed_1(speed):
        if speed == 0:
            return 0
        else:
            return 1


    def scroll_speed_2(speed):
        if speed == 1:
            return 2
        else:
            return 1


    def current_file_type_value(file_type, contract, tech, profile, memento, artifact):
        if file_type == "Contracts":
            return contract
        elif file_type == "Techs":
            return tech
        elif file_type == "Profiles":
            return profile
        elif file_type == "Mementos":
            return memento
        else:
            return artifact


    def article_match(button_value, asterion_value, my_key='none'):
        if my_key in ['wedding_ring', 'nose_ring']:
            return (button_value == 'True') == asterion_value
        elif 'glass' in button_value:
            return button_value == asterion_value
        else:
            return button_value in asterion_value


    def shuffle_list(my_list):
        return sorted(my_list, key=lambda x: renpy.random.random())


    def print_on_textbox(text):
        renpy.say(narrator, text)


    def random_between(int1, int2):
        return renpy.random.randint(int1, int2)


    def show_team(name_list):
        if len(name_list)>0:
            renpy.show(name_list[0], [xalcenter] if len(name_list) != 2 else [xalright])
        if len(name_list)>1:
            renpy.show(name_list[1], [xalleft] if len(name_list) == 2 else [xallefter])
        if len(name_list)>2:
            renpy.show(name_list[2], [xalrighter])


    def hide_team(name_list):
        for guest in name_list:
            renpy.hide(guest)


    def pose_team(name_list, emote='neutral'):
        for guest in name_list:
            globals()[guest].change('posing', emote)


    def new_build_update():
        # updates configurations at the start of new build content
        load_reward_list(preset_rewards, rewards)
        load_relationships(preset_couple_stats, relationships)


    def check_in_guest(guest_name):
        guest = load_guest(guest_name, preset_guest_stats)
        guests.add_guest(guest)
        if guest_name not in persistent.known_guests:
            persistent.known_guests.append(guest_name)
