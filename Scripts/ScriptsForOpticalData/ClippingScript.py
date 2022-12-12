from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/Optical_RS/NewYala/InputYala'
outDirectory ='/Users/hedrichfernando/Downloads/Optical_RS/NewYala/Output/clipped/clipped_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    input = os.path.join(inDirectory, filename)
    output = outDirectory + filename

    
    process = "gdal_translate -projwin 427267.9877 913385.5604 427375.0419 913286.2919 -of GTiff "+input+" "+output
    os.system(process)




