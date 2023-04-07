from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, Bubu!</h1>'

@app.route('/api/data', methods=['GET'])
@cross_origin()
def get_data():
    # Your code to get data goes here
    data = {'foo': 'bar', 'baz': 'pio'}
    return jsonify(data)


@app.route('/about', methods=['GET'])
def get_about():
    return '<h1>Hello, about!</h1>'


if __name__ == '__main__':
    app.run(port=8070, debug=True)



