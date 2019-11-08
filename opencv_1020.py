################################################
# 이미지를 다른 파일로 저장하기
################################################

import cv2

img_file = "./img/ancient.jpg"
img = cv2.imread(img_file)
img_gray = cv2.imread(img_file, 0)

print(">>> Image Save and Compression Start ====>")
# 비압축 이미지로 저장
cv2.imwrite("ancient_mine.bmp", img)
print(">>> Image BMP Ended ====>")

# PNG 압축 이미지로 저장, Png Compression 0 ~ 9
cv2.imwrite("ancient_mine.png", img, [cv2.IMWRITE_PNG_COMPRESSION, 4])
print(">>> Image PNG Ended ====>")

# JPG 압축 이미지로 저장, JPG Compression 0 ~ 100%
cv2.imwrite("ancient_mine.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 50])
print(">>> Image JPG Ended ====>")

cv2.destroyAllWindows()