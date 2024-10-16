import cv2
import numpy as np

def affine_scale():
    src = cv2.imread('rose.bmp')

    if src is None:
        print('Image load failed!')
        return

    dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    dst2 = cv2.resize(src, (1920, 1280))
    dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
    dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1[400:800, 500:900])
    cv2.imshow('dst2', dst2[400:800, 500:900])
    cv2.imshow('dst3', dst3[400:800, 500:900])
    cv2.imshow('dst4', dst4[400:800, 500:900])
    cv2.waitKey()
    cv2.destroyAllWindows()


affine_scale()