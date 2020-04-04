#!/usr/bin/python

import sys, os
import cv2
import numpy as np
from Inpainter import Inpainter
from InpainterV2 import InpainterV2 as paint

if __name__ == "__main__":
    """
    Usage: python main.py pathOfInputImage pathOfMaskImage [,halfPatchWidth=4].
    """
    if not len(sys.argv) == 3 and not len(sys.argv) == 4:
        print ('Usage: python main.py pathOfInputImage pathOfMaskImage [,halfPatchWidth].')
        exit(-1)
    
    if len(sys.argv) == 3:
        halfPatchWidth = 4
    elif len(sys.argv) == 4:
        try:
            halfPatchWidth = int(sys.argv[3])
        except ValueError:
            print ('Unexpected error:', sys.exc_info()[0])
            exit(-1)
    
    # image File Name
    imageName = sys.argv[1]
    # CV_LOAD_IMAGE_COLOR: loads the image in the RGB format TODO: check RGB sequence
    originalImage = cv2.imread(imageName, cv2.IMREAD_COLOR )
    if originalImage.any() == None:
        print ('Error: Unable to open Input image.')
        exit(-1)
    
    # mask File Name
    maskName = sys.argv[2]
    inpaintMask = cv2.imread(maskName, cv2.IMREAD_GRAYSCALE )
    if inpaintMask.any() == None:
        print ('Error: Unable to open Mask image.')
        exit(-1)
    
    i = paint(originalImage, inpaintMask, halfPatchWidth)
    if i.checkValidInputs() == True:
        i.doInpaint()
        cv2.imwrite("../tests/result.jpg", i.result)
        cv2.namedWindow("result")
        cv2.imshow("result", i.result)
        cv2.waitKey()
    else:
        print ('Error: invalid parameters.')