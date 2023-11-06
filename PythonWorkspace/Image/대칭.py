import cv2

src = cv2.imread("F:\Python\Image\lunar.jpg",cv2.IMREAD_COLOR)
dst=cv2.flip(src,1)

cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()

