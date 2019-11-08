################################################
# 이미지 변환 : Translation
#   - 이미지의 시작 위치 옮기기
#   - 가로/세로 1/4씩 이동시키기
################################################
import cv2
import numpy as np

image = cv2.imread('img/input.jpg')
cv2.imshow("Original Image", image)
cv2.waitKey()
cv2.destroyWindow("Original Image")

# image.shape => (이미지 세로, 이미지 가로, 채널수)
# 이미지 세로/가로 정보만 가져옴.
height, width = image.shape[:2]

#
quarter_height, quarter_width = height/4, width/4

# 어려운 고등수학 행렬
# Tx, Ty는 변환(Translation 연산방법이라는 것만 이해하자.)
#       | 1 0 Tx |
#  T  = | 0 1 Ty |

# T 는 이미지가 변환된 행렬임.
T = np.float32([[1, 0, quarter_width], [0, 1,quarter_height]])
print(T)
# T와 매트릭스를 이용해서 변환하는 함수, warpAffine(워파인)
img_translation = cv2.warpAffine(image, T, (width, height))
t_h, t_w = img_translation.shape[:2]
cv2.imshow('Translation', img_translation)

cv2.waitKey()
cv2.destroyAllWindows()