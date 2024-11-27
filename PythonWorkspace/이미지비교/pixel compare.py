# from PIL import Image
# import numpy as np

# # 이미지 불러오기
# def load_image(image_path):
#     return Image.open(image_path)

# # 두 이미지의 정확도를 계산
# def calculate_accuracy(img1, img2):
#     # 이미지가 동일한 크기인지 확인
#     if img1.size != img2.size:
#         raise ValueError("두 이미지의 크기가 다릅니다!")

#     # 이미지를 numpy 배열로 변환
#     img1_np = np.array(img1)
#     img2_np = np.array(img2)

#     # 픽셀이 일치하는지 여부를 계산
#     matches = np.sum(img1_np == img2_np)
    
#     # 전체 픽셀 수 계산
#     total_pixels = img1_np.size

#     # 정확도 계산
#     accuracy = matches / total_pixels
#     return accuracy

# # 이미지 파일 경로
# image1_path = r"F:\OneDrive - Radiant Vision Systems\02_Miguel_Toy\01_Python\이미지비교\img1\checkerboard_2x2.png"
# image2_path = r"F:\OneDrive - Radiant Vision Systems\02_Miguel_Toy\01_Python\이미지비교\img2\checkerboard_2x2.png"

# # 이미지 로드
# img1 = load_image(image1_path)
# img2 = load_image(image2_path)

# # 정확도 계산
# try:
#     accuracy = calculate_accuracy(img1, img2)
#     print(f"두 이미지의 정확도: {accuracy * 100:.2f}%")
# except ValueError as e:
#     print(e)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# 이미지 불러오기
def load_image(image_path):
    return Image.open(image_path)

# 이미지를 픽셀로 변환하여 비교하는 함수
def process_images(img1, img2):
    # 이미지가 동일한 크기인지 확인
    if img1.size != img2.size:
        raise ValueError("두 이미지의 크기가 다릅니다!")

    # 이미지를 numpy 배열로 변환
    img1_np = np.array(img1).astype(np.float32)
    img2_np = np.array(img2).astype(np.float32)

    return img1_np, img2_np

# 두 이미지의 상관 관계(correlation) 계산
def calculate_correlation(img1_np, img2_np):
    # RGB 이미지라면 일차원 배열로 변환 (플랫하게)
    img1_flat = img1_np.flatten()
    img2_flat = img2_np.flatten()

    # 상관 관계 계산 (Pearson 상관 계수)
    corr, _ = pearsonr(img1_flat, img2_flat)
    return corr

# 픽셀 차이 및 상관 관계 시각화
def plot_images_and_correlation(img1_np, img2_np, corr):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # 첫 번째 이미지 출력
    axs[0].imshow(img1_np.astype(np.uint8))
    axs[0].set_title("Image 1")
    axs[0].axis("off")

    # 두 번째 이미지 출력
    axs[1].imshow(img2_np.astype(np.uint8))
    axs[1].set_title("Image 2")
    axs[1].axis("off")

    # Correlation plot: 두 이미지의 픽셀값 비교 (산점도)
    sns.scatterplot(x=img1_np.flatten(), y=img2_np.flatten(), ax=axs[2], alpha=0.3)
    axs[2].set_title(f"Correlation Plot (Pearson: {corr:.2f})")
    axs[2].set_xlabel("Image 1 Pixels")
    axs[2].set_ylabel("Image 2 Pixels")

    # 그래프 보여주기
    plt.tight_layout()
    plt.show()

# 두 이미지의 픽셀 유사도(정확도) 계산
def calculate_pixel_similarity(img1_np, img2_np):
    # 두 이미지의 차이를 절대값으로 계산
    pixel_diff = np.abs(img1_np - img2_np)
    
    # 차이가 없을 때의 픽셀 수 계산
    similarity = np.sum(pixel_diff == 0)
    
    # 전체 픽셀 수 대비 유사도 계산
    total_pixels = img1_np.size
    similarity_ratio = similarity / total_pixels
    
    return similarity_ratio

# 이미지 파일 경로
image1_path = r"F:\OneDrive - Radiant Vision Systems\02_Miguel_Toy\01_Python\이미지비교\img1\step01_0300NIT_B064_imgY_Crop.tif"
image2_path = r"F:\OneDrive - Radiant Vision Systems\02_Miguel_Toy\01_Python\이미지비교\img2\step01_0300NIT_B072_imgY_Crop.tif"

# 이미지 로드
img1 = load_image(image1_path)
img2 = load_image(image2_path)

# 이미지 처리 (픽셀 비교 준비)
try:
    img1_np, img2_np = process_images(img1, img2)

    # 상관 관계 계산
    corr = calculate_correlation(img1_np, img2_np)
    print(f"이미지 상관 관계(Pearson): {corr:.2f}")

    # 픽셀 유사도 계산
    similarity_ratio = calculate_pixel_similarity(img1_np, img2_np)
    print(f"픽셀 유사도: {similarity_ratio * 100:.2f}%")

    # 이미지 및 상관 관계 시각화
    plot_images_and_correlation(img1_np, img2_np, corr)

except ValueError as e:
    print(e)


