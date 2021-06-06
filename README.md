# Andrius Siupinys

![Recipes](/images/responsive-design.png)

# Project Summary
This is a Recipe landing page, which was created for all people who love food and cooking and want to share it all world. 
There is also can be a storage platform for your recipes collection and anytime you have access to your recipes. 
You don't need anymore your notes. We all now live with smartphones. The website is created a responsive design that is very handy to see recipes from mobile devices
 to tablets or larger screens. The inspiration comes from seeing like my wife trying to save the recipes by a screenshot or take notes and always lost somewhere.
  Now she can simply add recipes through this website and save them. The website was created for educational purposes.

# Contents

- [User Experency (UX)](#ux)
    + [Ideal user](#ideal-user)                       
    + [Visitors to this website are searching for:](#visitors-to-this-website-are-searching-for)
    + [User stories - user not registered](#user-stories-user-not-registered )
    + [User stories - user registered](#user-stories-user-registered)
    + [User stories - registered as admin](#user-stories-registered-as-admin)
- [Strategy](#strategy)
- [Scope](#scope)
- [Structure](#structure)
- [Skeleton](#skeleton)
    + [Wireframe](#wireframe)
- [Features](#features)
    + [Existing Features](#existing-features)   
        + [Navigation Bar](#navigation-bar) 
        + [Home](#home)
        + [Profile](#profile)
        + [New Recipe](#new-recipe)
        + [Single Recipe](#single-recipe)
        + [Edit Recipe](#edit-recipe)
        + [Manage Categories](#manage-categories)
        + [Add Category](#add-category)
        + [Edit Category](#edit-category)
        + [Login](#login)
        + [Register](#register)
        + [Footer](#footer)
    + [Features Left to Implement](#features-left-to-implement)
        + [Home](#home-page)
        + [Profile](#profile-page)
        + [New Recipe](#new-recipe-page)
        + [Single Recipe](#single-recipe-page)
        + [Login](#login-page)
        + [Register](#register-page)
- [Responsive](#responsive)
- [Deployment](#deployment)
    + [Download](#download)
    + [Clone Repository](#clone-repository)
    + [Creating an Environment File](#creating-an-environment-file)
    + [MongoDB Schema](#mongodb-schema)
    + [Deployment to Heroku](#deployment-to-heroku)
- [Testing](#testing)  
    + [Code validators](#code-validators)
    + [Lighthouse](#lighthouse)
    + [Manual Testing](#manual-testing)
- [Tecnology Used](#tecnology-used)    
- [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Code](#code)
    + [Resources](#resources)
    + [Acknowledgements](#acknowledgements)      




# UX

## Ideal user
The ideal user is English reading and writing user who also loves food and cooking. The user wants to share the favorite recipe with the world, 
or simply use it for recipe collection storing.

## Visitors to this website are searching for
The website visitors searching for the recipe to cook something. They found the tasty image or they think that it is tasty than they look at the ingredients list, 
they also check the instructions how to cook. Or otherwise, they want to share their own recipe.

## User stories user not registered 
1. As a new visitor to the website, I want to easily navigate the site, so I can find what I need efficiently.
2. As a new visitor to the website, I want to has Register/Log In functions, that only I can have my own profile.
3. As a new visitor to the website, I want that users recipes can be available only to register users. 
4. As a new visitor to the website, I want to use search panel to found recipe by category or by ingredient from recipe.
5. As a new visitor to the website, I want to see social media link, to contact or followed the website on social media.



## User stories user registered
1. As a registered visitor to the website, I want to easily navigate the site, so I can find what I need efficiently.
2. As a registered visitor to the website, I want to has Register/Log In functions, that only I can have my own profile.
3. As a registered visitor to the website, I want to insert my own recipe and share to others users from the website.
4. As a registered visitor to the website, I want to edit my recipe if I made mistake for some reason.
5. As a registered visitor to the website, I want to remove my recipe, if I think that I don't want that others see this recipe.
6. As a registered visitor to the website, I want to have my own profile, that I can found my all recipes.
7. As a registered visitor to the website, I want to view othes users recipes, to try what is looks me tasty.
8. As a registered visitor to the website, I want to get security features, that if I duplicate pages for some reason and Log Out in one page, that others pages also will be logged out.
9. As a registered visitor to the website, I want to get security features, that others PC users can't come in in my profile from browser history. 
10. As a registered visitor to the website, I want to use search panel to found recipe by category or by ingredient from recipe.
11. As a registered to the website, I want to see social media link, to contact or followed the website on social media.
12. As a registered to the website, I want to got a confirmation message before deleting recipe. 



## User stories registered as admin
1. As a admin to the website, I want to easily navigate the site, so I can find what I need efficiently.
2. As a admin to the website, I want to has Register/Log In functions, that only I can have my own profile.
3. As a admin to the website, I want to insert my own recipe and share to others users from the website.
4. As a admin to the website, I want to edit my recipe if I made mistake for some reason.
5. As a admin to the website, I want to remove my recipe, if I think that I don't want that others see this recipe.
6. As a admin to the website, I want to has access to edit/remove users recipe, if I think that the recipe is can not be public.
7. As a admin to the website, I want to has ability to create, edit or remove category for recipe that will be help users will be easily sort or found recipes.
8. As a admin to the website, I want to got a confirmation message before deleting recipe or category. 
9. As a admin to the website, I want to have my own profile, that I can found my all recipes.
10. As a admin to the website, I want to view othes users recipes, to try what is looks me tasty.
11. As a admin to the website, I want to get security features, that if I duplicate pages for some reason and Log Out in one page, that others pages also will be logged out.
12. As a admin to the website, I want to get security features, that others PC users can't come in in my profile from browser history. 
13. As a admin to the website, I want to use search panel to found recipe by category or by ingredient from recipe.
14. As a admin to the website, I want to see social media link, to contact or followed the website on social media.

# Strategy

# Scope

# Structure

# Skeleton

## Wireframe
* [User not registered](WIREFRAMES.md)
* [Registered User](WIREFRAMES.md)
* [Admin](WIREFRAMES.md)



# Surface
## Color Scheme
![color-palette](/images/pick-color.png)

I used Grecian Holiday color palette for this website.

`#2988BC` Grecian Blue - used for buttons: Search, View More, Edit, Home.

`#2F496E` Sea - used for the website Manage Categories, cards background.

`#F4EADE` Plaster - was changed into `#fffbf5` and used for the website background color.

`#ED8C72` Coral - used for the website navbar and footer.

## Typography
google fonts

# Features

## Existing Features

### Navigation Bar 
The navigation bar features are fixed and when your navbar is resized into tablet screen size or below, the links on the right turn into a hamburger icon. 
Also added the entire sidenav, which will store navigation bar links.

### Home
The Home page features has keep search panel and all users recipes. The user can seek a recipe by category or by ingredient that is in the recipe.
Search button will find match a word.  If it found? the recipe will store below the search panel, otherwise displayed message that recipe not found.
The new added recipe goes at the bottom of all recipes page. 

### Profile
The Profile page features has the display the username top of the page, also will display all user's recipes, last added will be first in the page. 
Also recipe card has button to redirected user in to the single recipe page.

### New Recipe
The new recipe page feature has a form that the user can input text to add new recipe. The all input data will be stored into MongoDB and redirected into others pages.
The form has placeholder with icon that will move up when the user click into field. If the user leave the input field empty and clicked submit button will display
 an error message, also input line change colours.

* The CHOOSE CATEGORY field has list of categories that user can pick up for his recipe.
* The Recipe Name field a user can input 5-50 characters long.
* The Ingredients List field a user can input 5- 3000 characters long and can be separated on new line for final display all text into array.
* The form Instructions field a user can input 5- 3000 characters long text and can be separated on new line for final display all text into array.
* The form IMG URL field the user have to paste image address, and has to be 5-300 characters long.
* The Preparation Time field a user can input number 0-120.
* The Cooking Time field a user can input number 0-120.
* The Serving field a user can input number 1-10. 
* The Submit button has color change when the user is over the button.

### Single Recipe 
The Single Recipe page features to look at the user's single recipe. There are recipe name, category, image, preparation and cooking time, serving for how many people,
 ingredient list, the instruction of how to do it, also there are three buttons below all text(only recipe owner and admin can see those buttons). 
 They are Edit, Delete, and Home. 
 * Clicking the Edit button the user will be routed to the Edit recipe page. 
 * Clicking the Delete button, the confirmation message will popup with two buttons Agree and Close. 
    * Clicking Agree, the recipe will be removed from the website and database, and the user will be routed to his profile page. 
    * Clicking Close button, the user will be back to single recipe page. 
* Clicking the Home button, the user will be routed to the home page. 

### Edit Recipe 
The Edit recipe has features to edit recipe form same like user was used to add recipe. Only recipe owner and website admin can edit recipe. There is CANCEL button 
that will bring you back into single recipe page, and button EDIT RECIPE will update recipe will new text and routed you to the single recipe page. The all edited
 data will be stored into MongoDB and redirected into others pages. The form has placeholder with icon that will move up when the user click into field. 
 If the user leave the input field empty and clicked submit button will display an error message, also input line change colours.

* The CHOOSE CATEGORY field has list of categories that user can pick up and change for his recipe.
* The Recipe Name field a user can simple edit text, final input must be 5-50 characters long.
* The Ingredients List field a user can simple edit, final input must be 5- 3000 characters long and can be separated on new line for final display all text into array.
* The form Instructions field a user can simple edit, final input must be input 5- 3000 characters long text and can be separated on new line for final display all text into array.
* The form IMG URL field the user can simple edit, final input must be image address, and has to be 5-300 characters long.
* The Preparation Time field a user can simple edit, final input must be number 0-120.
* The Cooking Time field a user can simple edit, final input must be number 0-120.
* The Serving field a user can simple edit, final input must be number 1-10. 
* The Edit Recipe button has color change when the user is over the button, redirected user to single recipe page with new changes that user made.
* The CANCEL button redirected back to single recipe page.

### Manage Categories
The Manage Categories page features are that only website admin has access to this page. There is a button to Add Category, which will route the admin to add category
 page. Also on the page are displayed all categories that the admin created. In the single category card, there are category name and two buttons: Edit and Delete.
* Clicking the Edit button the admin will be routed to the Edit category page.
* Clicking the Delete button, the confirmation message will pop up with two buttons: Agree and Close.
    * Clicking Agree button the Category will be deleted from the page and from the database.
    * Clicking the Close button the confirmation message will be closed and the admin will stay on the same page.

### Add Category
The Add Category page features are that the website admin has access to this page. In the Add category page, the admin can input a 3-20 characters long text,
 and a single button to submit a new category is ADD CATEGORY. When the admin click submits button, he will be routed to the manage category page and the new category will be displayed in alphabetical order.
  Also, this category will be displayed for users in the add new recipe page, Choose category list.

### Edit Category
In the Edit Category page, the admin can edit the text and the final input has to be a 3-20 characters long text. There are two buttons: Cancel and Edit Category.
* Clicking the Cancel button, the admin will be routed back to the Manage Categories page.
* Clicking Edit Category, the new inputted text will be updated and admin will be routed to the manage category page and the category card will be displayed in alphabetical order.
 Also, this category will be displayed for users in the add new recipe page, Choose category list.

### Login 
The login page features are the form that the registered user has to input the username and password, to be able to login to the website.
The username field has to be a 5-15 character long string, included a lower and capital letter and any number.  Will be displayed an error message if the user 
will leave an empty field and submit the login button. The password field has to be a 5-15 character long string, included a lower and capital letter and any number.  
Will be displayed an error message if the user will leave an empty field and submit the login button. Clicking the login button the user will be routed the user's
 into the profile page if the username and password will match the registered user's username and password, otherwise will be displayed the flash message 
 with the text "Incorrect Username and/or Password", and the user will stay to the login page. 
 There is a link to the Register page, below the login form. Clicking that link the user will be routed to the Register page.

### Register
The register page features are that anyone can be registered to this website. The new user, in the username field, must be input the string which has to
 be 5-15 characters long, included a lower and capital letter and any number.  Will be displayed an error message if the user will leave an empty field and 
 submit the register button. The password field has to be a 5-15 character long string, included a lower and capital letter and any number. Will be displayed
  an error message if the user will leave an empty field and submit the login button.
 Clicking the register button the user will be routed to his own profile page.
### Footer
The footer features has social media links and copyright information. The social links opening on the new blank tab.


## Features Left to Implement

### Home Page
The Home page will implement to add Advertising, like sell kitchen stuff.

### Profile Page
The profile page, will implement the user own image, table of his recipes sorted by category, and also will be section to store favorite recipes. 

### New Recipe Page
The New recipe page, will implement the new input in the form, that the user could input countries kitchen, like Italian or Chinese kitchen.

### Single Recipe Page
The Single Recipe Page will implement chat function, the users can be left reviews about recipe or asked some questions to recipe owner.

### Login Page
The Login page, will implement forgot password function, that the user can reset his password and create a new one. 

### Register Page
The register page left to implement will add more input lines in form for new users like add email, phone number, for security reason. Also will be added reCAPTCHA.


# Responsive
The Home page has responsive design and recipe cards will change from mobile devices has one per screen, tablets and laptops has three per screen, desktops and above has four per screen.

# Tecnology Used
[Python3](https://www.python.org/) - for the backend development.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/) - Python framework was used all project. Flask depends on the Jinja template engine and the Werkzeug WSGI toolkit.
* [PyMongo](https://pymongo.readthedocs.io/en/stable/) - is a Python distribution containing tools, used for working with MongoDB.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security) - used for password security.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - used in conjuction with python for the working of the website

[MongoDB](https://www.mongodb.com/) - database was used to storing and retrieving information in the website.

[HTML](https://www.w3schools.com/html/) - used for creating the website.

[CSS](https://www.w3schools.com/css/default.asp) - used for styling the website.

[jQuery](https://jquery.com/) - used for confirmation messages and interactive design, also initialise MaterializeCSS components.

[MaterializeCSS](https://materializecss.com/) - used to create responsive design, grid system, buttons, navbar, sidenav, dropdown, footer, modal, cards, forms.

[balsamiq](https://balsamiq.com/) - used to create wireframes.

[Gitpod](https://www.gitpod.io/) - used to built all project. 

[GitHub](https://github.com/) - used to hosting the website.

[Heroku](https://www.heroku.com/) - used to deploy the website.

[Chrome DevTools](https://developer.chrome.com/docs/devtools/) - used all the time when created the website.

[grammarly](https://www.grammarly.com/) - used to check typo mistakes.

[W3C Markup Validation Service](https://validator.w3.org/) - used to validate HTML code.

[CSS Validation Service](http://jigsaw.w3.org/css-validator/) - used to validate css code.

[JSHint](https://jshint.com/) - used to validate the jQuery code. 

[PEP8 online](http://pep8online.com/) - used to validate the Python code.

[Lighthouse](https://developers.google.com/web/tools/lighthouse) - used to improve the quality of the webpage.


# Deployment

The website was developed using Gitpod workspace to commit and push to GitHub. The project uses GitHub for hosting and has been deployed using Heroku.
To access to my page please follow these steps: 

## Download

* Navigate to my repository https://github.com/andrius-siup/recipe-book.git .
* Click the **Code** button.
* Click the **Download Zip**.
* Extract where you want to keep all files. 


## Clone Repository

* GitHub navigate to **andrius-siup/recipe-book**.
* Click the **Code** button.
* To clone with **HTTPS** copy the URL in the box https://github.com/andrius-siup/recipe-book.git
* Open your Git Bash.
* Changed the directory to the location you want to clone to be made.
* Type git clone than paste the copied URL  `git clone https://github.com/andrius-siup/recipe-book.git` . 
* Enter and your local clone will be created.

## Creating an Environment File

Install Flask, in your terminal type `pip3 install Flask` , that sets up Flask functionality. Next you will need to create **env.py** file for storing sensitive data, 
type `touch env.py` in terminal. This file should never be pushed to GitHub, so type `touch .gitignore` to be able to ignore it. Than open the **.gitignore** file and lets 
ignore your **env.py** file typed:
```
env.py
__pycache__/ 

```
save and close it.

In the env.py file we need to hide several bits of data. Open env.py file and type:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "********")
os.environ.setdefault("MONGO_URI", "********")
os.environ.setdefault("MONGO_DBNAME", "recipe_manager")
```
Make sure that your env.py file isn't being tracked, type  `git status` and make sure that you can not see it listed.

## MongoDB schema

To create the data schema in your MongoDB Atlas, create a new database called **recipe_manager**, add three collections **categories**, **recipes**, **users**.
* recipe_manager
    * categories 
        * _id:ObjectId
        * category_name
    * recipes
        * _id:ObjectId
        * recipe_name 
        * ingredients_list **should be set into an array**
        * recipe_img
        * prep_time
        * cook_time
        * serves
        * instructions **should be set into an array**
        * created_by
    * users
        * _id:ObjectId
        * username
        * password                

## Deployment to Heroku

To deploy the app using Heroku, use the following steps:
1. In terminal type `pip3 freeze --local > requirements.txt` to create a list of the dependencies for the website.
1. Create a Procfile, is what Heroku looks for to know which file runs the app. Type in terminal `echo web: python app.py > Procfile`
1. Use git commands to stage, commit and pushed these files to your GitHub.
1. Go to [Heroku](https://www.heroku.com/) page and login.
1. Create new app by click on **New** and **Create New App** . Enter your unique app name, select your region and than click **create app**.
1. In the Deployment method section, select **GitHub - connect to GitHub** to set up automatic deployment from your GitHub repository.
1. Enter your repository name in the input field, and click search. Once is found your repository click connect.
1. To be able to read Heroku environment variables go to **Settings**  than click on **Reveal Config Vars** .
1. Add the following variables:
   * KEY **IP**  VALUE **0.0.0.0** click Add
   * KEY **PORT**  VALUE **5000** click Add
   * KEY **SECRET_KEY** VALUE **same unique key as you set it in env.py**
   * KEY **MONGO_URI** VALUE **to retrieved Mongo_URI you will find in MongoDb -> Clusters -> Connect -> Connect your aplication -> and copy connection string into application code**
   * KEY **MONGO_DBNAME** VALUE **recipe_manager**
1. Go back to **Deploy** tab, but before that go back to terminal and push requirement.txt and Procfile to GitHub. After that in Heroku you can click **Enable Automatic Deploys**.
1. Than click on the **Deploy Branch**
1. After less than minute to build you will see **Your app was successfully deployed**, click **View** to lounch the app.

# Testing

* [Code validators](TESTING.md)
* [Lighthouse](TESTING.md)
* [Manual Testing](TESTING.md)

# Credits

## Content

The recipes was borrowed from Taste and BBC Good Food websites.

Pasta with salmon & peas, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/pasta-salmon-peas)

Healthy potato salad, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/herby-potato-salad)

Smoked salmon omelettes,the recipe image and text was borrowed from the website [Taste](https://www.taste.com.au/recipes/smoked-salmon-omelettes/x7hu3bbi)

Carrot and orange smoothie, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/carrot-and-orange-smoothie)

Breakfast super shake, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/breakfast-super-shake)

Arabian buttered eggs mint lemon, the recipe image and text was borrowed from the website [Taste](https://www.taste.com.au/recipes/arabian-buttered-eggs-mint-lemon/5282cd39-610e-4eb2-b165-cd9152216022)

Cherry bakewell cake, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/cherry-bakewell-cake)

Carrot cake, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/carrot-cake)

Clean green smoothie, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/clean-green-smoothie)

Two minute breakfast smoothie, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/two-minute-breakfast-smoothie)

American pancakes, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/american-pancakes)

Eggy cheese crumpets, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/eggy-cheese-crumpets)

Breakfast smoothie, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/breakfast-smoothie)

Green breakfast smoothie, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/green-breakfast-smoothie)

Pasta salmon peas, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/pasta-salmon-peas)

Herby potato salad, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/herby-potato-salad)

Carrot cake porridge, the recipe image and text was borrowed from the website [BBC Good Food](https://www.bbcgoodfood.com/recipes/carrot-cake-porridge)

Pavlova popsicles, the recipe image and text was borrowed from the website [Taste ](https://www.taste.com.au/recipes/pavlova-popsicles-recipe/k310nxu0?r=recipes/strawberryrecipes&c=f6ac16f9-2dce-480e-9bb0-3d1cdea996a1/Strawberry%20recipes)

Panna cotta roasted strawberries, the recipe image and text was borrowed from the website [Taste](https://www.taste.com.au/recipes/panna-cotta-roasted-strawberries-recipe/7xyseu5a?r=recipes/strawberryrecipes&c=f6ac16f9-2dce-480e-9bb0-3d1cdea996a1/Strawberry%20recipes)


## Code

The code was borrowed from CI Tim Nelson tutorial.

` $("#copyright").text(new Date().getFullYear());`

`

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }`




## Resources

Code Institute course material.

MaterializeCSS - general resource.

W3Schools - general resource.

Flask docs - general resource.

PyMongo docs - general resource.

MongoDB docs - general resource.

Werkzeug docs - general resource.

The color palette was borrowed from [Canva](https://www.canva.com/learn/100-color-combinations/) website.


## Acknowledgements
Brian Macharia - mentor support, huge help through the project.

Code Institute Tutor support team.

