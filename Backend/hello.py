from flask import Flask, jsonify, send_file, request
from flask_cors import CORS, cross_origin
from PIL import Image
import json
import os
from osgeo import gdal
import numpy as np


app = Flask(__name__)


@app.route('/')
def hello():
    clip()
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
    model = request.args.get('model')


    print("Parameters Received from the frontend",x1,y1,x2,y2,model)

    if model == "LSTM":
        # Open the image file
        results_map = Image.open("assets/result_maps/lstm_model_result_map.jpg")

        clipped_image = results_map.crop((x1,y1,x2,y2))

        clipped_image.save("assets/clipped.jpg")

    elif model == 'CNN':

        results_map = Image.open("assets/result_maps/cnn_model_result_map.jpg")

        clipped_image = results_map.crop((x1,y1,x2,y2))

        clipped_image.save("assets/clipped.jpg")


    clipped = open("assets/clipped.jpg", "rb")

    # Return the image file as a response
    return send_file(clipped, mimetype='image/jpeg')
    

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



