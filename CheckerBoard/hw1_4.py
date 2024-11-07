import cv2
import numpy as np

# 입력 이미지를 그레이스케일로 변환하고, 이진화 및 가우시안 블러를 적용
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blurred = cv2.GaussianBlur(thresh, (5, 5), 0)
    return blurred

# 가장 큰 사각형 윤곽선을 찾고, 그 윤곽선을 반환
def find_board_contour(edges):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)  
        approx = cv2.approxPolyDP(contour, epsilon, True)  
        
        if len(approx) == 4:  
            return approx

    print("Error. Can't find rectangle!")
    return None

# 투시 변환을 수행하는 함수
def get_perspective_transform(image, board_contour):
    board_contour = board_contour.reshape(4, 2) 
    rect = np.zeros((4, 2), dtype="float32")
    s = board_contour.sum(axis=1)
    rect[0] = board_contour[np.argmin(s)]  
    rect[2] = board_contour[np.argmax(s)] 
    diff = np.diff(board_contour, axis=1)
    rect[1] = board_contour[np.argmin(diff)] 
    rect[3] = board_contour[np.argmax(diff)] 

    width = 500  
    height = 500 
    pts_dst = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])

    M = cv2.getPerspectiveTransform(rect, pts_dst)  
    transformed = cv2.warpPerspective(image, M, (width, height)) 
    return transformed


# 원근 변환된 이미지에서 원을 검출
def detect_circles(transformed):
    transformed_gray = cv2.cvtColor(transformed, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
    circles = cv2.HoughCircles(
        transformed_gray, cv2.HOUGH_GRADIENT, dp=1.2,  # 허프 원 변환을 사용하여 원 검출
        minDist=40, param1=50, param2=30, minRadius=10, maxRadius=30
    )
    return circles

# 검출된 원을 기준으로 흰색과 검은색 말의 개수 세는 함수
def count_pieces(transformed, circles):
    light_circles = 0
    dark_circles = 0

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int") 
        for (x, y, r) in circles:
            piece_color = transformed[y, x]  
            if np.mean(piece_color) > 128:  
                # 밝은 경우 흰색으로 분류
                light_circles += 1
            else:  
                # 어두운 경우 검은색으로 분류
                dark_circles += 1
            cv2.circle(transformed, (x, y), r, (0, 255, 0), 2)  

    return light_circles, dark_circles


def main(img):
    image = cv2.imread(img) 
    if image is None:
        print("Image Load Failed!")
        return None

    blurred = preprocess_image(image) 
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)  

    board_contour = find_board_contour(edges)  
    if board_contour is None:
        return

    transformed = get_perspective_transform(image, board_contour) 

    circles = detect_circles(transformed)
    light_circles, dark_circles = count_pieces(transformed, circles)

    print(f"White pieces: {light_circles}, Black pieces: {dark_circles}") 
    cv2.imshow("Result", transformed) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Invalid Command Line!")
    else:
        main(sys.argv[1])
