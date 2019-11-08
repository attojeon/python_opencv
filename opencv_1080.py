################################################
# 이미지 컬러 변신 : 히스토그램 표시하기
#   - 히스토그램을 이해할 수 있다.
#   - R/G/B 채널별 히스토그램을 표시해 본다.
################################################
'''
cv2.calcHist(images, channels, mask, histSize, ranges[, hist, accumulate])
    images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "img".
    channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is 0. For color image, you can pass 0, 1 or 2 to calculate histogram of blue, green or red channel respectively.
    mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
    histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass 256.
    ranges : this is our RANGE. Normally, it is 0,256.
'''

import cv2
import numpy as np

# 그래프를 그리기 위한 파이썬 라이브러리! 그 유명한 matplotlib
from matplotlib import pyplot as plt

image = cv2.imread('./img/monalisa.jpg')

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# B채널의 그래프를 표시함
plt.plot(histogram)
plt.show()

# B채널의 그래프를 면적으로 변환하여 표시함
plt.hist(image.ravel(), 256, [0, 256])
plt.show()

# B/G/R 모든 채널을 표시하기 위하여 ~
color = ('b', 'g', 'r')

# BGR별로 히스토그램을 계산함.
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])  # left/right limit 설정, [0,256] => 좌우로 화면 꽉 채우는 효과
    
plt.show()