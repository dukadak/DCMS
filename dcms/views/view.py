from flask import Flask, Blueprint, render_template, url_for

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/assets')
def assets():
    return render_template('assets.html')

@page.route('/add_assets')
def add_assets():
    return render_template('add_assets.html')

    