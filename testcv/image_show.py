# image_show.py
# 이미지 파일 읽어와서 화면 출력

import sys
import cv2

# 이미지(영상) 불러오기
img = cv2.imread('./images/cat.bmp')

if img is None: # 이미지가 없다면
    print('image read failed...')
    sys.exit()

# 이미지가 정상적으로 읽혔다면...
print(type(img))
print(img.shape)

# 화면 출력
cv2.namedWindow('imgshow')
cv2.imshow('imgshow', img)
cv2.waitKey() #키보드 입력이 있을떄까지 기다림

#창 닫기
cv2.destroyAllWindows()