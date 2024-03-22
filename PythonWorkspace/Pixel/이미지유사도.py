import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread(r'd:\NewImageName.bmp')
img2 = cv2.imread(r'd:\NewImageName2.bmp')
img3 = cv2.imread(r'F:\img\TEMP_step99_0300NIT_W064_imgY_Crop.tif')
# img4 = cv2.imread('taekwon_v.jpg')
img4 = cv2.imread(r'F:\img\step02_0300NIT_R020_imgY_Crop.tif')

cv2.imshow('img1', img1)
imgs = [img1, img2, img3, img4]
hists = []

for i, img in enumerate(imgs):
    plt.subplot(1, len(imgs), i+1)
    plt.title('img%d' %(i+1))
    plt.axis('off')
    plt.imshow(img[:, :, ::-1])  # BGR -> RGB
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 0번(h)은 0 ~ 180 사이, 1번(s)은 0 ~ 255 사이
    hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    hists.append(hist)

# print(hists[0])
query = hists[0]
methods = {'CORREL': cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR,
           'INTERSECT':cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}

for j, (name, flag) in enumerate(methods.items()):
    print('%-10s' % name, end='\t')
    for i, (hist, img) in enumerate(zip(hists, imgs)):
        ret = cv2.compareHist(query, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT:  # 교차 분석일 경우에만 변경
            ret = ret / np.sum(query)  # 1미만의 수로 정규화
        print('img%d:%7.2f' % (i+1, ret), end='\t')
    print()
plt.show()