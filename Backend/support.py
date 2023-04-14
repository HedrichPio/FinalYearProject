# from flask import Flask, jsonify, send_file, request
# from flask_cors import CORS, cross_origin
# from PIL import Image
# import json
# import os

# @app.route('/getNdviData', methods=['GET'])
# @cross_origin()
# def get_ndvi_data():

#     inDir = "assets/ndvi"

#     all_images=[]

#     for filename in os.listdir(inDir):

#         input = os.path.join(inDir, filename)
#         all_images.append(input)

#     return jsonify(all_images)


# @app.route('/getSingleNdviImage')
# @cross_origin()
# def get_single_ndvi_image():

#      file = request.args.get('filename')

#      return send_file(file, mimetype='image/jpeg')