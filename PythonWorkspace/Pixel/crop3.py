import os
import glob
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import mapping
import rioxarray as rxr
import geopandas as gpd


crop_extent = gpd.read_file("F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\test.tif")
crop_extent = crop_extent.to_crs(epsg=3857)
os.chdir(os.getcwd() + "/tiffy")
extension = 'tiff'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
tiffs = [rxr.open_rasterio(f) for f in all_filenames]


for tiff_name in all_filenames:
    raster = rxr.open_rasterio(tiff_name)
    # IMPORTANTLY check if have the same crs
    assert crop_extent.crs == raster.rio.crs, "diffrent crs"
    tiff_clipped = raster.rio.clip(crop_extent.geometry.apply(mapping),
                                      # This is needed if your GDF is in a diff CRS than the raster data
                                      crop_extent.crs)
    tiff_clipped.rio.to_raster(tiff_name + 'cropped.tif')
    clipped_chm = rxr.open_rasterio(tiff_name +'cropped.tif')
    f, ax = plt.subplots(figsize=(10, 5))
    clipped_chm.plot.imshow()
    ax.set(title="Chorzow")
    ax.set_axis_off()
    plt.show()