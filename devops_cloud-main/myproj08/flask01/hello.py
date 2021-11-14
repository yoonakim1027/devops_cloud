# pip install flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    # DB Access
    like_foods = [
        "두부 두루치기",
        "김치찌개",
        "칼국수",
        "쌀국수",
        "자장면",
    ]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
