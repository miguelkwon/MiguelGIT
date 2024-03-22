import numpy as np
from PIL import Image

img = Image.open('F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\lunar.jpg')
img.show()

x = np.array(img)
print(x)
print(x.shape)

x_2 = np.asarray(img)
print(x_2)
print(x_2.shape)

img_2 = Image.fromarray(x) # NumPy array to PIL image
img_2.show()