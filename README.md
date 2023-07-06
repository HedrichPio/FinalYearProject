# FinalYearProject
Detecting abandoned paddy lands using deep learning.

This project uses a pixel based approach that utilises the phenological growth stages of paddy rice to distinguish between the abandoned and active paddy lands. Satellite remote sensing data was used as the primary data source for the project. Passive remote sensing data from two satellites were used to train the deep learning model. Planet constellation and sentinel2 satellites were selected among the many satellites to gather data for the project.

The downloaded satellite data underwent a series of pre-processing steps before being used to train the deep learning model. All the pre-processing was done using python scripts and are available in this repository under the Scripts folder. The scripts used for each type of stalllite are seperated into folders. Each pre-processing task is divided into steps and the files are named accordinly.

## Step 1 
* This step is used to clip the satellite images or the raster files into the desired coordinates as satellite images comes in larger sizes covering a large area of land.
* Initially the input and output directories are assigned.
* Then the coordinates of the area of interest is assigned to the coordinates variable.
* Then the script can be executed and all the clipped satellite images will be saved in the output directory.

## Step 2
* This step is used to calculate the NDVI of each pixel of the satellite image or raster file.
* Initially the input and output directories are assigned. The input directory for this step is the output directory of step 1.
* Then execute the script and NDVI for all the pixels will be calculated and saved in the output directory.

## Step 3
* This step is used to convert the raster files containing the NDVI values into XYZ file format.
* Assign the input and output directories to the relevant variables. The input directory for this step is the output directory of step 2.

## Step 4
* This step is used to analyse the converted XYZ files to ensure that the NDVI changes based on the phenological growth can be observed.
* Assign the output directory from step 3 as the input directory in this step.
* Next pass the capture dates of the satellite images as an array of strings in the ascending order of the dates, ex:dates = `["04/04/2022","06/04/2022","23/04/2022"]`.
* Time series graphs will be generated to analyse the phenological growth curves of pixals in the satellite images.

## Step 5
* In this step the NDVI values of a pixel is interpolated with respect to the capture dates of the satellite image. The number of days from start of the farming season to the capture date is being used.
* Next the number of days between the start and end of the farming season is calculated which is then used to divided into 20 days with equal time intervals.
* Then the interpolated NDVI values are obtained for the calculated 20 days which will then be saved to an CSV file along with the class label.



