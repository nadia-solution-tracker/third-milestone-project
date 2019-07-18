import os
from flask import Flask,render_template,request,session,flash,redirect,url_for
from flask_pymongo import PyMongo,DESCENDING
from bson.objectid import ObjectId 
from flask_paginate import Pagination, get_page_args
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"]='myCookingDB'
app.config["MONGO_URI"]=os.getenv('MONGO_URI')
app.secret_key="some_secret"

mongo = PyMongo(app)
ITEMS_PER_PAGE = 6

@app.route('/')
def index():
    # Home page code 
    top_three_viewed_recipes=mongo.db.recipes.find().sort([('views',DESCENDING)]).limit(3)
    return render_template("index.html",recipes=top_three_viewed_recipes)
    
@app.route('/login',methods=['GET','POST'])
def login():
    # Login page checking for a valid or invalid user
    if request.method == 'POST':
        users = mongo.db.users
        # try and get one with same name as entered
        db_user = users.find_one({'user_name': request.form['user_name']})

        if db_user:
            # check password using hashing
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                             db_user['password']) == db_user['password']:
                session['user_name'] = request.form['user_name']
                session['logged_in'] = True
                # successful redirect to home logged in
                return redirect(url_for('index'))
            # must have failed set flash message
            flash('Invalid username/password combination','danger')
    return render_template("login.html")
    
@app.route('/logout')
def logout():
    """Clears session and redirects to home"""
    session.clear()
    return redirect(url_for('index'))
    
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'user_name' : request.form['user_name']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one(
              { 'user_name' : request.form['user_name'], 'password' : hashpass,'country_of_origin':request.form['country_of_origin'], 'email' : request.form['email'] } )
            session['user_name'] = request.form['user_name']
            return redirect(url_for('index'))
        
        flash('Username already exist','danger')

    return render_template('register.html')

@app.route('/add_recipe')
def add_recipe():
        return render_template('addrecipe.html',username=session['user_name'],
                    allergens=mongo.db.allergens.find(),
                    cuisines=mongo.db.cuisines.find(),
                    users=mongo.db.users.find())

                            
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    data=request.form.to_dict()
    data['allergen_name']=request.form.getlist('allergen_name')
    data['views']= 0
    data['upvotes']= 0
    data['user_name']=session['user_name']
    recipes.insert_one(data)
    return redirect(url_for('user_recipes'))

@app.route('/get_recipes')
def get_recipes():
    ITEMS_PER_PAGE=6
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = mongo.db.recipes.count_documents({})
    recipes_fetched = mongo.db.recipes.find().skip((page - 1)*ITEMS_PER_PAGE).limit(ITEMS_PER_PAGE)
    pagination = Pagination(page=page,
                            per_page=ITEMS_PER_PAGE,
                            total=total,
                            record_name='Recipes',
                            format_total=True,
                            format_number=True,
                            css_framework='foundation')
    return render_template('recipes.html',
                           recipes=recipes_fetched,cuisines=mongo.db.cuisines.find(),allergens=mongo.db.allergens.find(),
                           page=page,
                           per_page=per_page,
                           pagination=pagination)
                           

@app.route('/user_recipes')
def user_recipes():
    if not 'user_name' in session:
        return redirect('/login')
    else:
        #https://gist.github.com/Faizanq/a4d07f1a9624bdf6d3ddd9d4d6cc1b2d
        page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
        total = mongo.db.recipes.count_documents({})
        my_recipes_fetched = mongo.db.recipes.find().sort([('upvotes', DESCENDING)]).skip((page - 1)*ITEMS_PER_PAGE).limit(ITEMS_PER_PAGE)
        pagination = Pagination(page=page,per_page=ITEMS_PER_PAGE,total=total,record_name='Recipes')
        return render_template('userrecipes.html',recipes=my_recipes_fetched,username=session['user_name'],page=page,
                           per_page=per_page,
                           pagination=pagination)
    
if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
    port = int(os.environ.get('PORT')),
    debug = True)