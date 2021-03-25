# MS 3 Project

Purpose of Project
======

Create a website that lists U2's best songs, allows fans to rate the songs and add new songs to the list.

User Stories
======

As **a user**, I want to **view the most popular U2 songs** and **rate them with a score**.

As **a user**, I want to **propose new songs to add to the list**.

As **a user**, I want to **review the proposals of other users** and **vote in favour or against them**.


Features
====== 

#### Home Page:

The home page will contain a header, footer, an image of U2 and an explanation of the site.

The image that appears will be one of a number that is saved on the database and selected randomly.


#### Best Songs Page:

This page will contain a header and footer and a card for each song.

Initally it will include every song from U2's two best of albums.

The card for each song will display an image, some summary information about the song, the average rating that users have given the song and the rating (if any) that the logged in user has given the song.


#### Potential Best Songs:

This page will contain a header and footer, a paragraph with instructions, a button to propose a new song and a card for each song that has already been proposed by users.

Each card will contain an image, some summary information and a option for users to vote in favour or against adding the song to the list of best songs.

When the number of votes in favour of a song is greater than the number of votes against the song by ten votes, that song will be removed from this page and will be found in the best songs page.

#### Potential Best Songs:

This page will contain a header and footer, a form for new songs to propose and a button to submit the form.

It will display an error if the song has already been submitted.

If the song is successfully added, it will then be displayed in the potential best songs page and the user will be redirected.

#### Sign Up Page:

This page will contain a header and footer and a form to provide email address and password.

It will also provide a link to the log in page for users that have already registered.

It will check that the email is valid and that the password has a certain length.

If these conditions are not met, it will display an error.

Otherwise it will create a new user, log them in and redirect to the best songs page.


#### Log In Page:

This page will contain a header and footer and a form to provide email address and password.

It will also provide a link to the sign up page for users that have not yet registered.

It will check that the password is the correct password for that user.

If it is not, it will display an error.

Otherwise it will log the user in and redirect to the best songs page.


#### Header:

In the header, I will include a nav bar that has links to the home page, best songs page, potential best songs page, log in or sign up page, search option and a sort option. This will be on every page.

#### Footer:

In the footer, I will include links to the U2 page on social media platforms. These will open in a new window. This will be on every page.


#### Product Limitations:



#### Future Features:




Typography and Color Scheme:
======




Skeleton:
======

Wireframes are available [here](/docs/wireframes.pdf)



Technology:
======

HTML5
CSS3
Gitpod


Best Practices:
======



Testing:
======



#### Test cases:





#### Fixed Issues:



#### Open Issues:



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






