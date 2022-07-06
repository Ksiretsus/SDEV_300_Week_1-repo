"""This is the main app for URL routing and page rendering."""

from datetime import datetime

from flask import Flask, render_template, session, url_for, redirect, request, flash

from . import app

from passlib.hash import sha256_crypt
app.secret_key = "hello"
passfile = 'passfile.txt'

@app.route("/")
def welcome():
    """This fuction serves the home page.

    it calls renter_template on home.html"""
    return render_template(
        "welcome.html",
        #this line sends the current date and
        #time to the calling page
        date=datetime.now()
        )

@app.route("/login/", methods=["POST", "GET"])
def login():
    """This function serves the login page.

    it calls renter_template on login.html"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        check = check_creds(passfile, username, password)
        if check is True:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            flash("Username and/or password is incorrect", "warning")
            return render_template(
            "login.html",
            date=datetime.now()
        )

    else:
        if "user" in session:
            return redirect(url_for("home"))
        return render_template(
            "login.html",
            date=datetime.now()
        )

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash("Log out successful.", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/register", methods=["POST", "GET"])
def register():
    """This function serves the register page.

    it calls renter_template on register.html"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        available = check_available(passfile, username)
        match = pw_match(password, password2)
        if available is True:
            if match is True:
                flash("Account created! You can now log in.", "info")
                add_user(passfile, username, password)
            else:
                flash("Passwords don't match", "info")
                return render_template(
                    "register.html",
                    date=datetime.now()
                )
        else:
            flash("Username not available", "info")
            return render_template(
                "register.html",
                date=datetime.now()
            )
    return render_template(
        "register.html",
        date=datetime.now()
        )

@app.route("/home")
def home():
    """This fuction serves the home page.

    it calls renter_template on home.html"""
    if "user" in session:
        return render_template(
            "home.html",
            #this line sends the current date and
            #time to the calling page
            date=datetime.now()
            )
    else:
        flash("You must log in to view this page.", "info")
        return redirect(url_for("login"))

@app.route("/screenshots/")
def screenshots():
    """This function serves the screenshots page.

    it calls renter_template on screenshots.html"""
    if "user" in session:
        return render_template(
            "screenshots.html",
            date=datetime.now()
            )
    else:
        flash("You must log in to view this page.", "info")
        return redirect(url_for("login"))

@app.route("/links/")
def links():
    """this function serves the links page.

    it calls renter_template on links.html"""
    if "user" in session:
        return render_template(
            "links.html",
            date=datetime.now()
            )
    else:
        flash("You must log in to view this page.", "info")
        return redirect(url_for("login"))


def readfile(file):
    """This function reads the password file.

    Function takes the passfile.txt file and reads its contents
    into a dictionary of key value pairs"""

    pass_dict={}
    with open(file) as f:
        for line in f:
            (key, val) = line.split(',')
            pass_dict[key]=val.strip('\n')
        return pass_dict

def check_creds(file, username, password):
    """This function validates a username and password

    Function takes the file passed in as a dictionary then checks
    if the user supplied username is in the file. If it is in the file
    the function then checks the user supplied password against the
    saved hash in the pw file"""

    pass_dict = readfile(file)
    if username in pass_dict:
        test_pass = password
        sav_pass = pass_dict[username]
        return sha256_crypt.verify(test_pass, sav_pass)
    else:
        return None

def check_available(file, username):
    """This function checks username availability

    """
    pass_dict = readfile(file)
    if username not in pass_dict:
        return True

def pw_match(pw, pw2):
    """This function validates register password

    Fuction compares the two user supplied passwords from the 
    register form."""

    if pw == pw2:
        return True

def add_user(file, username, password):
    """This function adds a user

    Function takes a validated new username and password combo
    and adds the username and password hash to the pw file."""

    hash_pass = sha256_crypt.hash(password)
    with open(file, "a") as f:
        f.writelines(f"{username},{hash_pass}\n")