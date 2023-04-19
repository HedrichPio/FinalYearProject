from osgeo import gdal
import os


def clip():
    # assign directory
    inDirectory = '/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_planet/whole_land/data'
    outDirectory ='/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_planet/2_2/clipped/clipped_'

    #2_2
    coordinates = "424754.5412 913791.2896 425894.2662 912715.0683"

    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        if filename.endswith(".tif"):
        #join file path and file name
            input = os.path.join(inDirectory, filename)
            
            #setting output file path
            output = outDirectory + filename

            #clipping raster file to given coordinates
            process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
            
            #execute process
            os.system(process)
    
    calculate_ndvi()
    
    
def calculate_ndvi():
    # assign directory
    inDirectory = '/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_planet/2_2/clipped'
    outDirectory ='/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_planet/2_2/ndvi/ndvi_'
     
    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        if filename.endswith(".tif"):
            #join file path and file name
            input = os.path.join(inDirectory, filename)
            
            #setting output file path
            output = outDirectory + filename

            #calculating the ndvi from the given clipped raster files
            #generating raster file with calculated ndvi values
            process = """gdal_calc.py --overwrite --calc "(A-B)/(A+B)" --format GTiff --type Float32 --NoDataValue -9999.0 -A """+input+""" --A_band 4 -B """+input+""" --B_band 3 --outfile """+output
            
            #executing process
            os.system(process)
        
    convert_to_xyz()


def convert_to_xyz():
    # assign directory
    inDirectory = '/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_planet/2_2/ndvi'
    outDirectory ='/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_planet/2_2/xyz/xyz_'
     
    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        if filename.endswith(".tif"):
            #join file path and file name
            input = os.path.join(inDirectory, filename)
            
            #setting output file path
            output = outDirectory + os.path.splitext(filename)[0] + ".xyz"
            
            #translating the ndvi raster file into xyz format
            process = "gdal_translate -a_srs EPSG:32644 -a_nodata -9999.0 -of XYZ "+input+" "+output
            os.system(process)
    

clip()
