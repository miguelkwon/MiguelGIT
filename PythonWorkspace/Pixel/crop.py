import cv2


'''
    이미지를 자르는 함수
    :param
        img  : 이미지
        x, y : 자를곳 시작 좌표
        w, h : 자를 폭과 길이
'''
def im_trim(img, x, y, w, h):
    imgtrim = img[y: y + h, x: x + w]
    return imgtrim


# 현재경로의 이미지 불러오기
sample = cv2.imread('F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\lena.jpg')
cv2.imshow('org', sample)

# 함수 실행하기
# 원본영상의 자를 영역 원점 x,y좌표 지정. 그리고 새로 생성할 이미지 frame크기 지정
result = im_trim(sample, 200, 200, 300, 300)
cv2.imshow('img', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
