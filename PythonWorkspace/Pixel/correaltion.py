# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2






def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
     
 
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err


def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
 
    
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB,multichannel=True)
    
    
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
 
 
def compare_images2(compare1, compare2):
    hist1 = cv2.calcHist([compare1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([compare2], [0], None, [256], [0, 256])
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return similarity


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


 # load the images -- the original, the original + contrast,
# and the original + photoshop
image1 = fos_cap
image2 = img_input
# image1 = cv2.imread(r"C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Flat\step2_03_G43_imgY_Crop.tif")
# image2 = cv2.imread(r"C:\Users\ssa2p\Documents\KakaoTalk Downloads\Capture_Flat&Capture_Noise\Capture_Noise\step2_03_G43_imgY_Crop.tif")
# shopped = cv2.imread("F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step03_0010NIT_B062_imgY_Crop.tif")
# convert the images to grayscale
compare1 = image1
compare2 = image2
# compare1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# compare2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)



# initialize the figure
fig = plt.figure("Images")
images = ("1", compare1), ("2", compare2)

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

compare_images(compare1, compare2, "1 vs. 2")
# similarity_score = compare_images2(compare1, compare2)
# print(f"두 이미지의 유사도: {similarity_score}")


