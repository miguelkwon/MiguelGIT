import cv2

image = cv2.imread("F:\MiguelGIT\PythonWorkspace\Image\step01_0300NIT_B064_imgY_Crop.tif", cv2.IMREAD_COLOR)
cv2.imshow("original", image)
height, width, channel=image.shape
print(height, width, channel)
cv2.waitKey()
cv2.destroyAllWindows()