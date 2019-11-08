################################################
# numpy로 이미지 그리기
#   - numpy의 리스트(배열)을 이해할 수 있다.
#   - 활용하여 그래픽을 처리할 수 있다.
################################################
import cv2
import numpy as np

# 채널이 3개인 이미지
image = np.zeros((512,512,3), np.uint8)

# 채널이 하나 뿐(B/W)인 이미지
image_bw = np.zeros((512,512), np.uint8)

cv2.imshow("Black Rectangle (Color)", image)
cv2.imshow("Black Rectangle (B&W)", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()