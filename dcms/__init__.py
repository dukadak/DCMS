from flask import Flask, render_template
from dcms.views import view

app = Flask(__name__)
app.register_blueprint(view.page)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404