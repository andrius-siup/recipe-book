"""Imports"""

from bson.objectid import ObjectId
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash
import os

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

mongo = PyMongo(app)

# all recipes


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    """
    A function that return all recipes into home page
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes, page_title="All Recipes")


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    """
    Function find recipe by id
    """
    the_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "view_recipe.html", recipes=the_recipe, page_title="View Recipe"
    )


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search function - searching for entered text.
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes, page_title="Search Recipe")


# register


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Register to the website function
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html", page_title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login function - login user to the website
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Login")


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    """
    Profile function - user personal page with his own recipe collection
    """
    if "user" not in session:
        return redirect(url_for("login"))

    recipes = mongo.db.recipes.find({"created_by": session["user"]}).sort("_id", -1)

    return render_template(
        "profile.html", username=session["user"], recipes=recipes, page_title="Profile"
    )


@app.route("/logout")
def logout():
    """
    Logout finction - logout user from his profile, redirected to the login page
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["Get", "POST"])
def add_recipe():
    """
    Add recipe function - check if user is login
    add recipe to his collection and to recipe all page.
    """
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_list": request.form.get("ingredients_list").splitlines(),
            "recipe_img": request.form.get("recipe_img"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "instructions": request.form.get("instructions").splitlines(),
            "created_by": session["user"],
        }
        # print(submit)
        recipe = mongo.db.recipes.insert_one(submit)
        recipe_id = recipe.inserted_id
        flash("Recipe Successfully Added")
        return redirect(url_for("view_recipe", recipe_id=recipe_id))

    categories = mongo.db.categories.find().sort("category_name")
    return render_template(
        "add_recipe.html", categories=categories, page_title="Insert Recipe"
    )


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Edit recipe function - checked if user is login,
    if so can edited recipe.
    """
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_list": request.form.get("ingredients_list").splitlines(),
            "recipe_img": request.form.get("recipe_img"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "instructions": request.form.get("instructions").splitlines(),
            "created_by": session["user"],
        }
        # print(submit["ingredients_list"])
        for ingredient in submit["ingredients_list"]:
            ingredient = ingredient.strip()
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

        if submit:
            the_recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
            return redirect(url_for("view_recipe", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name")
    return render_template(
        "edit_recipe.html",
        recipe=recipe,
        categories=categories,
        page_title="Edit Recipe",
    )


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    Delete recipe function - deleted recipe.
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile"))


# only admin has access to this page
@app.route("/get_categories")
def get_categories():
    """
    Get categories function - only admin has access to this page.
    """
    if "user" not in session:
        return redirect(url_for("login"))

    categories = list(mongo.db.categories.find().sort("category_name", 1))

    if session["user"] == "admin":
        return render_template(
            "categories.html", categories=categories, page_title="Categories"
        )

    flash("You do not have permission")
    return redirect(url_for("login"))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    Add category function - only admin has access, and can add new categories.
    """
    if "user" not in session:
        return redirect(url_for("login"))

    if session["user"] == "admin":
        if request.method == "POST":
            category = {"category_name": request.form.get("category_name")}
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for("get_categories"))

        return render_template("add_category.html", page_title="Create Category")

    flash("You do not have permission")
    return redirect(url_for("login"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Edit category fnction - only admin has access, simply can edit category.
    """
    if "user" not in session:
        return redirect(url_for("login"))

    if session["user"] == "admin":
        if request.method == "POST":
            submit = {"category_name": request.form.get("category_name")}
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("Category Successfully Updated")
            return redirect(url_for("get_categories"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template(
            "edit_category.html", category=category, page_title="Edit Category"
        )

    flash("You do not have permission")
    return redirect(url_for("login"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Delete category function - admin has access, can delete category.
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=False)
