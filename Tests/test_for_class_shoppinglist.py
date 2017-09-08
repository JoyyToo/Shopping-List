"""Test for user class"""

import unittest
from ShoppingList.shoppinglist.Shopping import ShoppingList


class TestForClassListItems(unittest.TestCase):
    """Test for user class"""
    def setUp(self):
        """Initializes test for user Class"""
        self.lis = ShoppingList()

    # test for create list
    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.lis.create_shoppinglist('', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_existing_list(self):
        """Test for existing list"""
        self.lis.create_shoppinglist('Christmas dinner', 'must be')
        result = self.lis.create_shoppinglist('Christmas dinner', 'available before')
        self.assertEqual({"type": "error", "msg": "List already exist!!"}, result)

    # test for view list
    def test_for_non_existing_list(self):
        """Test for non-existing field"""
        self.lis.view_shoppinglist('Christmas dinner')
        result = self.lis.view_shoppinglist('Christ dinner')
        self.assertEqual({"type": "error", "msg": "List does not exist"}, result, msg=None)

    # test for update list
    def test_for_empty_update_fields(self):
        """Test for empty update fields"""
        result = self.lis.update_shoppinglist('', '')
        self.assertEqual({"type": "error", "msg": "Please Fill all the fields"}, result)

    def test_for_missing_update_list(self):
        """Test for non-existing update list"""
        self.lis.update_shoppinglist('Christmas dinner', 'must be')
        result = self.lis.update_shoppinglist('Christ dinner', 'available before')
        self.assertEqual({"type": "error", "msg": "List does not exist"}, result, msg=None)

    # test for delete list
    def test_for_delete_missing_list(self):
        """Test for non-existing delete list"""
        self.lis.view_shoppinglist('Christmas dinner')
        result = self.lis.view_shoppinglist('Christ dinner')
        self.assertEqual({"type": "error", "msg": "List does not exist"}, result, msg=None)
