import unittest
from shoppflask.shoppingitem.shoppinglist_items import ListItems


class TestForClassListItems(unittest.TestCase):
    def setUp(self):
        self.item = ListItems()

    # tests for add item function
    def test_for_empty_fields(self):
        result = self.item.add_item('', '', '')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_name_field(self):
        result = self.item.add_item('', '3 pieces', 'Bathing Supplies')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_amount_field(self):
        result = self.item.add_item('soap', '', 'Bathing Supplies')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_category_field(self):
        result = self.item.add_item('soap', '3 pieces', '')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_item_in_list(self):
        self.item.add_item('soap', '3 pieces', 'Bathroom Supplies')
        result = self.item.add_item('soap', '3 pieces', 'Bathroom Supplies')
        self.assertEqual({"type": "error", "msg": "Item already in list"}, result, msg=None)

    # tests for update item function
    def test_for_empty_update_fields(self):
        result = self.item.update_item('', '', '')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_update_name_field(self):
        result = self.item.update_item('', '3 pieces', 'Bathing Supplies')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_update_amount_field(self):
        result = self.item.update_item('soap', '', 'Bathing Supplies')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_empty_update_category_field(self):
        result = self.item.update_item('soap', '3 pieces', '')
        self.assertEqual({"type": "error", "msg": 'Fill in all fields'}, result, msg=None)

    def test_for_update_a_missing_item(self):
        self.item.update_item('soap', '3 pieces', 'Bathroom Supplies')
        result = self.item.update_item('ginger', '3 pieces', 'Bathroom Supplies')
        self.assertEqual({"type": "error", "msg": "Item Unavailable"}, result, msg=None)

    # tests for view item function
    def test_for_view_a_missing_item(self):
        self.item.view_item('soap')
        result = self.item.view_item('ginger')
        self.assertEqual({"type": "error", "msg": "Item Unavailable"}, result, msg=None)

    # tests for save item function
    def test_for_item_of_missing_category(self):
        result = self.item.save()
        self.assertEqual({'type': 'error', 'msg': 'Category Unrecognized'}, result, msg=None)
        self.assertEqual({'type': 'error', 'msg': 'Category Unrecognized'}, result, msg=None)


if __name__ == '__main__':
    unittest.main()





