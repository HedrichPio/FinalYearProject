from osgeo import gdal
import os


# assign directory
inDirectory_a = "/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/8a"
inDirectory_b = "/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/12"

outDirectory_a ="/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_1_clipped_8a/clipped_"
outDirectory_b ="/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_1_clipped_12/clipped_"

#plot 1 top abandoned
#coordinates = "427091.6225 914065.2363 427326.13 913880.9804"

#plot 2 middle cultivated
#coordinates = "423248.6804 913383.1087 423696.8471 912908.8857"

#coordinates = "424201.5197 914137.0564 427785.3617 912606.8766"

#2_1
coordinates = "426567.166 914120.5428 427771.847 913127.2683"


# iterate over files in
# that directory
for filename in os.listdir(inDirectory_a):
    
    if filename.endswith(".tif"):
        
        input = os.path.join(inDirectory_a, filename)
        
        output = outDirectory_a + filename

        
        process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
        os.system(process)
        
        

for filename in os.listdir(inDirectory_b):
    
    if filename.endswith(".tif"):
        
        input = os.path.join(inDirectory_b, filename)
        
        output = outDirectory_b + filename



        process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
        os.system(process)
        
        