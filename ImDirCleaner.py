from glob import glob
import pathlib as Path
from PIL import Image
import os


def ImDirCleaner(directory,treshold):
    files = glob(directory)
    counter = 0
    print('The directory contains ' + str(len(files)) + ' image files.')
    for file in files:
        im=Image.open(file)
        (m,n) = im.size # (width,height) tuple
        im.close()
        if m*n == treshold:
            os.remove(file)
            counter = counter + 1
    print(str(counter)+" files have been deleted.")

Im_dir = 'D:\Downloads\ExtractImagesPdf_TetT8PXt/*.png'
ImDirCleaner(Im_dir,837)