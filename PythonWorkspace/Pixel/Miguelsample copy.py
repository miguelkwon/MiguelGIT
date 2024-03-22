import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os

#윈도우 생성
win = Tk()
win.title("이미지 분석")
win.geometry("400x300")

#이미지 불러오기
#그레이스케일
def openimg():
    global dir_path
    dir_path = filedialog.askopenfilename(initialdir="F:\MiguelGIT\PythonWorkspace\TEST_IMAGE",\
					title = "파일 선택",
                    filetypes=(('tif','*.tif'),('all files','*.*')))
    
    # image1 = cv2.imread(dir_path, cv2.IMREAD_GRAYSCALE)
     
    # image2 = cv2.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step02_0300NIT_R020_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE)
    # image3 = cv2.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step03_0010NIT_B062_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE)
    # image4 = cv2.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\step03_0010NIT_B062_imgY_Crop.tif', cv2.IMREAD_GRAYSCALE)

    # #해상도 알아내기 이미지 불러오기
    # image11 = Image.open(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\test.tif')
    # image22 = Image.open(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\test.tif')
    # image33 = Image.open(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\test.tif')
    # image44 = Image.open(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\test.tif')



    #칼라 불러오기
    image_bgr = cv2.imread(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\test.tif', cv2.IMREAD_COLOR)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    
image1= cv2.imread(dir_path, cv2.IMREAD_GRAYSCALE)
    

#이미지 출력
#1개만 출력
#plt.imshow(image1); plt.show()

def print():
    print(image11.size,image22.size,image33.size,image44.size)
    w1, h1 = image11.size
    w2, h2 = image22.size
    w3, h3 = image33.size
    w4, h4 = image44.size
    print("width(가로) : ", w1,"height(세로) : ", h1)
    print("width(가로) : ", w2,"height(세로) : ", h2)
    print("width(가로) : ", w3,"height(세로) : ", h3)
    print("width(가로) : ", w4,"height(세로) : ", h4)

#이미지 저장
def save():
    cv2.imwrite(r'F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\new_plane.tif', image1)

#이미지 크롭
def crop():
 
    image_cropped1 = image1[0:2000,0:100]
    # image_cropped2 = image2[:100,:50]
    # image_cropped3 = image3[:50,:50]
    # image_cropped4 = image4[:50,:50]
    plt.imshow(image_cropped1); plt.show()


    #4이미지 4개 출력
    fig = plt.figure(figsize = (10,10))

    plt.subplot(2,2,1)
    plt.imshow(image_cropped1)
    plt.title('result 1')
    # plt.xticks([])
    # plt.yticks([]) 


    # plt.subplot(2,2,2)
    # plt.imshow(image_cropped2)
    # plt.title('result 2')
    # # plt.xticks([])
    # # plt.yticks([]) 

    # plt.subplot(2,2,3)
    # plt.imshow(image_cropped3)
    # plt.title('result 3')
    # # plt.xticks([])
    # # plt.yticks([]) 


    # plt.subplot(2,2,4)
    # plt.imshow(image_cropped4)
    # plt.title('result 4')
    # # plt.xticks([])
    # # plt.yticks([]) 


    plt.suptitle('COMPARE IMAGE', fontsize = 20)
    plt.show()



#버튼
Openfolder1btn = tk.Button(win, text='open',height=1, width=10, command=openimg)
Openfolder1btn.place(x=0, y=0)
printimgbtn = tk.Button(win, text='print',height=1, width=10, command=crop)
printimgbtn.place(x=0, y=25)

win.mainloop()