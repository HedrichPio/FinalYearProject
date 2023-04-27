from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_planet/2_1_clipped'
outDirectory ='/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_planet/2_1_ndvi/ndvi_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    #join file path and file name
    input = os.path.join(inDirectory, filename)
    
    #setting output file path
    output = outDirectory + filename

    #calculating the ndvi from the given clipped raster files
    #generating raster file with calculated ndvi values
    process = """gdal_calc.py --overwrite --calc "(A-B)/(A+B)" --format GTiff --type Float32 --NoDataValue -9999.0 -A """+input+""" --A_band 4 -B """+input+""" --B_band 3 --outfile """+output
    
    #executing process
    os.system(process)




