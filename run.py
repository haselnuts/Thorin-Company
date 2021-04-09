import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env
# 2 line space betwenn function needed ALWAYS, this is called PEP8 compliant
# request needed for forms
# flash needed for feedback to user, to provide a "flashed message"
# need to create a secret key, because Flask cryptographically signs..
# ..all messages for security purposes
# need to create a .gitignore file, any file or folder will be..
# ..igrnored by GitHub so we do not accidently commit files with..
# ..sensitive information
# also, we need to create a new py file called env.py, here we hide..
# ..any sensitive information
# if statement os.path.exists...  will only import env.py file if..
# ..it exists -> new directory __pycache__ will be created after saving file
app = Flask(__name__)
# instance of the class Flask
# flask needs this to look for templates and static files
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
# tells Flask which URL should be trigger the function
# when we try to browse root directory ("/"), Flask triggers
# index function
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
# clicking on a link tag to bring us to a page that
# displays more information
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
    # in the return statment
    # first member = member.html
    # second member = member{}


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    # "__main__" name of default module in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
        # debug = True only for developement, needs to be changed
        # before submition of the project
    )
# IP and PORT needed for Deployment at Heroku or other supporters
