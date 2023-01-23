from osgeo import gdal
import os


# assign directory
inDirectory = "/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/Sentinel2/YalaSeperated/band8a"
inDirectory_b = "/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/Sentinel2/YalaSeperated/band12"

outDirectory ="/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/Sentinel2/YalaSeperated/cultivated/clipped_band8a/clipped_"
outDirectory_b ="/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/Sentinel2/YalaSeperated/cultivated/clipped_band12/clipped_"

#plot 1 top abandoned
#coordinates = "427091.6225 914065.2363 427326.13 913880.9804"

#plot 2 middle cultivated
coordinates = "427208.8762 913728.3644 427681.6137 913499.4404"


# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    if filename.endswith(".tif"):
        
        input = os.path.join(inDirectory, filename)
        
        output = outDirectory + filename

        
        process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
        os.system(process)
        
        

for filename in os.listdir(inDirectory_b):
    
    if filename.endswith(".tif"):
        
        input = os.path.join(inDirectory_b, filename)
        
        output = outDirectory_b + filename



        process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
        os.system(process)
        
        