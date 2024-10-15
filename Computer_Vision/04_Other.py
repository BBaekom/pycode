import cv2
import numpy as np

def useful_func():
    img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('Image load failed!')
        return

    sum_img = np.sum(img)
    mean_img = np.mean(img, dtype=np.int32)
    print('Sum:', sum_img)
    print('Mean:', mean_img)


# useful_func()

def num():
    img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

    minVal, maxVal, minPos, maxPos = cv2.minMaxLoc(img)

    print('minVal is', minVal, 'at', minPos)
    print('maxVal is', maxVal, 'at', maxPos)


num()