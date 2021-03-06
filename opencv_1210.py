################################################
# 인터넷에 드로이드캠을 실행
# 드로이드캠의 영상을 캡쳐하여 보여주기
################################################
import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('http://192.168.1.80:4747/video')

frame_size = ( int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(frame_size)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('My Frame', frame)

    key = cv2.waitKey(25)
    if key == 27 : # Esc key
        break


if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()