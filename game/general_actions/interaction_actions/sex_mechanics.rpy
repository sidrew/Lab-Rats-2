init 2 python:
    def get_position_trance_chance_modifier(person, position):
        trance_chance_modifier = 0
        for opinion_tag in position.opinion_tags:
            trance_chance_modifier += 2 * person.get_opinion_score(opinion_tag)
        return trance_chance_modifier

    def get_position_opinion_score(person, position):
        opinion_score = 0
        for opinion_tag in position.opinion_tags:
            opinion_score += person.get_opinion_score(opinion_tag) #Add a bonus or penalty if she likes or dislikes the position.
            person.discover_opinion(opinion_tag)
        return opinion_score

label fuck_person(the_person, private = True, start_position = None, start_object = None, skip_intro = False, girl_in_charge = False, self_strip = True, hide_leave = False, position_locked = False, report_log = None, affair_ask_after = True, ignore_taboo = False, skip_condom = False):
    # When called fuck_person starts a sex scene with someone. Sets up the encounter, mainly with situational modifiers.
    show screen person_info_ui(the_person)
    if report_log is None:
        $ report_log = defaultdict(int) #Holds information about the encounter: what position were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
        $ report_log["positions_used"] = [] #This is a list, not an int.

    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ position_choice = None
    $ object_choice = None
    $ repeat_strip_allowed = True #Set False when a girl is told not to strip something. She won't ask about stripping down any more for the rest of the encounter.


    call apply_sex_slut_modifiers(the_person, in_private = private) from _call_apply_sex_slut_modifiers_fuck_person
    $ report_log["was_public"] = not private



    #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.
    if the_person.love < 0:
        $ the_person.add_situational_slut("love_modifier", the_person.love, "I hate you, get away from me!")
    elif private:
        if the_person.has_role(girlfriend_role): #Girlfriend and affairs gain full Love
            $ the_person.add_situational_slut("love_modifier", the_person.love, "You're my special someone, I love you!")
        elif the_person.has_role(affair_role):
            $ the_person.add_situational_slut("love_modifier", the_person.love, "I have to keep it a secret, but I love you!")
        elif the_person.has_family_taboo(): #Family now only gains 1/4 (but this now helps offset the taboo penalty)
            if the_person.has_role(mother_role):
                $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "Even if it's wrong, a mother should do everything she can for her son!")
            elif the_person.has_role(sister_role):
                $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "I love my brother, and even if it's wrong I want to be close to him!")
            else: #Generic family one
                $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/4), "I love you, even though we're related!")
        else: #If you aren't in a relationship with them only half their Love applies.
            $ the_person.add_situational_slut("love_modifier", __builtin__.int(the_person.love/2), "I really like you, let's see where this goes!")

    $ happiness_effect = __builtin__.round((the_person.happiness - 100)/5.0)
    if the_person.happiness <= 95:
        if the_person.happiness <= 75:
            $ the_person.add_situational_slut("happiness_modifier", happiness_effect, "I'm so unhappy, I just don't want to do anything!")
        else:
            $ the_person.add_situational_slut("happiness_modifier", happiness_effect, "I'm just not in the mood right now.")
    elif the_person.happiness >= 105:
        if the_person.happiness >= 125:
            $ the_person.add_situational_slut("happiness_modifier", happiness_effect, "I'm so happy, I'm up for anything!")
        else:
            $ the_person.add_situational_slut("happiness_modifier", happiness_effect, "Today's a good day, let's see where this goes!")

    $ round_choice = "Change" # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    $ first_round = True
    $ initial_position = None
    $ mc_softened = False
    $ girl_considers_hard = False
    $ girl_considers_vagina = False
    $ girl_considers_tits = False
    $ vagina_available = the_person.outfit.vagina_available()
    $ tits_available = the_person.outfit.tits_available()


    while not finished:
        if girl_in_charge:
            # The girls decisions set round_choice here.
            if start_position is None: #The first time we get here
                $ pass
            else:
                $ position_choice = start_position

            if position_choice is None and (first_round or not position_locked):
                call girl_choose_position(the_person, ignore_taboo = ignore_taboo) from _call_girl_choose_position #Get her to pick a position based on what's available #TODO: This function
                $ position_choice = _return #Can be none, if no option was available for her to take.

            if position_choice is not None:
                if initial_position != position_choice:
                    $ object_choice = None
                # We need to make sure we're using an appopriate object
                if object_choice is None:
                    call girl_choose_object(the_person, position_choice,forced_object = start_object) from _call_girl_choose_object
                    $ object_choice = _return


            if report_log.get("girl orgasms", 0) > 0 and the_person.love < 10 and the_person.obedience < 110: #She's cum and doesn't care about you finishing.
                the_person "Whew, that felt great. Thanks for the good time [the_person.mc_title]!"
                $ round_choice = "Girl Leave"
            elif report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) > 0: #Both parties have been satisfied
                the_person "Whew, that felt amazing. It's good to know it was as good for you as it was for me."
                $ round_choice = "Girl Leave"
            elif position_choice is None: #There's no position we can take
                "[the_person.title] can't think of anything more to do with you."
                $ round_choice = "Girl Leave"
            elif object_choice is None:
                "[the_person.title] looks around, but can't see anywhere to have fun with you."
                $ round_choice = "Girl Leave"
            else:
                if initial_position != position_choice:
                    $ position_choice.redraw_scene(the_person)
                    if first_round:
                        if not skip_intro:
                            $ the_person.draw_person() #Draw her standing until we pick a new position
                            if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                                $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                                $ the_person.break_taboo(position_choice.associated_taboo)
                            else:
                                $ position_choice.call_intro(the_person, mc.location, object_choice)
                    else:
                        $ the_person.change_arousal(-5) #Changing position lowers your arousal slightly
                        $ mc.change_arousal(-5)
                        if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                            $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
                else:
                    "[the_person.possessive_title] is in control, and keeps on [position_choice.verbing] you."
                $ round_choice = "Continue"

        else:
            # Forced actions (when the guy is in charge) go here and set round_choice.
            pass
            # if position_choice is None:
            #     $ round_choice = "Change" #Something has kicked our position out, so we need to ask the player what to do.

            # Note: There can be no chance based decisions in this section, because it loops on menu interactions, not on actual rounds of sex. Those go after the "change or continue" loop

        if round_choice is None: #If there is no set round_choice
            #TODO: Add a variant of this list when the girl is in control to ask if you want to resist or ask/beg for something.
            $ option_list = []
            python:
                if position_choice is not None:
                    option_list.append(["Keep " + position_choice.verbing + " her.\n" + position_choice.build_energy_arousal_line(the_person),"Continue"]) #Note: you're prevented from continuing if the energy cost would be too high by the pre-round checks.
                    option_list.append(["Pause and strip her down","Strip"])

                    if not position_locked and object_choice:
                        option_list.append(["Pause and change position\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
                        for position in position_choice.connections:
                            if object_choice.has_trait(position.requires_location):
                                appended_name = "Transition to " + position.build_position_willingness_string(the_person) #Note: clothing and energy checks are done inside of build_position_willingness, invalid positiosn marked (disabled)
                                option_list.append([appended_name,position])

                    if the_person.has_role(hypno_orgasm_role) and object_choice is not None and not the_person.event_triggers_dict.get("hypno_orgasmed_recently", False):
                        option_list.append(["Trigger an orgasm.","Hypno_Orgasm"])

                    if not hide_leave: #TODO: Double check that we can always get out
                        option_list.append(["Stop " + position_choice.verbing + " her and leave", "Leave"]) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

                else:
                    if not position_locked:
                        option_list.append(["Pick a new position\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
                    if not hide_leave:
                        option_list.append(["Stop and leave", "Leave"])

            $ round_choice = renpy.display_menu(option_list,True,"Choice") #This gets the players choice for what to do this round.


        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignroe all of that
                $ mc.condom = False # If we're changing position we want to be able to re-check if we need a condom.
                if start_position is None: #The first time we get here,
                    call pick_position(the_person, ignore_taboo = ignore_taboo) from _call_pick_position
                    $ position_choice = _return
                else:
                    $ position_choice = start_position

                if start_object is None:
                    call pick_object(the_person, position_choice) from _call_pick_object
                    $ object_choice = _return
                else:
                    call pick_object(the_person, position_choice, forced_object = start_object) from _call_pick_object_1
                    $ object_choice = _return

                if position_choice and object_choice and not position_locked:
                    call check_position_willingness(the_person, position_choice, ignore_taboo = ignore_taboo, skip_condom = skip_condom) from _call_check_position_willingness
                    if not _return: #If she wasn't willing for whatever reason (too slutty a position, not willing to wear a condom) we clear our settings and try again.
                        $ position_choice = None
                        $ object_choice = None
                        call clear_object_effects(the_person) from _call_clear_object_effects

                if position_choice and object_choice:
                    $ position_choice.redraw_scene(the_person)
                    if first_round:
                        if not skip_intro:
                            $ the_person.draw_person() #Draw her standing until we pick a new position
                            if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                                $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                                $ the_person.break_taboo(position_choice.associated_taboo)
                            else:
                                $ position_choice.call_intro(the_person, mc.location, object_choice)
                    else:
                        $ the_person.change_arousal(-5) #Changing position lowers your arousal slightly
                        $ mc.change_arousal(-5)
                        if the_person.has_taboo(position_choice.associated_taboo) and not ignore_taboo:
                            $ position_choice.call_taboo_break(the_person, mc.location, object_choice)
                            $ the_person.break_taboo(position_choice.associated_taboo)
                        else:
                            $ position_choice.call_transition(None, the_person, mc.location, object_choice)
                    # redraw position after transitions
                    $ position_choice.redraw_scene(the_person)

            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ start_object = None
            if position_choice and object_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                call sex_description(the_person, position_choice, object_choice, private = private, report_log = report_log) from _call_sex_description
                $ first_round = False
                $ initial_position = position_choice
                if mc.recently_orgasmed and not mc_softened:
                    $ mc_softened = True
                    $ girl_considers_hard = False
                if mc_softened and not mc.recently_orgasmed:
                    $ mc_softened = False
                    $ girl_considers_hard = True
                if position_choice.requires_hard and mc.recently_orgasmed:
                    "Your post-orgasm cock softens, stopping you from [position_choice.verbing] [the_person.possessive_title] for now."
                    $ position_choice = None
                elif girl_in_charge and not position_choice.requires_hard and girl_considers_hard and not position_locked:
                    "[the_person.possessive_title] considers your stiffened cock."
                    $ girl_considers_hard = False
                    $ position_choice = None
                elif position_choice.guy_energy > mc.energy:
                    if girl_in_charge:
                        "You're too exhausted to let [the_person.possessive_title] keep [position_choice.verbing] you."
                    else:
                        "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                    $ position_choice = None
                elif position_choice.girl_energy > the_person.energy:
                    #TODO: Add some differentiated dialgoue depending on the position.
                    #TODO: Add "no energy" transitions where you keep fucking her anyways. (double TODO: Add a way of "breaking" her like this)
                    the_person "I'm exhausted [the_person.mc_title], I can't keep this up..."
                    $ position_choice = None
                else: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                    if self_strip:
                        call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event
                        $ girl_considers_vagina = the_person.outfit.vagina_available() != vagina_available
                        $ vagina_available = the_person.outfit.vagina_available()
                        $ girl_considers_tits = the_person.outfit.tits_available() != tits_available
                        $ tits_available = the_person.outfit.tits_available()
                        if girl_in_charge and position_choice != None and not position_locked:
                            if girl_considers_vagina:
                                "[the_person.possessive_title]'s fingers brush over her pussy."
                                $ position_choice = None
                            elif girl_considers_tits:
                                "[the_person.possessive_title]'s hand caresses her tits."
                                $ position_choice = None
                    if position_choice != None and not position_locked:
                        if the_person.effective_sluttiness() > position_choice.slut_cap: #She's sluttier than this position, it's only good to warm her up.
                            if the_person.arousal > position_choice.slut_cap: #Once her arousal is higher than the cap she's completely bored by it.
                                "[the_person.title] wants to spice things up."
                                if girl_in_charge:
                                    $ position_choice = None


        elif isinstance(round_choice, Position): #The only non-strings on the list are positions we are changing to
            call check_position_willingness(the_person, round_choice, ignore_taboo = ignore_taboo, skip_condom = True) from _call_check_position_willingness_1
            if _return:
                $ round_choice.redraw_scene(the_person)
                if the_person.has_taboo(round_choice.associated_taboo) and not ignore_taboo:
                    $ round_choice.call_taboo_break(the_person, mc.location, object_choice)
                    $ the_person.break_taboo(round_choice.associated_taboo)
                else:
                    $ position_choice.call_transition(round_choice, the_person, mc.location, object_choice)
                $ position_choice = round_choice

            else: #If she wasn't willing we keep going with what we were doing, so just loop around.
                pass

        elif round_choice == "Strip":
            call strip_menu(the_person, position_choice, private) from _call_strip_menu

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end
            if renpy.random.randint(0,the_person.arousal) + 50 > the_person.obedience and the_person.energy >= 30 and report_log.get("girl orgasms", 0) == 0: #She's disobedient and will take control of the encounter. disobed
                $ the_person.call_dialogue("sex_take_control")
                $ the_person.change_obedience(-3)
                $ girl_in_charge = True
                $ finished = False
                $ position_choice = None #She picks the position now, because she has her own list of possibilities
                $ position_locked = False
            elif (the_person.arousal > the_person.max_arousal - 30) and (report_log.get("girl orgasms", 0) == 0) and report_log.get("beg finish", 0) == 0 and the_person.energy >= 30: #Within 30 of orgasming and she hasn't cum yet
                # They're close to their orgasm and beg you to help them finish.
                $ the_person.call_dialogue("sex_beg_finish")
                menu:
                    "Give her what she wants":
                        $ the_person.change_obedience(2)
                        if "beg finished" in report_log.keys():
                            $ report_log["beg finish"] += 1
                        else:
                            $ report_log["beg finish"] = 1
                        $ finished = False

                    "Stop and leave":
                        $ the_person.call_dialogue("sex_end_early")

            elif report_log.get("beg finish", 0) > 0 and report_log.get("girl orgasms", 0) == 0: #You promised to make her cum but didn't
                $ the_person.change_obedience(-5)
                $ the_person.change_happiness(-10)
                $ the_person.change_love(-3)
                the_person "But you promised..."
                #TODO: Add some personality specific dialgoue for this

            else: # You end the encounter and nothing special happens.
                #TODO: Add some personality specfic dialogue
                pass

        elif round_choice == "Girl Leave":
            $ finished = True

        elif round_choice == "Hypno_Orgasm":
            $ the_person.event_triggers_dict["hypno_orgasmed_recently"] = True
            $ the_word = the_person.event_triggers_dict.get("hypno_trigger_word","Cum")
            $ the_word.capitalize()
            mc.name "[the_word]."
            $ the_person.change_arousal(the_person.max_arousal)
            "[the_person.possessive_title] whimpers with pleasure as your training takes hold of her brain."
            call describe_girl_climax(the_person, position_choice, object_choice, private, report_log) from _call_describe_girl_climax_1 #Calls just the climax stuff without costing energy.

        $ round_choice = None #Get rid of our round choice at the end of the round to prepare for the next one. By doing this at the end instead of the begining of the loop we can set a mandatory choice for the first one.

    call clear_sex_slut_modifiers(the_person) from _call_clear_sex_slut_modifiers_fuck_person

    $ report_log["end arousal"] = the_person.arousal

    $ orgasms_recieved = report_log.get("girl orgasms",0)

    if orgasms_recieved > 0:
        $ the_person.change_arousal(-((the_person.arousal)/(orgasms_recieved+1))) # The more you make her cum the more satisfied she will be. At 0 orgasms her arousal does not move - you've just edged her!


    $ mc.condom = False
    $ mc.recently_orgasmed = False

    if affair_ask_after and private and ask_girlfriend_requirement(the_person) is True and not the_person.relationship == "Single":
        if the_person.love >= 60 and the_person.effective_sluttiness() >= 30 - (the_person.get_opinion_score("cheating on men") * 5) and report_log.get("girl orgasms",0) >= 1: #If she loves you enoguh, is moderately slutty, and you made her cum
            call affair_check(the_person, report_log) from _call_affair_check


    python: #Log all of the different classes of sex, but only once per class.
        types_seen = []
        for position_type in report_log.get("positions_used",[]): #Note: Clears out duplicates
            if position_type.record_class and position_type.record_class not in types_seen:
                the_person.sex_record[position_type.record_class] += 1
                types_seen.append(position_type.record_class)


    $ the_person.outfit.restore_all_clothing() #Pull all of her half-off clothing back into place.

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label pick_position(the_person, allow_none = True, ignore_taboo = False):
    $ position_option_list = []
    python:
        for position in list_of_positions: #No choice is given, so pick a position
            if mc.location.has_object_with_trait(position.requires_location) and (the_person.has_large_tits() or not position.requires_large_tits): #There is a valid object and if it requires large tits she has them.
                #Note: clothing checks are done in the build_position_willingness_string() check, where it markes them as obstructed and (disabled).
                position_option_list.append([position.build_position_willingness_string(the_person, ignore_taboo = ignore_taboo), position])
        if allow_none:
            position_option_list.append(["Nothing", "Nothing"])

    $ picked_position = renpy.display_menu(position_option_list,True,"Choice")

    $ del position_option_list
    if picked_position == "Nothing":
        $ picked_position = None

    return picked_position #Can be None, which just means "never mind"

label girl_choose_position(the_person, ignore_taboo = False):
    $ position_option_list = []
    python:
        for position in list_of_girl_positions:
            if mc.location.has_object_with_trait(position.requires_location):
                if position.her_position_willingness_check(the_person, ignore_taboo):
                    position_option_list.append(position)
        picked_position = get_random_from_list(position_option_list)
    $ del position_option_list
    return picked_position

label girl_choose_object(the_person, the_position, forced_object = None):
    $ possible_object_list = []
    if the_position is None:
        $ the_person.clear_situational_slut("sex_object")
        $ the_person.clear_situational_obedience("sex_object")
        return None
    python:
        for an_object in mc.location.objects_with_trait(the_position.requires_location):
            possible_object_list.append(an_object)
    if forced_object:
        $ picked_object = forced_object
    else:
        $ picked_object = get_random_from_list(possible_object_list)
    $ the_person.add_situational_slut("sex_object", picked_object.sluttiness_modifier, the_position.verbing + " on a " + picked_object.name)
    $ the_person.add_situational_obedience("sex_object",picked_object.obedience_modifier, the_position.verbing + " on a " + picked_object.name)
    return picked_object


label pick_object(the_person, the_position, forced_object = None):
    if the_position is None:
        return None

    $ object_option_list = []
    if the_position is None:
        $ the_person.clear_situational_slut("sex_object")
        $ the_person.clear_situational_obedience("sex_object")
        return None

    python:
        if forced_object:
            picked_object = forced_object
        else:
            for object in mc.location.objects:
                if object.has_trait(the_position.requires_location):
                    object_option_list.append([object.get_formatted_name(),object]) #Displays a list of objects in the room related to that position and their appropriate bonuses/penalties


            if (__builtin__.len(object_option_list) > 1):
                picked_object = renpy.display_menu(object_option_list,True,"Choice")
            elif (__builtin__.len(object_option_list) == 1):
                picked_object = object_option_list[0][1]


    $ del object_option_list
    $ the_person.add_situational_slut("sex_object", picked_object.sluttiness_modifier, the_position.verbing + " on a " + picked_object.name)
    $ the_person.add_situational_obedience("sex_object",picked_object.obedience_modifier, the_position.verbing + " on a " + picked_object.name)
    return picked_object

label check_position_willingness(the_person, the_position, ignore_taboo = False, skip_condom = False): #Returns if the person is willing to do this position or not, and charges the appropriate happiness hit if they needed obedience to be willing.
    $ willing = True
    $ the_taboo = the_position.associated_taboo
    if ignore_taboo:
        $ the_taboo = None

    if the_person.effective_sluttiness(the_taboo) >= the_position.slut_requirement:
        if not the_person.has_taboo(the_taboo):
            $ the_person.call_dialogue("sex_accept")
    elif the_person.effective_sluttiness(the_taboo) + (the_person.obedience-100) >= the_position.slut_requirement:
        # She's willing to be commanded to do it. Reduce her happiness by the difference (increase arousal if she likes being submissive)
        "[the_person.possessive_title] doesn't seem enthusiastic, but a little forceful encouragement would probably convince her."
        menu:
            "Order her":
                mc.name "[the_person.title], this is going to happen."
                $ happiness_drop = the_person.effective_sluttiness(the_position.associated_taboo) - the_position.slut_requirement #Our initial conditions mean this is a negative number
                $ the_person.change_arousal(the_person.get_opinion_score("being submissive")*2)
                $ the_person.discover_opinion("being submissive")
                $ the_person.change_happiness(happiness_drop)
                if the_person.has_taboo(the_taboo):
                    pass #If there is a taboo being broken we have special taboo break dialogue called from the position. TODO: We should have obedience specific taboo breaks (with variants for how much she dislikes it)
                else:
                    $ the_person.call_dialogue("sex_obedience_accept")
                $ report_log["used_obedience"] = True
                $ willing = True
            "Try something else":
                mc.name "Let's try something else that you might be more comfortable with."
                $ willing = False

    elif the_person.effective_sluttiness(the_taboo) > the_position.slut_requirement/2:
        # She's not willing to do it, but gives you a soft reject.
        $ the_person.call_dialogue("sex_gentle_reject")
        $ willing = False

    else:
        # You're nowhere close to the required sluttiness, lose some love for even trying.
        $ love_loss = the_person.effective_sluttiness(the_taboo) - the_position.slut_requirement #A negative number
        $ love_loss = __builtin__.round(love_loss/5)
        $ the_person.change_love(love_loss)
        $ the_person.call_dialogue("sex_angry_reject")
        $ willing = False

    if willing and the_position.skill_tag == "Vaginal" and not mc.condom and not skip_condom: #We might need a condom, which means she might say no. TODO: Add an option to pull _off_ a condom while having sex.
        # skip_condom is should be used any time you're transitioning - it's a fluid change and not enough of a difference for them to have a moment to stop you.
        call condom_ask(the_person) from _call_condom_ask
        $ willing = _return

    return willing

label clear_object_effects(the_person):
    $ the_person.clear_situational_slut("sex_object")
    $ the_person.clear_situational_obedience("sex_object")
    return

label sex_description(the_person, the_position, the_object, private = True, report_log = None):
    # Processes a single normal "round" of sex. Removes energy, increases arousal, calls for dialogue from people nearby, etc. then returns to the main loop.

    # Draw the person and deliver the position specific description
    $ the_position.redraw_scene(the_person)
    $ the_position.call_scene(the_person, mc.location, the_object)
    $ mc.listener_system.fire_event("sex_event", the_person = the_person, the_position = the_position, the_object = the_object)

    if the_person.lactation_sources > 0:
        call lactation_description(the_person, the_position, the_object, report_log) from _call_lactation_description

    if report_log is not None:
        $ report_log["total rounds"] += 1

    # Change the arousal for both people:

    # Her arousal first
    $ her_arousal_change = the_position.girl_arousal * (1.0 + 0.1 * mc.sex_skills[the_position.skill_tag]) # Each level the other party has in the sex class adds 10% arousal.
    if the_position.skill_tag == "Vaginal":
        $ the_person.discover_opinion("bareback sex")
        if mc.condom:
            $ her_arousal_change += -1 # Condoms don't feel as good (but matter less for her)
            $ her_arousal_change += -2 * the_person.get_opinion_score("bareback sex")
        else:
            $ her_arousal_change += 2 * the_person.get_opinion_score("bareback sex")

    $ opinion_score = get_position_opinion_score(the_person, the_position)
    $ her_arousal_change += opinion_score

    if the_person.effective_sluttiness() > the_position.slut_cap: #She's sluttier than this position, it's only good to warm her up.
        if opinion_score < 1 and the_person.arousal > the_position.slut_cap: #Once her arousal is higher than the cap he's completely bored by it.
            $ mc.log_event(the_person.title + ": Bored by position. Arousal gain halved.", "float_text_red")
            $ her_arousal_change = her_arousal_change / 2

    $ clothing_count = 0
    $ interfering_clothing = []
    if the_position.skill_tag == "Vaginal" or the_position.skill_tag == "Anal":
        python:
            for clothing in the_person.outfit.get_lower_ordered():
                if clothing.anchor_below and clothing.half_off_gives_access and clothing.half_off:
                    clothing_count += 1 #Each piece of clothing that's only half off lowers the amount of arousal gain for both parties
                    interfering_clothing.append(clothing)

    elif the_position.requires_large_tits:
        python:
            for clothing in the_person.outfit.get_upper_ordered():
                if clothing.anchor_below and clothing.half_off_gives_access and clothing.half_off:
                    clothing_count += 1 #Each piece of clothing that's only half off lowers the amount of arousal gain for both parties
                    interfering_clothing.append(clothing)

    if clothing_count > 0:
        $ clothing_string = format_list_of_clothing(interfering_clothing)
        "[the_person.title]'s half off [clothing_string] get in the way, lowering your enjoyment somewhat."
    $ del interfering_clothing

    $ her_arousal_change += -clothing_count
    $ the_person.change_arousal(her_arousal_change)

    # Now his arousal change
    $ his_arousal_change = the_position.guy_arousal * (1.0 + 0.1 * the_person.sex_skills[the_position.skill_tag])
    $ his_arousal_change += -clothing_count
    if the_position.skill_tag == "Vaginal" and mc.condom:
        $ his_arousal_change += -2 # Condoms don't feel as good.

    $ mc.change_arousal(his_arousal_change)
    $ mc.locked_clarity += (the_position.guy_arousal * the_person.sex_skills[the_position.skill_tag])
    if mc.recently_orgasmed and mc.arousal >= 10:
        $ mc.recently_orgasmed = False
        "Your cock stiffens again, coaxed back to life by [the_person.title]."


    # Change their energy as well.
    $ the_person.change_energy(-the_position.girl_energy, add_to_log = False) #NOTE: Don't show the energy cost to avoid energy notice spam. The energy cost is already displayed to the player.
    $ mc.change_energy(-the_position.guy_energy, add_to_log = False)

    # If someone orgasms describe that.
    if the_person.arousal >= the_person.max_arousal:
        call describe_girl_climax(the_person, the_position, the_object, private, report_log) from _call_describe_girl_climax_2



    if mc.arousal >= 80: #NOTE: use to be mc.max_arousal, this number is now the threshold for being forced to cum.
        call climax_check() from _call_climax_check_sex_description
        $ is_cumming = _return

        if is_cumming:
            $ the_position.call_outro(the_person, mc.location, the_object)
            if the_person.effective_sluttiness(the_position.associated_taboo) < the_position.slut_requirement: # bonus obedience if she if she had to be ordered to do this position ("I guess I really am just doing this for him...")
                $ the_person.change_obedience(3 + the_person.get_opinion_score("being submissive"))
            else:
                $ the_person.change_obedience(3)
            # $ mc.reset_arousal() The actual sex psoitions include a do_clarity_release call which will reset MC arousal.
            $ mc.recently_orgasmed = True
            $ report_log["guy orgasms"] += 1

    if not private:
        call watcher_check(the_person, the_position, the_object, report_log) from _call_watcher_check

    if report_log:
        $ report_log["positions_used"].append(the_position)

    return

label climax_check():
    $ is_cumming = False
    if mc.arousal < mc.max_arousal:
        menu:
            "Try and cum early":
                if renpy.random.randint(0,100) < 10*mc.focus + (mc.max_arousal - mc.arousal):
                    $ is_cumming = True
                    "You focus as hard as you can and feel yourself grow closer and closer to climax."
                else:
                    "You focus as hard as you can, but you're unable to push yourself over the edge."

            "Keep going!":
                pass
    else:
        menu:
            "Try to hold back":
                if renpy.random.randint(0,100) < 10*mc.focus + (mc.max_arousal - mc.arousal): #Note: arousal is > max_arousal, so that's focus - some number, ie it's harder and harder as your arousal increases.
                    "You focus yourself and stave off your climax for a little longer."
                else:
                    "You focus as hard as you can, but there's nothing you can do at this point!"
                    $ is_cumming = True

            "Cum!":
                $ is_cumming = True

    return is_cumming

label apply_sex_slut_modifiers(the_person, in_private = True):
    # Family situational modifiers
    if the_person.has_family_taboo(): #Check if any of the roles the person has belong to the list of family roles.
        $ the_person.add_situational_slut("taboo_sex", -20, "We're related, we shouldn't be doing this.")

    #Cheating modifiers
    if the_person.relationship != "Single":
        $ the_person.discover_opinion("cheating on men")
    if the_person.relationship == "Girlfriend":
        if the_person.get_opinion_score("cheating on men") > 0:
            $ the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 5, "I'm cheating on my boyfriend!")
        else:
            $ the_person.add_situational_slut("cheating", -5 + (the_person.get_opinion_score("cheating on men") * 10), "I can't cheat on my boyfriend!")
    elif the_person.relationship == "Fiancée":
        if the_person.get_opinion_score("cheating on men") > 0:
            $ the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 8, "I'm cheating on my fiancé!")
        else:
            $ the_person.add_situational_slut("cheating", -15 + (the_person.get_opinion_score("cheating on men") * 15), "I could never cheat on my fiancé!")
    elif the_person.relationship == "Married":
        if the_person.get_opinion_score("cheating on men") > 0:
            $ the_person.add_situational_slut("cheating", the_person.get_opinion_score("cheating on men") * 10, "I'm cheating on my husband!")
        else:
            $ the_person.add_situational_slut("cheating", -20 + (the_person.get_opinion_score("cheating on men") * 20), "I could never cheat on my husband!")

    #Privacy modifiers
    if mc.location.get_person_count() == 1 and not in_private:
        $ in_private = True #If we're alone in the space we're always Private, even if we had left the possibility for people being around.

    if not in_private:
        if the_person.effective_sluttiness() < 50:
            $ the_person.add_situational_slut("public_sex", -10 + the_person.get_opinion_score("public sex") * 5, "There are people watching...")
        else:
            $ the_person.add_situational_slut("public_sex", the_person.get_opinion_score("public sex") * 5, "There are people watching!")

    return

label clear_sex_slut_modifiers(the_person):
    if the_person is None:
        return

    python:
        the_person.clear_situational_slut("love_modifier")
        the_person.clear_situational_slut("happiness_modifier")
        the_person.clear_situational_slut("cheating")
        the_person.clear_situational_slut("taboo_sex")
        the_person.clear_situational_slut("sex_object")
        the_person.clear_situational_slut("public_sex")
        the_person.clear_situational_obedience("sex_object")
    return

# TODO: Replace Private being a boolean with being a bool OR a list, when a list it is the people we should consider being in the scene. When it is true it is everyone, when false no one.
label watcher_check(the_person, the_position, the_object, the_report): # Check to see if anyone is around to comment on the characters having sex.
    $ other_people = [person for person in mc.location.people if person is not the_person] #Build a list with all the _other_ people in the room other than the one we're fucking.
    python: #Checks to see if anyone watching is in a relationship, and if they are sets up an event where they confront you later about you actively cheating in front of the,
        for a_person in other_people:
            if a_person.get_opinion_score("public sex") > 0:
                a_person.add_situational_slut("public sex watcher", 5*a_person.get_opinion_score("public sex"), "They're doing it right in front of me! That's so fucking hot!")
            elif a_person.get_opinion_score("public sex") < 0:
                a_person.add_situational_slut("public sex watcher", 5*a_person.get_opinion_score("public sex"), "Right here in front of me?! That's disgusting!")

            if a_person.has_role(girlfriend_role) and the_position.slut_requirement > (a_person.effective_sluttiness()/2): #You can get away with stuff half as slutty as she would do
                caught_cheating_action = Action("Caught cheating action", caught_cheating_requirement, "caught_cheating_label", args = the_person)
                not_already_in = True
                for an_action in a_person.on_room_enter_event_list:
                    if an_action == caught_cheating_action:
                        not_already_in = False

                if not_already_in:
                    a_person.on_room_enter_event_list.append(caught_cheating_action)
                    renpy.say(None,a_person.title + " gasps when she sees what you and " + the_person.title + " are doing.")


            elif a_person.has_role(affair_role) and the_position.slut_requirement > ((a_person.effective_sluttiness()*2)/3): #You can get away with stuff two thirds as slutty as what she would do.
                caught_affair_cheating_action = Action("Caught affair cheating action", caught_affair_cheating_requirement, "caught_affair_cheating_label", args = the_person)
                not_already_in = True
                for an_action in a_person.on_room_enter_event_list:
                    if an_action == caught_affair_cheating_action:
                        not_already_in = False

                if not_already_in:
                    a_person.on_room_enter_event_list.append(caught_affair_cheating_action)
                    renpy.say(None,a_person.title + " gasps when she sees what you and " + the_person.title + " are doing.")

    $ the_watcher = get_random_from_list(other_people) #Get a random person from the people in the area, if there are any.
    if the_watcher:
        # NOTE: the dialogue here often draws the person talking with various emotions or positions, so we redraw the scene after we call them.
        $ the_watcher.call_dialogue("sex_watch", the_sex_person = the_person, the_position = the_position) #Get the watcher's reaction to the people having sex. This might include dialogue calls from other personalities as well!
        $ the_position.redraw_scene(the_person)
        $ the_person.call_dialogue("being_watched", the_watcher = the_watcher, the_position = the_position) #Call her response to the person watching her.
        $ the_person.change_arousal(the_person.get_opinion_score("public sex"))
        $ the_person.discover_opinion("public sex")

    python:
        for a_person in other_people:
            a_person.clear_situational_slut("public sex watcher")
        del other_people
    return

label describe_girl_climax(the_person, the_position, the_object, private, report_log):
    $ the_position.call_orgasm(the_person, mc.location, the_object)
    $ the_person.change_arousal(-__builtin__.max(the_person.arousal/(report_log.get("girl orgasms", 0)+2), the_person.arousal - 99)) # Repeated orgasms make it easier and easier to make a girl cum. It's possible to make her cum every single round!
    $ trance_chance_modifier = get_position_trance_chance_modifier(the_person, the_position) + report_log.get("girl orgasms", 0)
    if not trance_chance_modifier == 0:
        $ mc.log_event("Trance chance modified by " + str(trance_chance_modifier) + "% due to position opinion and previous orgasms.", "float_text_grey")
    $ the_person.run_orgasm(trance_chance_modifier = trance_chance_modifier, sluttiness_increase_limit = the_position.slut_requirement, reset_arousal = False)
    $ report_log["girl orgasms"] += 1
    return

label condom_ask(the_person):
    $ condom_threshold = the_person.get_no_condom_threshold()
    if the_person.has_role(pregnant_role) and the_person.event_triggers_dict.get("preg_knows", False):
        the_person "We don't need to worry about using a condom any more. You can't get me {i}more{/i} pregnant."

    elif the_person.effective_sluttiness("condomless_sex") < condom_threshold: # they demand you put on a condom.
        $ the_person.call_dialogue("condom_demand")
        menu:
            "Put on a condom":
                $ mc.condom = True
                "You pull out a condom from your wallet and rip open the package. [the_person.title] watches while you slide it on."

            "Refuse and do something else":
                "[the_person.title] doesn't seem like she's going to change her mind."
                mc.name "I don't have one on me. Guess we'll have to do it some other way."
                return False

            "Fuck her raw anyways" if the_person.obedience >= 150:
                mc.name "No way, this pussy is getting fucked raw."
                if the_person.has_taboo("condomless_sex"):
                    $ the_person.call_dialogue("condomless_sex_taboo_break")
                else:
                    if the_person.on_birth_control:
                        "[the_person.title] doesn't argue with you any more."
                    else:
                        if the_person.get_opinion_score("creampies") > 0:
                            the_person "Oh fuck, If you cum inside I'm going to get knocked up..."
                            "You aren't sure if she's worried or excited."
                        else:
                            $ the_person.update_birth_control_knowledge()
                            the_person "I'm not on birth control [the_person.mc_title], promise you won't cum inside me."
                            call condomless_promise(the_person) from _call_condomless_promise_condom_ask_1


            "Fuck her raw anyways\n{color=#ff0000}{size=18}Requires: 150 Obedience{/size}{/color} (disabled)" if the_person.obedience < 150:
                pass



    elif the_person.get_opinion_score("bareback sex") < 0 or the_person.effective_sluttiness("condomless_sex") < condom_threshold + 20 or the_person.has_taboo("condomless_sex"): # They suggest you put on a condom.
        $ the_person.call_dialogue("condom_ask")
        menu:
            "Put on a condom":
                $ mc.condom = True
                mc.name "I think you're right. One second."
                "[the_person.title] watches eagerly while you pull a condom out of your wallet, tear open the package, and unroll it down your dick."

            "Fuck her raw":
                mc.name "No way. I want to feel you wrapped around me."
                if the_person.has_taboo("condomless_sex"):
                    $ the_person.call_dialogue("condomless_sex_taboo_break")
                else:
                    if the_person.on_birth_control:
                        the_person "Okay. I'm on birth control, so it should be fine."
                        $ the_person.update_birth_control_knowledge()
                    else:
                        the_person "Fine, but you {i}really{/i} need to pull out this time. We shouldn't be taking risks like that."
                        call condomless_promise(the_person) from _call_condomless_promise_condom_ask_2

    else: #Slutty enough that she doesn't even care about a condom.
        if the_person.get_opinion_score("bareback sex") > 0 or the_person.get_opinion_score("creampies") > 0 or the_person.has_role(breeder_role):
            menu:
                "Put on a condom":
                    mc.name "One sec, let me just get a condom on..."
                    $ the_person.call_dialogue("condom_bareback_demand")
                    menu:
                        "Fuck her raw":
                            mc.name "Alright, as long as you know what you're getting into..."
                            "You abandon your plans to put on a condom and get ready to take [the_person.possessive_title] raw."

                        "Refuse and do something else":
                            "[the_person.possessive_title] seems like she's made up her cock-hungry mind, and you doubt you would be able to change it."
                            mc.name "We can't risk it [the_person.title]. We'll have to do something else."
                            return False

                        "Put on a condom anyways\n{color=#ff0000}{size=18}Requires: 140 Obedience{/size}{/color} (disabled)" if the_person.obedience < 140:
                            pass

                        "Put on a condom anyways." if the_person.obedience >= 140:
                            $ mc.condom = True
                            mc.name "I can't risk it [the_person.title], no matter how desperate you are for raw cock."
                            "You pull out a condom from your wallet, tear open the package, and start to unroll it down your dick."
                            mc.name "So you have a choice. You can have my cock inside you like this, or you can have no cock at all."
                            "She whimpers like a sad puppy, but you know there's only once choice she would ever make."
                            the_person "... Fine, just put it inside me already!"

                "Fuck her raw":
                    "You ignore any thoughts about putting on a condom and get ready to take [the_person.possessive_title] raw."

        else:
            $ the_person.call_dialogue("condom_bareback_ask")
            menu:
                "Put on a condom":
                    $ mc.condom = True
                    mc.name "Sorry, but I still think a condom is a good idea."
                    the_person "Fine, just make it quick please!"
                    "[the_person.title] watches impatiently while you pull a condom out of your wallet, tear open the package, and unroll it down your dick."

                "Fuck her raw":
                    mc.name "No arguments here."

    if mc.condom:
        "Sex with a condom on doesn't feel as good, for you or for her."
    else:
        $ the_person.break_taboo("condomless_sex")


    return True #If we make it to the end of the scene everything is fine and sex can continue. If we returned false we should go back to the position select, as if we asked for something to extreme.

label condomless_promise(the_person):
    menu:
        "Promise to pull out":
            mc.name "I'll pull out, don't worry."
            "[the_person.possessive_title] seems reassured by your promise."
            #TODO: Add negative stats if you promise and cum inside her anyways

        "Don't promise anything":
            mc.name "I'll do my best. I'm not sure I'll be able to resist."
            if not the_person.on_birth_control:
                the_person "You're going to get me pregnant if you aren't careful!"
            #TODO: Middle ground between warning her it's happening and lying to her.

        "Promise to cum inside":
            mc.name "Oh I'm not pulling out. I'm planning on dumping my load inside of your tight little pussy."
            if the_person.get_opinion_score("creampies") > 0:
                the_person "Oh god..."
            elif not the_person.on_birth_control:
                the_person "Fuck [the_person.mc_title], you're going to get me pregnant like that!"
                "She squirms uncomfortably, but this doesn't seem to be a deal breaker for her."
            else:
                the_person "Oh god, of course you are..."
            #TODO: Moderate stat penalties, but less than lying
    return

init 2 python:
    def build_sex_mechanic_strip_menu(person):
        full_off_list = ["Take off"]
        for clothing in the_person.outfit.get_unanchored():
            if not clothing.is_extension:
                formatted_name = clothing.display_name.capitalize() + "\n-5 {image=gui/extra_images/arousal_token.png}"
                full_off_list.append([formatted_name, [clothing,"Full"]]) #Keeps track if this was a full or partial strip, so we can reuse all of the strip taboo logic/dialogue

        half_off_list = ["Move away"]
        for clothing in the_person.outfit.get_unanchored(half_off_instead = True):
            if not clothing.half_off:
                half_off_list.append([clothing.display_name.capitalize(), [clothing,"Half"]])

        other_list = ["Other","Finish"]
        return [full_off_list, half_off_list, other_list]


label strip_menu(the_person, the_position, is_private = True): #TODO: Add an arousal cost to stripping a girl down, but give an arousal boost if she likes getting naked.
    python:
        the_verbing = the_position.verbing if isinstance(the_position, Position) else "wooing"
        the_position_tag = the_position.position_tag if isinstance(the_position, Position) else the_person.idle_pose


    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items(build_sex_mechanic_strip_menu(the_person)))
    else:
        call screen main_choice_display(build_sex_mechanic_strip_menu(the_person))
    $ choice_return = _return

    if not choice_return == "Finish":
        $ strip_choice = choice_return[0] #Gets what the actual potentially stripped item was.
        $ strip_type = choice_return[1] #Gets if this was a half-off or a full strip

        $ test_outfit = the_person.outfit.get_copy()
        if strip_type == "Half":
            $ test_outfit.half_off_clothing(strip_choice)
        else:
            $ test_outfit.remove_clothing(strip_choice)

        $ underwear_revealed = False
        $ boobs_revealed = False
        $ ass_revealed = False
        if (the_person.outfit.bra_covered() and the_person.outfit.panties_covered()) and not (test_outfit.bra_covered() and test_outfit.panties_covered()):
            $ underwear_revealed = True
        if (not the_person.outfit.tits_visible()) and test_outfit.tits_visible():
            $ boobs_revealed = True
        if (not the_person.outfit.vagina_visible()) and test_outfit.vagina_visible():
            $ ass_revealed = True

        $ willing_to_strip = False
        $ ordered_to_strip = False #TODO: Use this for some dialogue stuff later

        $ strip_requirement = 0
        if ass_revealed: #Doubles for pussy revealed
            $ strip_requirement = 40
        elif boobs_revealed:
            $ strip_requirement = 30
        elif underwear_revealed:
            $ strip_requirement = 20

        if ass_revealed and the_person.has_taboo("bare_pussy"):
            $ strip_requirement += 10
        if boobs_revealed and the_person.has_taboo("bare_tits"):
            $ strip_requirement += 10
        if underwear_revealed and the_person.has_taboo("underwear_nudity"):
            $ strip_requirement += 10

        if the_person.effective_sluttiness() >= strip_requirement: #Note that taboos are added separately.
            $ willing_to_strip = True

        # TODO: Check if we really care about this private option.
        if not is_private: #She also cares about what she will end up wearing in front of other people. #TODO: This hsould have special strip reject dialogue.
            $ willing_to_strip = willing_to_strip and the_person.judge_outfit(test_outfit, use_taboos = True)

        $ willing_if_ordered = False
        if not willing_to_strip: #If she won't strip we might have a chance to command her toself.
            $ ran_num = the_person.obedience - 100
            if strip_type == "Half":
                $ ran_num += 10 #She's more likely to listen to you obediently when you strip her quickly.

            if is_private:
                $ willing_if_ordered = the_person.effective_sluttiness() + ran_num >= strip_requirement
            else:
                $ willing_if_ordered = the_person.judge_outfit(test_outfit, temp_sluttiness_boost = ran_num, use_taboos = True)

            if willing_if_ordered:
                $ the_person.call_dialogue("strip_obedience_accept", the_clothing = strip_choice, strip_type = strip_type)
                menu:
                    "Do it anyways":
                        "You proceed despite [the_person.possessive_title]'s objections, trusting her to remain obedient and docile."
                        $ willing_to_strip = True
                        $ ordered_to_strip = True
                        $ the_person.discover_opinion("being submissive")
                        $ the_person.change_happiness(-5 + (5*the_person.get_opinion_score("being submissive")))

                    "Let it be":
                        "You leave [the_person.possessive_title]'s [strip_choice.display_name] in place, and she relaxes."

        if willing_to_strip:
            if ass_revealed and the_person.has_taboo("bare_pussy"):
                $ the_person.call_dialogue("bare_pussy_taboo_break", the_clothing =  strip_choice)
            elif boobs_revealed and the_person.has_taboo("bare_tits"):
                $ the_person.call_dialogue("bare_tits_taboo_break", the_clothing = strip_choice)
            elif underwear_revealed and the_person.has_taboo("underwear_nudity"):
                $ the_person.call_dialogue("underwear_nudity_taboo_break", the_clothing = strip_choice)

            if strip_type == "Half":
                $ the_person.draw_animated_removal(strip_choice, position = the_position_tag, half_off_instead = True)
                $ renpy.say(None,"You pull her " + strip_choice.display_name + " out of the way.")
            else:
                $ the_person.draw_animated_removal(strip_choice, position = the_position_tag)
                if strip_choice.half_off:
                    $ renpy.say(None, "You pull her " + strip_choice.display_name + " off entirely and drop it on the ground.")
                else:
                    $ renpy.say(None, "You pull her " + strip_choice.display_name + " off, dropping it to the ground.")

            $ arousal_change = 0
            if strip_type == "Full":
                $ arousal_change -= 5

            if underwear_revealed or boobs_revealed or ass_revealed:
                $ arousal_change += the_person.get_opinion_score("not wearing anything") * 2
                $ the_person.discover_opinion("not wearing anything")
                if underwear_revealed:
                    $ the_person.break_taboo("underwear_nudity")

            if boobs_revealed:
                $ arousal_change += the_person.get_opinion_score("showing her tits") * 3
                $ the_person.discover_opinion("showing her tits")
                $ the_person.break_taboo("bare_tits")
                if the_person.has_large_tits() and the_person.outfit.tits_available():
                    "Her big tits drop free, begging to be felt up."

            if ass_revealed:
                $ arousal_change += the_person.get_opinion_score("showing her ass") * 3
                $ the_person.discover_opinion("showing her ass")
                $ the_person.break_taboo("bare_pussy")


            if arousal_change > 0:
                the_person "Oh my god..."
                $ the_person.change_arousal(arousal_change)
                if the_person.arousal > the_person.max_arousal:
                    "[the_person.possessive_title] moans and shivers, seemingly on the edge of an orgasm."
                else:
                    if strip_type == "Half":
                        "[the_person.possessive_title] bites her lip and and moans as you pull at her clothing."
                    else:
                        "[the_person.possessive_title] bites her lip and and moans as you strip her down."
            elif arousal_change < 0:
                $ the_person.change_arousal(arousal_change)
                if strip_type == "Half":
                    "[the_person.possessive_title] is impatient as you pull at her clothing."
                else:
                    "[the_person.possessive_title] is impatient as you strip her down."

        else:
            if not willing_if_ordered: #If she was willing if ordered then the dialogue is called up top.
                if strip_type == "Half":
                    $ renpy.say(None, "You start to pull " + the_person.title + "'s " + strip_choice.name + " out of the way.")
                    $ renpy.say(None, "She grabs your hand gently.")
                else:
                    $ renpy.say(None, "You start to pull off " + the_person.title + "'s " + strip_choice.name + " when she grabs your hand and stops you.")
                $ the_person.call_dialogue("strip_reject", the_clothing = strip_choice , strip_type = strip_type) #TODO: pass the piece of clothing and base some dialogue off of that.
        $ renpy.call("strip_menu", the_person, the_position, is_private) #TODO: Girl sometimes interupts you to get you to keep going. Have to strip them down in segments.

    python:
        choice_return = None
        test_outfit = None
        strip_choice = None
        the_verbing = None
        the_position_tag = None
    return

label girl_strip_event(the_person, the_position, the_object):
    # Called when the girl has a chance of stripping down. Checks what she's prefer to strip based on her opinions.
    $ strip_chance = the_person.effective_sluttiness() - the_person.outfit.slut_requirement
    $ strip_chance += the_person.get_opinion_score("not wearing anything") * 5
    $ the_clothing = None

    if the_person.get_opinion_score("showing her tits") > the_person.get_opinion_score("showing her ass"): # If she has a preference (even a least-bad preference) she'll strip that down first.
        $ the_clothing = the_person.outfit.remove_random_any(exclude_feet = True, exclude_lower = True, do_not_remove = True)
    elif the_person.get_opinion_score("showing her tits") < the_person.get_opinion_score("showing her ass"):
        $ the_clothing = the_person.outfit.remove_random_any(exclude_feet = True, exclude_upper = True, do_not_remove = True)

    if the_clothing is None: #Either our previous checks failed to produce anything OR they were equal
        $ the_clothing = the_person.outfit.remove_random_any(exclude_feet = True, do_not_remove = True)

    if renpy.random.randint(0,100) < strip_chance and the_clothing:
        $ ask_chance = renpy.random.randint(0,100)
        if ask_chance < the_person.obedience - the_person.arousal:
            if repeat_strip_allowed:
                $ the_position.call_strip_ask(the_person, the_clothing, mc.location, the_object)
                $ repeat_strip_allowed = _return
        else:
            $ the_position.call_strip(the_person, the_clothing, mc.location, the_object) #If a girl's outfit is less slutty than she is currently feeling (with arousal factored in) she will want to strip stuff off.

    $ the_person.update_outfit_taboos()
    $ the_clothing = None
    return

label affair_check(the_person, report_log): #Report log is handed over so we can make reference to the specific scene if we want.
    $ so_title = SO_relationship_to_title(the_person.relationship)
    the_person "[the_person.mc_title], you make me feel ways my [so_title] never does. I feel alive! Excited! Aroused..."
    the_person "We both have feeling for each other, right? Maybe we can see each other some more. My [so_title] doesn't need to know. He'll never find out."
    $ the_person.discover_opinion("cheating on men")
    menu:
        "Have an affair with [the_person.title]":
            mc.name "I want that too, anything that will let me be close to you."
            $ the_person.draw_person(emotion = "happy")
            $ the_person.add_role(affair_role)
            $ the_person.change_slut(2, 60)
            "She smiles and hugs you."

        "Refuse":
            mc.name "That's not what I'm here for [the_person.title]. This was fun, but I don't want it to be anything but completely casual."
            $ the_person.change_love(-1)
    return

label lactation_description(the_person, the_position, the_object, report_log): #NOTE: Is only called if lactation_sources > 0.
    $ tit_rank = rank_tits(the_person.tits)
    $ strength = (the_person.arousal*1.0/the_person.max_arousal) * (the_person.lactation_sources + (tit_rank * 0.1)) #ie large tits add anywhere from 0 to 0.9 extra lactation sources.
    if strength > tit_rank + 1:
        $ strength = tit_rank + 1

    if the_person.outfit.tits_available():
        if strength <= 0.5:
            pass
        elif strength <= 0.75:
            "[the_person.title]'s bare tits are leaking milk, a single drop hanging from each nipple."
        elif strength <= 1.0:
            "[the_person.title]'s naked tits drip milk, a drop every couple of seconds."
        elif strength <= 1.5:
            "[the_person.title]'s tits are leaking faster now. With every move a couple of drops escape from her nipples." #Triggers at 100% arousal w/ 1 lactation source, 50% arousal w/ 2 sources or max sized tits.
        elif strength <= 2.0:
            "[the_person.title] has a steady trickle of milk running from her nipples and over her breasts."
        elif strength <= 3.0:
            "[the_person.title]'s tits are producing a steady stream of breast milk, which gets flung around in fat drops every time she moves."
        elif strength <= 4.0: #This is 100% arousal w/ big tits and 1 source, or the result of 2+ sources
            "Breast milk squirts out of [the_person.title]'s tits, provoked only by her own arousal."
        elif strength <= 6.0: #This is 100% arousal w/ hucow modification
            "Breast milk jets out of [the_person.title]'s nipples. It sprays out in an arc, pulsing farther with every jolt of pleasure."
        elif strength <= 7.5:
            "[the_person.title]'s tits continue to pulse out hot breast milk, unprovoked by anything other than her own arousal."
        else:
            "[the_person.title]'s tits are producing a heavy spray of milk, making a wet mess of her chest and anything within two feet that she points herself at."


    elif (the_person.outfit.wearing_bra() and not the_person.outfit.bra_covered()) or not the_person.outfit.wearing_bra():
        $ the_clothing = the_person.outfit.get_upper_top_layer()
        if strength <= 0.5:
            pass #Not a noticeable effect, do nothing
        elif strength <= 1.5:
            "[the_person.title]'s nipples must be dripping milk, because there are two wet spots on her [the_clothing.display_name] forming around them."
        elif strength <= 3.0:
            "[the_person.title]'s lactating tits have soaked through her [the_clothing.display_name], leaving large wet spots around her nipples."
        elif strength <= 7.5:
            "[the_person.title]'s milky tits have completely soaked her [the_clothing.display_name] now. Warm milk drips off away from the edges in a steady stream."
        else:
            "[the_person.title]'s tits are squirting milk so hard that it's spraying right through her [the_clothing.display_name]. Little arcs of the warm liquid sail out almost two inches from her chest."


    else:
        $ the_clothing = the_person.outfit.get_upper_top_layer()
        if strength <= 2.0:
            pass #Not a noticeable effect under all of her clothing.
        elif strength <= 4.0:
            "[the_person.title]'s nipples must be dripping milk, because there are two wet spots on her [the_clothing.display_name] forming around them."
        elif strength <= 7.5:
            "[the_person.title]'s lactating tits have soaked through her [the_clothing.display_name], leaving large wet spots around her nipples."
        else:
            "[the_person.title]'s milky tits have completely soaked her [the_clothing.display_name] now. Warm milk drips off away from the edges in a steady stream."
    return
