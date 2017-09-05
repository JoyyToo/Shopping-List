from flask import Flask, render_template, session, url_for
from flask import redirect
from flask import request
from shoppflask.shoppinglist.Shopping import ShoppingList
from user.user import User
from shoppingitem.shoppinglist_items import ListItems


app = Flask(__name__)
user = User()
shplist = ShoppingList()
shpitem = ListItems()
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=["GET", "POST"])
def login():
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


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if 'logged_in' in session.keys():
        return redirect('/')
    if request.method == 'POST':
        name = request.form['name']
        passwd = request.form['pass']
        cpasswd = request.form['pass']
        email = request.form['email']

        data = user.register(name, passwd, email, cpasswd)
        if data['type'] == "success":
            return redirect('/login')
    return render_template('signup.html')


@app.route('/logout')
def logout():
    if 'logged_in' in session.keys():
        session.pop('logged_in', None)
    return redirect('/')


# shopping list
@app.route('/shoppinglist')
def view_shoppinglist():
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shplist.all_shoppinglist()
    print(data)
    return render_template('viewshoppinglist.htm', data=data)


@app.route('/deleteitem/<string:id>')
def delete_shoppinglist(id):
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shplist.delete_shoppinglist(id)
    return redirect('/shoppinglist')


@app.route('/shoppinglist/<string:id>')
def single_shoppinglist(id):
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shplist.single_shoppinglist(id)
    return render_template('singleshoppinglist.htm', data=data)


@app.route('/shp', methods=["GET", "POST"])
def shoppinglist():
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = None
    print("Add shopping")
    if request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']

        data = shplist.create_shoppinglist(name, desc)
        if "success" in data["type"]:
            return redirect('/shoppinglist')
    return render_template('shp.html', data=data)


@app.route('/updatelist/<string:id>', methods=['GET', 'POST'])
def updatelist(id):
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shplist.delete_shoppinglist(id)
    return redirect('/shp')


@app.route('/additem/<string:id>', methods=["GET", "POST"])
def shoppingitems(id):
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = None
    print(data)
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        cat = request.form['cat']

        data = shpitem.add_item(name, amount, cat)
        if "success" in data["type"]:
            return redirect('/shoppinglist')
    return render_template('additem.html', data=data)


@app.route('/shoppingitems/<string:id>')
def single_shoppinglistitem(id):
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shpitem.save(id)
    print(data)
    return render_template('singleshoppinglistitem.html', data=data)

#
# @app.route('/shoppingitem')
# def view_shoppinglistitem():
#     if 'logged_in' not in session.keys():
#         return redirect('/login')
#     data = shpitem.all_shoppinglistitems()
#     return redirect('/singleshoppinglistitem.html')


@app.route('/deleteitem/<string:id>')
def delete_shoppinglistitem(id):
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shpitem.delete_item(id)
    return redirect('/additem/<string:id>')


@app.route('/updatelist/<string:id>', methods=['GET', 'POST'])
def updateitems(id):
    if 'logged_in' not in session.keys():
        return redirect('/login')
    data = shpitem.delete_item(id)
    return redirect('/additem')


if __name__ == '__main__':
    app.run(debug=True)
