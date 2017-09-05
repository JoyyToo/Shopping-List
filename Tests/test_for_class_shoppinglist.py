import unittest
from shoppflask.shoppinglist.Shopping import ShoppingList


class TestForClassListItems(unittest.TestCase):
    def setUp(self):
        self.lis = ShoppingList()

    # test for create list
    def test_for_empty_fields(self):
        result = self.lis.create_shoppinglist('', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_existing_list(self):
        self.lis.create_shoppinglist('Christmas dinner', 'must be')
        result = self.lis.create_shoppinglist('Christmas dinner', 'available before')
        self.assertEqual({"type": "error", "msg": "List already exist!!"}, result)

    # test for view list
    def test_for_non_existing_list(self):
        self.lis.view_shoppinglist('Christmas dinner')
        result = self.lis.view_shoppinglist('Christ dinner')
        self.assertEqual({"type": "error", "msg": "List does not exist"}, result, msg=None)

    # test for update list
    def test_for_empty_update_fields(self):
        result = self.lis.update_shoppinglist('', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_non_existing_update_list(self):
        self.lis.update_shoppinglist('Christmas dinner', 'must be')
        result = self.lis.update_shoppinglist('Christ dinner', 'available before')
        self.assertEqual({"type": "error", "msg": "List does not exist"}, result, msg=None)

    # test for delete list
    def test_for_delete_non_existing_list(self):
        self.lis.view_shoppinglist('Christmas dinner')
        result = self.lis.view_shoppinglist('Christ dinner')
        self.assertEqual({"type": "error", "msg": "List does not exist"}, result, msg=None)






