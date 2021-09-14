import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
DB = mongo.db


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort('recipe_name', 1))
    return render_template("recipes.html", recipes=recipes)


@app.route("/search",  methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find(
        {"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allow user to register and create an account. Checks if user already
    exists. If it doesn't, it redirects the user to their profile page
    """
    if request.method == "POST":

        # variables
        username = request.form.get("username")
        password = request.form.get("password")
        confirmed_password = request.form.get("confirm_password")
        # check if username already exist in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        elif len(username) < 5:
            flash("Username must contain at least 5 characters")
            return redirect(url_for("register"))
        elif len(password) < 5:
            flash("Password must contain more than 5 characters")
        elif password != confirmed_password:
            flash("The passwords do not match. Please try again")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(password)
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have been Registered Successfully!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")
    # return render_template(url_for("profile", username=session["username"]))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows user to log into their account. The function checks if the
    username exists. If it does, it checks the db password
    with the password the user has entered. If successful the
    user is then redirected to their profile. If the user input
    does not match the db, the user recieves a flash notification.
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                 existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome again, {}!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if username doesn't exist
            session['user'] = True
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user user's name from db
    username = mongo.db.users.find_one(
         {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remore user from session cookie
    session.pop("user", None)
    flash("See you soon!")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if 'user' not in session:
        flash('You have to be logged in to see this page')
        return render_template('404.html')

    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        recipe = {
            "course_type": request.form.get("course_type"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "ingredient_1": request.form.get("ingredient_1"),
            "ingredient_2": request.form.get("ingredient_2"),
            "ingredient_3": request.form.get("ingredient_3"),
            "ingredient_4": request.form.get("ingredient_4"),
            "ingredient_5": request.form.get("ingredient_5"),
            "ingredient_6": request.form.get("ingredient_6"),
            "ingredient_7": request.form.get("ingredient_7"),
            "direction_1": request.form.get("direction_1"),
            "direction_2": request.form.get("direction_2"),
            "direction_3": request.form.get("direction_3"),
            "direction_4": request.form.get("direction_4"),
            "direction_5": request.form.get("direction_5"),
            "direction_6": request.form.get("direction_6"),
            "direction_7": request.form.get("direction_7"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "vegetarian": vegetarian,
            "recipe_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Thank you! Your recipe has been added!")
        return redirect(url_for("get_recipes"))

    courses = mongo.db.courses.find().sort("course_type", 1)
    return render_template("add_recipe.html", courses=courses)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if 'user' not in session:
        flash('You have to be logged in to see this page')
        return render_template('404.html')

    if request.method == "POST":
        vegetarian = "on" if request.form.get("vegetarian") else "off"
        edit = {
            "course_type": request.form.get("course_type"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "ingredient_1": request.form.get("ingredient_1"),
            "ingredient_2": request.form.get("ingredient_2"),
            "ingredient_3": request.form.get("ingredient_3"),
            "ingredient_4": request.form.get("ingredient_4"),
            "ingredient_5": request.form.get("ingredient_5"),
            "ingredient_6": request.form.get("ingredient_6"),
            "ingredient_7": request.form.get("ingredient_7"),
            "direction_1": request.form.get("direction_1"),
            "direction_2": request.form.get("direction_2"),
            "direction_3": request.form.get("direction_3"),
            "direction_4": request.form.get("direction_4"),
            "direction_5": request.form.get("direction_5"),
            "direction_6": request.form.get("direction_6"),
            "direction_7": request.form.get("direction_7"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "vegetarian": vegetarian,
            "recipe_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Thank you! Your recipe has been updated!")
        return redirect(url_for("get_recipes"))

    courses = mongo.db.courses.find().sort("course_type", 1)
    return render_template("edit_recipe.html", recipe=recipe, courses=courses)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):

    if 'user' not in session:
        flash('You have to be logged in to see this page')
        return render_template('404.html')

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("The recipe has been removed!")
    return redirect(url_for("get_recipes"))


@app.route("/get_courses")
def get_courses():
    courses = list(mongo.db.courses.find().sort("course_type", 1))

    if 'user' not in session:
        flash('You have to be logged in to see this page')
        return render_template('404.html')

    return render_template("courses.html", courses=courses)


@app.route("/add_course", methods=["GET", "POST"])
def add_course():

    if 'user' not in session:
        flash('You have to be logged in to see this page')
        return render_template('404.html')

    if request.method == "POST":
        course = {
            "course_type": request.form.get("course_type")
        }
        mongo.db.courses.insert_one(course)
        flash("New Course Added!")
        return redirect(url_for("get_courses"))

    return render_template("add_course.html")


@app.route("/edit_course/<course_id>", methods=["GET", "POST"])
def edit_course(course_id):
    course = mongo.db.courses.find_one({"_id": ObjectId(course_id)})

    if 'user' not in session:
        flash('You have to be logged in to see this page')
        return render_template('404.html')

    if request.method == "POST":
        submit = {
            "course_type": request.form.get("course_type")
        }
        mongo.db.courses.update({"_id": ObjectId(course_id)}, submit)
        flash('Course type updated!')
        return redirect(url_for('get_courses'))

    return render_template("edit_course.html", course=course)


@app.route("/delete_course/<course_id>")
def delete_course(course_id):
    mongo.db.courses.remove({"_id": ObjectId(course_id)})
    flash('Course removed!')
    return redirect(url_for('get_courses'))


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    full_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=full_recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
