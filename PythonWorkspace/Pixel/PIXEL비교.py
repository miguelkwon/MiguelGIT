import cv2
import numpy as np

def compare_images1(image1_path, image2_path):
    # 이미지 불러오기
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images2(image3_path, image4_path):
    # 이미지 불러오기
    image1 = cv2.imread(image3_path)
    image2 = cv2.imread(image4_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images3(image5_path, image6_path):
    # 이미지 불러오기
    image1 = cv2.imread(image5_path)
    image2 = cv2.imread(image6_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images4(image7_path, image8_path):
    # 이미지 불러오기
    image1 = cv2.imread(image7_path)
    image2 = cv2.imread(image8_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images5(image9_path, image10_path):
    # 이미지 불러오기
    image1 = cv2.imread(image9_path)
    image2 = cv2.imread(image10_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images6(image11_path, image12_path):
    # 이미지 불러오기
    image1 = cv2.imread(image11_path)
    image2 = cv2.imread(image12_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images7(image13_path, image14_path):
    # 이미지 불러오기
    image1 = cv2.imread(image13_path)
    image2 = cv2.imread(image14_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images8(image15_path, image16_path):
    # 이미지 불러오기
    image1 = cv2.imread(image15_path)
    image2 = cv2.imread(image16_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images9(image17_path, image18_path):
    # 이미지 불러오기
    image1 = cv2.imread(image17_path)
    image2 = cv2.imread(image18_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images10(image19_path, image20_path):
    # 이미지 불러오기
    image1 = cv2.imread(image19_path)
    image2 = cv2.imread(image20_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images11(image21_path, image22_path):
    # 이미지 불러오기
    image1 = cv2.imread(image21_path)
    image2 = cv2.imread(image22_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images12(image23_path, image24_path):
    # 이미지 불러오기
    image1 = cv2.imread(image23_path)
    image2 = cv2.imread(image24_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images13(image25_path, image26_path):
    # 이미지 불러오기
    image1 = cv2.imread(image25_path)
    image2 = cv2.imread(image26_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images14(image27_path, image28_path):
    # 이미지 불러오기
    image1 = cv2.imread(image27_path)
    image2 = cv2.imread(image28_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images15(image29_path, image30_path):
    # 이미지 불러오기
    image1 = cv2.imread(image29_path)
    image2 = cv2.imread(image30_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images16(image31_path, image32_path):
    # 이미지 불러오기
    image1 = cv2.imread(image31_path)
    image2 = cv2.imread(image32_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images17(image33_path, image34_path):
    # 이미지 불러오기
    image1 = cv2.imread(image33_path)
    image2 = cv2.imread(image34_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
def compare_images18(image35_path, image36_path):
    # 이미지 불러오기
    image1 = cv2.imread(image35_path)
    image2 = cv2.imread(image36_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity
    # 이미지 불러오기
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # 이미지 크기 조정
    image1 = cv2.resize(image1, (2752, 2064))
    image2 = cv2.resize(image2, (2752, 2064))

    # 이미지를 그레이스케일로 변환
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity


image1_path = r'd:\NewImageName.bmp'
# image3_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\R384_10B.tif'
# image5_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\R72_10B.tif'
# image7_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\R64_10B.tif'
# image9_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\G432_10B.tif'
# image11_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\G384_10B.tif'
# image13_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\G72_10B.tif'
# image15_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\G64_10B.tif'
# image17_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\B432_10B.tif'
# image19_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\B384_10B.tif'
# image21_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\B72_10B.tif'
# image23_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\B64_10B.tif'
# image25_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\R24_10B.tif'
# image27_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\R20_10B.tif'
# image29_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\G24_10B.tif'
# image31_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\G20_10B.tif'
# image33_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\B24_10B.tif'
# image35_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3\InputIMG\B20_10B.tif'



image2_path = r'd:\NewImageName2.bmp'
# image4_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_R384_imgY_Crop.tif'
# image6_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_R072_imgY_Crop.tif'
# image8_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_R064_imgY_Crop.tif'
# image10_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_G432_imgY_Crop.tif'
# image12_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_G384_imgY_Crop.tif'
# image14_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_G072_imgY_Crop.tif'
# image16_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_G064_imgY_Crop.tif'
# image18_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_B432_imgY_Crop.tif'
# image20_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_B384_imgY_Crop.tif'
# image22_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_B072_imgY_Crop.tif'
# image24_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step01_0300NIT_B064_imgY_Crop.tif'
# image26_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step02_0300NIT_R024_imgY_Crop.tif'
# image28_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step02_0300NIT_R020_imgY_Crop.tif'
# image30_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step02_0300NIT_G024_imgY_Crop.tif'
# image32_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step02_0300NIT_G020_imgY_Crop.tif'
# image34_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step02_0300NIT_B024_imgY_Crop.tif'
# image36_path = r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MW41000B22BD3_20240223020054\step02_0300NIT_B020_imgY_Crop.tif'



similarity_score1 = compare_images1(image1_path, image2_path)
# similarity_score2 = compare_images2(image3_path, image4_path)
# similarity_score3 = compare_images3(image5_path, image6_path)
# similarity_score4 = compare_images4(image7_path, image8_path)
# similarity_score5 = compare_images5(image9_path, image10_path)
# similarity_score6 = compare_images6(image11_path, image12_path)
# similarity_score7= compare_images7(image13_path, image14_path)
# similarity_score8 = compare_images8(image15_path, image16_path)
# similarity_score9 = compare_images9(image17_path, image18_path)
# similarity_score10 = compare_images10(image19_path, image20_path)
# similarity_score11 = compare_images11(image21_path, image22_path)
# similarity_score12 = compare_images12(image23_path, image24_path)
# similarity_score13 = compare_images13(image25_path, image26_path)
# similarity_score14 = compare_images14(image27_path, image28_path)
# similarity_score15 = compare_images15(image29_path, image30_path)
# similarity_score16 = compare_images16(image31_path, image32_path)
# similarity_score17 = compare_images17(image33_path, image34_path)
# similarity_score18 = compare_images18(image35_path, image36_path)



print(f"R216: {similarity_score1}")
# print(f"R192: {similarity_score2}")
# print(f"R36: {similarity_score3}")
# print(f"R32: {similarity_score4}")
# print(f"G216: {similarity_score5}")
# print(f"G192: {similarity_score6}")
# print(f"G36: {similarity_score7}")
# print(f"G32: {similarity_score8}")
# print(f"B216: {similarity_score9}")
# print(f"B192: {similarity_score10}")
# print(f"B36: {similarity_score11}")
# print(f"B32: {similarity_score12}")
# print(f"R12: {similarity_score13}")
# print(f"R10: {similarity_score14}")
# print(f"G12: {similarity_score15}")
# print(f"G10: {similarity_score16}")
# print(f"B12: {similarity_score17}")
# print(f"B10: {similarity_score18}")