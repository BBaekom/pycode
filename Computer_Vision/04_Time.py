import cv2
import numpy as np

def time_inverse():
    src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    dst = np.empty(src.shape, dtype=src.dtype)

    tm = cv2.TickMeter()
    tm.start()

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = 255 - src[y, x]

    tm.stop()
    print('Image inverse implementation took %4.3f ms.' % tm.getTimeMilli())

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def time_inverse_numpy():
    src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    tm = cv2.TickMeter()
    tm.start()

    # numpy 연산을 이용한 영상 반전
    dst = ~src

    tm.stop()
    print('Image inverse (numpy) took %4.3f ms.' % tm.getTimeMilli())

    cv2.imshow('src', src)
    cv2.imshow('dst_numpy', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


time_inverse()

time_inverse_numpy()