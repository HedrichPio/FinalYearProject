from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/PlanetData_FYP/OutputFilesYala/ClippedUdmFiles'
outDirectory = '/Users/hedrichfernando/Downloads/PlanetData_FYP/OutputFilesYala/CloudFiles/clouds_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    input = os.path.join(inDirectory, filename)
    output = outDirectory + filename

    process = """gdal_calc.py --overwrite --calc "A" --format GTiff --type Float32 -A """+input+""" --A_band 6 --outfile """+output
    os.system(process)
