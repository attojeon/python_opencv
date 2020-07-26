################################################
# 영상을 아스키코드로 바꾸어 출력함.
################################################

import cv2

CHARS = ' .,-~:;=!*#$@'   # 13
new_width = 100

cap = cv2.VideoCapture('img/ToyStory4.mp4')

print("\x1b[2J", end='')

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape
    new_height = int(h/w * new_width)

    img = cv2.resize(img,  (new_width*2, new_height))

    for row in img:
        for pixel in row: # pixel 0~255 => CHARS 0-12
            idx = int( pixel/255 * (len(CHARS)-1))
            print(CHARS[idx], end = '')
        print()
    print("\x1b[H", end='')

# cv2.imshow("Ato2", img)
# cv2.waitKey()
# cv2.destroyAllWindows() 
