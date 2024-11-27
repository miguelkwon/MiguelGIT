import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 불러오기
    return img

# 2D FFT 변환 (주파수 도메인으로 변환)
def apply_fft(image):
    # 2D 푸리에 변환
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)  # 푸리에 변환 결과를 중앙으로 이동
    magnitude_spectrum = 20 * np.log(np.abs(fshift))  # 주파수 스펙트럼 계산
    return fshift, magnitude_spectrum

# 고역 통과 필터 (High-Pass Filter)를 적용하여 모아레 제거
def remove_moire(fshift, size=30):
    rows, cols = fshift.shape
    crow, ccol = rows // 2 , cols // 2  # 중앙 위치 계산

    # 저주파 성분 제거 (중앙을 잘라냄)
    fshift[crow-size:crow+size, ccol-size:ccol+size] = 0
    
    return fshift

# 2D IFFT (푸리에 변환 후 원본 이미지로 변환)
def apply_ifft(fshift):
    f_ishift = np.fft.ifftshift(fshift)  # 중앙 이동 해제
    img_back = np.fft.ifft2(f_ishift)    # 역 푸리에 변환
    img_back = np.abs(img_back)          # 복소수 부분 제거
    return img_back

# 시각화 함수
def plot_results(original, magnitude_spectrum, result):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    
    # 원본 이미지
    axs[0].imshow(original, cmap='gray')
    axs[0].set_title('Original Image')
    axs[0].axis('off')

    # 푸리에 변환 주파수 스펙트럼
    axs[1].imshow(magnitude_spectrum, cmap='gray')
    axs[1].set_title('Magnitude Spectrum')
    axs[1].axis('off')

    # 모아레 제거된 이미지
    axs[2].imshow(result, cmap='gray')
    axs[2].set_title('Image after Moiré Removal')
    axs[2].axis('off')

    plt.show()

# 이미지 파일 경로
image_path = r"F:\OneDrive - Radiant Vision Systems\02_Miguel_Toy\01_Python\Moirefilter\step01_0300NIT_B064_imgY_Crop.tif"

# 이미지 로드
image = load_image(image_path)

# 2D 푸리에 변환
fshift, magnitude_spectrum = apply_fft(image)

# 모아레 패턴 제거 (저주파 필터링)
fshift_filtered = remove_moire(fshift)

# 역 푸리에 변환
result_image = apply_ifft(fshift_filtered)

# 결과 시각화
plot_results(image, magnitude_spectrum, result_image)
