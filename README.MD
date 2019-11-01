# 이미지 파일의 다양한 형식에 대한 기본 이해가 필요합니다.
## 다음의 개념을 구글링으로 익힙니다.
- 압축이미지 VS 비압축이미지
- 비트맵 이미지
- 이미지의 픽셀
- 이미지 픽셀의 RGB란 무엇인가요?
- jpg 이미지
- png 이미지

# 파이썬으로 이미지, 카메라를 다루기
## OpenCV 기초 배우기

# 설치할 라이브러리 
- Numpy
- Matplotlib
- OpenCV

# 설치 방법
- 쉘에서 pip 또는 pip3 명령어를 사용할 수 있다.
    - $ pip install numpy
    - $ pip install matplotlib
    - $ pip install opencv_python

- pycharm에서 자동 인스톨을 사용할 수 있다.


# OpenCV에서 자주 사용하는 함수
- cv2.imread( filename ) : 이미지 읽기
- cv2.imwrite( filename, img) : 이미지를 파일이름으로 쓰기
- cv2.imshow( window_name, mat ) : 이미지를 지정된 window_name으로 화면에 보이게 한다.
- cv2.waitKey() : 키보드 입력 대기
- cv2.destroyWindow( window_name ) : window_name으로 지정된 이름의 윈도우 화면 닫기
- cv2.destroyAllWindows() : 모든 윈도우 화면 닫기

## 예제
~~~
import cv2

img_file = "./img/ato.jpg"
img = cv2.imread(img_file)
img_gray = cv2.imread(img_file, 0)
cv2.imshow("Ato1", img)
cv2.imshow("Ato2", img_gray)

cv2.waitKey()
cv2.destroyAllWindows()
~~~