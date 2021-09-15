# <center>**The Homemade Kitchen**

## Milestone 3 Project - Backend Development Milestone Project

### [View live project here](https://ms3-cookbook-project.herokuapp.com/)
![Image of the mockup of the live website](docs/testing/Mockup.png)

## OVERVIEW

The main reason behind creating this test documentation is to reduce any bugs and errors left on the software, like not working links, responsive issues, font-sizes... and this way improve User Experience and increase traffic to the site.

From the very beggining I used Google Chrome Dev Tools to style and fix the code on real time. This helped fix mistakes and errors on a timely manner as the tool helped to see responsive, styling and typo errors as I coded.

Once finished, I tested my site on a two different phones, laptop, tablet and desktop as well as DevTools and different browsers manually.

## Table of Content

1. [USER STORIES](#user-stories-testing)
    - [Anonymous user](#anonimus-user)
    - [Registered user](#registered-user)
    - [Admin user](#admin-user)
2. [VALIDATOR CHECKS](#validator)
   - [HTML](#html-validator)
     - Index.html
     - Game.html
     - End.html
   - [CSS](#css-validator)
     - style.css
     - game.css
     - highscore.css
   - [JSHint](#jshint-validator)
3. [LIGHTHOUSE TESTING](#lighthouse-testing)
   - Mobile
   - Desktop
4. [DEVICE RESPONSIVENESS](#device-responsiveness)
5. [BROWSER COMPATIBILITY](#browser-compatibility)
6. [BUGS](#bugs)
7. [KNOWN BUGS](#known-bugs)
8. [BACK TO README.md](README.md)

## USER STORIES TESTING

### **User stories**

#### Anonymous user:

- see all the recipes on the main page:
    - When the user loads the page, it brings the to the page where all recipes are displayed. This is available to non registered or anonymous users.
    ![screenshot of main page](docs/testing/user-stories/homepage.png)

- to be able to find information effortessly:
    - Any user has the option to search for specific recipes by name, by difficulty or course type
    ![screenshot of search bar](docs/testing/user-stories/search.png)
    ![screenshot of search words](docs/testing/user-stories/search-words.png)
    
    - There is a view full recipe button to open the recipe on a separate page where all the information is displayed
    ![screenshot of full view](docs/testing/user-stories/full-recipe-btn.png)
    ![screenshot of full view](docs/testing/user-stories/full-view.png)

- not to be able to add any recipes without registered
    - Users have a button on under the navbar which will redirect them to the login page.
    ![screenshot of navbar anonymous user](docs/testing/user-stories/anonymous-navbar.png)
    
- Not to be able to edit/add/remove any recipes others have created
    - users are not able to add, edit or delete any recipes without being logged in. No buttons are displayed unless a user is logged.  
    - Anonymous users are not able to see any of the buttons available at the bottom of the recipe card.
    ![screenshot of no buttons](docs/testing/user-stories/nobuttons.png)

#### As a registered user I want to:

- be able to manage my own posts by editing and/or deleting them
    - registered and logged users are able to manage only the recipes they have created from various places.
    ![screenshot of butns in hompage](docs/testing/user-stories/homepage-edit-delete.png)
    ![screenshot of full recipe edit and home page edit](docs/testing/user-stories/btns-full-view.png)

    - If the user tries to delete a recipe they created, a modal will be triggered to check if they want to continue with their operation. In the same modal the user is given the option to edit or cancel instead of deleting the recipe.
    ![screenshot of modal](docs/testing/user-stories/delete-modal.png)
    - Only session users can edit their own recipes. Not available on others recipe (see red box)
    ![screenshot of edit/delete buttons](docs/testing/user-stories/only-session-user.png)
- be able to create my own recipes and post them for everyone to see them
    - uppon loggin, the user is redirected to the users profile where they can add a recipe from a call to action button located on it, or from the main page where the user has the add recipe button on the top and in the navigation links
    ![screenshot of profile add](docs/testing/user-stories/profile-add.png)
    ![screenshot of main page add](docs/testing/user-stories/add-homepage.png)
- not to be allowed to remove any other posts except mine
    - in the same way as the visible button for only authorized and logged users, the user can only see the delete button on the recipes that the session user has created. This targets the recipe_by key value. Only username and recipe by matching recipes are available to see to the user. 
    ![screenshot of authorized recipes](docs/testing/user-stories/only-session-user.png)

- not to lose any recipes because others have removed it
    - As the option before, other users don't have the option to see my recipes either.

 #### As the admin I want to:

- be able to delete any users recipes:
    - the admin user has the option to delete all users recipes
    ![screenshot admin delete](docs/testing/user-stories/admin-access.png)
- be able to edit any users recipes
    - the admin user has the option to edit all users recipes
    ![screenshot admin delete](docs/testing/user-stories/admin-access.png)
- have unique access to all features 
    - the admin user has access to all funtionality. Admin can delete, edit any course created by any registered user. Furthermore, the user has unique tab for managing categories that are displayed for all user at the time of creating a recipe. This option allows admin user to add, edit and remove course types.
    ![screenshot admin access](docs/testing/user-stories/courses-admin.png)
    ![screenshot admin new course](docs/testing/user-stories/new-course-admin.png)