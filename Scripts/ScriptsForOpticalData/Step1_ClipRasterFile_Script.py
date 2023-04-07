from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_planet/data'
outDirectory ='/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_planet/2_1_clipped/clipped_'

#clipping coordinates plot 1 top abandoned
#coordinates = "427091.6225 914065.2363 427326.13 913880.9804"

#clipping coordinates of plot 2 middle cultivated
#coordinates = "427208.8762 913728.3644 427681.6137 913499.4404"

#2
#coordinates = "424201.5197 914137.0564 427785.3617 912606.8766"

#2.1
coordinates = "426567.166 914120.5428 427771.847 913127.2683"

 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    #join file path and file name
    input = os.path.join(inDirectory, filename)
    
    #setting output file path
    output = outDirectory + filename

    #clipping raster file to given coordinates
    process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
    
    #execute process
    os.system(process)




