import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def on_mouse(event, x, y, flags, param):
    global cnt, src_pts, src
    if event == cv2.EVENT_LBUTTONDOWN:
        if cnt < 4:
            # 선택된 좌표를 src_pts 배열에 저장하고 카운트 증가
            src_pts[cnt, :] = np.array([x, y]).astype(np.float32)
            cnt += 1

            # 선택된 좌표에 빨간색 점을 찍음
            cv2.circle(src, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('src', src)

        # 네 개의 점이 모두 선택되었을 때 실행
        if cnt == 4:
            # 결과 이미지의 너비와 높이 설정
            w = 400
            h = 400

            # 변환 후의 좌표 설정
            dst_pts = np.array([[0, 0],
                                [w - 1, 0],
                                [w - 1, h - 1],
                                [0, h - 1]]).astype(np.float32)

            # 투시 변환 행렬 계산
            pers_mat = cv2.getPerspectiveTransform(src_pts, dst_pts)

            # 투시 변환 적용
            dst = cv2.warpPerspective(src, pers_mat, (w, h))

            cv2.imshow("Result", dst)
            cv2.waitKey(0)
            cv2.destroyWindow("Result")

def main():
    global cnt, src_pts, src
    cnt = 0
    src_pts = np.zeros([4, 2], dtype=np.float32)

    if len(sys.argv) != 2:
        print("Invalid Command Line!")
        sys.exit(1)

    img = sys.argv[1]
    src = cv2.imread(img)

    if src is None:
        print('Image load failed!')
        exit()

    cv2.namedWindow('src')
    cv2.setMouseCallback('src', on_mouse)

    cv2.imshow('src', src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
