import os
import statistics
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


"""Create function to round numbers if they are not whole numbers
    Args:
        num:  a number
    Returns:
        number
"""


def float_trunc(num):
    if round(num, 1) > int(num):
        return round(num, 1)
    return int(num)


"""Create function to determine whether a song is a "best song"
    Args:
        song:  song dictionary from database
    Returns:
        Boolean
"""


def get_best_songs(song):
    reviews = list(mongo.db.reviews.find({"song": ObjectId(song["_id"])}))
    if song["onBestOfAlbum"] and len(reviews) < 10:
        return True
    elif len(reviews) >= 10:
        ratings = map(lambda x: x["rating"], reviews)
        average_rating = statistics.mean(ratings)
        if average_rating >= 4:
            return True
        else:
            return False


"""Create function to determine whether a song is a "contender song"
    Args:
        song:  song dictionary from database
    Returns:
        Boolean
"""


def get_contender_songs(song):
    reviews = list(mongo.db.reviews.find({"song": ObjectId(song["_id"])}))
    if song["onBestOfAlbum"] and len(reviews) < 10:
        return False
    elif len(reviews) >= 10:
        ratings = map(lambda x: x["rating"], reviews)
        average_rating = statistics.mean(ratings)
        if average_rating >= 4:
            return False
        else:
            return True
    else:
        return True


"""Create function to calculate a song's ratings
    Args:
        song:  song dictionary from database
    Returns:
        the song dictionary with rating included
"""


def calculate_ratings(song):
    reviews = list(mongo.db.reviews.find({"song": ObjectId(song["_id"])}))
    if len(reviews) == 0:
        song["rating"] = 0
    else:
        ratings = map(lambda x: x["rating"], reviews)
        average_rating = statistics.mean(ratings)
        song["rating"] = float_trunc(average_rating)
    return song


"""Create app route to get the home page
    Returns:
        Renders the index template
"""


@ app.route("/")
@ app.route("/index")
def index():
    return render_template("index.html")


"""Create app route to get the best songs
    Returns:
        Renders the songs template
"""


@ app.route("/get_songs")
def get_songs():
    all_songs = list(mongo.db.songs.find())
    best_songs = filter(get_best_songs, all_songs)
    best_songs_with_ratings = list(map(calculate_ratings, best_songs))
    best_songs_with_ratings.sort(reverse=True,
                                 key=lambda song: song["rating"])
    return render_template("songs.html", songs=best_songs_with_ratings)


"""Create app route to get the contender songs
    Returns:
        Renders the contender template
"""


@ app.route("/get_contenders")
def get_contenders():
    all_songs = list(mongo.db.songs.find())
    contenders = filter(get_contender_songs, all_songs)
    contenders_with_ratings = map(calculate_ratings, contenders)

    return render_template("contenders.html", songs=contenders_with_ratings)


"""Create app route to register new user
    Returns:
        Get method renders render_template
        Post method renders index template
"""


@ app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("index"))

    return render_template("register.html")


"""Create app route to log a user in
    Returns:
        Renders the get_reviews template
"""


@ app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "index"))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


"""Create app route to log a user out
    Returns:
        Renders the login template
"""


@ app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


"""Create app route to post new song to database
    Returns:
        Renders the add_song template for get request
        Renders the get_contenders template after successful post request
"""


@ app.route("/add_song", methods=["GET", "POST"])
def add_song():

    if "user" not in session:
        return render_template("login.html")
    else:
        if request.method == "POST":
            all_songs = list(mongo.db.songs.find())
            all_song_titles = list(map(lambda song: song["title"], all_songs))
            new_song_title = request.form.get("title")
            if new_song_title in all_song_titles:
                flash("Song Has Already Been Added")
            else:
                song = {
                    "title": new_song_title,
                    "year": request.form.get("year"),
                    "description": request.form.get("description"),
                    "onBestOfAlbum": False,
                    "created_by": session["user"],
                    "upVotes": 0,
                    "downVotes": 0
                }
                mongo.db.songs.insert_one(song)
                flash("Song Successfully Added")
                return redirect(url_for("get_contenders"))

        return render_template("add_song.html")


"""Create app route to get reviews associated with a song
    Args:
        song_id:  id of the song
    Returns:
        Renders the get_reviews template
"""


@ app.route("/get_reviews/<song_id>", methods=["GET", "POST"])
def get_reviews(song_id):

    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    reviews = list(mongo.db.reviews.find({"song": ObjectId(song_id)}))
    users_who_reviewed = list(
        map(lambda review: review["user"], reviews))
    user_review = False
    user_review_exists = False
    user_logged_in = False

    if "user" in session:
        user_logged_in = True
        userID = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        user_review_exists = userID in users_who_reviewed

    if user_review_exists:
        user_review = reviews[users_who_reviewed.index(
            session["user"])]

    if "user" in session and request.method == "POST":

        user_rating = round(float(request.form.get("rating")), 1)

        review = {
            "user": session["user"],
            "rating": user_rating,
            "review": request.form.get("review"),
            "song": ObjectId(song_id)
        }

        ratings = list(map(lambda x: x["rating"], reviews))
        if user_review_exists:
            # replace existing review with new one
            index = 'a'
            for user_review in reviews:
                if user_review["user"] == session["user"]:
                    index = reviews.index(user_review)
                    break
            reviews[index] = review
            ratings = list(map(lambda x: x["rating"], reviews))

        else:
            ratings.append(user_rating)

        average_rating = statistics.mean(ratings)

        if average_rating < 3 and len(ratings) >= 10:
            mongo.db.songs.remove({"_id": ObjectId(song_id)})
            flash("Song Deleted Because of Poor Reviews")
            all_songs = list(mongo.db.songs.find())
            best_songs = filter(get_best_songs, all_songs)
            best_songs_with_ratings = list(map(calculate_ratings, best_songs))
            best_songs_with_ratings.sort(reverse=True,
                                         key=lambda song: song["rating"])
            return render_template("songs.html", songs=best_songs_with_ratings)

        elif user_review_exists:
            reviews = list(mongo.db.reviews.find({"song": ObjectId(song_id)}))
            relevant_review = list(
                filter(lambda review: review["user"] == session["user"], reviews))
            print("relevant_review", relevant_review)
            reviewID = relevant_review[0]["_id"]
            mongo.db.reviews.update({"_id": ObjectId(reviewID)}, review)
            flash("Review Saved")
            reviews = list(mongo.db.reviews.find({"song": ObjectId(song_id)}))
            return render_template("get_reviews.html",
                                   song=song, reviews=reviews, user_review_exists=user_review_exists, user_review=review, user_logged_in=user_logged_in)

        else:
            mongo.db.reviews.insert_one(review)
            flash("Review Saved")
            reviews = list(mongo.db.reviews.find({"song": ObjectId(song_id)}))
            return render_template("get_reviews.html",
                                   song=song, reviews=reviews, user_review_exists=True, user_review=review, user_logged_in=user_logged_in)

    else:
        return render_template("get_reviews.html",
                               song=song, reviews=reviews, user_review_exists=user_review_exists, user_review=user_review, user_logged_in=user_logged_in)


"""Create app route to delete user review
    Args:
        user_review_id:  id of the user review
    Returns:
        Renders the login template if user is not logged in
        Displays flash message if this is not the users' review
        Renders the get_songs template if review is successfully deleted
"""


@ app.route("/delete_review/<user_review_id>")
def delete_review(user_review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(user_review_id)})
    if "user" not in session:
        return render_template("login.html")
    elif review["user"] != session["user"]:
        flash("This is not your review!")
    else:
        mongo.db.reviews.remove({"_id": ObjectId(user_review_id)})
        flash("Review Deleted")
        return redirect(url_for("get_songs"))


"""Create app route to handle errors
    Args:
        Exception:  error
    Returns:
        Renders the get_songs template
"""


# @app.errorhandler(Exception)
# def handle_exception(e):
#     # flash("An error occurred: 500")
#     return redirect(url_for("get_songs"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
