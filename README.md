# [KITCHEN STATION COOKING APP](https://kitchen-station.herokuapp.com/)

### Overview of the project

- Kitchen Station shares the highlights, discoveries and the recipes of the food you love to cook. With this easy-to-use recipe creation application, you can add / edit / delete /view recipes, ideas and photos in minutes. 
- Kitchen Station offers a large database of recipes that are made by different cooking experts, chefs and simply housewives who love to cook and like to experiment new dishes every day. The app offers the best and large categories of recipes.

![IMAGE](static/images/homepagesnapshot.jpg)

## UX
### Insights of the project
- Registering yourself to the application to access all the features of the app.
- Login to create and edit recipes for the world to see.
- Create your own recipe and save it.
- Create and save, edit and delete your cook book like normal physical diary.
- Like and View the recipes of other cooks.
- Large database of recipes from different cuisines and countries.
- Searching and Filtering recipes based on different attributes such as cuisines, allergens, meals and searching based on any recipes, ingredients or keywords
- Ordering recipes on reasonable aspects like “most liked” and “most popular” recipes
- Social community to share recipes and inspire others.
- Gain confidence in your cooking abilities

#### User Stories

**"Kate loves cooking and wants to share her own personal recipes to the world"**
- As a user,  Kate can register into the application by clicking the **Register** link on the navigation menu at the top, this will bring Kate a user entry form which when complete creates a new user account for Kate and presents additional features of the application where she can now create her personal food diary
- As a user,  Kate can login into the application by click the **Login link** on the navigation menu at the top ,fill up validate entries so that the it presents her the preferences.
- As a user Kate can create her own recipes and add it and also manage her cooking diary.
- As a user Kate can also View other chefs recipes and Like them

**"Richard wants to prepare a nice meal for his wife and want to access the web application to check out some nice dinner ideas”**
- As a user, Richard is provided with a search feature to search recipes by clicking the **Recipe** link on the navigation menu or the **View All recipes** button on the home page and searchh on any field he would like ,this would also include any kind of ingredients he has in his kitchen.
- As a user , Richard is provided with drop down filters based on Cuisine, Allergen and Meal clicking any one drop down or a combination of filters would give Richard the best recipe he would want to make.
- As a user, Richard can also type keywords in the text field this would include ingredient name, recipe name or any kind of keywords and would present Richard with a huge list of Recipes, count of the recipes will be displayed on the top, he could navigate through the list by clicking on the page number links provided at the bottom of the page.
- As a user ,Richard can also fasten his search by checking the Most popular Recipes or the Most viewed recipes button this would order recipes from the highest rating to the lowest rating.
- Once Richard has decided on what he wants to cook ,he can click on the view recipe button to get details like ingredients and method to prepare the recipe.
- Finally Richard can also give a vote if the recipe has been good enough to impress his wife.

**"As a first time user browsing the application"**
- As a user who is browsing through the web application he/she can also click on images provided in the recipe card to see a zoomed in image of the recipe.
- As a user , you can browse through the list of existing recipes by click the link **"RECIPES"** on the menu or the **"View All Recipes"** buuton on the home page.
- Finally as a user, you can View the details of Recipe and Cast a vote if you like it.
- As a user ,search facilties are also provided based on different user criterias in form of drop downs as well as typing in keywords

#### Design Process

[Schema diagram](https://www.dropbox.com/sh/mhe9ef9eevfb536/AAB9BvERCM2JlNUQuhLKDavta?dl=0)<br/>
While working on the application new features and changes were made on the design of the wireframe<br/>
[Wireframes for Desktop](https://www.dropbox.com/sh/p5v46s3obnoddtc/AACUqugEnEjXy9dlTMVsDK7Fa?dl=0)<br/>
[Wireframes for IPhone](https://www.dropbox.com/sh/zwvda3088wef633/AABq133OKwyu9Iegan9Etke6a?dl=0)<br/>
[Wireframes for IPad](https://www.dropbox.com/sh/6nywq8sldsm1ewv/AAA903PRicdp6xeNwA5No1M0a?dl=0)<br/>


## Features

#### Existing Features

The following features are added to the application which is geared towards enhancing the user online experience.  This multipage application provides a menu to access the various features of the application

**Home**- serves as an initial landing page for all users. Users are able to access the following :
- A static clickable navigation menu with items like Home, Recipes , Login, Register
- Have a snick pick at the top 3 most popular recipes as card.
- Clicking an image recipe in the card opens up the image to have a better look of the dish
- A **View Recipe** button that will redirect you to the detailed recipe.
- View all recipes store in the database either by clicking the **Recipe** link on the menu or the **View all Recipes** button on the home page.
- Search provided at the footer of the page to Search recipes by food title, multiple ingredients or any other keywords.
- A Carousal displaying 5 random images from different websites at a set interval.
- If a valid user logs in displays a message "Welcome <username>"

*Pages created:* base.html and index.html

**Register**- registering yourself to the application provides the following features: 
- Upon clicking the register the user is provide an input form to enter details like username, password, country of origin and email address
- The Register form provides validations for fields that are required and also checks it the username exists
- Submitting the form creates an account for the user where the user is provide with a home page and clickable menu which now includes additional features Home, Recipes, Add Recipes ,My Recipes(Personal cookbook diary),Logout
- The new user can also view all the recipes store in the database either by clicking the **Recipe** link on the menu or the **View all Recipes** button on the home page.
- Clicking on the Logout initiates a session time out and the user lands again on the home page with the additional features removed

*Pages created:*–register.html

**Login** – this creates an entry for returning users with existing accounts to manage their recipes
- Provide a link to **Sigin up** if the user has not yet logged in
- Clicking the login on the menu, directs the user to an input form to enter login details like username and password
- The Login form provides validations for fields that are required and also checks if login is successful
- Signing in the form creates opens the home page and clickable menu which now includes additional features Home, Recipes, Add Recipes ,My Recipes(Personal cookbook diary),Logout
- The new user can also view all the recipes store in the database either by clicking the **=Recipe** link on the menu or the **View all Recipes** button on the home page.
- Clicking on the Logout initiates a session time out and the user lands again on the home page with the additional features removed

*Pages created:*-login.html

**Recipes**- this page displays a wide collection of recipes creates by different cooking experts, chefs, housewives and logged in users.

The search section
- Provides a clickable drill down for a filtered view based on the following criteria Cuisines ,Allergens and Meals
- Search option - search for recipes by dishes names, most important by ingredients name or keywords that you have at your home.
- Ordering buttons are added to order recipes on the following aspects “Most popular” (upvotes) and “Most Viewed” (likes) recipes

The recipe collection section
- Displays Number of recipes on the current page from the total list of recipes ex **displaying 1 - 6 Recipes in total 8**
- When this page is first time loaded a list of recipes are displayed in which the user can browse.
- Pagination feature is incorporated so that users do not get lost and can concentrate on a particular amount of content, the page display 6 recipes at each time. The user can view the list of next 6 recipes by clicking on the pagination links provided at the bottom of the page.
- Each recipe card has link to View recipe (details about the recipe), number of likes and number of views. This would also help users to browse a recipe that is most liked by people or have most views.
- Clicking any card images of the recipe opens up the image to have a better view of the dish

*Pages created:*-recipes.html

**Searched Recipes** – this page displays list of recipes based on filtered criteria
- Provides users with recipe cards of recipes based on search criteria
	**Results for: butter**
- Displays Number of recipes on the current page from the total list of recipes ex **displaying 1 - 1 Recipes in total 1**
- The user can also get back to the recipe page by clicking a **Go Back to Recipe Page** button or the **Recipes** link in the menu.
- Pagination feature is incorporated so that users do not get lost and can concentrate on a particular amount of content, the page display 6 recipes at each time. 
- The user can view the list of next 6 recipes by clicking on the pagination links provided at the bottom of the page.

*Pages created:*-search.html

**Ordering Recipes**- Provides ordering of recipes 
- Users are able to view an ordering of recipes based on “Most popular" and "Most Viewed”
- This page has a same layout as the search Recipe page.

*Pages created:*-orderingrecipes.html 

**Add Recipe**- This page provides a kind of an editor for users to write recipes. 

The following fields attributes to creating a recipe
RecipeName, ShortDescription, Cusine, Allergens, Meal, Serves, Preptime, CookingTime, ImageUrl, Ingredients and Method
- All registered users can add a recipe to the database. If a user does not have an account they can create one at the start of the app - once they have an account they are free to add recipes to the database.
- The input field, drop downs are validated as required before the user submits the recipe.
- Attributes like Prep time and Cooking time opens up a time picker that allows the user to select the time from a clock.
- Attributes like Cuisine ,allergens and meal type are provided to the user as a drop down and a Multiselect dropdown. The values are fetched from the databases.
- Placeholders are provided with instructions for ingredients and method so that the user is aware of how they can write the fields.
- Submitting the recipes added the recipe to the collection of recipes and also to the users account **My Recipes** which provides a kind of a personal cookbook diary for the user with features like Edit and Delete.

*Pages created:*-addrecipe.html

**My Recipes**- provides a personal cookbook diary for a registered user
- Displays recipe cards for all recipes created by that user.
- Provides view ,edit, delete features to every recipe card.
- Also display pagination info and links on top and bottom of the page respectively to improve the readability score of the content.
- Clicking the **View** button presents a detailed view of the recipe
- Clicking the **Edit** button present a editable form so changes can be made to an users existing recipe
- Clicking the **Delete** button pops up a confirmation to the user asking if he/she is sure of deleting the recipe

*Pages created:*-userrecipes.html

**Edit Recipe**- editing to add and improve on your data
- Provide a form similar to the Add recipe form but in this case the user recipe collection is accessed for a particular item that needs to be edited
- Upon clicking submit, the recipe is updated and doesn’t add a new recipe into the database.

*Pages created:*-editrecipe.html


**Delete Recipe**- removes the recipe from the user’s collection of recipes as well as the recipe database
- Provides a Delete button to delete the recipe from the database

**View Recipe**-
- individual recipe page  accessed through clicking the **View recipe** button. 
- It uses an entire page to display a full recipe with larger text and the recipe image at its full capacity to the user. 
- Upon viewing it increments the recipe view count. Any user can also give a vote on the recipe by clicking the thumbs-up icon.
- If a valid user has logged in he/she will not be able to Like his/her own recipe but if provided a feature of liking other users recipes.

*Page created:* viewrecipe.html

#### Features Left to Implement
- An advanced search on more aspects and criteria’s this might require me to change the recipe collection in the mongodb.
- Adding reviews on recipes so users are able to explore the recipe a bit more and building connections with other cooks.
- Creating a more dynamic input adder/remover button for ingredients and method so that user can step by step instructions by clicking on add button

![IMAGE](static/images/dynamicadder.jpg)

- Responsive Charts - Use the dc.js library where on clicking each bar it would drill down into other bar chart results to compare data.

## Technologies Used
**Python 3**
- Backend Language for creating web applications.
- To determine what content to show a user and what actions to take.

**Flask**
- Python web Framework
- Running a Python server based project
- Serving HTML files from backend
- Writing Python logic inside of our HTML files
- Post data from HTML form to backend
- Make code reusable by using template logic

**Heroku** <link>(https://www.heroku.com/)
- Deploy and scale Python apps

**MongoDb Atlas** <link>(https://www.mongodb.com/)
- Backend database
- Python3 with Flask is used to interact with the database data, to database to perform CRUD operations
- Project has 5 collection as shown in schema above
- Created a .bashrc file to save the mongo URI 

**Materialize Css**- Materialize 0.100.2<link>(https://materializecss.com/)
- Frontend framework version 
- The project uses the Materialise css/javascript library to design and develop the form, buttons, lists, nav, side nav, list box and drop down elements.

**JQuery**
- This project uses Jquery to simplify DOM manipulation and provide better UX.
- Used to enable Materialize functionality, including select forms, sidenavs, character counter, and tabs


**HTML5** : to create structure of webpage.<br/>
**CSS3**: to style webpage, I used external stylesheet, file located in static/css/styles.css .<br/>
**Google Fonts**: for additional font-family options https://fonts.google.com/.<br/>
**Font Awesome**: for social media icons and envelope icon https://fontawesome.com/.<br/>
**Start Bootstrap**: Bootstrap starter template perfect for building websites https://startbootstrap.com/templates/small-business/<br/>


**Online software for drawing Wireframes and Schema Design**<br/>
Wireframe : https://wireframepro.mockflow.com<br/>
Wireframe :https://ninjamock.com/Designer/Workplace<br/>
Schema: https://www.draw.io/<br/>

**Installs made to the project**

- `~/workspace $ sudo pip3 install Flask`
- `~/workspace $ sudo pip3 install dnspython`
- `~/workspace $ sudo pip3 install pymongo`
- `~/workspace $ pip3 install –U flask-paginate`
- `~/workspace $ pip3 install flask-bcrypt `


## Testing
- The web application has been tested to make it responsive this is tested in Google Chrome Developer tools responsive mode on Galaxy S5, Pixel 2, Pixel 2XL,iPhone 5/SE, iPhone 6/7/8, iPhone Plus 6/7/8, iPhone X, iPad, iPad Pro.
- Web application is also been viewed on different browsers like Google Chrome,Firefox and Internet Edge
- Tested button and links directed to desired page.

#### Testing scenarios

**Home(index.html)**–*"Test PASS"*

- The home page is responsive and conforms to the browser size. 
- The navigation bar collapses to a burger icon when viewed on medium and small devices. On hovering on each of the link the color it highlights the active link, however Home link is active by default
- Tested every link on the navigation bar and verified that I was directed to the appropriate sections.
- Tested that clicking on the recipe image pops up the image to a larger view.

**Footer- Social media **
- Social media links - Clicked the social media icons i.e. github and confirmed it directs you to the desired site.
- On small devices the social media and copyright are centered on the webpage.
- Confirmed the search field works efficiently for any search criteria submitted.

**Recipes link(recipes.html)** –*"Test PASS"*
- Clicking the “Recipes” link takes me to a new webpage. 
- This responsive webpage has a layout with navigation and header image. The header image is made responsive this is achieved using VH (percent of view height) units.
- Upon loading the recipes search page, I am also given the option of using 3 inputs variations for searching, i.e. ‘Cuisine', and 'Allergen' and ‘Meal Types’. When user clicks the down arrow which is displayed near to the menu, the drop-down will be dropped down and will list all the choices below. So in order to select the down most items, there will option for users to scroll down. On make a selection and clicking the filter recipes  button the user is directed to a page that displays the recipes based on the search criteria
Test cases Example have been checked for each of the drop down,


| Cuisine        | Allergen                  | Meal Type           |   Records Fetched<br/>
| ------------- | ----------------------- | ----------------------- |<br/>
| Chinese      | None |  Lunch |    1
| Chinese     |  | Snack |  1
|       | Milk  | Lunch |   1
| American    |  |  |   5   
|    | Milk  |  | 5
|    |  | Dessert  | 1


 - The textfield to search for recipes is also tested for keywords, recipe names and ingredients, and redirects me  based on the desired search criteria 
 - The ordering buttons, order the recipe cards based on the ordering aspects. 
 - All links in Pagination work as desired displaying 6 recipe cards at each click.

**Login(login.html)** –*"Test PASS"*
- Tested the link to open Login page
- Verified error message on the form when the mandatory fields were left blank. 
- Verified for invalid user name and password
- 
![IMAGE](static/images/login.jpg)

![IMAGE](static/images/successfullogin.jpg)

- For all user the navigation bar is displayed as follows

![IMAGE](static/images/navforallusers.jpg)


- Successful login opens up navigation bar with more features

![IMAGE](static/images/navforallvalidusers.jpg)

**Register(register.html)**  –*"Test PASS"*
-  Tested the link to open Register page
-  Verified error message on the form when the mandatory fields were left blank. 
-  Verified error message on the form when the mandatory fields were left blank. This
also included the proper email format (xxx@xx.xxx) on testing.
- Verified if same username has been supplied by displaying a message username already exist

**Add recipe(addrecipe.html)** –*"Test PASS"*
- Tested the link opens up the add recipe form.
- Verified error message on the form when the mandatory fields were left blank this includes verifying drop down selections too.
- Tested for cooking time and preparation time modal time picker pop ups.

**User recipes(userrecipes.html)** –*"Test PASS"*
- Tested the view recipe, edit recipe and delete recipe buttons and they redirect me to the desired page and functionality
- All links in Pagination work as desired displaying 6 recipe cards at each click.

**Edit recipe(editrecipe.html)** –*"Test PASS"*
- Tested the edit button on the user recipe page opens up the edit recipe form with all values fetched from the recipe collection.
- Multiselect drop downs displays multiple values in the text box
- Verified error message on the form when the mandatory fields were left blank this includes verifying drop down selections too.
- Tested for cooking time and preparation time modal time picker pop ups.

**Delete recipe(deleterecipe.html)**–*"Test PASS"*
- Tested the delete button on the user recipe page,clicking the delete button deletes the recipe from the database.

**View recipe(viewrecipe.html)**–*"Test PASS"*
- Tested all the links and button that direct me to viewing a particular recipe. Link are found on the navigation menu, Buttons are found on the Home page and in individual cards displaying the recipe peek
- Viewed property gets incremented when a page is viewed and this is tested as the value gets reflected on the recipe page
- Tested the "like" button by clicking the thumbs up increments the total number of likes on that particular recipe
- Tested that when a user logins in he/she is not able to like his/her own recipe.However user is given the option to like other registered user recipes

Incoperated 404 Error handling in Flask.A 404 Error is showed whenever a page is not found.

The **app.py** code has been tested for PEP8 requirements/Python code requirments <link>(http://pep8online.com/)



**Testing of mongodb atlas changes**
When a user...
- Registers in the web application a new user entry is created in the users collections
- Logins verifies the user exists from the user collection
- Creates a new recipe, adds the recipe to the recipes collection, 
- Updates a recipe, the recipe values are changed to their updated values.
- Views individual recipes, it increments the recipe views section of the recipe.
- Upvotes a recipe, it increments the recipe upvotes section of the recipe
- Deletes a recipe, it removes the recipe data from the recipes collection

## Deployment

- Project is built on AWS Cloud 9 <link>(https://aws.amazon.com/cloud9/)

#### Running code locally

- Create an app.py file within your Python application and enter the following code snippet as an example:

```pythoncode
import os
from flask import Flask
	
app = Flask(__name__)

@app.route('/')
def hello():
return 'Hello World'
	
if __name__ == '__main__':
	    app.run(host = os.environ.get('IP'),
	    port = int(os.environ.get('PORT')),
	    debug = True)
```
- In the Cloud 9 Command Line run the app.py
`python3 app.py`
Click on Open->**Preview in Browser window**
- Now you can access your Flask application 

#### Git deployment
The files have been edited in this development instance. When ready, the changes were "deployed" to the staging instance. After user acceptance and testing, deploy again, this time to production. I used git and GitHub pages for deployment.
The following steps are followed to deploy the pages:
1.	Initialised the local directory in my project as a git repository used the cloud9 terminal to perform this step `$git init`
2.	Added the files in the local repository created. And staged them for commit `$git add .`
3.	Commited the files that I have staged in the local repository. 
`$git commit –m ”Initial commit”` This step is perfomed for any changes I have done to sections in webpages and stylesheets as well as the images and audios folder.
4.	Created a new repository in Github and in the terminal, added the URL for the remote repository where your local repository will be pushed.
5.	On major changes I have pushed the changes in the local repository to GitHub. `$git push origin master`
Github Link: <link>(https://github.com/nadia-solution-tracker/third-milestone-project)

#### Heroku deployment Steps

1.	Create our Heroku app on <link>(https://www.heroku.com/)
2.	Link our local Git repository with Heroku.<br/>
`~/workspace $ git status`<br/>
`~/workspace $ git init`<br/>
`~/workspace (master) $ git add .`<br/>
`~/workspace (master) $ git commit -m "Initial Commit"`<br/>
`~/workspace (master) $ git remote  add heroku https://git.heroku.com/<your-app-name>.git`<br/>
`~/workspace (master) $ git remote –v`<br/>
`~/workspace (master) $ git push -u heroku master`<br/>
3.	Create a **requirements.txt** file, which will install the dependencies for our project and tell Heroku that we're using Python.<br/>
`~/workspace (master) $ sudo pip3 freeze --local > requirements.txt`<br/>
`~/workspace (master) $ git add requirements.txt`<br/>
`~/workspace (master) $ git commit -m "requirements file step 3"`<br/>
`~/workspace (master) $ git push -u heroku master`<br/>
4.	Create a **Procfile**.<br/>
`~/workspace (master) $ echo web: python run.py > Procfile`<br/>
`~/workspace (master) $ git add Procfile`<br/>
`~/workspace (master) $ git commit -m "Add Procfile"`<br/>
`~/workspace (master) $ heroku ps:scale web=1`<br/>

Config Variable added to Heroku are as follows

![IMAGE](static/images/herokuconfigvar.jpg)

- To finally deploy any changes in the project
`~/workspace (master) $ git push -u heroku master`

Heroku Link to final Project: <link>(https://kitchen-station.herokuapp.com/)

## Credits

Content
- Cuisine List taken from - https://www.bbcgoodfood.com/recipes/category/cuisines
- Allergen list taken from- https://www.fda.gov/food/buy-store-serve-safe-food/what-you-need-know-about-food-allergies

Code Logic
-	For registration and Login code - https://github.com/PrettyPrinted/mongodb-user-login/blob/master/login_example.py
-	For pagination Code – https://pythonhosted.org/Flask-paginate/
-	For display Flash messages - https://pythonise.com/feed/flask/flask-message-flashing
-	To-output-a-comma-delimited-list-in-jinja-python-template: 
https://stackoverflow.com/questions/11974318/how-to-output-a-comma-delimited-list-in-jinja-python-template
-  404 Error Handling- https://www.geeksforgeeks.org/python-404-error-handling-in-flask/

Images and Recipes
-	All images and recipes are taken from https://www.bbcgoodfood.com/

Bugs and Solutions
-	Deploying application on Heroku was giving me errors “Application error” 
Solved this issue by pushing the requirements file everytime new installs were made and commiting the changes.
Also had to create a “Config Vars” to access the mongodb <br/>
~/environment (master) $ heroku config:set MONGO_URI=mongodb+srv://root:password@myfirstcluster-gtkhp.mongodb.net/test?retryWrites=true
~/environment (master) $ heroku config

-	When clicking the preparation time and cooking time field , the clock modal opens and immediately close. I referred the following link to get it working:
<br/>https://stackoverflow.com/questions/44368205/set-time-format-hhmmss-for-materialize-clockpicker/44782163#44782163
- To output a comma delimited list in the viewrecipe.html page 
<br/>https://stackoverflow.com/questions/11974318/how-to-output-a-comma-delimited-list-in-jinja-python-template-

## Acknowledgements
I would extend my sincere thanks to my mentor for giving me ideas and code snippets on optimizing my webpage. However all the work was done by me with references made to links as mentioned in "Credits" and referring "Code Institute UX Design" videos.I also took inspiration from the Mini Project "Thorin and company" and "Task Manager" from Code institute.
