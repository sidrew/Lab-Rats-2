## Holds definitions for limited time events/crises.
# These are a special class of event used for random events in the on_talk or on_enter list of a girl.
# If an action has a valid requirment it can be assigned to a person in the matching list, and after n number of turns it will be removed, or removed when it's triggered.

###################################
# Limited time events that exist: #
###################################

#######################
### On_talk events: ###
#######################
# Ask for a title change/mc title change

########################
### On_enter events: ###
#######################
# Walk in on sister masturbating
# Walk in on mother masturbating
# Night time walk-in
# Mom Nude Housework
# Breeding Mom
# Mom work report

init -2 python:
    limited_time_event_pool = [] #Drawn from to form the on_talk and on_enter events generated for people. Given in the form [event, weight, class], where class is "on_talk" or "on_enter"

init -1 python:
    # Definitions for the events
    def work_spank_opportunity_requirement(the_person):
        if not the_person.has_role(employee_role):
            return False
        elif not person_at_work(the_person):
            return False
        else:
            return True

    def ask_new_title_requirement(the_person):
        if the_person.obedience > 130: #If she has higher obedience she ONLY lets you change her title.
            return False
        # no available titles for event
        if __builtin__.len(get_titles(the_person)) <= 1 and __builtin__.len(get_player_titles(the_person)) <= 1:
            return False
        return True

    def new_insta_account_requirement(the_person):
        if the_person.has_role(mother_role) or the_person.has_role(sister_role):
            return False #We want explicit control of when these characters generate their Insta accounts
        elif the_person.has_role(instapic_role):
            return False #Role exists
        elif the_person.effective_sluttiness() < (100 - the_person.personality.insta_chance) - 5 * the_person.get_opinion_score("showing her tits") - 5 * the_person.get_opinion_score("showing her ass"):
            return False #Personality type and Opinions has a large impact on chance to generate a new profile.
        elif the_person.love < 15: #Girls who don't like you won't tell you they've made a profile (and are assumed to either have one or not depending on their starting generation)
            return False
        return True

    def new_dikdok_account_requirement(the_person):
        if the_person.has_role(mother_role) or the_person.has_role(sister_role):
            return False #We want explicit control of when these characters generate their DikDok accounts
        elif the_person.has_role(dikdok_role):
            return False #Role exists
        elif the_person.effective_sluttiness() < (100 - the_person.personality.dikdok_chance) - 5 * the_person.get_opinion_score("showing her tits") - 5 * the_person.get_opinion_score("showing her ass"):
            return False #Personality type and Opinions has a large impact on chance to generate a new profile.
        elif the_person.love < 15: #Girls who don't like you won't tell you they've made a profile (and are assumed to either have one or not depending on their starting generation)
            return False
        return True

    def new_onlyfans_account_requirement(the_person):
        if the_person.has_role(mother_role) or the_person.has_role(sister_role):
            return False #We want explicit control of when these characters generate their OnlyFans accounts
        elif the_person.has_role(onlyfans_role) or the_person.has_role(girlfriend_role):
            return False #Role exists / she's your GF
        elif the_person.effective_sluttiness() < 50 - 10 * the_person.get_opinion_score("showing her tits") - 5 * the_person.get_opinion_score("showing her ass") - 5 * the_person.get_opinion_score("public sex"):
            return False
        elif the_person.love < 30: #Girls who don't like you won't tell you they've made a profile (and are assumed to either have one or not depending on their starting generation)
            return False
        return True


    ### ON TALK EVENTS ###
    ask_new_title_action = Action("Ask new title", ask_new_title_requirement, "ask_new_title_label", event_duration = 2)
    work_walk_in = Action("Employee walk in", work_walk_in_requirement, "work_walk_in_label", event_duration = 4)
    work_spank_opportunity = Action("Employee spank opportunity", work_spank_opportunity_requirement, "work_spank_opportunity", event_duration = 2)


    new_insta_account_action = Action("Make New Insta", new_insta_account_requirement, "new_insta_account", event_duration = 4)
    new_dikdok_account_action = Action("Make New Dikdok", new_dikdok_account_requirement, "new_dikdok_account", event_duration = 4)
    new_onlyfans_account_action = Action("Make New Onlyfans", new_onlyfans_account_requirement, "new_onlyfans_account", event_duration = 4)

    limited_time_event_pool.append([ask_new_title_action,8,"on_talk"])
    limited_time_event_pool.append([work_walk_in,4,"on_talk"])
    limited_time_event_pool.append([new_insta_account_action,4, "on_talk"])
    limited_time_event_pool.append([new_dikdok_account_action,2, "on_talk"])
    limited_time_event_pool.append([new_onlyfans_account_action,1, "on_talk"])

    limited_time_event_pool.append([work_spank_opportunity,2, "on_enter"])

    #TODO: Add some girlfriend/paramour events where they ask right away if you want to fuck

    ### ON ENTER EVENTS ###


label ask_new_title_label(the_person):
    if renpy.random.randint(0,100) < 50:
        call person_new_title(the_person) from _call_person_new_title
    else:
        call person_new_mc_title(the_person) from _call_person_new_mc_title

    call talk_person(the_person) from _call_talk_person_10
    return

label work_walk_in_label(the_person): #Walk into the room and find someone masturbating (or maybe on talk instead?)
    #TODO: Include some references to masturbating opinion
    $ the_person.change_arousal(50, add_to_log = False)
    $ the_person.change_energy(-25, add_to_log = False)
    $ the_person.draw_person(position = "sitting")
    "You approach [the_person.title] from behind while she is sitting at her desk."
    if the_person.effective_sluttiness() < 40: #She was masturbating, but is embarrassed about it.
        mc.name "[the_person.title], I..."
        the_person "Ah!"
        "She yelps and nearly falls out of her chair. When she turns around her cheeks are flush and her breathing is quick."
        the_person "Oh my god, I... I'm... You nearly gave me a heart attack!"
        mc.name "Sorry about that, I didn't mean to startle you. Is everything alright?"
        the_person "Of course! I was just... Doing work. I was very focused on my work, and you startled me, that's all..."
        $ the_item = the_person.outfit.get_lower_top_layer()
        if the_item is None:
            "You notice [the_person.possessive_title] trying to inconspicuously wipe her hand off on her thigh as you talk."
        else:
            "You notice [the_person.possessive_title] trying to inconspicuously wipe her hand off on her [the_item.display_name] as you talk."
        $ mc.change_locked_clarity(5)
        "She crosses her legs, face turning beet red."
        the_person "Is there... something you wanted to talk to me about, [the_person.mc_title]?"
        menu:
            "Let it go":
                "You shrug and ignore whatever [the_person.title] is trying to hide."


            "Demand to know what she was doing" if the_person.obedience >= 120:
                mc.name "There is, now. What were you just doing [the_person.title]?"
                the_person "I... I told you, I was working."
                "She shuffles nervously in her chair."
                mc.name "No you weren't. I already know what you were doing, I just don't like you lying to me."
                #TODO: Have other girls in the room chime in.
                $ mc.change_locked_clarity(10)
                the_person "I... was... touching myself. I'm sorry, I know I should have waited until I was at home."
                "Once [the_person.possessive_title] has started talking she begins to speed up, babbling out excuses."
                the_person "And I absolutely shouldn't have been doing it at my desk. I'm sorry, it won't happen again."
                menu:
                    "Praise her":
                        "You wave your hand and smile."
                        mc.name "Calm down, you haven't done anything wrong."
                        the_person "I haven't? I mean, I was just..."
                        mc.name "Let me explain. What were you doing before you started to masturbate?"
                        the_person "Well, I was reading through a report about our products and..."
                        mc.name "Have you finished reading that report?"
                        "She shakes her head."
                        the_person "No, I'm sorry [the_person.mc_title]. I was distracted by some of the effect descriptions."
                        mc.name "Exactly. You were distracted and you weren't getting any work done, so you did what you could to remove the distraction."
                        the_person "I guess you could say that..."
                        mc.name "I need my employees focused, so if you feel \"distracted\" again I expect you to solve the problem."
                        "She's still blushing, but nods obediently."
                        $ the_person.change_slut(1 + the_person.get_opinion_score("masturbating"), 35)
                        $ the_person.discover_opinion("masturbating")
                        the_person "Okay [the_person.mc_title], I will. Is there anything else you wanted to talk about?"

                    "Scold her":
                        mc.name "Frankly, this just isn't acceptable [the_person.title]."
                        the_person "I know, I'm so sorry. I promise my... urges will never get in the way of work again."
                        mc.name "You're a grown woman, and I expect you to act like it. Not like a horny teenager, fingering herself at her own desk."
                        "[the_person.title] looks down at her lap in shame."
                        the_person "I'm sorry..."
                        mc.name "Look at me."
                        "She jerks her head up to look you in the eye."
                        mc.name "Tell me what you're sorry for."
                        $ mc.change_locked_clarity(5)
                        the_person "I'm... I'm sorry for touching myself..."
                        "You hold up your hand and correct her."
                        mc.name "\"For fingering your pussy.\""
                        $ mc.change_locked_clarity(5)
                        the_person "...For fingering my pussy at work."
                        mc.name "What were you acting like?"
                        "She clearly wants to look away, look anywhere but into your eyes, but her obedience holds her in place."
                        $ mc.change_locked_clarity(5)
                        the_person "...A horny highschool slut, [the_person.mc_title]."
                        mc.name "I expect you to shape up, or I'm going to have to start treating you like one."
                        $ the_person.change_obedience(2)
                        $ the_person.change_slut(1 + the_person.get_opinion_score("being submissive"), 35)
                        if office_punishment.is_active():
                            menu:
                                "Punish her for her inappropriate behaviour":
                                    mc.name "Of course, this will also be going on your record. There may be further punishment for this inappropriate behaviour."
                                    $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())

                                "Let it go":
                                    pass

                        else:
                            "[the_person.possessive_title] nods silently."
                        the_person "Did... you want to talk about anything else?"

            "Demand to know what she was doing\n{color=#ff0000}{size=18}Requires: 120 Obedience{/size}{/color} (disabled)" if the_person.obedience < 120:
                pass

        call talk_person(the_person) from _call_talk_person_15


    elif the_person.effective_sluttiness() < 60: #She was masturbating and admits it
        the_person "Mmph..."
        "You're about to say something when you hear her moan softly, obviously trying to stifle the sound."
        $ top_item = the_person.outfit.get_lower_top_layer()
        $ mc.change_locked_clarity(10)
        if top_item:
            "You take a quiet step closer. She has one hand between her legs and underneath her [top_item.display_name], subtly rubbing her crotch."
        else:
            "You take a quiet step closer. She has one hand between her legs, subtly rubbing her crotch."

        menu:
            "Interrupt her":
                mc.name "Having a good time [the_person.title]?"
                "[the_person.possessive_title] yelps and nearly falls out of her chair."
                the_person "Ah! Oh my god, [the_person.mc_title], I nearly had a heart attack!"
                mc.name "Sorry about that. I hope I wasn't interrupting anything."
                $ the_item = the_person.outfit.get_lower_top_layer()
                $ mc.change_locked_clarity(10)
                if the_item:
                    "[the_person.possessive_title] swivels her chair around to face you, wiping her hand off onto her thigh."
                else:
                    "[the_person.possessive_title] swivels her chair around to face you, wiping her hand off onto her [the_item.display_name]."
                $ the_person.change_slut(1 + the_person.get_opinion_score("masturbating"), 40)
                the_person "I, was just... relieving some tension. Have you read some of our product reports?"
                the_person "They really got my motor running and I couldn't focus."
                "She shrugs."
                the_person "I think that scare you gave me has killed the mood though, so that problem is solved."
                the_person "Did you need to talk to me about something?"


            "Just watch":
                "You stop a few steps behind [the_person.title]'s chair, watching and listening as she touches herself."
                the_person "Mmm... Ah..."
                $ mc.change_locked_clarity(10)
                "She slouches down into her chair, spreading her legs wider."
                the_person "Ah... Keep it quiet... Ah..."
                if top_item:
                    "Her breathing is getting louder, and you can now hear the faint wet sounds as she fingers her pussy underneath her [top_item.display_name]."
                else:
                    "Her breathing is getting louder, and you can now hear the faint wet sounds as she fingers her pussy."
                "Her pace quickens, and she pushes herself over the edge."
                $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                the_person "Ah! Ah... Ah..."
                $ the_person.run_orgasm(fire_event = False)
                $ mc.change_locked_clarity(10)
                "[the_person.possessive_title] slumps in her chair, panting quietly. After taking a moment to recover she sits up and glances around."
                $ the_person.draw_person(position = "sitting")
                "She freezes when she sees you, standing just behind her."
                the_person "... I... Hello [the_person.mc_title]. How... How long were you standing there?"
                mc.name "The whole time."
                $ the_person.discover_opinion("public sex")

                if the_person.get_opinion_score("public sex") < 0: #She's mortified
                    the_person "Oh my god, I... I'm sorry [the_person.mc_title]! I just..."
                    the_person "I didn't think anyone would notice, and I was getting so distracted."
                    mc.name "Take a breath, it's fine. If I was angry I wouldn't have just watched."
                    "Her cheeks have turned beet red. She looks away from you and nods."
                    the_person "It'll never happen again. Sorry."
                    the_person "Is there something you wanted to talk about, or can I go find someplace quiet to die of embarrassment?"
                elif the_person.get_opinion_score("public sex") == 0: #Normal
                    the_person "Right... Well, I guess you can count that as my lunch break."
                    the_person "I was reading some of our case studies. They get very... descriptive."
                    the_person "I couldn't focus, so I thought I would just... you know."
                    mc.name "Finger yourself in the middle of my office."
                    the_person "Well... Yeah, basically. I think it's worked, I feel like I can focus again."
                    the_person "Is there something you wanted to talk about?"
                else: #Turned on
                    the_person "The whole time? You were watching me while I... I..."
                    $ the_person.change_arousal(15 * the_person.get_opinion_score("public sex"))
                    "She moans, instinctively biting her lower lip."
                    the_person "Fuck... I just took care of this..."
                    $ mc.change_locked_clarity(5)
                    the_person "Did you need to talk about something? I might... I might need to go for another round before I can focus on work again."

                $ the_person.change_slut(1 + the_person.get_opinion_score("public sex"), 50)

        if office_punishment.is_active():
            menu:
                "Punish her for her inappropriate behaviour.":
                    mc.name "That was completely inappropriate for the office. I'm going to have to mark this down on your record."
                    the_person "I... Come on [the_person.mc_title], can't you let this one go?"
                    mc.name "I wish I could, but the rules are the rules. Everyone has to follow them."
                    $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())
                    "She sighs, but nods her understanding."

                "Let it go.":
                    pass

        else:
            pass
        the_person "Did... you want to talk about anything else?"
        $ top_item = None

        call talk_person(the_person) from _call_talk_person_16

    else: #She was masturbating, and she doesn't want to stop.
        the_person "Ah... Ah... Mmph..."
        "You hear her panting softly under her breath."
        $ the_item = the_person.outfit.get_lower_top_layer()
        $ mc.change_locked_clarity(10)
        if the_item:
            "You take another step closer and you can see that she has her legs spread wide, one hand underneath her [the_item.display_name] fingering her cunt."
        else:
            "You take another step closer and you can see that she has her legs spread wide, one hand between them fingering her cunt."

        "She must have heard you approaching, because she spins her chair around to face you."
        $ the_person.change_arousal(40, add_to_log = False) #ie. she starts very horny
        the_person "[the_person.mc_title], I'm... I just need a moment. I'm sorry, I just really need to cum!"
        $ mc.change_locked_clarity(10)
        "She doesn't stop playing with herself."
        menu:
            "Let her finish":
                mc.name "Well, hurry up then."
                if the_person.get_opinion_score("public sex") < 0:
                    the_person "I... With you right here?"
                    mc.name "You were already touching yourself in the middle of the day, in my office."
                    mc.name "If you can do that, you can cum in front of me."
                    "She nods."
                    the_person "I... I'll do my best..."
                    if office_punishment.is_active():
                        menu:
                            "Punish her for her inappropriate behaviour":
                                mc.name "This will go on your record, obviously. I may have to punish you for your inappropriate behaviour."
                                the_person "I... Ah, understand [the_person.mc_title], but I really need this! I'll accept whatever punishment you give me!"
                                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())

                            "Let it go":
                                pass

                    else:
                        pass
                    $ mc.change_locked_clarity(10)
                    "She rubs her pussy some more, trying to bring herself to orgasm. She turns her head to the side to avoid making eye contact."
                    "After a few minutes of her moaning quietly to herself she looks back at you and shakes her head."
                    the_person "I don't... I don't know if I can finish with you watching like this..."
                    menu:
                        "Make her cum":
                            mc.name "If you can't make yourself cum, I'll have to do it for you."
                            the_person "No, I can... I'll feel fine in a little bit, I..."
                            mc.name "I can't have you distracted all day just because you never learned how to get yourself off."
                            the_person "I know how to, I just don't like being watched..."
                            mc.name "I have no such issues. Leave it to me."
                            $ the_person.add_situational_obedience("event", 20, "He promised to make me cum, I'll do what he tells me to do.")
                            call fuck_person(the_person, private = False) from _call_fuck_person_90
                            $ the_person.clear_situational_obedience("event")
                            $ the_report = _return
                            if the_report.get("girl orgasms", 0) > 0:
                                $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                                "[the_person.possessive_title] collapses back into her chair and sighs happily."
                                mc.name "There, are you going to be able to focus now?"
                                "She nods obediently."
                                $ the_person.change_obedience(3 + the_person.get_opinion_score("being submissive"))
                                the_person "Yes [the_person.mc_title], thank you. What do you want to talk about?"
                            else:
                                $ the_person.draw_person(position = "sitting")
                                "[the_person.possessive_title] sits back down in her chair."
                                the_person "I told you, it just wasn't going to work..."
                                the_person "I'll be fine. What did you want to talk about?"

                        "Make her stop":
                            mc.name "Then wait until later. I'm here to talk to you, not watch you practice masturbating."
                            "She pulls her hand out of her pussy and sits up, blushing."
                            $ the_person.change_obedience(1)
                            the_person "Right. Sorry [the_person.mc_title]. What did you want to talk about?"

                elif the_person.get_opinion_score("public sex") > 0:
                    "She moans and pants as she masturbates, legs still wide for you to watch."
                    if office_punishment.is_active():
                        menu:
                            "Punish her for her inappropriate behaviour":
                                mc.name "This will go on your record, obviously. I may have to punish you for your inappropriate behaviour."
                                the_person "I... Ah, understand [the_person.mc_title], but I really need this! I'll accept whatever punishment you give me!"
                                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())

                            "Let it go":
                                pass

                    else:
                        pass
                    the_person "Do you like... watching me, [the_person.mc_title]?"
                    the_person "Is watching me finger myself making your dick hard? Thinking about is making me so wet!"
                    $ mc.change_locked_clarity(10)
                    "She moans again, arching her back and lifting her hips away from her office chair. There's a large wet spot left where she used to be sitting."
                    $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                    the_person "Fuck... Watch me cum [the_person.mc_title]! I'm cumming!"
                    $ mc.change_locked_clarity(10)
                    $ the_person.run_orgasm()
                    "[the_person.title]'s whole body quivers, her hips thrusting out with each pulse of her climax."
                    "She holds perfectly still for a moment, back still arched, as her pussy spasms a few last times."
                    "Then she collapses down into her chair, panting loudly."
                    the_person "I... I'm going to need a minute. I... Oh my god..."
                    $ the_person.draw_person(position = "sitting")
                    "You wait patiently until [the_person.title] is able to pull herself up in her chair and look you in the eyes."
                    mc.name "Better?"
                    "She nods, almost meekly now."
                    the_person "Much, I didn't realise how badly I needed that."
                    the_person "Now, what did you want to talk about?"
                    $ the_person.change_slut(2 + the_person.get_opinion_score("public sex"), 80)

                else:
                    the_person "Gladly! Ah!"
                    $ mc.change_locked_clarity(10)
                    "[the_person.possessive_title] cups a breast with one hand while she fingers herself with the other."
                    if office_punishment.is_active():
                        menu:
                            "Punish her for her inappropriate behaviour":
                                mc.name "This will go on your record, obviously. I may have to punish you for your inappropriate behaviour."
                                the_person "I... Ah, understand [the_person.mc_title], but I really need this! I'll accept whatever punishment you give me!"
                                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())

                            "Let it go":
                                pass

                    else:
                        pass
                    "She moans and pants as she stares into your eyes, right up until the moment she cums."
                    "Her breath catches in her throat and she closes her eyes as she begins to climax."
                    $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                    the_person "Oh... Oh god..."
                    $ mc.change_locked_clarity(10)
                    "She arches her back, lifting her hips away from her office chair where she has left a noticeable wet spot."
                    the_person "Ahh!"
                    $ the_person.run_orgasm()
                    "Her body quivers for a moment, then she slumps back into her chair and pants."
                    the_person "Sorry... about the wait. I just... ah, couldn't stop thinking about sex."
                    mc.name "Feeling better now?"
                    $ the_person.change_slut(1, 50)
                    "She takes a deep breath and nods, pulling herself up to sit properly in her chair."
                    the_person "I think so [the_person.mc_title]. Did you need to talk to me?"

                $ the_person.discover_opinion("public sex")


            "Demand she stops":
                mc.name "I don't have a moment. Cut it out, I need to talk to you."
                if the_person.obedience - 100 > ((the_person.arousal/2) + 10*the_person.get_opinion_score("public sex") + 10*the_person.get_opinion_score("masturbating")):
                    "[the_person.possessive_title] seems disappointed, but she puts her legs together and sits up straight in her chair."
                    $ mc.change_locked_clarity(5)
                    "She continues to rub her thighs together in an attempt to stimulate herself while you talk."
                    if office_punishment.is_active():
                        menu:
                            "Punish her for her inappropriate behaviour":
                                mc.name "This will still be going on your record, of course."
                                the_person "It was just for a moment though [the_person.mc_title]... Can't I get away with it this one time?"
                                "You shake your head."
                                mc.name "If I start making exceptions every girl in this office will be fucking herself at her desk when they should be working."
                                "[the_person.title] sighs, but nods her understanding."
                                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())

                            "Let it go":
                                pass
                    else:
                        pass
                else: #She ignores you
                    "She pants and shakes her head, refusing to stop."
                    if the_person.get_opinion_score("public sex") > 0:
                        $ the_person.discover_opinion("public sex")
                        $ mc.change_locked_clarity(10)
                        the_person "I can't stop, not with you watching me!"
                        "She rubs herself faster, legs spread wide for you to watch."
                        the_person "Watch me cum [the_person.mc_title]! I'm cumming!"
                    elif the_person.get_opinion_score("masturbating") > 0:
                        $ the_person.discover_opinion("masturbating")
                        $ mc.change_locked_clarity(10)
                        the_person "I can't stop, touching myself just feels too good!"
                        "She rubs herself faster, pumping her fingers in and out of her dripping wet pussy."
                    else:
                        $ mc.change_locked_clarity(10)
                        the_person "I'm so, so close! Just... Wait, okay?"
                        "She leans back and continues to finger herself."

                    $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                    the_person "Oh... Oh god..."
                    $ mc.change_locked_clarity(10)
                    "She arches her back, lifting her hips away from her office chair where she has left a noticeable wet spot."
                    the_person "Ahh!"
                    $ the_person.run_orgasm()
                    "Her body quivers for a moment, then she slumps back into her chair and pants."
                    if office_punishment.is_active():
                        menu:
                            "Punish her for disobedience":
                                mc.name "I hope that was worth it, because I'm going to have to write you up for disobedience now."
                                "She sighs and shrugs."
                                the_person "It was worth it, that felt so good..."
                                $ the_person.add_infraction(Infraction.disobedience_factory())

                            "Let it go":
                                pass

                    $ the_person.change_slut(2 + the_person.get_opinion_score("masturbating") + the_person.discover_opinion("public sex"), 80)
                    $ the_person.change_obedience(-2)
                    the_person "Now, what did you need to talk about?"

            "Offer to help":
                mc.name "Let's speed things up. I'll give you a hand."
                "She eyes you up and down as she considers, before nodding her approval."
                $ the_person.add_situational_obedience("event", 10, "He promised to make me cum, I'll do what he tells me to do.")
                call fuck_person(the_person, private = False) from _call_fuck_person_91
                $ the_report = _return
                $ the_person.clear_situational_obedience("event")
                if the_report.get("girl orgasms", 0) > 0:
                    $ the_person.draw_person(position = "sitting", emotion = "orgasm")
                    "[the_person.possessive_title] collapses back into her chair and sighs happily."
                    mc.name "There, are you going to be able to focus now?"
                    "She nods obediently."
                    $ the_person.change_obedience(3 + the_person.get_opinion_score("being submissive"))
                    the_person "Yes [the_person.mc_title], thank you. What do you want to talk about?"
                else:
                    $ the_person.draw_person(position = "sitting")
                    "[the_person.possessive_title] sits back down in her chair."
                    the_person "I think... you've just made things worse."
                    $ mc.business.change_team_effectiveness(-5)
                    the_person "I'll have to deal with this later. What did you want to talk about [the_person.mc_title]?"
        call talk_person(the_person) from _call_talk_person_17
    $ clear_scene()
    return

label new_insta_account(the_person):
    if not the_person.has_role(instapic_role):
        the_person "Hey [the_person.mc_title]! Oh, you'll probably be interested in this."
        the_person "I've started an InstaPic account, you should follow me! I'm just starting out, but I think I'm figuring it all out!"
        $ the_person.event_triggers_dict["insta_known"] = True
        $ the_person.add_role(instapic_role)
        $ mc.phone.register_number(the_person)
    call talk_person(the_person) from _call_talk_person_27
    return

label new_dikdok_account(the_person):
    if not the_person.has_role(dikdok_role):
        the_person "Hey [the_person.mc_title]! Oh, you'll probably be interested in this. I've started a DikDok channel."
        the_person "You should follow me! I'm just starting out but I think my videos are pretty great."
        $ the_person.event_triggers_dict["dikdok_known"] = True
        $ the_person.add_role(dikdok_role)
        $ mc.phone.register_number(the_person)
    call talk_person(the_person) from _call_talk_person_28
    return

label new_onlyfans_account(the_person):
    if not the_person.has_role(onlyfans_role):
        the_person "Hey [the_person.mc_title], I thought you might want to know..."
        the_person "I'm starting up an OnlyFanatics account. I think it might be a fun way for me to make a little extra money."
        the_person "You should check me out some time, if you don't think that would be too weird."
        $ the_person.event_triggers_dict["onlyfans_known"] = True
        $ the_person.add_role(onlyfans_role)
        $ mc.phone.register_number(the_person)
    call talk_person(the_person) from _call_talk_person_29
    return

label work_spank_opportunity(the_person):
    $ the_person.draw_person(position = "standing_doggy")
    "When you walk in you see [the_person.possessive_title], leaning over a desk and staring at paperworking."
    if the_person.outfit.vagina_visible():
        $ mc.change_locked_clarity(20)
        "She swings her hips idley, unintentionally shaking her bare ass at you."
    elif not the_person.outfit.panties_covered():
        $ mc.change_locked_clarity(10)
        "She swings her hips idley, shaking her barely-covered ass right at you."
    else:
        "She swings her hips idley, shaking her ass in your direction."

    menu:
        "Slap her ass":
            "You step close and slap your hand across her ass."
            $ mc.change_locked_clarity(20)
            if the_person.outfit.vagina_visible():
                "There's a loud smack as you make contact with her bare ass."
            elif not the_person.outfit.panties_covered():
                "There's a loud smack as you make contact with her tight ass."
            else:
                "There's a muffled smack as you make contact with her covered butt."

            if the_person.effective_sluttiness() + 5*the_person.get_opinion_score("being submissive") < 20 and not the_person.has_role(employee_freeuse_role):
                the_person "Oh my god!"
                $ the_person.draw_person(emotion = "angry")
                "She snaps straight up and spins around, glaring at you."
                $ the_person.change_love(-2)
                $ the_person.change_happiness(-10)
                the_person "What the hell was that?"
                mc.name "I was just saying hi. It looked like you wanted it."
                the_person "Clearly I don't."
                "You hold your hands up innocently. She shakes her head and turns away from you."
            elif the_person.effective_sluttiness() + 5*the_person.get_opinion_score("being submissive") < 40:
                the_person "Oh!"
                $ the_person.draw_person()
                "She snaps to attention, grabbing her bottom as she turns to face you."
                the_person "Oh, it's you [the_person.mc_title]."
                mc.name "Expecting someone else?"
                the_person "No, just... You startled me, is all."
                $ the_person.change_obedience(1)
                $ the_person.change_slut(1, 40)
            else:
                the_person "Mmmph..."
                "She glances over her shoulder at you. She keeps her ass pointed in your direction."
                the_person "Hello [the_person.mc_title]. Am I not working hard enough?"
                $ mc.change_locked_clarity(10)
                menu:
                    "You're doing fine.":
                        "You rest your hand on her butt, squeezing it gently."
                        mc.name "You're doing fine. Pretend I'm not even here."
                        the_person "You're making that a little hard... ah..."
                        mc.name "The feeling's mutual."

                    "No, you're not.":
                        "You smack her ass again. She gasps, more for effect than actual surprise."
                        mc.name "No, you're not. Now get back to it."
                        the_person "Right away [the_person.mc_title]!"

                "You step back and let [the_person.title] focus on her work."



        "Grope her pussy" if the_person.outfit.vagina_available():
            $ mc.change_locked_clarity(15)
            "You reach between [the_person.possessive_title]'s legs and press two fingers up against her pussy."
            if the_person.arousal > 50:
                $ mc.change_locked_clarity(20)
                "You're surprised to find that she's already wet."

            if the_person.effective_sluttiness() + 5*the_person.get_opinion_score("being fingered") < 20 and not the_person.has_role(employee_freeuse_role):
                the_person "Oh my god!"
                $ the_person.draw_person(emotion = "angry")
                "She snaps straight up and spins around, glaring at you."
                $ the_person.change_slut(the_person.get_opinion_score("being fingered"))
                $ the_person.change_love(-2 +the_person.get_opinion_score("being fingered"))
                $ the_person.change_happiness(-10)
                the_person "What the hell was that?"
                mc.name "I was just saying hi. It looked like you wanted it."
                the_person "Clearly I don't."
                "You hold your hands up innocently. She shakes her head and turns away from you."
            elif the_person.effective_sluttiness() + 5*the_person.get_opinion_score("being fingered") < 40:
                the_person "What the..."
                "She tries to stand up, but your hand between her legs stops her progress. You stroke the lips of her pussy slowly."
                mc.name "Hey [the_person.title]. Work going well?"
                the_person "You're making it... Mph.... hard to focus right now."
                "You slide a finger inside of her. She gasps and jumps, slamming her hips into the desk."
                the_person "[the_person.mc_title]!"
                mc.name "Sorry, it just looked very inviting."
                the_person "Well you should... ah... give a girl some warning!"
                $ the_person.break_taboo("touching_vagina")
                "You give her pussy a few more strokes, then pull out and wipe your fingers on her thigh."
                mc.name "You've got work to do. Maybe we can pick this up later."
                $ the_person.change_slut(the_person.get_opinion_score("being fingered"))
                $ the_person.change_arousal(20+ 20*the_person.get_opinion_score("being fingered"))
                "She nods, face suddenly flush and her breathing heavy."
            else:
                the_person "Oh... Hello [the_person.mc_title]..."
                $ mc.change_locked_clarity(30)
                "She sighs and lowers her shoulders to the desk, instinctively pressing her hips back against your hand."
                mc.name "Just checking in, making sure everything is going well..."
                the_person "It's... all very good..."
                $ the_person.break_taboo("touching_vagina")
                "You slip two fingers into her pussy. She sighs again and starts to move her hips with you."
                the_person "But I think... I need a break... Have I earned a break [the_person.mc_title]?"
                menu:
                    "Keep fingering her":
                        mc.name "I think you have. Here let me help you..."
                        $ the_person.change_arousal(10+10*the_person.get_opinion_score("being fingered"))
                        call fuck_person(the_person, start_position = standing_finger, skip_intro = True)
                        $ the_report = _return
                        $ the_person.call_dialogue("sex_review", the_report = the_report)

                    "Finish up":
                        "You slide your fingers back out and wipe them off on her thigh."
                        mc.name "Sorry, but I've got work to get done. So do you."
                        $ the_person.change_arousal(20+20*the_person.get_opinion_score("being fingered"))
                        "She moans, a little more desperately than she might have intended, and stands up."
                        $ the_person.draw_person()
                        the_person "Right, right..."

        "Enjoy the view":
            "You stop and stare for a little bit."
            $ mc.change_locked_clarity(10)
            "After a few moments [the_person.title] stands up and turns around."
            if the_person.effective_sluttiness() + 5*the_person.get_opinion_score("showing her ass") < 15:
                "She blushes, clearly aware that you've been there for a while."
                $ the_person.change_slut(1)
                $ the_person.change_love(-1)
                the_person "Oh, hey [the_person.mc_title]... Can I help you?"
                mc.name "Just passing by."
            elif the_person.effective_sluttiness() + 5*the_person.get_opinion_score("showing her ass") < 40:
                "She smiles at you. You aren't sure if she doesn't know you were staring at her, or if she just doesn't care."
                the_person "Hi [the_person.mc_title]. Need anything?"
                mc.name "Just passing by."
            else:
                the_person "Oh hi [the_person.mc_title]. I'm sorry, were you looking at something?"
                $ mc.change_locked_clarity(10)
                $ the_person.draw_person(position = "back_peek")
                "She turns around again, emphasizing her ass for you."
                mc.name "I was, actually, but I have work to do."
                the_person "Stop by any time."

        "Move along":
            "You pull your eyes off of the pleasant sight and move along."

    $ clear_scene()
    return
