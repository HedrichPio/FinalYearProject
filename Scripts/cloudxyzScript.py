from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/PlanetData_FYP/OutputFilesYala/CloudFiles'
outDirectory = '/Users/hedrichfernando/Downloads/PlanetData_FYP/OutputFilesYala/XYZCloudFiles/xyz_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    input = os.path.join(inDirectory, filename)
    output = outDirectory + os.path.splitext(filename)[0] + ".xyz"
    
    process = "gdal_translate -a_srs EPSG:32644 -a_nodata -9999.0 -of XYZ "+input+" "+output
    os.system(process)