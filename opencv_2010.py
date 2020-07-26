################################################
# 사진을 아스키코드로 바꾸어 출력함.
################################################

import cv2

CHARS = ' .,-~:;=!*#$@'   # 13
new_width = 100

img = cv2.imread('./img/ato.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = img.shape
new_height = int(h/w * new_width)
print("h:{}, w:{}, nh:{}".format(h, w, new_height))

img = cv2.resize(img,  (new_width*2, new_height))

for row in img:
    for pixel in row: # pixel 0~255 => CHARS 0-12
        #idx = int( pixel/255 * (len(CHARS)-1))
        idx = int( pixel/256 * len(CHARS))
        print(CHARS[idx], end = '')
    print()

# cv2.imshow("Ato2", img)
# cv2.waitKey()
# cv2.destroyAllWindows() 
