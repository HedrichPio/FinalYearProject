from osgeo import gdal
import os


# assign directory
inputFile = '/Users/hedrichfernando/Downloads/predicted_XYZ/model10_test_2_1_preds_coords.xyz'
outputFile ='/Users/hedrichfernando/Downloads/test2_jpeg.jpg'
     
#process = "gdal_translate "+inputFile+" "+outputFile
#os.system(process)


process = "gdal_translate -of JPEG -scale -co worldfile=yes "+inputFile+" "+outputFile
os.system(process)
    
    
    
    
    
    