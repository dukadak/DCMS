from flask import Blueprint, render_template, url_for, request
from dcms.models import Assets
from dcms import db

page = Blueprint('page', __name__, template_folder='templates')

# index page
@page.route('/')
def index():
    return render_template('index.html')

# page for listing assets
@page.route('/assets', methods=['GET', 'POST'])
def assets():
    if request.method == 'POST':
        add_data = Assets(request.form['asset_name'], request.form['asset_count'], request.form['asset_serial_num'])
        db.session.add(add_data)
        db.session.commit()

    asset_data = Assets.query.all()
    return render_template('assets.html', assets=asset_data)

# page for adding assets
@page.route('/add_assets')
def add_assets():
    return render_template('add_assets.html')
