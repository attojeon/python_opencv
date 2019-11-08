################################################
# 이미지 컬러 변신, R/G/B 채널 분리하기 1
#   - 다음의 R/G/B 채널 분리하기와 차이점을 이해할 수 있어야 함.
################################################

import cv2

image = cv2.imread('./img/beatle.jpg')

# split함수를 사용하여 이미지를, B/G/R 각각의 채널별 이미지로 분리함.
B, G, R = cv2.split(image)

print(">>> B:{}".format( B.shape ))
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 채널별 값을 합쳐서 다시 원래의 BGR이미지로 ~
merged = cv2.merge([B, G, R]) 
cv2.imshow("Merged", merged) 
cv2.waitKey(0)
cv2.destroyAllWindows()

# Blue 채널만 강조하여 이미지를 보여줌
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged) 
cv2.waitKey(0)
cv2.destroyAllWindows()