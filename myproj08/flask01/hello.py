# 항상 현재 디렉토리 확인
from flask import render_template

from flask import Flask

app = Flask(__name__)

## 함수는 아무 역할안한다 생각할 수 있지만,
# 그래도 중복되지 않고 의미있게 작성해야함~
@app.route("/")
def index():
    return render_template("index.html")


# 별도 이름을 가진 것이 도메인주소 -> 쓰려면 사야함 (연단위)


@app.route("/profile")
def profile():  # 우리가 호출하는 것이 아니라 flask가 자동으로 호출해주는 것.
    # 이게 리턴될때까지 사용자에게는 로딩중...
    # DB Access
    like_foods = [
        "등촌칼국수",
        "양념갈비",
        "참치주먹밥",
        "스테이크",
        "짜장면",
    ]
    return render_template("profile.html", like_foods=like_foods)
    # 뒤에가 변수명, 앞에는 템플릿에서 참조할 이름


@app.route("/posts")  # 함수명이 아니라 이 "사이의 " 주소가 중요
def post_list():
    return render_template("post_list.html")
