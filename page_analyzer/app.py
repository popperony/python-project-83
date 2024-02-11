import os
import requests
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    flash,
    get_flashed_messages,
    url_for,
    redirect
)
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

# @app.get('/urls')
# def get_urls():
#     """
#         Get all urls from DB
#         Show all urls
#     """
#     urls = get_all_urls()
#     return render_template(
#         'urls.html',
#         urls=urls
#     )