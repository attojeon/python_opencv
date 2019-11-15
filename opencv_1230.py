################################################
# 유튜브의 영상을 보여주는 프로그램
# 유튜브의 영상을 변형하여 테두리선을 보여주는 프레임 효과 발생
# 사전 필수 사항
#   pip install youtube_dl
#   pip install pafy
################################################
import cv2
import pafy

url = 'https://www.youtube.com/watch?v=zcs3TClPsR8'
video = pafy.new(url)

print(video.title)
print(video.rating)
print(video.duration)

best = video.getbest()
print(best.resolution)

cap = cv2.VideoCapture(best.url)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('My Frame', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow('edges', edges)

    key = cv2.waitKey(25)
    if key == 27 : # Esc key
        break


if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()