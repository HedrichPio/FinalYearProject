from flask import Flask, jsonify, send_file, request
from flask_cors import CORS, cross_origin
from PIL import Image

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



@app.route('/getResultsAPI')
@cross_origin()
def get_newdata():
    # Get the values of the parameters from the request URL
    x1 = int(request.args.get('x1'))
    y1 = int(request.args.get('y1'))
    x2 = int(request.args.get('x2'))
    y2 = int(request.args.get('y2'))


    print("Parameters Received from the frontend",x1,y1,x2,y2)

    # Open the image file
    results_map = Image.open("assets/result_map.jpg")

    clipped_image = results_map.crop((x1,y1,x2,y2))

    clipped_image.save("assets/clipped.jpg")

    clipped = open("assets/clipped.jpg", "rb")

    # Return the image file as a response
    return send_file(clipped, mimetype='image/jpeg')





if __name__ == '__main__':
    app.run(port=3000, debug=True)



