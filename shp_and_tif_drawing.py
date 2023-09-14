# -*- coding: utf-8 -*-

#批量出图，对应矢量覆盖在栅格上同时出图的情况，mxd中只需放入一组样本即可（shp在上栅格在下），此代码以每组一个shp一个栅格为例，具体情况具体修改
import arcpy
import os

mxd = arcpy.mapping.MapDocument(r"F:\test\gis\Batch_plot_test.mxd")
outpath = r"F:\test\gis\output"
shp_dir=r'F:\test\gis\shp'
tif_dir=r'F:\test\gis\tif'

shpdir_all_name=os.listdir(shp_dir)
shp_name=[]
for name in shpdir_all_name:
    if name.endswith(".shp"):
        file_name,ext=name.split('.')#后续shp_layer.replaceDataSource中的dataset_name=shp_name[i]不能包含后缀名！！！所有得去掉.shp后缀（但是tif则可以）
        shp_name.append(file_name)

tifdir_all_name=os.listdir(tif_dir)
tif_name=[]
for name in tifdir_all_name:
    if name.endswith(".tif"):
        tif_name.append(name)

df = arcpy.mapping.ListDataFrames(mxd)#获取出图的方框数量
feature_layers = arcpy.mapping.ListLayers(mxd)#获取当前mxd文件中的元素（包括tif和shp）存为list，具体元素为Layer类

shp_layer=feature_layers[0]#获取shp样本
tiff_layer=feature_layers[1]#获取tif样本


for i in range(len(shp_name)):
    # print(mxd_content[i],content_name[i])
    print (shp_dir,shp_name[i])
    print (tif_dir, tif_name[i])
    shp_layer.replaceDataSource(workspace_path=shp_dir, workspace_type='SHAPEFILE_WORKSPACE',
                                 dataset_name=shp_name[i])
    tiff_layer.replaceDataSource(workspace_path=tif_dir, workspace_type='RASTER_WORKSPACE',
                                 dataset_name=tif_name[i])#需要输入三个参数，即元素的路径，元素的类型，元素的名称
    outname = "map_{0}.png".format(i)
    fullpath = os.path.join(outpath, outname)
    arcpy.mapping.ExportToPNG(mxd, fullpath)
    print (i)



print("Finish")