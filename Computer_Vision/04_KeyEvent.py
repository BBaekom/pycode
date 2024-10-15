import cv2

def func1():
    img = cv2.imread('cat.bmp')
    if img is None:
        print('Image load failed!')
        exit()

    cv2.namedWindow('img')
    cv2.imshow('img', img)
    while True:
        keycode = cv2.waitKey()
        if keycode == ord('i') or keycode == ord('I'):
            img = ~img
            cv2.imshow('img', img)
        elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
            break
    cv2.destroyAllWindows()

img = None

def on_mouse(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2. EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2. EVENT_MOUSEMOVE:
        if flags & cv2. EVENT_FLAG_LBUTTON:
            cv2. line(img, (oldx, oldy), (x, y), (0, 255, 255), 2) 
            cv2. imshow('img', img)
            oldx, oldy = x, y

img = cv2. imread ('cat.bmp')
if img is None:
    print( 'Image load failed!')
    exit()
cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)
cv2.imshow('img', img)
while True:
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.setMouseCallback('img', on_mouse)
        cv2.imshow('img', img)
    elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
        break
cv2.destroyAllWindows()

