from flask import render_template, request, flash, session, redirect
from .helpers import *
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = None
    if session.get("USER_ID"):
        user = dbreq(f"SELECT * FROM users WHERE id = '{session.get('USER_ID')}'")[0]

    posts_info = dbreq("SELECT posts.*, users.username AS author FROM posts, users WHERE 'posts'.author_id = users.id ORDER BY 'posts'.pdate LIMIT 15")

    return render_template("index.html", posts=posts_info, title="Новости", user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

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
    session.clear()

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

        dbreq(f"INSERT INTO users (email, username, passwordhash, image) VALUES ('{request.form.get('email')}', '{request.form.get('username')}', '{tohash(request.form.get('password'))}', 'default.png')")
        user_info = dbreq(f"SELECT * FROM users WHERE email = '{request.form.get('email')}'")[0]

        session["USER_ID"] = user_info["id"]
        return redirect("/")

    return render_template("register.html", title="Регистрация")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/profile")
def profile():
    return redirect(f"/user{session.get('USER_ID')}")


@app.route("/post<int:post_id>/")
def post(post_id):
    post_info = dbreq(f"SELECT posts.*, users.username AS author FROM posts, users WHERE posts.id = {post_id}")[0]

    return render_template("post.html", post=post_info, title=post_info["title"], user=getuser(session.get("USER_ID")))


@app.route("/user<int:user_id>/")
def user(user_id):
    user_info = getuser(user_id)
    user_posts = dbreq(f"SELECT * FROM posts WHERE author_id = {user_id}")

    return render_template("profile.html", title=user_info["username"], user=getuser(session.get("USER_ID")),tuser=user_info, posts=user_posts)
