from PIL import Image

# 이미지 크기 설정
image_width, image_height = 1920, 1080

# 4x4 체커보드 RGB 색상 정의 (빨강, 초록, 파랑, 노랑)
colors_4x4 = [
    (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
]

# 새로운 이미지 생성
img_4x4 = Image.new("RGB", (image_width, image_height))

# 픽셀 값 설정
pixels = img_4x4.load()

# 4x4 체커보드 패턴 반복하여 이미지 채우기
for y in range(image_height):
    for x in range(image_width):
        color_index = (x % 4) + (y % 4) * 4
        pixels[x, y] = colors_4x4[color_index]

# 이미지 저장
img_4x4.save("checkerboard_4x4.png")

# 이미지 출력
img_4x4.show()