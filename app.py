from flask import Flask, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# database setting - SQLite db used
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# setting up db object, ORM - SQLAlchemy 
db = SQLAlchemy(app)


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
