import gdal, ogr, osr, time
import numpy as np

from scipy.ndimage import measurements
from skimage import morphology, measure
from skimage.morphology import binary_closing, binary_dilation, binary_erosion, square


def test1():
    inRasterPath = "/home/simulant/ag_lukas/personen/Mostafa/potDH/result1.tif"
    cutRastDatasource = gdal.Open(inRasterPath)
    b11 = cutRastDatasource.GetRasterBand(1)
    
    arr1 = (b11.ReadAsArray()).astype(int)
    
    struct = [[1,1,1],[1,1,1],[1,1,1]]
    label,num_feature = measurements.label(arr1,structure=struct,)
    print(np.amin(num_feature))

if __name__ == "__main__":
    test1()    