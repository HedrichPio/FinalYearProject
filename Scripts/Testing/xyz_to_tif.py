from osgeo import gdal
import os


# assign directory
#inputFile = '/Users/hedrichfernando/Downloads/predicted_XYZ/model10_test_2_1_preds_coords.xyz'
#outputFile ='/Users/hedrichfernando/Downloads/test2_jpeg.jpg'
     
#process = "gdal_translate "+inputFile+" "+outputFile
#os.system(process)


#process = "gdal_translate -of JPEG -scale -co worldfile=yes "+inputFile+" "+outputFile
#os.system(process)
    
input_a = '/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_planet/2_1_xyz/xyz_ndvi_clipped_2022_07_19_harmonized_clip.xyz'

output_a = '/Users/hedrichfernando/Downloads/xyz_to_jpg2.jpg'


process_a = "gdal_translate -of JPEG -scale "+input_a+" "+output_a

os.system(process_a)

    
    
    