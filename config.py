from os import getenv

CSRF_ENABLED = True
SECRET_KEY = getenv("CSRF_KEY")
UPLOAD_FOLDER = 'app/static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
