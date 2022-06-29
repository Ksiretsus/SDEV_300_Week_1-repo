"""This is the main app for URL routing and page rendering."""

from datetime import datetime

from flask import Flask, render_template

from . import app


@app.route("/")
def home():
    """This fuction serves the home page.

    it calls renter_template on home.html"""
    return render_template(
        "home.html",
        #this line sends the current date and
        #time to the calling page
        date=datetime.now()
        )

@app.route("/screenshots/")
def screenshots():
    """This function serves the screenshots page.

    it calls renter_template on screenshots.html"""
    return render_template(
        "screenshots.html",
        date=datetime.now()
        )

@app.route("/links/")
def links():
    """this function serves the links page.

    it calls renter_template on links.html"""
    return render_template(
        "links.html",
        date=datetime.now()
        )
