import cv2 as cv
img = cv.imread('cat.bmp', cv.IMREAD_GRAYSCALE)
# img1 = cv.imread('dust.bmp', cv.IMREAD_GRAYSCALE)

#답
img[:img.shape[0]//2, :] = ~img[:img.shape[0]//2, :]
# img1[img1.shape[1]//2:, :] = ~img1[img1.shape[1]//2:, :]

cv.imshow('result', img)
# cv.imshow('result1', img1)
cv.waitKey()
cv.destroyAllWindows()