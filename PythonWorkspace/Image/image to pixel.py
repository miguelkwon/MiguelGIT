#import cv2
#import cv2 as cv    

#image = cv2.imread('F:\Python\Image\lunar.jpg')

#def main():
    # 이미지 읽기
    #lena_color = cv.imread("F:\Python\Image\PANEL_SHAPE_X2961.bmp", cv.IMREAD_COLOR)
    #lena_gray = cv.imread("F:\Python\Image\PANEL_SHAPE_X2961.bmp", cv.IMREAD_GRAYSCALE)
    
    # 이미지 출력하기
    #cv.imshow("Title_color", lena_color)
    #cv.imshow("Tilte_gray", lena_gray)

    # size 확인, 픽셀값 읽기
    #print("Size of Img\n", lena_color.shape)
    #print("Pixel value of (10,10)\n", lena_color[10,10])

#if __name__ == "__main__":
    #main()

#cv2.imshow('MOON', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


import cv2 as cv
 
img_color = cv.imread('F:\Python\Image\lunar.jpg', cv.IMREAD_COLOR)
 
height,width = img_color.shape[:2]
print (height)
print (width)
f = open('F:\Python\Image\image.txt', 'w')
 
for y in range(height):
    for x in range(width):
        f.write("%s"%img_color[y,x])
    f.write("\n")
 
f.close()
cv.waitKey(0)