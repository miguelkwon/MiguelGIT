# import cv2
# import matplotlib.pyplot as plt

# img = cv2.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\national-cancer-institute-jdfn7Z03Qa4-unsplash.jpg', cv2.IMREAD_UNCHANGED)
# img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# plt.subplot(1,2,1)
# plt.imshow(img)

# plt.subplot(1,2,2)
# plt.imshow(img_norm)
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 255])

# for i, h in enumerate([hist, hist_norm]):
#     plt.subplot(1,2,i+1)
#     plt.plot(h)
# plt.show()

import cv2
import numpy as np
import matplotlib.pylab as plt
from skimage.metrics import structural_similarity as ssim


# box1 = 6
# box2 = 10
# row = 1668
# col = 2420
# col = 2420
# reshape_y = row/box1
# reshape_x = col/box2

# scale = 1
# spec_R = 0.93
# spec_G = 0.93
# spec_B = 0.80

# R216_flat = cv2.imread(r'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Flat\step2_03_R43_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE).astype(float)
# G216_flat = cv2.imread(r'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Flat\step2_03_G43_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE).astype(float)
# B216_flat = cv2.imread(r'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Flat\step2_03_B43_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE).astype(float)
# R216_noise = cv2.imread(r'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Noise\step2_03_R43_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE).astype(float)
# G216_noise = cv2.imread(r'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Noise\step2_03_G43_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE).astype(float)
# B216_noise = cv2.imread(r'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Noise\step2_03_B43_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE).astype(float)

# # Resize noise images
# row, col = R216_noise.shape
# scale = 2  # Example value for scale, replace it with your actual value
# R216_noise_resized = cv2.resize(cv2.resize(R216_noise, (int(col/scale), int(row/scale))), (col, row))
# G216_noise_resized = cv2.resize(cv2.resize(G216_noise, (int(col/scale), int(row/scale))), (col, row))
# B216_noise_resized = cv2.resize(cv2.resize(B216_noise, (int(col/scale), int(row/scale))), (col, row))

# # Create W216_noise and W216_flat arrays
# W216_noise = np.dstack((R216_noise_resized, G216_noise_resized, B216_noise_resized))
# W216_flat = np.dstack((R216_flat, G216_flat, B216_flat))

# # Read capture images
# capture_flat_paths = ['step2_03_R43_imgY_Crop.tif', 'step2_03_G43_imgY_Crop.tif', 'step2_03_B43_imgY_Crop.tif']
# capture_noise_paths = ['step2_03_R43_imgY_Crop.tif', 'step2_03_G43_imgY_Crop.tif', 'step2_03_B43_imgY_Crop.tif']

# W216_capture_noise = np.zeros((row, col, 3))
# W216_capture_flat = np.zeros((row, col, 3))

# for i, path in enumerate(capture_flat_paths):
#     W216_capture_flat[:,:,i] = cv2.imread(rf'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Noise\{path}', cv2.IMREAD_GRAYSCALE).astype(float)

# for i, path in enumerate(capture_noise_paths):
#     W216_capture_noise[:,:,i] = cv2.imread(rf'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Flat\{path}', cv2.IMREAD_GRAYSCALE).astype(float)

# fos_cap = np.zeros_like(W216_capture_noise)
# img_input = np.zeros_like(W216_noise)

# for color in range(3):
#     fos_cap[:,:,color] = 1 + ((W216_capture_noise[:,:,color] - W216_capture_flat[:,:,color]) / W216_capture_flat[:,:,color])
#     img_input[:,:,color] = (1 + ((300 * (W216_noise[:,:,color] / 255) ** 2.2) - (300 * (216 / 255) ** 2.2)) / (300 * (216 / 255) ** 2.2))
    
# # R216_flat = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_flat_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
# # G216_flat = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_flat_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
# # B216_flat = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_flat_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
# # R216_noise = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_noise_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
# # G216_noise = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_noise_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
# # B216_noise = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_noise_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)

# # # Resize noise images
# # row, col = R216_noise.shape
# # scale = 2  # Example value for scale, replace it with your actual value
# # R216_noise_resized = cv2.resize(cv2.resize(R216_noise, (int(col/scale), int(row/scale))), (col, row))
# # G216_noise_resized = cv2.resize(cv2.resize(G216_noise, (int(col/scale), int(row/scale))), (col, row))
# # B216_noise_resized = cv2.resize(cv2.resize(B216_noise, (int(col/scale), int(row/scale))), (col, row))

# # # Create W216_noise array
# # W216_noise = np.dstack((R216_noise_resized, G216_noise_resized, B216_noise_resized))

# # # Read capture images
# # capture_flat_paths = ['R43 (Synthetic).txt', 'G43 (Synthetic).txt', 'B43 (Synthetic).txt']
# # capture_noise_paths = ['R43 (Synthetic).txt', 'G43 (Synthetic).txt', 'B43 (Synthetic).txt']

# # W216_capture_noise = np.zeros((row, col, 3))
# # W216_capture_flat = np.zeros((row, col, 3))

# # for i, path in enumerate(capture_flat_paths):
# #     W216_capture_flat[:,:,i] = np.loadtxt(rf'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Noise\{path}')

# # for i, path in enumerate(capture_noise_paths):
# #     W216_capture_noise[:,:,i] = np.loadtxt(rf'C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Flat\{path}')

# # fos_cap = np.zeros_like(W216_capture_noise)

# # for color in range(3):
# #     # Capture image normalization
# #     fos_cap[:,:,color] = 1 + ((W216_capture_noise[:,:,color] - W216_capture_flat[:,:,color]) / W216_capture_flat[:,:,color])
    
# #     # Display pattern normalization
# #     img_input[:,:,color] = 1 + (300 * ((W216_noise[:,:,color] / 255) ** 2.2) - (300 * (216 / 255) ** 2.2)) / (300 * (216 / 255) ** 2.2)

# # Capture image normalization
# fos_cap = np.zeros_like(W216_capture_noise)
# img_input = np.zeros_like(W216_noise)

# for color in range(3):
#     fos_cap[:,:,color] = 1 + ((W216_capture_noise[:,:,color] - W216_capture_flat[:,:,color]) / W216_capture_flat[:,:,color])
#     img_input[:,:,color] = (1 + ((300 * (W216_noise[:,:,color] / 255) ** 2.2) - (300 * (216 / 255) ** 2.2)) / (300 * (216 / 255) ** 2.2))

# # Calculation body
# similar = np.zeros((row * col // (box1 * box2), 3))
# correct_map = np.zeros((row, col, 3))
# fos_cap_box = np.zeros((box1, box2, 3))
# img_input_box = np.zeros((box1, box2, 3))

# for color2 in range(3):
#     z = 1
#     for i in range(0, row, box1):
#         for j in range(0, col, box2):
#             fos_cap_box[:,:,color2] = fos_cap[i:i+box1,j:j+box2,color2]
#             img_input_box[:,:,color2] = img_input[i:i+box1,j:j+box2,color2]
#             similar_box = np.corrcoef(fos_cap_box[:,:,color2].flatten(), img_input_box[:,:,color2].flatten())
#             similar[z,color2] = similar_box[0, 1]
#             correct_map[i:i+box1,j:j+box2,color2] = fos_cap_box[:,:,color2] / img_input_box[:,:,color2]
#             z += 1

#     similar_map[:,:,color2] = np.reshape(similar[:,color2], [reshape_x, reshape_y]).T

#     similar_edge_top2cen[:,color2] = similar_map[0,5:-5,color2] / similar_map[1,5:-5,color2]
#     similar_edge_bot2cen[:,color2] = similar_map[-1,5:-5,color2] / similar_map[-2,5:-5,color2]
#     similar_edge_left2cen[:,color2] = similar_map[5:-5,0,color2] / similar_map[5:-5,1,color2]
#     similar_edge_right2cen[:,color2] = similar_map[5:-5,-1,color2] / similar_map[5:-5,-2,color2]

# similar_map_R = similar_map[:,:,0]
# similar_map_G = similar_map[:,:,1]
# similar_map_B = similar_map[:,:,2]

# similar_map_1D = np.zeros((similar_map.shape[0] * similar_map.shape[1], 3))
# similar_map_1D[:,0] = similar_map_R.flatten()
# similar_map_1D[:,1] = similar_map_G.flatten()
# similar_map_1D[:,2] = similar_map_B.flatten()

# count_R = np.sum(similar_map_1D[:,0] > spec_R) / len(similar_map_1D[:,0])
# count_G = np.sum(similar_map_1D[:,1] > spec_G) / len(similar_map_1D[:,1])
# count_B = np.sum(similar_map_1D[:,2] > spec_B) / len(similar_map_1D[:,2])

# count_R = "{:.2%}".format(count_R)
# count_G = "{:.2%}".format(count_G)
# count_B = "{:.2%}".format(count_B)

# # Output figure summary
# fig, axs = plt.subplots(4, 3, figsize=(15, 15))

# for i in range(3):
#     axs[0, i].imshow(similar_map[:,:,i], cmap='viridis', vmin=0, vmax=1)
#     axs[0, i].set_title(f'{["R", "G", "B"][i]}={["count_R", "count_G", "count_B"][i]}')
#     axs[0, i].set_xticks([])
#     axs[0, i].set_yticks([])
#     axs[0, i].set_aspect('equal')
#     axs[0, i].set_xlabel('X')
#     axs[0, i].set_ylabel('Y')
#     axs[0, i].set_xlim(0, similar_map.shape[1])
#     axs[0, i].set_ylim(0, similar_map.shape[0])
#     fig.colorbar(axs[0, i].imshow(similar_map[:,:,i], cmap='viridis', vmin=0, vmax=1), ax=axs[0, i])

# for i in range(3):
#     axs[1, i].hist(similar_map[:,:,i].flatten(), bins=50, range=(0, 1), color=['red', 'green', 'blue'][i])
#     axs[1, i].set_title(['R', 'G', 'B'][i])
#     axs[1, i].set_xlim(0, 1)
#     axs[1, i].set_xlabel('Value')
#     axs[1, i].set_ylabel('Frequency')

# edge_data = [similar_edge_top2cen, similar_edge_bot2cen, similar_edge_left2cen, similar_edge_right2cen]
# titles = ['top2cen', 'bot2cen', 'left2cen', 'right2cen']
# for i, data in enumerate(edge_data):
#     for j in range(3):
#         axs[i+2, j].plot(data[:, j], color=['red', 'green', 'blue'][j])
#         axs[i+2, j].set_title(titles[i])
#         axs[i+2, j].set_ylim(0.85, 1.15)
#         axs[i+2, j].set_xlabel('Index')
#         axs[i+2, j].set_ylabel('Value')

# plt.tight_layout()

# # Set the new width and height in pixels
# new_width = 1300  # Replace with your desired width
# new_height = 2160  # Replace with your desired height

# # Get the current figure position
# current_position = fig.get_position()

# # Update the width and height while preserving the figure's position on the screen
# new_position = [current_position.x0, current_position.y0, new_width, new_height]
# fig.set_position(new_position)

# plt.savefig(input_station_ID + input_camera_num + '_summary.png')
# plt.show()

# Combine matrices into W216_capture_noise and W216_capture_flat
# W216_capture_noise = np.dstack((R_matrix_noise, G_matrix_noise, B_matrix_noise))
# W216_capture_flat = np.dstack((R_matrix_flat, G_matrix_flat, B_matrix_flat))


# Read flat and noise images
R216_flat = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_flat_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
G216_flat = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_flat_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
B216_flat = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_flat_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
R216_noise = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_noise_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
G216_noise = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_noise_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)
B216_noise = cv2.imread(r'C:\Users\ssa2p\Desktop\X2381\W216_noise_X2381.bmp', cv2.IMREAD_GRAYSCALE).astype(float)

# Resize noise images
row, col = R216_noise.shape
scale = 2  # Example value for scale, replace it with your actual value
R216_noise_resized = cv2.resize(cv2.resize(R216_noise, (int(col/scale), int(row/scale))), (col, row))
G216_noise_resized = cv2.resize(cv2.resize(G216_noise, (int(col/scale), int(row/scale))), (col, row))
B216_noise_resized = cv2.resize(cv2.resize(B216_noise, (int(col/scale), int(row/scale))), (col, row))

# Create W216_noise and W216_flat arrays
W216_noise = np.dstack((R216_noise_resized, G216_noise_resized, B216_noise_resized))
W216_flat = np.dstack((R216_flat, G216_flat, B216_flat))

# Read capture images
W216_capture_noise = np.zeros((row, col, 3))
W216_capture_flat = np.zeros((row, col, 3))

for color in range(3):
    W216_capture_noise[:, :, color] = cv2.imread(f'C:/Users/ssa2p/Documents/KakaoTalk Downloads/Capture_Flat&Capture_Noise/Capture_Noise/step2_03_{"RGB"[color]}43_imgY_Crop.tif', cv2.IMREAD_UNCHANGED).astype(float)
    W216_capture_flat[:, :, color] = cv2.imread(f'C:/Users/ssa2p/Documents/KakaoTalk Downloads/Capture_Flat&Capture_Noise/Capture_Flat/step2_03_{"RGB"[color]}43_imgY_Crop.tif', cv2.IMREAD_UNCHANGED).astype(float)

# Capture image normalization and display pattern normalization
fos_cap = np.zeros_like(W216_capture_noise)
img_input = np.zeros_like(W216_noise)

for color in range(3):
    fos_cap[:,:,color] = 1 + ((W216_capture_noise[:,:,color] - W216_capture_flat[:,:,color]) / W216_capture_flat[:,:,color])
    img_input[:,:,color] = (1 + ((300 * (W216_noise[:,:,color] / 255) ** 2.2) - (300 * (216 / 255) ** 2.2)) / (300 * (216 / 255) ** 2.2))

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
 
    
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
    
    
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	# show the images
	plt.show()
# initialize the figure
fig = plt.figure("Images")
images = ("1", fos_cap), ("2", img_input)

# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 2, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
# show the figure
plt.show()
# compare the images
compare1 = cv2.cvtColor(fos_cap)
compare2 = cv2.cvtColor(img_input)

compare_images(compare1, compare2, "1 vs. 2")
#--① 그레이 스케일로 영상 읽기
# img = cv2.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\images.jpg')
# #--② 직접 연산한 정규화
# img_f = img.astype(np.float32)
# img_norm = ((img_f - img_f.min()) * (255) / (img_f.max() - img_f.min()))
# img_norm = img_norm.astype(np.uint8)

# #--③ OpenCV API를 이용한 정규화
# img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# #--④ 히스토그램 계산
# hist = cv2.calcHist([img], [0], None, [256], [0, 255])
# hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 255])
# hist_norm2 = cv2.calcHist([img_norm2], [0], None, [256], [0, 255])

# cv2.imshow('Before', img)
# cv2.imshow('Manual', img_norm)
# cv2.imshow('cv2.normalize()', img_norm2)

plt.subplot(1,2,1)
plt.imshow(fos_cap)
plt.subplot(1,2,2)
plt.imshow(img_input)
# plt.subplot(1,3,2)
# plt.imshow(img_norm)
# plt.subplot(1,3,3)
# plt.imshow(img_norm2)
plt.show()

# hists = {'Before' : hist, 'Manual':hist_norm, 'cv2.normalize()':hist_norm2}
# for i, (k, v) in enumerate(hists.items()):
#     plt.subplot(1,3,i+1)
#     plt.title(k)
#     plt.plot(v)
# plt.show()



# shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
     
 
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

# similarity_score = compare_images2(compare1, compare2)
# print(f"두 이미지의 유사도: {similarity_score}")