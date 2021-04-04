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


def get_best_songs(song):
    if song["onBestOfAlbum"]:
        return True
    # elif len(song["upVotes"]) - len(song["downVotes"]) >= 10:
    #     return True
    else:
        return False


def get_contender_songs(song):
    if song["onBestOfAlbum"]:
        return False
    # elif len(song["upVotes"]) - len(song["downVotes"]) < 10:
    #     return True
    else:
        return True


def calculate_ratings(song):
    if len(song["reviews"]) == 0:
        song["rating"] = 0
    else:
        reviews = song["reviews"]
        ratings = map(lambda x: x["rating"], reviews)
        average_rating = statistics.mean(ratings)
        song["rating"] = round(average_rating, 1)
    return song


def get_reviews(song_id):

    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    users_who_reviewed = list(
        map(lambda review: review["user"], song["reviews"]))
    user_review = False
    user_review_exists = False
    user_logged_in = False
    if "user" in session:
        user_logged_in = True
        user_review_exists = session["user"] in users_who_reviewed

    if user_review_exists:
        user_review = song["reviews"][users_who_reviewed.index(
            session["user"])]

    return render_template("get_reviews.html",
                           song=song, user_review_exists=user_review_exists, user_review=user_review, user_logged_in=user_logged_in)


@ app.route("/")
@ app.route("/get_songs")
def get_songs():
    all_songs = list(mongo.db.songs.find())
    best_songs = filter(get_best_songs, all_songs)
    best_songs_with_ratings = map(calculate_ratings, best_songs)

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
        return redirect(url_for("profile", username=session["user"]))

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
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@ app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@ app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@ app.route("/add_song", methods=["GET", "POST"])
def add_song():
    if request.method == "POST":
        song = {
            "title": request.form.get("title"),
            "year": request.form.get("year"),
            "description": request.form.get("description"),
            "onBestOfAlbum": False,
            "created_by": session["user"],
            "upVotes": 0,
            "downVotes": 0
        }
        mongo.db.songs.insert_one(song)
        flash("Song Successfully Added")
        return redirect(url_for("get_songs"))

    return render_template("add_song.html")


@ app.route("/get_reviews/<song_id>", methods=["GET", "POST"])
def get_reviews(song_id):

    song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    users_who_reviewed = list(
        map(lambda review: review["user"], song["reviews"]))
    user_review = False
    user_review_exists = False
    user_logged_in = False
    if "user" in session:
        user_logged_in = True
        user_review_exists = session["user"] in users_who_reviewed

    if user_review_exists:
        user_review = song["reviews"][users_who_reviewed.index(
            session["user"])]

    return render_template("get_reviews.html",
                           song=song, user_review_exists=user_review_exists, user_review=user_review, user_logged_in=user_logged_in)


@ app.route("/edit_song/<song_id>", methods=["GET", "POST"])
def edit_song(song_id):
    if request.method == "POST":
        song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})

        print("song reviews", song["reviews"])

        review = {
            "user": session["user"],
            "rating": int(request.form.get("rating")),
            "review": request.form.get("review")
        }

        # print("review", review)

        song["reviews"].append(review)

        mongo.db.songs.update({"_id": ObjectId(song_id)}, song)
        flash("Review Saved")
        song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
        users_who_reviewed = list(
            map(lambda review: review["user"], song["reviews"]))
        user_review = False
        user_review_exists = False
        user_logged_in = False
        if "user" in session:
            user_logged_in = True
            user_review_exists = session["user"] in users_who_reviewed

        if user_review_exists:
            user_review = song["reviews"][users_who_reviewed.index(
                session["user"])]

        return render_template("get_reviews.html",
                               song=song, user_review_exists=user_review_exists, user_review=user_review, user_logged_in=user_logged_in)

    # def edit_song(song_id):
    # if request.method == "POST":


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
