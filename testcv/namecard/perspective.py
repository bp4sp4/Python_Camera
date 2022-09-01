# namecard/perspective.py
# 찌그러진 명함을 반드시 사각형으로 변형시키기

import sys
import numpy as np
import cv2

src = cv2.imread('../images/namecard1.jpg')

if src is None:
    print('image read failed...')
    sys.exit()

w, h = 720, 400 # 출력용 크기로 미리 지정함
# 원 소스의 외곽선 좌표에 대한 배열 만들기
# <= 외곽선 좌표 추출 함수를 이용해서 사용함
srcQuard = np.array([[325, 307], [760, 369], [718, 611], [231, 515]],np.float32)
# 최종 완성할 명함 이미지 크기용 배열
dstQuard = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)


# 찌그러진 명함을 반듯한 사각형으로 변형시키기
pers = cv2.getPerspectiveTransform(srcQuard, dstQuard)
dst = cv2.warpPerspective(src, pers, (w, h))

# 출력 확인
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

