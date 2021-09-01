# **The Homemade Kitchen**</center>

## Milestone 3 Project - Backend Development Milestone Project

### [View live project here]()

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

- As a user I want to:

    - know that my information is safe and secure on a database
    - be able to manage my own posts by editing and/or deleting them
    - be able to create my own recipes and post them for everyone to see them
    - be able to access the website from multiple devices of different sizes
    - to be able to find information effortessly


### **Website owner goals**

As the site owner, I want:

  - to allow the user to register and create their own account to access their own recipes
  - to lay all information clearly for users to easily navigate throught the website
  - to make sure the website is responsive across major screen sizes
  - to make sure users information is securely stored on a database


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
  - Allow users to create and manage their own account.
  - Allow users to create recipes with full CRUD functionality.
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

    - The navigation menu will be a hamburger/bars menu icon on smaller screen sizes. It will be fixed/sticky in the top right corner allowing the user to navigate with a single hand .

   - Withing the header, in the middle, there will be a search bar so the user will have a fast access to it.

   - The header will have a hero section to create a pleasant look so the users enjoy the experience of using the site. It will be divided in two colums: One column which includes a hero image with information about the website and the other column will contain the registration form, a log in link for members, and a call to action as a sign up button.

  - Body - Main Page Elements: 

   - (the extended navigation bar with access to the CRUD functionality for members only)

   - It will contain all the recipes in cards. The user will be able to click on a call to action button to extend the recipe and show it on the middle of the page.

   - The pages specific to using forms will have minimal extra content to make the forms the only imporatnt part of the section
  
  - Footer - Bottom Level
   
   -   Social media links placed here to ensure the user does not navigate away from the page to soon.

   - Copyright information

 
- 

---

### Skeleton Plane

As this project is the first one for me usign Python and Databases, 
When I started this project, I had the idea of hard coding the questions and separating them in three different themes. As I deployed my project very early on and asked family to check the first look/idea of the game, they recomended to add more variaty of questions as they thought it would get boring for users to play the same 10 questions over and over again.
As I looked into other options to introduce more questions, I found an API with a large trivia database free to use, so I decided to change the first design and make changes to it. Below are the first wireframes and the new ones:

- Wireframes:
  - [Mobile Wireframe](docs/wireframes/Mobile.png)
  - [Ipad Wireframe](docs/wireframes/Ipad.png)
  - [Desktop Wireframe](docs/wireframes/Desktop.png)


## DESIGN

The design of the website was created to be as simple but pretty as posible, not to distract the customer with too many color schemes and trying to bring the focus to the picture of the recipes.

### **Colors**

The colors used in this project are very simple, to keep a minimalistic and tidy website, as well as keeping the color contrasts the highests posible to facilitate the screen readers and make this site accessible to all.

The colors chosen are combinations of: bright orange and darks typography, white and shades of grey. The color were found using [Coolors](https://coolors.co/).

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


- .
---

### **Logo**

- The favicon was created using [Favicon.io](https://favicon.io/favicon-converter/) and the logo used to create it was created using an online application called [Canva](https://www.canva.com/). It represents cooking tools nodding the  main subject of the website. The use of the favicon makes it easier to recognize the application tab in between others that the user might have had already opened.

- The logo's design represents theme of the site and is easily recogniseable by users as a movie orientated game.

---

### **Database Model**

- This project uses MongoDB for all database aspects. MongoDB is a cross platform document-orientated database program. Classified as a NoSQL database program it uses JSON-like documents with optional schemas.

- The main schema used in this project is ObjectId.


---

## FEATURES

### Existing Features

- The site will consist of four pages: homepage, the game page, the end page and the highscores page. Based on the user selection, the user will be taken to the respective page. The site will be responsive for most screen sizes, but it's best enjoyed on medium to large size screens.

- All buttons and links will be styled with hovering effects to invite the user to click on them.

- The logo will stay static along the game to give the website consistency.

- **Homepage:** 

  - Header: An area to introduce the user to the game
  - Image: to set the theme of the quiz visually
  - Controls Section: under the hero image there will be a section highlighted on another darker color with lighter buttons to point the user to the contol section:
    - Start the game Button: 'Start' button to hint the user to click on it to Start the quiz. Clicking this will direct the user to the game.
    - High Score Button: a button directing the user to the top 5 scores page which are saved on the end page. Clickin this button will direct the user to high scores page.
    - A modal button which contains the instructions of the game. clicking this button will open a modal explaining the user the game rules.

- **Sign In:**

 - A section above the displayed question with two areas: the area on the left counts the current question with a progress bar to make the counter more appealing and easier to visually see it. The area on the right display the added score when the user answers the question correctly. - 

- **Log In:** 

  - A section above the displayed question with two areas: the area on the left counts the current question with a progress bar to make the counter more appealing and easier to visually see it. The area on the right display the added score when the user answers the question correctly. 
  - There will be 10 questions on display. The questions have been created thanks to the use of an [open Trivia API](https://opentdb.com/). 
  - If the API fails to load, the user will be presented with an error message prompting them to reload the page and try again.
  - The user will be given 4 multiple choice answers. The user has to click on the answer. The answer will turn red or green depending if the answer is correct or incorrect. The user won't be able to see right answer if the choice is incorrect, as the intention is to be able to retake the quiz and try to beat their own score,
  - The question will automatically load a second after the user has made the selection, so there will not be any buttons for the user to jump into the next question manually. This is to make the user's experience nicer, by clicking less.
    
- **End:** This will be the feedback page.
  - There will be a section with the score summary, which will be updated as the user answers correct questions. As each question is 10 points the maximum amount of points the user can get is 100 points.
  

---

### Features left to implement

- The option for the user to upload their own images: as it was adviced by student care, this functionality was left out, but would be implemented further down the course, as it will be taught in future lessons.

- 

- 

---