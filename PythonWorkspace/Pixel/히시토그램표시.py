

import numpy as np, cv2

import matplotlib.pylab as plt

 

# 이미지를 그레이 스케일로 읽기 및 출력

img = cv2.imread(r"F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step02_0300NIT_R020_imgY_Crop.tif", cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)

 

# 히스토그램 계산 및 그리기

hist = cv2.calcHist([img], [0], None, [4096], [0, 4096])



plt.subplot(1,2,1)
plt.plot(hist)
plt.title('Hitogram')
# plt.xticks([])
# plt.yticks([]) 


plt.subplot(1,2,2)
plt.imshow(img)
plt.title('IMG') 
 
 

print(hist.shape)               # 히스토그램의 shape (256, 1)

print(hist.sum(), img.shape)    # 히스토그램의 총 합계와 이미지의 크기

plt.suptitle('Histogram', fontsize = 20)
plt.show()
