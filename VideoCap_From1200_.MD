# 드로이드캠(DroidCam)
- 안드로이드폰에서 사용할 수 있는 웹캠 앱
- 안드로이드 운영체제만 지원

# 드로이드캠 사용법 #1
- 안드로이드폰에서 드로이드캠을 실행하고 설정된 IP, 포트번호를 확인한다.
- mjpegfeed를 사용하여 ViedoCapture 객체 cap을 생성하여 파이썬에서 제어할 수 있다.

# 드로이드캠 사용법 #2
- 참고 url의 글을 참조하여 익힐 수 있습니다.
  https://m.blog.naver.com/PostView.nhn?blogId=bwhang&logNo=220384953881&proxyReferer=https%3A%2F%2Fwww.google.com%2F

# 접속 화면
드로이드 접속 전 화면
[image](./droi1.jpg)
- 드로이드 캠의 IP와 port번호를 잘 기억해야 한다.

드로이드 접속 후 화면 
[image](./droid2.jpg)
- 접속자의 ip번호를 확인할 수 있다.


# 비디오 프레임 캡처에 대한 이해
영화, 게임 등에서 초당 몇 프레임의 성능이 나온다? 는 말을 들어보았을 겁니다. 
우리가 보는 많은 영상들은 모두 초당 수 장 ~ 수 십장의 영상 파일들이 연속적으로 재생되어 자연스러운 움직임을 재생합니다. 그러나 반대로 영상에서 의미 있는 데이터를 얻기 위해서는 매 프레임의 각 이미지 화면들을 분석하고 가공해야 합니다. 이 때 '프레임을 캡처'하는 과정이 필요합니다.
본 과정을 수행하기 위해서는 다음의 용어들을 잘 이해할 필요가 있습니다.
- 비디오 파일 또는 영상카메라
- 비디오의 프레임
- 아날로그 비디오, 디지털 비디오
- 비디오 압축 알고리즘
- 인코딩/디코딩

# 비디오캡처에서 많이 사용하는 함수
- cv2.VideoCapture() : VideoCapture Object 얻기
- cv2.VideoCapture(filename) : VideoCapture Object 얻기
- cv2.VideoCapture(device) : VideoCapture Object 얻기
- cv2.VideoCapture.release() : VideoCapture Object 해제, 위와 쌍을 이룸
- cv2.VideoCapture.read() 또는 cv2.VideoCapture.read(image) : 프레임 얻기
- cv2.VideoCapture.grab() : 프레임 잡기
- cv2.VideoCapture.get(propid) : 비디오 특성 얻기

