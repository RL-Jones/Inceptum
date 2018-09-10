from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
      return "This is a POST request"
  else:
      return "This is not a POST request"
