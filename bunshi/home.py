from flask import flash, render_template, session, request
from bunshi import app
from bunshi.image import getImage

session["recent"] = []
recentMax = 5

@app.route("/", methods = ["POST", "GET"])
def home():
    # flash(session["recent"])
    if request.method == "POST":
        session["compound"] = request.form["compound"].lower()

        try:
            error = False
            links = getImage(session["compound"])
            imageSource = links[0]
            pageURL = links[1]

            if session["compound"] in session["recent"]:
                session["recent"].remove(session["compound"])
            session["recent"].insert(0, session["compound"])

            if len(session["recent"]) > recentMax:
                session["recent"].pop(-1)

        except TypeError as e:
            error = True
            imageSource = ""
            pageURL = ""

        return render_template("home.html",
                               imageSource = imageSource,
                               compound = session["compound"],
                               pageURL = pageURL,
                               error = error,
                               recent = session["recent"])

    return render_template("home.html",
                           recent = session["recent"])
