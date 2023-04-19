import cv2
cap = cv2.VideoCapture(1)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,w*2)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
while(1):
    _, frame = cap.read()
    assert _, "摄像头获取失败"
    cv2.imshow('img', frame)
    c = cv2.waitKey(1)
    if c == 27:
        cap.release()
        break
