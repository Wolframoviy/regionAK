from os import getenv

CSRF_ENABLED = True
SECRET_KEY = getenv("CSRF_KEY")

