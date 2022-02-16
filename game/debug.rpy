## This file is used to house all of the functions and lables used to debug LR2.##

init -15 python:
    from datetime import datetime
    import traceback

    def run_unit_tests():
        unittest.main(module = renpy.store, argv = ['first-arg-is-ignored'], exit = False)

    def log_message(the_message):
        if not config.developer:
            return #Don't log anything if we're on a production platform.
        file_path = os.path.abspath(os.path.join(config.basedir, "game"))
        file_name = os.path.join(file_path,"DEBUG_LOG.txt")
        opened_file = os.open(file_name,os.O_WRONLY|os.O_APPEND|os.O_CREAT) #Open the log, create it if it doesn't exist already.

        string_to_write = "TIME: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " | " + the_message + "\n"
        os.write(opened_file, string_to_write)
        os.close(opened_file) #Close everything

    def log_missing_personality_labels():
        for personality in list_of_personalities:
            for ending in personality.response_label_ending:
                if not renpy.has_label(personality.personality_type_prefix + "_" + ending):
                    if not renpy.has_label(personality.default_prefix + "_" + ending):
                        log_message("CRITICAL ERROR: Personality \"" + personality.personality_type_prefix + "\" Lacks any label for dialogue type \"" + ending + "\"")
                    else:
                        log_message("Warning: Personality \"" + personality.personality_type_prefix + "\" is using it's default entry for dialogue type \"" + ending + "\"")

    def add_test_text_message():
        mc.phone.add_new_message(mom, test_text_action)
        mc.phone.add_new_message(lily, test_text_action)

    def give_all_insta():
        for place in list_of_places:
            for person in place.get_person_list():
                person.add_role(instapic_role)

    def verify_wardrobe_report(the_wardrobe = None):
        if the_wardrobe is None:
            the_wardrobe = default_wardrobe

        for an_outfit in the_wardrobe.underwear_sets:
            for an_item in an_outfit.generate_clothing_list():
                if an_item.layer >= 2:
                    print "Problem: " + an_outfit.name + " is stored as underwear set but contains layer 2 items."
                    break

        for an_outfit in the_wardrobe.overwear_sets:
            for an_item in an_outfit.generate_clothing_list():
                if an_item.layer < 2:
                    print "Problem: " + an_outfit.name + " is stored as overerwear set but contains layer 1 items."
                    break


    def verify_wardrobe (the_wardrobe = None):
        if the_wardrobe is None:
            the_wardrobe = default_wardrobe

        for an_outfit in the_wardrobe.underwear_sets:
            for an_item in an_outfit.generate_clothing_list():
                if an_item.layer >= 2:
                    print "Problem: " + an_outfit.name + " is stored as underwear set but contains layer 2 items."
                    return False

        for an_outfit in the_wardrobe.overwear_sets:
            for an_item in an_outfit.generate_clothing_list():
                if an_item.layer < 2:
                    print "Problem: " + an_outfit.name + " is stored as overerwear set but contains layer 1 items."
                    return False

        return True



label test_memory_use():
    #TODO: Create 10 people
    #TODO: Draw each of them
    #TODO: Check total memory usage.
    python:
        for x in range(0,10):
            the_person = create_random_person()
            the_person.draw_person()
            renpy.say("TEST", "Talking to person " + str(x) + ": " + the_person.name)
    $ renpy.profile_memory(0.8, 1028)
    return

label debug_label():
    call screen colour_selector()
    if isinstance(_return, Color):
        "We got a colour return!"
    else:
        "Something went wrong, no color return."
    return


label text_message_style_test(the_person = None): #For now we need to both set the text_conversation person as well as the text font. We need to figure out a way to apply it dynamically.
    mom "This is the normal person style!"
    $ mc.start_text_convo(the_person)
    mom "...And this is the text message style!"
    mom "Here's a much longer conversation!"
    mom "... It just keeps going!"
    mom "Oh my god [mom.mc_title], your message log is so large!"
    mc.name "Now let's see what it looks like when I message you!"
    mc.name "Ahah! It's working!"
    mc.name "And now we can display a veeeeeeeeery long mesage to see how well the system handles it. Isn't that impressive?"
    mc.name "Yeah, of course it is!"
    mom "So impressive!"
    "[lily.possessive_title] knocks on your door and opens it up."
    $ lily.draw_person()
    mc.name "One second [mom.title], [lily.title] just came into the room."
    mom "Okay, take your time!"
    $ mc.phone.add_system_message(mom, mom.title + " set her status to \"Away\".")
    $ mc.pause_text_convo()
    mc.name "Hey [lily.title]."
    lily "Hey [lily.mc_title]. Cool texting system you've got going there."
    mc.name "Thanks, it works pretty well. Talk to you later, okay?"
    lily "Okay, talk to you later."
    $ clear_scene()
    $ mc.resume_text_convo()
    mc.name "I'm back. Glad to see this is still working well!."
    mom "Me too. Now, let's see if it can handle having to make a choice!"
    menu:
        "Of course it can!":
            mc.name "Of course it can [mom.title]!"

        "I have my doubts.":
            mc.name "I doubt I even made it this far. Oh well."
    mom "I knew it would work. Good job!"
    mom "Me too, it's very good. Now let's end the conversation and see if that works properly."
    $ mc.end_text_convo()
    mom "And now we should be back to normal!"
    return


label person_select_debug:
    "Calling screen now!"
    call screen employee_overview(person_select = True)
    "Done! The returned person was: [_return.name]!"
    return

label debug_start:
    #TODO: Debug stuff here.
    $ log_message("Starting our debugging!")
    $ log_message("Creating town with no people.")
    $ town_time = time.time()
    call create_test_variables("DEBUG", "DEBUG INC.","LASTNAME",[0,0,0], [0,0,0,0,0], [0,0,0,0,0],max_num_of_random=0) from _call_create_test_variables_1
    $ log_message("Finished. Took: " + str(time.time()-town_time) + " Seconds")
    $ people_per_location = 20

    $ log_message("Populating town now. Adding " + str(people_per_location) + " people to each location.")
    $ person_time = time.time()
    $ location_count = 0
    python:
        for place in list_of_places:
            if place.public:
                location_count += 1
                for x in range(0,people_per_location):
                    the_person = create_random_person()
                    the_person.generate_home()
                    place.add_person(the_person)
    $ log_message("Finished. Added " + str(location_count*people_per_location) + " people total to " + str(location_count) + " places.")
    $ log_message("Total time: " + str(time.time()-person_time) + " Seconds. Average time per person: " + str((time.time()-person_time)/(people_per_location*location_count)) + " Seconds.")

    $ log_message("Now doubling number of people. Time per person should remain constant.")
    $ person_time = time.time()
    $ location_count = 0
    python:
        for place in list_of_places:
            if place.public:
                location_count += 1
                for x in range(0,people_per_location):
                    place.add_person(create_random_person())
    $ log_message("Finished. Added " + str(location_count*people_per_location) + " people total to " + str(location_count) + " places.")
    $ log_message("Total time: " + str(time.time()-person_time) + " Seconds. Average time per person: " + str((time.time()-person_time)/(people_per_location*location_count)) + " Seconds.")

    $ log_message("Debugging Finished.")
    return

label debug_run_turn:
    $ log_message("Starting our turn debugging!")
    $ log_message("Advancing time now.")
    $ turn_time = time.time()
    call advance_time from _call_advance_time_27
    $ log_message("Finished. Time taken: " + str(time.time()-turn_time))
    return

label debug_create_position_csv():
    python:
        string = ""
        full_list_of_positions = list_of_positions[:]
        for position in list_of_positions + list_of_girl_positions:
            for connection in position.connections:
                full_list_of_positions.append(connection) #Get all of their stuff
        set_of_positions = __builtin__.set(full_list_of_positions) #Trim out repeated objects.

        for position in set_of_positions:
            string += position.name + ", "
            string += position.skill_tag + ", "
            string += str(position.guy_arousal) + ", "
            string += str(position.girl_arousal) + ", "
            string += str(position.guy_energy) + ", "
            string += str(position.girl_energy) + ", "
            string += str(position.slut_requirement) + ", "
            string += str(position.slut_cap) + ", "
            for trans in position.transitions:
                string += position.name + " -> " + trans[0].name + " | "
            string += "\n"

        log_message("Position CSV: " + string)
    return

label edit_default_wardrobe:
    call screen girl_outfit_select_manager(default_wardrobe, show_sets = True)
    $ picked_outfit = _return
    call create_outfit(picked_outfit) from _call_create_outfit_2
    return

label load_select_from_wardrobe(the_wardrobe):
    call screen girl_outfit_select_manager(the_wardrobe, show_sets = True)
    $ picked_outfit = _return
    call create_outfit(picked_outfit) from _call_create_outfit_3
    return

screen display_all_faces():
    add "Paper_Background.png"
    hbox:
        spacing -250
        add "character_images/default_Face_1_stand2_white.png"
        add "character_images/default_Face_2_stand2_white.png"
        add "character_images/default_Face_3_stand2_white.png"
        add "character_images/default_Face_4_stand2_white.png"
        add "character_images/default_Face_5_stand2_white.png"
        add "character_images/default_Face_6_stand2_white.png"

screen display_all_hair():
    add "Paper_Background.png"
    viewport:
        mousewheel True
        scrollbars "vertical"
        xsize 1920
        ysize 1080

        vbox:
            spacing -900
            for hair in hair_styles:
                hbox:
                    text hair.name
                    $ hair_displayable = hair.generate_item_displayable("standard_body", "AA", "stand2")
                    add hair_displayable

screen test_variable_display():

    text "Energy: [mc.energy]":
        xanchor 1.0
        xalign 1.0

    textbutton "Energy: [mc.energy]":
        xanchor 1.0
        xalign 1.0

label test_malformed_say(the_person):
    the_person "Hello world!"
    the_person "This is a test!"
    return
