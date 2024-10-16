import cv2
import numpy as np

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

emboss = np.array([[-1, -1,  0],
                   [-1,  0,  1],
                   [ 0,  1,  1]], np.float32)

dst = cv2.filter2D(src, -1, emboss, delta=128) # 128을 더해야 입체감이 잘 나옴

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()