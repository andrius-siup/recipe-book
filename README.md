
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

## Creating an env.py file

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

* categories 
    * category_name
* recipes
    * recipe_name 
    * ingredients_list **should be set into an array**
    * recipe_img
    * prep_time
    * cook_time
    * serves
    * instructions **should be set into an array**
    * created_by
* users
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

## Manual Testing
### Home page

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link, has been routed to the users profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link, has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to Login page. | Tested, works as should.| No |
| Clicinkg on the navigation bar's Login link has been routed to the login page.| Tested, works as should.| No |
| Clicking on the navigation bar's Register link, has been routed to the register page.| Tested, works as should.| No |
| Clicking Home page recipes card View More button, has been routed to the single recipe page. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |
| Clicking the search panel SEARCH button,  an error message appears asking "Please fill out this field". | Tested, works as should.| No |
| Clicking the search panel's SEARCH button, with input text, the matching word will be looked at in the recipes ingredients list or in the recipes instructions. If it will be found, the recipes will be displayed below the search panel. If not be found, the message will be "No Results found". | Tested, works as should.| No |
| Clicking the search panel RESET button, the user has been redirected to the Home page and removed input text. | Tested, works as should.| No |
| Clicking the profile page recipes card VIEW MORE button, has been routed to the single recipe page. | Tested, works as should.| No |

### Profile page 

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link, has been routed to the users profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link, has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to Login page. | Tested, works as should.| No |
| Clicinkg on the navigation bar's Login link has been routed to the login page.| Tested, works as should.| No |
| Clicking on the navigation bar's Register link, has been routed to the register page.| Tested, works as should.| No |
| Clicking Home page recipes card View More button, has been routed to the single recipe page. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |

### New Recipe page

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link, has been routed to the users profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link, has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to Login page. | Tested, works as should.| No |
| Clicinkg on the navigation bar's Login link has been routed to the login page.| Tested, works as should.| No |
| Clicking on the navigation bar's Register link, has been routed to the register page.| Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |
| Clicking add recipe Category field, the user can choose the category from the list.| Tested, works as should.| No |
| Clicking on the recipe name field, the user can enter the recipe name, must be lenght between 5-50 chareacters.| Tested, works as should.| No |
| Clicking on the recipe ingredients field, the user can enter the recipe ingredients, must be lenght between 5-3000 chareacters. All text can be separated on the new line. | Tested, works as should.| No |
| Clicking on the recipe instructions field, the user can enter the recipe instructions, must be lenght between 5-3000 chareacters. All text can be separated on the new line. | Tested, works as should.| No |
| Clicking on the recipe Image URL field, the user can paste the recipe img url. Added a invalid url or longer than 300 characters should display error message. | Tested, works as should.| No |
prep time 0-120 number
cook_time 0-120 number
serves 1-10 number

