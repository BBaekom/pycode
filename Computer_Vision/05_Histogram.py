import cv2
import numpy as np

def getGrayHistImage(hist):
    _, histMax, _, _ = cv2.minMaxLoc(hist)
    imgHist = np.ones((100, 256), np.uint8) * 255  # 흰색 배경 생성

    for x in range(imgHist.shape[1]):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x,0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)  # 검은색으로 히스토그램 그리기

    return imgHist


def calcGrayHist(img):
    channels = [0]
    histSize = [256]
    histRange = [0, 256]

    # 히스토그램 계산
    hist = cv2.calcHist([img], channels, None, histSize, histRange)
    
    return hist



def histogram_stretching():
    # 이미지 로드
    src = cv2.imread('dust.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    # 이미지의 최소값, 최대값 구하기
    gmin, gmax, _, _ = cv2.minMaxLoc(src)

    # 히스토그램 스트레칭 수행
    alpha = 255.0/(gmax - gmin)  # 스트레칭 계수
    beta = -gmin * 255.0/(gmax - gmin)  # 베타 값

    dst = cv2.convertScaleAbs(src, alpha=alpha, beta=beta)

    # 원본 이미지와 스트레칭된 이미지 히스토그램 계산
    srcHist = calcGrayHist(src)
    dstHist = calcGrayHist(dst)

    # 결과 출력
    cv2.imshow('Source Image', src)
    cv2.imshow('Source Histogram', getGrayHistImage(srcHist))

    cv2.imshow('Stretched Image', dst)
    cv2.imshow('Stretched Histogram', getGrayHistImage(dstHist))

    cv2.waitKey()
    cv2.destroyAllWindows()

def histgoram_equalization():
    src = cv2.imread('dust.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = cv2.equalizeHist(src)

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # histogram_stretching()
    histgoram_equalization()