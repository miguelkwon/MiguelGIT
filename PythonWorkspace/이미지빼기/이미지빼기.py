
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. 이미지 파일 경로 설정 (사용자가 원하는 경로로 설정)
image1_path = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (2)\step01_0300NIT_G064_imgY_Crop.tif'
image2_path = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (3)\step01_0300NIT_G064_imgY_Crop.tif'

image3_path = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (2)\step01_0300NIT_G432_imgY_Crop.tif'
image4_path = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (3)\step01_0300NIT_G432_imgY_Crop.tif'

# 2. 이미지 열기
image1 = Image.open(image1_path)  # 흑백 변환 ('L' 모드)
image2 = Image.open(image2_path)
image3 = Image.open(image3_path)  # 흑백 변환 ('L' 모드)
image4 = Image.open(image4_path)


# 3. 이미지를 numpy 배열로 변환
arr1 = np.array(image1)
arr2 = np.array(image2)
arr3 = np.array(image3)
arr4 = np.array(image4)

# 4. 두 이미지의 차이 계산
difference1 = np.abs(arr1 - arr2)
difference2 = np.abs(arr3- arr4)

# 5. 일치율 계산
total_pixels = arr1.size  # 전체 픽셀 수
matching_pixels1 = np.sum(difference1 == 0)  # 차이가 0인 픽셀 수
similarity1 = (matching_pixels1 / total_pixels) * 100  # 일치율 계산 (%)
total_pixels = arr1.size  # 전체 픽셀 수
matching_pixels2 = np.sum(difference2 == 0)  # 차이가 0인 픽셀 수
similarity2 = (matching_pixels2 / total_pixels) * 100  # 일치율 계산 (%)


# 6. 시각화 및 일치율 표시
plt.figure(figsize=(15, 5))

# 원본 이미지 1
plt.subplot(2, 3, 1)
plt.title('ResisterPixelsLGD2 - g32')
plt.imshow(arr1, cmap='gray')
plt.axis('off')

# 원본 이미지 2
plt.subplot(2, 3, 2)
plt.title('RegisterPixels_Tablet - g32')
plt.imshow(arr2, cmap='gray')
plt.axis('off')

# 차이 이미지
plt.subplot(2, 3, 3)
plt.title('Difference')
plt.imshow(difference1, cmap='hot')
plt.axis('off')


plt.subplot(2, 3, 4)
plt.title('ResisterPixelsLGD2 - g216')
plt.imshow(arr1, cmap='gray')
plt.axis('off')

# 원본 이미지 2
plt.subplot(2, 3, 5)
plt.title('RegisterPixels_Tablet - g216')
plt.imshow(arr2, cmap='gray')
plt.axis('off')

# 차이 이미지
plt.subplot(2, 3, 6)
plt.title('Difference')
plt.imshow(difference2, cmap='hot')
plt.axis('off')

# 7. 그래프 아래에 일치율 표시
plt.suptitle(f'Similarity: {similarity1:.2f}%', fontsize=16, y=0.05)
plt.suptitle(f'Similarity: {similarity2:.2f}%', fontsize=16, y=1)
plt.tight_layout()
plt.show()
