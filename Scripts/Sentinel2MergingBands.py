from osgeo import gdal
import os


# assign directory
inDirectory = "/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/MahaSentinel/2021_10_22/clipped"

tif_arr=[]

outvrt = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/MahaSentinel/2021_10_22/clipped/m.vrt'
outtif = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/MahaSentinel/2021_10_22/clipped/stacked.tif'

# iterate over files in the directory
for filename in os.listdir(inDirectory):
    
    if filename.endswith(".tif"):
        
        input = os.path.join(inDirectory, filename)
        tif_arr.append(input)
        
        
        
outvrtds = gdal.BuildVRT(outvrt, tif_arr, separate=True)
outds = gdal.Translate(outtif, outvrtds,format='GTiff')
        