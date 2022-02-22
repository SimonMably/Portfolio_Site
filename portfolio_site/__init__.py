from datetime import datetime as dt
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import query
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, login_required, \
    current_user, logout_user

IMG_UPLOAD_FOLDER = "static/images/project-imgs"
ALLOWED_IMG_EXTENSIONS = {"jpg", "png"}

app = Flask(__name__)
Bootstrap(app)
ckeditor = CKEditor(app)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URL", "sqlite:///portfolio.db")
app.config['UPLOAD_FOLDER'] = IMG_UPLOAD_FOLDER
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)

from portfolio_site import routes