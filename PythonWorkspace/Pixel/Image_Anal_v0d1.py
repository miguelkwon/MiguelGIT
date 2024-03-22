# Converting an RGB image to grayscale and manipulating the pixel data in python
# https://stackoverflow.com/questions/23935840/converting-an-rgb-image-to-grayscale-and-manipulating-the-pixel-data-in-python
# https://stackoverflow.com/questions/59303163/finding-the-percentage-of-cracks-in-a-sem-image
# How to detect and measure(fitEllipse) objects on the SEM image using OpenCV?
# https://stackoverflow.com/questions/54604608/how-to-detect-and-measurefitellipse-objects-on-the-sem-image-using-opencv

# Required modules
# pip install pillow (python image file load/save, manipulation)
# pip install numpy (handle image as array)0
# pip install matplotlib (graph plotting)
# pip install opencv-python (open source computer vision library)

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import cv2


def main():
    # Load image as grayscale, count pixel under thres value 
    img_file = r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step02_0300NIT_R020_imgY_Crop.tif' # SEM image file
        
    img = Image.open(img_file)
    igs = img.convert('L') # image grayscale, (R,G,B)->(wb,wb,wb)
    w, h = igs.size
    print('img w:', w, 'img h:', h)
    # igs.save('sem_test_gs.png')

    y=np.asarray(igs.getdata(),dtype=np.uint8).reshape((h, w))
    # print(y)
    y = y - np.amin(y) # shift values down to 0 
    
    imax = np.amax(y)
    imin = np.amin(y) # set to 0
    thres10 = int((imax-imin)/10)
    print('max:', imax, 'min:', imin, 'threshold-10%:', thres10)

    # threshold value for black
    thres = int(input('Input threshold value for pore (black): '))
    if thres == '':
        thres = thres10
        
    y2 = y[np.where(y < thres)] # slice array and count 
    count = y2.size
    # print(y2)    
    
##    count = 0 # a bit slow double for loop 2D array counting
##    for irow in y:
##        for icol in irow:
##            if icol <= thres:
##                count += 1   

    # Calculate crack percentage
    percentage = count / (w * h) * 100
    print('Pore percentage: {:.2f}%'.format(percentage))

##    # If necessary, save processed image
##    y=np.asarray(y,dtype=np.uint8) # now y color values from 0 to imax
##    wimg=Image.fromarray(y,mode='L')
##    wimg.save(img_file.split('.')[0]+'_out.png')


    # Fill R_color for every pixels if their values are under thres
    img2 = cv2.imread(img_file, cv2.IMREAD_COLOR)
    wx, hy, rgb = img2.shape
    # print('wx:', wx, 'hy:', hy, 'rgb:', rgb)

    for x in range(wx):
        for y in range(hy):
            if img2[x, y][0] < thres:
                img2[x, y] = np.array([255, 10, 0])

    strL = 'Original image ('+str(wx)+', '+str(hy)+'), area= '+ \
           str(wx*hy)
    strR = 'Pore-colored image, Porosity= '+str(round(percentage, 2))+' %'
    print(strL, strR, sep='\n')
    
    # Plotting original image & red color filled one
    fig = plt.figure(figsize=(12,6))

    figL = plt.subplot2grid((6,4), (1,0), rowspan=5, colspan=2)
    figR = plt.subplot2grid((6,4), (1,2), rowspan=5, colspan=2)
    
    figL.set_title(strL, fontsize=16)
    figR.set_title(strR, fontsize=16)

    figL.imshow(img)
    figR.imshow(img2)
    plt.tight_layout()
    # plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig(img_file.split('.')[0]+'_out.png')
    plt.show()


# main 함수 로딩부
if __name__ == '__main__':
    main()
