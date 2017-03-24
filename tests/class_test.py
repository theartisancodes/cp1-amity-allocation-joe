import unittest
from modules.amity import Amity, Room
from modules.person import Person, Fellow, Staff
from modules.room import Office, LivingSpace


class TestClassInheritance(unittest.TestCase):
    def setUp(self):
        self.test_amity = Amity()
        self.living_space = LivingSpace()
        self.office = Office()
        self.room = self.office , self.living_space
        self.fellow = Fellow()
        self.staff = Staff()
        self.living_space = LivingSpace()
        self.office = Office()

    '''checks the class relationships'''

    def test_office_is_subclass(self):
        self.assertIsInstance(Office, Room)

    def test_living_space_is_subclass(self):
        self.assertIsInstance(LivingSpace, Room)

    def test_room_is_subclass(self):
        self.assertIsInstance(Room, Amity)

    def test_staff_is_subclass(self):
        self.assertIsInstance(Staff, Person)

    def test_fellow_is_subclass(self):
        self.assertIsInstance(Fellow, Person)

# create living space
    def test_create_living_space(self):
        self.new_room = Amity
        self.assertEqual(self.new_room.create_room, "Room Created")
# create living space

    def test_create_office(self):
        self.room = {"Name": ["Old Valyria"],Office:True, LivingSpace: False}
        self.assertEqual(1, len(self.office))

    def test_room_exists(self):
        self.find_room = Amity
        self.assertTrue(self.find_room.view_rooms, 'room exists')

    def test_office_has_space(self):
        self.office = {"Person": [5]}
        self.assertNotEqual(self.office, 'Sorry, Office is full')

    def test_living_space_has_space(self):
        self.living_space = {"Fellow": [3]}
        self.assertNotEqual(self.office, 'Sorry, Living space is full')

    def test_add_person(self):
        self.person = Person()
        self.new_person = self.staff or self.fellow
        self.assertTrue(self.new_person.add_person, True)
    # Test adding of new staff
    def test_add_staff(self):
        self.new_staff = self.staff
        self.assertEqual(self.new_staff.add_staff, "Staff Added")

    # Test adding of new fellow
    def test_add_fellow(self):
        self.new_fellow = self.fellow
        self.assertEqual(self.new_fellow.add_fellow, "Fellow Added")
    # Test person is a fellow
    def test_is_fellow(self):
        self.a_person = Fellow()
        self.assertTrue(self.a_person.is_fellow, msg= "Person is a fellow" )

    def test_is_staff(self):
        self.a_person = Staff
        self.assertTrue(self.a_person.is_staff,msg= "Person is a Staff" )
# Check name doesnt exist
    def test_name_exists(self):
        self.an_office = Amity()
        self.assertNotEqual(self.an_office.view_rooms, "Name exists")

    def test_check_duplicate_person_to_office(self):
        self.allocate_person = Person
        self.assertNotEqual(self.allocate_person.view_allocated,"Person already exists")

    def test_allocate_person(self):
        self.allocate_person = {"Person": ["id"], Staff:True, Fellow:True}

        self.assertTrue(self.allocate_person, True)


if __name__ == '__main__':
    unittest.main()
