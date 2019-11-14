################################################
# 이미지 컬러 변신, R/G/B 채널 분리하기 2
#   - 이전의 R/G/B 채널 분리하기와 차이점을 이해할 수 있어야 함. 
#   - 제로매트릭스를 만들 수 있다.
#   - 제로매트릭스와 R/G/B를 합칠 수 있다.
#   - 각 채널의 색상값을 파일로 저장하기
################################################

import cv2
import numpy as np
import os

image = cv2.imread('./img/raingirl.png')

# split함수를 사용하여 이미지를, B/G/R 각각의 채널별 이미지로 분리함.
B, G, R = cv2.split(image)

# image.shape => ( 이미지세로, 이미지가로, 채널수)에서 
# 이미지의 가로/세로를 모두 0으로 채운 '제로매트릭스'를 만든다.
zeros = np.zeros(image.shape[:2], dtype = "uint8")
zerop = np.zeros(image.shape[:2], dtype = "uint8")
zerop = cv2.copyTo(R, None)

mystr = np.array(zerop)

filename = "red_channel.txt"
if os._exists( filename):
    os.remove(filename)

with open(filename, 'w') as f:
    for r in mystr:
        f.write(np.array2string(r, separator=','))
f.close()


# 제로매트릭스 + R/G/B
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows() 