# <center>**The Homemade Kitchen**

## Milestone 3 Project - Backend Development Milestone Project

### [View live project here](https://ms3-cookbook-project.herokuapp.com/)
![Image of the mockup of the live website](docs/testing/Mockup.png)

## Overview

This website is a virtual cookbook to save and keep track of personal recipes and allow other users to share with others their own culinary creations, family traditions, etc.

The website will be responsive and accessible on all devices, but it's optimized to be seen on medium screens, as the user will want to have the device close to them to be able to cook along with it. The website will be visually simple but pleasant, focusing on the posibility to update the data available to the user. It will be aimed for those people who want to store and share their own cooking creations with others.

---

## Table of Contents

1. [UX](#ux)

- [User Stories](#user-stories)
- [Game goals](#game-goals)
- [User Centered Design](#user-centered-design)
  - [Strategy plane](#strategy-plane)
    - [User needs](#user-needs)
    - [Technical capabilities](#technical-capabilities)
  - [Scope plane](#scope-plane-|-trade-offs)
  - [Structure plane](#structure-plane)
  - [Skeleton plane](#Skeleton-plane)

2. [DESIGN](#design)

- [Color scheme](#color-scheme)
- [Typography](#typography)
- [Imagery](#imagery)
- [Logo](#logo)

3. [FEATURES](#features)

- [Existing Features](#existing-features)
- [Features left to implement](#features-left-to-implement)

4. [DATABASE MODEL](#database-model)

- [Users Data](#users-data)
- [Recipes Data](#recipes-data)
- [Courses Data](#courses-data)

5. [TECHNOLOGIES USED](#technologies-used)

- [Syntax](#syntax)
- [Frameworks, Libraries & Programs](#frameworks-libraries-&-programs)

6. [TESTING](#testing)

- [Testing document](TESTING.md)

7. [DEPLOYMENT](#deployment)

- [Heroku](#heroku)
- [Forking the repository](#forking-the-GitHub-repository)
- [Making a local clone](#making-a-local-clone)

8. [CREDITS](#credits)

9. [REFERENCES](#references)

10. [ACKNOWLEDGEMENTS](#acknowledgements)

## UX

### **User stories**

 #### As an anonymous user I want to:
  - see all the recipes on the main page
  - to be able to find information effortessly
  - not to be able to add any recipes without registered
  - Not to be able to edit/add/remove any recipes others have created

 #### As a registered user I want to:
  - be able to manage my own posts by editing and/or deleting them
  - be able to create my own recipes and post them for everyone to see them
  - not to be allowed to remove any other posts except mine
  - not to lose any recipes because others have removed it

 #### As the admin I want to:
  - be able to delete any users recipes 
  - be able to edit any users recipes
  - have unique access to all features 

---

## USER CENTERED DESIGN

### **Strategy Plane**

- #### User needs

The main goal of this website is to convert visitors into active users. As this website aims to create a sense of community for those users that want to share their own recipes, all users will be able to search and see all recipes, leaving the options to create, edit and delete recipes will be only available to registered users. To convert a visitor the landing page will display all recipes to convince users to continue using the website, allowing them to become registered users. The website will show a bright palette as well as minimalistic but aesthetically pleasing imagery to invite users to start cooking themselves.

There is already thousands of recipe and cooking websites, but not many of them allow users to contribute into them. Many of us have recipe notebooks at home, that when most needed are not accessible, or we cannot find them. But most of us have the phones close to us most time of the day. Taking this in account, this website is the perfect place to create a profile where you can savely store our most precious recipes, where will be saved for (virtually) forever. 

The steps a new user would idealy take when arriving into the website would be the following:

 - Explore the websites landing page, where the information will explain the user the reason to be of the site.
 - Create a new account.
 - Explore the additional features available to registered users.
 - create their own recipes and see them posted on the main page
 - Access and edit posted recipes to be able to update/make changes on them.
 - Delete created recipes that the user doesn't want to see anymore.

This will all be achieved through creating a clear and strong UI focusing on well structured content. Having a clear hierarchy will allow the user to navigate and use the functionality of the website without the need of instructions.

- #### Technical capabilities

  - To use this site the user needs to have access to some internet connection within their chosen device.

  - They also need to have basic understanding on how to select and navigate the page.

  - This page will be done with Materialize framework to create a responsive structure and implement sections that the user needs. The website will be kept separated in 5 main sections (landing, sign in, log in,, add recipe, edit and delete recipe) but easily accessible from the homepage (the functionalities of add edit and delete will be just available for registered users). The admin will have an extra section to add more courses to allow the searches be more specific and easier to group for users. 

---

### **Scope plane | Trade-offs**

- **Features within the design plan with highest priority:**

  - Minimal but appealing homepage 
  - Navigation links clearly visible on the top of the website.
  - Responsive navigation bar
  - Only allow registered users to create and manage their own account.
  - Only allow registered users to create recipes with full CRUD functionality.
  - A form with steps to allow users create their recipes fast and easily

- **Lower priority features that may not be included in the initial release of the website:**

  - Responsive sticky navigation bar.
  - The ability for logged in users to search the websites database
  - Search bar on the navigation bar so the users have fast access to recipes
  - Contact section to send an email to the Admin
  - A comment section that allow all users to write their own opinions under each recipe
  - A recipe rating option with stars
  - A gallery section for the users to upload their own images of created recipes.

---
### Structure Plane

- The structure of the site will be layed out in four pages (five pages for admin).The landing page (homepage) where the user will be able to see all the recipes available. Anonimus users will be allowed to navigate through all recipes, being able to see them in its own page, to easily read the recipes. If an anonimus user wants to become a member, they have the option to log in, add recipe, edit and delete recipe their own recipes once they have registered and logged in. When a user logs in, they will directed to their profile, where they can choose what to do. Members are only able to manipulate the recipes they have created. Only the admin user has access to all functionalities. The admin user has the capability to add new courses, which will then be available in the dropdown for users to select. Logged in users will have the logout option to stop their session cookies. The basic structure of the website is:

  - Header/Navigation - Top Level

    - The navigation menu will be a hamburger/bars menu icon on smaller and medium screen sizes. It is not sticky as the users have all available functionality in various places repited on the website. The hamburger menu will be located in the top right corner allowing the user to navigate with a single hand. The navigation bar will have extra links with access to the CRUD functionality for members only. 
      - Anonimus users will only be able to see the following links: Home (all recipes), Log in and Register.
      - Registered and logged in users will be able to see the following links: Home (all recipes, available to all), Profile(personalized with each users name and options to add a recipe and see all recipe links), Add recipe (direct link to a form to add a new recipe), Log Out (end session). 
      - Admin user has access to all links to functionality registered users have plus the option to add a course.
    - The navigation bar will be responsible and will reduce to a hamburger size to keep all links tidy and organized. The hamburger menu will be positioned on the right side so users can access to the navigation links with the right hand. 

  
  - Body 
  
    - Home Page Elements: 

      - Under the navigation bar, anonimus users will see a button prompting them to register or log in to be able to share their recipes. Logged in users and admin user will be able to see a button linked to add recipe. This allow the user to have the option to add a recipe from the main page without the need to open the hamburger menu to access the navigation link. The idea of this is to allow the user navigate the website with as few clicks as possible. 
      - Under the button there will be a search bar so the user will be able to find their recipe on a fast manner. This functionality is available to all type of users.
      - All recipes will be displayed on individual cards, which will contain an image as a visual representation and guide for a finished product, the card title, a very short description, a little carrot to with a toolkit if the recipe is vegetarian and a button to display the whole recipe and all the data on a separate page.
      - At the bottom of each recipe will have a delete button on the left and a green edit button on the right. This will only be visible for recipes created by the the user or for the admin user. 
      - The delete call to action button will open a modal to ask the user to verify their decision.
      - The edit button will open the edit form with populated fields so the user can see the precious data and choose what to change.

    - Register Page Elements:

      - A card containing a form with input fields for a possible user to enter their username, password and another input field to confirm the entered password.
      - A call to action button to add the username and password to the MongoDB database. If successful the user will be redirected to their new profile page and displayed a flash message confirming the registration to the database.
      - The new registered user will now have access to the rest of functionalities (add, edit and delete recipes)

    - Profile Page Elements (only accessible to authenticated and authorized users):

      - The user will be welcomed with a message and the users username. 
      - A flash message will give feedback when logged in.
      - Three cards divided in two columns will display options to the user:
        - See all recipes: redirects the user to the home page displaying all recipes
        - Add a new recipe: redirects the user to the add recipe form
        - ONLY FOR ADMIN: Add a course: redirects the admin user to the add a course form
      - A Logout button for users who want to end the session from the profile page.

    - Add Recipe Page Elements (accessible to all logged users):

      - The user will be presented with a form with inputs and dropdowns the user to fill and select options.
      - The required inputs and dropdowns will be underlined in red color if not filled. Properly filled fields will be underlined in green.
      - All fields will have placeholders or labels to hint the user on the information needed for each input.
      - A switch to choose if the recipe is vegetarian or not
      - The user will have two buttons at the end to cancel and be redirected to the home page or a submit button to add the data to MongoDB. Once the recipe has been successfully registered the user will get a flash message as feedback and will be redirected to the home page where the user will be able to see all the recipes including the new inserted one.
  
    - Add Course Page Elements (accessible only to admin):

      - A single input form to allow the admin user inset extra course types to database. All the courses will be displayed once the admin clicks on either the cancel or add buttons.
      - All new courses the admin adds are available when the user is creating or editing a recipe under the 'recipe type' dropdown.

    - Edit recipe (not accessible from the navbar):
      
      - Users are able to access to this page from two different places: on the homepage under the recipe cards and under the view of the full recipe
      -  When clicked on the green edit button, the user will be able to see the information that they inserted previously, so they can review the information and make the necessary changes to them.
      - When the user submits the form, this information updates the data already stored on the database under the specific id number.

    - Manage Course (only available to admin user):
      
      - Admin will be shown all the courses available on cards. At the bottom of the card the admin user is allowed to edit or delete the course chosen.
      - The delete button will trigger a modal prompting the admin user to confirm if they want to delete or cancel the action.
      - The edit button will open the course form already filled, so the admin user can edit it and update the database with the new information.

  - Footer - Bottom Level
   
    - The website name
    - Copyright simbol
    - The creator name
    - Social links to allow users to further connect and interact with the 'community' by following the social media accounts for the page.

---

### Skeleton Plane

#### Wireframes:
  - [Mobile Wireframe](docs/wireframes/Mobile-wireframes.png)
  - [Ipad Wireframe](docs/wireframes/Ipad-wireframes.png)
  - [Desktop Wireframe](docs/wireframes/Desktop-wireframes.png)


## DESIGN

The design of the website was created to be as simple but pretty as posible, not to distract the user with too many color schemes and trying to bring the focus to the picture of the recipes to tempt the user to return and become members.

### **Colors**

The colors used in this project are very simple, to keep a minimalistic and tidy website, as well as keeping the color contrasts the highests posible to facilitate the screen readers and make this site accessible to all.

The colors chosen are combinations of: teal with white text, blue for add course button, orange to log out, red for delete and green for edit. This colors where taken from the [Materialize](https://materializecss.com/color.html) css section. 

- #26a69a: for navbar, course card background, headers and most home page buttons to keep a balance between the images and the rest of the buttons.
- #f44336: for delete buttons
- #4caf50: for edit buttons
- #03a9f4: to add card button, add recipe submit button, edit recipe button, cancel button on modal.
- #ff9800: for logout button on profile page.

---

### **Typography**

The fonts used for the site were taken from [Google Fonts](https://fonts.google.com/). To make sure the questions are represented on a fun way but easy to read, it was decided to use simple but and consistent fonts previously used in other projects within Code Institute like:

- "Love Ya Like A Sister": used for the name of the website
- "Montserrat alternates": to create fun and attractive fonts as well as drawing attention to the most important information.
- "Quicksand": for more suttle but attractive font. It's clean and simple, making this a pleasant font to look at.
- Sans-serif: used as a fallback font in cases there is an issue when importing fonts or the browser does not support these.

---

### **Imagery**

- As this project will be focused on the data rather than the frontend design of the website, the images will be included as an URL. The user will have to provide a URL to add the respective image to the top of the recipe. This image can be used as a guide of the end product of that certain recipe.

- Although in the beginning a background was added, it made the important information lose importance, so it was decided to keep just the recipe images as the focus of data.

---

### **Logo**

- The favicon was created using [Favicon.io](https://favicon.io/favicon-converter/) and the logo used to create it was created using an online application called [Canva](https://www.canva.com/). It represents cooking tools nodding the  main subject of the website. The use of the favicon makes it easier to recognize the application tab in between others that the user might have had already opened.
( *This logo was not used in the final draft*)

- As a logo, I used the Name of the website, as the words already explain what the website is about. The typography used was imported from google fonts called 'Love Ya Like a sister'.

---

### **Database Model**

- This project uses MongoDB for all database aspects. MongoDB is a cross platform document-orientated database program. Classified as a NoSQL database program it uses JSON-like (BSON) documents with optional schemas.

- The main schema used in this project is ObjectId.

- Users data:

      | Title              | Data Type     |
      | ------------------ |:-------------:|
      | _id                | ObjectId      |
      | username           | string        |
      | password           | string        |

- Recipes data:

      | Title              | Data Type     |
      | ------------------ |:-------------:|
      | _id                | ObjectId      |
      | course_type        | string        |
      | recipe_name        | string        |
      | recipe_description | string        |
      | image_url          | string        |
      | recipe_difficulty  | string        |
      | ingredient_1       | string        |
      | ingredient_2       | string        |
      | ingredient_3       | string        |
      | ingredient_4       | string        |
      | ingredient_5       | string        |
      | ingredient_6       | string        |
      | ingredient_7       | string        |
      | direction_1        | string        |
      | direction_2        | string        |
      | direction_3        | string        |
      | direction_4        | string        |
      | direction_5        | string        |
      | direction_6        | string        |
      | direction_7        | string        |
      | prep_time          | string        |
      | cook_time          | string        |
      | serves             | string        |
      | vegetarian         | string        |
      | recipe_by          | string        |

- Courses data:

      | Title              | Data Type     |
      | ------------------ |:-------------:|
      | _id                | ObjectId      |
      | course_type        | string        |
      
---

## FEATURES

### Existing Features

- All buttons and links will be styled with hovering effects to invite the user to click on them.
- The logo, seach bar and will stay static along the website to give the website consistency.

- **Homepage:** 

 

- **Sign In:**


- **Log In:** 

  -


---

### Features left to implement

- The option for the user to upload their own images: as it was adviced by student care, this functionality was left out, but would be implemented further down the course, as it will be taught in future lessons.
- Give the option to download all created recipes to create a personalized cookBook and be able to make profit from this
-  Active page class to let the user know which page they are currently on: Although this was an easy input before using flask, I have found this a challenging step to add to this project. As I have been short with times, I have decided to leave this feature for later realeases when I have some extra time to expand the MVP.

---