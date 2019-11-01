################################################
# 이미지 읽고 화면에 보이기
################################################

import cv2

img_file = "./img/ancient_sm.jpg"
img_bgr = cv2.imread(img_file)
img_rgb = cv2.imread(img_file, cv2.COLOR_BGR2RGB)
cv2.imshow("Ato1", img_bgr)
cv2.imshow("Ato2", img_rgb)

cv2.waitKey()
cv2.destroyAllWindows()