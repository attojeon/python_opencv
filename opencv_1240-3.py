################################################
# 노트북에 설치되어 있는 웹캠의 화면을 보여주기
# 원본-GaussianBlur적용-diff  각각의 프레임 비교해 보기
# 변경된 영역을 추적하여표시해 주기
# 변경된 영역 사각형 표시하기
################################################
import cv2
import numpy as np


cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Applied", cv2.WINDOW_AUTOSIZE)

# Structuring element
es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,4))

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
    ret, thresh = cv2.threshold(diff, 10, 0xff, cv2.THRESH_BINARY)

    # 이미지 확장(dilate)
    dilated = cv2.dilate(thresh, es, iterations=3)

    # 경계표시하기
    # one_frame.copy()를 하여 image ref를 깨고, copy해야 함.
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    dest = cv2.drawContours(one_frame.copy(), contours, -1, (0, 255, 0), 5)
    # print(">>> dest len:{}, {}:".format(len(contours), contours))
    
    for c in contours:
        if cv2.contourArea(c) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(dest, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Original', one_frame)
    cv2.imshow('Applied', gray_frame)
    cv2.imshow("diff", dest)

    previous_frame = gray_frame

    key = cv2.waitKey(25)
    if key == 27 : # Esc key
        break


if cap.isOpened():
    cap.release()

cv2.waitKey()
cv2.destroyAllWindows()