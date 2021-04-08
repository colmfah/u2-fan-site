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


def float_trunc(num):
    if round(num, 1) > int(num):
        return round(num, 1)
    return int(num)


def get_best_songs(song):
    reviews = list(mongo.db.reviews.find({"song": ObjectId(song["_id"])}))
    if song["onBestOfAlbum"] and len(reviews) < 10:
        return True
    elif len(reviews) >= 10:
        ratings = map(lambda x: x["rating"], reviews)
        average_rating = statistics.mean(ratings)
        if average_rating >= 3:
            return True
        else:
            return False


def get_contender_songs(song):
    reviews = list(mongo.db.reviews.find({"song": ObjectId(song["_id"])}))
    if song["onBestOfAlbum"] and len(reviews) < 10:
        return False
    elif len(reviews) >= 10:
        ratings = map(lambda x: x["rating"], reviews)
        average_rating = statistics.mean(ratings)
        if average_rating >= 3:
            return False
        else:
            return True
    else:
        return True


def calculate_ratings(song):
    reviews = list(mongo.db.reviews.find({"song": ObjectId(song["_id"])}))
    if len(reviews) == 0:
        song["rating"] = 0
    else:
        ratings = map(lambda x: x["rating"], reviews)
        average_rating = statistics.mean(ratings)
        song["rating"] = float_trunc(average_rating)
    return song


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
    return render_template("get_reviews.html",
                           song=song, reviews=reviews, user_review_exists=user_review_exists, user_review=user_review, user_logged_in=user_logged_in)


@ app.route("/")
@ app.route("/home")
def home():
    return render_template("home.html")


@ app.route("/get_songs")
def get_songs():
    all_songs = list(mongo.db.songs.find())
    best_songs = filter(get_best_songs, all_songs)
    best_songs_with_ratings = list(map(calculate_ratings, best_songs))
    best_songs_with_ratings.sort(reverse=True,
                                 key=lambda song: song["rating"])
    return render_template("songs.html", songs=best_songs_with_ratings)


@ app.route("/get_contenders")
def get_contenders():
    all_songs = list(mongo.db.songs.find())
    contenders = filter(get_contender_songs, all_songs)
    contenders_with_ratings = map(calculate_ratings, contenders)

    return render_template("contenders.html", songs=contenders_with_ratings)


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
        return redirect(url_for("home"))

    return render_template("register.html")


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
                    "home"))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@ app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@ app.route("/add_song", methods=["GET", "POST"])
def add_song():
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

    return render_template("get_reviews.html",
                           song=song, reviews=reviews, user_review_exists=user_review_exists, user_review=user_review, user_logged_in=user_logged_in)


@ app.route("/edit_review/<song_id>", methods=["GET", "POST"])
def edit_review(song_id):
    if request.method == "POST":

        user_rating = round(float(request.form.get("rating")), 1)

        review = {
            "user": session["user"],
            "rating": user_rating,
            "review": request.form.get("review"),
            "song": ObjectId(song_id)
        }

        reviews = list(mongo.db.reviews.find({"song": ObjectId(song_id)}))
        ratings = list(map(lambda x: x["rating"], reviews))
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

        else:
            users_who_reviewed = list(
                map(lambda review: review["user"], reviews))
            userID = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
            user_review_exists = userID in users_who_reviewed

            if user_review_exists:
                relevant_review = list(
                    filter(lambda review: review["user"] == session["user"], reviews))
                reviewID = relevant_review[0]["_id"]
                mongo.db.reviews.update({"_id": ObjectId(reviewID)}, review)
            else:
                mongo.db.reviews.insert_one(review)

            # mongo.db.reviews.insert_one(review)
            flash("Review Saved")

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

            return render_template("get_reviews.html",
                                   song=song, reviews=reviews, user_review_exists=user_review_exists, user_review=user_review, user_logged_in=user_logged_in)


@ app.route("/delete_review/<user_review_id>")
def delete_review(user_review_id):
    mongo.db.reviews.remove({"_id": ObjectId(user_review_id)})
    flash("Review Deleted")
    return redirect(url_for("get_songs"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
