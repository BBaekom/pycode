import cv2 as cv
a = cv.imread('cat.bmp', cv.IMREAD_COLOR)
b_resized = cv.imread('wb.png', cv.IMREAD_GRAYSCALE)
c_resized = cv.imread('card.bmp', cv.IMREAD_COLOR)

b = cv.resize(b_resized, (a.shape[1], a.shape[0]))
c = cv.resize(c_resized, (a.shape[1], a.shape[0]))

# A: b 이미지의 흰색 영역을 r 이미지에서 빨간색으로 변경
# r = a.copy(); r[b_resized == 255] = (0, 0, 255)
r = cv.bitwise_or(cv.bitwise_and(a, a, mask=b), cv.bitwise_and(c, c, mask=cv.bitwise_not(b)))

cv.imshow('result', r)
cv.waitKey()
cv.destroyAllWindows()
