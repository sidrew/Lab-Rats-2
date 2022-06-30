init 0 python:
    class TestSerumInventory(unittest.TestCase):
        def test_init(self):
            test_inventory = SerumInventory()

            self.assertIsInstance(test_inventory, SerumInventory)

        def test_change_count(self):
            test_inventory = SerumInventory()
            test_design_one = SerumDesign()
            test_design_two = SerumDesign()
            test_design_two.name = "Other!"

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 0)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0)

            test_inventory.change_serum(test_design_one, 0)

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 0)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0)

            test_inventory.change_serum(test_design_one, 1)

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 1)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0)

            test_inventory.change_serum(test_design_one, 2)

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 3)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0)

            test_inventory.change_serum(test_design_two, -1)

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 3)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0)

            test_inventory.change_serum(test_design_one, -1)

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 2)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0)

        def test_get_any_serum_count(self):
            test_inventory = SerumInventory()
            test_design_one = SerumDesign()
            test_design_two = SerumDesign()
            test_design_two.name = "Other!"

            self.assertEqual(test_inventory.get_any_serum_count(), 0)

            test_inventory.change_serum(test_design_one, 2)

            self.assertEqual(test_inventory.get_any_serum_count(), 2)

            test_inventory.change_serum(test_design_two, 3)

            self.assertEqual(test_inventory.get_any_serum_count(), 5)

            test_inventory.change_serum(test_design_one, -1)

            self.assertEqual(test_inventory.get_any_serum_count(), 4)

            test_inventory.change_serum(test_design_two, -1)

            self.assertEqual(test_inventory.get_any_serum_count(), 3)

            test_inventory.change_serum(test_design_two, -10)

            self.assertEqual(test_inventory.get_any_serum_count(), 1)

        def test_get_serum_type_list(self):
            test_inventory = SerumInventory()
            test_design_one = SerumDesign()
            test_design_two = SerumDesign()
            test_design_two.name = "Other!"

            self.assertIsInstance(test_inventory.get_serum_type_list(), list)

            test_inventory.change_serum(test_design_one, 2)

            self.assertIn(test_design_one, test_inventory.get_serum_type_list())
            self.assertNotIn(test_design_two, test_inventory.get_serum_type_list())

            test_inventory.change_serum(test_design_two, 1)

            self.assertIn(test_design_one, test_inventory.get_serum_type_list())
            self.assertIn(test_design_two, test_inventory.get_serum_type_list())

            test_inventory.change_serum(test_design_one, -2)

            self.assertNotIn(test_design_one, test_inventory.get_serum_type_list())
            self.assertIn(test_design_two, test_inventory.get_serum_type_list())

        def test_add_similar_serum(self):
            test_inventory = SerumInventory()
            test_design_one = SerumDesign()
            test_design_two = SerumDesign()
            test_design_three = SerumDesign()
            test_design_three.name = "Other!"

            self.assertIsInstance(test_inventory.get_serum_type_list(), list)
            self.assertEqual(test_inventory.get_serum_count(test_design_one), 0)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0) # Should be the same as one
            self.assertEqual(test_inventory.get_serum_count(test_design_three), 0)

            test_inventory.change_serum(test_design_one, 1)
            test_inventory.change_serum(test_design_two, 2)
            test_inventory.change_serum(test_design_three, 10)

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 3)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 3)
            self.assertEqual(test_inventory.get_serum_count(test_design_three), 10)

            test_design_two.name = "Other!" #Now looks the same as 3

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 3)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 10)
            self.assertEqual(test_inventory.get_serum_count(test_design_three), 10)

            test_inventory.change_serum(test_design_two, 5) #Should change the count of both two and 3

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 3)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 15)
            self.assertEqual(test_inventory.get_serum_count(test_design_three), 15)

            test_design_two.name = "None!" #Now looks like none of them.

            self.assertEqual(test_inventory.get_serum_count(test_design_one), 3)
            self.assertEqual(test_inventory.get_serum_count(test_design_two), 0)
            self.assertEqual(test_inventory.get_serum_count(test_design_three), 15)
