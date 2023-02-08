from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/PlanetScope/NewYala/InputYala'
outDirectory ='/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/PlanetScope/NewYala/OutputYala/cultivated/clipped/clipped_'

#clipping coordinates plot 1 top abandoned
#coordinates = "427091.6225 914065.2363 427326.13 913880.9804"

#clipping coordinates of plot 2 middle cultivated
coordinates = "427208.8762 913728.3644 427681.6137 913499.4404"

 
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




