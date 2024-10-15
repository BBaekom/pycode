import cv2

def play_video():
    cap = cv2.VideoCapture('prom.avi')

    if not cap.isOpened():
        print('Video load failed!')
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Video Playback', frame)

        # ESC 키를 누르면 동영상 재생 종료
        if cv2.waitKey(25) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# 동영상 재생 함수 호출
play_video()