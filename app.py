import os
from flask import Flask,render_template,request,session,flash,redirect,url_for
from flask_pymongo import PyMongo,DESCENDING
from bson.objectid import ObjectId 
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"]='myCookingDB'
app.config["MONGO_URI"]=os.getenv('MONGO_URI')
app.secret_key="some_secret"

mongo = PyMongo(app)

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
    return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
    port = int(os.environ.get('PORT')),
    debug = True)