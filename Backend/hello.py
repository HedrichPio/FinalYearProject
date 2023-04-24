from flask import Flask, jsonify, send_file, request
from flask_cors import CORS, cross_origin
from PIL import Image
import json
import os
from osgeo import gdal
#import numpy as np


app = Flask(__name__)


@app.route('/')
def hello():
    #clip()
    calculateCultivatedExtent()
    return '<h1>Hello, Bubu!</h1>'


@app.route('/dataJson', methods=['GET'])
@cross_origin()
def get_ndvi_json():

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
    map = request.args.get('map')
    model = request.args.get('model')


    print("Parameters Received from the frontend",x1,y1,x2,y2,map,model)

    if map == 'map1':
        if model == "LSTM":
            # Open the image file
            results_map = Image.open("assets/result_maps/lstm_model_result_map_1.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save("assets/clipped.jpg")

        elif model == 'CNN':

            results_map = Image.open("assets/result_maps/cnn_model_result_map_1.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save("assets/clipped.jpg")

        elif model == 'RF':

            results_map = Image.open("assets/result_maps/rf_model_result_map_1.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save("assets/clipped.jpg")

    elif map == 'map2':
        if model == "LSTM":
            # Open the image file
            results_map = Image.open("assets/result_maps/lstm_model_result_map_2.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save("assets/clipped.jpg")

        elif model == 'CNN':

            results_map = Image.open("assets/result_maps/cnn_model_result_map_2.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save("assets/clipped.jpg")

        elif model == 'RF':

            results_map = Image.open("assets/result_maps/rf_model_result_map_2.jpg")

            clipped_image = results_map.crop((x1,y1,x2,y2))

            clipped_image.save("assets/clipped.jpg")

    clipped = open("assets/clipped.jpg", "rb")

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

            filename = 'assets/result_xyz.nosync/2_1_results_lstm_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'CNN':
            filename = 'assets/result_xyz.nosync/2_1_results_cnn_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'RF':
            filename = 'assets/result_xyz.nosync/2_1_results_rf_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

    elif map == 'map2':

        if model == "LSTM":
            filename = 'assets/result_xyz.nosync/2_2_results_lstm_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'CNN':
            filename = 'assets/result_xyz.nosync/2_2_results_cnn_model.xyz'
            data = calculateCultivatedExtent(filename)
            # return a JSON response
            return jsonify(data)

        elif model == 'RF':
            filename = 'assets/result_xyz.nosync/2_2_results_rf_model.xyz'
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



def clip():
    # assign directory
    inDirectory = 'assets/planet_data/1_satellite_image'
    outDirectory ='assets/planet_data/clipped/2_clipped_'

    #2_2
    coordinates = "424754.5412 913791.2896 425894.2662 912715.0683"

    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        if filename.endswith(".tif"):
        #join file path and file name
            input = os.path.join(inDirectory, filename)
            
            #setting output file path
            output = outDirectory + filename

            #clipping raster file to given coordinates
            process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
            
            #execute process
            os.system(process)
    calculate_ndvi()
    
    
def calculate_ndvi():
    # assign directory
    inDirectory = 'assets/planet_data/2_clipped'
    outDirectory ='assets/planet_data/3_ndvi/ndvi_'
     
    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        if filename.endswith(".tif"):
            #join file path and file name
            input = os.path.join(inDirectory, filename)
            
            #setting output file path
            output = outDirectory + filename

            #calculating the ndvi from the given clipped raster files
            #generating raster file with calculated ndvi values
            process = """gdal_calc.py --overwrite --calc "(A-B)/(A+B)" --format GTiff --type Float32 --NoDataValue -9999.0 -A """+input+""" --A_band 4 -B """+input+""" --B_band 3 --outfile """+output
            
            #executing process
            os.system(process)
        
    convert_to_xyz()


def convert_to_xyz():
    # assign directory
    inDirectory = 'assets/planet_data/3_ndvi'
    outDirectory ='assets/planet_data/4_xyz/xyz_'
     
    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        if filename.endswith(".tif"):
            #join file path and file name
            input = os.path.join(inDirectory, filename)
            
            #setting output file path
            output = outDirectory + os.path.splitext(filename)[0] + ".xyz"
            
            #translating the ndvi raster file into xyz format
            process = "gdal_translate -a_srs EPSG:32644 -a_nodata -9999.0 -of XYZ "+input+" "+output
            os.system(process)



if __name__ == '__main__':
    app.run(port=3000, debug=True)



