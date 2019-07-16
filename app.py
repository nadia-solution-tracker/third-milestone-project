import os
from flask import Flask,render_template
from flask_pymongo import PyMongo,DESCENDING

app = Flask(__name__)

app.config["MONGO_DBNAME"]='myCookingDB'
app.config["MONGO_URI"]=os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def index():
    top_three_viewed_recipes=mongo.db.recipes.find().sort([('views',DESCENDING)]).limit(3)
    return render_template("index.html",recipes=top_three_viewed_recipes)
    
if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
    port = int(os.environ.get('PORT')),
    debug = True)