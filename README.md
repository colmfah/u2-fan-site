# MS 3 Project

Purpose of Project
======

Create a website that lists U2's best songs, allows fans to rate the songs and add new songs to the list.

User Stories
======

As **a visiting user**, I want to **view U2 songs** and **view their average rating**.

As **a visiting user**, I want to **register to use all features on the site**.

As **a registered user**, I want to **log in to the site to be able to access all features**.

As **a registered user**, I want to **view U2 songs** and **review them and rate them with a score**.

As **a registered user**, I want to **view U2 songs** and **edit my previous reviews**.

As **a registered user**, I want to **view U2 songs** and **delete my previous reviews**.

As **a registered user**, I want to **propose new songs to include on the site**.



Features
====== 

#### Home Page:

The home page will contain a nav an image of U2 and an explanation of the site.


#### Best Songs Page:

This page will contain a nav and an accordion containing the name of each "best song", its year, a "review" button and its average rate. When the user clicks on the review button or rating, it will link to the review for that song. When the user clicks anywhere else, the accordion will expand and more details about the song will be provided.

In order to be listed as a "best song", the song must:

* Have an average rating of at least 3 if it has at least 10 reviews
* If it has less than 10 reviews, it must be a song that was is listed on U2's official best of albums

When a song has at least 10 reviews, and its average rating is less than 2, it will automatically be deleted from the database.


#### Contenders:

This page will contain a nav and an accordion containing the name of each "contender song", its year, a "review" button and its average rate. When the user clicks on the review button or rating, it will link to the review for that song. When the user clicks anywhere else, the accordion will expand and more details about the song will be provided.

In order to be listed as a "contender song", the song must:

* Have an average rating of between 2 and 3 if it has at least 10 reviews
* If it has less than 10 reviews, it must not be a song that was is listed on U2's official best of albums

When a song has at least 10 reviews, and its average rating is less than 2, it will automatically be deleted from the database.

When a song has at least 10 reviews, and its average rating is at least 3, it will automatically be removed from the contender list and listed on the best songs list

#### Review Page:

This page displays all reviews the song has received and allows logged in users to review the song or edit or delete their previous review.

#### Potential Best Songs:

This page will contain a nav bar, a form for new songs to propose and a button to submit the form.

It will display an error if the song has already been submitted.

If the song is successfully added, it will then be displayed in the contenders page and the user will be redirected.

#### Sign Up Page:

This page will contain a nav bar and a form to provide email address and password.

It will also provide a link to the log in page for users that have already registered.

It will check that the email is valid and that the password has a certain length.

If these conditions are not met, it will display an error.

Otherwise it will create a new user, log them in and redirect to the best songs page.


#### Log In Page:

This page will contain a nav bar and a form to provide email address and password.

It will also provide a link to the sign up page for users that have not yet registered.

It will check that the password is the correct password for that user.

If it is not, it will display an error.

Otherwise it will log the user in and redirect to the best songs page.


#### Nav Bar:

I will include a nav bar that has links to the home page, best songs page, potential best songs page, log in or sign up page. This will be on every page.



Typography and Color Scheme:
======

Red: #fe0000

Black: rgba(0,0,0,0.87)

Fonts: Nunito Google Fonts



Skeleton:
======

Wireframes are available [here](/docs/wireframes.pdf)



Technology:
======

HTML5
CSS3
Gitpod
Flask
Jinja


Testing:
======

Validated CSS using https://jigsaw.w3.org/css-validator.

Validated HTML using https://validator.w3.org/.





#### Test cases:

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











Version control:
======

This project was developed using Gitpod, committed to git and pushed to GitHub using the built in function within Gidpod.

Deployment:
======



Credits:
======

add space in html: https://www.wikihow.com/Insert-Spaces-in-HTML

length of list in jinja:
https://stackoverflow.com/questions/1465249/get-lengths-of-a-list-in-a-jinja2-template


Get average: https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list

Check if key exists in dictionary: https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary

Star rating: https://codepen.io/jamesbarnett/pen/vlpkh

https://stackoverflow.com/questions/8206565/check-uncheck-checkbox-with-javascript

https://stackoverflow.com/questions/7774814/remove-white-space-below-image

https://www.ginifab.com/feeds/pms/color_picker_from_image.php

http://stackoverflow.com/questions/10361460/how-can-i-change-or-remove-html5-form-validation-default-error-messages



Mongo commands

https://www.w3schools.com/python/python_mongodb_update.asp
https://docs.mongodb.com/manual/reference/operator/update/unset/
https://stackoverflow.com/questions/22901788/remove-attribute-from-all-mongodb-documents-using-python-and-pymongo




U2 song details: 

https://en.wikipedia.org/wiki/With_or_Without_You
https://en.wikipedia.org/wiki/Pride_(In_the_Name_of_Love)
https://en.wikipedia.org/wiki/New_Year%27s_Day_(U2_song)




Acknowledgements: 
======
My Code Institute Mentor, Rohit






