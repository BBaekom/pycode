import cv2 as cv
import numpy as np

def func1():
    img1 = cv.imread('cat.bmp', cv.IMREAD_COLOR)

    if img1 is None:
        print('Image laod failed!')
        exit()

    print('type(img1):', type(img1))
    print('img1.shape:', img1.shape)

    if len(img1.shape) == 2:
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is a truecolor image')

    cv.imshow('img1', img1)
    cv.waitKey()
    cv.destroyAllWindows()\
    

def func2():
    img1 = np.empty((48, 64), np.uint8)  # 480x640 크기의 빈 그레이스케일 이미지 (8비트 정수)
    img2 = np.zeros((48, 64, 3), np.uint8)  # 480x640 크기의 3채널(컬러) 이미지, 모든 값은 0
    img3 = np.ones((48, 64), np.int32)  # 480x640 크기의 1로 채워진 행렬 (32비트 정수)
    img4 = np.full((48, 64), 0, np.float32)  # 480x640 크기의 0으로 채워진 행렬 (32비트 부동소수점)
    
    mat1 = np.array([[11, 12, 13, 14],
                    [21, 22, 23, 24],
                    [31, 32, 33, 34]]).astype(np.uint8)
    mat1[0, 1] = 100  # 첫 번째 행, 두 번째 열의 값을 100으로 변경
    mat1[2, :] = 200  # 세 번째 행의 모든 값을 200으로 변경
    print(mat1)


def func3():
    img1 = cv.imread('cat.bmp')

    img2 = img1
    img3 = img1.copy()

    img1[:, :] = (0, 255, 255)

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()


def func4():
    img1 = cv.imread('cat.bmp', cv.IMREAD_GRAYSCALE)

    img2 = img1[150:300, 150:300]
    img3 = img1[150:300, 150:300].copy()

    img2 += 30

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()


def func6():
    mat1 = np.ones((3,4), np.int32)
    mat2 = np.arange(12).reshape(3,4)
    mat3 = mat1 + mat2
    mat4 = mat2 * 2

    print("mat1:")
    print(mat1)
    print("mat2:")
    print(mat2)
    print("mat3:")
    print(mat3)
    print("mat4:")
    print(mat4)


# func1()
# func2()
# func3()
# func4()
func6()

