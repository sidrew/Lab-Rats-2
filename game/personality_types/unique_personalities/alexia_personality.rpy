### PERSONALITY CHARACTERISTICS ###
init 1300:
    python:
        def alexia_titles(the_person):
            valid_titles = []
            valid_titles.append(the_person.name)
            valid_titles.append("Alex")
            return valid_titles

        def alexia_possessive_titles(the_person):
            valid_titles = []
            valid_titles.append("Your old classmate")
            return valid_titles

        def alexia_player_titles(the_person):
            valid_titles = [mc.name]
            if the_person.love > 10:
                valid_titles.append("Teacher's pet")
            return valid_titles

        alexia_personality = Personality("alexia", default_prefix = "relaxed",
        common_likes = ["sports", "the colour yellow", "pop music", "marketing work"],
        common_sexy_likes = ["doggy style sex", "bareback sex", "not wearing anything", "skimpy outfits"],
        common_dislikes = ["pants", "conservative outfits", "hiking"],
        common_sexy_dislikes = ["anal sex", "being fingered", "taking control"],
        titles_function = alexia_titles, possessive_titles_function = alexia_possessive_titles, player_titles_function = alexia_player_titles,
        insta_chance = 40, dikdok_chance = 20)
