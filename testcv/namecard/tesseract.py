import sys
import numpy as np
import cv2
import pytesseract

# 사용자 정의 함수 작성 ------------------------
def reorderPts(pts):
    # 전달된 도형 정보를 이용해서 4꼭지점 좌표값 구해서 리턴
    idx = np.lexsort((pts[:, 1], pts[:, 0]))
    # 컬럼 0 --> 컬럼 1 순으로 정렬한 인덱스를 리턴 받음

    pts = pts[idx] # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts
# ---------------------------------------------------------------------------

filename = '../images/namecard1.jpg'

# exe 파일 실행시, 파일명려엉 뒤에 파일명이 전달이 오면...
if len(sys.argv) > 1: # 프롬프트> tesseract ncard2.jpg
    filename = sys.argv[1] # 전달온 파일명을 변수에 대입함

src = cv2.imread(filename)

if src is None:
    print('image read failed...')
    sys.exit()

# 출력 영상 설정
w, h = 720, 400
# 명함 4꼭지점 좌표 저장용 배열 만들기
# 순서 : lt, lb, rb, rt
srcQuad = np.array([[0,0], [0,0], [0,0], [0,0]], np.float32)
dstQuad= np.array([[0, 0], [0, h], [w, h], [w,0]], np.float32)

# 외곽선 색상 저장용 배열 만들기 : 전체 0으로 초기화함
dst = np.zeros((h, w), np.uint8)

# 이미지 전처리 : 이진화
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
th, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 검출
contours, _= cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for pts in contours:
    # 너무 작은 객체는 제외함
    if (cv2.contourArea(pts) < 10):
        continue  # 아래 내용을 생략하고 다음 객체로 넘어감
        
    # 외곽선 근사화(면적이 10보다 큰 객체만 적용될 것임)
    # 다각형 처리 작업임
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)

    # 컨백스가 아니거나 제외함
    if not cv2.isContourConvex(approx) or len(approx) != 4:
        continue  # 다음 객체로 넘어가게 함

    # 외곽선을 그림
    cv2.polylines(src, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    # 원본 이미지의 4꼭지점의 좌표값 획득
    srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))

    # 찌그러진 명함을 반듯한 사각형으로 변형시키기
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst =


    # 명함에서 글자 추출하기

# for end