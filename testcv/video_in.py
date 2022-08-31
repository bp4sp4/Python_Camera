# video_in
# 동영상 파일 읽어 들이기
# 동영상 파일 읽어 들이기 : 카메라 연결 처리와 코드가 같다.
import sys
import cv2

# 동영상 파일을 읽어들이려면, 카메라 객체 생성과 동일하게
# cv2.VideoCapture 객체를 생성함

cap = cv2.VideoCapture('./multi/vtest.avi')

if not cap.isOpened(): # 동영상 파일이 없다면
    print('video file ope failed...')
    sys.exit()

# 대상 파일이 있다면
# 동영상 해상도 확인
print('file width : ', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('file height : ', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 동영상 프레임 갯수 확인
print('frame count : ', round(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

# 초당 프레임 갯수 : FPS(Frame per Second)
fps = round(cap.get(cv2.CAP_PROP_FPS))
print('fps : ', fps)

# 작동 지연 시간 설정
delay = round(1000 / fps) # delay : 10

# 매 프레임 처리 및 화면 출력
while True:
    ret, frame = cap.read() # 다른 앱에서 카메라 사용중이면 작동 안 됨
    # frame : 동영상 파일에서 일긍ㄴ 프레임 정보 저장
    # ret : 읽기 성공 여부 저장 (True / false)
    
    if not ret: # 읽기가 false 이면
        break # 반복 종료

    # 읽은 프레임을 선 형태로 만들기
    edge = cv2.Canny(frame, 50, 150)
    # cv2.Canny(영상/이미지, x좌표, y좌표)

    # edge 와 frame 출력
    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(delay) == 27: # esc 키 누르면
        break
# while end

# 자원 해제
cap.release()
cv2.destroyAllWindows()
