from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_1_res'
outDirectory ='/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_1_xyz/xyz_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    if filename.endswith(".tif"):
        
        input = os.path.join(inDirectory, filename)
        output = outDirectory + os.path.splitext(filename)[0] + ".xyz"
        
        process = "gdal_translate -a_srs EPSG:32644 -a_nodata -9999.0 -of XYZ "+input+" "+output
        os.system(process)