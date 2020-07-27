################################################
# 노트북에 설치되어 있는 웹캠의 화면을 보여주기
# 원본-GaussianBlur적용-diff  각각의 프레임 비교해 보기
################################################
import cv2
import numpy as np


cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Applied", cv2.WINDOW_AUTOSIZE)

cap = cv2.VideoCapture(0)

frame_size = ( int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(frame_size)

previous_frame = None

while True:
    ret, one_frame = cap.read()

    if not ret:
        break

    gray_frame = cv2.resize(one_frame, (640, 480))
    gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if previous_frame is None:
        previous_frame = gray_frame
        continue
    diff = cv2.absdiff(gray_frame, previous_frame)

    # 경계값을 활용하여 binalization을 실행할 수 있는 다양한 옵션 있음. 
    # 참고 url https://m.blog.naver.com/samsjang/220504782549 
    ret, thresh = cv2.threshold(diff, 10, 0xff, cv2.THRESH_OTSU)

    cv2.imshow('Original', one_frame)
    cv2.imshow('Applied', gray_frame)
    cv2.imshow("diff", thresh)

    previous_frame = gray_frame

    key = cv2.waitKey(25)
    if key == 27 : # Esc key
        break


if cap.isOpened():
    cap.release()

cv2.waitKey()
cv2.destroyAllWindows()