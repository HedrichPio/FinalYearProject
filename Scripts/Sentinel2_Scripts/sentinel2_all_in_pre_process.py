from osgeo import gdal
import os


def clip():
    # assign directory
    inDirectory_a = "/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/whole_land/8a"
    inDirectory_b = "/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/whole_land/12"

    outDirectory_a ="/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/clipped_8a/clipped_"
    outDirectory_b ="/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/clipped_12/clipped_"

    #2_2
    coordinates = "424754.5412 913791.2896 425894.2662 912715.0683"


    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory_a):
        
        if filename.endswith(".tif"):
            
            input = os.path.join(inDirectory_a, filename)
            
            output = outDirectory_a + filename

            
            process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
            os.system(process)
            
            

    for filename in os.listdir(inDirectory_b):
        
        if filename.endswith(".tif"):
            
            input = os.path.join(inDirectory_b, filename)
            
            output = outDirectory_b + filename



            process = "gdal_translate -projwin "+coordinates+" -of GTiff "+input+" "+output
            os.system(process)
        
        
    calculate_LSWI()
    
    

def calculate_LSWI():
    # assign directory
    inDirectory_band8a = '/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/clipped_8a'
    inDirectory_band11 = '/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/clipped_12'

    outDirectory ='/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/lswi/lswi_'

    unsorted_band8a = []
    unsorted_band11 = []


    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory_band8a):
        
        if filename.endswith(".tif"):
            
            unsorted_band8a.append(filename)
            

    for filename in os.listdir(inDirectory_band11):
        
        if filename.endswith(".tif"):
            
            unsorted_band11.append(filename)



    sorted_band8a = sorted(unsorted_band8a)
    sorted_band11 = sorted(unsorted_band11)

    #for i in range(len(sorted_band8a)):
        #print(sorted_band8a[i])
        #print(sorted_band11[i])
        #print('----------')
        
    for i in range(len(sorted_band8a)):
        
        input_band8a = os.path.join(inDirectory_band8a, sorted_band8a[i])
        input_band11 = os.path.join(inDirectory_band11, sorted_band11[i])

        output = outDirectory + sorted_band8a[i]

        process = """gdal_calc.py --overwrite --calc "(A-B)/(A+B)" --format GTiff --type Float32 --NoDataValue -9999.0 -A """+input_band8a+""" --A_band 1 -B """+input_band11+""" --B_band 1 --outfile """+output
        os.system(process)
    
    resample_LSWI()


def resample_LSWI():
    # assign directory
    inDirectory = "/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/lswi"

    outDirectory ="/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/resample/resampled_"

    res = 3
    algo = "near"

    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        
        if filename.endswith(".tif"):
            
            input = os.path.join(inDirectory, filename)
            
            output = outDirectory + filename

            process = gdal.Warp(output,input, xRes=res, yRes=res, resampleAlg=algo)
            
    convert_to_xyz()
    
    
            
def convert_to_xyz():
    # assign directory
    inDirectory = '/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/resample'
    outDirectory ='/Users/hedrichfernando/Downloads/FYP/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_2/xyz/xyz_'
     
    # iterate over files in
    # that directory
    for filename in os.listdir(inDirectory):
        
        if filename.endswith(".tif"):
            
            input = os.path.join(inDirectory, filename)
            output = outDirectory + os.path.splitext(filename)[0] + ".xyz"
            
            process = "gdal_translate -a_srs EPSG:32644 -a_nodata -9999.0 -of XYZ "+input+" "+output
            os.system(process)
            
            
            
clip()