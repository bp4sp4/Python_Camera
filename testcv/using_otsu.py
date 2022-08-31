# using_otsu.py
# 명함 사진 이용 >> 흑백이미지로 변환

import cv2
import sys

filenames = ['./images/namecard1.jpg', './images/namecard2.jpg','./images/namecard3.jpg']

for fname in filenames:
    # 이미지 파일을 컬러모드로 읽기
    src = cv2.imread(fname, cv2.IMREAD_COLOR)

    if src is None:
        print('image read failed...')
        sys.exit()

    # 이미지 크기 조정하기
    src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    # 이미지 그레이스케일로 변경하기
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    # 그레이스 케일을 흑백 이미지로 바꿈
    th, dst = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print('threshold : ', th) # 흑백 변환 한계점

    # 출력 확인
    cv2.imshow('src', src)
    cv2.imshow('src_gray', src_gray)
    cv2.imshow('dst', dst)
    cv2.waitKey()

# close for
cv2.destroyAllWindows()