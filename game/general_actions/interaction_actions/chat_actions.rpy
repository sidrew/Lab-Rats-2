init -1 python:
    #Chat actions shown with all girls. Add to these lists to have options displayed when talking to someone.
    chat_actions = [] #Default actions that are displayed when you are talking to a girl. Remember to set is_fast = False if an event can advance time.

    small_talk_action = Action("Make small talk   {color=#FFFF00}-15{/color} {image=gui/extra_images/energy_token.png}", requirement = small_talk_requirement, effect = "small_talk_person",
        menu_tooltip = "A pleasant chat about your likes and dislikes. A good way to get to know someone and the first step to building a lasting relationship. Provides a chance to study the effects of active serum traits and raise their mastery level.")
    chat_actions.append(small_talk_action)

    compliment_action = Action("Compliment her   {color=#FFFF00}-15{/color} {image=gui/extra_images/energy_token.png}", requirement = compliment_requirement, effect = "compliment_person",
        menu_tooltip = "Lay the charm on thick and heavy. A great way to build a relationship, and every girl is happy to receive a compliment! Provides a chance to study the effects of active serum traits and raise their mastery level.")
    chat_actions.append(compliment_action)

    flirt_action = Action("Flirt with her   {color=#FFFF00}-15{/color} {image=gui/extra_images/energy_token.png}", requirement = flirt_requirement, effect = "flirt_person",
        menu_tooltip = "A conversation filled with innuendo and double entendre. Both improves your relationship with a girl and helps make her a little bit sluttier. Provides a chance to study the effects of active serum traits and raise their mastery level.")
    chat_actions.append(flirt_action)


    make_girlfriend_action = Action("Ask her to be your girlfriend", requirement = ask_girlfriend_requirement, effect = "ask_be_girlfriend_label",
        menu_tooltip = "Ask her to start an official, steady relationship and be your girlfriend.", priority = 10)
    chat_actions.append(make_girlfriend_action)

    bc_talk_action = Action("Talk about her birth control", requirement = bc_talk_requirement, effect = "bc_talk_label",
        menu_tooltip = "Talk to her about her use of birth control. Ask her to start or stop taking it, or just check what she's currently doing.")
    chat_actions.append(bc_talk_action)

    date_action = Action("Ask her on a date", requirement = date_option_requirement, effect = "date_person",
        menu_tooltip = "Ask her out on a date. The more you impress her the closer you'll grow. If you play your cards right you might end up back at her place.", is_fast = False)
    chat_actions.append(date_action)


    specific_actions = [] #Default "agressive" actions that are displayed when talking to a girl.

    grope_action = Action("Grope her   {color=#FFFF00}-5{/color} {image=gui/extra_images/energy_token.png}", requirement = grope_requirement, effect = "grope_person",
        menu_tooltip = "Be \"friendly\" and see how far she is willing to let you take things. May make her more comfortable with physical contact, but at the cost of her opinion of you.")
    specific_actions.append(grope_action)

    command_action = Action("Give her a command", requirement = command_requirement, effect = "command_person",
        menu_tooltip = "Leverage her obedience and command her to do something.")
    specific_actions.append(command_action)

init -2 python:
    def always_true_requirement():
        return True

    def small_talk_requirement(the_person):
        if mc.energy < 15:
            return "Requires: 15{image=gui/extra_images/energy_token.png}"
        return True

    def compliment_requirement(the_person):
        if the_person.love < 10:
            return "Requires: 10 Love"
        elif mc.energy < 15:
            return "Requires: 15{image=gui/extra_images/energy_token.png}"
        return True

    def flirt_requirement(the_person):
        if the_person.love < 10:
            return "Requires: 10 Love"
        elif mc.energy < 15:
            return "Requires: 15{image=gui/extra_images/energy_token.png}"
        return True

    def date_option_requirement(the_person):
        if the_person.love < 20:
            return "Requires: 20 Love"
        return True

    def lunch_date_requirement(the_person):
        love_requirement = 20

        if time_of_day < 2:
            return "Too early to go for lunch"
        elif time_of_day > 2:
            return "Too late to go for lunch"
        elif the_person.love < love_requirement:
            return "Requires: " + str(love_requirement) + " Love"
        return True

    def movie_date_requirement(the_person):
        love_requirement = 30
        if the_person.relationship == "Girlfriend":
            love_requirement += 10
        elif the_person.relationship == "Fiancée":
            love_requirement += 15
        elif the_person.relationship == "Married":
            love_requirement += 20
        if the_person.relationship != "Single":
            love_requirement += -10*the_person.get_opinion_score("cheating on men")
        if love_requirement < 30:
            love_requirement = 30

        if the_person.love < love_requirement:
            return "Requires: " + str(love_requirement) + " Love"
        elif mc.business.event_triggers_dict.get("movie_date_scheduled", False):
            return "Already planned movie date!"
        elif day%7 == 1 and time_of_day >= 3:
            return "Too late to plan movie date"
        return True


    def dinner_date_requirement(the_person):
        love_requirement = 40
        if the_person.relationship == "Girlfriend":
            love_requirement += 20
        elif the_person.relationship == "Fiancée":
            love_requirement += 30
        elif the_person.relationship == "Married":
            love_requirement += 40
        if the_person.relationship != "Single":
            love_requirement += -10*the_person.get_opinion_score("cheating on men")
        if love_requirement < 40:
            love_requirement = 40

        if the_person.love < love_requirement:
            return "Requires: " + str(love_requirement) + " Love"
        elif mc.business.event_triggers_dict.get("dinner_date_scheduled", False):
            return "Already planned dinner date!"
        elif day%7 == 4 and time_of_day >= 3:
            return "Too late to plan dinner date"
        return True

    def evening_date_trigger(day_of_week): #Used for a mandatory crisis that triggers on the next Friday in turn 3.
        if time_of_day == 3 and day%7 == day_of_week: #Day of week is a number from 0 to 6, where 0 is Monday.
            return True
        return False

    # TODO: Decide if this is even needed with the new serum/sex change
    def serum_give_requirement(the_person):
        #the_person parameter passed to match other actions and for future proofing.
        if mc.inventory.get_any_serum_count() <= 0:
            return "Requires: Serum in inventory"
        return True

    def seduce_requirement(the_person):
        if the_person.sluttiness < 15:
            return "Requires: {image=gui/heart/three_quarter_red_quarter_empty_heart.png}"
        return True

    def grope_requirement(the_person):
        if the_person.sluttiness < 5:
            return False #Don't show the option at all at minimal sluttiness.
        elif the_person.event_triggers_dict.get("last_groped", (-1,-1)) == (day, time_of_day):
            return "Just groped her"
        elif mc.energy < 5:
            return "Not enough {image=gui/extra_images/energy_token.png}"
        return True

    def command_requirement(the_person):
        if the_person.obedience < 105:
            return "Requires: 105 Obedience"
        elif mc.energy < 10:
            return "Not enough {image=gui/extra_images/energy_token.png}"
        return True

    def change_titles_requirement(the_person):
        if the_person.obedience < 105:
            return "Requires: 105 Obedience"
        return True

    def serum_demand_requirement(the_person):
        if the_person.has_role(employee_role):
            #It's easier to convince her if she works for you
            if the_person.obedience < 110:
                return "Requires: 110 Obedience"
            elif mc.inventory.get_any_serum_count() <= 0:
                return "Requires: Serum in inventory"
            return True

        else:
            if the_person.obedience < 120:
                return "Requires: 120 Obedience"
            elif mc.inventory.get_any_serum_count() <= 0:
                return "Requires: Serum in inventory"
            return True

    def wardrobe_change_requirment(the_person):
        if the_person.obedience < 120:
            return "Requires: 120 Obedience"
        return True

    def bc_talk_requirement(the_person):
        if persistent.pregnancy_pref == 0:
            return False
        elif the_person.effective_sluttiness() < 20 and the_person.love < 20:
            return False
        elif the_person.has_role(pregnant_role): # don't talk about bc when she is pregnant
            return False
        return True

    def demand_touch_requirement(the_person):
        if the_person.obedience < 125: #TODO: Note: This isn't based on sluttiness directly, but we should have some dialogue reference to it.
            return "Requires: 125 Obedience"
        return True

    def suck_demand_requirement(the_person):
        if the_person.has_taboo("sucking_cock"):
            return False #Doesn't appear until you've broken the taboo in the first place
        elif the_person.obedience < 150:
            return "Requires: 150 Obedience"
        return True


    def demand_strip_requirement(the_person):
        if demand_strip_tits_requirement(the_person) == True or demand_strip_underwear_requirement(the_person) == True or demand_strip_naked_requirement(the_person) == True:
            return True
        return False

    def demand_bc_requirement(the_person):
        if persistent.pregnancy_pref == 0: #Don't talk about pregnancy if we don't want any of it.
            return False
        elif the_person.obedience < 100:
            return False
        elif the_person.obedience < 115:
            return "Requires: 115 Obedience"
        else:
            return True

    def build_person_introduction_titles():
        title_tuple = []
        for title in get_player_titles(the_person):
            title_tuple.append([title,title])
        return title_tuple

    def get_date_plan_actions(the_person):
        lunch_date_action = Action("Ask her out to lunch {image=gui/heart/Time_Advance.png}", lunch_date_requirement, "lunch_date_plan_label",
            menu_tooltip = "Take her out on casual date out to lunch. Gives you the opportunity to impress her and further improve your relationship.")
        movie_date_action = Action("Ask her out to the movies", movie_date_requirement, "movie_date_plan_label",
            menu_tooltip = "Plan a more serious date to the movies. Another step to improving your relationship, and who knows what you might get up to in the dark!")
        dinner_date_action = Action("Ask her out to a romantic dinner", dinner_date_requirement, "dinner_date_plan_label",
            menu_tooltip = "Plan a romantic, expensive dinner with her. Impress her and you might find yourself in a more intimate setting.")

        date_list = [[lunch_date_action, the_person], [movie_date_action, the_person], [dinner_date_action, the_person]]
        for a_role in the_person.special_role:
            for a_date in a_role.role_dates:
                date_list.append([a_date, the_person])

        date_list.insert(0, "Select Date")
        date_list.append(["Never mind", None])
        return date_list

    def create_movie_date_action(the_person):
        movie_action = Action("Movie date", evening_date_trigger, "movie_date_label", args=the_person, requirement_args=1) #it happens on a tuesday.
        mc.business.mandatory_crises_list.append(movie_action)
        mc.business.event_triggers_dict["movie_date_scheduled"] = True
        return

    def create_dinner_date_action(the_person):
        dinner_action = Action("Dinner date", evening_date_trigger, "dinner_date_label", args=the_person, requirement_args=4) #it happens on a friday, so day%7 == 4
        mc.business.mandatory_crises_list.append(dinner_action)
        mc.business.event_triggers_dict["dinner_date_scheduled"] = True
        return

    def new_title_menu(the_person):
        title_tuple = []
        title_choice = None
        for title in get_titles(the_person):
            title_tuple.append([title,title])
        title_tuple.append(["Do not change her title","Back"])
        title_choice = renpy.display_menu(title_tuple,True,"Choice")
        return title_choice

    def new_mc_title_menu(the_person):
        title_tuple = []
        title_choice = None
        for title in get_player_titles(the_person):
            title_tuple.append([title,title])
        title_tuple.append(["Do not change your title","Back"])
        title_choice = renpy.display_menu(title_tuple,True,"Choice")
        return title_choice

    def new_possessive_title_menu(the_person):
        title_tuple = []
        title_choice = None
        for title in get_possessive_titles(the_person):
            title_tuple.append([title,title])
        title_tuple.append(["Do not change your title","Back"])
        title_choice = renpy.display_menu(title_tuple,True,"Choice")
        return title_choice

    def get_two_titles_for_person(title_func, person):
        title_one = get_random_from_list(title_func(person))
        title_two = get_random_from_list(list( set(title_func(person)) - set([title_one]) ))
        return (title_one, title_two)

label person_introduction(the_person, girl_introduction = True):
    if girl_introduction:
        $ the_person.call_dialogue("introduction")

    #She's given us her name, now she asks for yours.
    $ title_choice = renpy.display_menu(build_person_introduction_titles(),True,"Choice")
    mc.name "[title_choice], it's a pleasure to meet you."
    $ the_person.set_mc_title(title_choice)
    return

label person_new_title(the_person): #She wants a new title or to give you a new title.
    if __builtin__.len(get_titles(the_person)) <= 1: #There's only the one title available to them. Don't bother asking to change
        return
    $ ran_num = the_person.obedience + renpy.random.randint(-20, 20) #Randomize their effective obedience a little so they sometimes ask, sometimes demand

    if ran_num > 120: #She just asks you for something "fresh". Her obedience is high enough that we already have control over this.
        the_person "[the_person.mc_title], do you think [the_person.title] is getting a little old? I think something new might be fun!"
        menu:
            "Change what you call her":
                $ title_choice = new_title_menu(the_person)
                if not (title_choice == "Back" or the_person.create_formatted_title(title_choice) == the_person.title):
                    mc.name "I think [title_choice] would really suit you."
                    $ the_person.set_title(title_choice)
                    "[the_person.title] seems happy with her new title."
                else:
                    mc.name "On second thought, I think [the_person.title] suits you just fine."
                    the_person "If you think so [the_person.mc_title]."

            "Don't change her title":
                mc.name "I think [the_person.title] suits you just fine."
                the_person "If you think so [the_person.mc_title]."

    elif ran_num > 95: #She picks a couple of choices and asks you to decide.
        $ (title_one, title_two) = get_two_titles_for_person(get_titles, the_person)
        if the_person.title == the_person.create_formatted_title(title_one) or the_person.title == the_person.create_formatted_title(title_two):  #If we picked the one we're currently using we have a slightly different dialogue setup.
            if the_person.title == the_person.create_formatted_title(title_two):
                $ placeholder = title_two #Swap them around so title_one is always the current title she has
                $ title_two = title_one
                $ title_one = placeholder
                $ placeholder = None
            $ formatted_title_one = the_person.title
            $ formatted_title_two = the_person.create_formatted_title(title_two)
            the_person "Hey [the_person.mc_title], do you like calling me [formatted_title_one] or do you think [formatted_title_two] sounds better?"
            menu:
                "Keep calling her [formatted_title_one]":
                    mc.name "I think [the_person.title] suits you perfectly, you should keep using it."
                    "She nods in agreement."
                    the_person "Yeah, I think you're right."
                "Change her title to [formatted_title_two]":
                    mc.name "[formatted_title_two] does have a nice ring to it. You should start using that."
                    $ the_person.set_title(title_two)
                    the_person "I think you're right. Thanks for the input!"
        else: #Both are new!
            $ formatted_title_one = the_person.create_formatted_title(title_one)
            $ formatted_title_two = the_person.create_formatted_title(title_two)
            the_person "So [the_person.mc_title], I'm thinking of changing things up a bit. Do you think [formatted_title_one] or [formatted_title_two] sounds best?"
            menu:
                "Change her title to [formatted_title_one]":
                    mc.name "I think [formatted_title_one] is the best of the two."
                    $ the_person.set_title(title_one)
                    the_person "Yeah, I think you're right. I'm going to have people call me that from now on."

                "Change her title to [formatted_title_two]":
                    mc.name "I think [formatted_title_two] is the best of the two."
                    $ the_person.set_title(title_two)
                    the_person "Yeah, I think you're right. I'm going to have people call me that from now on."

                "Refuse to change her title\n{color=#ff0000}{size=18}-5 Happiness{/size}{/color}":
                    mc.name "I don't think either of those sound better than [the_person.title]. You should really just stick with that."
                    "[the_person.title] rolls her eyes."
                    $ the_person.change_happiness(-5)
                    the_person "Well that isn't very helpful [the_person.mc_title]. Fine, I guess [the_person.title] will do."

        $ formatted_title_one = None
        $ formatted_title_two = None
        $ title_one = None
        $ title_two = None
    else: #She doesn't listen to you, so she just picks one and demands that you use it, or becomes unhappy.
        $ new_title = get_random_from_list(get_titles(the_person))
        python:
            while the_person.create_formatted_title(new_title) == the_person.title:
                new_title = get_random_from_list(get_titles(the_person))

        $ formatted_new_title = the_person.create_formatted_title(new_title)
        the_person "By the way [the_person.mc_title], I want you to start referring to me as [formatted_new_title] from now on. I think it suits me better."
        menu:
            "Change her title to [formatted_new_title]":
                mc.name "I think you're right, [formatted_new_title] sounds good."
                $ the_person.set_title(new_title)

            "Refuse to change her title\n{color=#ff0000}{size=18}-10 Happiness{/size}{/color}":
                mc.name "I think that sounds silly, I'm just going to keep calling you [the_person.title]."
                "[the_person.title] scoffs and rolls her eyes."
                $ the_person.change_happiness(-10)
                the_person "Whatever. It's not like I can force you to do anything."

        $ new_title = None
        $ formatted_new_title = None
    return

label person_new_mc_title(the_person):
    if __builtin__.len(get_player_titles(the_person)) <= 1: #There's only the one title available to them. Don't bother asking to change
        return
    $ ran_num = the_person.obedience + renpy.random.randint(-20, 20)
    if ran_num > 120: #She just asks you for something "fresh". Her obedience is high enough that we already have control over this.
        the_person "I was just thinking that I've called you [the_person.mc_title] for a pretty long time. If you're getting tired of it I could call you something else."
        menu:
            "Change what she calls you":
                $ title_choice = new_mc_title_menu(the_person)
                if not (title_choice == "Back" or title_choice == the_person.mc_title):
                    mc.name "I think you should call me [title_choice] from now on."
                    $ the_person.set_mc_title(title_choice)
                    "[the_person.title] seems happy with your new title."
                else:
                    mc.name "On second thought, I think [the_person.mc_title] is fine for now."
                    the_person "If you think so [the_person.mc_title]."

            "Don't change her title for you":
                mc.name "I think [the_person.mc_title] is fine for now."
                the_person "Okay, if you say so!"

    elif ran_num > 95: #She picks a couple of choices and asks you to decide.
        $ (title_one, title_two) = get_two_titles_for_person(get_player_titles, the_person)
        if the_person.mc_title == title_one or the_person.mc_title == title_two:  #If we picked the one we're currently using we have a slightly different dialogue setup.
            if the_person.mc_title == title_two:
                $ placeholder = title_two #Swap them around so title_one is always the current title she has
                $ title_two = title_one
                $ title_one = placeholder
                $ placeholder = None

            the_person "Hey [the_person.mc_title], would you rather I called you [title_two]?"
            menu:
                "Have her keep calling you [title_one]":
                    mc.name "I think I like [title_one], but thanks for asking."
                    "She shrugs."
                    the_person "Sure, whatever you like [the_person.mc_title]."
                "Have her call you [title_two] instead":
                    mc.name "[title_two] does have a nice ring to it. You should start using that."
                    $ the_person.set_mc_title(title_two)
                    the_person "Alright, you got it [the_person.mc_title]!"

        else: #Both are new!
            the_person "You know, I really think [title_one] or [title_two] would fit you a lot better than [the_person.mc_title]. Which one do you think is better?"
            menu:
                "Have her call you [title_one]":
                    mc.name "I think [title_one] is the best of the two."
                    $ the_person.set_mc_title(title_one)
                    the_person "Yeah, you're right. I think I'll start calling you that from now on."

                "Have her call you [title_two]":
                    mc.name "I think [title_two] is the best of the two."
                    $ the_person.set_mc_title(title_two)
                    the_person "Yeah, you're right. I think I'll start calling you that from now on."

                "Refuse to change your title\n{color=#ff0000}{size=18}-5 Happiness{/size}{/color}":
                    mc.name "I don't think either of those sound better than [the_person.mc_title]. Let's stick with that for now."
                    "[the_person.title] rolls her eyes."
                    $ the_person.change_happiness(-5)
                    the_person "Fine, if you don't like change I can't make you."
        $ title_one = None
        $ title_two = None
    else: #She doesn't listen to you, so she just picks one and demands that you use it, or becomes unhappy.
        $ new_title = get_random_from_list(get_player_titles(the_person))
        python:
            while new_title == the_person.mc_title:
                new_title = get_random_from_list(get_player_titles(the_person))

        the_person "You know, I think [new_title] fits you better than [the_person.mc_title]. I'm going to start using that."
        menu:
            "Let her call you [new_title]":
                mc.name "Alright, if you think that's better."
                $ the_person.set_mc_title(new_title)

            "Demand she keeps calling you [the_person.mc_title]\n{color=#ff0000}{size=18}-10 Happiness{/size}{/color}":
                mc.name "I think that sounds silly, I want you to keep calling me [the_person.mc_title]."
                "[the_person.title] scoffs and rolls her eyes."
                $ the_person.change_happiness(-10)
                the_person "Whatever. If it's so important to you then I guess I'll just do it."
        $ new_title = None
    return

label small_talk_person(the_person, apply_energy_cost = True, is_phone = False): #Tier 0. Useful for discovering a character's opinions and the first step to building up love.
    # if is_phone then most narration or descriptions are ignored or replaced. Assume it's on the phone. TODO: Phone conversations should probably be their own full thing.
    if apply_energy_cost: # Useful if you want to reuse this event inside of other events.
        $ mc.change_energy(-15)
    mc.name "So [the_person.title], what's been on your mind recently?"
    $ the_person.discover_opinion("small talk")
    $ ran_num = renpy.random.randint(0,100)
    if not the_person.event_triggers_dict.get("job_known", True):
        $ the_person.event_triggers_dict["job_known"] = True
    # TODO: Add a chance that she wants to talk about someone she knows.
    if ran_num < 60 + (the_person.get_opinion_score("small talk") * 20) + (mc.charisma * 5):
        if is_phone:
            "There's a short pause, then [the_person.title] texts you back."
        else:
            if the_person.get_opinion_score("small talk") >= 0:
                $ the_person.draw_person(emotion = "happy")
                "She seems glad to have a chance to take a break and make small talk with you."

            else:
                "She seems uncomfortable with making small talk, but after a little work you manage to get her talking."

        $ opinion_learned = the_person.get_random_opinion(include_known = True, include_sexy = the_person.sluttiness > 50)

        if not opinion_learned is None:
            $ opinion_state = the_person.get_opinion_topic(opinion_learned)
            $ opinion_string = opinion_score_to_string(opinion_state[0])
            if is_phone:
                the_person "Oh, this and that."
                "The two of you text back and forth between each other for half an hour." #TODO: Either play out that conversation or add some message history to fill it in.
            else:
                "The two of you chat pleasantly for half an hour."

            the_person "So [the_person.mc_title], I'm curious what you think about [opinion_learned]. Do you have any opinions on it?"
            menu:
                "I love [opinion_learned]":
                    $ prediction = 2
                    mc.name "Me? I love [opinion_learned]. Absolutely love it."

                "I like [opinion_learned]":
                    $ prediction = 1
                    mc.name "I really like [opinion_learned]."

                "I don't have any opinion about [opinion_learned]":
                    $ prediction = 0
                    mc.name "I don't really have any thoughts on it, I guess I just don't think it's a big deal."

                "I don't like [opinion_learned]":
                    $ prediction = -1
                    mc.name "I'm not a fan, that's for sure."

                "I hate [opinion_learned]":
                    $ prediction = -2
                    mc.name "I'll be honest, I absolutely hate [opinion_learned]. I just can't stand it."

            $ prediction_difference = abs(prediction - opinion_state[0])
            if prediction_difference == 4: #as wrong as possible
                the_person "Really? Wow, we really don't agree about [opinion_learned], that's for sure."
            elif prediction_difference == 3:
                the_person "You really think so? Huh, I guess we'll just have to agree to disagree."
            elif prediction_difference == 2:
                the_person "I guess I could understand that."
            elif prediction_difference == 1:
                the_person "Yeah, I'm glad you get it. I feel like we're both on the same wavelength."
            else: #prediction_difference == 0
                the_person "Exactly! It's so rare that someone feels exactly the same way about [opinion_learned] as me!"


            if opinion_state[1]:
                if is_phone:
                    "[the_person.possessive_title] sends you a bunch of texts about how she [opinion_string] [opinion_learned]."
                else:
                    "You listen while [the_person.possessive_title] talks about how she [opinion_string] [opinion_learned]."
            else:
                $ the_person.discover_opinion(opinion_learned)
                if is_phone:
                    "[the_person.possessive_title] sends you a bunch of texts, and you learn that she [opinion_string] [opinion_learned]."
                else:
                    "You listen while [the_person.possessive_title] talks and discover that she [opinion_string] [opinion_learned]."

            $ the_person.change_love(2 - prediction_difference, max_modified_to = 20)

        else:
            if is_phone:
                the_person "Oh, this and that. What about you?"
                "You and [the_person.possessive_title] text back and forth for a while. You've had a fun conversation, but you don't think you've learned anything new."
            else:
                "You and [the_person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."

        if the_person.love > 10 and the_person.has_role(instapic_role) and not the_person.event_triggers_dict.get("insta_known", False):
            $ the_person.event_triggers_dict["insta_known"] = True
            the_person "Hey, are you on InstaPic? You should follow me on there, so you can see what I'm up to."
            if is_phone:
                "She text you her InstaPic profile name. You'll be able to look up her profile now."
            else:
                $ mc.phone.register_number(the_person)
                "She gives you her InstaPic profile name. You'll be able to look up her profile now."

        $ the_person.change_happiness(the_person.get_opinion_score("small talk") + 1)

        if the_person.get_opinion_score("small talk") >= 0:
            the_person "It was nice chatting [the_person.mc_title], we should do it more often!"
        else:
            if is_phone:
                the_person "I've got to go. Talk to you later."
            else:
                the_person "So uh... I guess that's all I have to say about that..."
                "[the_person.title] trails off awkwardly."
    else:
        if the_person.get_opinion_score("small talk") < 0:
            the_person "Oh, not much."
            $ the_person.change_happiness(the_person.get_opinion_score("small talk"))
            if is_phone:
                "You try and spark the conversation with a few more messages, but eventually [the_person.title] just stops responding."
            else:
                "You try and keep the conversation going, but making small talk with [the_person.title] is like talking to a wall."
        else:
            the_person "Oh, not much honestly. How about you?"
            $ the_person.change_happiness(the_person.get_opinion_score("small talk"))
            if is_phone:
                "You and [the_person.possessive_title] chat for a while. You don't feel like you've learned much about her, but you both enjoyed talking."
            else:
                "[the_person.possessive_title] seems happy to chitchat, and you spend a few minutes just hanging out."
                "You don't feel like you've learned much about her, but least she seems to have enjoyed talking."

    if not is_phone:
        $ the_person.apply_serum_study()
    return

label compliment_person(the_person): #Tier 1. Raises the character's love. #TODO: just have it raise love and not sluttiness.
    $ mc.change_energy(-15)
    mc.name "Hey [the_person.title]. How are you doing today? You're looking good, that's for sure."
    the_person "Aww, thank you. You're too kind. I'm doing well."
    "You chat with [the_person.possessive_title] for a while and slip in a compliment when you can. She seems flattered by all the attention."
    $ the_person.change_love(5, max_modified_to = 20)
    $ the_person.change_happiness(2)
    the_person "It's been fun talking [the_person.mc_title], we should do this again sometime!"
    $ the_person.apply_serum_study()
    return

label flirt_person(the_person): #Tier 1. Raises a character's sluttiness up to a low cap while also raising their love by less than a compliment.
    $ mc.change_energy(-15)
    if the_person.has_role(girlfriend_role):
        mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
        $ the_person.call_dialogue("flirt_response_girlfriend")

    elif the_person.has_role(affair_role):
        mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
        $ the_person.call_dialogue("flirt_response_affair")

    elif the_person.love <= 20:
        #Low Love
        mc.name "[the_person.title], you're looking nice today. That outfit looks good on you."
        $ the_person.call_dialogue("flirt_response_low")

    elif the_person.love <= 40 or the_person.get_opinion_score("kissing") < -1: #20 to 40 or hates kissing
        # Mid Love
        mc.name "You're looking hot today [the_person.title]. That outfit really shows off your body."
        $ the_person.call_dialogue("flirt_response_mid")

    else:
        # High Love
        mc.name "[the_person.title], your outfit is driving me crazy. What are my chances of getting you out of it?"
        $ the_person.call_dialogue("flirt_response_high")


    # mc.name "Hey [the_person.title], you're looking particularly good today. I wish I got to see a little bit more of that fabulous body."
    $ mc.listener_system.fire_event("player_flirt", the_person = the_person)
    $ change_amount = 1 + the_person.get_opinion_score("flirting") # cap out at 20, but get there a little faster or slower depending on if they like flirting
    if change_amount <= 0:
        $ change_amount = 1
    $ the_person.change_happiness(the_person.get_opinion_score("flirting"))
    $ the_person.change_slut(change_amount, 20)
    $ the_person.change_love(1, max_modified_to = 25)
    $ the_person.discover_opinion("flirting")
    $ the_person.apply_serum_study()
    # $ the_person.call_dialogue("flirt_response") #This has been divided up into flirt_response_[low,mid,high].

    return

label give_serum(the_person, add_to_log = True):
    call screen serum_inventory_select_ui(mc.inventory, the_person)
    if not _return == "None":
        $ the_serum = _return
        if add_to_log:
            "You decide to give [the_person.title] a dose of [the_serum.name]."
        $ mc.inventory.change_serum(the_serum,-1)
        $ the_person.give_serum(copy.copy(the_serum), add_to_log = add_to_log) #Use a copy rather than the main class, so we can modify and delete the effects without changing anything else.
        return the_serum

    if add_to_log:
        "You decide not to give [the_person.title] anything."
    return None

label date_person(the_person): #You invite them out on a proper date
    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([get_date_plan_actions(the_person)]))
    else:
        call screen main_choice_display([get_date_plan_actions(the_person)])
    if isinstance(_return, Action):
        $ _return.call_action(the_person) #This is where you're asked to plan out the date, or whatever.
    return

label lunch_date_plan_label(the_person):
    # Take her out to lunch, raises love to a max of 50 if you pick the correct chat options
    if the_person.has_role(sister_role):
        mc.name "I was thinking about getting some lunch, do you want to come with me and hang out?"
        the_person "Hey, that sounds nice! You're always out of the house, I wish we got to spend more time together like we did when we were younger."

    elif the_person.has_role(mother_role):
        mc.name "I'm going to go out for lunch. You've been busy lately, would you like to take a break and join me?"
        the_person "Aww, it's so sweet that you still want to spend time with your mother. I'd love to!"

    elif the_person.has_role(aunt_role):
        mc.name "Would you like to come and have lunch with me? I haven't seen you much since I was a kid, I'm sure we have a lot to catch up on."
        the_person "It has been a long time, hasn't it. Lunch sounds wonderful!"

    elif the_person.has_role(cousin_role):
        mc.name "I'm going to get some lunch, would you like to come along with me?"
        the_person "You want me to be seen in public with you? You're really pushing it [the_person.mc_title], but sure."

    elif affair_role in the_person.special_role:
        mc.name "[the_person.title], I was going to get some lunch, would you like to join me?"
        the_person "That sounds nice, [the_person.mc_title]."
        "She pauses and seems to consider something for a moment."
        the_person "Are you sure my husband won't find out?"
        if the_person == christina:
            mc.name "You could always say you had to go over something, with [emily.name] her tutor."
            the_person "You are right, let's go!"
        else:
            mc.name "Can't you go and grab lunch with an acquaintance?"
            the_person "Of course I can, let's get going!"

    elif not (the_person.relationship == "Single" or the_person.get_opinion_score("cheating on men") > 0): #IF she likes cheating she doesn't even mention she's in a relationship
        mc.name "[the_person.title], I was going to get some lunch, would you like to join me? Maybe just grab a coffee and hang out for a while?"
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "That sounds nice, [the_person.mc_title]."
        "She pauses and seems to consider something for a moment."
        the_person "Just so we're on the same page, this is just as friends, right? I have a [so_title], I don't want to get anything confused here."
        mc.name "Of course! I just want to hang out and talk, that's all."
        the_person "Okay, let's go then!"

    else:
        mc.name "Would you like to go get a coffee, maybe a little lunch, and just chat for a while? I feel like I want to get to know you better."
        the_person "That sounds nice, I think I'd like to get to know you better too."
        the_person "If you're ready to go right now I suppose I am too. Let's go!"

    call lunch_date_label(the_person) from _call_lunch_date_label #There's no need to schedule anything because this happens right away.
    return

label movie_date_plan_label(the_person):
    # She starts to wonder if she should be telling her boyfriend, etc. about this.
    if day%7 == 1 and time_of_day < 3:
        $ is_tuesday = True #It's already Tuesday and early enough that the date would be right about now.
    else:
        $ is_tuesday = False


    if the_person.has_role(sister_role):
        mc.name "Hey, I was wondering if you'd like to see a movie with me some time? You know, spend a little more time together as brother-sister."
        the_person "It's been like, a year since I went to the movies with you. I think it was when my date ghosted me and you swept in and saved the night by coming with me."
        the_person "I can't quite remember what we saw though..."
        "She seems puzzled for a moment, then shrugs and smiles at you."
        the_person "Oh well, it's probably not important. Sure thing [the_person.mc_title], a movie sounds fun!"
        if is_tuesday:
            the_person "How about tonight? I think tickets are half price."
        else:
            the_person "How about Tuesday night? I think tickets are half price."

    elif the_person.has_role(mother_role):
        mc.name "Hey [the_person.title], would you like to come to the movies with me? I want to spend some more time together, mother and son."
        the_person "Aww, you're precious [the_person.mc_title]. I would love to go to the movies with you."
        the_person "Remember how you and I used to watch movies together every weekend? I felt like our relationship was so close because of that."
        "She seems distracted by the memory for a moment, then snaps back to the conversation."
        if is_tuesday:
            the_person "Would you be free tonight?"
        else:
            the_person "Would you be free Tuesday night?"

    elif the_person.has_role(aunt_role):
        mc.name "[the_person.title], would you like to come see a movie with me? I think it would just be nice to spend some more time together."
        the_person "You know, I haven't been out much since I left my ex, so a movie sounds like a real good time."
        if is_tuesday:
            the_person "How about later tonight? I don't have anything going on."
        else:
            the_person "How about Tuesday night? I don't have anything going on then."

    elif the_person.has_role(cousin_role):
        mc.name "Hey, do you want to come see a movie with me and spend some time together?"
        the_person "Fine, but no telling people we're related, okay? I don't want anyone to think I might be a dweeb like you."
        "She gives you a wink."
        if is_tuesday:
            the_person "How about tonight? I didn't have anything going on."
        else:
            the_person "How about Tuesday? I don't have anything going on then."

    elif not the_person.relationship == "Single":
        mc.name "So [the_person.title], I was going to see a movie some time this week and wanted to know if you'd like to come with me."
        mc.name "It would give us a chance to spend time together."
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.get_opinion_score("cheating on men") > 0:
            the_person "Oh, a movie sounds fun!"
            "She gives you a playful smile."
            the_person "Just don't tell my [so_title], okay? He might not like me hanging around with a hot guy like you."
            mc.name "My lips are sealed."
            if the_person.effective_sluttiness() > 60:
                if is_tuesday:
                    the_person "Treat me right and mine might not be. He's normally out late with work tonight, how does that sound?"
                else:
                    the_person "Treat me right and mine might not be. He's normally out late with work on Tuesdays, how does that sound?"
            else:
                if is_tuesday:
                    the_person "He's normally out late with work on Tuesdays, so how about would tonight sound for you?"
                else:
                    the_person "He's normally out late with work on Tuesdays, how does that sound for you?"

        else:
            the_person "Oh, a movie sounds fun! But..."
            mc.name "Is there something wrong?"
            the_person "No, I just don't know what my [so_title] would think. He might be a little jealous of you, you know?"
            mc.name "You don't have to tell him that I'll be there, if you don't want to. There's no reason you couldn't go out by yourself if you wanted to."
            "She thinks about it for a moment, then nods and smiles."
            if is_tuesday:
                the_person "You're right, of course. He's normally busy with work tonight, so how does that sound for you?"
            else:
                the_person "You're right, of course. He's normally busy with work on Tuesdays, how does that sound for you?"

    else:
        mc.name "So [the_person.title], I was wondering if you'd like to come see a movie with me some time this week."
        mc.name "It would give us a chance to spend some time together and get to know each other better."
        if is_tuesday:
            the_person "Oh, a movie sounds fun! I don't have anything going on tonight, would that work for you?"
        else:
            the_person "Oh, a movie sounds fun! I don't have anything going on Tuesday night, would that work for you?"

    menu:
        "Plan a date for tonight" if is_tuesday:
            mc.name "Tonight would be perfect, I'll will see you later."
            the_person "See you!"
            $ create_movie_date_action(the_person)

        "Plan a date for Tuesday night" if not is_tuesday:
            mc.name "Tuesday would be perfect, I'm already looking forward to it."
            the_person "Me too!"
            $ create_movie_date_action(the_person)

        "Maybe some other time":
            mc.name "I'm busy on Tuesday unfortunately."
            the_person "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."

    return "Advance Time"

label dinner_date_plan_label(the_person):
    if day%7 == 4 and time_of_day < 3:
        $ is_friday = True #It's already Tuesday and early enough that the date would be right about now.
    else:
        $ is_friday = False

    if the_person.has_role(sister_role):
        mc.name "[the_person.title], I was wondering if you'd like to go out for a dinner date together. Some brother sister bonding time."
        if is_friday:
            the_person "That sounds great [the_person.mc_title]. Would tonight work for you?"
        else:
            the_person "That sounds great [the_person.mc_title]. Would Friday be good?"

    elif the_person.has_role(mother_role):
        mc.name "Mom, I was wondering if I could take you out to dinner, just the two of us. I'd enjoy some mother son bonding time."
        if is_friday:
            the_person "Aww, that's so sweet. How about tonight, after we're both finished with work."
        else:
            the_person "Aww, that's so sweet. How about Friday, after we're both finished with work."

    elif the_person.has_role(aunt_role):
        mc.name "[the_person.title], would you like to go out on a dinner date with me? I think it would be a nice treat for you."
        the_person "That sounds like it would be amazing. It's been tough, just me and [cousin.title]. I don't get out much any more."
        "She smiles and gives you a quick hug."
        if is_friday:
            the_person "How about tonight?"
        else:
            the_person "How about Friday night?"

    elif the_person.has_role(cousin_role):
        mc.name "Hey, I want to take you out to dinner."
        the_person "Jesus, at least buy me dinner first. Wait a moment..."
        "She laughs at her own joke."
        if is_friday:
            the_person "Fine, how about tonight?"
        else:
            the_person "Fine, how about Friday?"

    elif not the_person.relationship == "Single":
        mc.name "[the_person.title], I'd love to spend some time together, just the two of us. Would you let me take you out for dinner?"
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "[the_person.mc_title], you know I've got a [so_title], right? Well..."
        if the_person.get_opinion_score("cheating on men") > 0:
            "She doesn't take very long to make up her mind."
            if is_friday:
                the_person "He's out with friends tonight and what he doesn't know can't hurt him. Shall we go tonight?"
            else:
                the_person "He won't know about it, right? What he doesn't know can't hurt him. Are you free Friday?"
        else:
            "She thinks about it for a long moment."
            if is_friday:
                the_person "Just this once, and we have to make sure my [so_title] never finds out. Shall we go tonight?"
            else:
                the_person "Just this once, and we have to make sure my [so_title] never finds out. Are you free Friday?"

    else:
        mc.name "[the_person.title], I'd love to get to know you better. Would you let me take you out for dinner?"
        if is_friday:
            the_person "That sounds delightful [the_person.mc_title]. I'm free tonight, if you are available."
        else:
            the_person "That sounds delightful [the_person.mc_title]. I'm free Friday night, if you would be available."

    menu:
        "Plan a date for tonight" if is_friday:
            mc.name "It's a date. I'll see you tonight."
            the_person "See you!"
            $ create_dinner_date_action(the_person)

        "Plan a date for Friday night" if not is_friday:
            mc.name "It's a date. I'm already looking forward to it."
            the_person "Me too!"
            $ create_dinner_date_action(the_person)

        "Maybe some other time":
            mc.name "I'm busy on Friday unfortunately."
            the_person "Well maybe next week then. Let me know, okay?"
            "She gives you a warm smile."
    return

label serum_give_label(the_person):
    $ sneak_serum_chance = 70 + (mc.int*5) - (the_person.focus*5)  #% chance that you will successfully give serum to someone sneakily. Less focused people are easier to fool.
    $ ask_serum_chance = 10*mc.charisma + 5*the_person.int #The more charismatic you are and the more intellectually curious they are the better the chance of success
    $ demand_serum_chance = mc.charisma * (the_person.obedience - 90) #The more charismatic you are and the more obedient they are the more likely this is to succeed.

    if sneak_serum_chance < 0:
        $ sneak_serum_chance = 0
    elif sneak_serum_chance > 100:
        $ sneak_serum_chance = 100

    if ask_serum_chance < 0:
        $ ask_serum_chance = 0
    elif ask_serum_chance > 100:
        $ ask_serum_chance = 100

    if mc.business.get_employee_title(the_person) == "None":
        $demand_serum_chance += -35 #if she doesn't work for you there is a much lower chance she will listen to your demand (unless you are very charismatic or she is highly obedient.)
    if demand_serum_chance < 0:
        $ demand_serum_chance = 0
    elif demand_serum_chance > 100:
        $ demand_serum_chance = 100

    $ pay_serum_cost = the_person.salary * 5
    $ ran_num = renpy.random.randint(0,100)

    menu:
        "Give it to her stealthily\n{color=#ff0000}{size=18}Success Chance: [sneak_serum_chance]%%{/size}{/color}": #TODO: Have this modified by something so there are interesting gameplay decisions
            "You chat with [the_person.title] for a couple of minutes. Waiting to find a chance to deliver a dose of serum."
            if ran_num < sneak_serum_chance:
                #Success
                "You're able to distract [the_person.title] and have a chance to give her a dose of serum."
                call give_serum(the_person) from _call_give_serum

            else:
                #Caught!
                "You finally distract [the_person.title] and have a chance to give her a dose of serum."
                the_person "Hey, what's that?"
                "You nearly jump as [the_person.title] points down at the small vial of serum you have clutched in your hand."
                $ ran_num = renpy.random.randint(0,10)
                if ran_num < mc.charisma:
                    if mc.business.get_employee_title(the_person) == "None":
                        mc.name "This? Oh, it's just something we're working on at the lab that I thought you might be interested in."
                        "You dive into a technical description of your work, hoping to distract [the_person.title] from your real intentions."

                    else:
                        mc.name "This? Oh, it's just one of the serums I grabbed from production for quality control. I was just fidgeting with it I guess."
                        "You make small talk with [the_person.title], hoping to distract her from your real intentions."
                    "After a few minutes you've managed to avoid her suspicion, but haven't been able to deliver the dose of serum."

                else:
                    mc.name "This? Uh..."
                    $ the_person.draw_person(emotion="angry")
                    $ the_person.change_obedience(-10)
                    $ the_person.change_happiness(-10)
                    $ the_person.change_love(-5)
                    the_person "Were you about to put that in my drink? Oh my god [the_person.mc_title]!"
                    mc.name "Me? Never!"
                    "[the_person.title] shakes her head and storms off. You can only hope this doesn't turn into something more serious."
                    $ clear_scene()
                    return

        "Ask her to take it\n{color=#ff0000}{size=18}Success Chance: [ask_serum_chance]%%{/size}{/color}" if not mandatory_unpaid_serum_testing_policy.is_active() or mc.business.get_employee_title(the_person) == "None":
            if mc.business.get_employee_title(the_person) == "None":
                mc.name "[the_person.title], I've got a project going on at work that could really use a test subject. Would you be interested in helping me out?"

            else:
                mc.name "[the_person.title], there's a serum design that is in need of a test subject. Would you be interested in helping out with a quick field study?"

            if ran_num < ask_serum_chance:
                #Success
                if mc.business.get_employee_title(the_person) == "None":
                    if the_person.personality.personality_type_prefix == "nora":
                        the_person "I'd be happy to help. I've seen your work, I have complete confidence you've tested this design thoroughly."
                    else:
                        the_person "I'd be happy to help, as long as you promise it's not dangerous of course. I've always wanted to be a proper scientist!"
                else:
                    the_person "I'll admit I'm curious what it would do to me. Okay, as long as it's already passed the safety test requirements, of course."
                mc.name "It's completely safe, we just need to test what the results from it will be. Thank you."
                call give_serum(the_person) from _call_give_serum_2

            else:
                #Denies
                $ the_person.change_obedience(-2)
                the_person "I'm... I don't think I would be comfortable with that. Is that okay?"
                mc.name "Of course it is, that's why I'm asking in the first place."

        "Ask her to take it\n{color=#ff0000}{size=18}Success Chance: Required by Policy{/size}{/color}" if mandatory_unpaid_serum_testing_policy.is_active() and not mc.business.get_employee_title(the_person) == "None":
            #Auto success
            mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this."
            call give_serum(the_person) from _call_give_serum_3

        "Demand she takes it\n{color=#ff0000}{size=18}Success Chance: [demand_serum_chance]%%{/size}{/color}": #They must work for you to demand it.
            mc.name "[the_person.title], you're going to drink this for me."
            "You pull out a vial of serum and present it to [the_person.title]."
            the_person "What is it for, is it important?"
            mc.name "Of course it is, I wouldn't ask you to if it wasn't."
            if ran_num < demand_serum_chance:
                #Success
                the_person "Okay, if that's what you need me to do..."
                call give_serum(the_person) from _call_give_serum_4
            else:
                #Refuse
                $ the_person.draw_person(emotion = "angry")
                $ the_person.change_obedience(-2)
                $ the_person.change_happiness(-2)
                $ the_person.change_love(-2)
                the_person "You expect me to just drink random shit you hand to me? I'm sorry, but that's just ridiculous."

        "Pay her to take it\n{color=#ff0000}{size=18}Costs: $[pay_serum_cost]{/size}{/color}" if mandatory_paid_serum_testing_policy.is_active() and not mandatory_unpaid_serum_testing_policy.is_active() and not mc.business.get_employee_title(the_person) == "None": #This becomes redundent when they take it for free.
            #Pay cost and proceed
            $ mc.business.change_funds(-pay_serum_cost)
            mc.name "[the_person.title], we're running field trials and you're one of the test subjects. I'm going to need you to take this, a bonus will be added onto your paycheck."
            call give_serum(the_person) from _call_give_serum_5


        "Pay her to take it\n{color=#ff0000}{size=18}Requires: Mandatory Paid Serum Testing{/size}{/color} (disabled)" if not mandatory_unpaid_serum_testing_policy.is_active() and not mandatory_paid_serum_testing_policy.is_active() and not mc.business.get_employee_title(the_person) == "None":
            pass

        "Do nothing":
            pass
    return

label grope_person(the_person):
    # Note: the descriptors of the actual stages are stored in grope_descriptions.rpy to keep things organized.
    $ mc.change_energy(-5)
    $ the_person.event_triggers_dict["last_groped"] = (day, time_of_day)
    call grope_shoulder(the_person) from _call_grope_shoulder
    if _return:
        call grope_waist(the_person) from _call_grope_waist
        if _return:
            call grope_ass(the_person) from _call_grope_ass
            if _return:
                call grope_tits(the_person) from _call_grope_tits
                if _return:
                    $ should_be_private = True
                    if mc.location.get_person_count() > 1: #We aren't alone and should ask if we want to find somewhere private
                        $ extra_people_count = mc.location.get_person_count() - 1
                        $ obedience_required = 130 - (10*the_person.get_opinion_score("public sex"))
                        if the_person.get_opinion_score("cheating on men") < 1 and the_person.relationship != "Single" and not the_person.has_role(affair_role):
                            $ obedience_required += 10 + -10*the_person.get_opinion_score("cheating on men")
                        $ the_person.discover_opinion("public sex")
                        if the_person.effective_sluttiness("touching_body") < 40 or the_person.get_opinion_score("public sex") < 0:
                            # She's nervous about it and asks to go somewhere private.
                            the_person "Wait, wait..."
                            "[the_person.possessive_title] glances around at the people nearby."
                            the_person "I don't want other people to watch. Let's find someplace we can be alone."
                            menu:
                                "Find somewhere quiet\n{color=#ff0000}{size=18}No interruptions{/size}{/color}":
                                    mc.name "Alright, come with me."
                                    "You take [the_person.title] by her wrist and lead her away."
                                    #TODO: have each location have a unique "find someplace quiet" descriptor with a default fallback option
                                    "After a couple of minutes searching you find a quiet space with just the two of you."
                                    "You don't waste any time getting back to what you were doing, fondling [the_person.possessive_title]'s tits and ass."

                                "Stay where you are\n{color=#ff0000}{size=18}[extra_people_count] watching{/size}{/color}" if the_person.obedience >= obedience_required:
                                    $ should_be_private = False
                                    "You scoff and keep feeling up her body."
                                    mc.name "Come on, we don't need to worry about them. Just relax."
                                    the_person "But they're going to be watching..."
                                    $ the_person.change_happiness(5*the_person.get_opinion_score("public sex"))
                                    mc.name "You ignore her and keep going. Her anxiety is obvious, but she doesn't object any further."

                                "Stay where you are\n{color=#ff0000}{size=18}Requires: [obedience_required] Obedience{/size}{/color} (disabled)" if the_person.obedience < obedience_required:
                                    pass

                        else:
                            # She doesn't care, but you can find someplace private.
                            "[the_person.possessive_title] either doesn't notice or doesn't care, but there are other people around."
                            menu:
                                "Find somewhere quiet\n{color=#ff0000}{size=18}No interruptions{/size}{/color}":
                                    mc.name "Let's find somewhere that isn't quite as busy. I don't want to be interrupted."
                                    if the_person.get_opinion_score("public sex"):
                                        the_person "Aww, you don't want to put on a little show? I'm sure they would be {i}very{/i} entertained."
                                    else:
                                        the_person "Oh yeah, that's a good idea."
                                    "After searching for a couple of minutes you find a quiet space with just the two of you."
                                    "You don't waste any time getting back to what you were doing, fondling [the_person.possessive_title]'s tits and ass."

                                "Stay where you are\n{color=#ff0000}{size=18}[extra_people_count] watching{/size}{/color}":
                                    $ should_be_private = False
                                    pass

                    if the_person.has_role(prostitute_role):
                        the_person "We can continue what you started, but it would cost you two hundred dollars."
                        menu:
                            "Pay her\n{color=#ff0000}{size=18}Costs: $200{/size}{/color}" if mc.business.funds > 200:
                                $ mc.business.change_funds (-200)
                                $ the_person.change_obedience(1)
                                call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True) from _call_fuck_person_grope_person_prostitute_role
                                $ the_person.call_dialogue("sex_review", the_report = _return)
                                $ the_person.review_outfit()
                            "Pay her\n{color=#ff0000}{size=18}Requires: $200{/size}{/color} (disabled)" if mc.business.funds <= 200:
                                pass
                            "No":
                                mc.name "Thanks for the offer, but no thanks."
                                "She shrugs."
                                the_person "Your loss."
                    else:
                        call fuck_person(the_person, private = should_be_private, start_position = standing_grope, start_object = None, skip_intro = True) from _call_fuck_person_43 # Enter the sex system, starting from this point.
                        $ the_person.call_dialogue("sex_review", the_report = _return)
                        $ the_person.review_outfit()
    return

init -2 python:
    def build_command_person_actions_menu(the_person):
        change_titles_action = Action("Change how we refer to each other", requirement = change_titles_requirement, effect = "change_titles_person", args = the_person, requirement_args = the_person,
            menu_tooltip = "Manage how you refer to " + the_person.title + " and tell her how she should refer to you. Different combinations of stats, roles, and personalities unlock different titles.", priority = -5)

        wardrobe_change_action = Action("Change your wardrobe", requirement = wardrobe_change_requirment, effect = "wardrobe_change_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Add and remove outfits from " + the_person.title + "'s wardrobe, or ask her to put on a specific outfit.", priority = -5)

        serum_demand_action = Action("Drink a dose of serum for me", requirement = serum_demand_requirement, effect = "serum_demand_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Demand " + the_person.title + " drinks a dose of serum right now. Easier to command employees to test serum.", priority = -5)

        strip_demand_action = Action("Strip for me", requirement = demand_strip_requirement, effect = "demand_strip_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Command her to strip off some of her clothing.", priority = -5)

        touch_demand_action = Action("Let me touch you   {color=#FFFF00}-10{/color} {image=gui/extra_images/energy_token.png}", requirement = demand_touch_requirement, effect = "demand_touch_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Demand " + the_person.title + " stays still and lets you touch her. Going too far may damage your relationship.", priority = -5)

        suck_demand_action = Action("Suck my cock", requirement = suck_demand_requirement, effect = "suck_demand_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Demand " + the_person.title + " gets onto her knees and worships your cock.", priority = -5)

        bc_demand_action = Action("Talk about birth control", requirement = demand_bc_requirement, effect = "bc_demand_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Discuss " + the_person.title + "'s use of birth control.", priority = -5)

        return ["Command", change_titles_action, wardrobe_change_action, serum_demand_action, strip_demand_action, touch_demand_action, suck_demand_action, bc_demand_action, ["Never mind", "Return"]]

label command_person(the_person):
    mc.name "[the_person.title], I want you to do something for me."
    the_person "Yes [the_person.mc_title]?"

    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([build_command_person_actions_menu(the_person)]))
    else:
        call screen main_choice_display([build_command_person_actions_menu(the_person)])

    if isinstance(_return, Action):
        $ _return.call_action()
    return

label bc_talk_label(the_person):
    # Contains the Love and Sluttiness based approaches to asking someone to stop taking birth control.
    mc.name "Can we talk about something?"
    the_person "Mmhm, what's that?"
    mc.name "I want to talk about your birth control."
    if the_person.has_role(girlfriend_role) or the_person.has_role(affair_role):
        #She'll talk to you about it. High Love or moderate sluttiness are needed to convince her to stop taking BC. Easier to convince her to start.
        # High influence from opinion of creampies.

        $ needed_start = 30 + (15 * the_person.get_opinion_score("creampies"))
        $ needed_stop = 45 - (15 * the_person.get_opinion_score("creampies"))
        if the_person.has_role(affair_role):
            $ needed_stop += -10*the_person.get_opinion_score("cheating on men") #They think it's hot to have another man's baby

        if the_person.on_birth_control:
            if the_person.get_opinion_score("creampies") > 0: #She's not happy about it
                the_person "Oh, sure. I'm taking it right now, so if you get a little too excited and unload inside me..."
                "She smiles and shrugs."
                the_person "Well that wouldn't be the end of the world."
            else:
                the_person "Oh, sure. I'm taking it right now, so we shouldn't have any \"accidents\" to worry about."
        else:
            if the_person.get_opinion_score("creampies") > 0: #She's happy about not being on BC
                the_person "I'm not taking any right now, so..."
                "She smiles and shrugs."
                the_person "If you cum in me you might get me knocked up. It's kind of hot to think about that..."
            else:
                the_person "Oh, well... I'm not taking any right now."
        $ the_person.update_birth_control_knowledge()

        menu:
            "Start taking birth control" if not the_person.on_birth_control:
                mc.name "You should start taking some, I don't want you getting pregnant."
                if the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start:
                    "She thinks about it for a moment, then nods."
                    if the_person.has_taboo("condomless_sex"):
                        the_person "It would be nice to not have to worry about a condom breaking when he have sex."
                        the_person "Okay, I'll talk to my doctor and start taking it as soon as possible."
                    else:
                        the_person "If we keep doing it raw that's a smart idea."
                        the_person "I'll talk to my doctor and start taking it as soon as possible."
                    the_person "I should be able to start tomorrow, we will still need to careful until then."
                    $ manage_bc(the_person, start = True)

                else:
                    "She shakes her head."
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        the_person "I don't care about that. I love the thrill of a hot load of cum inside my perfectly fertile pussy."
                        the_person "There's nothing hotter than that. You're just going to have to accept that it's a risk."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "I'm sorry [the_person.mc_title], but I've tried it before and it plays hell with my hormones."
                        the_person "We can just use a condom, or do something else to have fun together."

            "Stop taking birth control" if the_person.on_birth_control:
                mc.name "I want you to stop taking it."
                if the_person.love >= needed_stop or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        the_person "Yeah? I've wanted to stop too, I don't care if it's risky."
                        the_person "There's nothing that's more of a turn on than having a hot load inside of my pussy. Ah..."
                        "[the_person.possessive_title] sighs and seems lost in thought for a moment."
                        the_person "Sorry, I'm getting distracted."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "Do you think that's a good idea? What if something happened?"
                        mc.name "We can deal with that when it happens. If we don't want you to get pregnant we can always use a condom."
                        "She thinks about it for a long moment, then nods and smiles."
                        the_person "Okay, I won't take my birth control in the morning. We'll just be careful, it'll be fine..."

                    $ manage_bc(the_person, start = False)

                else:
                    if the_person.get_opinion_score("bareback sex") > 0:
                        the_person "I don't think that's a good idea. If I'm on my birth control you don't need to wear a condom when we fuck."
                        the_person "I love feeling you raw inside me. I don't want to have to give that up."
                        $ the_person.discover_opinion("bareback sex")
                    else:
                        the_person "I don't think that's a good idea. What if something happened? Are we ready for that change in our lives?"
                        the_person "Maybe one day, but I'm not comfortable with it right now."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check on that."

    elif the_person.effective_sluttiness() > 40:
        $ needed_start = 40 + (15 * the_person.get_opinion_score("creampies"))
        $ needed_stop = 75 - (15 * the_person.get_opinion_score("creampies"))

        if the_person.on_birth_control:
            if the_person.get_opinion_score("bareback sex") > 0:
                the_person "Oh, is that all? Yeah, I'm on birth control right now because I hate how condoms feel."
                $ the_person.discover_opinion("bareback sex")
            else:
                the_person "Oh, is that all? Yeah, I'm on birth control right now so I don't have to worry about getting pregnant."
        else:
            the_person "Oh, I guess that's probably an important thing for you to know about."
            the_person "I'm not taking any birth control right now."

        $ the_person.update_birth_control_knowledge()
        menu:
            "Start taking birth control" if not the_person.on_birth_control:
                mc.name "You should probably start taking it, before something happens and you get pregnant."
                if the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_start:
                    the_person "That's probably a good idea. I'll talk to my doctor as soon as possible about it."
                    $ manage_bc(the_person, start = True)
                else:
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        "She shrugs and shakes her head."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person "I don't care about that. I love the feeling of a warm, risky creampie too much to ever give it up."
                    else:
                        the_person "Sorry, I've tried it before and it just messes with my hormones too badly."
                        the_person "We'll just be careful and use a condom, or you can pull out. Okay?"

            "Stop taking birth control" if the_person.on_birth_control:
                mc.name "You should stop taking it. Wouldn't that be really hot?"
                if the_person.love >= needed_start or the_person.effective_sluttiness() >= needed_stop:
                    if the_person.get_opinion_score("creampies") > 0 and the_person.get_opinion_score("bareback sex") > 0:
                        the_person "Do you think so? I've always wanted to, I don't think I can trust myself to tell a man to pull out."
                        the_person "Even if I know that's the smart thing to do I would probably just beg for a hot load inside me..."
                        "She closes her eyes and moans softly, obviously lost in a fantasy of her own making."
                        "After a moment she shakes her head and focuses again."
                        $ the_person.discover_opinion("creampies")
                        $ the_person.discover_opinion("bareback sex")
                        the_person "Sorry... I guess if you think it's a good idea I can give it a try. What's the worst that can happen..."
                    else:
                        the_person "Do you really think so? I mean, it sounds kind of hot but I would have to trust you to pull out, or have you wear a condom."
                        mc.name "Then that's what I'll do. I just think it's so much sexier to know there's a little bit of risk."
                        "[the_person.possessive_title] thinks about it for a long moment. Finally she shrugs and nods."
                        the_person "Okay, we can give it a try. We'll just need to be very careful."
                    $ manage_bc(the_person, start = False)
                else:
                    "[the_person.possessive_title] shakes her head."
                    the_person "That would be crazy! There's no way I could gamble the rest of my life on some guy pulling out or me getting lucky."

            "That's all I wanted to know":
                mc.name "That's all, I just wanted to check."
    else:
        if the_person.love > 30:
            # She loves you enough to tell you her status
            the_person "Well that's kind of private, but if it really matters to you I guess I can tell you."
            if the_person.on_birth_control:
                the_person "I'm not looking to get pregnant right now, so I'm taking birth control."
            else:
                the_person "I'm not taking any birth control right now."

            $ the_person.update_birth_control_knowledge()
            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        elif the_person.effective_sluttiness() > 20:
            the_person "Oh, I guess I can tell you if you're really curious."
            if the_person.on_birth_control:
                the_person "I'm taking birth control right now. I don't want to worry about getting pregnant by accident."
            else:
                the_person "I'm not taking birth control right now."

            $ the_person.update_birth_control_knowledge()
            "It's clear from her tone that [the_person.possessive_title] wouldn't be swayed by you telling her what to do."

        else:
            the_person "That's a pretty personal question. Let's get to know each other a little more before we talk about that, okay?"
    return

label bc_demand_label(the_person):
    # Contains the obedience based approach to asking someone to stop taking birth control.
    # This event can have a moderately low Obedience requirement, with higher requirements to actually make changes.
    mc.name "Tell me about your birth control."
    if the_person.on_birth_control:
        the_person "I'm taking birth control right now."
    else:
        the_person "I'm... not taking any right now."
    $ the_person.update_birth_control_knowledge()

    menu:
        "Start taking birth control" if not the_person.on_birth_control and the_person.obedience >= 130:
            mc.name "I want you to start taking some. I don't want you getting pregnant."
            "[the_person.possessive_title] nods."
            the_person "Okay, I can do that. I'll talk to my doctor, I think I'll be able to start it tomorrow."
            mc.name "Good."
            $ manage_bc(the_person, start = True)

        "Start taking birth control\n{color=#FF0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if not the_person.on_birth_control and the_person.obedience < 130:
            pass

        "Stop taking birth control" if the_person.on_birth_control and the_person.obedience >= 160:
            mc.name "I want you to stop taking it."
            $ complains_threshold = 45 - (15 * the_person.get_opinion_score("creampies"))
            if the_person.effective_sluttiness() >= complains_threshold:
                # She's slutty enough that it's not even a concern.
                "[the_person.possessive_title] nods obediently."
                the_person "Okay, I'll stop right away."
            elif the_person.is_family():
                "[the_person.possessive_title] shuffles nervously before working up the nerve to speak back."
                the_person "[the_person.mc_title], I can't do that. If you got me pregnant I... I don't know what I would do!"
                mc.name "I didn't say I was going to get you pregnant. I just told you to stop taking your birth control."
                mc.name "I'm sure you can avoid getting knocked up if you really put your mind to it. Now, do we have a problem?"
                "[the_person.title] starts to say something, then thinks better of it. She shakes her head."
                the_person "No, there's no problem. I won't take any birth control in the morning."

            else:
                "[the_person.possessive_title] shuffles nervously before working up the nerve to speak back."
                the_person "I... I don't know if that's a good idea. I don't know if I want to get pregnant."
                mc.name "I didn't ask if you wanted to get pregnant. I told you to stop taking your birth control. Is there a problem with that?"
                "She blushes and looks away under your glare."
                the_person "No. I'll stop right away. Sorry."

            $ manage_bc(the_person, start = False)

        "Stop taking birth control\n{color=#FF0000}{size=18}Requires: 160 Obedience{/size}{/color} (disabled)" if  the_person.on_birth_control and the_person.obedience < 160:
            pass

        "That's all I wanted to know":
            mc.name "Good. That's all I wanted to know."
    return

init 5 python:
    def manage_bc(person, start, update_knowledge = True):
        if start:
            event_label = "bc_start_event"
        else:
            event_label = "bc_stop_event"

        bc_start_action = Action("Change birth control", always_true_requirement, event_label, args = [person, update_knowledge])
        mc.business.mandatory_morning_crises_list.append(bc_start_action) # She starts or stops the next morning.
        return

label bc_start_event(the_person, update_knowledge = True):
    $ the_person.on_birth_control = True
    if update_knowledge:
        $ the_person.update_birth_control_knowledge()
    return

label bc_stop_event(the_person, update_knowledge = True):
    $ the_person.on_birth_control = False
    if update_knowledge:
        $ the_person.update_birth_control_knowledge()
    return
