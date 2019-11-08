################################################
# numpy로 대각선 그리기
#   - 대각선 그리기
################################################
import cv2
import numpy as np

# 대각선 그리기
image = np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,0), (511,511), (255,127,0), 5)
cv2.imshow("Blue Line", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

################################################
# numpy로 내부에 사각형 그리기
################################################
import cv2
import numpy as np

image = np.zeros((512,512,3), np.uint8)

cv2.rectangle(image, (100,100), (300,250), (127,50,127), -1)
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


################################################
# numpy로 내부에 원형 그리기
################################################
import cv2
import numpy as np

image = np.zeros((512,512,3), np.uint8)

cv2.circle(image, (350, 350), 100, (15,75,50), -1) 
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()