################################################
# 이미지 읽고 화면에 보이기
################################################

import cv2

img_file = "./res/king_of_diamonds2.png" 
img = cv2.imread(img_file) 
img_gray = cv2.imread(img_file, 0) 
cv2.imshow("card-color", img) 
cv2.imshow("card-gray", img_gray) 

cv2.waitKey() 
cv2.destroyAllWindows() 