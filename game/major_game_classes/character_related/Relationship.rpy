init -2 python:
    class Relationship(): #A class used to store information about the relationship between two people. Do not manipulate directly, use RelationshipArray to change things.
        def __init__(self, person_a, person_b, type_a, type_b = None, visible = None):
            self.person_a = person_a #Person a and b are Person objects.
            self.person_b = person_b
            self.type_a = type_a #person_a TO person_b, written so you could tell what person_b is if you listed them. Ie. "Lily - Daughter".
            if type_b is None: #Type can vary depending on what direction you view the relationship ie. mother-daughter, employee-boss.
                self.type_b = type_a
            else:
                self.type_b = type_b

            if visible is None:
                self.visible = True
            else:
                self.visible = visible

        @property
        def person_a(self):
            if not hasattr(self, "_person_a"):
                self._person_a = None
            return next((x for x in all_people_in_the_game() if x.identifier == self._person_a), None)

        @person_a.setter
        def person_a(self, value):
            if isinstance(value, Person):
                self._person_a = value.identifier

        @property
        def person_b(self):
            if not hasattr(self, "_person_b"):
                self._person_b = None
            return next((x for x in all_people_in_the_game() if x.identifier == self._person_b), None)

        @person_b.setter
        def person_b(self, value):
            if isinstance(value, Person):
                self._person_b = value.identifier

        def get_other_person(self, the_person): #Used to make it simpler to get a relationship for one person and know who the "other" person is.
            if the_person == self.person_a:
                return self.person_b
            elif the_person == self.person_b:
                return self.person_a
            else:
                return None #In theory this shouldn't come up unless this class is being abused in some way. (But some classes are into that sort of thing. I don't judge)

        def get_other_person_identifier(self, identifier):
            if identifier == self._person_a:
                return self._person_b
            if identifier == self._person_b:
                return self._person_a
            return None

        def get_type(self, the_person = None):
            if the_person == self.person_a:
                return self.type_a
            elif the_person == self.person_b:
                return self.type_b
            return None

        def get_type_by_identifier(self, identifier):
            if identifier == self._person_a:
                return self.type_a
            if identifier == self._person_b:
                return self.type_b
            return None


    class RelationshipArray():
        relationship_scale = ["Nemesis", "Rival", "Acquaintance", "Friend", "Best Friend"]

        def __init__(self):
            self.relationships = [] #List of relationships. Relationships are bi-directional, so if you look for person_a, person_b you'll get the same object as person_b, person_a (but the type can be relative to the order).
            ### Types of Relationships (* denotes currently unused but planned roles)
            # Family: Mother, Daughter, Cousin, Niece, Aunt, Grandmother*, Granddaughter*
            # Positive: Acquaintance, Friend, Best Friend, Girlfriend*, Fiancée*, Wife*
            # Negative: Rival, Nemesis*

        def update_relationship(self, person_a, person_b, type_a, type_b = None, visible = None): #Note that type_a is required, but if you want to do just one half of a relationship you can flip the person order around.
            if person_a is person_b: #Don't form relationships with yourself!
                return
            if not person_a or not person_b:    # Don't create empty relationship
                return

            the_relationship = self.get_relationship(person_a, person_b)
            if the_relationship is None: #No relationship exists yet, make one.
                self.relationships.append(Relationship(person_a, person_b, type_a, type_b, visible))

            else: #A relationship exists, update it to the new state.
                if person_a.identifier == the_relationship._person_a: #Relationships may have been refered to in the opposite order, so flip the references around if needed.
                    if type_a is not None:
                        the_relationship.type_a = type_a

                    if type_b is None:
                        the_relationship.type_b = type_a
                    else:
                        the_relationship.type_b = type_b

                elif person_a.identifier == the_relationship._person_b:
                    if type_a is not None:
                        the_relationship.type_b = type_a

                    if type_b is None:
                        the_relationship.type_a = type_a
                    else:
                        the_relationship.type_a = type_b

                if visible is not None:
                    the_relationship.visible = visible


        def get_relationship(self, person_a, person_b):
            for relationship in self.relationships:
                if (relationship._person_a == person_a.identifier and relationship._person_b == person_b.identifier) or \
                    (relationship._person_a == person_b.identifier and relationship._person_b == person_a.identifier):
                    return relationship #If we find a relationship containing the same two people (but perhaps with their position inverted) return it.

            return None #Otherwise these people have no relationship.

        def get_relationship_list(self, the_person, types = None, visible = None):
            return_list = []
            if isinstance(types, basestring):
                types = [types]
            for relationship in self.relationships:
                if (the_person.identifier == relationship._person_a and relationship._person_b and (types is None or relationship.type_a in types)) or \
                    (the_person.identifier == relationship._person_b and relationship._person_a and (types is None or relationship.type_b in types)): #What type we are looking at depends on if this is person A or B.
                    if visible is None or visible == relationship.visible:
                        return_list.append(relationship)

            return return_list

        def get_relationship_type_list(self, the_person, types = None, visible = None):
            return_list = []
            if isinstance(types, basestring):
                types = [types]
            for relationship in self.get_relationship_list(the_person, types, visible):
                other_person = relationship.get_other_person(the_person)
                if other_person:
                    return_list.append([other_person, self.get_relationship_type(the_person, other_person)]) #Creates a tuple of [Person, Type] for every entry in the list.
            return return_list

        def get_business_relationships(self, types = None): #Returns a list containing all relationships between people in your company.
            return_list = []
            if isinstance(types, basestring):
                types = [types]
            employee_list = mc.business.get_employee_list()
            for person in employee_list:
                for relationship in self.get_relationship_list(person, types):
                    if relationship.get_other_person_identifier(person.identifier) in [x.identifier for x in employee_list] and relationship not in return_list:
                        return_list.append(relationship)
            return return_list

        def get_relationship_type(self, person_a, person_b): #Note that getting relationship for (person_a, person_b) may yield a different result from (person_b, person_a), because the perspective is different.
            the_relationship = self.get_relationship(person_a, person_b)
            if the_relationship is not None:
                return the_relationship.get_type_by_identifier(person_a.identifier)
            return None

        def get_existing_children(self, the_person):
            return_list = []
            for relationship in self.get_relationship_type_list(the_person, "Daughter"):
                return_list.append(relationship[0])
            return return_list

        def get_existing_child_count(self, the_person): #Returns a count of how many children this character has who are "real" characters, vs just a stat.
            return len(self.get_existing_children(the_person))

        def remove_all_relationships(self, the_person): #Clears this person out of the relationship database (if, for example, we want to delete a person from the game)
            for relationship in self.get_relationship_list(the_person):
                self.relationships.remove(relationship)

        def improve_relationship(self, person_a, person_b, visible = None): #Improves a non-familial relationship between the two people.
            the_relationship = self.get_relationship(person_a, person_b)
            if the_relationship is not None: #If it exists we're going to improve it by one step, up to best friend.
                the_type = the_relationship.get_type_by_identifier(person_a.identifier)
                if the_type in self.relationship_scale: #You can only change non-family and non-romantic relationships like this.
                    the_state = self.relationship_scale.index(the_type)
                    the_state += 1
                    if the_state+1 >= len(self.relationship_scale): #Get the current state and increase it by one.
                        the_state = len(self.relationship_scale)-1

                    self.update_relationship(person_a,person_b, self.relationship_scale[the_state], visible)

            else:
                self.update_relationship(person_a, person_b, "Friend", visible)

        def worsen_relationship(self, person_a, person_b, visible = None): #Worsens a non-familial relationship between two people
            the_relationship = self.get_relationship(person_a, person_b)
            if the_relationship is not None: #If it exists we're going to improve it by one step, up to best friend.
                the_type = the_relationship.get_type_by_identifier(person_a.identifier)
                if the_type in self.relationship_scale: #You can only change non-family and non-romantic relationships like this.
                    the_state = self.relationship_scale.index(the_type)
                    the_state -= 1
                    if the_state < 0: #Get the current state and increase it by one.
                        the_state = 0

                    self.update_relationship(person_a,person_b, self.relationship_scale[the_state], visible)

            else:
                self.update_relationship(person_a, person_b, "Rival", visible)

        def begin_relationship(self, person_a, person_b, visible = None): #Sets their relationship to Acquaintance if they do not have one, otherwise leaves it untouched.
            the_relationship = self.get_relationship(person_a, person_b)
            if the_relationship is None: #Only sets a relationship for these people if one does not exist, so as to not override friendships or familial relationships
                self.update_relationship(person_a, person_b, get_random_from_weighted_list([[self.relationship_scale[1], 20], [self.relationship_scale[2], 60], [self.relationship_scale[3], 20]]))

        def is_family(self, person_a, person_b):
            return self.get_relationship_type(person_a, person_b) in ["Mother", "Daughter", "Sister", "Cousin", "Niece", "Aunt", "Grandmother", "Granddaughter"]
