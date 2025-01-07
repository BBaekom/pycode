import cv2
import numpy as np
import sys

def main(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Image Load Failed!")
        return
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Otsu 이진화를 사용하여 이진 이미지 생성
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    blurred = cv2.GaussianBlur(thresh, (5, 5), 0)
    
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

    # 외곽선을 찾기 위한 함수 호출
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 외곽선을 면적 기준으로 내림차순 정렬
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    # 외곽선 중 사각형(네 꼭짓점)을 찾기
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        if len(approx) == 4:
            # 사각형 외곽선을 찾았을 때
            board_contour = approx
            break
    else:
        # 사각형을 찾지 못했을 때 오류 메시지 출력
        print("Error. Can't find lines of rectangle")
        return
    
    # 찾은 외곽선을 (4, 2) 크기의 배열로 변환
    board_contour = board_contour.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")
    # 좌표 합 계산을 통해 사각형의 꼭짓점 순서 결정
    s = board_contour.sum(axis=1)
    rect[0] = board_contour[np.argmin(s)]  # 좌상단
    rect[2] = board_contour[np.argmax(s)]  # 우하단
    diff = np.diff(board_contour, axis=1)
    rect[1] = board_contour[np.argmin(diff)]  # 우상단
    rect[3] = board_contour[np.argmax(diff)]  # 좌하단
    
    # 투시 변환을 위한 좌표 설정
    pts_src = rect
    width = 500
    height = 500
    pts_dst = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
    
    M = cv2.getPerspectiveTransform(pts_src, pts_dst)
    
    transformed = cv2.warpPerspective(image, M, (width, height))
    
    cv2.imshow("Result", transformed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid Command Line!")
    else:
        main(sys.argv[1])
