from cs50 import SQL
from hashlib import sha256
from datetime import datetime
from app import app

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
