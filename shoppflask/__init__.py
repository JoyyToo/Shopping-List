from flask import Flask
from shoppinglist.Shopping import ShoppingList
from shoppingitem.shoppinglist_items import ListItems
from user.user import User

app = Flask(__name__, instance_relative_config=True)
user = User()
shplist = ShoppingList()
shpitem = ListItems()
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from shoppflask import views