init python:

    def rd_team_names():
        return guests.get_rd_team().names()

    def exploration_team_names():
        return guests.get_exploration_team().names()

    def accumulate_rd_stats():
        inventory.accumulate_stats(calculate_rd_team_stats(), 'RD')

    def accumulate_exploration_stats():
        inventory.accumulate_stats(calculate_exploration_team_stats(), 'Exploration')

    def team_in_danger():
        ex_stats = calculate_exploration_team_stats().filter_exploration(UI_permissions['fragments'])
        return "Danger" in ex_stats.top_stats() and ex_stats.get_value('Danger') != 0

    def obtain_reward(reward_name, team='RD', subtract=True):
        rewards.obtain_reward(reward_name)
        if subtract:
            stat_cost, material_cost = rewards.get_stat_requirement(reward_name)
            inventory.spend_stats(stat_cost, team)
            inventory.raw_materials -= material_cost

    def advance_guest_route(guest_name, amount=1):
        guests.advance_guest_route(guest_name, preset_guest_route_length, amount)

    def advance_relationship(guest1, guest2, amount=1):
        relationships.advance_relationship([guest1, guest2], amount, max_progress=preset_maximum_relationship_length[guest1+','+guest2], guest_list=guests)

    def calculate_rd_team_stats():
        rd_team = guests.get_rd_team()
        rd_team_stats = rd_team.sum_stats()
        passive_bonus = inventory.get_passive_bonus()
        relationship_bonus = relationships.get_relationships_with_guests(rd_team.names()).sum_bonus()
        return rd_team_stats + passive_bonus + relationship_bonus

    def calculate_exploration_team_stats():
        ex_team = guests.get_exploration_team()
        ex_team_stats = ex_team.sum_stats()
        passive_bonus = inventory.get_passive_bonus()
        relationship_bonus = relationships.get_relationships_with_guests(ex_team.names()).sum_bonus()
        return ex_team_stats + passive_bonus + relationship_bonus


    def determine_reward(reward_list, team_stats, team=None, materials=0):
        if team == "RD":
            team_stats = team_stats.filter_rd()
        if team == "Exploration":
            team_stats = team_stats.filter_exploration()
        if len(reward_list.possible_rewards(stats=team_stats, team=team, material=materials)) > 0:
            reward_list.sort_rewards(team_stats.list_stats())
            return reward_list.possible_rewards(stats=team_stats, team=team, material=materials)[0].name
        else:
            return 'none'


    def determine_rd_reward(reward_list, inventory, guest_list, relationship_list):
        team_stats = inventory.accumulated_stats['RD'] + calculate_rd_team_stats()
        return determine_reward(reward_list, team_stats, team='RD', materials=inventory.raw_materials)


    def determine_exploration_reward(reward_list, inventory, guest_list, relationship_list):
        team_stats = inventory.accumulated_stats['Exploration'] + calculate_exploration_team_stats()
        return determine_reward(reward_list, team_stats, team='Exploration', materials=inventory.raw_materials)


    def advance_day(days=1):
        daily_events.advance_days(days)
        guests.advance_day(days)

    def danger_attack():
        # upon a failed danger event determines which teammates get attacked.
        someone_injured = False
        guest_name_list = guests.get_exploration_team().names()
        for guest_name in guest_name_list:
            chance = random_between(1, 7 if player_background == 'speedrunner' else 5)
            if chance < 4:
                someone_injured = True
                days = 'a day' if chance == 1 else str(chance) + " days"
                print_on_textbox(guest_name + " is injured. He will take " + days + " to recover.")
                guests.disable_guest(guest_name, chance)
        if not someone_injured:
            print_on_textbox("Thankfully, no one was injured. You make a mental note to be more careful next time.")
        return someone_injured


    def get_relationship_routes():
        can_start= guests.get_guests_can_start_relationship().names()
        can_date = guests.get_guests_can_date().names()
        return relationships.get_available_couple_routes(can_start, can_date, preset_current_relationship_length)

    def get_relationship_maximum_length(guest1, guest2):
        couple_key = guest1+','+guest2
        if couple_key not in preset_maximum_relationship_length.keys():
            couple_key = guest2+','+guest1
        return preset_maximum_relationship_length[couple_key]


    def survey():
        # determines your survey reward.
        # if you meet a special reward the function returns a special label
        my_label = 'none'
        survey_stat = calculate_exploration_team_stats().get_value("Surveying")
        random_number = random_between(1, 100)
        if player_background == "speedrunner":
            random_number += 10
        if random_number <= 10:
            print_on_textbox("Your team didn't find any raw materials.")
        elif random_number < 60:
            print_on_textbox("Your team found " + str(survey_stat) + " raw materials!")
            inventory.raw_materials += survey_stat
        else:
            survey_stat *= 2
            print_on_textbox("Your team got really lucky, and found " + str(survey_stat) + " raw materials, twice what you expected!")
            inventory.raw_materials += survey_stat
        # if random_number == 100:
        #    my_label='Cool'
        # example of an extra surveying reward if you get super lucky
        return my_label
