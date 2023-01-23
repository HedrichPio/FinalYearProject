from osgeo import gdal
import os


# assign directory
inDirectory = "/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/Sentinel2/YalaSeperated/cultivated/lswi"

outDirectory ="/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/Sentinel2/YalaSeperated/cultivated/resampled/resampled_"

res = 3
algo = "near"

# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    if filename.endswith(".tif"):
        
        input = os.path.join(inDirectory, filename)
        
        output = outDirectory + filename

        process = gdal.Warp(output,input, xRes=res, yRes=res, resampleAlg=algo)

        