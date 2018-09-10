from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
      return "This is a POST request"
  else:
      return render_template('hello.html')
