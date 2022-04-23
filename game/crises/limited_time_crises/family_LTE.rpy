init -1 python:
    def sister_walk_in_requirement(the_person):
        if not the_person.has_role(sister_role):
            return False
        elif the_person not in the_person.home.people:
            return False
        elif the_person.energy < 40:
            return False
        elif lily_bedroom.get_person_count() > 1:
            return False
        return True

    def nude_walk_in_requirement(the_person):
        if not (the_person.has_role(sister_role) or the_person.has_role(mother_role)):
            return False
        elif the_person not in the_person.home.people:
            return False
        elif the_person.home.get_person_count() > 1:
            return False
        return True

    def mom_house_work_nude_requirement(the_person):
        if not the_person.has_role(mother_role):
            return False
        elif the_person not in kitchen.people:
            return False
        elif the_person.effective_sluttiness() < (20 - the_person.get_opinion_score("not wearing anything")*3): #TODO: OR require her to work nude as one of your weekly requests
            return False
        return True

    def mom_breeding_intro_requirement(the_person):
        if not the_person.has_role(mother_role):
            return False
        elif persistent.pregnancy_pref == 0:
            return False
        elif the_person not in mom_bedroom.people:
            return False
        elif mom_bedroom.get_person_count() > 1:
            return False
        elif the_person.effective_sluttiness() + the_person.fertility_percent < (80 - (10*the_person.get_opinion_score("creampies"))):
            return False
        elif the_person.love + the_person.fertility_percent < (75 - (10*the_person.get_opinion_score("creampies"))):
            return False
        elif the_person.get_opinion_score("creampies") < 0 or the_person.get_opinion_score("bareback sex") < 0:
            return False
        elif the_person.has_role(breeder_role):
            return False
        elif the_person.on_birth_control:   # when she's taking BC she won't ask for breeding her
            return False
        elif the_person.has_role(pregnant_role) and the_person.event_triggers_dict.get("preg_knows", False):
            return False
        return True

    def work_walk_in_requirement(the_person): #AKA she has to work for you, be at work, and be turned on
        if not the_person.has_role(employee_role):
            return False
        elif not person_at_work(the_person):
            return False
        elif the_person.energy < 40:
            return False
        elif the_person not in mc.business.get_employee_list():
            return False
        elif the_person.effective_sluttiness() < 40 - (5*the_person.get_opinion_score("masturbating")):
            return False
        elif the_person.arousal < (the_person.max_arousal * .8):
            return False
        return True

    #TODO: We really need to be able to assign LTE's to roles instead of being general events

    def mom_work_slutty_requirement(the_person):
        if not the_person.has_role(mother_role):
            return False
        elif mc.business.is_weekend():
            return False
        elif time_of_day <= 1 or time_of_day >= 4:
            return False
        elif the_person.event_triggers_dict.get("mom_office_slutty_level",0) < 1:
            return False
        return True

    def aunt_home_lingerie_requirement(the_person):
        if not the_person.has_role(aunt_role):
            return False
        elif not aunt_apartment.has_person(the_person):
            return False
        elif cousin_bedroom.has_person(cousin):
            return False
        return True

    def cousin_home_panties_requirement(the_person):
        if not the_person.has_role(cousin_role):
            return False
        elif not cousin_bedroom.has_person(the_person):
            return False
        return True

    def add_mom_outfit_coloured_apron(person):
        coloured_apron = apron.get_copy()
        coloured_apron.colour = [0.74,0.33,0.32,1.0]
        coloured_apron.pattern = "Pattern_1"
        coloured_apron.colour_pattern = [1.0,0.83,0.90,1.0]
        person.outfit.add_dress(coloured_apron)
        return

    def sister_go_shopping_requirement(the_person):
        if not the_person.has_role(sister_role):
            return False
        elif not lily_bedroom.has_person(the_person):
            return False
        elif not (time_of_day == 3):
            return False
        return True

    def mom_go_shopping_requirement(the_person):
        if not the_person.has_role(mother_role):
            return False
        elif not person_at_home(the_person):
            return False
        elif not (time_of_day == 3):
            return False
        return True

    ### ON TALK EVENTS ###
    mom_work_slutty_event = Action("Mom work slutty", mom_work_slutty_requirement, "mom_work_slutty_report", event_duration = 2)

    limited_time_event_pool.append([mom_work_slutty_event,8,"on_talk"])

    ### ON ENTER EVENTS ###
    sister_walk_in = Action("Sister walk in", sister_walk_in_requirement, "sister_walk_in_label", event_duration = 5)
    sister_go_shopping_action = Action("Sister go shopping", sister_go_shopping_requirement, "sister_go_shopping_label", event_duration = 5)

    nude_walk_in = Action("Nude walk in", nude_walk_in_requirement, "nude_walk_in_label", event_duration = 5)

    mom_house_work_nude = Action("Mom nude house work", mom_house_work_nude_requirement, "mom_house_work_nude_label", event_duration = 5)
    breeding_mom = Action("Mom breeding", mom_breeding_intro_requirement, "breeding_mom_intro_label", event_duration = 5)
    mom_go_shopping_action = Action("Mom go shopping", mom_go_shopping_requirement, "mom_go_shopping_label", event_duration = 5)


    aunt_home_lingerie = Action("Aunt home lingerie", aunt_home_lingerie_requirement, "aunt_home_lingerie_label", event_duration = 3)

    cousin_home_panties = Action("Cousin home panties", cousin_home_panties_requirement, "cousin_home_panties_label", event_duration = 3)


    limited_time_event_pool.append([sister_walk_in,4,"on_enter"])
    limited_time_event_pool.append([nude_walk_in,4,"on_enter"])
    limited_time_event_pool.append([mom_house_work_nude,4,"on_enter"])
    limited_time_event_pool.append([breeding_mom,4,"on_enter"])
    limited_time_event_pool.append([aunt_home_lingerie,4,"on_enter"])
    limited_time_event_pool.append([cousin_home_panties,4,"on_enter"])
    limited_time_event_pool.append([sister_go_shopping_action,6,"on_enter"])
    limited_time_event_pool.append([mom_go_shopping_action,4,"on_enter"])

label sister_walk_in_label(the_person):
    if the_person.effective_sluttiness() < 10:
        "You try to open the door to [the_person.title]'s room, but find it locked."
        $ the_person.change_arousal(30, add_to_log = False)
        the_person "Ah! One... One second!"
        "You hear scrambling on the other side of the door, then the lock clicks and [the_person.possessive_title] pokes her head out."
        $ the_person.draw_person()
        the_person "Oh... [the_person.mc_title], it's only you. Come on in, what's up?"
        "Her face is flush and her breathing rapid. You wonder for a moment what you almost caught her doing as she leans nonchalantly against the door frame."
        $ mc.change_locked_clarity(5)
        $ clear_scene()
        return

    elif the_person.effective_sluttiness() < 25:
        "You try to open the door to [the_person.title]'s room, but find it locked."
        $ the_person.change_arousal(40, add_to_log = False)
        the_person "Ah! One... One second!"
        "You hear scrambling on the other side of the door, then the lock clicks and [the_person.possessive_title] pokes her head out."
        $ the_person.draw_person()
        the_person "[the_person.mc_title], it's you. What's up?"
        "Her face is flush and her breathing rapid. Her attempt at being nonchalant is ruined when a loud moan comes from her laptop, sitting on her bed."
        "Laptop" "Ah! Fuck me! Ah! Yes!"
        the_person "Oh my god, no!"
        "She sprints to her bed, opening up her laptop and turning it off as quickly as possible."
        $ mc.change_locked_clarity(10)
        mc.name "Am I interrupting?"
        "[the_person.possessive_title] spins around, beet red, and stammers for a moment."
        the_person "I... I don't... Umm... I think my laptop has a virus, all these crazy popups!"
        mc.name "Mmmhm? Do you want me to take a look?"
        the_person "No, no that's okay. It's probably fine."
        menu:
            "Encourage her":
                mc.name "You know there's nothing wrong with watching porn, right?"
                the_person "I wasn't! I..."
                mc.name "Of course not, but even if you were there's nothing wrong with that. It's a natural thing, everyone does it. I certainly do."
                $ the_person.change_slut(1, 20)
                $ the_person.change_happiness(5)
                the_person "Really? Ew, I don't need to know about that."
                "She still seems more interested than her words would suggest."

            "Threaten to tell [mom.possessive_title]":
                mc.name "I can let [mom.title] know, maybe she can take it somewhere to get it fixed."
                the_person "No! I mean, you can't tell Mom. Nothing's wrong with it, okay?"
                mc.name "So you were..."
                $ the_person.change_obedience(2)
                $ the_person.change_love(-1)
                the_person "I was watching porn, okay? Can you not make such a big deal about it?"
                mc.name "You should have just told me that right away, there's nothing wrong with watching some porn and getting off."
                the_person "I wasn't getting off, I was just..."
                mc.name "Watching it for the acting?"
                the_person "Ugh, shut up. What do you need?"

    else:
        $ the_person.outfit.strip_to_vagina()
        $ the_person.draw_person(position = "missionary")
        $ the_person.change_arousal(40, add_to_log = False)
        "You open the door to [the_person.title]'s room and find her sitting up in bed with her laptop beside her, legs splayed open and fingers deep in her own pussy."
        "Her eyes are closed, and because of her headphones it doesn't seem like she's noticed you come in. She lets out the softest moan."
        $ mc.change_locked_clarity(20)
        the_person "Mmmph..."
        menu:
            "Offer to help":
                "You step into the room and close the door."
                mc.name "Having a good time?"
                if the_person.effective_sluttiness("touching_vagina") < 35:
                    the_person "Hmm? Oh my god!"
                    "She opens her eyes slowly, before yelling in surprise and grabbing desperately for her blankets in an attempt to salvage her decency."
                    the_person "Oh my god, [the_person.mc_title]! What are you... I... Get out of here!"
                    mc.name "Don't be so dramatic [the_person.title], I just want to know if you want some help."
                    the_person "Help?! Ew, oh god!"
                    "She grabs a pillow and throws it at you."
                    the_person "Get out! Get out!"
                    "You retreat from the room before [mom.title] hears what's happening and comes to investigate."

                else:
                    the_person "Hmm?"
                    if the_person.effective_sluttiness("touching_vagina") < 55 or the_person.has_taboo(["touching_vagina","bare_pussy"]):
                        "She opens her eyes slowly, then gasps in surprise. She grabs a pillow and uses it to cover herself."
                        the_person "Oh my god, [the_person.mc_title]! What are you doing, I'm..."
                        "She blushes a little."
                        the_person "Well, you know."
                        mc.name "I just wanted to know if you need a hand."
                        the_person "I... We really shouldn't..."
                        "Despite her verbal hesitations she slides the pillow out of the way and gives you \"fuck me\" eyes."
                        $ mc.change_locked_clarity(10)

                    else:
                        "She opens her eyes slowly."
                        the_person "Oh, it's you [the_person.mc_title]. What do you need? I was just relaxing a little."
                        "She rubs her pussy gently while she talks to you, stroking the wet pink slit with a finger."
                        $ mc.change_locked_clarity(20)
                        mc.name "I don't need anything, but it looks like you might. Do you need a hand with that?"
                        "She nods and gives you \"fuck me\" eyes."
                    $ the_person.update_outfit_taboos()


                    "You slide onto the bed and run your fingers along [the_person.title]'s body, moving down towards her already-wet pussy."
                    $ the_person.break_taboo("touching_vagina")
                    "When you first touch her she gasps and quivers, and when you slide your middle finger into her pussy she moans."
                    "She slides her body against you, and when you pull her off the bed she doesn't argue."
                    "You stand behind her, one hand grasping a breast and the other gently pumping a finger in and out of her."
                    call fuck_person(the_person, start_position = standing_finger, private = True) from _call_fuck_person_2
                    $ the_report = _return
                    if the_report.get("girl orgasms", 0) > 0:
                        "[the_person.possessive_title] falls back on her bed and sighs happily."
                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                        $ the_person.change_love(2)
                        $ the_person.change_obedience(1)
                        the_person "Thank you [the_person.mc_title], that's exactly what I wanted. Ahh..."
                        "She rolls over and gathers up a collection of pink blankets on top of herself, quickly falling asleep."
                        "You step out of the room to give her some time to recover."

                    elif the_report.get("guy orgasms", 0) > 0:
                        $ the_person.draw_person(position = "stand4", emotion = "angry")
                        the_person "So... Is that it?"
                        mc.name "What do you mean?"
                        $ the_person.change_love(-2)
                        $ the_person.change_obedience(-2)
                        $ the_person.draw_person(position = "missionary", emotion = "angry")
                        "She scoffs and falls back onto her bed, pulling her blankets over herself."
                        the_person "Nothing, I'm glad you enjoyed yourself at least. Get out of here so I can get off."

                    else:
                        $ the_person.draw_person(position = "stand4", emotion = "angry")
                        the_person "So... are you finished?"
                        mc.name "Heh, yeah. Sorry [the_person.title], I'm just not feeling it."
                        $ the_person.draw_person(position = "missionary", emotion = "angry")
                        "She frowns, but nods. She gathers her blankets over herself as you are walking out of her room."
                        $ the_person.change_obedience(-2)


            "Just watch":
                "You step into the room and close the door to [the_person.title]'s room."
                "You lean on the doorframe and watch her fingering herself."
                $ mc.change_arousal(5)
                the_person "Ah... Mmmm."
                "She opens her eyes and glances at her laptop, then finally notices you."
                if the_person.effective_sluttiness("bare_pussy") + (the_person.obedience - 100) < 40: #If she's not slutty or obedient she yells at you to get out
                    the_person "Oh my god, [the_person.mc_title]! What are you... I... Get out of here!"
                    mc.name "Don't be so dramatic [the_person.title], just keep going."
                    the_person "What?! Ew, how long have you been there? Oh god!"
                    "She grabs a pillow and throws it at you."
                    the_person "Get out! Get out!"
                    "You retreat from the room before [mom.title] hears what's happening and comes to investigate."

                else: #Otherwise she lets you stay long enough for you to tell her to keep going.
                    the_person "Oh my god, [the_person.mc_title]! What are you doing, I'm..."
                    "She blushes a little."
                    the_person "Well, you know."
                    mc.name "Don't worry about me, just keep going."
                    if the_person.effective_sluttiness("bare_pussy") < 60: #She's a little unsure about it, but goes for it
                        the_person "Really? I... I mean, do you really want to see me like this?"
                        "[the_person.possessive_title] relaxes a little, her hand unconsciously drifting back between her legs."
                        mc.name "I think it's hot, keep touching yourself for me."
                        "She shrugs and nods, spreading her legs and sliding a finger along her wet slit."
                        $ the_person.change_obedience(2)
                    else:
                        the_person "If you want..."
                        "She smiles and spreads her legs, sliding a finger along her wet slit."

                    $ mc.change_locked_clarity(10)
                    $ the_person.update_outfit_taboos()

                    "[the_person.possessive_title] starts to finger herself again, slowly moving a pair of fingers in and out, in and out."
                    "Soon she's almost forgotten about you standing and watching at her door. She arches her back and turns her head, moaning into a pillow."
                    "She starts to rock her hips against her own hand as her fingering becomes increasingly intense."
                    "Even as she starts to climax she keeps her legs wide open, giving you a clear view of her dripping wet cunt."
                    $ the_person.run_orgasm()
                    "Her body spasms as she cums, fingers buried deep inside of herself. She holds them there for a long moment, eyes shut tight."
                    "Finally she relaxes and pulls her fingers out, trailing her own juices behind them. She glances up at you and smiles weakly."
                    $ mc.change_locked_clarity(20)
                    the_person "Ah... That was good."
                    "You smile at her and walk out of the room."
                    $ the_person.change_slut(1+the_person.get_opinion_score("masturbating"), 50)
                    $ the_person.discover_opinion("masturbating")
                    $ the_person.reset_arousal()

            "Leave her alone":
                $ clear_scene()
                $ the_person.run_orgasm()
                "You take a quick step back and, as quietly as you can manage and close her door."



    $ mc.change_location(hall)
    $ mc.location.show_background()
    $ the_person.apply_outfit()
    $ clear_scene()
    return

label nude_walk_in_label(the_person):
    if renpy.random.randint(0,100) < 50:
        $ the_person.apply_outfit(Outfit("Nude"))
        $ mc.change_locked_clarity(15)
        $ the_person.draw_person()
        "You open the door to [the_person.possessive_title]'s room and see her standing in front of her mirror, completely nude."
        if the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) < (50 - (the_person.get_opinion_score("not wearing anything")*10)):
            # She asks you to step out for a moment.
            if the_person.has_large_tits():
                "She turns and tries to cover herself with her hands, but her big tits are still easily on display."
            else:
                "She turns and tries to cover herself with her hands."
            the_person "Just... Just a minute, I was getting changed!"
            $ clear_scene()
            "[the_person.title] shoos you out of the room. You can hear her getting dressed on the other side."
            $ the_person.apply_outfit()
            $ the_person.draw_person()
            "Soon enough she opens the door and invites you in."
            $ the_person.change_slut(1+the_person.get_opinion_score("not wearing anything"), 60)
            $ the_person.discover_opinion("not wearing anything")
            the_person "Sorry about that, I always forget to lock the door."
        else:
            # She doesn't mind and invites you in to talk, while being nude
            if the_person.update_outfit_taboos():
                "She turns around and waves you in, then seems to realise that she's naked and tries to cover herself with her hands."
                the_person "Oh, I'm not dressed! If you want I can put something on."
                mc.name "Don't worry about it. We're family, we should be comfortable around each other."
                $ mc.change_locked_clarity(10)
                "She smiles and nods, moving her hands away from her tits and pussy."
            else:
                $ mc.change_locked_clarity(10)
                "She turns to you and smiles, seemingly oblivious to her own nudity."
                the_person "Come on in! Did you need something?"



    else:
        # She's in her underwear
        $ the_person.apply_outfit(the_person.wardrobe.get_random_appropriate_underwear(the_person.effective_sluttiness(), guarantee_output = True))
        $ the_person.draw_person(position = "sitting")
        $ mc.change_locked_clarity(10)
        "You open the door to [the_person.possessive_title]'s room and find her sitting on her bed, wearing nothing but her underwear."
        if the_person.effective_sluttiness("underwear_nudity") < (30 - (the_person.get_opinion_score("not wearing anything")*10)):
            the_person "Oh! One second, I'm not dressed!"
            $ clear_scene()
            "She hurries to the door and closes it in your face, locking it quickly. You can hear her quickly getting dressed on the other side."
            $ the_person.apply_outfit()
            $ the_person.draw_person()
            "When she opens the door she's fully dressed and invites you in."
            $ the_person.change_slut(1+the_person.get_opinion_score("not wearing anything"), 40)
            $ the_person.discover_opinion("not wearing anything")
            the_person "Sorry about that, I was just relaxing and forgot the door wasn't locked."
        else:
            if the_person.update_outfit_taboos():
                "She turns around and waves you in, then seems to realise how little she is wearing."
                the_person "Oh, I'm not fully dressed! If you mind I can put something on."
                mc.name "Of course I don't mind. We're family, we can trust each other."
                "She smiles and nods."
            else:
                "She turns to you and smiles, waving a hand to invite you in."
                the_person "Come on in, do you need something?"


    call talk_person(the_person) from _call_talk_person_19
    return

label mom_house_work_nude_label(the_person):
    # When she's in the kitchen (or any other part of the house, for later events) she'll work in her underwear or (later) nude.
    $ effective_slut = the_person.effective_sluttiness("underwear_nudity") + (the_person.get_opinion_score("not wearing anything")*10)
    if effective_slut < 20: #TODO: This method of adding clothing with specific colours is dumb. (I suppose we could do the apron as being an overwear and then add it to underwear, but we should still have a system for it).
        # She's in her underwear but self conscious about it
        $ the_person.apply_outfit(the_person.wardrobe.get_random_appropriate_underwear(the_person.effective_sluttiness(), guarantee_output = True))
        $ add_mom_outfit_coloured_apron(the_person)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen working on dinner. She glances over her shoulder when you enter, seeming meek."
        the_person "Hi [the_person.mc_title]. I hope you don't mind the way I'm dressed, it's nice to wear something more comfortable after I come home from work."
        $ mc.change_locked_clarity(5)
        mc.name "It's fine, I don't mind."
        "She turns her attention back to preparing dinner."

    elif the_person.effective_sluttiness("underwear_nudity") < 40:
        $ the_person.apply_outfit(the_person.wardrobe.get_random_appropriate_underwear(the_person.effective_sluttiness(), guarantee_output = True))
        $ add_mom_outfit_coloured_apron(the_person)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen working on dinner in her underwear. She glances over her shoulder when you enter."
        $ mc.change_locked_clarity(5)
        the_person "Hi [the_person.mc_title], I hope you've had a good day."
        "She turns back to her work and hums happily."

    elif the_person.effective_sluttiness(["bare_pussy","bare_tits"]) < 60:
        $ the_person.apply_outfit(Outfit("Nude"))
        $ add_mom_outfit_coloured_apron(the_person)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen, completely nude except for her apron. She glances over her shoulder when you enter."
        the_person "Hi [the_person.mc_title]. If me being... naked makes you uncomfortable just let me know. It's just nice to relax a little after work."
        $ mc.change_locked_clarity(10)
        mc.name "I don't mind at all Mom."
        "She turns her attention back to preparing dinner."

    else:
        $ the_person.apply_outfit(Outfit("Nude"))
        $ add_mom_outfit_coloured_apron(the_person)
        $ the_person.draw_person(position = "back_peek")
        "You find [the_person.possessive_title] in the kitchen, completely nude except for her apron. She glances over her shoulder when you enter."
        $ mc.change_locked_clarity(15)
        the_person "Hi [the_person.mc_title], I hope you've had a great day. Dinner should be ready soon!"
        "She turns back to her work and sings happily to herself, wiggling her butt as she works."

    $ the_person.update_outfit_taboos()
    $ the_person.discover_opinion("not wearing anything")
    $ clear_scene()
    return

label breeding_mom_intro_label(the_person):
    $ the_person.apply_outfit(Outfit("Nude"))
    $ the_person.draw_person(position = "sitting")
    $ the_person.update_outfit_taboos()
    $ mc.change_locked_clarity(10)
    "You walk into [the_person.title]'s room and find her sitting on the edge of her bed, completely naked."
    the_person "[the_person.mc_title], close the door, please. I have something I need to ask you."
    "You close the door to [the_person.possessive_title]'s bedroom and walk over to her bed."
    "She pats the bed beside her and you sit down."
    the_person "I've been thinking a lot about this. You're all grown up and [lily.title] isn't far behind."
    the_person "Soon you'll both be leaving home, but I don't think I'm done being a mother yet."
    "She takes your hands in hers and looks passionately into your eyes."
    the_person "I want you to give me a child. Your child."
    #TODO: Reference her fertility percent here. If it's very high we can have some reference to her body "just telling her that now is the time". Normally because the MC drugged her to be more fertile
    if the_person.has_large_tits():
        "Her face is flush and her breathing rapid. Her breasts heave up and down."
    else:
        "Her face is flush and her breathing rapid."
    $ mc.change_locked_clarity(50)

    menu:
        "Fuck her and try to breed her":
            "You nod, and the mere confirmation makes her shiver. She lies down on the bed and holds out her hands for you."
            $ the_person.draw_person(position = "missionary")
            "You strip down and climb on top of her. The tip of your hard cock runs along the entrance of her cunt and finds it dripping wet."
            the_person "Go in raw [the_person.mc_title], enjoy my pussy and give me your cum!"
            $ mc.change_locked_clarity(20)
            $ the_person.break_taboo("vaginal_sex")
            $ the_person.break_taboo("condomless_sex")
            "She wraps her arms around your torso and pulls you tight against her. She gives you a breathy moan when you slide your cock home."
            the_person "Ah... Fuck me and give me your baby! I'll take such good care of them, just like I did for you and [lily.title]!"
            $ starting_creampies = the_person.sex_record.get("Vaginal Creampies",0)
            call fuck_person(the_person, start_position = missionary, start_object = mc.location.get_object_with_name("bed"), skip_intro = True, position_locked = True) from _call_fuck_person_19
            $ the_report = _return
            if the_person.sex_record.get("Vaginal Creampies", 0) > starting_creampies: #We've creampied her at least once this encounter.
                "You roll off of [the_person.possessive_title] and onto the bed beside her, feeling thoroughly spent."
                "She brings her knees up against her chest and tilts her hips up, holding all of your cum deep inside of her."
                mc.name "Do you think that did it?"
                the_person "I don't know. It's the right time of the month."
                "You lie together in silence. [the_person.possessive_title] rocks herself side to side. You imagine your cum sloshing around her womb."
                $ the_person.draw_person(position = "sitting")
                "Eventually she puts her legs down and the two of you sit up in bed."
                $ the_person.add_role(breeder_role)

            else:
                "You roll off of [the_person.possessive_title] and onto the bed beside her."
                $ the_person.change_happiness(-20)
                the_person "I'm sorry... I'm sorry I'm not good enough to make you cum. I'm not good enough to earn your child..."
                "She sounds as if she is almost on the verge of tears."
                "You wrap your arms around her and hold her close."
                mc.name "Shh... You were fantastic. It's me, I'm just not feeling it today. Maybe we can try some other day."
                the_person "I don't know, this might have all been a mistake. Let's just... be quiet for a while, okay?"
                $ the_person.draw_person(position = "sitting")
                "You hold [the_person.possessive_title] until she's feeling better, then sit up in bed with her."

        "Refuse":
            $ the_person.draw_person(position = "sitting", emotion = "sad")
            "You shake your head. [the_person.title] looks immediately crestfallen."
            $ the_person.change_happiness(-20)
            the_person "But why..."
            mc.name "[the_person.title], I love you but I can't give you what you want."
            "She nods and turns her head."
            $ the_person.change_slut(-2)
            $ the_person.change_love(-2)
            the_person "Of course... I was just being silly. I should know better."

    $ clear_scene()
    return

label aunt_home_lingerie_label(the_person):
    $ the_person.outfit.strip_to_underwear()
    $ the_person.draw_person()
    $ mc.change_locked_clarity(10)
    "You find [the_person.possessive_title] humming a happy tune, dressed only in her underwear, as you open the door to her apartment."
    if the_person.effective_sluttiness("underwear_nudity") < 10 or the_person.has_taboo("underwear_nudity"):
        "[the_person.title] jumps when she notices you."
        the_person "Oh, [the_person.mc_title]! I didn't know you were coming over!"
        $ the_person.draw_person(position = "back_peek")
        "She turns away, trying to hide the view. You step inside and close the door."
        mc.name "Sorry, I can come back later if you'd like."
        the_person "No, it's fine. I just need a moment to get dressed. You startled me, is all."
        "[the_person.title] seems to relax now that she's recovered from the shock."
        $ the_person.draw_person(position = "walking_away")
        $ the_person.change_slut(1, 35)

        the_person "I'm sure you don't want to see me prancing around like this. Just wait there, I'll be back in a moment!"
        $ get_dressed = True
        menu:
            "Tell her to stay":
                mc.name "Don't worry about it [the_person.title], I really don't mind."
                $ the_person.draw_person(position = "back_peek")
                "[the_person.possessive_title] stops and peeks over her shoulder again."
                if the_person.effective_sluttiness("underwear_nudity") >= 10:
                    $ get_dressed = False
                    the_person "You don't? Isn't it embarrassing to have to look at a half-naked old woman?"
                    mc.name "We're family, we're suppose to be comfortable with each other."
                    the_person "Well... I suppose if you don't mind then I won't bother."
                    $ the_person.draw_person()
                    the_person "But you just let me know if you want me to get dressed!"
                    $ the_person.break_taboo("underwear_nudity")
                    the_person "I'm so glad you stopped by!"

                else:
                    the_person "You're sweet, but you really shouldn't see me like this. We're family, it's a little... strange."
                    the_person "I'll be back before you know it!"

            "Let her get dressed":
                pass


        if get_dressed:
            $ clear_scene()
            "[the_person.title] steps into her bedroom and closes the door."
            $ the_person.apply_outfit()
            "After a brief wait she steps back out."
            $ the_person.draw_person()
            the_person "So sorry about that. [cousin.name] is out, so I was just lounging around."
            the_person "Anyways, I'm glad you stopped by!"

    elif the_person.effective_sluttiness() < 40:
        $ the_person.draw_person(position = "back_peek")
        "[the_person.title] jumps when she notices you, turning her body away to hide the view"
        the_person "Oh, one second, I... Oh, it's just you [the_person.mc_title]! I nearly had a heart attack!"
        $ the_person.draw_person()
        "She laughs and relaxes, turning back to face you."
        mc.name "Sorry [the_person.title], I didn't mean to scare you."
        the_person "It's not your fault, I was scared I had left the door unlocked is all. [cousin.name] is out, so I'm not dressed for company."
        the_person "You don't mind, do you? I can go throw something on."
        menu:
            "Tell her to stay":
                mc.name "Not at all, you're looking good."
                "[the_person.possessive_title] smiles and pats you playfully on the shoulder."
                the_person "Oh, stop. I'm just so glad you stopped by!"

            "Tell her to get dressed":
                mc.name "Might be a good idea, in case [cousin.name] comes home."
                the_person "Good point, that would be hard to explain..."
                the_person "I'll be back in a second!"
                $ clear_scene()
                $ the_person.apply_outfit()
                "[the_person.possessive_title] hurries into her bedroom."
                "After a short wait she's back again."
                $ the_person.draw_person()
                the_person "Now, I'm so glad you stopped by!"

    else:
        "She smiles when she notices you."
        the_person "Oh, hey there [the_person.mc_title]. Just lock the door behind you, okay?"
        the_person "I wouldn't want anyone else walking in on me in my undies."
        "You lock the door again and step inside."
        the_person "I'm so happy you stopped by!"

    call talk_person(the_person) from _call_talk_person_1
    return

label cousin_home_panties_label(the_person):
    $ the_person.outfit.strip_to_underwear()
    $ the_person.draw_person(position = "sitting")
    $ mc.change_locked_clarity(10)
    "You open the door to [the_person.possessive_title]'s room. She's sitting on her bed in her underwear, browsing her phone."
    if the_person.effective_sluttiness("underwear_nudity") < 10 or the_person.has_taboo("underwear_nudity"):
        "She looks up and glares at you."
        the_person "Hey, have you heard of knocking?"
        mc.name "I was..."
        "She cuts you off."
        the_person "I'm not dressed, you idiot! Get out!"
        "[the_person.title] chucks a pillow at you. You step back and close the door."
        "You wait a moment, then shout through the door."
        mc.name "Can I come in yet?"
        the_person "Are you still out there? Ugh..."
        if the_person.effective_sluttiness("underwear_nudity") >= 10:
            the_person "Fuck it, just come in."
            $ the_person.draw_person(position = "sitting")
            "You open the door. [the_person.possessive_title] never even moved from the bed."
            $ the_person.break_taboo("underwear_nudity")
            the_person "Just don't fucking stare, and don't get cum on my stuff if you're going to jizz your pants."
        else:
            $ the_person.change_happiness(-5)
            $ the_person.apply_outfit()
            "You hear [the_person.possessive_title]'s bed creak, then her shuffle around her room for a moment."
            the_person "Alright dweeb, come in and say what you have to say."
            $ the_person.draw_person()

    elif the_person.effective_sluttiness() < 40:
        "She looks up and glares at you."
        the_person "Hey, have you heard of knocking?"
        mc.name "I was..."
        "She cuts you off."
        the_person "I bet you were hoping for this, right? To see me in my panties?"
        if not the_person.outfit.tits_available():
            the_person "Maybe you even thought you'd see my tits? My big, juicy, naked tits?"
            "She laughs sharply."
        else:
            the_person "Probably the closest you can get to seeing a real girl naked."
        the_person "Whatever, I don't even care. Just don't get cum on my stuff if you're going to jizz your pants."
        pass
    else:
        "She looks up at you and sighs."
        the_person "Hey, have you heard of knocking?"
        mc.name "I was..."
        "She cuts you off."
        the_person "Whatever. What do you want?"

    call talk_person(the_person) from _call_talk_person_30
    return

label sister_go_shopping_label(the_person): #TODO: Hook this up as an on_enter event in her room.
    if mc.location.has_person(the_person):
        $ mc.location.move_person(the_person, mall) # Move her to the mall either way, if you don't go she's not in her room any more.
    $ the_person.draw_person()
    "You nearly run into [the_person.title] as you open the door to her room."
    $ trigger_date = False
    if the_person.love < 10:
        the_person "Oh! Hey [the_person.mc_title], I was just heading out."
        "She pushes past you and closes the door to her room behind her."
        the_person "Tell [mom.title] I'm at the mall if she needs me. See ya later!"
        "[the_person.possessive_title] hurries past you and out of the house."
    elif the_person.love < 30:
        the_person "Oh! Hey [the_person.mc_title], I was just heading to the mall."
        "She pushes past you and closes the door to her room behind her."
        menu:
            "Ask to join":
                mc.name "That sounds like fun. Mind if I tag along?"
                the_person "You really want to come on a shopping trip with your sister? Man, you must be {i}booooooored{/i}!"
                "[the_person.possessive_title] smirks and shrugs."
                $ the_person.change_obedience(-1)
                the_person "I guess you can come with me though. I might need someone to carry my things!"
                $ trigger_date = True

            "Say goodbye":
                mc.name "Alright, have fun out there."
                "Tell [mom.title] where I am if she needs me, okay? See ya later!"
                "[the_person.possessive_title] hurries past you and out of the house."

    else:
        the_person "Oh, you have perfect timing [the_person.mc_title]!"
        "She grabs your hand and pulls you into the hallway, closing the door to her room behind her."
        the_person "I was going to head to the mall, but it's always more fun shopping with a friend."
        the_person "Wanna come with me?"
        menu:
            "Go shopping":
                mc.name "Sure, that sounds like fun."
                "[the_person.possessive_title] smiles and nods in agreement."
                $ the_person.change_happiness(5)
                $ trigger_date = True

            "Not right now":
                mc.name "Sorry [the_person.title], I'm busy right now actually."
                the_person "Aww, alright. I've got to get going, see ya later!"
                "[the_person.possessive_title] hurries past you and out of the house."


    if trigger_date:
        "You and [the_person.possessive_title] head downtown, to the largest shopping mall around."
        call shopping_date_intro(the_person, skip_intro = True) from _call_shopping_date_intro

    #TODO: Have a version of this event for Mom
    #TOOO: Have a version where both Lily and Mom go shopping together.
    #TODO: Have a random event where Lily and Mom have already _gone_ shopping, and they want to show you what they bought.
    return

label mom_go_shopping_label(the_person):
    if mc.location.has_person(the_person):
        $ mc.location.move_person(the_person, mall)

    $ the_person.draw_person()
    the_person "Oh, hello [the_person.mc_title]. I was just about to head out and do some shopping."
    $ trigger_date = False
    if the_person.love < 10:
        the_person "I might be back late, but there's dinner in the fridge. All you need to do is warm it up."
        the_person "Take care of your sister, and call me if you need me."
        "She smiles and waves goodbye as she heads for the front door."

    elif the_person.love < 30:
        the_person "I might be back late, but there's dinner in the fridge. All you need to do is warm it up."
        menu:
            "Ask to join":
                mc.name "You know, I have some shopping to do too. Would you like some company?"
                "[the_person.possessive_title] smiles and puts her hand on her chest."
                $ the_person.change_love(1)
                $ the_person.change_obedience(-1)
                the_person "Oh, you're so sweet. Of course you can, if you don't mind being seen with your Mom out in public."
                the_person "I'll try not to embarrass you too badly."
                $ trigger_date = True

            "Say goodbye":
                mc.name "Okay, have fun [the_person.title]."
                the_person "Take care of your sister, and call me if you need me."
                "She smiles and waves goodbye as she heads for the front door."

    else:
        the_person "You have such good taste in clothing, would you like to come along and give me some advice?"
        the_person "If you aren't to embarrassed to be seen shopping with your mom, of course."
        menu:
            "Go shopping":
                mc.name "I've got some shopping of my own to do too. Sure, I'll come along."
                "She smiles happily."
                the_person "It's always nice when we get to spend time together, just the two of us."
                $ trigger_date = True

            "Not right now":
                mc.name "Sorry [the_person.title], I've made plans for the afternoon already."
                the_person "Of course, you're a busy boy! Well then, there's dinner in the fridge."
                the_person "I'll be back later tonight. Take care of your sister."
                "She smiles and waves goodbye, heading for the front door."

    if trigger_date:
        "You and [the_person.possessive_title] head downtown, to the largest shopping mall around."
        call shopping_date_intro(the_person, skip_intro = True) from _call_shopping_date_intro_1
    else:
        $ clear_scene()
    return

#TODO: Add a Mom+Lily shopping haul review (or maybe a Mom+Aunt? They should get more screen time together)
#TODO: You come home and find that Mom/Lily/Aunt have just gotten back from the mall, and they have stuff to show you.
#TODO: Basic option to review their outfits, plus ability to have them strip down/dance/tease you while you watch.
#TODO: Maybe do that as part of the expanded Lily/Mom storyline stuff. I want more context aware stuff from them as well.

#TODO: Some late night events with Lily or Mom masturbating (LR1 vibes)
#TODO: Lily's bedroom search - maybe a generic search for everyone else?
# |-> Roll Gabrielle's room search into this, where you find info about her part time job
