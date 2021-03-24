import os
import json
from flask import Flask, render_template
# 2 line space betwenn function needed ALWAYS, this is called PEP8 compliant

app = Flask(__name__)
# instance of the class Flask
# flask needs this to look for templates and static files


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


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


@app.route("/contact")
def contact():
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
