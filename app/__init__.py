from flask import Flask

app = Flask(__name__)
from app import views
app.jinja_env.globals.update(format_date_joined=views.format_date_joined)