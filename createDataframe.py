# -*- coding: utf-8 -*-
import geopandas as gpd
import rasterio as rio
import numpy as np
from osgeo import gdal
import pandas as pd
import matplotlib.pyplot as plt

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

#Preparing output data
Suitable = rio.open(r'C:\Users\jiunc\OneDrive\Desktop\FYP\Tsukuba data\square data\2SquareResult.tif')
Suitable_data = Suitable.read(1)
print("Suitable location for wind farm:", np.unique(Suitable_data)) 
plt.imshow(Suitable_data, cmap = None)
plt.title("suitable") 



