import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn import linear_model, datasets, metrics
from sklearn.datasets import fetch_olivetti_faces
import numpy as np
from PIL import Image
from scipy import signal
from scipy import misc

#fetch the Olivetti dataset. Save data in X (64 x 64 pixels) and targets in y
Df = fetch_olivetti_faces(return_X_y=False) #
X, y = fetch_olivetti_faces(return_X_y=True)
X.shape#the appende

#extract first image from dataset
X1 = X[1,:]
X1.shape
X2 = np.reshape(X1,(64, 64))
X2.shape

#plot 2D array as image with matplotlib.pyplot
plt.imshow(X2, cmap="gray")
plt.xticks(())
plt.yticks(())
plt.savefig("Olive1.png", bbox_inches='tight')

#Call up image and save as object 'img1'. Not necessary for correlation
img1 = plt.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\lunar.jpg')


#extract first image from dataset
X3 = X[2,:]
X3.shape
X4 = np.reshape(X3,(64, 64))
X4.shape

#plot 2D array as image with matplotlib.pyplot
plt.imshow(X4, cmap="gray")
plt.xticks(())
plt.yticks(())
plt.savefig("Olive2.png", bbox_inches='tight')

#Call up image and save as object 'img1'. Not necessary for correlation
img2 = plt.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\lunar.jpg')



#extract image from a different person in the dataset
X5 = X[101,:]
X5.shape
X6 = np.reshape(X5,(64, 64))
X6.shape

#plot 2D array as image with matplotlib.pyplot
plt.imshow(X6, cmap="gray")
plt.xticks(())
plt.yticks(())
plt.savefig("Olive3.png", bbox_inches='tight')

#Call up image and save as object 'img1'. Not necessary for correlation
img3 = plt.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\lunar.jpg')


#Now calculate Pearson correlation coefficient between both images from different people
corrIm = np.corrcoef(X2, X6)
corrImAbs = np.absolute(corrIm)
np.mean(corrImAbs)
np.max(corrImAbs)
np.median(corrImAbs)
# First quartile (Q1) 
Q1 = np.percentile(corrImAbs, 25, interpolation = 'midpoint') 
print(Q1)
# Third quartile (Q3) 
Q3 = np.percentile(corrImAbs, 75, interpolation = 'midpoint') 
print(Q3)
# Interquaritle range (IQR) 
IQR = Q3 - Q1 
print(IQR)


#scale data
X = np.asarray( X, 'float32')
X = (X - np.min(X, 0)) / (np.max(X, 0) + 0.0001)  # 0-1 scaling

# Convert image array to binary with threshold. This will create black-and-white images
X = X > 0.5