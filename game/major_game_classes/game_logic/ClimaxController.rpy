init -2 python:
    #TODO: These climax types might have to be Action based at some point if we want to add requirements to them.
    class ClimaxController(renpy.store.object): #A class that allows for the easy formatting and menu display of sex climax options.
        climax_type_dict = {
            "masturbation":0.5,
            "air":0.75, #ie a girl gets you off somehow, but you cum into open air/the floor/yourself
            "body":1.0, #Generic bodyshot. Stomach or ass, normally.
            "face":1.25, #Onto her face, but not explicitly her mouth
            "tits":1.25, #You already know what these are.
            "mouth":1.5, #Cum into her mouth explicitly. Bonus for her swallowing?
            "pussy":2.0, #Creampie. Knocked down to 1.5x if you're wearing a condom.
            "anal":2.0, #Butt-pie? Does this have some sexy name I don't know about?
            "throat":2.0, #Throatpie. Down the hatch!
            "threesome":3.0 #Threesomes rule
            }

        def __init__(self, *args): #Each argument provided should be a list of "display_name" and the climax type that should be associated with that climax
            self.selected_climax_type = None #Set when the player selects a return value, let's us call run_climax() at the correct moment later.
            self.climax_options = args

        @staticmethod
        def get_climax_multiplier(climax_type, with_novelty = False):
            multiplier = ClimaxController.climax_type_dict.get(climax_type, 1.0)
            if mc.condom and climax_type in ["pussy", "anal"]:
                multiplier -= 0.5

            return multiplier

        def set_climax_type(self, type):
            self.selected_climax_type = type

        def show_climax_menu(self): #NOTE: We show the menu even when we don't intend to give more than one option. More player interaction + more information display.
            display_list = []
            for climax_option in self.climax_options:
                display_name = climax_option[0]
                climax_type = climax_option[1]
                if climax_type in ClimaxController.climax_type_dict:
                    display_name += "{size=20}{color=#29B6F6}\n"
                    display_name += "x{multiplier:.2f} Clarity Produced".format(multiplier = self.get_climax_multiplier(climax_type))
                    display_name += "{/color}{/size}"
                    display_name += " (tooltip)All Locked Clarity is released when you climax. How much Clarity is produced varies depending on how you cum, and it's possible to have a multiplier greater than 1!"
                else:
                    climax_option = "masturbation" #TODO: Test this. Allows for non-climax options to be used.
                display_list.append([display_name,climax_option])

            the_choice = renpy.display_menu(display_list, screen = "choice")
            self.set_climax_type(the_choice[1])
            return the_choice[0] #Returns the display string so an event can fllow the appropriate branch

        def do_clarity_release(self, the_person = None, add_to_log = True):
            multiplier = ClimaxController.get_climax_multiplier(self.selected_climax_type)
            if the_person:
                mc.convert_locked_clarity(multiplier, with_novelty = the_person.novelty)
                the_person.change_novelty(-5, add_to_log = add_to_log)
            else:
                mc.convert_locked_clarity(multiplier, with_novelty = mc.masturbation_novelty)
                mc.change_masturbation_novelty(-5, add_to_log = False)
            mc.reset_arousal()
            return

        @staticmethod
        def manual_clarity_release(climax_type = "masturbation", the_person = None, add_to_log = True):
            multiplier = ClimaxController.get_climax_multiplier(climax_type)

            if climax_type != "masturbation" and the_person is None:
                renpy.say(None, "Error: called manual clarity release with " + climax_type + " without passing a person parameter.")

            if the_person:
                mc.convert_locked_clarity(multiplier, with_novelty = the_person.novelty, add_to_log = add_to_log)
                the_person.change_novelty(-5, add_to_log = add_to_log)
            else:
                mc.convert_locked_clarity(multiplier, with_novelty = mc.masturbation_novelty)
                mc.change_masturbation_novelty(-5, add_to_log = False)
            mc.reset_arousal()
            return
