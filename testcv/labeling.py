# labeling.py
# 이진화 처리된 이미지에 레이블링 표시하기

import sys
import random
import numpy as np
import cv2

src = cv2.imread('./images/coins.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('image read failed...')

# 읽어온 이미지의 행렬(세로X가로)을 가로(너비), 세로(높이) 값 구함
print('shape : ', src.shape)
h, w = src.shape[:2]  # h = index 0 , w= index 1
print('h : ', h, ', w : ', w)

# 0으로 채워진 2차원배열 3개 만들기
dst1 = np.zeros((h, w, 3), np.uint8)  # 외곽선 색상 저장용
dst2 = np.zeros((h, w, 3), np.uint8)  # 외곽선 색상 저장용
# print('dst1', dst1)
# print('dst2', dst2)

# 이미지 전처리 : 이진화
src = cv2.blur(src, (3, 3))
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)


# 레이블링
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
print('cnt : ', cnt) # 검출된 객체 수
print('labels : ', labels)
print('stats : ', stats)
print('centroids : ', centroids)

# 레이블링 영역에 색상 적용
for i in range(1, cnt):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    dst1[labels == i] = color

# 외곽선 검출
contours, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 외곽선에 색상적용
for i in range(len(contours)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst2, contours, i, color, 1)

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()