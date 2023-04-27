from flask import Flask, jsonify, send_file, request
from flask_cors import CORS, cross_origin
from PIL import Image
import json
import numpy as np

from preprocessing import clip,clear_files



app = Flask(__name__)


@app.route('/')
def hello():
    #clip()
    #clear_files('assets/planet_data/4_xyz')
    #calculateCultivatedExtent()
    return '<h1>Hello, Bubu!</h1>'


@app.route('/getNdviJson', methods=['GET'])
@cross_origin()
def get_ndvi_json():

    with open('assets/ndvi_data.json','r') as ndvi:
        data = json.load(ndvi)

    return jsonify(data)


@app.route('/getLswiJson', methods=['GET'])
@cross_origin()
def get_lswi_json():

    with open('assets/lswi_data.json','r') as lswi:
        data = json.load(lswi)

    return jsonify(data)


@app.route('/getResultsAPI')
@cross_origin()
def get_newdata():
    # Get the values of the parameters from the request URL
    x1 = int(request.args.get('x1'))
    y1 = int(request.args.get('y1'))
    x2 = int(request.args.get('x2'))
    y2 = int(request.args.get('y2'))
    map = request.args.get('map')
    model = request.args.get('model')


    print("Parameters Received from the frontend",x1,y1,x2,y2,map,model)
    save_directory = 'assets/history/clipped.jpg'

    if map == 'map1':
        if model == "LSTM":
            # Open the image file
            results_map = Image.open("assets/result_maps/lstm_model_result_map_1.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save(save_directory)

        elif model == 'CNN':

            results_map = Image.open("assets/result_maps/cnn_model_result_map_1.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save(save_directory)

        elif model == 'RF':

            results_map = Image.open("assets/result_maps/rf_model_result_map_1.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save(save_directory)

    elif map == 'map2':
        if model == "LSTM":
            # Open the image file
            results_map = Image.open("assets/result_maps/lstm_model_result_map_2.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save(save_directory)

        elif model == 'CNN':

            results_map = Image.open("assets/result_maps/cnn_model_result_map_2.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save(save_directory)

        elif model == 'RF':

            results_map = Image.open("assets/result_maps/rf_model_result_map_2.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save(save_directory)

    clipped = open(save_directory, "rb")

    # Return the image file as a response
    return send_file(clipped, mimetype='image/jpeg')


@app.route('/getAdditionalInfoAPI')
@cross_origin()
def get_additional():
    # Get the values of the parameters from the request URL
    map = request.args.get('map')
    model = request.args.get('model')

    print("Parameters Received from the frontend",map,model)

    if map == 'map1':
        if model == "LSTM":

            filename = 'assets/result_xyz/2_1_results_lstm_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'CNN':
            filename = 'assets/result_xyz/2_1_results_cnn_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'RF':
            filename = 'assets/result_xyz/2_1_results_rf_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

    elif map == 'map2':

        if model == "LSTM":
            filename = 'assets/result_xyz/2_2_results_lstm_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'CNN':
            filename = 'assets/result_xyz/2_2_results_cnn_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'RF':
            filename = 'assets/result_xyz/2_2_results_rf_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

    
    
def calculateCultivatedExtent(filename):

    if filename.endswith(".xyz"):

        #open file
        xyz_file = open(filename, "r")

        #read all lines and put to a list
        xyz_file_as_list = xyz_file.readlines()

        culitvated_pixels_count=0
        abandoned_pixels_count=0

        for pixel in xyz_file_as_list:

            pixel_value = pixel.split(" ")

            if pixel_value[2] == '1':
                culitvated_pixels_count += 1

            else:
                abandoned_pixels_count += 1

        print('total number of pixels -',len(xyz_file_as_list))
        print('cultivated pixels -',culitvated_pixels_count)
        print('abandoned pixels -',abandoned_pixels_count)

        cultivated_extent = culitvated_pixels_count*9
        abandoned_extent = abandoned_pixels_count*9

        return {'cultivated': cultivated_extent, 'abandoned': abandoned_extent,}







if __name__ == '__main__':
    app.run(port=3000, debug=True)



