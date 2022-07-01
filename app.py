from flask import Flask, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import string
from datetime import datetime
from random import choices


app = Flask(__name__)

# database setting - SQLite db used
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# setting up db object, ORM - SQLAlchemy 
db = SQLAlchemy(app)


# defining the models
class Link(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  original_url = db.Column(db.String(512))
  short_url = db.Column(db.String(5), unique=True)
  visits = db.Column(db.Integer, default=0)
  date_created = db.Column(db.DateTime,  default=datetime.now)

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.short_url = self.generate_short_link()

  def generate_short_link(self):
    characters = string.digits + string.ascii_letters
    short_url = ''.join(choices(characters, k=5))
    
    link = self.query.filter_by(short_url=short_url).first()
    if link:
      return self.generate_short_link()
    
    return short_url


# API routes
# main root url - just used here to check if API is working
@app.route('/', methods=['GET'])
def hello_world():
  data = {
    "name": "URL Shortener API",
    "desc": "A url shortening api service."
  }
  return jsonify(data)

# /shorten_url = used to pass long_url to shorten it as json 
# format : { 'original_url': 'https://www.example.com/ }
@app.route('/shorten_url', methods=['POST'])
def shorten_url():
  pass


# /<short_url> = used to redirect from short_url to original_url 
@app.route('/<short_url>')
def redirect_to_url(short_url):
  pass


@app.route('/stats', methods=['GET'])
def get_all_stats():
  pass



# main call for the app
if __name__ == '__main__':
  # port = int(os.environ.get('PORT', 5000))
  # print(f'Server running on : {port}')
  app.run(port=5000, host='0.0.0.0', debug=True)
