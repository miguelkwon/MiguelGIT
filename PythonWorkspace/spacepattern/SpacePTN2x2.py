from PIL import Image

# 이미지 크기 설정
image_width, image_height = 2752, 2064

# 2x2 체커보드 RGB 색상 정의 (빨강, 초록, 파랑, 노랑)
colors_2x2 = [(0, 255, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

# 새로운 이미지 생성
img_2x2 = Image.new("RGB", (image_width, image_height))

# 픽셀 값 설정
pixels = img_2x2.load()

# 2x2 체커보드 패턴 반복하여 이미지 채우기
for y in range(image_height):
    for x in range(image_width):
        color_index = (x % 2) + (y % 2) * 2
        pixels[x, y] = colors_2x2[color_index]

# 이미지 저장
img_2x2.save(r"F:\OneDrive - Radiant Vision Systems\02_Miguel_Toy\01_Python\spacepattern\checkerboard_2x2.png")

# 이미지 출력
img_2x2.show()
