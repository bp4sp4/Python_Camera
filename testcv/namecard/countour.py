# countour.py
# 명함 사진에서 외곽선 검출 처리 테스트

import sys
import random
import numpy as np
import cv2

# 명함 사진 읽어오기
src = cv2.imread('../images/namecard1.jpg')

if src is None:
    print('image read failed...')
    sys.exit()

# 사진을 0.5배 줄이기
src = cv2.resize(src,(0, 0), fx=0.5, fy=0.5)
# 컬러사진을 그레이스케일로 바꾸기
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 읽어온 이미지의 행렬(세로x가로)을 가로(너비), 세로(높이) 값 구함
print('shape : ', src.shape)
h, w = src.shape[:2]
print('w :', w, ', h :', h)

# 3차원 배열 만들기 : 모두 0으로 초기화함
dst1 = np.zeros((h, w, 3), np.uint8) # 외곽선 색상 저장용
dst2 = np.zeros((h, w, 3), np.uint8) # 외곽선 색상 저장용

# 이미지 전처리 : 이진화
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 검출
contours1, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours2, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 외곽선에 색상적용
for i in range(len(contours1)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst1, contours1, i, color, 1)

for i in range(len(contours2)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst2, contours2, i, color, 1)


# 출력 확인
cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()



