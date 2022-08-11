init -2 python:
    class Person(renpy.store.object): #Everything that needs to be known about a person.
        #Define "private" range limits, use static/class methods to retrieve from the Person class
        _final_stat_floor = 0
        _initial_stat_floor = 1
        _initial_stat_ceiling = 5

        _final_skill_floor = 0
        _initial_skill_floor = 1
        _initial_skill_ceiling = 5

        _final_sex_skill_floor = 0
        _initial_sex_skill_floor = 1
        _initial_sex_skill_ceiling = 5

        _final_happiness_floor = 0
        _initial_happiness_floor = 90
        _initial_happiness_ceiling = 110

        _initial_suggestibility_floor = 0
        _initial_suggestibility_ceiling = 15

        _initial_sluttiness_floor = 0
        _initial_sluttiness_ceiling = 10

        _final_love_floor = -100
        _initial_love_floor = 0
        _initial_love_ceiling = 0
        _final_love_ceiling = 100

        _final_obedience_floor = 0
        _initial_obedience_floor = 90
        _initial_obedience_ceiling = 110

        _final_work_experience_floor = 1
        _initial_work_experience_floor = 1
        _initial_work_experience_ceiling = 3
        _final_work_experience_ceiling = 5

        _initial_age_floor = 18
        _initial_age_ceiling = 50
        _final_age_floor = 18
        _final_age_ceiling = 60
        _teen_age_ceiling = 19
        _old_age_floor = 40

        _height_step = 0.015 #1 inch
        _initial_height_floor =   ((5 * 12) +  0) * _height_step #5'  0"
        _initial_height_ceiling = ((5 * 12) + 10) * _height_step #5' 10"
        _final_height_floor =     ((4 * 12) +  0) * _height_step #4'  0"
        _final_height_ceiling =   ((7 * 12) +  0) * _height_step #7'  0"
        _short_height_ceiling =   ((5 * 12) +  3) * _height_step #5'  3"
        _tall_height_floor =      ((5 * 12) +  9) * _height_step #5'  9"

        _base_list_of_relationships = [["Single",120],["Girlfriend",50],["Fiancée",120],["Married",20]]

        _large_tit_minimum = "D"
        _huge_tit_minimum = "E"
        _small_tit_maximum = "C"
        _tiny_tit_maximum = "AA"

        _list_of_names = []

        _list_of_names.append("Jessica")
        _list_of_names.append("Jenny")
        _list_of_names.append("Victoria")
        _list_of_names.append("Lily")
        _list_of_names.append("Jennifer")
        _list_of_names.append("Nora")
        _list_of_names.append("Stephanie")
        _list_of_names.append("Alexia")
        _list_of_names.append("Danielle")
        _list_of_names.append("Ashley")
        _list_of_names.append("Brittany")
        _list_of_names.append("Sally")
        _list_of_names.append("Helen")
        _list_of_names.append("Sarah")
        _list_of_names.append("Erika")
        _list_of_names.append("Sandra")
        _list_of_names.append("Maya")
        _list_of_names.append("Emma")
        _list_of_names.append("Katya")
        _list_of_names.append("Saphirette")
        _list_of_names.append("Charisma")
        _list_of_names.append("Mayumi")
        _list_of_names.append("Brendan")
        _list_of_names.append("Josie")
        _list_of_names.append("Saya")
        _list_of_names.append("Yamiko")
        _list_of_names.append("Rowena")
        _list_of_names.append("Katie")
        _list_of_names.append("Dawn")
        _list_of_names.append("Sasha")
        _list_of_names.append("Melanie")
        _list_of_names.append("Tina")
        _list_of_names.append("Raven")
        _list_of_names.append("Sarah")
        _list_of_names.append("Antonia")
        _list_of_names.append("Mina")
        _list_of_names.append("Marisha")
        _list_of_names.append("Misty")
        _list_of_names.append("Krya")
        _list_of_names.append("Kida")
        _list_of_names.append("Miyu")
        _list_of_names.append("Rayne")
        _list_of_names.append("Joana")
        _list_of_names.append("Bobbi")
        _list_of_names.append("Moira")
        _list_of_names.append("Penelope")
        _list_of_names.append("Julie")
        _list_of_names.append("Geneviève")
        _list_of_names.append("Persephone")
        _list_of_names.append("Kylie")
        _list_of_names.append("Alice")
        _list_of_names.append("Ginger")
        _list_of_names.append("Shirley")
        _list_of_names.append("Alicia")
        _list_of_names.append("Arianne")
        _list_of_names.append("Roxy")
        _list_of_names.append("Sheyla")
        _list_of_names.append("Candice")
        _list_of_names.append("Becky")
        _list_of_names.append("Susan")
        _list_of_names.append("Kirsten")
        _list_of_names.append("Sylvia")
        _list_of_names.append("Niamh")
        _list_of_names.append("Teagan")
        _list_of_names.append("Robin")
        _list_of_names.append("Mara")
        _list_of_names.append("Veronica")
        _list_of_names.append("Misa")
        _list_of_names.append("Kerri")
        _list_of_names.append("Marianne")
        _list_of_names.append("Mary-Ann")
        _list_of_names.append("Angela")
        _list_of_names.append("June")
        _list_of_names.append("Angie")
        _list_of_names.append("Gillian")
        _list_of_names.append("Faith")
        _list_of_names.append("Julia")
        _list_of_names.append("Bailey")
        _list_of_names.append("Sierra")
        _list_of_names.append("Terry")
        _list_of_names.append("Cordula")
        _list_of_names.append("Suzy")
        _list_of_names.append("Elizabeth")
        _list_of_names.append("Danny")
        _list_of_names.append("Kanya")
        _list_of_names.append("Kay")
        _list_of_names.append("Soni")
        _list_of_names.append("Alana")
        _list_of_names.append("Lira")
        _list_of_names.append("Lilith")
        _list_of_names.append("Raislyn")
        _list_of_names.append("Gina")
        _list_of_names.append("Chrystal")
        _list_of_names.append("Jenny")
        _list_of_names.append("Selene")
        _list_of_names.append("Piper")
        _list_of_names.append("Nicole")
        _list_of_names.append("Seraphina")
        _list_of_names.append("Kitty")
        _list_of_names.append("Isabelle")
        _list_of_names.append("Fae")
        _list_of_names.append("Beth")
        _list_of_names.append("Lystra")
        _list_of_names.append("Katreena")
        _list_of_names.append("Hannah")
        _list_of_names.append("Mara")
        _list_of_names.append("Trinity")
        _list_of_names.append("Stephine")
        _list_of_names.append("Sydney")
        _list_of_names.append("Amai")
        _list_of_names.append("Edith")
        _list_of_names.append("Alina")
        _list_of_names.append("Jae")
        _list_of_names.append("Abbigail")
        _list_of_names.append("Kayla")
        _list_of_names.append("Tia")
        _list_of_names.append("Mimi")
        _list_of_names.append("Evelyn")
        _list_of_names.append("Leah")
        _list_of_names.append("Katya")
        _list_of_names.append("Kathryn")
        _list_of_names.append("Bronwyn")
        _list_of_names.append("Tilly")
        _list_of_names.append("Katsuni")
        _list_of_names.append("Samantha")
        _list_of_names.append("Mara")
        _list_of_names.append("Zimu")
        _list_of_names.append("Maria")
        _list_of_names.append("Bunny")
        _list_of_names.append("Kara")
        _list_of_names.append("Dina")
        _list_of_names.append("Priya")
        _list_of_names.append("Zaya")
        _list_of_names.append("Mitzy")
        _list_of_names.append("Abigail")
        _list_of_names.append("Georgia")
        _list_of_names.append("Kaitlyn")
        _list_of_names.append("Asa")
        _list_of_names.append("Olivia")
        _list_of_names.append("Kimberley")
        _list_of_names.append("Daisy")
        _list_of_names.append("Ariel")
        _list_of_names.append("Jade")
        _list_of_names.append("Kaia")
        _list_of_names.append("Madeline")
        _list_of_names.append("Nu")
        _list_of_names.append("Piper")
        _list_of_names.append("Kelly")
        _list_of_names.append("Claire")
        _list_of_names.append("Elizabeth")
        _list_of_names.append("Hayley")
        _list_of_names.append("Melanie")
        _list_of_names.append("Morrigan")
        _list_of_names.append("Talia")
        _list_of_names.append("Sandra")
        _list_of_names.append("Kaylani")
        _list_of_names.append("Emily")
        _list_of_names.append("Steffi")
        _list_of_names.append("Vanessa")
        _list_of_names.append("Bonnie")
        _list_of_names.append("Jasmine")
        _list_of_names.append("Sasha")
        _list_of_names.append("Alessandra")
        _list_of_names.append("Ara")
        _list_of_names.append("Ami")
        _list_of_names.append("Ann-Kathrin")
        _list_of_names.append("Lizzie")
        _list_of_names.append("Bamboo")
        _list_of_names.append("Layla")
        _list_of_names.append("Electra")
        _list_of_names.append("Angelina")
        _list_of_names.append("Kaiya")
        _list_of_names.append("Romina")
        _list_of_names.append("Jasmine")
        _list_of_names.append("Judy")


        _list_of_last_names = []
        _list_of_last_names.append("Hitchcock")
        _list_of_last_names.append("Peters")
        _list_of_last_names.append("Fallbrooke")
        _list_of_last_names.append("Williams")
        _list_of_last_names.append("Orion")
        _list_of_last_names.append("Marie")
        _list_of_last_names.append("Millstein")
        _list_of_last_names.append("Sky")
        _list_of_last_names.append("Spherica")
        _list_of_last_names.append("Fields")
        _list_of_last_names.append("Moran")
        _list_of_last_names.append("Kurokami")
        _list_of_last_names.append("Bergstrom")
        _list_of_last_names.append("Fernandez")
        _list_of_last_names.append("Bergstrom")
        _list_of_last_names.append("Sasamiya")
        _list_of_last_names.append("Onihime")
        _list_of_last_names.append("Lancie")
        _list_of_last_names.append("Simmons")
        _list_of_last_names.append("Parsons")
        _list_of_last_names.append("Lockheart")
        _list_of_last_names.append("Summers")
        _list_of_last_names.append("Seras")
        _list_of_last_names.append("Proud")
        _list_of_last_names.append("Blanes")
        _list_of_last_names.append("Shaw")
        _list_of_last_names.append("Bailey")
        _list_of_last_names.append("Daniels")
        _list_of_last_names.append("Castillo")
        _list_of_last_names.append("Kimiko")
        _list_of_last_names.append("Farrowsdotter")
        _list_of_last_names.append("Prashad")
        _list_of_last_names.append("Pharys")
        _list_of_last_names.append("Pires")
        _list_of_last_names.append("Brock")
        _list_of_last_names.append("Kingsley")
        _list_of_last_names.append("Navarias")
        _list_of_last_names.append("LaPorte")
        _list_of_last_names.append("Isabella")
        _list_of_last_names.append("Hamilton")
        _list_of_last_names.append("Hellene")
        _list_of_last_names.append("Belladonna")
        _list_of_last_names.append("Vedeer")
        _list_of_last_names.append("Currance")
        _list_of_last_names.append("Murray")
        _list_of_last_names.append("Silvers")
        _list_of_last_names.append("Vermelen")
        _list_of_last_names.append("Blair")
        _list_of_last_names.append("Rojas")
        _list_of_last_names.append("Reichart")
        _list_of_last_names.append("Swift")
        _list_of_last_names.append("Carroll")
        _list_of_last_names.append("Maugher")
        _list_of_last_names.append("Moonstone")
        _list_of_last_names.append("Kirk")
        _list_of_last_names.append("Deal")
        _list_of_last_names.append("Quinn")
        _list_of_last_names.append("Jade")
        _list_of_last_names.append("Smythe")
        _list_of_last_names.append("Rose")
        _list_of_last_names.append("Chanen")
        _list_of_last_names.append("Pesche")
        _list_of_last_names.append("Lighton")
        _list_of_last_names.append("Michaelson")
        _list_of_last_names.append("Anderson")
        _list_of_last_names.append("Connors")
        _list_of_last_names.append("Song")
        _list_of_last_names.append("Rosen")
        _list_of_last_names.append("Mayfair")
        _list_of_last_names.append("Morgan")
        _list_of_last_names.append("Grün")
        _list_of_last_names.append("Berry")
        _list_of_last_names.append("Sanders")
        _list_of_last_names.append("Samson")
        _list_of_last_names.append("Chailai")
        _list_of_last_names.append("Hara")
        _list_of_last_names.append("Newman")
        _list_of_last_names.append("Mead")
        _list_of_last_names.append("Ersson")
        _list_of_last_names.append("Sill")
        _list_of_last_names.append("Mahjor")
        _list_of_last_names.append("Whitehair")
        _list_of_last_names.append("Perrit")
        _list_of_last_names.append("White")
        _list_of_last_names.append("Wolf")
        _list_of_last_names.append("Jung")
        _list_of_last_names.append("Dussoir")
        _list_of_last_names.append("Dreadlow")
        _list_of_last_names.append("Duroche")
        _list_of_last_names.append("Hampson")
        _list_of_last_names.append("Faith")
        _list_of_last_names.append("Lee")
        _list_of_last_names.append("Carbonero")
        _list_of_last_names.append("Cotten")
        _list_of_last_names.append("Ookami")
        _list_of_last_names.append("Du Roche")
        _list_of_last_names.append("Collins")
        _list_of_last_names.append("Sladek")
        _list_of_last_names.append("Liu")
        _list_of_last_names.append("Carbonara")
        _list_of_last_names.append("Anne")
        _list_of_last_names.append("Li")
        _list_of_last_names.append("West")
        _list_of_last_names.append("Everette")
        _list_of_last_names.append("Derry")
        _list_of_last_names.append("Ling")
        _list_of_last_names.append("Bjornson")
        _list_of_last_names.append("Lin")
        _list_of_last_names.append("Jaye")
        _list_of_last_names.append("Bowing")
        _list_of_last_names.append("Llandry")
        _list_of_last_names.append("Selkirk")
        _list_of_last_names.append("James")
        _list_of_last_names.append("Laura")
        _list_of_last_names.append("Belgazoo")
        _list_of_last_names.append("Linden")
        _list_of_last_names.append("Sov")
        _list_of_last_names.append("Fang")
        _list_of_last_names.append("Sykora")
        _list_of_last_names.append("Honey")
        _list_of_last_names.append("Troy")
        _list_of_last_names.append("Landry")
        _list_of_last_names.append("Rai")
        _list_of_last_names.append("Cassidy")
        _list_of_last_names.append("Irons")
        _list_of_last_names.append("Bard")
        _list_of_last_names.append("Holmes")
        _list_of_last_names.append("Birch")
        _list_of_last_names.append("Akira")
        _list_of_last_names.append("Holmes")
        _list_of_last_names.append("Benson")
        _list_of_last_names.append("Spitz")
        _list_of_last_names.append("Rose")
        _list_of_last_names.append("Collins")
        _list_of_last_names.append("Jones")
        _list_of_last_names.append("Cakes")
        _list_of_last_names.append("Nguyen")
        _list_of_last_names.append("Perri")
        _list_of_last_names.append("Archer")
        _list_of_last_names.append("Grant")
        _list_of_last_names.append("Black")
        _list_of_last_names.append("Williams")
        _list_of_last_names.append("Glaser")
        _list_of_last_names.append("Meade")
        _list_of_last_names.append("Crusher")
        _list_of_last_names.append("Lei")
        _list_of_last_names.append("Swann")
        _list_of_last_names.append("Wildmoser")
        _list_of_last_names.append("Sánchez")
        _list_of_last_names.append("Jones")
        _list_of_last_names.append("Tanaka")
        _list_of_last_names.append("DeVille")
        _list_of_last_names.append("Onuki")
        _list_of_last_names.append("Luck")
        _list_of_last_names.append("Archer")
        _list_of_last_names.append("Bui")
        _list_of_last_names.append("Stephanopoulus")
        _list_of_last_names.append("Wright")
        _list_of_last_names.append("Kühnel")
        _list_of_last_names.append("Lynn")
        _list_of_last_names.append("Mueller")
        _list_of_last_names.append("Howarth")
        _list_of_last_names.append("Marsh")

        _list_of_male_names = []
        _list_of_male_names.append("Aaron")
        _list_of_male_names.append("Andre")
        _list_of_male_names.append("Bradley")
        _list_of_male_names.append("Colin")
        _list_of_male_names.append("Dustin")
        _list_of_male_names.append("Erwin")
        _list_of_male_names.append("Felix")
        _list_of_male_names.append("Glenn")
        _list_of_male_names.append("Harold")
        _list_of_male_names.append("Ivan")
        _list_of_male_names.append("Jake")
        _list_of_male_names.append("Jon")
        _list_of_male_names.append("Julian")
        _list_of_male_names.append("Kurt")
        _list_of_male_names.append("Kim")
        _list_of_male_names.append("Lowell")
        _list_of_male_names.append("Maxwell")
        _list_of_male_names.append("Morton")
        _list_of_male_names.append("Neil")
        _list_of_male_names.append("Omar")
        _list_of_male_names.append("Peter")
        _list_of_male_names.append("Raul")
        _list_of_male_names.append("Rudy")
        _list_of_male_names.append("Steve")
        _list_of_male_names.append("Stuart")
        _list_of_male_names.append("Terrance")
        _list_of_male_names.append("Terry")
        _list_of_male_names.append("Tyrone")
        _list_of_male_names.append("Vincent")
        _list_of_male_names.append("Wilbur")
        _list_of_male_names.append("William")
        _list_of_male_names.append("Zachary")

        _coffee_list = []
        _coffee_list.append("just black")
        _coffee_list.append("one milk")
        _coffee_list.append("two milk")
        _coffee_list.append("cream and sugar")
        _coffee_list.append("just a splash of cream")
        _coffee_list.append("lots of sugar")
        _coffee_list.append("just a little sugar")



        #These are "ideal" hair colours. Individuals will have minor variations applied to them so that different "blonds" have slightly different hair.
        _list_of_hairs = []
        _list_of_hairs.append(["blond", [0.89,0.75,0.47,1]])
        _list_of_hairs.append(["brown", [0.21,0.105,0.06,1]])
        _list_of_hairs.append(["black",[0.09,0.07,0.09,1]])
        _list_of_hairs.append(["chestnut", [0.59,0.31,0.18,1]])
        #TODO: Add more hair colours

        _list_of_skins = []
        _list_of_skins.append(["white",5])
        _list_of_skins.append(["black",1])
        _list_of_skins.append(["tan",2])

        _list_of_faces = [] # Only character critical faces are included in all versions.
        _list_of_faces.append("Face_1")
        _list_of_faces.append("Face_2")
        _list_of_faces.append("Face_3")
        _list_of_faces.append("Face_4")
        _list_of_faces.append("Face_5")

        _list_of_faces.append("Face_6")
        _list_of_faces.append("Face_7")
        _list_of_faces.append("Face_8")
        _list_of_faces.append("Face_9") #Used to be Mobile Exclusion
        #_list_of_faces.append("Face_10") #Bad render
        _list_of_faces.append("Face_11") #Used to be Mobile Exclusion
        _list_of_faces.append("Face_12") #Used to be Mobile Exclusion
        _list_of_faces.append("Face_13") #Used to be Mobile Exclusion
        _list_of_faces.append("Face_14") #Used to be Mobile Exclusion

        _list_of_eyes = []
        _list_of_eyes.append(["dark blue",[0.32, 0.60, 0.82, 1.0]]) # (["dark blue",[0.18, 0.33, 0.44, 1.0]])
        _list_of_eyes.append(["light blue",[0.60, 0.75, 0.98, 1.0]]) # 0.25, 0.32, 0.37, 1.0]])
        _list_of_eyes.append(["green",[0.35, 0.68, 0.40, 1.0]])
        _list_of_eyes.append(["brown",[0.6, 0.5, 0.3, 1.0]])
        _list_of_eyes.append(["grey",[0.95, 0.98, 0.98, 1.0]])

        _list_of_tits = []
        _list_of_tits.append(["AA",5])
        _list_of_tits.append(["A",15])
        _list_of_tits.append(["B",30])
        _list_of_tits.append(["C",30])
        _list_of_tits.append(["D",15])
        _list_of_tits.append(["DD",10])
        _list_of_tits.append(["DDD",5])
        _list_of_tits.append(["E",2])
        _list_of_tits.append(["F",1])
        _list_of_tits.append(["FF",1])

        _list_of_clothing_colours = []
        _list_of_clothing_colours.append([0.15,0.15,0.15,1]) #Black
        _list_of_clothing_colours.append([1.0,1.0,1.0,1]) #White
        _list_of_clothing_colours.append([0.7,0.4,0.4,1]) #Light Pink
        _list_of_clothing_colours.append([0.4,0.7,0.4,1]) #Light blue
        _list_of_clothing_colours.append([0.4,0.4,0.7,1]) #Light green
        _list_of_clothing_colours.append([0.31,0.23,0.33,1]) #Purple
        _list_of_clothing_colours.append([0.9,0.5,0.1,1]) #Orange

        _list_of_body_types = []
        _list_of_body_types.append("thin_body")
        _list_of_body_types.append("standard_body")
        _list_of_body_types.append("curvy_body")

        # Regular opinions _usually_ add a bit of bonus happiness, but some may influence some options or effects.
        _opinions_list = [] #A master list of things a character might like or dislike. Should always be named so it fits the framework "Likes X" or "Dislikes X". Personalities have a unique list that they always draw from as well
        _opinions_list.append("skirts")
        _opinions_list.append("pants")
        _opinions_list.append("small talk") #Has gameplay effect.
        _opinions_list.append("Mondays") #Has gameplay effect
        _opinions_list.append("Fridays") #Has gameplay effect
        _opinions_list.append("the weekend") #Has gameplay effect
        _opinions_list.append("working") #Has gameplay effect
        _opinions_list.append("the colour blue")
        _opinions_list.append("the colour yellow")
        _opinions_list.append("the colour red")
        _opinions_list.append("the colour pink")
        _opinions_list.append("the colour black")
        _opinions_list.append("heavy metal music")
        _opinions_list.append("jazz")
        _opinions_list.append("punk music")
        _opinions_list.append("classical music")
        _opinions_list.append("pop music")
        _opinions_list.append("conservative outfits") #Has gameplay effect
        _opinions_list.append("work uniforms") #Has gameplay effect
        _opinions_list.append("research work") #Has gameplay effect
        _opinions_list.append("marketing work") #Has gameplay effect
        _opinions_list.append("HR work") #Has gameplay effect
        _opinions_list.append("supply work") #Has gameplay effect
        _opinions_list.append("production work") #Has gameplay effect
        _opinions_list.append("makeup")
        _opinions_list.append("flirting") #Has gameplay effect
        _opinions_list.append("sports") #Has gameplay effect
        _opinions_list.append("hiking") #Hsa gameplay effect


        # Sexy opinions _usually_ add a bit of bonus sluttiness, but some may influence some sex scenes, make some approaches more likely, or have other effects.
        _sexy_opinions_list = [] #Another list of opinions, but these ones are sex/kink related and probably shoudn't be brought up in polite conversation.
        _sexy_opinions_list.append("doggy style sex") #Has gameplay effect
        _sexy_opinions_list.append("missionary style sex") #Has gameplay effect
        _sexy_opinions_list.append("sex standing up") #Has gameplay effect
        _sexy_opinions_list.append("giving blowjobs") #Has gameplay effect
        _sexy_opinions_list.append("getting head") #Has gameplay effect
        _sexy_opinions_list.append("anal sex") #Has gameplay effect
        _sexy_opinions_list.append("vaginal sex") #Has gameplay effect
        _sexy_opinions_list.append("public sex") #Has gameplay effect
        _sexy_opinions_list.append("kissing") #Has gameplay effect
        _sexy_opinions_list.append("lingerie") #Has gameplay effect
        _sexy_opinions_list.append("masturbating") #Has gameplay effect
        _sexy_opinions_list.append("giving handjobs") #Has gameplay effect
        _sexy_opinions_list.append("giving tit fucks") #Has gameplay effect
        _sexy_opinions_list.append("being fingered") #Has gameplay effect
        _sexy_opinions_list.append("skimpy uniforms") #Has gameplay effect
        _sexy_opinions_list.append("skimpy outfits") #Has gameplay effect
        _sexy_opinions_list.append("not wearing underwear") #Has gameplay effect
        _sexy_opinions_list.append("not wearing anything") #Has gameplay effect
        _sexy_opinions_list.append("showing her tits") #Has gameplay effect
        _sexy_opinions_list.append("showing her ass") #Has gameplay effect
        _sexy_opinions_list.append("being submissive") #Has gameplay effect
        _sexy_opinions_list.append("taking control") #Has gameplay effect
        _sexy_opinions_list.append("drinking cum") #Has gameplay effect
        _sexy_opinions_list.append("creampies") #Has gameplay effect
        _sexy_opinions_list.append("cum facials") #Has gameplay effect
        _sexy_opinions_list.append("being covered in cum") #Has gameplay effect
        _sexy_opinions_list.append("bareback sex") #Has gameplay effect.
        _sexy_opinions_list.append("big dicks")
        _sexy_opinions_list.append("cheating on men") #Has gameplay effect
        _sexy_opinions_list.append("anal creampies") #Has gameplay effect
        _sexy_opinions_list.append("incest") #Has gameplay effect
        #TODO: Add an "open relationships" sexy opinion. Reduces penalties of a girl seeing you cheating on her (at high levels add a special training to give a "harem member" role).
        #TODO: Add a "voyeurism" sexy opinion. Increases effects of watching someone having sex.



        @classmethod
        def get_random_tit(cls,min=None,max=None):
            if not min:
                start = 0
            else:
                start = cls.get_tit_index(min)
            if not max:
                end = len(cls._list_of_tits)
            else:
                end =  cls.get_tit_index(max)+1
            return get_random_from_weighted_list(cls._list_of_tits[start:end])


        @classmethod
        def get_tit_weighted_list(cls,min=None,max=None):
            if not min:
                start = 0
            else:
                start = cls.get_tit_index(min)
            if not max:
                end = len(cls._list_of_tits)
            else:
                end =  cls.get_tit_index(max)+1
            return cls._list_of_tits[start:end]

        @classmethod
        def get_maximum_tit(cls):
            return get_random_from_weighted_list(cls._list_of_tits[-1:])

        @classmethod
        def get_tit_index(cls,current_tits):
            return index_in_weighted_list(current_tits,cls._list_of_tits)

        @classmethod
        def rank_tits(cls,the_tits): #Useful if you need to know exactly who has larger tits and want to compare ints. Also see Person.has_large_tits(), for a flat definition of large tits as D or larger
            #Mostly an alias for get_tit_index but defaults to 0 (which is undesirable for a function that may be as like setting a maximum as a minimum)
            try:
                return cls.get_tit_index(the_tits)
            except UnboundLocalError as err:
                return 0

        @classmethod
        def get_smaller_tit(cls,current_tit):
            current_index = cls.get_tit_index(current_tit)
            return cls._list_of_tits[__builtin__.max(0,current_index-1)][0]


        @classmethod
        def get_larger_tit(cls,current_tit):
            current_index = cls.get_tit_index(current_tit)
            return cls._list_of_tits[__builtin__.min(current_index+1,len(cls._list_of_tits)-1)][0]


        @classmethod
        def get_random_tiny_tit(cls):
            return cls.get_random_tit(max=cls._tiny_tit_maximum)


        @classmethod
        def get_random_small_tit(cls):
            return cls.get_random_tit(max=cls._small_tit_maximum)


        @classmethod
        def get_random_large_tit(cls):
            return cls.get_random_tit(min=cls._large_tit_minimum)

        @classmethod
        def get_random_huge_tit(cls):
            return cls.get_random_tit(min=cls._huge_tit_minimum)

        @classmethod
        def get_maximum_tiny_tit(cls):
            return cls._tiny_tit_maximum

        @classmethod
        def get_maximum_small_tit(cls):
            return cls._small_tit_maximum

        @classmethod
        def get_minimum_large_tit(cls):
            return cls._large_tit_minimum

        @classmethod
        def get_minimum_huge_tit(cls):
            return cls._huge_tit_minimum


        @classmethod
        def get_tiny_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(max=cls._tiny_tit_maximum)

        @classmethod
        def get_small_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(max=cls._small_tit_maximum)

        @classmethod
        def get_large_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(min=cls._large_tit_minimum)

        @classmethod
        def get_huge_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(min=cls._huge_tit_minimum)

        @staticmethod
        def tit_is_in_weighted_tits_list(tit,weighted_tit_list):
            return is_in_weighted_list(tit,weighted_tit_list)

        @classmethod
        def tit_is_tiny(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_tiny_tits_weighted_list())

        @classmethod
        def tit_is_small(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_small_tits_weighted_list())

        @classmethod
        def tit_is_large(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_large_tits_weighted_list())

        @classmethod
        def tit_is_huge(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_huge_tits_weighted_list())


        @classmethod
        def get_random_skin(cls):
            return get_random_from_weighted_list(cls._list_of_skins)


        @classmethod
        def get_random_hair_colour(cls):
            return get_random_from_list(cls._list_of_hairs)

        @staticmethod
        def get_darkened_colour(the_colour, variation_constant = 0.07):
            return_list = the_colour[:]
            for component_index in __builtin__.range(3): #In case there's an alpha component, we don't want to change that.
                return_list[component_index] = return_list[component_index] * (1-variation_constant)

            return return_list

        @classmethod
        def generate_hair_colour(cls,base_colour = None, create_variation = True):
            if base_colour:
                for hair in cls.get_list_of_hairs():
                    if hair[0] == base_colour:
                        return_hair = copy.deepcopy(hair)
            else:
                return_hair = copy.deepcopy(cls.get_random_hair_colour()) #Deep copy the hair colours because lists are passed by reference and it is two lists deep.

            if create_variation: #The colour is modified slightly to give different characters slightly different hair colours even if they have the same base.
                hair_colour = return_hair[1]
                for component_index in __builtin__.range(3): #The RGB components can be 10% lighter or darker each.
                    component_variation_constant = 0.07
                    if renpy.random.randint(0,1) == 0:
                        # Shade it, it's a little darker.
                        shade_factor = renpy.random.random() * component_variation_constant
                        hair_colour[component_index] = hair_colour[component_index] * (1-shade_factor)

                    else:
                        # Tint it, it's a little lighter.
                        tint_factor = renpy.random.random() * component_variation_constant
                        hair_colour[component_index] = hair_colour[component_index] + ((1-hair_colour[component_index])*tint_factor)

            return return_hair

        @classmethod
        def get_random_eye(cls):
            return get_random_from_list(cls._list_of_eyes)


        @classmethod
        def generate_eye_colour(cls,base_colour = None, create_variation = True):
            if base_colour:
                for eyes in cls.get_list_of_eyes():
                    if eyes[0] == base_colour: #If we ask for a specific base...
                        return_eyes = copy.deepcopy(eyes)
            else: #Otherwise just get a random one
                return_eyes = copy.deepcopy(cls.get_random_eye()) #Deep copy the hair colours because lists are passed by reference and it is two lists deep.

            if create_variation: #The colour is modified slightly to give different characters slightly different hair colours even if they have the same base.
                eye_colour = return_eyes[1]
                for component_index in __builtin__.range(3): #The RGB components can be 10% lighter or darker each.
                    component_variation_constant = 0.02 #TODO: Test how much this should vary for eye colour.
                    if renpy.random.randint(0,1) == 0:
                        # Shade it, it's a little darker.
                        shade_factor = renpy.random.random() * component_variation_constant
                        eye_colour[component_index] = eye_colour[component_index] * (1-shade_factor)

                    else:
                        # Tint it, it's a little lighter.
                        tint_factor = renpy.random.random() * component_variation_constant
                        eye_colour[component_index] = eye_colour[component_index] + ((1-eye_colour[component_index])*tint_factor)

            return return_eyes



        @classmethod
        def get_random_face(cls):
            return get_random_from_list(cls._list_of_faces)

        @classmethod
        def get_random_name(cls):
            return get_random_from_list(cls._list_of_names)

        @classmethod
        def get_random_last_name(cls):
            return get_random_from_list(cls._list_of_last_names)

        @classmethod
        def get_random_male_name(cls):
            return get_random_from_list(cls._list_of_male_names)

        @classmethod
        def get_random_glasses_frame_colour(cls):
            # Picks one of several mostly-neutral colours that should go well with most items
            return get_random_from_list(cls._list_of_clothing_colours)

        @classmethod
        def get_random_body_type(cls):
            return get_random_from_list(cls._list_of_body_types)

        @classmethod
        def get_normal_opinions_list(cls):
            return cls._opinions_list[:]

        @classmethod
        def get_sexy_opinions_list(cls):
            return cls._sexy_opinions_list[:]


        @classmethod
        def get_random_normal_opinion(cls):
            return get_random_from_list(cls._opinions_list)

        @classmethod
        def get_random_sexy_opinion(cls):
            return get_random_from_list(cls._sexy_opinions_list)

        @classmethod
        def get_random_coffee_style(cls):
            return get_random_from_list(cls._coffee_list)

        @classmethod
        def get_list_of_hairs(cls):
            return copy.deepcopy(cls._list_of_hairs) #Return a deepcopy so that original list and it's content is immutable

        @classmethod
        def get_list_of_eyes(cls):
            return copy.deepcopy(cls._list_of_eyes) #Return a deepcopy so that original list and it's content is immutable

        @classmethod
        def get_stat_floor(cls,initial=True):
            if initial:
                return cls._initial_stat_floor
            else:
                return cls._final_stat_floor

        @classmethod
        def get_skill_floor(cls,initial=True):
            if initial:
                return cls._initial_skill_floor
            else:
                return cls._final_skill_floor

        @classmethod
        def get_sex_skill_floor(cls,initial=True):
            if initial:
                return cls._initial_sex_skill_floor
            else:
                return cls._final_sex_skill_floor

        @classmethod
        def get_stat_ceiling(cls):
            return cls._initial_stat_ceiling

        @classmethod
        def get_skill_ceiling(cls):
            return cls._initial_skill_ceiling

        @classmethod
        def get_sex_skill_ceiling(cls):
            return cls._initial_sex_skill_ceiling

        @classmethod
        def get_happiness_floor(cls,initial=True):
            if initial:
                return cls._initial_happiness_floor
            else:
                return cls._final_happiness_floor

        @classmethod
        def get_happiness_ceiling(cls):
            return cls._initial_happiness_ceiling


        @classmethod
        def get_suggestibility_floor(cls):
            return cls._initial_suggestibility_floor

        @classmethod
        def get_suggestibility_ceiling(cls):
            return cls._initial_suggestibility_ceiling

        @classmethod
        def get_sluttiness_floor(cls):
            return cls._initial_sluttiness_floor

        @classmethod
        def get_sluttiness_ceiling(cls):
            return cls._initial_sluttiness_ceiling

        @classmethod
        def get_love_floor(cls,initial=True):
            if initial:
                return cls._initial_love_floor
            else:
                return cls._final_love_floor

        @classmethod
        def get_love_ceiling(cls,initial=True):
            if initial:
                return cls._initial_love_ceiling
            else:
                return cls._final_love_ceiling

        @classmethod
        def get_obedience_floor(cls,initial=True):
            if initial:
                return cls._initial_obedience_floor
            else:
                return cls._final_obedience_floor

        @classmethod
        def get_obedience_ceiling(cls):
            return cls._initial_obedience_ceiling


        @classmethod
        def get_work_experience_floor(cls,initial=True):
            if initial:
                return cls._initial_work_experience_floor
            else:
                return cls._final_work_experience_floor

        @classmethod
        def get_work_experience_ceiling(cls,initial=True):
            if initial:
                return cls._initial_work_experience_ceiling
            else:
                return cls._final_work_experience_ceiling

        @classmethod
        def get_age_floor(cls,initial=True):
            if initial:
                return cls._initial_age_floor
            else:
                return cls._final_age_floor

        @classmethod
        def get_age_ceiling(cls,initial=True):
            if initial:
                return cls._initial_age_ceiling
            else:
                return cls._final_age_ceiling

        @classmethod
        def get_height_floor(cls,initial=True):
            if initial:
                return cls._initial_height_floor
            else:
                return cls._final_height_floor

        @classmethod
        def get_height_ceiling(cls,initial=True):
            if initial:
                return cls._initial_height_ceiling
            else:
                return cls._final_height_ceiling

        @classmethod
        def get_old_age_floor(cls):
            return cls._old_age_floor

        @classmethod
        def get_teen_age_ceiling(cls):
            return cls._teen_age_ceiling

        @classmethod
        def get_tall_height_floor(cls):
            return cls._tall_height_floor

        @classmethod
        def get_short_height_ceiling(cls):
            return cls._short_height_ceiling

        @classmethod
        def get_height_step(cls):
            return cls._height_step

        @staticmethod
        def get_initial_kids_range(age_range,relationships_array):
            kids_range = [-1,4]
            if age_range[0] > 22 :
                kids_range[0] += 1 #Young people have less time to have kids in general, so modify their number down a bit.
                kids_range[1] += 1

            if age_range[1] < 28:
                kids_range[1] -= 1 #Young characters don't have as many kids

            if age_range[1] < 38:
                kids_range[1] -= 1 #As you get older you're more likely to have one

            if not (is_in_weighted_list("Girlfriend",relationships_array) or is_in_weighted_list("Fiancée",relationships_array) or is_in_weighted_list("Married",relationships_array)):
                kids_range[1] -= 1 #People who are dating have kids more often than single people

            if not (is_in_weighted_list("Fiancée",relationships_array) or is_in_weighted_list("Married",relationships_array)):
                kids_range[1] -= 2 #And married/engaged people have more kids still

            return kids_range

        @classmethod
        def get_potential_relationships_list(cls):
            return copy.deepcopy(cls._base_list_of_relationships)

        #Tighten kid range now that true age is known ?
        @classmethod
        def finalize_kids_range(cls,kids_range,age_range,relationships_list,age,relationship):
            if age_range is None or age_range[0] <= 22:
                if age > 22:
                    kids_range[0] += 1 #Young people have less time to have kids in general, so modify their number down a bit.
                    kids_range[1] += 1
            if age_range is None or age_range[1] >= 28:
                if age < 28:
                    kids_range[1] -= 1 #Young characters don't have as many kids
            if age_range is None or age_range[1] >= 38:
                if age < 38:
                    kids_range[1] -= 1 #Young characters don't have as many kids
            if relationships_list is None or (is_in_weighted_list("Girlfriend",relationships_list) or is_in_weighted_list("Fiancée",relationships_list) or is_in_weighted_list("Married",relationships_list)):
                if relationship not in ["Girlfriend","Fiancée","Married"]:
                    kids_range[1] -= 1 #People who are dating have kids more often than single people
            if relationships_list is None or (is_in_weighted_list("Fiancée",relationships_list) or is_in_weighted_list("Married",relationships_list)):
                if relationship not in ["Fiancée","Married"]:
                    kids_range[1] -= 2 #People who are dating have kids more often than single people
            return kids_range

        @classmethod
        def finalize_relationships_weight(cls,relationships_list,age):
            for relationship in relationships_list:
                if relationship[0] == "Single":
                    relationship[1] -= age
                if relationship[0] == "Fiancée":
                    relationship[1] -= 2*age
                if relationship[0] == "Married":
                    relationship[1] += 4*age
            return relationships_list



        global_character_number = 0 #This is increased for each character that is created.
        def __init__(self,name,last_name,age,body_type,tits,height,body_images,expression_images,hair_colour,hair_style,pubes_colour,pubes_style,skin,eyes,job,wardrobe,personality,stat_list,skill_list,
            sluttiness=0,obedience=100,suggest=0,sex_skill_list=[0,0,0,0], love = 0, happiness = 100, home = None,
            font = "fonts/Avara.tff", name_color = "#ffffff", dialogue_color = "#ffffff",
            face_style = "Face_1",
            special_role = None,
            title = None, possessive_title = None, mc_title = None,
            relationship = None, SO_name = None, kids = None, base_outfit = None,
            generate_insta = False, generate_dikdok = False, generate_onlyfans = False, coffee_style=None,
            work_experience = 1, type="random"):

            self.type = type
            ## Personality stuff, name, ect. Non-physical stuff.
            self.name = name
            self.last_name = last_name
            self.character_number = Person.global_character_number #This is a gunique number for each character. Used as a tag when showing a character to identify if they are already drawn (and thus need to be hidden)
            Person.global_character_number += 1

            self.event_triggers_dict = {} #A dict used to store extra parameters used by events, like how many days has it been since a performance review.

            self.title = title #Note: We format these down below!
            self.possessive_title = possessive_title #The way the girl is refered to in relation to you. For example "your sister", "your head researcher", or just their title again.
            if mc_title:
                self.mc_title = mc_title #What they call the main character. Ie. "first name", "mr.last name", "master", "sir".
            else:
                self.mc_title = "Stranger"

            self.home = home #The room the character goes to at night. If none a random public location is picked.

            self.schedule = Schedule()

            self.override_schedule = Schedule() #The mandatory place a person will go EVEN if they have work (useful for giving days off or requiring weekend work)



            # Relationship and family stuff
            if relationship:
                self.relationship = relationship
            else:
                self.relationship = "Single" #Should be Single, Girlfriend, Fiancée, or Married.

            if SO_name:
                self.SO_name = SO_name
            else:
                self.SO_name = None #If not single, name of their SO (for guilt purposes or future events).

            if kids:
                self.kids = kids
            else:
                self.kids = 0


            self.personality = personality


            # Loves, likes, dislikes, and hates determine some reactions in conversations, options, etc. Some are just fluff.
            self.opinions = {} #Key is the name of the opinion (see random list), value is a list holding [value, known]. Value ranges from -2 to 2 going from hate to love (things not on the list are assumed 0). Known is a bool saying if the player knows about their opinion.

            self.sexy_opinions = {}
            # We establish random opinions first and will overwrite any that conflict with generated personality opinions.
            for x in __builtin__.range(1,5):
                the_opinion_key = Person.get_random_normal_opinion()
                degree = renpy.random.randint(-2,2)
                if not degree == 0: #ie. ignore 0 value opinions.
                    self.opinions[the_opinion_key] = [degree, False]

            for x in __builtin__.range(1,2):
                the_opinion_key = Person.get_random_sexy_opinion()
                degree = renpy.random.randint(-2,2)
                if not degree == 0: #ie. ignore 0 value opinions.
                    self.sexy_opinions[the_opinion_key] = [degree, False]

            #Now we get our more likely default personality ones.
            for x in __builtin__.range(1,4):
                the_opinion_key, opinion_list = self.personality.generate_default_opinion()
                if the_opinion_key:
                    self.opinions[the_opinion_key] = opinion_list

            for x in __builtin__.range(1,3):
                the_opinion_key, opinion_list = self.personality.generate_default_sexy_opinion()
                if the_opinion_key:
                    self.sexy_opinions[the_opinion_key] = opinion_list



            #TODO: Relationship with other people (List of known people plus relationship with them.)

            #Using char instead of a string lets us customize the font and colour we are using for the character.
            self.char = Character("???", #The name to be displayed above the dialogue.
                what_font = font, #The font to be used for the character.
                who_font = font,
                color = name_color, #The colour of the character's NAME section
                what_color = dialogue_color, #The colour of the character's dialogue.
                what_style = "general_dialogue_style") #Used to describe everything that isn't character specific.

            self.what_font = font
            self.who_font = font
            self.what_color = dialogue_color

            if title: #Format the given titles, if any, so they appear correctly the first time you meet at person.
                self.set_title(title) #The way the girl is referred to by the MC. For example: "Mrs. Whatever", "Lily", or "Mom". Will reset "???" if appropriate
            else:
                self.char.name = self.create_formatted_title("???")
            if possessive_title:
                self.set_possessive_title(possessive_title)

            self.text_modifiers = [] #A list of functions, each of which take Person, String and return a modified String. Used to modify text to dynamically highlight words, or reflect a speech difference.

            ## Physical things.
            self.age = age
            self.body_type = body_type
            self.tits = tits
            self.height = height
            self.body_images = body_images.get_copy() #instance of Clothing class, which uses full body shots.
            self.face_style = face_style
            #self.expression_images = expression_images #instance of the Expression class, which stores facial expressions for different skin colours

            self.pubes_colour = None

            self.hair_style = hair_style
            if pubes_style is None:
                self.pubes_style = shaved_pubes #An empty image place holder so we can always call on them to draw.
            else:
                self.pubes_style = pubes_style

            self.set_hair_colour(Color(rgb=(hair_colour[1][0],hair_colour[1][1],hair_colour[1][2])))


            self.skin = skin
            self.set_eye_colour(Color(rgb=(eyes[1][0], eyes[1][1], eyes[1][2])))
            # self.eyes = eyes #A list of [description, color value], where colour value is a standard RGBA list.
            #TODO: Tattoos eventually

            self.serum_tolerance = 2 #How many active serums this person can tolerate before they start to suffer negative effects.
            self.serum_effects = [] #A list of all of the serums we are under the effect of.

            if not special_role:  #Characters may have a special role that unlocks additional actions. By default this is an empty list.
                self.special_role = []
            elif isinstance(special_role, Role):
                self.special_role = [special_role] #Support handing a non-list special role, in case we forget to wrap it in a list one day.
            elif isinstance(special_role, list):
                self.special_role = special_role #Otherwise we've handed it a list
            else:
                self.special_role = []
                log_message("Person \"" + name + " " + last_name + "\" was handed an incorrect special role parameter.")

            self.on_room_enter_event_list = [] #Checked when you enter a room with this character. If an event is in this list and enabled it is run (and no other event is until the room is reentered)
                # If handed a list of [action, positive_int], the integer is how many turns this action is kept around before being removed, triggered or not.
            self.on_talk_event_list = [] #Checked when you start to interact with a character. If an event is in this list and enabled it is run (and no other event is until you talk to the character again.)\
                # If handed a list of [action, positive_int], the integer is how many turns this action is kept around before being removed, triggered or not.

            ##Mental stats##
            #Mental stats are generally fixed and cannot be changed permanently. Ranges from 1 to 5 at start, can go up or down (min 0)
            self.charisma = stat_list[0] #How likeable the person is. Mainly influences marketing, also determines how well interactions with other characters go. Main stat for HR and sales
            self.int = stat_list[1] #How smart the person is. Mainly influences research, small bonuses to most tasks. #Main stat for research and production.
            self.focus = stat_list[2] #How on task the person stays. Influences most tasks slightly. #Main stat for supplies

            self.charisma_debt = 0 #Tracks how far into the negative a characters stats are, for the purposes of serum effects. Effective stats are never lower than 0.
            self.int_debt = 0
            self.focus_debt = 0

            ##Work Skills##
            #Skills can be trained up over time, but are limited by your raw stats. Ranges from 1 to 5 at start, can go up or down (min 0)
            self.hr_skill = skill_list[0]
            self.market_skill = skill_list[1]
            self.research_skill = skill_list[2]
            self.production_skill = skill_list[3]
            self.supply_skill = skill_list[4]

            self.max_energy = 100
            self.energy = self.max_energy

            self.salary_modifier = 1.0 # Set by events for what this character considers "fair" for their skill, and/or reflects what they were promised.
            self.productivity_adjustment = 1.0 # Set by events for what this character is actually able to produce. Generally a "hidden" stat that you can't change.

            self.work_experience = work_experience # How experienced with work in general this girl is. The higher it is the more money a girl will want, but the more duties she can handle.
            self.job = None
            self.duties = []
            self.change_job(job)


            self.salary = self.calculate_base_salary()


            self.idle_pose = get_random_from_list(["stand2","stand3","stand4","stand5"]) #Get a random idle pose that you will use while people are talking to you.
            self.idle_animation = idle_wiggle_animation #If we support animation we use this to jiggle their tits and ass just a little to give the screen some movement.
            #self.idle_animation.innate_animation_strength += 0.05 * rank_tits(self.tits) # Larger tits swing more #TODO: Implement region specific weighting.

            self.personal_region_modifiers = {"breasts":0.1+0.1 * Person.rank_tits(self.tits)} #A dict that stores information about modifiers that should be used for specific regions of animations. Default is 1.

            ##Personality Stats##
            #Things like suggestibility, that change over the course of the game when the player interacts with the girl
            self.suggestibility = 0 + suggest #How likely a girl is to enter or deepen a trance when orgasming
            self.suggest_bag = [] #This will store a list of integers which are the different suggestion values fighting for control. Only the highest is used, maintained when serums are added and removed.

            self.happiness = happiness #Higher happiness makes a girl less likely to quit and more willing to put up with you pushing her using obedience.
            self.love = love
            self.sluttiness = 0 + sluttiness #How slutty the girl is by default. Higher will have her doing more things just because she wants to or you asked.
            self.core_sluttiness = self.sluttiness #Core sluttiness is the base level of what a girl considers normal. normal "sluttiness" is the more variable version, technically refered to as "temporary slutiness".
            self.obedience = obedience #How likely the girl is to listen to commands. Default is 100 (normal person), lower actively resists commands, higher follows them.

            if coffee_style is None:
                self.coffee_style = self.get_random_coffee_style()
            else:
                self.coffee_style = coffee_style

            #Situational modifiers are handled by events. These dicts and related functions provide a convenient way to avoid double contributions. Remember to clear your situational modifiers when you're done with them!!
            self.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
            self.situational_obedience = {} #A dict that stores a "situation" string and a corresponding amount that it has affected their obedience by.

            ##Sex Stats##
            #These are physical stats about the girl that impact how she behaves in a sex scene. Future values might include things like breast sensitivity, pussy tighness, etc.
            self.arousal = 0 #How actively horny a girl is, and how close she is to orgasm.
            self.max_arousal = 100 #Her maximum arousal. TODO: Keep this hidden until you make her cum the first time?

            self.novelty = 100 #How novel this girl making you cum is. Breaking taboos and time increases it, the girl making you cum decreases it.

            ##Sex Skills##
            #These represent how skilled a girl is at different kinds of intimacy, ranging from kissing to anal. The higher the skill the closer she'll be able to bring you to orgasm (whether you like it or not!)
            self.sex_skills = {}
            self.sex_skills["Foreplay"] = sex_skill_list[0] #A catch all for everything that goes on before blowjobs, sex, etc. Includes things like kissing and strip teases.
            self.sex_skills["Oral"] = sex_skill_list[1] #The girls skill at giving head.
            self.sex_skills["Vaginal"] = sex_skill_list[2] #The girls skill at different positions that involve vaginal sex.
            self.sex_skills["Anal"] = sex_skill_list[3] #The girls skill at different positions that involve anal sex.

            self.sex_record = {}
            self.sex_record["Handjobs"] = 0
            self.sex_record["Blowjobs"] = 0
            self.sex_record["Cunnilingus"] = 0
            self.sex_record["Tit Fucks"] = 0
            self.sex_record["Vaginal Sex"] = 0
            self.sex_record["Anal Sex"] = 0
            self.sex_record["Cum Facials"] = 0
            self.sex_record["Cum in Mouth"] = 0
            self.sex_record["Cum Covered"] = 0
            self.sex_record["Vaginal Creampies"] = 0
            self.sex_record["Anal Creampies"] = 0
            self.sex_record["Fingered"] = 0
            self.sex_record["Kissing"] = 0

            self.broken_taboos = [] #Taboos apply a penalty to the _first_ time you are trying to push some boundry (first time touching her pussy, first time seeing her tits, etc.), and trigger special dialogue when broken.

            bc_chance = 100 - (self.age + (self.get_opinion_score("bareback sex")*15))
            if persistent.pregnancy_pref == 2 and renpy.random.randint(0,100) > bc_chance:
                self.on_birth_control = False #If this character is on birth control or not. Note that this may be overridden by a game wide setting preventing pregnancy. (and on other settings may not be 100% effective)
            else:
                self.on_birth_control = True
            self.bc_penalty = 0 #Lowers the chance of birht control preventing a pregnancy. (Default is 100% if predictable or 90% if realistic). #TODO: Add serum traits that affect this.
            self.fertility_percent = 20.0 - ((self.age-18.0)/3.0) #The chance, per creampie, that a girl gets pregnant.
            self.ideal_fertile_day = renpy.random.randint(0,29) #Influences a girls fertility chance. It is double on the exact day of the month, dropping down to half 15 days before/after. Only applies on realistic setting.

            self.lactation_sources = 0 #How many things are causing this girl to lactate. Mainly serum traits, side effects, or pregnancy.

            ## Clothing things.
            self.wardrobe = copy.copy(wardrobe) #Note: we overwrote default copy behaviour for wardrobes so they do not have any interference issues with eachother.
            if base_outfit is None:
                self.base_outfit = Outfit(name + "'s Base Outfit")
            else:
                self.base_outfit = base_outfit


            self.infractions = [] #List of infractions this character has committed.

            self.planned_outfit = self.wardrobe.decide_on_outfit(self.sluttiness) #planned_outfit is the outfit the girl plans to wear today while not at work. She will change back into it after work or if she gets stripped. Cop0y it in case the outfit is changed during the day.
            self.planned_uniform = None #The uniform the person was planning on wearing for today, so they can return to it if they need to while at work.
            self.apply_outfit(self.planned_outfit)


            ## Internet things ##
            if generate_insta: #NOTE: By default all of these are not visible to the player.
                self.add_role(instapic_role)
            if generate_dikdok:
                self.add_role(dikdok_role)
            if generate_onlyfans:
                self.add_role(onlyfans_role)

            ## Conversation things##
            self.sexed_count = 0

            self.training_log = defaultdict(int) #Contains a list of Trainable.training_tag's that this person has had trained already, which is used to increase the cost of future training in similar things.

        def __call__(self, what, *args, **kwargs): #Required to play nicely with statement equivalent say() when passing only Peron object.
            new_what = self.personalise_text(what) #keep the old what as a reference in case we need it.

            if not persistent.text_effects:
                self.char(new_what, *args, **kwargs)
                return

            new_colour = Color(self.what_color) #Multiple sections may modify the colour of the entire string, so we apply it once at the end.

            #Tags that are applied are generally applied to the inner most parts up here, more general as we go down.
            if self.has_role(trance_role): #Desaturate her dialogue as she falls deeper into a trance.
                if self.has_exact_role(trance_role):
                    new_colour = new_colour.multiply_hsv_saturation(0.7)
                elif self.has_exact_role(heavy_trance_role):
                    new_colour = new_colour.multiply_hsv_saturation(0.4)
                elif self.has_exact_role(very_heavy_trance_role):
                    new_colour = new_colour.multiply_hsv_saturation(0.1)

            flattened_phrase = remove_punctuation(what).lower() #Strip the entire phrase so we can check for individual words.
            if "knocked up" in new_what.lower():
                if self.arousal > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_role(breeder_role):
                    start_index = new_what.lower().find("knocked up")
                    start_substring = new_what[start_index:start_index + len("knocked up")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "knock me up" in new_what.lower():
                if self.arousal > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_role(breeder_role):
                    start_index = new_what.lower().find("knock me up")
                    start_substring = new_what[start_index:start_index + len("knock me up")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "preg me" in new_what.lower():
                if self.arousal > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_role(breeder_role):
                    start_index = new_what.lower().find("preg me")
                    start_substring = new_what[start_index:start_index + len("preg me")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "oh god" in new_what.lower():
                if self.arousal > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_role(breeder_role):
                    start_index = new_what.lower().find("oh god")
                    start_substring = new_what[start_index:start_index + len("oh god")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "oh my god" in new_what.lower():
                if self.arousal > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_role(breeder_role):
                    start_index = new_what.lower().find("oh my god")
                    start_substring = new_what[start_index:start_index + len("oh my god")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)


            temp_what = ""
            for word in new_what.split(): #Per word modifications
                flattened_word = remove_punctuation(word).lower() #Stripped and lower case for easy comparison, we use the full raw word (including punctaiton) for replacement.
                modified_word = False
                effect_strength = str(int(6*(self.arousal/self.max_arousal)) + 2) #If an effect triggers this scales the effect with arousal.
                if word[0] == "{" and word [-1] == "}":
                    pass #Don't do anything to tags.

                elif flattened_word == "cum" or flattened_word == "cumming": #Strip punctuation, avoids us catching phrases like "cumming" and only shaking the front.
                    if self.arousal > (40 - 10*(self.get_opinion_score("drinking cum")+self.get_opinion_score("being covered in cum")+self.get_opinion_score("cum facials")+self.get_opinion_score("creampies"))):
                        modified_word = True
                        cum_color = Color("#e5e5d6")

                        word_replace = self.wrap_string(word, the_colour = cum_color, the_font = "fonts/plasdrip.ttf")
                        word_replace = "{atl=0.3,drop_text~#~ 2.0, bounce_text~" + effect_strength + "}" + word_replace + "{/atl}"
                        temp_what += word_replace + " "

                elif flattened_word == "cock" or flattened_word == "dick":
                    if self.arousal > (40 - 10*(self.get_opinion_score("big dicks"))):
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour, size_mod = effect_strength)
                        word_replace = "{sc=1}{bt=" + effect_strength + "}" + word_replace + "{/bt}{/sc}"
                        temp_what += word_replace + " "

                elif flattened_word == "pussy" or flattened_word == "vagina" or flattened_word == "cunt":
                    if self.arousal > (50):
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour)
                        word_replace = "{bt=" + effect_strength + "}" + word_replace + "{/bt}"
                        temp_what += word_replace + " "

                elif any(flattened_word == target_word for target_word in ["tit","tits","boob","boobs","breast","breasts","mommy milkers"]):
                    if self.arousal > 40 - 10*self.get_opinion_score("showing her tits"):
                        modified_word = True
                        tit_effect_strength = str(int(6*(self.arousal/self.max_arousal)) + Person.rank_tits(self.tits))
                        word_replace = self.wrap_string(word, the_colour = new_colour)
                        word_replace = "{atl=bounce_text~" + tit_effect_strength + "}" + word_replace + "{/atl}"
                        temp_what += word_replace + " "

                elif flattened_word == "fuck":
                    if self.arousal > 60:
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour, size_mod = effect_strength)
                        temp_what += word_replace + " "

                elif flattened_word == "pregnant" or flattened_word == "bred" or flattened_word == "breed": #TODO: Add a word effect that swells through the middle?
                    if self.arousal > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_role(breeder_role):
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour, size_mod = effect_strength)
                        word_replace = "{sc=1}" + word_replace + "{/sc}"
                        temp_what += word_replace + " "

                if not modified_word:
                    temp_what += word + " "

            new_what = temp_what #[:-1] #STrip the last character, which is an unused space.
            new_what = self.wrap_string(new_what, the_colour = new_colour)

            self.char(new_what, *args, **kwargs)

        def wrap_string(self, string, the_colour = None, the_font = None, size_mod = None): #Useful for wrapping a piece of advanced tag dialogue with the proper font, colour, style.
            return_string = string
            if the_colour is None:
                the_colour = self.what_color.hexcode
            else:
                the_colour = the_colour.hexcode

            if the_font is None:
                the_font = self.who_font
            return_string = "{color=" + the_colour + "}" + return_string + "{/color}"
            return_string = "{font=" + the_font + "}" + return_string + "{/font}" #Then set the font
            if size_mod is not None:
                size_string = str(size_mod)
                if size_mod > 0:
                    size_string = "+" + size_string
                return_string = "{size=" + size_string + "}" + return_string + "{/size}"
            #return_string = "{=general_dialogue_style}" + return_string + "{/=general_dialogue_style}"
            return return_string

        @property
        def identifier(self):
            if not hasattr(self, "_identifier"):
                self._identifier = hashlib.md5(self.name + self.last_name + str(self.age)).hexdigest()
            return self._identifier

        @property
        def location(self): # Check what location a person is in e.g the_person.location == downtown. Use to trigger events?
            location = next((x for x in list_of_places if self in x.people), None)
            return (location if location else self.home) # fallback location for person is home

        @property
        def expression_images(self):
            global emotion_images_dict
            return emotion_images_dict[self.skin][self.face_style]

        @property
        def home(self):
            if not hasattr(self, "_home"):
                self._home = None
            return next((x for x in list_of_places if x.identifier == self._home), None)

        @home.setter
        def home(self, value):
            if isinstance(value, Room):
                self._home = value.identifier
            else:
                self._home = None

        @property
        def fname(self):
            return self.create_formatted_title(self.name)

        @property
        def work(self):
            if not hasattr(self, "_work"):
                self._work = None
            return next((x for x in list_of_places if x.identifier == self._work), None)

        @work.setter
        def work(self, value):
            if isinstance(value, Room):
                self._work = value.identifier
            else:
                self._work = None

        def has_limited_time_event(self, the_event):
            if isinstance(the_event, Action):
                return any(x for x in self.on_room_enter_event_list + self.on_talk_event_list if x == the_event)
            if isinstance(the_event, basestring):
                return any(x for x in self.on_room_enter_event_list + self.on_talk_event_list if x.effect == the_event)
            return False

        def generate_home(self, set_home_time = True): #Creates a home location for this person and adds it to the master list of locations so their turns are processed.
            # generate new home location if we don't have one
            start_home = self.home
            if not start_home:
                start_home = Room(self.name + " " + self.last_name + " home", self.name + " " + self.last_name + " home", [], standard_house_backgrounds, [make_wall(), make_floor(), make_couch(), make_window()],[],[],False,[0.5,0.5], visible = False, hide_in_known_house_map = False, lighting_conditions = standard_indoor_lighting)

            # add home location to list of places, before assignment
            if not start_home in list_of_places:
                list_of_places.append(start_home)

            self.home = start_home

            if set_home_time:
                self.set_schedule(self.home, the_times = [0,4])
            return self.home

        def generate_daughter(self, force_live_at_home = False): #Generates a random person who shares a number of similarities to the mother
            age = renpy.random.randint(18, self.age-16)

            if renpy.random.randint(0,100) < 60:
                if self.body_type == "standard_preg_body":
                    body_type = self.event_triggers_dict.get("pre_preg_body", "standard_body")
                else:
                    body_type = self.body_type

            else:
                body_type = None

            if renpy.random.randint(0,100) < 40: #Slightly lower for facial similarities to keep characters looking distinct
                face_style = self.face_style
            else:
                face_style = None

            if renpy.random.randint(0,100) < 60: #60% of the time they share hair colour
                hair_colour = self.hair_colour
            else:
                hair_colour = None

            if renpy.random.randint(0,100) < 60: # 60% they share the same breast size
                tits = self.tits
            else:
                tits = None

            if renpy.random.randint(0,100) < 60: #Share the same eye colour
                eyes = self.eyes
            else:
                eyes = None

            if renpy.random.randint(0,100) < 60: #Have heights that roughly match (but not exactly, and readjusted for the general scaling factor.)
                height = (self.height/0.8) * (renpy.random.randint(95,105)/100.0)
                if height > 1.0:
                    height = 1.0
                elif height < 0.8:
                    height = 0.8
            else:
                height = None

            if renpy.random.randint(0,100) < 85 - age or force_live_at_home: #It is less likely she lives at home the older she is.
                start_home = self.home
            else:
                start_home = None


            the_daughter = create_random_person(last_name = self.last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
                hair_colour = hair_colour, skin = self.skin, eyes = eyes, start_home = start_home)

            if start_home is None:
                the_daughter.generate_home()
            else:
                the_daughter.set_schedule(the_location = start_home, the_times = [0,4])

            the_daughter.home.add_person(the_daughter)

            for sister in town_relationships.get_existing_children(self): #First find all of the other kids this person has
                town_relationships.update_relationship(the_daughter, sister, "Sister") #Set them as sisters

            town_relationships.update_relationship(self, the_daughter, "Daughter", "Mother") #Now set the mother/daughter relationship (not before, otherwise she's a sister to herself!)

            return the_daughter


        def run_turn(self):
            self.change_energy(20, add_to_log = False)

            remove_list = []
            for serum in self.serum_effects: #Compute the effects of all of the serum that the girl is under.
                serum.run_on_turn(self) #Run the serum's on_turn funcion if it has one.
                if serum.duration_expired(): #Returns true if the serum effect is suppose to expire in this time, otherwise returns false. Always updates duration counter when called.
                    remove_list.append(serum) #Use a holder "remove" list to avoid modifying list while iterating.

            for serum in remove_list:
                serum.run_on_remove(self)
                self.serum_effects.remove(serum)

            # Check for serum overdoses after expired effects have been removed.
            over_tolerance_count = len(self.serum_effects) - self.serum_tolerance
            if over_tolerance_count > 0:
                self.change_happiness(over_tolerance_count*-5, add_to_log = False)
                self.add_situational_slut("over serum tolerance", over_tolerance_count*-5, "My body feels strange...")
                self.add_situational_obedience("over serum tolerance", over_tolerance_count*-5, "My body feels strange...")
            else:
                self.clear_situational_slut("over serum tolerance")
                self.clear_situational_obedience("over serum tolerance")

            if self.lactation_sources > 0: #She'll have milky tits, which can be milked in some cases
                self.event_triggers_dict["max_milk_in_breasts"] = Person.rank_tits(self.tits) * 2 #Max milk is determind by tit size
                self.event_triggers_dict["milk_in_breasts"] = self.event_triggers_dict.get("milk_in_breasts", 0) + Person.rank_tits(self.tits) * self.lactation_sources * 0.2
                if self.event_triggers_dict.get("milk_in_breasts",0) > self.event_triggers_dict.get("max_milk_in_breasts",0):
                    self.event_triggers_dict["milk_in_breasts"] = self.event_triggers_dict.get("max_milk_in_breasts",0)

            else:
                self.event_triggers_dict["max_milk_in_breasts"] = 0

            for a_role in self.special_role:
                a_role.run_turn(self)



        def run_move(self,location): #Move to the apporpriate place for the current time unit, ie. where the player should find us.

            #Move the girl the appropriate location on the map. For now this is either a division at work (chunks 1,2,3) or downtown (chunks 0,5). TODO: add personal homes to all girls that you know above a certain amount.
            for serum in self.serum_effects: #Compute the effects of all of the serum that the girl is under.
                serum.run_on_move(self) #Run the serum's on_move function if one exists


            self.sexed_count = 0 #Reset the counter for how many times you've been seduced, you might be seduced multiple times in one day!

            if time_of_day == 0: #It's a new day, get a new outfit out to wear!
                self.planned_outfit = self.wardrobe.decide_on_outfit(self.sluttiness)
                self.apply_outfit(self.planned_outfit)
                self.planned_uniform = None

            destination = self.get_destination()
            if destination: #We have somewhere scheduled to be for this turn. Let's move over there.
                location.move_person(self, destination) #Always go where you're scheduled to be.
                if self.is_at_work(): #We're going to work.
                    if self.should_wear_uniform(): #Get a uniform if we should be wearing one.
                        self.wear_uniform()
                        self.change_happiness(self.get_opinion_score("work uniforms"),add_to_log = False)
                        if self.planned_uniform and self.planned_uniform.slut_requirement > self.sluttiness*0.75: #A skimpy outfit/uniform is defined as the top 25% of a girls natural sluttiness.
                            self.change_slut(self.get_opinion_score("skimpy uniforms"), 30, add_to_log = False)

                elif destination == self.home:
                    self.apply_outfit(self.planned_outfit)

                #NOTE: There is no else here because all of the destinations should be set. If it's just a location they travel there and that's the end of it.

            else:
                #She finds somewhere to burn some time
                self.apply_outfit(self.planned_outfit)
                location.move_person(self, get_random_from_list([x for x in list_of_places if x.public]))

            #We do uniform/outfit checks in run move because it happens at the _start_ of the turn. The girl looks forward to wearing her outfit (or dreads it) rather than responds to actually doing it.
            if self.outfit and self.planned_outfit.slut_requirement > self.sluttiness*0.75: #A skimpy outfit is defined as the top 25% of a girls natural sluttiness.
                self.change_slut(self.get_opinion_score("skimpy outfits"), 30, add_to_log = False)
            elif self.outfit and self.planned_outfit.slut_requirement < self.sluttiness*0.25: #A conservative outfit is defined as the bottom 25% of a girls natural sluttiness.
                self.change_happiness(self.get_opinion_score("conservative outfits"), add_to_log = False)

            if self.outfit.tits_available() and self.outfit.tits_visible() and self.outfit.vagina_available() and self.outfit.vagina_visible():
                self.change_slut(self.get_opinion_score("not wearing anything"), 50, add_to_log = False)

            if not self.outfit.wearing_bra() or not self.outfit.wearing_panties(): #We need to determine how much underwear they are not wearing. Each piece counts as half, so a +2 "love" is +1 slut per chunk.
                underwear_bonus = 0
                if not self.outfit.wearing_bra():
                    underwear_bonus += self.get_opinion_score("not wearing underwear")
                if not self.outfit.wearing_panties():
                    underwear_bonus += self.get_opinion_score("not wearing underwear")
                underwear_bonus = __builtin__.int(underwear_bonus/2.0) #I believe this rounds towards 0. No big deal if it doesn't, very minor detail.
                self.change_slut(underwear_bonus, 40, add_to_log = False)

            if self.outfit.tits_visible():
                self.change_slut(self.get_opinion_score("showing her tits"), 60, add_to_log = False)
            if self.outfit.vagina_visible():
                self.change_slut(self.get_opinion_score("showing her ass"), 60, add_to_log = False)

            for event_list in [self.on_room_enter_event_list, self.on_talk_event_list]: #Go through both of these lists and curate them, ie trim out events that should have expired.
                removal_list = [] #So we can iterate through without removing and damaging the list.
                for an_action in event_list:
                    if isinstance(an_action, Limited_Time_Action): #It's a LTA holder, so it has a turn counter
                        an_action.turns_valid += -1
                        if an_action.turns_valid <= 0:
                            removal_list.append(an_action)

                for action_to_remove in removal_list:
                    event_list.remove(action_to_remove)

            for a_role in self.special_role:
                a_role.run_move(self)

        def run_day(self): #Called at the end of the day.
            #self.outfit = self.wardrobe.decide_on_outfit(self.sluttiness) #Put on a new outfit for the day!

            self.change_energy(.6 * self.max_energy, add_to_log = False)
            self.change_novelty(1, add_to_log = False)

            #Now we will normalize happiness towards 100 over time. Every 5 points of happiness above or below 100 results in a -+1 per turn, rounded towards 0.
            hap_diff = self.happiness - 100
            hap_diff = __builtin__.int(hap_diff/5.0) #python defaults to truncation towards 0, so this gives us the number we should be changing our happinss by
            self.change_happiness(-hap_diff, add_to_log = False) #Apply the change

            if self.arousal > (self.max_arousal / 2.0): #If her arousal is high she masturbates at night, generating a small amount of sluttiness #TODO: Have this trigger an LTE where girls might be getting off when you walk in.
                self.arousal = 0
                if self.get_opinion_score("masturbating") > 0: # Masturbating turns her on, so just getting off turns her back on!
                    self.arousal = 15*self.get_opinion_score("masturbating")
                self.change_happiness(5+5*self.get_opinion_score("masturbating"), add_to_log = False)
                self.run_orgasm(show_dialogue = False, trance_chance_modifier = self.get_opinion_score("masturbating"), add_to_log = False, fire_event = False)

            remove_list = []
            for serum in self.serum_effects:
                serum.run_on_turn(self) #If a run_on_turn is called and the serum has expired no effects are calculated, so we can safely call this as many times as we want.
                serum.run_on_turn(self) #Night is 3 turn chunks, but one is already called when time progresses. Run serums twice more, and if we've gotten here we also run the on day function.
                serum.run_on_day(self) #Serums that effect people at night must effect two of the three turns.
                if serum.duration_expired(): #Night is 3 segments, but 1 is allready called when run_turn is called.
                    remove_list.append(serum)

            for serum in remove_list:
                serum.run_on_remove(self)
                self.serum_effects.remove(serum)

            for infraction in self.infractions:
                infraction.days_existed += 1
                if infraction.days_existed > infraction.days_valid:
                    self.remove_infraction(infraction)


            if day%7 == 0: #If the new day is Monday
                self.change_happiness(self.get_opinion_score("Mondays")*10, add_to_log = False)

            elif day%7 == 4: #If the new day is Friday
                self.change_happiness(self.get_opinion_score("Fridays")*10, add_to_log = False)

            elif day%7 == 5 or day%7 == 6: #If the new day is a weekend day
                self.change_happiness(self.get_opinion_score("the weekend")*10, add_to_log = False)

            for a_role in self.special_role:
                a_role.run_day(self)

        def get_display_colour_code(self, saturation = 1.0, given_alpha = 1.0):
            the_colour = Color(self.char.what_args["color"])
            the_colour = the_colour.multiply_hsv_saturation(saturation)
            the_colour = the_colour.multiply_value(saturation)
            the_colour = the_colour.replace_opacity(given_alpha)

            return the_colour.hexcode


        def build_person_displayable(self,position = None, emotion = None, special_modifier = None, lighting = None): #Encapsulates what is done when drawing a person and produces a single displayable.
            if position is None:
                position = self.idle_pose #Easiest change is to call this and get a random standing posture instead of a specific idle pose. We redraw fairly frequently so she will change position frequently.

            displayable_list = [] # We will be building up a list of displayables passed to us by the various objects on the person (their body, clothing, etc.)

            if emotion is None:
                emotion = self.get_emotion()

            forced_special_modifier = self.outfit.get_forced_modifier()
            if forced_special_modifier is not None:
                special_modifier = forced_special_modifier # Overrides all other things, supports people with ball gags always having an open mouth (mechanically, not emotionally)

            x_size, y_size = position_size_dict.get(position)

            displayable_list.append(self.body_images.generate_item_displayable(self.body_type,self.tits,position,lighting)) #Add the body displayable
            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
            displayable_list.append(self.pubes_style.generate_item_displayable(self.body_type,self.tits, position, lighting = lighting)) #Add in her pubes. #TODO: See if we need to mask this with her body profile for particularly bush-y bushes to prevent clothing overflow.

            displayable_list.extend(self.outfit.generate_draw_list(self,position,emotion,special_modifier, lighting = lighting)) #Get the displayables for everything we wear. Note that extnsions do not return anything because they have nothing to show.
            displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position, lighting = lighting)) #Get hair
            #NOTE: Positional modifiers like xanchor that expect pixles need to be given ints, they do not auto convert from floats.

            composite_list = [(x_size,y_size)] #Now we build a list of our parameters, done like this so they are arbitrarily long

            for display in displayable_list:
                if isinstance(display, __builtin__.tuple):
                    composite_list.extend(display)
                else:
                    composite_list.append((0,0)) #Displayables are all handed over as composites with the image centered, so no extra work is needed here.
                    composite_list.append(display) #Append the actual displayable

            character_composite = Composite(*composite_list)

            if persistent.vren_display_pref == "Float" or persistent.vren_display_pref == "Frame":
                character_raw_body = im.Composite((x_size, y_size),
                    (0,0), self.body_images.generate_raw_image(self.body_type,self.tits,position),
                    #(0,0), self.expression_images.generate_raw_image(position, emotion, special_modifier = special_modifier),
                    self.hair_style.crop_offset_dict.get(position,(0,0)), self.hair_style.generate_raw_image("standard_body", self.tits, position))

                blurred_image = im.Blur(character_raw_body, 6)
                aura_colour = self.get_display_colour_code()
                recoloured_blur = im.MatrixColor(blurred_image, im.matrix.colorize(aura_colour, aura_colour))

                final_composite = Composite((x_size, y_size), (0,0), recoloured_blur, (0,0), character_composite)
            else:
                final_composite = character_composite

            final_image = Flatten(final_composite) # Create a composite image using all of the displayables
            return final_image

        def build_weight_mask(self, the_animation, position, animation_effect_strength): #Builds a weight mask displayable that highlights the sections of a character that should be animated.
            x_size, y_size = position_size_dict.get(position)

            composite_components = []
            region_weight_items_dict = the_animation.get_weight_items()
            for region_weight_name in region_weight_items_dict: #Goes through each region ie. "breasts", "butt", and others to come, and applies the animation strength, the personal region strength, and animation region strength
                the_weight_item = region_weight_items_dict[region_weight_name]
                composite_components.append(the_weight_item.crop_offset_dict.get(position, (0,0)))
                region_weight_modifier = animation_effect_strength * self.personal_region_modifiers.get(region_weight_name, 1) * the_animation.innate_animation_strength * the_animation.region_specific_weights.get(region_weight_name, 1)
                if region_weight_modifier > 1:
                    region_weight_modifier = 1

                region_brightness_matrix = im.matrix.brightness(-1 + region_weight_modifier)
                region_mask = the_weight_item.generate_raw_image(self.body_type, self.tits, position)
                region_mask = im.MatrixColor(region_mask, region_brightness_matrix)
                composite_components.append(region_mask)

            the_mask_composite = im.Composite((x_size, y_size), *composite_components)

            weight_mask = im.Blur(the_mask_composite, 2)

            return weight_mask

        def draw_person(self,position = None, emotion = None, special_modifier = None, show_person_info = True, lighting = None, background_fill = "auto", the_animation = None, animation_effect_strength = 1.0,
            draw_layer = "solo", display_transform = None, extra_at_arguments = None, display_zorder = None, wipe_scene = True): #Draw the person, standing as default if they aren't standing in any other position
            #log_message(self.name + " | Start | " + str(time.time()))

            if position is None:
                position = self.idle_pose #Easiest change is to call this and get a random standing posture instead of a specific idle pose. We redraw fairly frequently so she will change position frequently.

            if the_animation is None:
                the_animation = self.idle_animation

            if not can_use_animation():
                the_animation = None

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            character_image = self.build_person_displayable(position, emotion, special_modifier, lighting) #The static 2D displayable.

            if not the_animation is None:
                weight_mask = self.build_weight_mask(the_animation, position, animation_effect_strength)

            else:
                weight_mask = Solid("#000000") #Black mask = no influence.

            x_size, y_size = position_size_dict[position]

            animated_image = ShaderPerson(character_image, weight_mask)
            if background_fill == "auto":
                if persistent.vren_display_pref == "Frame":
                    background_fill = self.get_display_colour_code(saturation = 0.8, given_alpha = 0.6) # Sets it to be partially transparent.
                else:
                    background_fill = None

            if background_fill is not None: #If a background colour is given we add a solid to the back and a frame around the entire thing.
                bg_colour =  Composite((x_size, y_size), (0,0), Solid(background_fill))
                image_frame = Composite((x_size, y_size), (0,0), Frame("/gui/Character_Window_Frame.png", 12, 12))

            if display_transform is None:
                display_transform = character_right

            frame_at_arguments = [display_transform, scale_person(self.height)] # A list without basic_bounce to use for the background and the frame.
            at_arguments = [display_transform, scale_person(self.height)]
            if the_animation is not None:
                at_arguments.append(basic_bounce(the_animation))

            if extra_at_arguments:
                if isinstance(extra_at_arguments, list):
                    frame_arguments.extend(extra_at_arguments)
                    at_arguments.extend(extra_at_arguments)
                else:
                    frame_arguments.append(extra_at_arguments)
                    at_arguments.append(extra_at_arguments)
            else:
                extra_at_arguments = []

            if display_zorder is None:
                display_zorder = 0

            character_tag = str(self.character_number)

            self.hide_person()
            if wipe_scene:
                clear_scene() #Make sure no other characters are drawn either.

            if background_fill is not None:
                renpy.show(character_tag+"_bg_fill", at_list=frame_at_arguments, layer=draw_layer, what=bg_colour, zorder = display_zorder, tag=character_tag+"_bg_fill")
            renpy.show(character_tag, at_list=at_arguments, layer=draw_layer, what=animated_image, zorder = display_zorder, tag=character_tag)
            if background_fill is not None:
                renpy.show(character_tag+"_frame", at_list=frame_at_arguments, layer=draw_layer, what=image_frame, zorder = display_zorder, tag=character_tag+"_frame")

            if show_person_info:
                renpy.show_screen("person_info_ui",self)

        def hide_person(self, draw_layer = "solo"): #Hides the person. Makes sure to hide all posible known tags for the character.
            # We keep track of tags used to display a character so that they can always be unique, but still tied to them so they can be hidden
            character_tag = str(self.character_number)
            renpy.hide(character_tag, draw_layer)
            renpy.hide(character_tag+"_extra", draw_layer)
            renpy.hide(character_tag+"_bg_fill", draw_layer)
            renpy.hide(character_tag+"_frame", draw_layer)


        def draw_animated_removal(self, the_clothing, position = None, emotion = None, special_modifier = None, show_person_info = True, lighting = None, background_fill = "auto", the_animation = None, animation_effect_strength = 1.0, half_off_instead = False,
            draw_layer = "solo", display_transform = None, extra_at_arguments = None, display_zorder = None, wipe_scene = True):
            #The new animated_removal method generates two image, one with the clothing item and one without. It then stacks them and layers one on top of the other and blends between them.

            if position is None:
                position = self.idle_pose

            if not can_use_animation():
                the_animation = None
            elif the_animation is None:
                the_animation = self.idle_animation

            if background_fill == "auto":
                if persistent.vren_display_pref == "Frame":
                    background_fill = self.get_display_colour_code(saturation = 0.8, given_alpha = 0.6) # Sets it to be partially transparent.
                else:
                    background_fill = None

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            global draw_layers
            if draw_layer not in draw_layers:
                add_draw_layer(draw_layer)

            if display_transform is None:
                display_transform = character_right

            x_size, y_size = position_size_dict[position]

            frame_at_arguments = [display_transform, scale_person(self.height)]
            at_arguments = [display_transform, scale_person(self.height)] #TODO: make sure this works with a None animation.
            if the_animation is not None:
                at_arguments.append(basic_bounce(the_animation))

            if extra_at_arguments:
                if isinstance(extra_at_arguments, list):
                    frame_at_arguments.extend(extra_at_arguments)
                    at_arguments.extend(extra_at_arguments)
                else:
                    frame_at_arguments.append(extra_at_arguments)
                    at_arguments.append(extra_at_arguments)
            else:
                extra_at_arguments = []

            if display_zorder is None:
                display_zorder = 0

            if wipe_scene:
                clear_scene()

            if show_person_info:
                renpy.show_screen("person_info_ui",self)

            bottom_displayable = Flatten(self.build_person_displayable(position, emotion, special_modifier, lighting)) #Get the starting image
            if isinstance(the_clothing, list):
                for cloth in the_clothing:
                    if half_off_instead:
                        self.outfit.half_off_clothing(cloth) #Half-off the clothing
                    else:
                        self.outfit.remove_clothing(cloth) #Remove the clothing
            else:
                if half_off_instead:
                    self.outfit.half_off_clothing(the_clothing) #Half-off the clothing
                else:
                    self.outfit.remove_clothing(the_clothing) #Remove the clothing
            top_displayable = self.build_person_displayable(position, emotion, special_modifier, lighting) #Get the top image

            if not the_animation is None:
                weight_mask = self.build_weight_mask(the_animation, position, animation_effect_strength)
            else:
                weight_mask = weight_mask = Solid("#000000") #Black mask = no influence.

            bottom_animation = ShaderPerson(bottom_displayable, weight_mask)
            top_animation = ShaderPerson(top_displayable, weight_mask)

            self.hide_person()
            character_tag = str(self.character_number)

            if background_fill is not None: #If a background colour is given we add a solid to the back and a frame around the entire thing.
                bg_colour =  Composite((x_size, y_size), (0,0), Solid(background_fill))
                renpy.show(character_tag + "_bg_fill", at_list=frame_at_arguments, layer = draw_layer, what = bg_colour, zorder = display_zorder, tag = character_tag + "_bg_fill")

            renpy.show(character_tag, at_list=at_arguments, layer = draw_layer, what = top_animation, zorder = display_zorder, tag = character_tag)
            fade_at_arguments = at_arguments[:]
            fade_at_arguments.append(clothing_fade)
            renpy.show(character_tag + "_extra", at_list=fade_at_arguments, layer = draw_layer, what = bottom_animation, zorder = display_zorder, tag = character_tag + "_extra") #Blend from old to new.

            if background_fill is not None:
                image_frame = Composite((x_size, y_size), (0,0), Frame("/gui/Character_Window_Frame.png", 12, 12))
                renpy.show(character_tag + "_frame", at_list=frame_at_arguments, layer = draw_layer, what = image_frame, zorder = display_zorder, tag = character_tag + "_frame") #Uses an at_list copy that does not include the clothing_fade.
            return

        def get_emotion(self): # Get the emotion state of a character, used when the persons sprite is drawn and no fixed emotion is required.
            if self.arousal>= self.max_arousal:
                return "orgasm"

            elif self.happiness > 100:
                return "happy"

            elif self.happiness < 80:
                if self.love > 0:
                    return "sad"
                else:
                    return "angry"

            else:
                return "default"

        def call_dialogue(self, type, **extra_args): #Passes the parameter along to the persons personality and gets the correct dialogue for the event if it exists in the dict.
            self.personality.get_dialogue(self, type, **extra_args)

        def get_known_opinion_score(self, topic):
            the_topic = self.get_opinion_topic(topic)
            if the_topic is None:
                return 0
            else:
                if the_topic[1]:
                    return the_topic[0]
                else:
                    return 0

        def has_unknown_opinions(self, normal_opinions = True, sexy_opinions = True):
            if normal_opinions:
                for topic in self.opinions:
                    if not self.opinions[topic][1]:
                        return True

            if sexy_opinions:
                for topic in self.sexy_opinions:
                    if not self.sexy_opinions[topic][1]:
                        return True

            return False

        def get_opinion_score(self, topic): #Like get_opinion_topic, but only returns the score and not a tuple. Use this when determining a persons reaction to a relavent event.
            return_value = 0
            if isinstance(topic, list):
                for a_topic in topic:
                    return_value += self.get_opinion_score(a_topic)
            else:
                if topic in self.opinions:
                    return_value += self.opinions[topic][0]

                if topic in self.sexy_opinions:
                    return_value += self.sexy_opinions[topic][0]

            return return_value

        def get_opinion_topics_list(self, include_unknown = True, include_normal = True, include_sexy = True, include_hate = True, include_dislike = True, include_like = True, include_love = True):
            #TODO: Needs unit testing
            opinion_return_list = []
            lists_to_check = []
            if include_normal:
                for topic in self.opinions:
                    if self.opinions[topic][1] or include_unknown:
                        if self.opinions[topic][0] == -2 and include_hate:
                            opinion_return_list.append(topic)
                        elif self.opinions[topic][0] == -1 and include_dislike:
                            opinion_return_list.append(topic)
                        elif self.opinions[topic][0] == 1 and include_like:
                            opinion_return_list.append(topic)
                        elif self.opinions[topic][0] == 2 and include_love:
                            opinion_return_list.append(topic)
            if include_sexy:
                for topic in self.sexy_opinions:
                    if self.sexy_opinions[topic][1] or include_unknown:
                        if self.sexy_opinions[topic][0] == -2 and include_hate:
                            opinion_return_list.append(topic)
                        elif self.sexy_opinions[topic][0] == -1 and include_dislike:
                            opinion_return_list.append(topic)
                        elif self.sexy_opinions[topic][0] == 1 and include_like:
                            opinion_return_list.append(topic)
                        elif self.sexy_opinions[topic][0] == 2 and include_love:
                            opinion_return_list.append(topic)
            return opinion_return_list

        def get_opinion_topic(self, topic): #topic is a string matching the topics given in our random list (ie. "the colour blue", "sports"). Returns a tuple containing the score: -2 for hates, -1 for dislikes, 0 for no opinion, 1 for likes, and 2 for loves, and a bool to say if the opinion is known or not.
            if topic in self.opinions:
                return self.opinions[topic]

            if topic in self.sexy_opinions:
                return self.sexy_opinions[topic]

            return None

        def get_random_opinion(self, include_known = True, include_sexy = False, include_normal = True, only_positive = False, only_negative = False): #Gets the topic string of a random opinion this character holds. Includes options to include known opinions and sexy opinions. Returns None if no valid opinion can be found.
            the_dict = {} #Start our list of valid opinions to be listed as empty

            if include_normal: #if we include normal opinions build a dict out of the two
                the_dict = dict(the_dict, **self.opinions)

            if include_sexy: #If we want sexy opinions add them in too.
                the_dict = dict(the_dict, **self.sexy_opinions)


            known_keys = []
            if not include_known: #If we do not want to talk about known values
                for k in the_dict: #Go through each value in our combined normal and sexy opinion dict
                    if the_dict[k][1]: #Check if we know about it...
                        known_keys.append(k) #We build a temporary list of keys to remove because otehrwise we are modifying the dict while we traverse it.
                for del_key in known_keys:
                    del the_dict[del_key]

            remove_keys = []
            if only_positive or only_negative: # Let's us filter opinions so they only include possitive or negative ones.
                if only_positive:
                    for k in the_dict:
                        if self.get_opinion_score(k) < 0:
                            remove_keys.append(k)

                if only_negative:
                    for k in the_dict:
                        if self.get_opinion_score(k) > 0:
                            remove_keys.append(k)

                for del_key in remove_keys:
                    del the_dict[del_key]

            if the_dict:
                return get_random_from_list(the_dict.keys()) #If we have something in the list we can return the topic string we used as a key for it. This can then be used with get_opinion_score to get the actual opinion
            else:
                return None #If we have nothing return None, make sure to deal with this when we use this function.


        def discover_opinion(self, topic, add_to_log = True): #topic is a string matching the topics given in our random list (ie. "the colour blue"). If the opinion is in either of our opinion dicts we will set it to known, otherwise we do nothing. Returns True if the opinion was updated, false if nothing was changed.
            display_name = self.create_formatted_title("???")
            updated = False
            if self.title:
                display_name = self.title
            if topic in self.opinions:
                if not self.opinions[topic][1]:
                    updated = True
                    if add_to_log and self.title is not None:
                        mc.log_event("Discovered: " + display_name + " " + opinion_score_to_string(self.opinions[topic][0]) + " " + topic,"float_text_grey")
                self.opinions[topic][1] = True

            if topic in self.sexy_opinions:
                if not self.sexy_opinions[topic][1]:
                    updated = True
                    if add_to_log and self.title is not None:
                        mc.log_event("Discovered: " + display_name + " " + opinion_score_to_string(self.sexy_opinions[topic][0]) + " " + topic,"float_text_grey")
                self.sexy_opinions[topic][1] = True

            return updated

        def set_opinion(self, topic, strength, known = False): #override function to set an opinion to a known value, mainly used to set up characters before they are introduced
            is_sexy_opinion = False
            if topic in self.get_sexy_opinions_list():
                is_sexy_opinion = True

            if not strength == 0:
                if is_sexy_opinion:
                    self.sexy_opinions[topic] = [strength, known]
                else:
                    self.opinions[topic] = [strength, known]

            else:
                if topic in self.opinions:
                    self.opinions.pop(topic)
                if topic in self.sexy_opinions:
                    self.sexy_opinions.pop(topic)



        def strengthen_opinion(self, topic, add_to_log = True):
            display_string = ""

            old_opinion = self.get_opinion_topic(topic)
            if old_opinion is None: #You cannot strengthen an opinion of 0, for that make a new one entirely.
                return False

            updated = False
            if old_opinion[0] == 1 or old_opinion[0] == -1:
                updated = True
                new_opinion_value = 2*old_opinion[0]
                if topic in self.opinions:
                    self.opinions[topic] = [new_opinion_value, old_opinion[1]]
                else:
                    self.sexy_opinions[topic] = [new_opinion_value, old_opinion[1]]
                display_string += opinion_score_to_string(self.get_opinion_score(topic)) + " " + topic

            if add_to_log and display_string:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                display_string = "Opinion Strengthened: " + display_name + " now " + display_string
                mc.log_event(display_string, "float_text_grey")

            return updated

        def weaken_opinion(self, topic, add_to_log = True):
            display_string = ""

            old_opinion = self.get_opinion_topic(topic)
            if old_opinion is None: #You cannot strengthen an opinion of 0, for that make a new one entirely.
                return False

            updated = False
            if old_opinion[0] == 2 or old_opinion[0] == -2:
                updated = True
                new_opinion_value = int(old_opinion[0]/2)
                if topic in self.opinions:
                    self.opinions[topic] = [new_opinion_value, old_opinion[1]]
                else:
                    self.sexy_opinions[topic] = [new_opinion_value, old_opinion[1]]
                display_string += opinion_score_to_string(self.get_opinion_score(topic)) + " " + topic

            else: #ie it was -1 or 1, because 0 already returned
                updated = True
                if topic in self.opinions:
                    self.opinions.pop(topic)
                elif topic in self.sexy_opinions:
                    self.sexy_opinions.pop(topic)
                display_string += opinion_score_to_string(self.get_opinion_score(topic)) + " " + topic

            if add_to_log and display_string:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                display_string = "Opinion Weakened: " + display_name + " now " + display_string
                mc.log_event(display_string, "float_text_grey")

            return updated

        def create_opinion(self, topic, start_positive = True, start_known = True, add_to_log = True):
            start_value = 1
            if not start_positive:
                start_value = -1 #Determines if the opinion starts as like or dislike.
            if not self.get_opinion_score(topic) == 0: #She already has an opinion
                return False

            is_sexy_opinion = False
            if topic in self.get_sexy_opinions_list():
                is_sexy_opinion = True

            opinion_tuple = [start_value, start_known]
            if is_sexy_opinion:
                self.sexy_opinions[topic] = opinion_tuple
            else:
                self.opinions[topic] = opinion_tuple

            if add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                mc.log_event("Opinion Inspired: " + display_name + " now " + opinion_score_to_string(self.get_opinion_score(topic)) + " " + topic, "float_text_grey")

            return True

        def has_taboo(self, the_taboos):
            if the_taboos is None:
                return False

            if isinstance(the_taboos, basestring):
                the_taboos = [the_taboos]

            for a_taboo in the_taboos: #We also handle lists, if we what to check if someone has _any_ of several taboos at once
                if a_taboo not in self.broken_taboos:
                    return True
            return False

        def has_broken_taboo(self, the_taboos):
            if the_taboos is None:
                return False

            if isinstance(the_taboos, basestring):
                the_taboos = [the_taboos]

            for a_taboo in the_taboos: #We also handle lists, if we wnat to check if someone has _any_ of several taboos at once
                if a_taboo in self.broken_taboos:
                    return True
            return False

        def break_taboo(self, the_taboo, add_to_log = True, fire_event = True):
            if the_taboo in self.broken_taboos:
                return False

            self.broken_taboos.append(the_taboo)
            self.change_novelty(5, add_to_log = add_to_log)

            if add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                mc.log_event(" Taboo broken with " + display_name + "!", "float_text_red")

            if fire_event:
                mc.listener_system.fire_event("girl_taboo_break", the_taboo = the_taboo)
            return True

        def restore_taboo(self, the_taboo, add_to_log = True):
            if not the_taboo in self.broken_taboos:
                return False

            while the_taboo in self.broken_taboos:
                self.broken_taboos.remove(the_taboo)

            if add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                mc.log_event(" Taboo reasserted with " + display_name + "!", "float_text_red")
            return True

        def pick_position_comment(self, the_report): #Takes a report and has the person pick the most notable thing out of it. Generally used to then have them comment on it.
            highest_slut_position = None
            highest_slut_opinion = 0
            for position in the_report.get("positions_used", []):
                slut_opinion = position.slut_requirement
                if position.opinion_tags is not None:
                    for opinion_tag in position.opinion_tags:
                        slut_opinion += 5*self.get_opinion_score(opinion_tag)
                if highest_slut_position is None or slut_opinion > highest_slut_opinion:
                    highest_slut_position = position
                    highest_slut_opinion = slut_opinion

            return highest_slut_position

        def add_outfit(self,the_outfit, outfit_type = "full"):
            if outfit_type == "under":
                self.wardrobe.add_underwear_set(the_outfit)
            elif outfit_type == "over":
                self.wardrobe.add_overwear_set(the_outfit)
            else: #outfit_type = full
                self.wardrobe.add_outfit(the_outfit)

        def set_outfit(self,new_outfit):
            if new_outfit is not None:
                self.planned_outfit = new_outfit.get_copy() #Get a copy to return to when we are done.
                self.apply_outfit(new_outfit)

        def set_uniform(self,uniform, wear_now = False):
            if uniform is not None:
                self.planned_uniform = uniform.get_copy()
                if wear_now:
                    self.wear_uniform()

        def apply_outfit(self, the_outfit = None, ignore_base = False, update_taboo = False): #Hand over an outfit, we'll take a copy and apply it to the person, along with their base accessories unless told otherwise.
            if the_outfit is None:
                # put on uniform if required
                if self.should_wear_uniform():
                    self.wear_uniform()
                    return

                the_outfit = self.planned_outfit
                if the_outfit is None:
                    return #We don't have a planned outfit, so trying to return to it makes no sense.
            if ignore_base:
                self.outfit = the_outfit.get_copy()
            else:
                self.outfit = the_outfit.get_copy().merge_outfit(self.base_outfit)

            if update_taboo: #If True, we assume this outfit is being put on or shown to the MC. It can break taboos about showing underwear, tits, pussy.
                self.update_outfit_taboos()

        def update_outfit_taboos(self):
            return_value = False
            if self.outfit.tits_visible():
                if self.break_taboo("bare_tits"):
                    return_value = True
            if self.outfit.vagina_visible():
                if self.break_taboo("bare_pussy"):
                    return_value = True
            if (self.outfit.wearing_panties() and not self.outfit.panties_covered()) or (self.outfit.wearing_bra() and not self.outfit.bra_covered()):
                if self.break_taboo("underwear_nudity"):
                    return_value = True
            return return_value


        def give_serum(self,the_serum_design, add_to_log = True):
            if the_serum_design is None:
                return #We might have handed over no serum because we aren't producing any and a crisis was looking for one, or something similar.
            else:
                the_serum_design = copy.copy(the_serum_design) #Take a copy so we aren't touchinn the reference we are handed.
            self.serum_effects.append(the_serum_design)
            the_serum_design.run_on_apply(self, add_to_log)

        def is_under_serum_effect(self):
            if self.serum_effects:
                return True
            else:
                return False

        def apply_serum_study(self, add_to_log = True): #Called when the person is studied by the MC. Raises mastery level of all traits used in active serums by 0.2
            studied_something = False
            for serum in self.serum_effects:
                for trait in serum.traits:
                    trait.add_mastery(0.2)
                    studied_something = True

            if studied_something and add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                mc.log_event("Observed " + display_name + ", mastery of all active serum traits increased by 0.2", "float_text_blue")

        def change_suggest(self,amount, add_to_log = True): #This changes the base, usually permanent suggest. Use add_suggest_effect to add temporary, only-highest-is-used, suggestion values
            self.suggestibility += amount
            if add_to_log and amount != 0 and self.title:
                mc.log_event(self.title + ": Suggestibility increased permanently by "+ ("+" if amount > 0 else "") + str(amount) + "%", "float_text_blue")

            # Note that suggestibility can be negative, representing someone who is _resistant_ to trances for some reason.

        def add_suggest_effect(self,amount, add_to_log = True):
            if amount > __builtin__.max(self.suggest_bag or [0]):
                self.change_suggest(-__builtin__.max(self.suggest_bag or [0]), add_to_log = False) #Subtract the old max and...
                self.change_suggest(amount, add_to_log = False) #add our new suggest.
                if add_to_log and amount != 0 and self.title:
                    mc.log_event(self.title + ": Suggestibility increased, by " + str(amount), "float_text_blue")
            else:
                if add_to_log and amount != 0 and self.title:
                    mc.log_event(self.title + ": Suggestibility " + str(amount) + " lower than current " + str(self.suggestibility) + " amount. Suggestibility unchanged.", "float_text_blue")
            self.suggest_bag.append(amount) #Add it to the bag, so we can check to see if it is max later.


        def remove_suggest_effect(self,amount):
            if amount in self.suggest_bag: # Avoid removing the "amount" if we don't actually have it in the bag.
                self.change_suggest(- __builtin__.max(self.suggest_bag or [0]), add_to_log = False) #Subtract the max
                self.suggest_bag.remove(amount)
                self.change_suggest(__builtin__.max(self.suggest_bag or [0]), add_to_log = False) # Add the new max. If we were max, it is now lower, otherwie it cancels out.

        def change_happiness(self,amount, add_to_log = True):
            self.happiness += amount*self.get_trance_multiplier()
            if self.happiness < 0:
                self.happiness = 0

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string = ("+" if amount > 0 else "")+ str(amount) + " Happiness"
                if self.get_trance_multiplier() != 1:
                    log_string += "\nChange amplified by " + str(int((self.get_trance_multiplier()*100)-100)) + "% due to trance"
                mc.log_event(display_name + ": " + log_string, "float_text_yellow")

        def change_love(self, amount, max_modified_to = None, add_to_log = True):
            amount = __builtin__.int(amount)
            if max_modified_to is not None and self.love + amount > max_modified_to:
                amount = max_modified_to - self.love
                if amount < 0: #Never subtract love because of a cap, only limit how much they gain.
                    amount = 0

            if self.love + amount < -100:
                amount = -100 - self.love
            elif self.love + amount > 100:
                amount = 100 - self.love

            self.love += amount

            if add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                if amount == 0:
                    log_string = "Love limit reached for interaction"
                else:
                    log_string = ("+" if amount > 0 else "") + str(amount) + " Love"
                mc.log_event(display_name + ": " + log_string, "float_text_pink")
            return amount

        def change_slut(self, amount, max_modified_to = None, add_to_log = True):
            if max_modified_to and self.sluttiness + amount > max_modified_to:
                amount = max_modified_to - self.sluttiness
                if amount < 0:
                    amount = 0

            if self.sluttiness + amount < 0:
                amount = -self.sluttiness
            elif self.sluttiness + amount > 300:
                amount = 300 - self.sluttiness

            self.sluttiness += amount

            if add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                if amount == 0:
                    log_string = "No Effect on Sluttiness"
                else: #It is exactly 0
                    log_string = ("+" if amount > 0 else "") + str(amount) + " Sluttiness"
                mc.log_event(display_name + ": " + log_string, "float_text_pink")
            return amount

        def change_slut_temp(self, amount, add_to_log = True):
            return self.change_slut(amount, add_to_log = add_to_log)
        def change_slut_core(self, amount, add_to_log = True, fire_event = True):
            return self.change_slut(amount, add_to_log = add_to_log)

        def add_situational_slut(self, source, amount, description = ""):
            self.situational_sluttiness[source] = (amount,description)

        def clear_situational_slut(self, source):
            self.add_situational_slut(source, 0) #We don't actually ever care if we remove the key, we just want to set the amount to 0.

        def add_situational_obedience(self, source, amount, description = ""):
            if source in self.situational_obedience:
                difference = amount - self.situational_obedience[source][0]
                self.change_obedience(difference, add_to_log = False)
            else:
                self.change_obedience(amount, add_to_log = False)
            self.situational_obedience[source] = (amount,description)

        def clear_situational_obedience(self, source):
            self.add_situational_obedience(source, 0)

        def change_obedience(self,amount, add_to_log = True):
            if self.obedience + amount < 0:
                amount = -self.obedience
            elif self.obedience + amount > 300:
                amount = 300 - self.obedience

            self.obedience += amount

            if add_to_log and amount != 0: #If we don't know the title don't add it to the log, because we know nothing about the person
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title

                log_string = display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Obedience"
                mc.log_event(log_string,"float_text_grey")
            return amount

        def change_cha(self, amount, add_to_log = True):
            self.charisma += self.charisma_debt #Set our charisma to be our net score
            self.charisma_debt = 0 #We are currently holding no stat debt.

            self.charisma += amount #Adjust our stat now, may be positive or negative.
            if self.charisma < 0:
                self.charisma_debt = self.charisma #If we are less than 0 store it as a debt.
                self.charisma = 0

            if amount != 0 and add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title

                log_string = display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Charisma"
                mc.log_event(log_string, "float_text_grey")

        def change_int(self, amount, add_to_log = True):
            self.int += self.int_debt
            self.int_debt = 0

            self.int += amount
            if self.int < 0:
                self.int_debt = self.int
                self.int = 0

            if amount != 0 and add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title

                log_string = display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Intelligence"
                mc.log_event(log_string, "float_text_grey")

        def change_focus(self, amount, add_to_log = True): #See charisma for full comments
            self.focus += self.focus_debt
            self.focus_debt = 0

            self.focus += amount
            if self.focus < 0:
                self.focus_debt = self.focus
                self.focus = 0

            if amount != 0 and add_to_log:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title

                log_string = display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Focus"
                mc.log_event(log_string, "float_text_grey")

        def change_hr_skill(self, amount, add_to_log = True):
            if amount + self.hr_skill < 0:
                amount = -self.hr_skill #Min 0
            self.hr_skill += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title

                log_string =  display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " HR Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_market_skill(self, amount, add_to_log = True):
            if amount + self.market_skill < 0:
                amount = -self.market_skill #Min 0
            self.market_skill += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string =  display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Market Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_research_skill(self, amount, add_to_log = True):
            if amount + self.research_skill < 0:
                amount = -self.research_skill #Min 0
            self.research_skill += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string =  display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Research Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_production_skill(self, amount, add_to_log = True):
            if amount + self.production_skill < 0:
                amount = -self.production_skill #Min 0
            self.production_skill += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string =  display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Production Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_supply_skill(self, amount, add_to_log = True):
            if amount + self.supply_skill < 0:
                amount = -self.supply_skill #Min 0
            self.supply_skill += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string =  display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Supply Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_sex_skill(self, skill_name, amount, add_to_log = True): #NOTE: We assume we pass a proper skill name here, otherwise we crash out.
            # ["Foreplay","Oral","Vaginal","Anal"]
            if amount + self.sex_skills[skill_name] < 0:
                amount = -self.sex_skills[skill_name] #At most we make it 0. No negative values.
            self.sex_skills[skill_name] += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string =  display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " " + skill_name + " Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_arousal(self,amount, add_to_log = True):
            self.arousal += __builtin__.int(__builtin__.round(amount)) #Round it to an integer if it isn't one already.
            if self.arousal < 0:
                self.arousal = 0

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string = display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Arousal"
                mc.log_event(log_string, "float_text_red")

        def reset_arousal(self):
            self.arousal = 0

        def change_max_arousal(self, amount, add_to_log = True):
            if amount + self.max_arousal < 20:
                amount = -(self.max_arousal - 20)

            self.max_arousal += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title

                log_string = display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Max Arousal"
                mc.log_event(log_string, "float_text_red")
            return amount

        def change_novelty(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount + self.novelty > 100:
                amount = 100 - self.novelty
            elif amount + self.novelty < 0:
                amount = self.novelty
            self.novelty += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string = display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Novelty"
                mc.log_event(log_string, "float_text_yellow")
            return amount

        def change_energy(self, amount, add_to_log = True):
            amount = __builtin__.round(amount)
            if amount + self.energy > self.max_energy:
                amount = self.max_energy - self.energy
            elif amount + self.energy < 0:
                amount = -self.energy

            self.energy += amount

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string = display_name+ ": " + ("+" if amount > 0 else "") + str(amount) + " Energy"
                mc.log_event(log_string, "float_text_yellow")
            return amount

        def change_max_energy(self, amount, add_to_log = True):
            amount = __builtin__.round(amount)
            if amount + self.max_energy < 0:
                amount = -self.max_energy

            self.max_energy += amount

            if self.energy > self.max_energy: #No having more energy than max
                self.energy = self.max_energy

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string = display_name+ ": " + ("+" if amount > 0 else "") + str(amount) + " Max Energy"
                mc.log_event(log_string, "float_text_yellow")
            return amount

        def review_outfit(self, dialogue = True, draw_person = True):
            if self.should_wear_uniform() and not self.is_wearing_uniform():
                self.wear_uniform()#Reset uniform
                if draw_person:
                    self.draw_person()
                if dialogue:
                    self.call_dialogue("clothing_review")

            elif not self.judge_outfit(self.outfit):
                self.apply_outfit()
                if draw_person:
                    self.draw_person()
                if dialogue:
                    self.call_dialogue("clothing_review")

        def judge_outfit(self, outfit, temp_sluttiness_boost = 0, use_taboos = True, as_underwear = False, as_overwear = False): #Judge an outfit and determine if it's too slutty or not. Can be used to judge other people's outfits to determine if she thinks they look like a slut.
            # temp_sluttiness can be used in situations (mainly crises) where an outfit is allowed to be temporarily more slutty than a girl is comfortable wearing all the time.
            #Returns true if the outfit is wearable, false otherwise
            if not outfit:
                return False

            if as_underwear or as_overwear:
                use_taboos = False

            if use_taboos and not (outfit.bra_covered() and outfit.panties_covered()) and "underwear_nudity" not in self.broken_taboos:
                taboo_modifier = "underwear_nudity"
            elif use_taboos and outfit.tits_visible() and "bare_tits" not in self.broken_taboos:
                taboo_modifier = "bare_tits"
            elif use_taboos and outfit.vagina_visible() and "bare_pussy" not in self.broken_taboos:
                taboo_modifier = "bare_pussy"
            else:
                taboo_modifier = None

            slut_require = outfit.slut_requirement
            if as_underwear:
                slut_require = outfit.get_underwear_slut_score()

            elif as_overwear:
                slut_require = outfit.get_overwear_slut_score()

            if (outfit.get_bra() or outfit.get_panties()) and not as_overwear: #Girls who like lingerie judge outfits with lingerie as less slutty than normal
                lingerie_bonus = 0
                if outfit.get_bra() and outfit.get_bra().slut_value > 2: #We consider underwear with an innate sluttiness of 3 or higher "lingerie" rather than just underwear.
                    lingerie_bonus += self.get_opinion_score("lingerie")
                if outfit.get_panties() and outfit.get_panties().slut_value > 2:
                    lingerie_bonus += self.get_opinion_score("lingerie")
                lingerie_bonus = __builtin__.int(lingerie_bonus*2) # Up to an 8 point swing in either direction
                slut_require += -lingerie_bonus #Treated as less slutty if she likes it, more slutty if she dislikes lingerie

            # Considers the outfit less slutty if she likes showing her tits and ass and that's what it would do.
            if outfit.vagina_visible() or (outfit.wearing_panties() and not outfit.panties_covered()):
                slut_require += -2*self.get_opinion_score("showing her ass")

            if outfit.tits_visible() or (outfit.wearing_bra() and not outfit.bra_covered()):
                slut_require += -2*self.get_opinion_score("showing her tits")

            if slut_require > (self.effective_sluttiness(taboo_modifier) + temp_sluttiness_boost): #Arousal is important for judging potential changes to her outfit while being stripped down during sex.
                return False
            return True

        def is_wearing_uniform(self): # Returns True if the clothing the girl is wearing contains all of the uniform clothing items. #TODO: may want to support more flexibility for over/underwear sets that had optional bits chosen by the girl.
            #May want to make this a Business side check. Make "is_valid_uniform" check like this against all uniforms available for the character. Would provide the flexiblity I mentioned above.
            if self.planned_uniform is None:
                return False #If no uniform is set you aren't wearing one at all.

            uniform_wardrobe = mc.business.get_uniform_wardrobe_for_person(self)
            matching_full = False
            full_set = False #Boolean used to track if we have at least one full set we _could_ have been wearing

            matching_overwear = False
            overwear_set = False #Tracks if we had at least one overwear we _could_ have been wearing

            matching_underwear = False
            underwear_set = False #Tracks if we had an underwear set we could have been wearing

            for potential_uniform in uniform_wardrobe.get_valid_outfit_list(): #Check if we match any of the full uniforms
                full_set = True
                if not matching_full:
                    matching_full = True #Assume they match, then find a counter example. When we do, break and try the next one.
                    for cloth in potential_uniform.generate_clothing_list():
                        if not self.outfit.has_clothing(cloth):
                            matching_full = False
                            break

            for potential_uniform in uniform_wardrobe.get_valid_overwear_sets_list(): #Check if we match the overwear and underwear sets.
                overwear_set = True
                if not matching_overwear:
                    matching_overwear = True
                    for cloth in potential_uniform.generate_clothing_list():
                        if not self.outfit.has_clothing(cloth):
                            matching_overwear = False
                            break

            for potential_uniform in uniform_wardrobe.get_valid_underwear_sets_list():
                underwear_set = True
                if not matching_underwear:
                    matching_underwear = True
                    for cloth in potential_uniform.generate_clothing_list():
                        if not self.outfit.has_clothing(cloth):
                            matching_underwear = False
                            break

            if matching_full:
                return True

            elif matching_overwear and matching_underwear:
                return True

            elif matching_overwear or matching_underwear: #Sometimes this is okay
                if matching_overwear and not underwear_set:
                    return True
                elif matching_underwear and not overwear_set:
                    return True

            return False

        def should_wear_uniform(self):
            if not self.is_at_work():  # quick exit
                return False

            if self.event_triggers_dict.get("forced_uniform", False):
                return True

            wardrobe = mc.business.get_uniform_wardrobe_for_person(self)
            return wardrobe and wardrobe.get_count() > 0

        def wear_uniform(self): #Puts the girl into her uniform, if it exists.
            if self.planned_uniform is None:
                if self.event_triggers_dict.get("forced_uniform", False):
                    the_uniform = self.event_triggers_dict.get("forced_uniform")
                else:
                    the_uniform = mc.business.get_uniform_wardrobe_for_person(self).decide_on_uniform(self)
                self.set_uniform(the_uniform, False) #If we don't have a uniform planned for today get one.

            if self.planned_uniform is not None: #If our planned uniform is STILL None it means we are unable to construct a valid uniform. Only assign it as our outfit if we have managed to construct a uniform.
                self.apply_outfit(self.planned_uniform) #We apply clothing taboos to uniforms because the character is assumed to have seen them in them.

        def get_job_happiness_score(self):
            happy_points = self.happiness - 100 #Happiness over 100 gives a bonus to staying, happiness less than 100 gives a penalty
            happy_points += self.obedience - 95 #A more obedient character is more likely to stay, even if they're unhappy. Default characters can be a little disobedint without any problems.
            happy_points += self.salary - self.calculate_base_salary() #A real salary greater than her base is a bonus, less is a penalty. TODO: Make this dependent on salary fraction, not abosolute pay.

            if (day - self.event_triggers_dict.get("employed_since",0)) < 14:
                happy_points += 14 - (day - self.event_triggers_dict.get("employed_since",0)) #Employees are much less likely to quit over the first two weeks.
            return happy_points

        def get_no_condom_threshold(self, situational_modifier = 0):
            if self.has_role(pregnant_role) and self.event_triggers_dict.get("preg_knows", False):
                return 0 #You can't get more pregnant, so who cares?

            if self.has_role(breeder_role):
                return 0 #She _wants_ to get knocked up. This will probably trigger other dialogue as well.

            no_condom_threshold = 50 + (self.get_opinion_score("bareback sex") * -10) + situational_modifier
            if any(relationship in [sister_role,mother_role,aunt_role,cousin_role] for relationship in self.special_role):
                no_condom_threshold += 10

            if persistent.pregnancy_pref == 0:
                no_condom_threshold += 10 #If pregnancy content is being ignored we return to the baseline of 60
            elif self.on_birth_control: #If there is pregnancy content then a girl is less likely to want a condom when using BC, much more likely to want it when not using BC.
                no_condom_threshold -= 20

            return no_condom_threshold

        def wants_condom(self, situational_modifier = 0, use_taboos = True):
            taboo_modifier = 0
            if use_taboos and self.effective_sluttiness("condomless_sex") < self.get_no_condom_threshold(situational_modifier = situational_modifier):
                return True
            elif self.effective_sluttiness() < self.get_no_condom_threshold(situational_modifier = situational_modifier):
                return True
            return False

        def has_family_taboo(self): #A check to see if we should use an incest taboo modifier.
            if self.get_opinion_score("incest") > 0: #If she thinks incest is hot she doesn't have an incest taboo modifier. Maybe she should, but it should just be reduced? For now this is fine.
                return False

            elif self.is_family():
                return True

            return False

        def is_family(self):
            if any(relationship in [sister_role,mother_role,aunt_role,cousin_role] for relationship in self.special_role):
                return True

        def is_at_work(self):
            if not self.job:
                return False
            return self.job.job_location == self.location

        def has_tiny_tits(self): #Returns true if the girl has tiny breasts. "AA" cups.
            return self.tit_is_tiny(self.tits)

        def has_small_tits(self): #Returns true if the girl has small breasts (Below "C" cup)
            return self.tit_is_small(self.tits)

        def has_large_tits(self): #Returns true if the girl has large breasts. "D" cups and up are considered large enough for titfucking, swinging, etc.
            return self.tit_is_large(self.tits)

        def has_huge_tits(self): #Returns true if the girl has huge breasts ("E" and up)
            return self.tit_is_huge(self.tits)

        def wants_creampie(self): #Returns True if the girl is going to use dialogue where she wants you to creampie her, False if she's going to be angry about it. Used to help keep dialogue similar throughout events
            creampie_threshold = 75
            if self.on_birth_control:
                creampie_threshold -= 20 #Much more willing to let you creampie her if she's on BC


            if girlfriend_role in self.special_role:
                creampie_threshold -= 10 + (5 * self.get_opinion_score("being submissive")) #Desire to be a "good wife"

            if self.is_family(): # If she hates incest, it increases the treshhold
                creampie_threshold += 10 - (10 * self.get_opinion_score("incest"))

            effective_slut = self.effective_sluttiness("creampie") + (10 * self.get_opinion_score("creampies")) + (10 * self.get_opinion_score("anal creampies"))
            if effective_slut >= creampie_threshold or self.event_triggers_dict.get("preg_knows", False):
                return True

            return False

        def calculate_realistic_fertility(self):
            day_difference = self.days_from_ideal_fertility() # Gets the distance between the current day and the ideal fertile day.
            multiplier = 2 - (float(day_difference)/10.0) # The multiplier is 2 when the day difference is 0, 0.5 when the day difference is 15.
            effective_fertility = self.fertility_percent * multiplier
            return effective_fertility

        def days_from_ideal_fertility(self):
            day_difference = abs((day % 30) - self.ideal_fertile_day)
            if day_difference > 15:
                day_difference = 30 - day_difference #Wrap around to get correct distance between months.
            return day_difference

        def fertility_cycle_string(self): #Turns the difference of days from her ideal fertile day into a string
            day_difference = self.days_from_ideal_fertility
            if day_difference >= 12:
                return "Very Safe"
            elif day_difference >= 8:
                return "Safe"
            elif day_difference >= 3:
                return "Normal"
            return "Risky"

        def update_birth_control_knowledge(self, force_known_state = None, force_known_day = None): #Called any time a girl gives you information about her BC. Allows for an up to date detailed info screen that doesn't give more than you know
            if force_known_state is None: #Useful when you an event changes a girls BC and you can expect that she's not going to be on birth control the next day.
                known_state = self.on_birth_control
            else:
                known_state = force_known_day

            if force_known_day is None:
                known_day = day
            else:
                known_day = force_known_day

            self.event_triggers_dict["birth_control_status"] = known_state
            self.event_triggers_dict["birth_control_known_day"] = known_day


        def effective_sluttiness(self, taboos = None): #Used in sex scenes where the girl will be more aroused, making it easier for her to be seduced.
            if taboos is None:
                taboos = []
            elif not isinstance(taboos, list): #Handles handing over a single item without pre-wrapping it for "iteration".
                taboos = [taboos]

            return_amount = __builtin__.int(self.sluttiness + (self.arousal/4))

            for taboo in taboos:
                if taboo not in self.broken_taboos: #If any of the taboo handed over are not already broken this person has a -15 effective sluttiness.
                    return_amount += -10
                    break #Only appies once, so break once the mallus is applied.


            for source in self.situational_sluttiness:
                return_amount += self.situational_sluttiness[source][0]

            return return_amount

        def run_orgasm(self, show_dialogue = True, force_trance = False, trance_chance_modifier = 0, add_to_log = True, sluttiness_increase_limit = 30, reset_arousal = True, fire_event = True):
            self.change_slut(1, sluttiness_increase_limit, add_to_log = add_to_log)
            if fire_event:
                mc.listener_system.fire_event("girl_climax", the_person = self)
            if renpy.random.randint(0,100) < self.suggestibility + trance_chance_modifier or force_trance:
                self.increase_trance(show_dialogue = show_dialogue, reset_arousal = reset_arousal, add_to_log = add_to_log)

        def increase_trance(self, show_dialogue = True, reset_arousal = True, add_to_log = True):
            display_name = self.create_formatted_title("???")
            if self.title:
                display_name = self.title

            if not self.has_role(trance_role):
                self.add_role(trance_role)
                mc.listener_system.fire_event("girl_trance", the_person = self)
                if add_to_log:
                    mc.log_event(display_name + " sinks into a trance!", "float_text_red")
                if show_dialogue:
                    renpy.say(None, self.possessive_title + "'s eyes lose focus slightly as she slips into a climax induced trance.")

            elif self.has_exact_role(trance_role):
                self.remove_role(trance_role)
                self.add_role(heavy_trance_role)
                if add_to_log:
                    mc.log_event(display_name + " sinks deeper into a trance!", "float_text_red")
                if show_dialogue:
                    renpy.say(None, self.possessive_title + " seems to lose all focus as her brain slips deeper into a post-orgasm trance.")

            elif self.has_exact_role(heavy_trance_role):
                self.remove_role(heavy_trance_role)
                self.add_role(very_heavy_trance_role)
                if add_to_log:
                    mc.log_event(display_name + " sinks deeper into a trance!", "float_text_red")
                if show_dialogue:
                    renpy.say(None, self.possessive_title + "'s eyes glaze over, and she sinks completely into a cum addled trance.")

            if reset_arousal:
                self.reset_arousal() #TODO: Decide if resetting should only halve it, like making a girl cum yoruself.

        def get_trance_multiplier(self):
            if self.has_exact_role(trance_role):
                return 1.5
            elif self.has_exact_role(heavy_trance_role):
                return 2.0
            elif self.has_exact_role(very_heavy_trance_role):
                return 3.0
            return 1.0

        def cum_in_mouth(self, add_to_record = True): #Add the appropriate stuff to their current outfit, and peform any personal checks if rquired.
            mc.listener_system.fire_event("sex_cum_mouth", the_person = self)
            if self.outfit.can_add_accessory(mouth_cum):
                the_cumshot = mouth_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("drinking cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("drinking cum"), add_to_log = add_to_record)
            self.discover_opinion("drinking cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum in Mouth"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["mouth_cum"] = report_log.get("mouth_cum", 0) + 1


        def cum_in_vagina(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_vagina", the_person = self)
            if self.outfit.can_add_accessory(creampie_cum):
                the_cumshot = creampie_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            slut_change_amount =  self.get_opinion_score("creampies")

            if self.wants_creampie():
                self.change_happiness(5*self.get_opinion_score("creampies"), add_to_log = add_to_record)
            else:
                self.change_happiness(-5 + (5*self.get_opinion_score("creampies")), add_to_log = add_to_record)
                self.change_love(-2 + self.get_opinion_score("creampies"), add_to_log = add_to_record)
                slut_change_amount += self.get_opinion_score("being_submissive")

            self.change_slut(slut_change_amount, add_to_log = add_to_record)
            self.discover_opinion("creampies", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Vaginal Creampies"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["creampies"] = report_log.get("creampies", 0) + 1

            # Pregnancy Check #
            if persistent.pregnancy_pref > 0 and pregnant_role not in self.special_role:
                if persistent.pregnancy_pref == 1 and self.on_birth_control: #Establish how likely her birth contorl is to work (if needed, and if present)
                    bc_percent = 100 - self.bc_penalty
                elif persistent.pregnancy_pref == 2 and self.on_birth_control:
                    bc_percent = 90 - self.bc_penalty
                else:
                    bc_percent = 0

                preg_chance = renpy.random.randint(0,100)
                bc_chance = renpy.random.randint(0,100)
                if persistent.pregnancy_pref == 2: # On realistic pregnancy a girls chance to become pregnant fluctuates over the month.
                    modified_fertility = self.calculate_realistic_fertility()
                else:
                    modified_fertility = self.fertility_percent

                if preg_chance < modified_fertility and pregnant_role not in self.special_role: #There's a chance she's pregnant
                    if bc_chance >= bc_percent : # Birth control failed to prevent the pregnancy
                        become_pregnant(self) #Function in role_pregnant establishes all of the pregnancy related variables and events.


        def cum_in_ass(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_ass", the_person = self)
            #TODO: Add an anal specific cumshot once we have renders for it.
            if self.outfit.can_add_accessory(creampie_cum):
                the_cumshot = creampie_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            if not self.wants_creampie():
                self.change_love(-2 + self.get_opinion_score("anal creampies"), add_to_log = add_to_record)

            self.change_happiness(5 * self.get_opinion_score("anal creampies"), add_to_log = add_to_record)
            self.change_slut(self.get_opinion_score("anal creampies"), add_to_log = add_to_record)
            self.discover_opinion("anal creampies", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Anal Creampies"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["anal creampies"] = report_log.get("anal creampies", 0) + 1


        def cum_on_face(self, add_to_record = True):
            if self.outfit.can_add_accessory(face_cum):
                the_cumshot = face_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("cum facials"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("cum facials"), add_to_log = add_to_record)
            self.discover_opinion("cum facials", add_to_log = add_to_record)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Facials"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["facials"] = report_log.get("facials", 0) + 1


        def cum_on_tits(self, add_to_record = True):
            if self.outfit.can_add_accessory(tits_cum):
                the_cumshot = tits_cum.get_copy()
                if self.outfit.get_upper_visible():
                    top_layer = self.outfit.get_upper_visible()[0].layer #Get the top most pice of clothing and get it's layer.
                else:
                    top_layer = -1
                the_cumshot.layer = top_layer+1 #The cumshot lives on a layer it hit, above the one it hit. Accessories are drawn first in the hirearchy, so they have to be on a level higehr than what they hit.
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Covered"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["body_cum"] = report_log.get("body_cum", 0) + 1


        def cum_on_stomach(self, add_to_record = True):
            if self.outfit.can_add_accessory(stomach_cum):
                the_cumshot = stomach_cum.get_copy()
                if self.outfit.get_upper_visible():
                    top_layer = self.outfit.get_upper_visible()[0].layer #Get the top most pice of clothing and get it's layer.
                else:
                    top_layer = -1
                the_cumshot.layer = top_layer+1 #The cumshot lives on a layer it hit, above the one it hit. Accessories are drawn first in the hirearchy, so they have to be on a level higehr than what they hit.
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Covered"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["body_cum"] = report_log.get("body_cum", 0) + 1


        def cum_on_ass(self, add_to_record = True):
            if self.outfit.can_add_accessory(ass_cum):
                the_cumshot = ass_cum.get_copy()
                if self.outfit.get_lower_visible():
                    top_layer = self.outfit.get_lower_visible()[0].layer #Get the top most pice of clothing and get it's layer.
                else:
                    top_layer = -1
                the_cumshot.layer = top_layer+1 #The cumshot lives on a layer it hit, above the one it hit. Accessories are drawn first in the hirearchy, so they have to be on a level higehr than what they hit.
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Covered"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["body_cum"] = report_log.get("body_cum", 0) + 1

        def change_salary(self, amount, add_to_log = True):
            amount = __builtin__.round(amount)
            self.salary += amount
            if self.salary < 0:
                self.salary = 0

            if add_to_log and amount != 0:
                display_name = self.create_formatted_title("???")
                if self.title:
                    display_name = self.title
                log_string = display_name + ": " + ("+" if amount > 0 else "") + "$" + str(amount) + "/Day"
                mc.log_event(log_string, "float_text_green")

        #TODO: We should add an "expected salary modifier" field, so people who are interns don't get angry about it.
        def calculate_base_salary(self): #returns the default value this person should be worth on a per day basis.
            return __builtin__.int(((self.int + self.focus + self.charisma)*2 + (self.hr_skill + self.market_skill + self.research_skill + self.production_skill + self.supply_skill)) * self.salary_modifier * (0.5+0.25*self.work_experience))

        def calculate_job_salary(self, salary_modifier = None): #NOTE: base_salary includes self.salary_modifier.
            if salary_modifier is None:
                salary_modifier = 1.0
            return __builtin__.int(self.calculate_base_salary() * salary_modifier * self.job.wage_adjustment);

        def calculate_job_efficency(self):
            return self.job.productivity_adjustment * self.productivity_adjustment;

        def set_schedule(self, the_location, the_days = None, the_times = None):
            self.schedule.set_schedule(the_location, the_days, the_times)

        def set_override_schedule(self, the_location, the_days = None, the_times = None):
            self.override_schedule.set_schedule(the_location, the_days, the_times)

        def copy_schedule(self): #Returns a properly formatted dict without references to the current schedule.
            return self.schedule.get_copy()
            #TODO: Should this return some sort of overlapped work/life schedule?

        def get_destination(self, specified_day = None, specified_time = None): #TODO: Needs to check against personal and work schedule
            override_return = self.override_schedule.get_destination(specified_day, specified_time)
            if override_return is not None:
                return override_return

            work_return = self.job.schedule.get_destination(specified_day, specified_time)
            if work_return is not None:
                return work_return #our job is telling us to be somewhere, so go there

            return self.schedule.get_destination(specified_day, specified_time) #Otherwise, go where we want.

        def get_next_destination(self):
            override_return = self.override_schedule.get_next_destination()
            if override_return is not None:
                return override_return

            work_return = self.job.schedule.get_next_destination()
            if work_return is not None:
                return work_return

            return self.schedule.get_next_destination()

        def person_meets_requirements(self, slut_required = 0, slut_max = 2000, obedience_required = 0, obedience_max = 2000, love_required = -200, love_max = 2000):
            if self.sluttiness >= slut_required and self.sluttiness <= slut_max and self.obedience >= obedience_required and self.obedience <= obedience_max and self.love >= love_required and self.love <= love_max:
                return True
            return False

        def valid_role_actions(self):
            count = 0
            for role in self.special_role:
                for act in role.actions:
                    if act.is_action_enabled(self) or act.is_disabled_slug_shown(self): #We should also check if a non-action disabled slug would be available so that the player can check what the requirement would be.
                        count += 1
            return count

        def create_formatted_title(self, the_title):
            formatted_title = "{color=" + self.char.who_args["color"] + "}" + "{font=" + self.char.what_args["font"] + "}" + the_title + "{/font}{/color}"
            return formatted_title

        def set_title(self, new_title): #Takes the given title and formats it so that it will use the characters font colours when the_person.title is used.
            self.char.name = new_title #This ensures the dialogue name is correct for the new title.
            self.title = self.create_formatted_title(new_title)

        def set_possessive_title(self, new_title):
            self.possessive_title = self.create_formatted_title(new_title)

        def set_mc_title(self, new_title):
            self.mc_title = new_title

        def personalise_text(self, what):
            for text_modifier in self.text_modifiers:
                what = text_modifier(self, what)

            return what

        def has_job(self, the_job):
            if self.job and self.job == the_job:
                return True
            return False


        def change_job(self, new_job, job_known = True): #Start a new job, quitting your old one if nessesary
            if self.job and new_job == self.job: #Don't do anything if we already have this job.
                return

            if self.job: # If we had a job before we should quit it. Should only come up on init (after that we're always Unemployed, which is still a Job)
                if self.job.quit_function:
                    self.job.quit_function(self)

                for a_role in self.job.job_roles: #Remove any job roles that aren't shared with the new job (we do this to maintain linkd roles which are still valid)
                    if not a_role in new_job.job_roles:
                        self.remove_role(a_role)

                for old_duty in self.duties:
                    if not old_duty in new_job.mandatory_duties + new_job.available_duties: #
                        self.remove_duty(old_duty) #Remove duties that aren't available in the new job


            if new_job.hire_function:
                new_job.hire_function(self)

            for a_role in new_job.job_roles:
                if not self.has_exact_role(a_role):
                    self.add_role(a_role)

            for new_duty in new_job.mandatory_duties:
                if new_duty not in self.duties:
                    self.add_duty(new_duty)

            self.limit_duties() # Make sure we don't have too many duties after changing our job.

            self.job = new_job

            self.salary = self.calculate_job_salary()
            self.event_triggers_dict["job_known"] = job_known

        def quit_job(self, job_known = True): #Quit and become unemployed
            self.change_job(unemployed_job)

        def add_duty(self, the_duty):
            if the_duty not in self.duties: #Isn't possible to have the same duty twice.
                if the_duty.on_apply is not None:
                    the_duty.on_apply(self)
                self.duties.append(the_duty)

        def remove_duty(self, the_duty):
            if the_duty in self.duties:
                if the_duty.on_remove is not None:
                    the_duty.on_remove(self)
                self.duties.remove(the_duty)

        def has_duty(self, the_duty):
            for a_duty in self.duties:
                if a_duty == the_duty:
                    return True
            return False

        def limit_duties(self): #Checks if we are over our duty limit and removes non-mandatory duties until we are under
            if len(self.duties) > self.work_experience:
                over_count = len(self.duties) - self.work_experience
                for a_duty in self.duties[::-1]: #Traverse the list backwards, so the most recently added duty is first trimmed.
                    if a_duty not in self.job.mandatory_duties:
                        self.remove_duty(a_duty)
                        over_count += -1
                        if over_count == 0:
                            break
            return

        def get_duty_actions(self):
            return_list = []
            for duty in self.duties:
                if self.is_at_work() or not duty.only_at_work:
                    for act in duty.actions:
                        if act not in return_list: #Trim duplicates out of our duty list (NOTE: maybe we want to trim them out at the UI level?)
                            return_list.append(act)
            return return_list

        def get_duty_internet_actions(self):
            return_list = []
            for duty in self.duties:
                if self.is_at_work() or not duty.only_at_work:
                    for act in duty.internet_actions:
                        if act not in return_list:
                            return_list.append(act)
            return return_list

        def add_role(self, the_role):
            if not the_role in self.special_role:
                self.special_role.append(the_role)

        def remove_role(self, the_role, remove_all = False, remove_linked = True):
            if the_role in self.special_role:
                self.special_role.remove(the_role)
                if remove_linked:
                    for linked_role in the_role.linked_roles:
                        self.remove_role(linked_role, remove_all, remove_linked)
                if remove_all:
                    self.remove_role(the_role, remove_all, remove_linked)

        def has_role(self, the_role):
            if the_role in self.special_role:
                return True
            else:
                for a_role in self.special_role:
                    if a_role.check_looks_like(the_role):
                        return True

            return False

        def has_exact_role(self, the_role): #As has_role, but checks against all roles and all of their looks_like roles.
            if the_role in self.special_role:
                return True
            return False

        def get_role_reference(self, the_role):
            for role in self.special_role:
                if the_role == role:
                    return role
            return None

        def get_role_reference_by_name(self, the_role):
            for role in self.special_role:
                if role.role_name == the_role:
                    return role
            return None

        def has_queued_event(self, the_event):
            for an_event in self.on_talk_event_list:
                if an_event == the_event:
                    return True

            for an_event in self.on_room_enter_event_list:
                if an_event == the_event:
                    return True

            return False

        def has_queued_event_with_name(self, the_name):
            for an_event in self.on_talk_event_list:
                if an_event.name == the_name:
                    return True

            for an_event in self.on_room_enter_event_list:
                if an_event.name == the_name:
                    return True

            return False

        def add_infraction(self, the_infraction, add_to_log = True, require_policy = True):
            if office_punishment.is_active() or not require_policy:
                self.infractions.append(the_infraction)
                if add_to_log:
                    display_name = self.create_formatted_title("???")
                    if self.title:
                        display_name = self.title
                    mc.log_event(display_name + " committed infraction: " + the_infraction.name + ", Severity " + str(the_infraction.severity), "float_text_grey")

        def remove_infraction(self, the_infraction):
            if the_infraction in self.infractions:
                self.infractions.remove(the_infraction)

        def set_eye_colour(self, new_colour):
            new_colour = Color(rgb=(new_colour.rgb)) #Make sure we don't have any alpha problems.
            eye_colour_name = closest_colour(new_colour).capitalize()
            eye_colour_list = [new_colour.rgb[0], new_colour.rgb[1], new_colour.rgb[2], 1.0]

            self.eyes = [eye_colour_name, eye_colour_list]

        def set_hair_colour(self, new_colour, change_pubes = True, darken_pubes_amount = 0.07):
            #NOTE: new_colour should be a Ren'py colour.
            new_colour = Color(rgb=(new_colour.rgb)) #Make sure we don't have any alpha problems.
            hair_colour_name = closest_colour(new_colour).capitalize()
            hair_colour_list = [new_colour.rgb[0], new_colour.rgb[1], new_colour.rgb[2], 1.0]

            self.hair_colour = [hair_colour_name, hair_colour_list]

            if change_pubes:
                pubes_colour = new_colour.shade(1.0-darken_pubes_amount)
                self.pubes_style.colour = [pubes_colour.rgb[0], pubes_colour.rgb[1], pubes_colour.rgb[2], 1.0]
                self.pubes_colour = self.pubes_style.colour
            self.hair_style.colour = hair_colour_list

        def get_milk_trait(self): # Generates a milk trait that can be used any time you harvest lactating milk. #TODO: Add ways to give this trait augments, like +duration or it suppresses side effects.
            milk_trait = SerumTrait(self.title + "'s Breast Milk",
                "Fresh breast milk produced by " +  self.possessive_title + ". Valuable to the right sort of person.",
                sexual_aspect = 2, medical_aspect = 2)
            return milk_trait


        def get_titles(self): #Returns a list of character titles this person can have. A title is what you call a person, often but not always their name or based on their name.
            list_of_titles = []

            personality_titles = self.personality.get_personality_titles(self)
            if isinstance(personality_titles, list):
                list_of_titles.extend(personality_titles)
            else:
                list_of_titles.append(personality_titles)

            if self.sluttiness > 20:
                if self.obedience > 150:
                    list_of_titles.append("Slave")


            if self.sluttiness > 60:
                list_of_titles.append("Slut")
                if self.obedience > 140:
                    list_of_titles.append("Cocksleeve")
                    list_of_titles.append("Cock Slave")

                if self.has_huge_tits():
                    list_of_titles.append("Melony")
                elif self.has_tiny_tits():
                    list_of_titles.append("Sweet Pea")
                elif self.has_large_tits():
                    list_of_titles.append("Big Tits")
                else:
                    list_of_titles.append("Little Tits")

                if self.sex_record.get("Vaginal Creampies", 0) >= 20:
                    list_of_titles.append("Breeding Material")

            if self.sluttiness > (70 - (self.get_opinion_score("drinking cum")*5 + self.get_opinion_score("creampies")*5 + self.get_opinion_score("cum facials")*5 + self.get_opinion_score("being covered in cum")*5)):
                if self.sex_record.get("Cum Facials", 0) > 5 or self.sex_record.get("Cum in Mouth", 0) > 5 or self.sex_record.get("Cum Covered", 0) > 5:
                    list_of_titles.append("Cumslut")

            if self.sluttiness > (70 - (self.get_opinion_score("bareback sex")*5 + self.get_opinion_score("creampies")*5)):
                if self.sex_record.get("Vaginal Creampies", 0) > 5 or self.sex_record.get("Anal Creampies", 0) > 5:
                    list_of_titles.append("Cumdump")



            if self.love >= 60 and self.has_role(girlfriend_role):
                list_of_titles.append("Love")

            if self.love < 0:
                list_of_titles.append("Cunt")
                list_of_titles.append("Bitch")

            return list(set(list_of_titles)) #We return the list so that it can be presented to the player. In general the girl will always want to pick the first one on the list.

        def get_random_title(self):
            return get_random_from_list(self.get_titles())

        def get_possessive_titles(self):
            list_of_possessive_titles = []
            #Your mother and sister both have specific personality types, so they get their family titles there.

            personality_possessive_titles = self.personality.get_personality_possessive_titles(self)
            if isinstance(personality_possessive_titles, list):
                list_of_possessive_titles.extend(personality_possessive_titles)
            else:
                list_of_possessive_titles.append(personality_possessive_titles)

            if self.has_role(employee_role):
                list_of_possessive_titles.append("Your employee")
                if self.sluttiness > 60:
                    list_of_possessive_titles.append("Your office slut")

            if self.love > 10:
                list_of_possessive_titles.append("Your friend")

            if self.obedience > 150:
                list_of_possessive_titles.append("Your slave")
                if self.sluttiness > 60:
                    list_of_possessive_titles.append("Your dedicated cocksleeve")


            if self.sluttiness > 60:
                if self.int <= 1 and self.has_large_tits():
                    list_of_possessive_titles.append("Your airhead bimbo")


                if self.love > 50:
                    list_of_possessive_titles.append("Your personal slut")
                elif self.love < 0:
                    list_of_possessive_titles.append("Your hatefuck slut")
                else:
                    list_of_possessive_titles.append("Your slut")

                if self.kids > 0:
                    list_of_possessive_titles.append("Your slutty MILF")

                if not self.relationship == "Single":
                    list_of_possessive_titles.append("Your cheating slut")

                if self.sex_record.get("Vaginal Creampies", 0) >= 20:
                    list_of_possessive_titles.append("Your breeder")

            if self.sluttiness > (70 - (self.get_opinion_score("drinking cum")*5 + self.get_opinion_score("creampies")*5 + self.get_opinion_score("cum facials")*5 + self.get_opinion_score("being covered in cum")*5)):
                if self.sex_record.get("Cum Facials", 0) > 5 or self.sex_record.get("Cum in Mouth", 0) > 5 or self.sex_record.get("Cum Covered", 0) > 5:
                    list_of_possessive_titles.append("Your cumslut")

                if self.sex_record.get("Vaginal Creampies", 0) > 5 or self.sex_record.get("Anal Creampies", 0) > 5:
                    list_of_possessive_titles.append("Your cumdump")



            if self.love >= 60 and self.has_role(girlfriend_role):
                list_of_possessive_titles.append("Your love")
                list_of_possessive_titles.append("Your girlfriend")

            if self.love >= 60 and self.has_role(affair_role):
                list_of_possessive_titles.append("Your lover")

            if self.has_role(student_role):
                list_of_possessive_titles.append("Your student")

            return list(set(list_of_possessive_titles))

        def get_random_possessive_title(self):
            return get_random_from_list(self.get_possessive_titles())

        def get_player_titles(self):
            list_of_player_titles = ["Mr. " + mc.last_name, mc.name]
            personality_player_titles = self.personality.get_personality_player_titles(self)
            if isinstance(personality_player_titles, list):
                list_of_player_titles.extend(personality_player_titles)
            else:
                list_of_player_titles.append(personality_player_titles)

            if self.has_role(employee_role) or self.has_role(student_role):
                if self.obedience > 120:
                    list_of_player_titles.append("Sir")
                elif self.obedience < 80 and self.has_role(employee_role):
                    list_of_player_titles.append("Boss")

            if self.obedience > 140 and self.sluttiness > 50:
                list_of_player_titles.append("Master")

            if self.sluttiness > 50:
                if self.love > 50:
                    list_of_player_titles.append("Daddy")
                elif self.love < 0:
                    list_of_player_titles.append("Fuck Meat")
                    list_of_player_titles.append("Cunt Slave")
                else:
                    list_of_player_titles.append("Boy Toy")

            if self.has_role(student_role):
                list_of_player_titles.append("Teacher")

            return list(set(list_of_player_titles))

        def get_random_player_title(self):
            return get_random_from_list(self.get_player_titles())

        def get_appropriate_mag_name(self, discover_opinion = False): # Returns the name of a porn magazine this person might be interested in reading, based on her opinions.
            if self.get_opinion_score("drinking cum") > 0:
                if discover_opinion:
                    self.discover_opinion("drinking cum")
                return "Cum Guzzlers Monthly"
            elif self.get_opinion_score("creampies") > 0:
                if discover_opinion:
                    self.discover_opinion("creampies")

                if self.get_opinion_score("bareback sex") > 0:
                    if discover_opinion:
                        self.discover_opinion("bareback sex")
                    return "Storked - Sluts Fucked Pregnant!"
                else:
                    return "Close Up Cum Shots - Filled to the Brim!"
            elif self.get_opinion_score("being covered in cum") > 0:
                if discover_opinion:
                    self.discover_opinion("being covered in cum")
                return "Glazed: Busty Sluts get Covered in Cum!"
            elif self.get_opinion_score("giving blowjobs") > 0:
                if discover_opinion:
                    self.discover_opinion("giving blowjobs")
                return "Throated: Girls get Messy!"
            elif self.get_opinion_score("incest") > 0:
                if discover_opinion:
                    self.discover_opinion("incest")
                return "A Mother's Duty - Fuck Your Son!"
            elif self.get_opinion_score("anal sex") > 0:
                if discover_opinion:
                    self.discover_opinion("anal sex")
                return "Anal Domination"
            elif self.get_opinion_score("public sex") > 0:
                if discover_opinion:
                    self.discover_opinion("public sex")
                return "Public Sluts"
            elif self.get_opinion_score("lingerie") > 0:
                if discover_opinion:
                    self.discover_opinion("lingerie")
                return "Lingerie Monthly: What to Wear"
            elif self.get_opinion_score("giving handjobs") > 0:
                if discover_opinion:
                    self.discover_opinion("giving handjobs")
                return "Getting Handy with Handjobs."
            elif self.get_opinion_score("giving tit fucks") > 0:
                if discover_opinion:
                    self.discover_opinion("giving tit fucks")
                return "Bimbo Quarterly - Titfuck Edition"
            elif self.get_opinion_score("being submissive") > 0:
                if discover_opinion:
                    self.discover_opinion("being submissive")
                return "The Good Wife's Guide to Getting Fucked"
            else:
                return "Playgirl - Sluts on Display!"
