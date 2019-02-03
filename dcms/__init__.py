from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database
app.config.from_object('config')
db = SQLAlchemy(app)
from dcms import models

# view
from dcms.views import view
app.register_blueprint(view.page)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404