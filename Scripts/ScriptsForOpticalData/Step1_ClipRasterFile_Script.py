from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/PlanetScope/NewYala/InputYala'
outDirectory ='/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/PlanetScope/NewYala/OutputYala/cultivated/clipped/clipped_'

#plot 1 top abandoned
#coordinates = "427091.6225 914065.2363 427326.13 913880.9804"

#plot 2 middle cultivated
coordinates = "427208.8762 913728.3644 427681.6137 913499.4404"

 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    input = os.path.join(inDirectory, filename)
    output = outDirectory + filename

    
    process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
    os.system(process)




