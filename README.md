# **The Homemade Kitchen**</center>

## Milestone 3 Project - Backend Development Milestone Project

### [View live project here](https://ms3-cookbook-project.herokuapp.com/)
![Image of the mockup of the live website](docs/testing/Mockup.png)

## Overview

This website is a virtual cookbook to save and keep track of personal recipes and allow other users to share with others their own culinary creations, family traditions, etc.

The website will be responsive and accessible on all devices, but it's optimized to be seen on a small/medium screens, as the user will want to have the device close to them to be able to cook along with it. The website will be visually pleasant, focusing on the posibility to update the data available to the user. It will be aimed for those people who want to store and share their own cooking creations with others.

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

4. [TECHNOLOGIES USED](#technologies-used)

- [Syntax](#syntax)
- [Frameworks, Libraries & Programs](#frameworks-libraries-&-programs)

5. [TESTING](#testing)

- [Testing document](TESTING.md)

6. [DEPLOYMENT](#deployment)

- [Heroku](#heroku)
- [Forking the repository](#forking-the-GitHub-repository)
- [Making a local clone](#making-a-local-clone)

7. [CREDITS](#credits)

8. [REFERENCES](#references)

9. [ACKNOWLEDGEMENTS](#acknowledgements)

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

The main goal of this website is to convert visitors into active users. As this website aims to create a sense of comunity for those users that want to share their own recipes, the option to create, edit and delete recipes will be only available to registered users. To convert a visitor the landing page will try to convince users to register, which will show a bright palette as well as aesthetically pleasing imagery to invite users to start cooking themselves.

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

  - This page can be done with Materialize framework to create a structure and implement sections that the user needs. The website will be kept separated in 5 main sections (landing, sign in, log in,, add recipe, edit and delete recipe) but easily accessible from the homepage (the functionalities of add edit and delete will be just available for registered users). 

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

- The structure of the site will be layed out in five pages.The landing page (homepage) where the user will be able to easily register, log in, add recipe, edit and delete recipe (for registered users only) and a logout option for those logged in. The basic structure of the website is:

  - Header/Navigation - Top Level

    - The navigation menu will be a hamburger/bars menu icon on smaller screen sizes. It will be fixed/sticky in the top right corner allowing the user to navigate with a single hand. The navigation bar will have extra links with access to the CRUD functionality for members only.
    - Withing the header, in the middle, there will be a search bar so the user will have a fast access to it.
    - The header will have a hero section to create a pleasant look so the users enjoy the experience of using the site. It will be divided in two colums: One column which includes a hero image with information about the website and the other column will contain the registration form, a log in link for members, and a call to action as a sign up button.

  - Body - Main Page Elements: 

    - It will contain all the recipes in cards. The user will be able to click on a call to action button to extend the recipe and show it on the middle of the page.
    - The pages specific to using forms will have minimal extra content to make the forms the only imporatnt part of the section
  
  - Footer - Bottom Level
   
    - Social media links placed here to ensure the user does not navigate away from the page to soon.
    - Creators information

---

### Skeleton Plane

#### Wireframes:
  - [Mobile Wireframe](docs/wireframes/Mobile.png)
  - [Ipad Wireframe](docs/wireframes/Ipad.png)
  - [Desktop Wireframe](docs/wireframes/Desktop.png)


## DESIGN

The design of the website was created to be as simple but pretty as posible, not to distract the user with too many color schemes and trying to bring the focus to the picture of the recipes.

### **Colors**

The colors used in this project are very simple, to keep a minimalistic and tidy website, as well as keeping the color contrasts the highests posible to facilitate the screen readers and make this site accessible to all.

The colors chosen are combinations of: bright orange with dark typography, white and shades of grey. The color were found using [Coolors](https://coolors.co/).

Some of the colors used in this project are: [....................this to be changed.................]
- rgb(87, 15, 55): this color was used as the main color, but I've added opacity to make different shades of it.
- rgba(173, 169, 183, 0.7): used as a background color.
- #fff: used as button background color.

---

### **Typography**

The fonts used for the site were taken from [Google Fonts](https://fonts.google.com/). To make sure the questions are represented on a fun way but easy to read, it was decided to use simple but and consistent fonts previously used in other projects within Code Institute like:

- "Montserrat alternates": to create fun and attractive fonts as well as drawing attention to the most important information.
- "Quicksand": for more suttle but attractive font. It's clean and simple, making this a pleasant font to look at.
- Sans-serif: used as a fallback font in cases there is an issue when importing fonts or the browser does not support these.

---

### **Imagery**

- As this project will be focused on the data rather than the frontend design of the website, the images will be included as an URL. The user will have to provide a URL if they want to show an image as a thumbnail of the recipe. 

- The hero image will be the only image that it will be included in this project.

---

### **Logo**

- The favicon was created using [Favicon.io](https://favicon.io/favicon-converter/) and the logo used to create it was created using an online application called [Canva](https://www.canva.com/). It represents cooking tools nodding the  main subject of the website. The use of the favicon makes it easier to recognize the application tab in between others that the user might have had already opened.

- The logo's design represents theme of the site and is easily recogniseable by users as a movie orientated game.

---

### **Database Model**

- This project uses MongoDB for all database aspects. MongoDB is a cross platform document-orientated database program. Classified as a NoSQL database program it uses JSON-like documents with optional schemas.

- The main schema used in this project is ObjectId.

- ((add database images here))
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
-  

---