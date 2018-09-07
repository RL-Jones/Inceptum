from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Inceptum is born'


@app.route('/example/get')
def example_json_get():
    extracted_name = request.args.get('name', type=str)
    if extracted_name is None:
        return jsonify("new", "you must provide a name", "age")
    return jsonify(message="welcome " + 'i\'m lying - i\'m not a string', age=20)


@app.route('/robbie/route')
def robbie_written_route():
    extracted_name = request.args.get('name', type=str)
    extracted_age = request.args.get('age', type=str)
    if extracted_name is None:
        return jsonify(message="please return a proper name")
    if extracted_age is None:
        return jsonify(message="please return a proper age")
    return jsonify(message="Welcome " + extracted_name + " you are " + extracted_age)
