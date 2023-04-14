from osgeo import gdal
import os

input = '/Users/hedrichfernando/Downloads/cnn_results/cnn_model_4_test_2_1_preds_coords.xyz'

output = '/Users/hedrichfernando/Downloads/cnn_results/cnn_model_4_results_jpeg.jpg'


process = "gdal_translate -of JPEG -scale "+input+" "+output

os.system(process)




