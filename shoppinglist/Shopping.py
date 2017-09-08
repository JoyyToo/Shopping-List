"""ShoppingList class"""


class ShoppingList(object):
    """Shopping list class"""

    shoppinglist = {}

    priorities = [
        'High', 'Low', 'Medium'
    ]

    def __init__(self):
        """Initializes the class"""
        self.name = None
        self.desc = None
        self.priority = None

    def create_shoppinglist(self, name, desc):
        """Creates a shopping list"""
        if name and desc:
            if name in self.shoppinglist.keys():
                return {
                    "type": "error",
                    "msg": "List already exist!!"
                }
            self.shoppinglist[name] = {
                "name": name,
                "desc": desc,
            }
            return {
                "type": "success",
                "data": self.shoppinglist
            }
        return {
            "type": "error",
            "msg": "Please Fill all the fields"
        }

    def update_shoppinglist(self, name, desc):
        """Updates a shopping list"""
        if name and desc:
            # print (name, desc, self.shoppinglist[name], self.shoppinglist)
            if name not in self.shoppinglist.keys():
                return {
                    "type": "error",
                    "msg": "List does not exist"
                    }
            self.shoppinglist[name] = {
                "name": name,
                "desc": desc
            }
            print (self.shoppinglist)
            return {
                "type": "success",
                "data": self.shoppinglist
            }
        return {
            "type": "error",
            "msg": "Please Fill all the fields"
        }

    def view_shoppinglist(self, name):
        """Enables viewing of shopping list"""
        if name not in self.shoppinglist.keys():
            return {
                "type": "error",
                "msg": "List does not exist"
            }
        self.shoppinglist[name] = {
            "name": name
        }
        return {
            "type": "success",
            "data": self.shoppinglist.pop(name)
        }

    def delete_shoppinglist(self, name):
        """Enables deleting a shopping list"""
        if name not in self.shoppinglist.keys():
            return {
                "type": "error",
                "msg": "List does not exist"
            }
        self.shoppinglist[name] = {
            "name": name
        }
        return {
            "type": "success",
            "data": self.shoppinglist.pop(name)
        }

    def all_shoppinglist(self):
        """Enables viewing all lists"""
        return self.shoppinglist

    def single_shoppinglist(self, id):
        """Enables viewing single list"""
        return self.shoppinglist[id]
