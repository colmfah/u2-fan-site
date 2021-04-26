# MS 3 Project

# Purpose of Project

Create a website that lists U2's best songs, allows fans to rate the songs and add new songs to the list.

# User Stories

As **a visiting user**, I want to **view U2 songs** and **view their average rating**.

As **a visiting user**, I want to **register to use all features on the site**.

As **a registered user**, I want to **log in to the site**.

As **a registered user**, I want to **view U2 songs** and **review them and rate them with a score**.

As **a registered user**, I want to **view U2 songs** and **edit my previous reviews**.

As **a registered user**, I want to **view U2 songs** and **delete my previous reviews**.

As **a registered user**, I want to **propose new songs to include on the site**.


# Features

#### Home Page:

![HomePage](/assets/images/homepage-screenshot.png)
The home page will contain a nav an image of U2 and an explanation of the site.


#### Best Songs Page:

![BestSongs](/assets/images/best-songs-screenshot.png)
This page will contain a nav and an accordion containing the name of each "best song", its year, a "review" button and its average rate. When the user clicks on the review button or rating, it will link to the review for that song. When the user clicks anywhere else, the accordion will expand and more details about the song will be provided.

In order to be listed as a "best song", the song must:

* Have an average rating of at least 4 if it has at least 10 reviews
* If it has less than 10 reviews, it must be a song that was is listed on U2's official best of albums

When a song has at least 10 reviews, and its average rating is less than 2, it will automatically be deleted from the database.


#### Contenders:

![Contenders](/assets/images/contenders.png)

This page will contain a nav and an accordion containing the name of each "contender song", its year, a "review" button and its average rate. When the user clicks on the review button or rating, it will link to the review for that song. When the user clicks anywhere else, the accordion will expand and more details about the song will be provided.

In order to be listed as a "contender song", the song must:

* Have an average rating of between 2 and 3 if it has at least 10 reviews
* If it has less than 10 reviews, it must not be a song that was is listed on U2's official best of albums

When a song has at least 10 reviews, and its average rating is less than 2, it will automatically be deleted from the database.

When a song has at least 10 reviews, and its average rating is at least 3, it will automatically be removed from the contender list and listed on the best songs list

#### Review Page:

![Review](/assets/images/review.png)

This page displays all reviews the song has received and allows logged in users to review the song or edit or delete their previous review.

#### Potential Best Songs:

This page will contain a nav bar, a form for new songs to propose and a button to submit the form.

It will display an error if the song has already been submitted.

If the song is successfully added, it will then be displayed in the contenders page and the user will be redirected.

#### Register Page:

![Register](/assets/images/register.png)

This page will contain a nav bar and a form to provide email address and password.

It will also provide a link to the log in page for users that have already registered.

It will check that the email is valid and that the password has a certain length.

If these conditions are not met, it will display an error.

Otherwise it will create a new user, log them in and redirect to the best songs page.


#### Log In Page:

![Log In](/assets/images/login.png)

This page will contain a nav bar and a form to provide email address and password.

It will also provide a link to the sign up page for users that have not yet registered.

It will check that the password is the correct password for that user.

If it is not, it will display an error.

Otherwise it will log the user in and redirect to the best songs page.


#### Nav Bar:

I will include a nav bar that has links to the home page, best songs page, potential best songs page, log in or sign up page. This will be on every page.


# Typography and Color Scheme:

Red: #fe0000

Black: rgba(0,0,0,0.87)

Fonts: Nunito Google Fonts


# Skeleton:


Wireframes are available [here](/docs/wireframes.pdf)


# Technology:

*   HTML5
*   CSS3
*   Gitpod
*   Flask
*   Jinja
*   Heroku

My requirements.txt file contains the following:

*   click==7.1.2
*   dnspython==2.1.0
*   Flask==1.1.2
*   Flask-PyMongo==2.3.0
*   itsdangerous==1.1.0
*   pymongo==3.11.3
*   Werkzeug==1.0.1


# Testing:

Validated CSS using https://jigsaw.w3.org/css-validator.

Validated HTML using https://validator.w3.org/.

Validated Python using Pylint

Validated javascript using https://jshint.com/

Tested website on chrome, firefox and safari on a desktop mac and tested on chrome and firefox on an andriod mobile.

Used google chrome simulator to test for responsiveness for:
*   moto g4 
*   galaxy s5
*   pixel 2
*   pixel 2xl
*   iphone5/se
*   iphone 6/7/8
*   iphone 6/7/8 plus
*   iphone x
*   ipad
*   ipad pro
*   surface duo
*   galaxy fold and desktop.


# Test cases:

As **a visiting user**, I want to **view the most popular U2 songs** and **view their average rating**.

When logged out, I visit the website. 
When I click the "best songs" page and the "contenders" page, I can view a list of U2 songs and see their average ratings to one decimal place.

As **a visiting user**, I want to **register to use all features on the site**.

When logged out, I visit the website. 
When I click "register", I am brought to the registration page. 
If I enter a username that already exists in the database it displays an error.
If I enter a username or password that is not between 5 and 15 characters and only contains letters and numbers, it displays an error.
If all these conditions are fulfilled, it creates a new account.

As **a registered user**, I want to **log in to the site to be able to access all features**.

When logged out, I visit the website. 
When I click "log in", I am brought to the log-in page. 
If I don't enter one of the fields, an error displays.
If I enter a username or password that does not match those stored in the database, an error displays.


As **a registered user**, I want to **view U2 songs** and **review them and rate them with a score**.

When logged into the website I click on "best songs" or "contenders" and I am brought to those pages.
I click "review" on the song that I wish to review.
I am brought to the review page.
If I do not enter a rating or a sufficiently long review, an error message is displayed.
When I enter a rating and a sufficiently long review, a flash message displays to tell me that my review has been saved.
I can see my review on screen and I have the option to edit or delete it.

As **a registered user**, I want to **view U2 songs** and **edit my previous reviews**.

When logged into the website I click on "best songs" or "contenders" and I am brought to those pages.
I click "review" on a song that I have already reviewed.
I am brought to the review page for that song.
I can change the rating and/or the review.
When I click "update review", a flash message displays to tell me that my review has been saved.
I can see my review on screen and I have the option to edit it again or delete it.

As **a registered user**, I want to **view U2 songs** and **delete my previous reviews**.

When logged into the website I click on "best songs" or "contenders" and I am brought to those pages.
I click "review" on a song that I have already reviewed.
I am brought to the review page for that song.
When I click "delete review", a flash message displays to tell me that my review has been deleted.
I am redirected to the best songs.

As **a registered user**, I want to **propose new songs to include on the site**.

When logged into the website I click "propose new songs" and I am brought to that page.
I submit the song name, the song year and the song description and I click submit.
If my input meets the requirements, it is saved in the database and a flash message is displayed.
Otherwise an error message is displayed.

#### Test to ensure users that are not logged in cannot access features exclusive to logged in user

I logged into my account. I clicked on the reviews section of a song. I copied the url. I pasted it into chrome incognito mode. I could did not have the option to edit or delete the review in chrome incognito mode.

In chrome I naviated to 'propose songs' page. I copied the url. I pasted it into chrome incognito mode. I could not propose new songs. It redirected me to the login page


#### Test to ensure 404 errors redirect to best songs page

I changed the end of the url to /sdkfslkdfjslj

It redirected me to the best songs page.

#### Test that songs move from "contenders" page to "best songs" page when they have at least 10 reviews and an average rating of at least 4

I posted a new song to the database.

I manually added 10 reviews of that song to the database with a rating of 4 (because one user can only add one review).

The song no longer appeared on the "contenders" page and now appeared on the "best songs" page

#### Test that songs are deleted from the database when they have at least 10 reviews and an average rating of 2 or less

I manually added 9 reviews to a song in database with a rating of 2 (because one user can only add one review).

I logged in and posted another review with a rating of 2.

The song was deleted from the database.

A flash image told me the song was deleted and I was redirected to the best songs page.


## Outstanding issues

### Pylint errors

app.py:13:4: W0611: Unused import env (unused-import)

### Bug: Border around body to keep footer in place

If there isn't a border around the body, the footer appears in the wrong place on some pages.
As a result a small white line is visible around the page


# Version control:

This project was developed using Gitpod, committed to git and pushed to GitHub using the built in function within Gidpod.

# Deployment:

All of the files necessary to run this website have been stored in a GitHub repository. If you would like to work on your own version of this site or use it as a template for your own work, you have the option to either fork, or make a clone of the original repo.

### Forking the GitHub Repository
By forking the GitHub Repository you can make a copy of the original repository on your GitHub account, which enables you to view and/or make your own changes without affecting the original repository. This can be achieved using the following steps...

*   Log in to GitHub and locate the GitHub Repository
*   At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
*   You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone
*   Log in to GitHub and locate the GitHub Repository
*   Under the repository name, click "Clone or download".
*   To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
*   Open Git Bash
*   Change the current working directory to the location where you want the cloned directory to be made.
*   Type "git clone", and then paste the URL you copied in Step 3.
*   It is important that you create an env.py file to save your Environment Variables such as:
*   IP - (0.0.0.0 Used, but not recommended for production apps)
*   PORT - (5000 used)
*   MONGODB URI - The URI for your MongoDB Database
*   MONGODB PASSWORD - The password for your MongoDB Database The web app will not function without these variables.

### Heroku app creation
As this is a full-stack website it has been deployed to Heroku.com using the following procedure:

1. Log in to Heroku.com
2. From the Dashboard, select the "New" button on the Top-Right of the screen
3. Select "Create new app"
4. Insert your app name
5. Heroku will let you know whether your chosen name is available
6. Select the most appropriate region for your location
7. Click the "Create app" button

### Heroku Deployment
The above steps will automatically bring you to the "Deploy" tab of your new app.

*   In the "Deployment Method" section select Github
*   Once selected a Connect to GitHub section will display below
*   Ensure your profile is displayed
*   If not type in your GitHub username

#### Heroku + Github Repo
*   Search for, and select the Repo corresponding to the Heroku app
*   Click "Connect"

#### Set the Config Vars within Heroku

*   Under the "Settings" tab, in the Config Vars section select the "Reveal Config Vars" button.
*   This will reveal a form for inputting the key and value pairs necessary to connect to the app.
*   Enter the values stored in your .env file for IP, PORT, SECRET KEY, MONGO_URI, and MONGO_DBNAME


#### Enabling Automatic Deployment

*   Select the Heroku "Deploy" tab
*   In the "Automatic deploys" section select the branch you wish to use
*   There is no difference between the developed version of W3Recipes and that deployed on Heroku

# Credits:

Add space in html: https://www.wikihow.com/Insert-Spaces-in-HTML

Get length of list in jinja: https://stackoverflow.com/questions/1465249/get-lengths-of-a-list-in-a-jinja2-template

Get average value: https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list

Check if key exists in dictionary: https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary

Star rating: https://codepen.io/jamesbarnett/pen/vlpkh

Check/uncheck box with javascript: https://stackoverflow.com/questions/8206565/check-uncheck-checkbox-with-javascript

Remove white space below an image: https://stackoverflow.com/questions/7774814/remove-white-space-below-image

Pick a color from an image: https://www.ginifab.com/feeds/pms/color_picker_from_image.php

Change default hmtl 5 error message: http://stackoverflow.com/questions/10361460/how-can-i-change-or-remove-html5-form-validation-default-error-messages

Positioning footer: https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/

Displaying images: https://flask.palletsprojects.com/en/1.1.x/tutorial/static/

Code Institute Task Mini Project

Mongo commands

https://www.w3schools.com/python/python_mongodb_update.asp
https://docs.mongodb.com/manual/reference/operator/update/unset/
https://stackoverflow.com/questions/22901788/remove-attribute-from-all-mongodb-documents-using-python-and-pymongo

U2 song details: 

https://en.wikipedia.org/wiki/With_or_Without_You
https://en.wikipedia.org/wiki/Pride_(In_the_Name_of_Love)
https://en.wikipedia.org/wiki/New_Year%27s_Day_(U2_song)

# Acknowledgements: 

My Code Institute Mentor, Rohit






