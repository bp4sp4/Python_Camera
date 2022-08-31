# camera_in.py
# opencv 로 카메라 작동해서 이미지/영상 입력

import cv2
import sys

# 시스템 기본 카메라로 부터 cv2.VideoCapture 객체 생성
camera = cv2.VideoCapture(0)

if not camera.isOpened():  #카메라 열기가 실패했다면
    print('Camera open failed...') #카메라가 없거나, 카메라 드라이버 미설정
    sys.exit()


print('Camera Open...')
# 카메라 프레임 해상도 확인 출력
print('frame width : ', round(camera.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('frame hiehgt : ', round(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))


# 매 프레임 처리 및 화면 출력
while True:
    ret, frame = camera.read() # 다른 앱에서 카메라 사용중이면 작동 안됨
    # frame : 카메라로 부터 읽은 프레임 정보 저장
    # ret : 읽기 성공 여부 저장 (True / False)
    if not ret: # ret 가 False 이면
        break # 반복 루프 중지함
    # 카메라에서 읽은 프레임 영상 출력용 창 만들기
    edge = cv2.Canny(frame, 50, 150) # 영상 테두리선 표시 처리

    # 창에 출력 처리
    cv2.imshow('frame', frame) # 영상 그대로 출력
    cv2.imshow('edge', edge) # 영상 테두리 보여지는 출력임

    # esc키를 누르면 루프가 종료되게 처리
    if cv2.waitKey(1) == 27: # esc키를 누르면
        break
# while end

# 자원 해제
camera.release()
cv2.destroyAllWindows()



