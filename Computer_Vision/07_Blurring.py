import cv2

def blurring_mean():
    src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    cv2.imshow('src', src)

    for ksize in range(3, 9, 2):
        dst = cv2.blur(src, (ksize, ksize)) # ksize가 커질수록 블러가 심해짐

        desc = "Mean: %dx%d" % (ksize, ksize)
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()


blurring_mean()