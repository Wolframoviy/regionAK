from flask import Flask

app = Flask(__name__)
SESSION_TYPE = "filesystem"
app.config.from_object("config")

from app import views

