from osgeo import gdal
import os
import numpy as np

#arr = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
#newa = np.where(arr==2, 4, arr)
#print(newa)


#assign directory
ndvi_xyz_Directory= '/Users/hedrichfernando/Documents/UNI/PlanetData_FYP/OutputFilesYala/XYZFiles'
cloud_xyz_Directory = '/Users/hedrichfernando/Documents/UNI/PlanetData_FYP/OutputFilesYala/XYZCloudFiles'
ouput_Directory = '/Users/hedrichfernando/Documents/UNI/PlanetData_FYP/OutputFilesYala/XyzNdviNoCloudsFiles'
 
list_of_ndvi_xyz_files = os.listdir(ndvi_xyz_Directory)
list_of_cloud_xyz_files = os.listdir(cloud_xyz_Directory)


for i in range(len(list_of_ndvi_xyz_files)):
    
#open xyz files of ndvi and clouds
    ndvi_xyz_file = open(ndvi_xyz_Directory+"/"+list_of_ndvi_xyz_files[i], "r")
    cloud_xyz_file = open(cloud_xyz_Directory+"/"+list_of_cloud_xyz_files[i], "r")

    
#add all xyz lines into seperate lists
    ndvi_line_list = ndvi_xyz_file.readlines()
    cloud_line_list = cloud_xyz_file.readlines()


#array of ndvi values after removing clouds
    ndvi_no_clouds_line_list = []

    for j in range(0, len(ndvi_line_list)):
        
        ndvi_line = ndvi_line_list[j];
        cloud_line = cloud_line_list[j];
        
        split_cloud_line = cloud_line.split(" ")
        
        print(split_cloud_line)

        if(split_cloud_line[2] == "0\n"):
            ndvi_no_clouds_line_list.append(ndvi_line)
        else:
            split_ndvi_line = ndvi_line.split(" ");
            new_ndvi_line = split_ndvi_line[0]+" "+split_ndvi_line[1]+" -10000\n"
            ndvi_no_clouds_line_list.append(new_ndvi_line)

#output xyz file name
    ndvi_no_cloud_xyz_file = ouput_Directory+'/no_clouds'+list_of_ndvi_xyz_files[i]+'.xyz'


    with open(ndvi_no_cloud_xyz_file, 'w') as file:
        
        for k in range(len(ndvi_no_clouds_line_list)):
            file.write(ndvi_no_clouds_line_list[k])




