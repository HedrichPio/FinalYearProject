from osgeo import gdal
import os


# assign directory
inDirectory_band8a = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_1_clipped_8a'
inDirectory_band11 = '/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_1_clipped_12'

outDirectory ='/Users/hedrichfernando/Downloads/RemoteSensingData/Optical_RS/testData/2/test_sentinel2/2_1_lswi/lswi_'

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











