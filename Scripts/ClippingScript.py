from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Documents/UNI/FinalYear/FYP/Implementation/PlanetData_FYP/Input/Maha/harmonized'
outDirectory ='/Users/hedrichfernando/Documents/UNI/FinalYear/FYP/Implementation/PlanetData_FYP/MahaOutput/clipped/clipped_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    input = os.path.join(inDirectory, filename)
    output = outDirectory + filename

    
    process = "gdal_translate -projwin 427510.8046 913623.5888 427612.0769 913522.3164 -of GTiff "+input+" "+output
    os.system(process)




