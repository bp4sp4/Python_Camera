# video_in
# 동영상 파일 읽어 들이기

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