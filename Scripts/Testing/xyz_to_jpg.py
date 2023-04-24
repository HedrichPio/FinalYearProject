from osgeo import gdal
import os

input = '/Users/hedrichfernando/Downloads/FYP/predicting_CSV/results/rf_results/2_rf_model_2_1_preds_coords.xyz'

output = '/Users/hedrichfernando/Downloads/jpeg_2_1_results_rf_model.jpg'

process = "gdal_translate -of JPEG -scale "+input+" "+output

os.system(process)




