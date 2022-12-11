from osgeo import gdal
import os
import numpy as np


#assign directory
cloud_xyz_Directory = '/Users/hedrichfernando/Documents/UNI/PlanetData_FYP/OutputFilesYala/XYZCloudFiles'

list_of_cloud_xyz_files = os.listdir(cloud_xyz_Directory)

cloud_xyz_file = open(cloud_xyz_Directory+"/"+list_of_cloud_xyz_files[0], "r")

cloud_line_list = cloud_xyz_file.readlines()


for j in range(0, len(cloud_line_list)):
    
    cloud_line = cloud_line_list[j];
    
    split_cloud_line = cloud_line.split(" ")
    
    print(split_cloud_line)


