from flask import session, redirect
from cs50 import SQL
from functools import wraps
from hashlib import sha256
from datetime import datetime
from app import app

try:
    db = SQL("sqlite:///app/database.db")
except RuntimeError:
    db = SQL("sqlite:///venv/database.db")


def dbreq(req):
    return db.execute(req)


def tohash(inp):
    byte = bytes(inp, "UTF-8")
    res = sha256(byte).hexdigest()
    return res


def checkpasshash(chash, passw):
    passhash = tohash(passw)
    return chash == passhash


@app.template_filter("unixtostring")
def unixtostring(ut):
    return datetime.utcfromtimestamp(ut).strftime('%Y-%m-%d %H:%M')


def getuser(uid):
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
