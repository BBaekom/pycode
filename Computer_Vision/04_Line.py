import numpy as np
import cv2 as cv

img = np.full((400, 400, 3), 255, np.uint8)

cv.line(img, (50, 50), (200, 50), (0, 0, 255))  # 기본 두께의 빨간 선
cv.line(img, (50, 100), (200, 100), (255, 0, 255), 3)  # 두께 3의 보라색 선
cv.line(img, (50, 150), (200, 150), (255, 0, 0), 10)  # 두께 10의 파란색 선 (b, g, r)
# cv.line(image, 시작 좌표, 끝 좌표, 선의 색상, 선의 두께, lineType, shift)


cv.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv.LINE_4)  # 4-connected 빨간 선
cv.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv.LINE_8)  # 8-connected 보라색 선
cv.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv.LINE_AA)  # 안티에일리어싱 파란 선
# LINE_4 는 상하좌우 네 방향으로 픽셀이 연결
# LINE_8 타입의 직선은 픽셀이 대각선 방향으로도 연결
# LINE_AA 는 안티에일리어싱(antialiasing) 기법이 적요오디어 다소 부드럽게 직선이 그어짐

cv.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1)
cv.arrowedLine(img, (50, 250), (350, 250), (255, 0, 255), 1, cv.LINE_AA, 0, 0.07)
cv.arrowedLine(img, (50, 300), (350, 300), (255, 0, 0), 1, cv.LINE_AA, 0, 0.05)

cv.drawMarker(img, (50, 350), (0, 0, 255), cv.MARKER_CROSS)
cv.drawMarker(img, (100, 350), (0, 255, 0), cv.MARKER_TILTED_CROSS)
cv.drawMarker(img, (150, 350), (255, 0, 0), cv.MARKER_STAR)
cv.drawMarker(img, (200, 350), (0, 0, 255), cv.MARKER_DIAMOND)
cv.drawMarker(img, (250, 350), (255, 0, 255), cv.MARKER_SQUARE)
cv.drawMarker(img, (300, 350), (0, 255, 255), cv.MARKER_TRIANGLE_UP)
cv.drawMarker(img, (350, 350), (255, 255, 0), cv.MARKER_TRIANGLE_DOWN)

cv.imshow("img", img)
cv.waitKey()
cv.destroyAllWindows()