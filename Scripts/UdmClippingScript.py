from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/PlanetData_FYP/InputFilesYala/udmFiles'
outDirectory = '/Users/hedrichfernando/Downloads/PlanetData_FYP/OutputFilesYala/ClippedUdmFiles/clipped_'
 
# iterate over files in
# that directory
for filename in os.listdir(inDirectory):
    
    input = os.path.join(inDirectory, filename)
    output = outDirectory + filename

    
    process = "gdal_translate -projwin 427179.6142 913746.8861 427706.2631 913483.5616 -of GTiff "+input+" "+output
    os.system(process)
