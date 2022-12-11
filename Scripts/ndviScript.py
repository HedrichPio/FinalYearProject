from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Documents/UNI/FinalYear/FYP/Implementation/PlanetData_FYP/MahaOutput/clipped'
outDirectory ='/Users/hedrichfernando/Documents/UNI/FinalYear/FYP/Implementation/PlanetData_FYP/MahaOutput/ndvi/ndvi_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    input = os.path.join(inDirectory, filename)
    output = outDirectory + filename

    
    process = """gdal_calc.py --overwrite --calc "(A-B)/(A+B)" --format GTiff --type Float32 --NoDataValue -9999.0 -A """+input+""" --A_band 4 -B """+input+""" --B_band 3 --outfile """+output
    os.system(process)




