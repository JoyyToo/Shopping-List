class ShoppingList(object):

    shoppinglist = {}

    priorities = [
        'High', 'Low', 'Medium'
    ]

    def __init__(self):
        self.name = None
        self.desc = None
        self.priority = None

    def create_shoppinglist(self, name, desc):

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
        if name and desc:

                if name not in self.shoppinglist.keys():
                    return {
                        "type": "error",
                        "msg": "List does not exist"
                     }
                self.shoppinglist[name] = {
                    "name": name,
                    "desc": desc
                }
                return {
                    "type": "success",
                    "data": self.shoppinglist
                }
        return {
            "type": "error",
            "msg": "Please Fill all the fields"
        }

    def view_shoppinglist(self, name):
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
        return self.shoppinglist

    def single_shoppinglist(self, id):
        return self.shoppinglist[id]


