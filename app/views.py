from flask import render_template, request, flash, session, redirect
from .helpers import *
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = None
    if session.get("USER_ID"):
        user = dbreq(f"SELECT * FROM users WHERE id = '{session.get('USER_ID')}'")[0]

    posts = [{"author": {"name": "Aboba1", "id": 34},
              "title": "Lorem ipsum dolor",
              "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem earum enim excepturi "
                         "expedita facere id inventore laborum maxime provident quisquam recusandae, repellendus "
                         "rerum saepe sed sunt tempora vero. Alias debitis est obcaecati perferendis rerum! Atque "
                         "blanditiis dicta eos esse facere quisquam. Ad animi aperiam consequuntur dignissimos "
                         "doloremque dolores, doloribus, earum eligendi facere fugiat id magnam minima nihil nisi, "
                         "odio optio perspiciatis placeat quisquam repellat sint tempora temporibus voluptatem! "
                         "Assumenda aut beatae commodi consectetur consequatur consequuntur corporis cupiditate "
                         "debitis dicta dignissimos doloribus ducimus eligendi enim et harum, impedit ipsum iure "
                         "iusto labore minus modi nobis non odio odit optio pariatur perspiciatis possimus qui quidem "
                         "quo recusandae reiciendis soluta temporibus, ullam vel voluptate voluptates. Adipisci "
                         "aliquam at, blanditiis doloribus est et explicabo facilis fugiat incidunt ipsam, "
                         "neque nostrum obcaecati quae repellendus tenetur. Cum doloribus, eum incidunt laboriosam "
                         "officia quisquam ratione sapiente temporibus? Deserunt facilis laboriosam velit? Doloremque "
                         "excepturi fugiat laudantium quod soluta?",
              "source": "Аноним",
              "image": "image.png",
              "date": "24.02.2022 04:55",
              "id": 69},
             {"author": {"name": "Aboba2", "id": 69},
              "title": "Lorem ipsum dolor",
              "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem earum enim excepturi "
                         "expedita facere id inventore laborum maxime provident quisquam recusandae, repellendus "
                         "rerum saepe sed sunt tempora vero. Alias debitis est obcaecati perferendis rerum! Atque "
                         "blanditiis dicta eos esse facere quisquam.",
              "date": "24.02.2022 04:56",
              "id": 34}
             ]
    return render_template("index.html", posts=posts, title="Новости", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not (request.form.get("email") and request.form.get("password")):
            flash("Все поля должны быть заполнены!")
            return render_template("login.html", title="Вход")

        users_info = dbreq(f"SELECT * FROM users WHERE email = '{request.form.get('email')}'")
        if not users_info:
            flash("Не правильный парооль или E-mail!")
            return render_template("login.html", title="Вход")

        user_info = users_info[0]

        if not checkpasshash(user_info["passwordhash"], request.form.get("password")):
            flash("Не правильный парооль или E-mail!")
            return render_template("login.html", title="Вход")

        session["USER_ID"] = user_info["id"]
        return redirect("/")

    return render_template("login.html", title="Вход")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not (request.form.get("email") and request.form.get("password") and request.form.get("username")):
            flash("Все поля должны быть заполнены!")
            return render_template("register.html", title="Регистрация")

        if not request.form.get("password") == request.form.get("cpassword"):
            flash("Пароли не совпадают!")
            return render_template("register.html", title="Регистрация")

        users_info = dbreq(f"SELECT * FROM users WHERE email = '{request.form.get('email')}'")

        if len(users_info) != 0:
            flash("Данный E-Mail уже используется!")
            return render_template("register.html", title="Регистрация")

        dbreq(f"INSERT INTO users (email, username, passwordhash) VALUES ('{request.form.get('email')}', '{request.form.get('username')}', '{tohash(request.form.get('password'))}')")
        user_info = dbreq(f"SELECT * FROM users WHERE email = '{request.form.get('email')}'")[0]

        session["USER_ID"] = user_info["id"]
        return redirect("/")

    return render_template("register.html", title="Регистрация")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/post<int:post_id>/")
def post(post_id):
    return f"POST {post_id}\nTODO"


@app.route("/user<int:user_id>/")
def user(user_id):
    return f"USER {user_id}\nTODO"
