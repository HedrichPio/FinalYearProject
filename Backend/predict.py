import pandas as pd
import numpy as np
import csv
from tensorflow import keras
from osgeo import gdal
import os

def get_predictions(ndviFile,lswiFile,coordFile):

    ndvi = ndviFile
    lswi = lswiFile
    coordinates = coordFile

    ndvi = ndvi.drop(['label'],axis=1)
    lswi = lswi.drop(['label'],axis=1)

    ndvi_array = np.array(ndvi)
    lswi_array = np.array(lswi)

    print('ndvi -',len(ndvi_array))
    print('lstw -',len(lswi_array))

    no_of_rows = len(ndvi_array) if len(ndvi_array) <= len(lswi_array) else len(lswi_array)
    no_of_columns = len(ndvi_array[0])

    ndvi_lswi_all_pixels=[]

    for i in range(no_of_rows):

        all_ndvi_lswi_values_of_single_pixel=[]

        for j in range(no_of_columns):

            ndvi_lswi_per_day=[ndvi_array[i][j],lswi_array[i][j]]

            all_ndvi_lswi_values_of_single_pixel.append(ndvi_lswi_per_day)

        ndvi_lswi_all_pixels.append(all_ndvi_lswi_values_of_single_pixel)


    X = ndvi_lswi_all_pixels


    model = keras.models.load_model('assets/models/model_10.h5')

    predictions = model.predict(X)

    predicted_labels=[]

    for i in predictions:
        if i>0.5:
            predicted_labels.append(1)
   
        else:
            predicted_labels.append(0)


    coordinate_array = np.array(coordinates)

    coordinate_prediction=[]

    myfile = open("assets/predicted_results/predictions.xyz","w")

    for i in range(len(coordinate_array)):
    
        single_line=[coordinate_array[i][0],coordinate_array[i][1],predicted_labels[i]]
    
        myfile.write("%f %f %d \n" % (coordinate_array[i][0],coordinate_array[i][1],predicted_labels[i]))
    
        coordinate_prediction.append(single_line)

    myfile.close()

    generate_map()


def generate_map():

    input = 'assets/predicted_results/predictions.xyz'

    output = 'assets/predicted_results/predicted_map.jpg'

    process = "gdal_translate -of JPEG -scale "+input+" "+output

    os.system(process)

