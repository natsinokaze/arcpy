# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# model1.py
# Created on: 2022-03-21 18:40:00.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
import os

# Local variables:

input_fy_dir='F:\\xiangmu\\LST\\radiation_brightness\\MOD021KM\\FY\\rad13_glt_setnull\\'
input_modis_dir='F:\\xiangmu\LST\\radiation_brightness\\MOD021KM\\Modis\\band32\\tiff_setnull\\'
output_dir = 'F:\\xiangmu\\LST\\radiation_brightness\\MOD021KM\\MODIS\\Minus\\band32_\\'

fy_list=os.listdir(input_fy_dir)
modis_list=os.listdir(input_modis_dir)
file_n=len(fy_list)

for file_i in range(file_n):
    FY12_2020_0110_1900_tiff = input_fy_dir+fy_list[file_i]
    MYD31_2020_01_10_1905_tiff = input_modis_dir+modis_list[file_i]  # type: str
    v01_tif = output_dir+os.path.splitext(fy_list[file_i])[0] + ".tif"
    # v01_tif__2_ = "F:\\xiangmu\\LST\\radiation_brightness\\MYD021KM\\Modis\\Minus\\band31\\set0\\"+os.path.splitext(fy_list[file_i])[0]+ ".tif"
    # Process: Minus
    arcpy.gp.Minus_sa(FY12_2020_0110_1900_tiff, MYD31_2020_01_10_1905_tiff, v01_tif)

    # Process: Raster Calculator
    # a=os.path.splitext(fy_list[file_i])[0]+ ".tif"
    # arcpy.gp.RasterCalculator_sa("(\"%a%\" > 0) * \"%a%\"", v01_tif__2_)
    # arcpy.gp.RasterCalculator_sa("(\"%01.tif%\" > 0) * \"%01.tif%\"", v01_tif__2_)




