# -*- coding: utf-8 -*-

#只需要对tif单独批量出图，此代码需将所有待出图的tif数据放入mxd中，且不要包含其他格式的无关数据
import arcpy
import os

mxd = arcpy.mapping.MapDocument(r"F:\test\gis\Batch_plot_test.mxd")
outpath = r"F:\test\gis\output"
df = arcpy.mapping.ListDataFrames(mxd)#获取出图的方框数量
feature_layers = arcpy.mapping.ListLayers(mxd)#获取当前mxd文件中的元素（包括tif和shp）存为list，具体元素为Layer类

tiff_layer=feature_layers[0]

mxd_content=[]
content_dir=[]


for i in range(len(feature_layers)):
    mxd_content.append(str(feature_layers[i].dataSource))
    content_dir.append(os.path.dirname(mxd_content[i]))#获取元素的绝对路径存到list中


content_name=[]
for i in range(len(feature_layers)):
    content_name.append(str(feature_layers[i].datasetName))#获取元素名称包括后缀名存到list中


for i in range(len(feature_layers)):
    # print(mxd_content[i],content_name[i])
    tiff_layer.replaceDataSource(workspace_path=content_dir[i], workspace_type='RASTER_WORKSPACE',
                                 dataset_name=content_name[i])#需要输入三个参数，即元素的路径，元素的类型，元素的名称
    outname = "map_{0}.png".format(i)
    fullpath = os.path.join(outpath, outname)
    arcpy.mapping.ExportToPNG(mxd, fullpath)
    print (i)



print("Finish")