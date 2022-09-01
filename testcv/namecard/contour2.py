# namecard/contour2.py
# 읽어온 이미지의 행렬 구하기

import sys
import random
import numpy as np
import cv2

src = cv2.imread('../images/namecard1.jpg')

if src is None:
    print('image read failed...')
    sys.exit()

# 원 소스 이미지 크기 1/2로 줄이기
src = cv2.resize(src, (0,0), fx=0.5, fy=0.5)
# cv2는 이미지 읽어 들일 떄
# BGR => 그레이스케일로 바꾸기
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 읽어온 이미지의 행렬(세로X가로)을 가로(너비), 세로(높이) 값 구함
print('shape : ', src.shape)
h, w = src.shape[:2] # h = index 0 , w= index 1
print('h : ', h, ', w : ',w)

# 0으로 채워진 2차원배열 3개 만들기
dst1 = np.zeros((h, w, 3), np.uint8) # 외곽선 색상 저장용
dst2 = np.zeros((h, w, 3), np.uint8) # 외곽선 색상 저장용

# 이미지 전처리 : 이진화
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 검출 : 외곽선 리스트가 리턴됨
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 외곽선에 대한 객체 처리 => 컨백스 중에서 4각형만 골라냄
# 명함이 4각형임
for i in range(len(contours)):
    # 외곽선 객체를 변수에 저장
    pts = contours[i]

    
    # 외곽선에 색상적용
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst1, contours, i, color, 1)

    
    # 너무 작은 객체는 제외함
    print(i, 'area : ', cv2.contourArea(pts))
    if(cv2.contourArea(pts) < 1000):
        continue # 아래 내용을 생략하고 다음 index로 넘어감
    # 외곽선 근사화(면적이 1000보다 큰 객체만 적용될 것임)
    # 다각형 처리 작업임
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)
    
    # 컨백스가 아니면 제외함
    if not cv2.isContourConvex(approx):
        continue # 컨백스가 아니면 다음 index 로 넘어가게 함

    # 컨백스 중에서 4각형만 골라냄(명함이 4각형임)
    if len(approx) == 4:
        # 외곽선을 그림
        cv2.drawContours(dst2, contours, i, color, 2)
        print('pts :', pts)
# for end
cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()


        