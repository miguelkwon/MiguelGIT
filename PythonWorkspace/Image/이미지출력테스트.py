import cv2

image = cv2.imread("F:\Python\Image\lunar.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Test", image)
cv2.waitKey()
cv2.destroyAllWindows()