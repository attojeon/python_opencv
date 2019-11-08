################################################
# 이미지 읽고 화면에 보이기
################################################

import cv2

img_file = "./img/ancient.png"
img = cv2.imread(img_file)
img_gray = cv2.imread(img_file, 0)
cv2.imshow("Ato1", img)
cv2.imshow("Ato2", img_gray)

cv2.waitKey()
cv2.destroyAllWindows()