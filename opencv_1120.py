################################################
# 이미지 변환 : 크기
#   - 이미지의 크기 변환
################################################
import cv2
import numpy as np

# 
image = cv2.imread('img/input.jpg')

# 가로/세로 각각 75% 사이즈
image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
cv2.imshow('Scaling - Linear Interpolation', image_scaled) 
cv2.waitKey()

# 가로/세로 두 배 사이즈
img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)
cv2.waitKey()

# 크기 지정
img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled) 
cv2.waitKey()

cv2.destroyAllWindows()