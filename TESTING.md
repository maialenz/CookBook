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
    - [CSS](#css-validator)
    - [JSHint](#jshint-validator)
    - [PyLint](#pylint-validator)
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

#### Registered user:

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

 #### Admin user:

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

---

## VALIDATOR:

During the whole project, I continuously checked my code using W3 Validators to make sure I fixed my code as I wrote it. At the end, I ran all the finished pages and made sure all the errors were fixed.

As a css validator, I also used w3 Validator to make sure it checked my style.css file to CSS level 3 + SVG standards.

(See passed validator results at the end of HTML and CSS sections)

### HTML Validator:

- As to develop this project with the [Jinja Templating Engine](https://jinja.palletsprojects.com/en/3.0.x/), the validator would count all url_for() as errors. So I had to validate the code introducing the URL on the [W3 Validator](https://validator.w3.org/) to check the whole website.

- Although the validator gave a warning because a section did not have a header, the reason for this is that this section only shows if there is a message to give feedback to the user. So no header is needed in this case.

- See [HTML Validator results here](docs/testing/validator/html-validator.png)

---

### CSS Validator
- The [jigsaw validator](https://jigsaw.w3.org/css-validator) did not find any errors.

- See [css validator results here](docs/testing/validator/css-validator.png)

---

### JSHint Validator
- [JSHint](https://jshint.com/) did not find any warning or errors.

- See [JSHint validator results here](docs/testing/validator/jshint-validator.png)

---

### Pylint Validator
- After running pylint on the terminal, I got a few warnings:
    - e argument does not user snake_case. I changed this for app_error. This still gives a warning sayin Unused argument. But if this argument is removed from hadle_404(app_error) and server_error(500), the 404.html and 500.html do not render. So it was decided to leave the arguments on plave.
- Unnecessary 'else' after 'return' and unnecessary 'elif' after'return': although I changed the elif statements at (/register) for if statements, I decided to leave the else statement in place on line 124 as changing this for another if statement makes the code a little confusing to understand. 

- See [Pylint validations results here](docs/testing/validator/pylint-validator.png)

---

## LIGHTHOUSE TESTING

Using DevTool's Lighthouse tool, I checked all pages on mobile and desktop to make sure the scores were as high as I posibly could. Below can be found the results and scores the tests tests

(All tests were carried out the same way: I cleared cache data, opened new incognito page (Chrome and Edge), and reloaded and tested each page twice. Same procedure was used for mobile and web assessment)

Due to the simplicity of the website, the results of the lighthouse testing have come back mostly strong. Since there is very few heavy files, the site loads very fast and with no major issues, both on mobile and desktop, increasing like this the UX.

The only major thing to be fixed to improve accessibility was the missing attributes aria-label and alt for images. This was fixed immediately, improving considerably the accessibility scores.

### Mobile:

- [Home mobile Anonimus User:](docs/testing/lighthouse/Mobile-homepage.png)
In the home page the performance was lower than the rest because the loading time of the images.

- [Logged User](docs/testing/lighthouse/logged-home.png)

- [Login Page](docs/testing/lighthouse/login-mobile.png)

- [Register Page](docs/testing/lighthouse/register-mobile.png)

- [Profile Page](docs/testing/lighthouse/mobile-profile.png)

- [Add recipe](docs/testing/lighthouse/add-recipe-mobile.png)

- [Edit Recipe](docs/testing/lighthouse/edit-recipe-mobile.png)

- [Manage Courses](docs/testing/lighthouse/manage-course-mobile.png)

- [Add course](docs/testing/lighthouse/add-course-mobile.png)

- [Edit course](docs/testing/lighthouse/edit-course-mobile.png)

### Desktop:

- [Home mobile Anonymous User:](docs/testing/lighthouse/desktop-anonymous-home.png)

- [Logged User](docs/testing/lighthouse/desktop-home.png)

- [Login Page](docs/testing/lighthouse/desktop-login.png)

- [Register Page](docs/testing/lighthouse/desktop-register.png)

- [Profile Page](docs/testing/lighthouse/desktop-profile.png)

- [Add recipe](docs/testing/lighthouse/desktop-add-recipe.png)

- [Edit Recipe](docs/testing/lighthouse/desktop-edit-recipe.png)

- [Manage Courses](docs/testing/lighthouse/desktop-manage-course.png)

- [Add course](docs/testing/lighthouse/desktop-add-course.png)

- [Edit course](docs/testing/lighthouse/desktop-edit-course.png)

## DEVICE RESPONSIVENESS

I continuously tested the project on various devices from the very beginning. I mostly used Google Chrome DevTools, but as soon as I deployed the website to Heroku, I pushed my code very often to see the results of the changes in real time on my own personal devices (Samsung S8+, HP Envy 13", Samsung 5Se Tablet and Desktop and HP desktop 31.5" screen) and make sure the site was responsive on various viewports. Below are the pictures of the homepage of these viewports as a way a user would see them when arriving at the website:

- Samsung Galaxy S8+: 

![screenshot of samsung s8+](docs/testing/device-responsiveness/galaxys8+.jpeg)

- Samsung A70: 

![screenshot of samsung A70](docs/testing/device-responsiveness/A70.jpeg)

- Samsung Galaxy Tab5e:

![screenshot of samsung Tab](docs/testing/device-responsiveness/Tab5e.jpeg)

- Hp Envy 13":

![screenshot of samsung Envy](docs/testing/device-responsiveness/Envy13.jpeg)

- PC HP 31.5":

![screenshot of HP 31.5"](docs/testing/device-responsiveness/.jpeg)

Apart from that, I used an online app by [Media Genesis](https://responsivedesignchecker.com) as well as Google Chrome Developer tools to manually check responsiveness on those screens I did not have access to.IThe results helped improve the UI on very small viewports like the front screen on the samsung galaxy fold or the iPhone 5, where the viewports are 238px and 320px respectively wide. See bugs to see the fixes. 

## BROWSER COMPATIBILITY

I thoroughly checked on different devices and different browsers. Wherever posible I downloaded the browsers into my devices and I tested my site on them manually, making sure all links were checked and tested. 
As a main conclusion of these tests, I have to add that I did not find any differences from one browser to another. There was full compatibility of all features and links cross browser/device. 

All the screenshots to my manual tests on various major devices are below:

- Samsung Galaxy S8+ (My personal device) (mobile device): As mentioned before, I continuously tested my code on my own mobile device as I went writting and styling the code as I had deployed to Heroku as soon as I created the needed files, so I could see how it looked on smaller screens. Thanks to testing on my phone I noticed the headings had to be made a little smaller it did look oversized. Below there is screenshots of a last test done on this device:

    - [Samsung S8+ screenshot home](docs/testing/browser-tests/samsungs8+-home.jpeg)
    - [Samsung S8+ screenshot full recipe](docs/testing/browser-tests/samsungs8+-full-recipe.jpeg)
    - [Samsung S8+ screenshot full recipe bottom](docs/testing/browser-tests/samsungs8+-full-recipe-bottom.jpeg)
    - [Samsung S8+ screenshot navbar](docs/testing/browser-tests/samsungs8+-navbar.jpeg)
    - [Samsung S8+ screenshot login](docs/testing/browser-tests/samsungs8+-login.jpeg)
    - [Samsung S8+ screenshot register](docs/testing/browser-tests/samsungs8+-register.jpeg)
    - [Samsung S8+ screenshot profile](docs/testing/browser-tests/samsungs8+-profile.jpeg)
    - [Samsung S8+ screenshot profile bottom](docs/testing/browser-tests/samsungs8+-profile-bottom.jpeg)
    - [Samsung S8+ screenshot edit delete option for logged user only](docs/testing/browser-tests/samsung8+-options.jpeg)
    - [Samsung S8+ screenshot add recipe](docs/testing/browser-tests/samsungs8+-add.jpeg)
    - [Samsung S8+ screenshot edit recipe](docs/testing/browser-tests/samsungs8+-edit.jpeg)
    - [Samsung S8+ screenshot delete recipe](docs/testing/browser-tests/samsungs8+-delete.jpeg)
    - [Samsung S8+ screenshot full recipe](docs/testing/browser-tests/samsungs8+-full.jpeg)
    - [Samsung S8+ screenshot add course](docs/testing/browser-tests/samsungs8+-add-course.jpeg)
    - [Samsung S8+ screenshot edit course](docs/testing/browser-tests/samsungs8+-edit-course.jpeg)
    - [Samsung S8+ screenshot courses](docs/testing/browser-tests/samsungs8+-courses.jpeg)
    - [Samsung S8+ screenshot full recipe bottom](docs/testing/browser-tests/samsungs8+-full-recipe-bottom.jpeg): The user here has the authorization to see the delete/edit options because the user is the creator of the recipe


- Samsung A70 (mobile device): I also tested the website on another mobile device:

    - [Samsung A70 screenshot home](docs/testing/browser-tests/A70-home.jpeg)
    - [Samsung A70 screenshot full recipe](docs/testing/browser-tests/A70-full-recipe.jpeg)
    - [Samsung A70 screenshot full recipe bottom](docs/testing/browser-tests/A70-full-recipe-bottom.jpeg)
    - [Samsung A70 screenshot navbar](docs/testing/browser-tests/A70-navbar.jpeg)
    - [Samsung A70 screenshot login](docs/testing/browser-tests/A70-login.jpeg)
    - [Samsung A70 screenshot register](docs/testing/browser-tests/A70-register.jpeg)
    - [Samsung A70 screenshot profile](docs/testing/browser-tests/A70-profile.jpeg)
    - [Samsung A70 screenshot profile bottom](docs/testing/browser-tests/A70-profile-bottom.jpeg)
    - [Samsung A70 screenshot edit delete option for logged user only](docs/testing/browser-tests/A70-options.jpeg)
    - [Samsung A70 screenshot add recipe](docs/testing/browser-tests/A70-add.jpeg)
    - [Samsung A70 screenshot add recipe bottom](docs/testing/browser-tests/A70-add-bottom.jpeg)
    - [Samsung A70 screenshot edit recipe](docs/testing/browser-tests/A70-edit.jpeg)
    - [Samsung A70 screenshot delete recipe](docs/testing/browser-tests/A70-delete.jpeg)
    - [Samsung A70 screenshot full recipe](docs/testing/browser-tests/A70-full.jpeg)
     - [Samsung A70 screenshot full recipe bottom](docs/testing/browser-tests/A70-full-recipe-bottom.jpeg): The user here does not have the authorization to see the delete/edit options because it's not the creator of the recipe


- Samsung S5e (tablet)

    - [Galaxy Tab S5e home](docs/testing/browser-tests/5se-home.jpg)
    - [Galaxy Tab S5e full recipe](docs/testing/browser-tests/5se-full-recipe.jpg)
    - [Galaxy Tab S5e full recipe bottom](docs/testing/browser-tests/5se-full-recipe-bottom.jpg)
    - [Galaxy Tab S5e navbar](docs/testing/browser-tests/5se-navbar.jpg)
    - [Galaxy Tab S5e login](docs/testing/browser-tests/5se-login.jpg)
    - [Galaxy Tab S5e register](docs/testing/browser-tests/5se-register.jpg)
    - [Galaxy Tab S5e profile](docs/testing/browser-tests/5se-profile.jpg)
    - [Galaxy Tab S5e profile bottom](docs/testing/browser-tests/5se-profile-bottom.jpg)
    - [Galaxy Tab S5e edit delete option for logged user only](docs/testing/browser-tests/5se-options.jpg)
    - [Galaxy Tab S5e add recipe](docs/testing/browser-tests/5se-add.jpg)
    - [Galaxy Tab S5e add recipe bottom](docs/testing/browser-tests/5se-add-bottom.jpg)
    - [Galaxy Tab S5e edit recipe](docs/testing/browser-tests/5se-edit.jpg)
    - [Galaxy Tab S5e delete recipe](docs/testing/browser-tests/5se-delete.jpg)
    - [Galaxy Tab S5e add course](docs/testing/browser-tests/5se-new-course.jpg)
    - [Galaxy Tab S5e edit course](docs/testing/browser-tests/5se-edit-course.jpg)
    - [Galaxy Tab S5e courses](docs/testing/browser-tests/5se-courses.jpg)
    - [Galaxy Tab S5e full recipe](docs/testing/browser-tests/5se-full.jpg)
    - [Galaxy Tab S5e full recipe bottom](docs/testing/browser-tests/5se-full-recipe-bottom.jpg)

- HP Envy 13" (laptop)

    - Google Chrome (browser):
        - [HP Envy Chrome home](docs/testing/browser-tests/chrome-home.png)
        - [HP Envy Chrome login](docs/testing/browser-tests/chrome-login.png)
        - [HP Envy Chrome register](docs/testing/browser-tests/chrome-register.png)
        - [HP Envy Chrome profile](docs/testing/browser-tests/chrome-profile.png)
        - [HP Envy Chrome profile bottom](docs/testing/browser-tests/chrome-profile-bottom.png)
        - [HP Envy Chrome edit delete option for logged user only](docs/testing/browser-tests/chrome-options.png)
        - [HP Envy Chrome add recipe](docs/testing/browser-tests/chrome-add.png)
        - [HP Envy Chrome add recipe bottom](docs/testing/browser-tests/chrome-add-bottom.png)
        - [HP Envy Chrome edit recipe](docs/testing/browser-tests/chrome-edit.png)
        - [HP Envy Chrome delete recipe](docs/testing/browser-tests/chrome-delete.png)
        - [HP Envy Chrome add course](docs/testing/browser-tests/chrome-add-course.png)
        - [HP Envy Chrome edit course](docs/testing/browser-tests/chrome-edit-course.png)
        - [HP Envy Chrome courses](docs/testing/browser-tests/chrome-courses.png)
        - [HP Envy Chrome full recipe](docs/testing/browser-tests/chrome-full-recipe.png)
        - [HP Envy Chrome full recipe bottom](docs/testing/browser-tests/chrome-full-recipe-bottom.png)

    - Mozilla Firefox (browser): 
        - [HP Envy Mozilla home](docs/testing/browser-tests/mozilla-home.png)
        - [HP Envy Mozilla login](docs/testing/browser-tests/mozilla-login.png)
        - [HP Envy Mozilla register](docs/testing/browser-tests/mozilla-register.png)
        - [HP Envy Mozilla profile](docs/testing/browser-tests/mozilla-profile.png)
        - [HP Envy Mozilla profile bottom](docs/testing/browser-tests/mozilla-profile-bottom.png)
        - [HP Envy Mozilla edit delete option for logged user only](docs/testing/browser-tests/mozilla-options.png)
        - [HP Envy Mozilla add recipe](docs/testing/browser-tests/mozilla-add.png)
        - [HP Envy Mozilla add recipe bottom](docs/testing/browser-tests/mozilla-add-bottom.png)
        - [HP Envy Mozilla edit recipe](docs/testing/browser-tests/mozilla-edit-recipe.png)
        - [HP Envy Mozilla delete recipe](docs/testing/browser-tests/mozilla-delete.png)
        - [HP Envy Mozilla add course](docs/testing/browser-tests/mozilla-add-course.png)
        - [HP Envy Mozilla edit course](docs/testing/browser-tests/mozilla-edit-course.png)
        - [HP Envy Mozilla courses](docs/testing/browser-tests/mozilla-courses.png)
        - [HP Envy Mozilla full recipe](docs/testing/browser-tests/mozilla-full-recipe.png)
        - [HP Envy Mozilla full recipe bottom](docs/testing/browser-tests/mozilla-full-recipe-bottom.png)
   
    - Microsoft Edge (brower)

        - [HP Envy Edge home](docs/testing/browser-tests/edge-home.png)
        - [HP Envy Edge login](docs/testing/browser-tests/edge-login.png)
        - [HP Envy Edge register](docs/testing/browser-tests/edge-register.png)
        - [HP Envy Edge profile](docs/testing/browser-tests/edge-profile.png)
        - [HP Envy Edge profile bottom](docs/testing/browser-tests/edge-profile-bottom.png)
        - [HP Envy Edge edit delete option for logged user only](docs/testing/browser-tests/edge-options.png)
        - [HP Envy Edge add recipe](docs/testing/browser-tests/edge-add.png)
        - [HP Envy Edge add recipe bottom](docs/testing/browser-tests/edge-add-bottom.png)
        - [HP Envy Edge edit recipe](docs/testing/browser-tests/edge-edit.png)
        - [HP Envy Edge delete recipe](docs/testing/browser-tests/edge-delete.png)
        - [HP Envy Edge add course](docs/testing/browser-tests/edge-add-course.png)
        - [HP Envy Edge edit course](docs/testing/browser-tests/edge-edit-course.png)
        - [HP Envy Edge courses](docs/testing/browser-tests/edge-courses.png)
        - [HP Envy Edge full recipe](docs/testing/browser-tests/edge-full-recipe.png)
        - [HP Envy Edge full recipe bottom](docs/testing/browser-tests/edge-full-recipe-bottom.png)

    - Opera (browser) 

        - [HP Envy Opera home](docs/testing/browser-tests/opera-home.png)
        - [HP Envy Opera login](docs/testing/browser-tests/opera-login.png)
        - [HP Envy Opera register](docs/testing/browser-tests/opera-register.png)
        - [HP Envy Opera profile](docs/testing/browser-tests/opera-profile.png)
        - [HP Envy Opera profile bottom](docs/testing/browser-tests/opera-profile-bottom.png)
        - [HP Envy Opera edit delete option for logged user only](docs/testing/browser-tests/opera-options.png)
        - [HP Envy Opera add recipe](docs/testing/browser-tests/opera-add.png)
        - [HP Envy Opera add recipe bottom](docs/testing/browser-tests/opera-add-bottom.png)
        - [HP Envy Opera edit recipe](docs/testing/browser-tests/opera-edit.png)
        - [HP Envy Opera delete recipe](docs/testing/browser-tests/opera-delete.png)
        - [HP Envy Opera add course](docs/testing/browser-tests/opera-add-course.png)
        - [HP Envy Opera edit course](docs/testing/browser-tests/opera-edit-course.png)
        - [HP Envy Opera courses](docs/testing/browser-tests/opera-courses.png)
        - [HP Envy Opera full recipe](docs/testing/browser-tests/opera-full-recipe.png)
        - [HP Envy Opera full recipe bottom](docs/testing/browser-tests/opera-full-recipe-bottom.png)

        
- PC HP desktop 31.5" screen

    - Google Chrome (browser)

        - [HP Desktop home](docs/testing/browser-tests/desktop-home.png)
        - [HP Desktop login](docs/testing/browser-tests/desktop-login.png)
        - [HP Desktop register](docs/testing/browser-tests/desktop-register.png)
        - [HP Desktop profile](docs/testing/browser-tests/desktop-profile.png)
        - [HP Desktop edit delete option for logged user only](docs/testing/browser-tests/desktop-options.png)
        - [HP Desktop add recipe](docs/testing/browser-tests/desktop-add.png)
        - [HP Desktop add recipe bottom](docs/testing/browser-tests/desktop-add-bottom.png)
        - [HP Desktop edit recipe](docs/testing/browser-tests/desktop-edit.png)
        - [HP Desktop delete recipe](docs/testing/browser-tests/desktop-delete.png)
        - [HP Desktop add course](docs/testing/browser-tests/desktop-add-course.png)
        - [HP Desktop edit course](docs/testing/browser-tests/desktop-edit-course.png)
        - [HP Desktop courses](docs/testing/browser-tests/desktop-courses.png)
        - [HP Desktop full recipe](docs/testing/browser-tests/desktop-full-recipe.png)
        - [HP Desktop full recipe bottom](docs/testing/browser-tests/desktop-full-recipe-bottom.png)




---

## FURTHER TESTING

- All features have been thoroughtly tested by myself on different screen sizes/operating systems, including all internal links and buttons, hover effects, wrong inputs and errors, different users, closing modals , etc.

- The live project has been tested by family and friends, acting as anonymous and registered users, on their own devices of different makes and sizes to make sure everything was working as designed. They checked all features mentioned above. They adviced on the need of an edit button inside the modal to have easy access to this feature. This tests can be seen as inputs from my family are on a different language.

## Bugs

Listed below are the biggest bugs that I encountered whilst building this project and what I did to fix them. Ass I used Dev Tool while developing this application, little errors like colors or font sizes where corrected immediately.

- Favicon did not show after loading and hard loading :
	- This happened because i forgot to use url_for when using internal links with jinja templates
	- used [flask documentation:](https://flask.palletsprojects.com/en/2.0.x/patterns/favicon/) to solve the issue

- When testing on smallest sizes (galaxy fold on Chrome Dev Tools) I noticed that the message box was too short for the message, and it showed in multiple lines, showing only one word per line. To fix this, I changed the column size on the base.html from s6 to s10. This fixed the issue.

- Similar to the issue before, the welcome card on the profile, the h4 font size was too large, so I added it to a media query for small screen sizes. This fixed the issue

- When testing the delete button, I noticed only the first item of the list was been removed instead of the one I was selecting. I checked the id, but the issue was that I used the same modal twice, without changing the id on the modal. So the iteration was only counting the first delete, and not targetting the ObjectId. 
    - To fix this I added {{ loop.index }} in all sections where the modal was present. This fixed the issue.

- When adding the full_recipe(), the page was rendering with no information on the fields. 
    - I noticed I missed the underscore to the id ({_id: 'ObjectId'}) on the dictionary.
    - Fixing this error fixed the issue.

- When adding the background to the body, this would only show over the rest of the elements. 
    - To fix this i used  body::before. 
    - I did not use this at the end and instead I used a background and styling provided by [Hero Patterns](https://www.heropatterns.com/)


## KNOWN BUGS

- The footer moves up in very large viewports. Although I tried to fix this by setting a fixed footer, It keeps moving up if there is a gap between the content and the footer. This is not a big issue as the users of this website they will want to cook along their devices and most of them they'll be either small or medium screen sizes.

- In the admin's profile, in the extra large screens, the admin only card (add courses) moves to the right side, making the card above change sizes. Although I tried to fix this by adding col l4 to all cards, this shows the rest of the users to see the cards offset. 
    - As this site is intended to be seen in small and medium devices, this bug will be attented to be fixed in future releases.

---

## <center> Back to [README.md](README.md)

---