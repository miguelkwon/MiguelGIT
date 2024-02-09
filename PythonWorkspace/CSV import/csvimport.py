import pandas as pd
import csv
import shutil
import os
import glob
import time
from datetime import datetime
from os import path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox









TabletSetup = tk.Tk()
TabletSetup.title("RADIANT-TABLET-SETUP")
TabletSetup.geometry('700x100')



label1 = tk.Label(TabletSetup, text='Test')
label1.place(x=500, y=0)

def csvimport():
    
 csv_test = pd.read_csv('C:/Users/ssa2p/Documents/KakaoTalk Downloads/All.csv')
 print(csv_test)
 
#  list_file = []                                          #파일 목록 담을 리스트 생성
#  files = filedialog.askopenfilenames(initialdir="/",\
#                  title = "파일을 선택 해 주세요",\
#                     filetypes = (("*.csv","*csv"),("*.xlsx","*xlsx"),("*.xls","*xls")))
# #files 변수에 선택 파일 경로 넣기
# #  print(files)  #files 리스트 값 출력
 

 
#  if files == '':
#     messagebox.showwarning("경고", "파일을 추가 하세요")    #파일 선택 안했을 때 메세지 출력
# #  f=open(files,'r')
# #  rdr=csv.reader(files) 
# #  for line in rdr: 
# #     # print(files)  #files 리스트 값 출력

  

	

button4 = tk.Button(TabletSetup, text='click', command=csvimport)
button4.place(x=500, y=30)






































TabletSetup.mainloop()