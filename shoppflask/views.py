"""flask module"""

from user.user import User
from flask import render_template, session
from flask import redirect
from flask import request
from shoppinglist.Shopping import ShoppingList
from shoppingitem.shoppinglist_items import ListItems
from shoppflask import app, user,shplist, shpitem


# app = Flask(__name__)
# user = User()
# shplist = ShoppingList()
# shpitem = ListItems()
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


# index
@app.route('/')
def home():
    """Defines landing page"""
    return render_template('index.html')


# about page
@app.route('/about')
def about():
    """Defines about page"""
    return render_template('about.html')


# login page
@app.route('/login', methods=["GET", "POST"])
def login():
    """Defines login page"""
    if 'logged_in' in session.keys():
        return redirect('/')
    data = None
    if request.method == 'POST':
        passwd = request.form['pass']
        email = request.form['email']

        data = user.login(passwd, email)

        if data['type'] == "success":
            session['logged_in'] = data['user_detail']
            return redirect('/shp')
    return render_template('login.html', data=data)


# sign up page
@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Defines sign up page"""
    if 'logged_in' in session.keys():
        return redirect('/')
    data = None
    if request.method == 'POST':
        name = request.form['name']
        passwd = request.form['pass']
        cpasswd = request.form['pass']
        email = request.form['email']

        data = user.register(name, passwd, email, cpasswd)
        if data['type'] == "success":
            return redirect('/login')
    return render_template('signup.html', data=data)


# logout page
@app.route('/logout')
def logout():
    """Defines logout page"""
    if 'logged_in' in session.keys():
        session.pop('logged_in', None)
    return redirect('/')


# shopping list
@app.route('/shoppinglist')
def view_shoppinglist():
    """Defines page to view shopping list"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shplist.all_shoppinglist()
    return render_template('viewshoppinglist.htm', data=data)


@app.route('/deleteitem/<string:id>')
def delete_shoppinglist(id):
    """Defines page to delete shopping list"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shplist.delete_shoppinglist(id)
    return redirect('/shoppinglist')


@app.route('/shoppinglist/<string:id>')
def single_shoppinglist(id):
    """Defines page to view single shopping list"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shplist.single_shoppinglist(id)
    return render_template('singleshoppinglist.htm', data=data)


@app.route('/shp', methods=["GET", "POST"])
def shoppinglist():
    """Defines page to create shopping lists"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = None
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']

        data = shplist.create_shoppinglist(name, desc)
        if "success" in data["type"]:
            return redirect('/shoppinglist')
    return render_template('shp.html', data=data)


@app.route('/updatelist/<string:item>', methods=['GET', 'POST'])
def updatelist(item):
    """Defines page to update shopping list"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    if request.method == "POST":
        name = request.form['name']
        desc = request.form['desc']
        shplist.update_shoppinglist(name, desc)
        return redirect('/shoppinglist')
    data = shplist.single_shoppinglist(item)
    return render_template('updateshoppinglist.html', data=data)


@app.route('/additem/<string:shopping>', methods=["GET", "POST"])
def shoppingitems(shopping):
    """Defines page to add items to list"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = None
    shopping = shopping
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        cat = request.form['cat']

        data = shpitem.add_item(name, amount, cat, shopping)

        if "success" in data["type"]:
            return redirect('/shoppinglist')
    return render_template('additem.html', data=data)


@app.route('/shoppingitems/<string:id>')
def single_shoppinglistitem(id):
    """Defines viewing shopping list items"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shpitem.view_item(id)
    return render_template('singleshoppinglistitem.html', data=data)


@app.route('/deleteshpitem/<string:id>')
def delete_shoppinglistitem(id):
    """Defines page to delete items in list"""
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shpitem.delete_item(id)
    return redirect('/shoppinglist')


@app.route('/updateshpitem/<string:item>', methods=['GET', 'POST'])
def updateitems(item):
    """Defines page to update items in list"""
    if 'logged_in' not in session.keys():
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        cat = request.form['cat']
        shopping = request.form['shopping']

        shpitem.update_item(name, amount, cat, shopping)

        return redirect('/shoppingitems/'+shopping)

    data = shpitem.singleItem(item)
    return render_template("updateitem.html", data=data)

# if __name__ == '__main__':
#     app.run(debug=True)
