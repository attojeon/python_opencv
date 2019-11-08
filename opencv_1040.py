################################################
# 이미지 정보 알아보기 : shape
#   - 크기 정보
#   - 컬러 정보
#   - image.shape => ( 이미지세로, 이미지가로, 채널수)의 정보
################################################

import cv2

img_color = cv2.imread("./img/beatle.jpg")
img_bw = cv2.imread("./img/4star.jpg")
cv2.imshow("Color Image", img_color)

# 이미지 정보 출력하기
print(">>> Color Image Info : {}".format(img_color.shape))
cv2.waitKey()
cv2.destroyWindow("Color Image")

cv2.imshow("BlackWhite Image", img_bw)
# 이미지 정보 출력하기
print(">>> BlacWhite Image Info : {}".format(img_bw.shape))
cv2.waitKey()
cv2.destroyWindow("BlackWhite Image")

img_gray = cv2.cvtColor(img_bw, cv2.COLOR_BGR2GRAY)
cv2.imshow("Real BW Image", img_gray)
print(">>> Real BW Image Info : {}".format(img_gray.shape))
cv2.waitKey()
cv2.destroyWindow("Real BW Image")