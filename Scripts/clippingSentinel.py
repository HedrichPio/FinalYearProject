from osgeo import gdal
import os


# assign directory
inDirectory = '/Users/hedrichfernando/Downloads/Optical_RS/MahaSentinel'
outDirectory ='/Users/hedrichfernando/Downloads/Optical_RS/MahaSentinel/clipped/clipped_'
 
# iterate over files in
# that directory

import os.path
import glob

for subdir in glob.glob("X/certain*"):
    path = os.path.join(subdir, "result.txt")
    with open(path, 'w') as fp:
        fp.write("This is the result\n")
        
        




