from flask import Flask
from flask import jsonify # Import `jsonify` http://flask.pocoo.org/docs/1.0/api/#flask.json.jsonify
from flask import request # Import `request` to use in `example_query_parameters`

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Inceptum is born'

@app.route('/example/json') # Add a new route for /example/json
def example_json():
    example_values = {      # `example_values` is a dictionary used to store keys with values
        # 'key': 'value',   # read more with a tutorial: https://www.python-course.eu/dictionaries.php
        "name": "jack",
        "age": 30,
        "profession": "unemployed",
        "skills": ['gis', 'python', 'flask', 'leadership']
    }
    return jsonify(example_values)

@app.route('/example/query')        # Add a new route for /example/query
def example_query_parameters():
    # Extracting query parameters as found https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url
    # official Flask documentation link: http://flask.pocoo.org/docs/1.0/api/#flask.Request.args
    age = request.args.get('age', -1, type=int) # Extract the age from the query parameter sent like /example/query?age=35
    # read the official documentation to understand what the `0` and `type=int` mean

    # based on the age extracted, handle something differently
    if age < 0:
        return "you must enter a proper age"
    elif age <= 25:
        return "just getting started - go get 'em"
    elif age > 25 and age <=120:
        return "how is life going?"
    elif age > 120:
        return "vampire!!!"
