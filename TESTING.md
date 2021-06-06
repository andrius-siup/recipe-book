+ [Code validators](#code-validators)
+ [Lighthouse](#lighthouse)
+ [Manual Testing](#manual-testing)
    + [Home, user not logged in](#home-page-user-not-logged-in)
    + [Home, user logged in](#home-page-user-logged-in)
    + [Profile](#profile-page-manual-test)
    + [New Recipe](#new-recipe-page-manual-test)
    + [Single Recipe](#single-recipe-page-manual-test)
    + [Edit Recipe](#edit-recipe-page-manual-test)
    + [Manage Categories](#manage-categories-page-manual-test)
    + [Create Category](#create-category-page-manual-test)
    + [Edit Category](#edit-category-page-manual-test)
    + [Login](#login-page-manual-test)
    + [Register](#register-page-manual-test)

## Code Validators

![HTML](/images/validators/html-validator.png)

1. The end tag was changed into `</h1>` that match the opened tag.
2. In the `<img>` element was add `alt=""` attribute.
3. The duplicated id was replaced into class `home-pg-prep-time` and solved that issue.  

![CSS](/images/validators/css-validator-no-error.png)

There are no errors found on the CSS validator.

![jshint](/images/validators/no-errors-jshint.png)

There are no errors found on the JSHint.

![Pep8online](/images/validators/pep8online-checked-found-3-errors.png)

The Python file `app.py` was left four lines too long than 79 characters and Gitpod does not show that. Easily fixed that by split lines.




## Lighthouse

![mobile](/images/lighthouse/lighthouse-mobile-first.png)

Added `alt=""` attribute into `<img>` that if image does not upload, the user can read what is write in attribute.

Added attribute `rel="noopener"`  into `<a>` anchor for social media links.

* Mobile 

![pass-mobile](/images/lighthouse/pass-lighthouse-mobile.png)

* Desktop

![pass-desktop](/images/lighthouse/pass-lighthouse-desktop.png)

Added google font family Roboto and `<meta name="description" content="text here">`

* Mobile

![mobile](/images/lighthouse/last-one-mobile.png)

* Desktop

![](/images/lighthouse/last-one-desktop.png)


## Manual Testing

### Home page user not logged in

|   Test              |  Result         |  Errors 
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Login link has been routed to the login page.| Tested, works as should.| No |
| Clicking on the navigation bar's Register link has been routed to the register page.| Tested, works as should.| No |
| Clicking the search panel SEARCH button, an error message appears asking "Please fill out this field". | Tested, works as should.| No |
| Clicking the search panel's SEARCH button, with input text, the matching word will be looked at in the recipes ingredients list or in the recipes category name. If it will be found, the recipes will be displayed below the search panel. If not be found, the message will be "No Results found". | Tested, works as should.| No |
| Clicking the search panel RESET button, the user has been redirected to the Home page and removed input text. | Tested, works as should.| No |
| Clicking the profile page recipes card VIEW MORE button has been routed to the login page. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons has been routed to the blank page of this website. | Tested, works as should.| No |



### Home page user logged in

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link has been routed to the user's profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link should log out the user from the website and has been routed to the Login page. | Tested, works as should.| No |
| Clicking the search panel SEARCH button,  an error message appears asking "Please fill out this field". | Tested, works as should.| No |
| Clicking the search panel's SEARCH button, with input text, the matching word will be looked at in the recipes ingredients list or in the recipes category name. If it will be found, the recipes will be displayed below the search panel. If not be found, the message will be "No Results found". | Tested, works as should.| No |
| Clicking the search panel RESET button, the user has been redirected to the Home page and removed input text. | Tested, works as should.| No |
| Clicking Home page recipes card, View More button, has been routed to the single recipe page. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons has been routed to the blank page of this website. | Tested, works as should.| No |


### Profile page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link has been routed to the user's profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to the Login page. | Tested, works as should.| No |
| Clicking Profile page, recipes card View More button, has been routed to the single recipe page. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons has been routed to the blank page of this website. | Tested, works as should.| No |


### New Recipe page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link has been routed to the user's profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to the Login page. | Tested, works as should.| No |
| Clicking add Recipe Category field, the user can choose the category from the list.| Tested, works as should.| No |
| Clicking on the Recipe Name field, the user can enter the recipe name, which must be length between 5-50 characters. Display error message when characters are over than in range.| Tested, works as should.| No |
| Clicking on the Recipe Ingredients field, the user can enter the recipe ingredients, which must be length between 5-3000 characters. All text can be separated on the new line. Display error message when characters are over than in range. | Tested, works as should.| No |
| Clicking on the Recipe Instructions field, the user can enter the recipe instructions, which must be length between 5-3000 characters. All text can be separated on the new line. Display error message when characters are over than in range. | Tested, works as should.| No |
| Clicking on the recipe Image URL field, the user can paste the recipe IMG URL. Added an invalid URL or longer than 300 characters should display an error message. | Tested, works as should.| No |
| Clicking on the recipe Prepare Time field, the user can enter numbers between 0-120 min. Added number out of range when and clicking submit button should display an error message. | Tested, works as should.| No |
| Clicking on the recipe Cook Time field, the user can enter numbers between 0-120 min. Added number out of range when and clicking submit button should display an error message. | Tested, works as should.| No |
| Clicking on the recipe Serving field, the user can enter numbers between 1-10. Added number out of range when and clicking submit button should display an error message. | Tested, works as should.| No |
| Clicking ADD RECIPE button to add a new recipe, the user has been redirected to the VIEW RECIPE page. Display an error message if one of the fields is empty or a character or number out of range. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons has been routed to the blank page of this website. | Tested, works as should.| No |

### Single Recipe page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link has been routed to the user's profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to the Login page. | Tested, works as should.| No |
| Clicking the single recipe page EDIT button, the user has been routed to EDIT recipe page. | Tested, works as should.| No |
| Clicking the single recipe page DELETE button, the pop-up confirmation message pop up on the screen. Clicking AGREE the recipe will be deleted from the page and redirected back to a user profile page. Clicking CLOSE the pop up message will close. | Tested, works as should.| No |
| Clicking the single recipe page HOME button, the user has been routed to home page. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons has been routed to the blank page of this website. | Tested, works as should.| No |

### Edit Recipe page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link has been routed to the user's profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to the Login page. | Tested, works as should.| No |
| Clicking the EDIT recipe Category field, the user can choose the category from the list.| Tested, works as should.| No |
| Clicking the EDIT recipe, Recipe Name field, the user can edit or enter the new recipe name, must be length between 5-50 characters. Display error message when characters are over than in range.| Tested, works as should.| No |
| Clicking the EDIT recipe, Recipe Ingredients field, the user can edit or enter the new recipe ingredients, which must be thelength between 5-3000 characters. All text can be separated on the new line. Display error message when characters are over than in range. | Tested, works as should.| No |
| Clicking the EDIT recipe, Instructions field, the user can edit or enter the new recipe instructions, which must be the length between 5-3000 characters. All text can be separated on the new line. Display error message when characters are over than in range. | Tested, works as should.| No |
| Clicking the EDIT recipe, an Image URL field, the user can edit or paste the new recipe IMG URL. Added an invalid URL or longer than 300 characters should display an error message. | Tested, works as should.| No |
| Clicking the EDIT recipe, Prepare Time field, the user can edit or enter the new number between 0-120 (min). Added number out of range when and clicking submit button should display an error message. | Tested, works as should.| No |
| Clicking the EDIT recipe, Cook Time field, the user can edit or enter the new number between 0-120 (min). Added number out of range when and clicking submit button should display an error message. | Tested, works as should.| No |
| Clicking the EDIT recipe, Serving field, the user can edit or enter the new number between 1-10. Added number out of range when and clicking submit button should display an error message. | Tested, works as should.| No |
| Clicking the EDIT recipe CANCEL button, the user has been redirected to the SINGLE recipe page without any change on the recipe. | Tested, works as should.| No |
| Clicking the EDIT recipe EDIT RECIPE button, the user has been routed to the SINGLE recipe page with newly new updated recipe. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons has been routed to the blank page of this website. | Tested, works as should.| No |

### Manage Categories page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link, has been routed to the users profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link, has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to Login page. | Tested, works as should.| No |
| Clicking ADD CATEGORY button, the website admin has permision to do that and has been routed to ADD CATEGORY page. | Tested, works as should.| No |
| Clicking EDIT CATEGORY button, the website admin has permision to do that and has been routed to EDIT CATEGORY page. | Tested, works as should.| No |
| Clicking DELETE CATEGORY button, the website admin has permision to do that and the pop up confirmation message pop up on the screen. Clicking AGREE the category will be deleted from the page. Clicking CLOSE the pop up message will close. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |

### Create Category page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link, has been routed to the users profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link, has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to Login page. | Tested, works as should.| No |
| Clicking Category Name field, the admin can enter 3-20 characters long text. Display error message if text is out of range. | Tested, works as should.| No |
| Clicking ADD CATEGORY button, the admin has been routed to the MANAGE CATEGORIES page and the new category will be added in alphabetical order. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |

### Edit Category page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicking on the navigation bar's Profile link, has been routed to the users profile page.| Tested, works as should.| No |
| Clicking on the navigation bar's New Recipe link, has been routed to the add new recipe page.| Tested, works as should.| No |
| Clicking on the navigation bar's Manage Categories link(only admin has access), has been routed to the categories page only admin has access to this link. | Tested, works as should.| No |
| Clicking on the navigation bar's Log Out link, should log out the user from the website and has been routed to Login page. | Tested, works as should.| No |
| Clicking Category Name field, the admin can enter 3-20 characters long text. Display error message if text is out of range. | Tested, works as should.| No |
| Clicking CANCEL button, the admin has been routed back to MANAGE CATEGORIES page. | Tested, works as should.| No |
| Clicking EDIT CATEGORY button, the admin has been routed to the MANAGE CATEGORIES page and the edited category will be added in alphabetical order. | Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |

### Login page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicinkg on the navigation bar's Login link has been routed to the login page.| Tested, works as should.| No |
| Clicking on the navigation bar's Register link, has been routed to the register page.| Tested, works as should.| No |
| Clicking on the USERNAME input field, the entered text can be any letter or number and 5-15 characters long. Display an error message for special character or not in range. | Tested, works as should.| No |
| Clicking on the PASSWORD input field, the entered text can be any letter or number and 5-15 characters long. Display an error message for special character or not in range. | Tested, works as should.| No |
| Clicking LOG IN button, the username and password have to match the user's inputs in registration page. If it match the user has been routed to Profile page, if not match user will redirected back to Login page, and display message for incorrect of the input fields. | Tested, works as should.| No |
| Clicking on the  Register ACCOUNT link below LOGIN form, has been routed to the register page.| Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |

### Register page manual test

|   Test              |  Result         |  Errors                                                            
| ------------------- | --------------- | ------------------------------------------------------------------ |
| Clicking on the navigation bar's navbar logo and a Home link has been routed to the home page.| Tested, works as should.| No|
| Clicinkg on the navigation bar's Login link has been routed to the login page.| Tested, works as should.| No |
| Clicking on the navigation bar's Register link, has been routed to the register page.| Tested, works as should.| No |
| Clicking on the USERNAME input field, the entered text can be any letter or number and 5-15 characters long. Display an error message for special character or not in range. | Tested, works as should.| No |
| Clicking on the PASSWORD input field, the entered text can be any letter or number and 5-15 characters long. Display an error message for special character or not in range. | Tested, works as should.| No |
| Clicking REGISTER button, if all input fields entered correctly, than the user has been routed to Profile page. | Tested, works as should.| No |
| Clicking on the  Log In link below REGISTER form, has been routed to the login page.| Tested, works as should.| No |
| Clicking in the footer social media one of the icons, has been routed to the blank page of this website. | Tested, works as should.| No |
