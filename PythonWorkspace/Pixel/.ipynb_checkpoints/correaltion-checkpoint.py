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
 
def compare_images2(compare1, compare2):
    hist1 = cv2.calcHist([compare1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([compare2], [0], None, [256], [0, 256])
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return similarity
 
 # load the images -- the original, the original + contrast,
# and the original + photoshop
image1 = cv2.imread("F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step02_0300NIT_G020_imgY_Crop.tif")
image2 = cv2.imread("F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step02_0300NIT_G024_imgY_Crop.tif")
# shopped = cv2.imread("F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step03_0010NIT_B062_imgY_Crop.tif")
# convert the images to grayscale
compare1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
compare2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
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