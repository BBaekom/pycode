import cv2

src = cv2.imread('dust.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    exit()

cv2.imshow('src', src)

for sigma in range(1, 6):
    blurred = cv2.GaussianBlur(src, (0, 0), sigma)

    alpha = 1.0
    dst = cv2.addWeighted(src, 1 + alpha, blurred, -alpha, 0.0)

    desc = "sigma: %d" % sigma
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()

# # 기본적인 filter2D 사용 예시
# import cv2
# import numpy as np

# # 이미지 불러오기
# img = cv2.imread('cat.bmp')

# # 샤프닝 커널 정의
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)

# # filter2D 함수로 필터링 수행
# sharpened_img = cv2.filter2D(img, -1, kernel)

# # 결과 출력
# cv2.imshow('Sharpened Image', sharpened_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()