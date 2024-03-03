# -*- coding: utf-8 -*-
#import geopandas as gpd
import rasterio as rio
import numpy as np
#from osgeo import gdal
#import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#fukushima_shp = gpd.read_file(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\Shp\FukushimaPref.shp')


#result_raster = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\Result\Excluded_areas.tif')
#result_data = result_raster.read(1)
#print(np.unique(result_data)) #unique data is 0=not suitable, 1=suitable, 127 = no data

#ds = gdal.Open(r"C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\Result\Excluded_areas.tif")
# xyz = gdal.Translate("result.xyz", ds)
# xyz = None 

# df = pd.read_csv("result.xyz", sep = " ", header = None)
# df.columns = ["x", "y", "result"]
# df.to_csv("result.csv", index = False)

# def extract_data(tif_path):
#     with rio.open(tif_path) as src:
#         data = src.read(1)
#         transform = src.transform


# transform = result_raster.transform
# lon, lat = [], []

# for y in range(result_data.shape[0]):
#     for x in range(result_data.shape[1]):
#         lon_val, lat_val = transform * (x,y)
#         lon.append(lon_val)
#         lat.append(lat_val)
        
# lon_array = np.array(lon)
# lat_array = np.array(lat)


# result_raster2 = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Start work data\raw_data.tif')
# result_data2 = result_raster2.read(1)
# print(np.unique(result_data2)) #0 for no, 1 for yes


# result_raster3 = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Start work data\rendered_im.tif')
# result_data3 = result_raster3.read(1)
# print(np.unique(result_data3)) #rendered_im had 3 band, inaccurate data

def normalizing(data):
    min_val = np.min(data) 
    max_val = np.max(data)
    data_normalized = (data - min_val) / (max_val - min_val)
    return data_normalized

def get_patch(array, size=256):
    patch_list = []
    height, width, _ = array.shape
    for i in range(0, height, size):
        for j in range(0, width, size):
            patch = array[i:i+size, j:j+size, :]
            if patch.shape[0] == size and patch.shape[1] == size:
                patch_list.append(patch)
    return patch_list

def get_patch2(array, size=256):
    patch_list = []
    height, width = array.shape
    for i in range(0, height, size):
        for j in range(0, width, size):
            patch = array[i:i+size, j:j+size] #The diff with above func is that this make it 2D array
            if patch.shape[0] == size and patch.shape[1] == size:
                patch_list.append(patch)
    return patch_list


elec_demand = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareElec.tif')
elec_demand_data = elec_demand.read(1)
print("Elec:", np.unique(elec_demand_data))
elec_demand_norm = normalizing(elec_demand_data)
print("Elec norm:", np.unique(elec_demand_norm))
#plt.imshow(elec_demand_data)

Interest_spot = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareInterest.tif')
Interest_spot_data = Interest_spot.read(1)
print("Interest:", np.unique(Interest_spot_data)) 
Interest_spot_norm = normalizing(Interest_spot_data)
print("Interest norm:", np.unique(Interest_spot_norm))


Land_price = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareLandPrice.tif')
Land_price_data = Land_price.read(1)
print("land price:", np.unique(Land_price_data)) 
Land_price_norm = normalizing(Land_price_data)
print("Land price norm:", np.unique(Land_price_norm))


Natural_environment = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareNat.tif')
Natural_environment_data = Natural_environment.read(1)
print("nat:", np.unique(Natural_environment_data))
Natural_environment_norm = normalizing(Natural_environment_data)
print("Nat norm:", np.unique(Natural_environment_norm))


Roads = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareRoad.tif')
Roads_data = Roads.read(1)
print("road:", np.unique(Roads_data)) 
Roads_norm = normalizing(Roads_data)
print("road norm:", np.unique(Roads_norm)) 


Elevation = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareSlopeElevation.tif')
Elevation_data = Elevation.read(1)
print("eleva:", np.unique(Elevation_data)) 
Elevation_norm = normalizing(Elevation_data)
print("elev norm:", np.unique(Elevation_norm)) 



Transmission_line = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareTrans.tif')
Transmission_line_data = Transmission_line.read(1)
print("transmi:",np.unique(Transmission_line_data)) 
Transmission_line_norm = normalizing(Transmission_line_data)
print("trans norm:", np.unique(Transmission_line_norm)) 


Urban_area = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareUrban.tif')
Urban_area_data = Urban_area.read(1)
print("urban:", np.unique(Urban_area_data))
Urban_area_norm = normalizing(Urban_area_data)
print("urban norm:", np.unique(Urban_area_norm))  


Wind_speed = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareWindAtlas.tif')
Wind_speed_data = Wind_speed.read(1)
print("wind:", np.unique(Wind_speed_data)) 
Wind_speed_norm = normalizing(Wind_speed_data)
print("wind norm:", np.unique(Wind_speed_norm)) 


#Prepare to stack all 9 criteria map together as 1 input
input_data = np.stack((elec_demand_norm, Interest_spot_norm, Land_price_norm,
                        Natural_environment_norm, Roads_norm, Elevation_norm,
                        Transmission_line_norm, Urban_area_norm, Wind_speed_norm), axis=-1)

print("Shape of input data:", input_data.shape)

#Prepare output data, the result
result_im = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareResult.tif')
result_data = result_im.read(1)
print("result:", np.unique(result_data)) 
print("Shape of result data:", result_data.shape)


# #Combine the result raster as well
# combined = np.stack((elec_demand_norm, Interest_spot_norm, Land_price_norm,
#                         Natural_environment_norm, Roads_norm, Elevation_norm,
#                         Transmission_line_norm, Urban_area_norm, Wind_speed_norm,
#                         output_data), axis=-1)
# print("Shape of combined data:", combined.shape)

# #remove result from combined, turn into testingNP 
# testingNP = np.delete(combined, -1, axis=2)
# print("Shape of testingNP :", testingNP.shape)

#Split input data(4096x4096x9 into a 256x256x9 array, and store in input_patches, should have 256 array in the list)
input_patches = get_patch(input_data)
#same goes for result
result_patches = get_patch2(result_data)


#Turn the lists into a numpy array 
input_patches_array = np.array(input_patches)
result_patches_array = np.array(result_patches)


#Now split them to training sets 
#training+validation get 80%, whereas testing get 20%
x_train_val, x_test, y_train_val, y_test = train_test_split(input_patches_array, result_patches_array, test_size=0.2, random_state=42)
#Now traning and validation got 80%, we split them into 25%, meaning:
#training 64%, vali 16%, test 20%
x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.25, random_state=42)






























