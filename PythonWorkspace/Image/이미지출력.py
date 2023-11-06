import cv2

image = cv2.imread("F:\Python\Image\PANEL_SHAPE_X2961.bmp", cv2.IMREAD_COLOR)
cv2.imshow("original", image)
height, width, channel=image.shape
print(height, width, channel)
cv2.waitKey()
cv2.destroyAllWindows()