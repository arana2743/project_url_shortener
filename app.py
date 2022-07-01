from flask import Flask, redirect, request, jsonify

app = Flask(__name__)

# API routes
# main root url - just used here to check if API is working
@app.route('/', methods=['GET'])
def hello_world():
  data = {
    "name": "URL Shortener API",
    "desc": "A url shortening api service."
  }
  return jsonify(data)


# main call for the app
if __name__ == '__main__':
  # port = int(os.environ.get('PORT', 5000))
  # print(f'Server running on : {port}')
  app.run(port=5000, host='0.0.0.0', debug=True)
