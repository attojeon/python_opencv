################################################
# 이미지 변환 : 크기
#   - 이미지의 크기 변환
################################################
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

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