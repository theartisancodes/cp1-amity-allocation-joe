
"""This is an application that models room allocation for Andela """


class Amity(object):

    def __init__(self):
        pass

    def __len__(self):
        return len([])

# Creates rooms in Amity
    def create_room(self):

        pass

# allocate room type

    def choose_room_type(self):
        pass

    def office_has_space(self):
        pass

    def living_space_has_space(self):
        pass

# view rooms

    def view_rooms(self):
        pass

# Reallocate the person with person_identifier to new_room_name.

    def reallocate_person(self):
        pass

# Prints a list of allocations

    def print_allocations(self):
        pass

# Prints a list of unallocated

    def print_unallocated(self):
        pass


class Room (Amity):
    def __init__(self, office, living_space):

        self.Office = office
        self.Living_space = living_space
        pass






