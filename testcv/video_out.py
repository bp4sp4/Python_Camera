# video_out.py
# 카메라로 찍은 동영상을 저장하기

import sys
import cv2

# 시스템 기본 카메라에 대한 객체 생성
camera = cv2.VideoCapture(0)

if not camera.isOpened():  # 카메라 열기가 실패했다면
    print('camera not opened...')  # 카메라가 없거나, 카메라 드라이버 미설정
    sys.exit()

# 카메라로 촬영한 동영상 저장용 객체 생성
# 입력된 프레임 크기와 동일하게 저장 설정함
w = round(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = round(camera.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# *'DIVX' == 'D', 'I', 'V', 'X'

out = cv2.VideoWriter('./multi/output.avi', fourcc, fps, (w, h))

# 매 프레임 입력과 저장 처리
while True:
    ret, frame = camera.read()  # 다른 앱의 카메라 사용 중지함
    # frame : 읽은 이미지 정보
    # ret   : 읽기 성공(True), 읽기 실패(False)

    if not ret:  # ret 가 False 이면
        break  # 반복 종료

    out.write(frame)  # 파일에 기록

    # edge 만들기
    edge = cv2.Canny(frame, 50, 150)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    # 화면 출력
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(10) == 27:  # esc 키 누르면
        break

# while end

# 자원 해제
camera.release()
out.release()
cv2.destroyAllWindows()

