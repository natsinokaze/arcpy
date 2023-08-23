# coding=utf-8


import arcpy
import os
import numpy

arcpy.env.workspace = "F:\\xiangmu\\LST\\radiation_brightness\\MYD021KM\\new\\Modis_chengdu_nocloud\\32_TIFF_setnull"
max = arcpy.mapping.MapDocument("F:\\learn\\ArcGIS\\notitile.mxd")

lyr = arcpy.mapping.ListLayers(max)
input_directory = "F:\\xiangmu\\LST\\radiation_brightness\\MYD021KM\\new\\Modis_chengdu_nocloud\\32_TIFF_setnull\\"
file_list = os.listdir(input_directory)
output_directory = "F:\\learn\\output\\"
if not os.path.exists(output_directory):
    os.mkdir(output_directory)
file_prefix = '.tiff'
for file_i in file_list:
    if file_i.endswith(file_prefix):
        raster = arcpy.Raster(input_directory + os.path.splitext(file_i)[0] + ".tiff")
        nump = arcpy.RasterToNumPyArray(raster)
        max_data = numpy.max(nump)
        min_data = numpy.min(nump)

        doy = os.path.splitext(file_i)[0]
        year = doy[0:4]
        month = doy[4:6]
        day = doy[6:8]
        # high是2，图层名字是3，lower是0
        title = arcpy.mapping.ListLayoutElements(max, "TEXT_ELEMENT")[0]
        # title.text=str(year)+"年"+str(month)+"月"+str(day)+"日"+"相对绿度结果图"
        # title = arcpy.mapping.ListLayoutElements(max, "TEXT_ELEMENT")[2]
        # title.text = "High : "+str(20)
        # title = arcpy.mapping.ListLayoutElements(max, "TEXT_ELEMENT")[0]
        # title.text = "Low : "+str(10)
        # title = arcpy.mapping.ListLayoutElements(max, "TEXT_ELEMENT")[3]
        # title.text = os.path.splitext(file_i)[0]
        #  listdr=arcpy.mapping.ListDataFrames(max)
        #  lyr=arcpy.mapping.ListLayers(max,"",listdr[1])
        lyr[1].replaceDataSource(arcpy.env.workspace, "RASTER_WORKSPACE", os.path.splitext(file_i)[0] + ".tiff")
        # leg = arcpy.mapping.ListLayoutElements(max, "LEGEND_ELEMENT")[0]
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        arcpy.mapping.ExportToJPEG(max, output_directory + os.path.splitext(file_i)[0] + '_ces.jpg')
