class ListItems(object):
    """
    Users can add, update, view or delete items in a shopping list
    """

    items = {}
    categories = [
        'Groceries', 'Bathroom Supplies', 'Household Supplies', 'Office Supplies', 'Kitchen Supplies']

    def __init__(self):
        self.name = None
        self.category = None
        self.amount = None

    def add_item(self, name, amount, category):
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
                "cat": category
            }

            print(self.items)
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
        self.name = name
        self.amount = amount
        self.category = category
        if self.name != '' and self.amount != '' and self.category != '':
            if self.name in self.items.keys():
                return {
                    "type": "success",
                    "data": self.updatedata()
                }
            else:
                return {
                    "type": "error",
                    "msg": "Item Unavailable"
                }
        else:
            return {
                "type": "error",
                'msg': 'Fill in all fields'
            }

    def view_item(self, name):
        """User can view items in a list"""
        sl = []
        if name not in self.items.keys():
            return {
                "type": "error",
                "msg": "Item Unavailable"
            }
        self.items[name] = sl.append(name)
        return {
            "type": "success",
            "data": self.items.pop(name)
        }

    def delete_item(self, name):
        """Delete items in a list"""
        self.name = name
        if self.name in self.items.keys():
            return {
                "msg": "Item deleted successfully",
                "data": self.items.pop(self.name)
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
        if self.category in self.categories:
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

    def all_shoppinglistitems(self):
        return self.items

    def single_shoppinglistitem(self, id):
        return self.items[id]


