"""Test for User class"""

import unittest
from ShoppingList.shoppingitem.shoppinglist_items import ListItems


class TestForClassListItems(unittest.TestCase):
    """Test for User class"""
    def setUp(self):
        """Initializes test for listitems Class"""
        self.item = ListItems()

    # tests for add item function
    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.item.add_item('', '', '', '')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_name_field(self):
        """Test for empty name field"""
        result = self.item.add_item('', '3 pieces', 'Bathing Supplies', 'sp')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_amount_field(self):
        """Test for empty amount field"""
        result = self.item.add_item('soap', '', 'Bathing Supplies', 'sp')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_category_field(self):
        """Test for empty category field"""
        result = self.item.add_item('soap', '3 pieces', '', 'sp')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_item_in_list(self):
        """Test for item in list"""
        self.item.add_item('soap', '3 pieces', 'Bathroom Supplies', '')
        result = self.item.add_item('soap', '3 pieces', 'Bathroom Supplies', '')
        self.assertEqual({"type": "error", "msg": "Item already in list"}, result, msg=None)

    # tests for update item function
    def test_for_empty_update_fields(self):
        """Test for empty update field"""
        result = self.item.update_item('', '', '', '')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_uname_field(self):
        """Test for empty update name field"""
        result = self.item.update_item('', '3 pieces', 'Bathing Supplies', 'shopping')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_uamount_fields(self):
        """Test for empty update amount field"""
        result = self.item.update_item('soap', '', 'Bathing Supplies', 'shopping')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_ucategory_field(self):
        """Test for empty update category field"""
        result = self.item.update_item('soap', '3 pieces', '', 'shopping')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_update_a_missing_item(self):
        """Test for update missing item"""
        self.item.update_item('soap', '3 pieces', 'Bathroom Supplies', 'shopping')
        result = self.item.update_item('ginger', '3 pieces', 'Bathroom Supplies', 'shopping')
        self.assertEqual({"type": "error", "msg": "Item unavailable"}, result, msg=None)

    # tests for view item function
    def test_for_view_a_missing_item(self):
        """Test for view missing item"""
        self.item.view_item('soap')
        result = self.item.view_item('ginger')
        self.assertEqual({"type": "error", "msg": "Items not available at the moment."},
                         result, msg=None)

    # tests for save item function
    def test_for_missing_category_item(self):
        """Test for item missing category"""
        result = self.item.save('')
        self.assertEqual({'type': 'error', 'msg': 'Category Unrecognized'}, result, msg=None)

if __name__ == '__main__':
    unittest.main()
