import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import os





img1 = Image.open(r'C:\Radiant Vision Systems Data\TrueTest\AppData\PANEL_SHAPE_2752x2064.bmp')
img2 = cv2.imread(r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MP41002P11BA3\InputIMG\B72_10B.tif', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MP41002P11BA3_20240223074001\step02_0300NIT_G020_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE)
img4 = Image.open(r'G:\01_LGDisplay\02_Tablet\01_X2146\01_LGDVH\02_Data\20240223_imagecheck\503-10-2\A5MP41002P11BA3_20240223074001\step99_0300NIT_W062_imgY_Crop.tif')



# 픽셀해상도
print(img1.size,img4.size)
w1, h1 = img1.size
w2, h2 = img4.size
print("width(가로) : ", w1,"height(세로) : ", h1)
print("width(가로) : ", w2,"height(세로) : ", h2)



#이미지 출력

fig = plt.figure(figsize = (10,10))



plt.subplot(2,2,1)
plt.imshow(img1)
plt.title('result 1')
# plt.xticks([])
# plt.yticks([]) 


plt.subplot(2,2,2)
plt.imshow(img4)
plt.title('result 2')
# plt.xticks([])
# plt.yticks([]) 

plt.subplot(2,2,3)
plt.imshow(img1)
plt.title('result 3')
# plt.xticks([])
# plt.yticks([]) 


plt.subplot(2,2,4)
plt.imshow(img4)
plt.title('result 4')
# plt.xticks([])
# plt.yticks([]) 


plt.suptitle('IMAGE 4', fontsize = 20)
plt.show()

# def compare(img1,img2):
#     image1 = cv2.imread(img1)
#     image2 = cv2.imread(img2)
    
#     image1 = cv2.resize(image1, (300, 300))
#     image2 = cv2.resize(image2, (300, 300))
    
#     # 이미지를 그레이스케일로 변환
#     image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#     image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
#     hist1 = cv2.calcHist([image1_gray], [0], None, [256], [0, 256])
#     hist2 = cv2.calcHist([image2_gray], [0], None, [256], [0, 256])

#     similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

#     return similarity

# image1 = cv2.resize(img1, (1000, 1000))
# image2 = cv2.resize(img2, (100, 100))

# img1.save("F:\MiguelGIT\PythonWorkspace\Image/2727409-200_resize.png")


# difference = cv2.subtract(image1, image2)
# if np.count_nonzero(difference) == 0:
#     print("두 이미지는 동일합니다.")
# else:
#     print("두 이미지는 동일하지 않습니다.")



# similarity_score = compare(img1, img2)
# print(f"두 이미지의 유사도: {similarity_score}")






