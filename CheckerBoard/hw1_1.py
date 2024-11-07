import sys
import cv2
import numpy as np

# 체커보드 코너를 탐지하는 함수 정의
def detect_checkerboard_corners(img):
    img = cv2.imread(img)
    if img is None:
        print("Image Load Failed!")
        sys.exit(1)

    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 그레이스케일 이미지에 가우시안 블러 적용
    blurred_gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Canny Edge Detection을 사용해 이미지의 edge 검출
    edges = cv2.Canny(blurred_gray, 50, 150)

    height, width = gray.shape
    # 관심 영역(ROI) 설정을 위해 여백 비율 정의
    roi_margin = 0.1 
    roi_x1 = int(roi_margin * width)
    roi_y1 = int(roi_margin * height)
    roi_x2 = int((1 - roi_margin) * width)
    roi_y2 = int((1 - roi_margin) * height)
    
    # 허프 변환을 사용하여 직선 검출
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)
    if lines is not None:
        # 검출된 각 직선을 반복하여 이미지에 그리기
        for rho, theta in lines[:, 0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            # 직선의 시작점과 끝점 계산
            x1 = int(np.round(x0[0])) if isinstance(x0, np.ndarray) else int(np.round(x0))
            y1 = int(np.round(y0[0])) if isinstance(y0, np.ndarray) else int(np.round(y0))
            x2 = int(np.round(x0[0] - 1000 * (-b))) if isinstance(x0, np.ndarray) else int(np.round(x0 - 1000 * (-b)))
            y2 = int(np.round(y0[0] + 1000 * (a))) if isinstance(y0, np.ndarray) else int(np.round(y0 + 1000 * (a)))
            # 직선이 ROI 내에 있는 경우에만 그리기
            if (roi_x1 <= x1 <= roi_x2 and roi_y1 <= y1 <= roi_y2 and
                roi_x1 <= x2 <= roi_x2 and roi_y1 <= y2 <= roi_y2):
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    corners = []
    # 코너 간 최소 거리 설정
    min_distance = 30 

    # 새로운 코너가 기존 코너들과 충분히 떨어져 있는지 확인하는 함수 정의
    def is_close_to_existing(x0, y0, corners, min_distance):
        for (cx, cy) in corners:
            if np.sqrt((x0 - cx) ** 2 + (y0 - cy) ** 2) < min_distance:
                return True
        return False

    # 허프 변환으로 검출된 선들 간의 교차점 찾기
    if lines is not None:
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                line1 = lines[i][0]
                line2 = lines[j][0]
                rho1, theta1 = line1
                rho2, theta2 = line2
                
                # 두 선이 평행하지 않은 경우 교차점 계산
                if abs(theta1 - theta2) > 1e-3:
                    A = np.array([[np.cos(theta1), np.sin(theta1)], [np.cos(theta2), np.sin(theta2)]])
                    B = np.array([[rho1], [rho2]])
                    try:
                        # 두 선의 교차점 좌표 계산
                        x0, y0 = np.linalg.solve(A, B)
                        x0, y0 = int(np.round(x0[0])), int(np.round(y0[0])) if x0.ndim > 0 else (int(np.round(x0)), int(np.round(y0)))
                        # 교차점이 관심 영역 내에 있고, 기존 코너와 충분히 떨어져 있는 경우 리스트에 추가
                        if (roi_x1 <= x0 <= roi_x2 and roi_y1 <= y0 <= roi_y2 and
                            not is_close_to_existing(x0, y0, corners, min_distance)):
                            corners.append((x0, y0))
                    except np.linalg.LinAlgError:
                        pass
    
    # 최종 코너 리스트에서 중복된 점들을 필터링
    filtered_corners = []
    for corner in corners:
        if not is_close_to_existing(corner[0], corner[1], filtered_corners, min_distance):
            filtered_corners.append(corner)
            # 필터링된 코너를 이미지에 빨간 점으로 표시
            cv2.circle(img, (corner[0], corner[1]), 5, (0, 0, 255), -1)

    # 탐지된 코너의 수를 기반으로 체커보드의 크기를 판단하여 출력
    if len(filtered_corners) >= 90:
        print("Detected Checkerboard: 10x10")
    else:
        print("Detected Checkerboard: 8x8")

    cv2.imshow('Image Window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid Command Line!")
        sys.exit(1)

    img = sys.argv[1]
    detect_checkerboard_corners(img)
