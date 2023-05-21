from flask import session, redirect
from cs50 import SQL
from functools import wraps
from hashlib import sha256
from datetime import datetime

import config
from app import app

try:
    db = SQL("sqlite:///app/database.db")
except RuntimeError:
    db = SQL("sqlite:///venv/database.db")


def dbreq(req):
    return db.execute(req)


def to_hash(inp):
    byte = bytes(inp, "UTF-8")
    res = sha256(byte).hexdigest()
    return res


def check_passhash(chash, passw):
    passhash = to_hash(passw)
    return chash == passhash


@app.template_filter("unixtostring")
def unix_to_string(ut):
    return datetime.utcfromtimestamp(ut).strftime('%Y-%m-%d %H:%M')


def get_user(uid):
    users = dbreq(f"SELECT * FROM users WHERE id = {uid}")
    if len(users) == 0:
        return {"id": 0, "username": "Пользователь не найден", "email": "not@found.sorry", "passwordhash": "абоба", "image": "defauld.png"}

    return users[0]


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("USER_ID") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS
