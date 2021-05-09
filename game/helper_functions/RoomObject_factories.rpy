init -1 python:
    def make_wall(): #Helper functions for creating instances of commonly used objects.
        return Object("wall",["Lean"], sluttiness_modifier = 0, obedience_modifier = 0) #0/5

    def make_window():
        return Object("window",["Lean"], sluttiness_modifier = 0, obedience_modifier = 0) #-5/5

    def make_chair():
        return Object("chair",["Sit","Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_desk():
        return Object("desk",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_table():
        return Object("table",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_bed():
        return Object("bed",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0) #10/10

    def make_couch():
        return Object("couch",["Sit","Lay","Low"], sluttiness_modifier = 0, obedience_modifier = 0) #5/-5

    def make_floor():
        return Object("floor",["Lay","Kneel"], sluttiness_modifier = 0, obedience_modifier = 0) #-10/-10

    def make_grass():
        return Object("grass",["Lay","Kneel"], sluttiness_modifier = 0, obedience_modifier = 0) #-5/-10

    def make_stage():
        return Object("stripclub stage",["Lay","Sit"], sluttiness_modifier = 0, obedience_modifier = 0) #5/-5

    def make_front_door():
        return Object("front door", ["Lean"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_hall_carpet():
        return Object("hall carpet", ["Kneel", "Lay"], sluttiness_modifier = 0, obedience_modifier = 0)

    def make_stairs():
        return Object("stairs", ["Sit", "Low"], sluttiness_modifier = 0, obedience_modifier = 0)
