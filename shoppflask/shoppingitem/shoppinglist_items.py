"""ShoppingList items class"""


class ListItems(object):
    """
    Users can add, update, view or delete items in a shopping list
    """

    items = {}
    categories = [
        'Groceries', 'Bathroom Supplies', 'Household Supplies',
        'Office Supplies', 'Kitchen Supplies']

    def __init__(self):
        """Initializes the class"""
        self.name = None
        self.category = None
        self.amount = None

    def add_item(self, name, amount, category, bucket):
        """Add items to a list"""

        if name != '' and amount != '' and category != '':
            if name in self.items.keys():
                return {
                    "type": "error",
                    "msg": "Item already in list"
                }
            self.items[name] = {
                "name": name,
                "amount": amount,
                "cat": category,
                "bucket": bucket
            }
            return {
                "type": "success",
                "msg": "Item successfully added"
            }
        return {
            "type": "error",
            "msg": 'Fill in all fields'
        }

    def update_item(self, name, amount, category):
        """Update items in a list"""
        if name and amount and category:
            if self.name in self.items:
                # returns original list under specificed list name
                original_list = self.items[self.name]
                # remove the original list name
                original_list.remove(self.name)
                # updated list by substituting names
                original_list.append(self.amount)
                temporary_dict = {self.name: original_list}
                del self.items[self.name]
                self.items.update(temporary_dict)
                return self.items
            else:
                return {
                    'type': 'error',
                    'msg': 'Item unavailable'
                }
        else:
            return {
                "type": "error",
                "msg": 'Fill in all fields'
            }

    def view_item(self, name):
        """User can view items in a list"""
        data = []
        if self.items:
            for item in self.items:
                if self.items[item]['bucket'] == name:
                    data.append(self.items[item])
            if data:
                return {
                    "type": "success",
                    "data": data
                }
        return {
            "type": "error",
            "msg": "Items not available at the moment."
        }

    def delete_item(self, name):
        """Delete items in a list"""
        self.name = name
        if self.name in self.items.keys():
            self.items.pop(self.name)

            return {
                "msg": "Item deleted successfully",
                "data": self.items
            }

        else:
            return {
                'type': 'error',
                'msg': 'Item unavailable'
            }

    def save(self, id):
        """Saves items entered in a list"""
        if self.category in self.categories:
            if self.name not in self.items.keys():
                self.items[self.name] = {
                    'name': self.name,
                    'category': self.category,
                    'amount': self.amount
                    }
                return {
                    "msg": "success",
                    "data": self.items.keys()
                }
            else:
                return {
                    'type': 'error',
                    'msg': 'Item not in list'
                }
        else:
            return {
                'type': 'error',
                'msg': 'Category Unrecognized'
            }

    def updatedata(self):
        """Updates items entered in a list"""
        if self.name in self.items.keys():
            self.items[self.name] = {
                'name': self.name,
                'category': self.category,
                'amount': self.amount
            }
            return {
                "type": "success",
                "data": self.items
            }
        else:
            return {
                'type': 'error',
                'msg': 'Category Unrecognized'
            }
