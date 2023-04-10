from flask import Flask, jsonify, send_file, request
from flask_cors import CORS, cross_origin
from PIL import Image
import json
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, Bubu!</h1>'


@app.route('/getNdviData', methods=['GET'])
@cross_origin()
def get_ndvi_data():

    inDir = "assets/ndvi"

    all_images=[]

    for filename in os.listdir(inDir):

        input = os.path.join(inDir, filename)
        all_images.append(input)

    return jsonify(all_images)


@app.route('/getSingleNdviImage')
@cross_origin()
def get_single_ndvi_image():

     file = request.args.get('filename')

     return send_file(file, mimetype='image/jpeg')


@app.route('/dataJson', methods=['GET'])
@cross_origin()
def get_json():

    with open('assets/ndvi_data.json','r') as f:
        data = json.load(f)

    return jsonify(data)


@app.route('/getLswiJson', methods=['GET'])
@cross_origin()
def get_lswi_json():

    with open('assets/lswi_data.json','r') as f:
        data = json.load(f)

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



