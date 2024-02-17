import webbrowser
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import subprocess
import psutil
from pywinauto import application
import time
import glob
import shutil
from tkinter import messagebox



window=Tk()
window.title("Web")
window.geometry("180x500+1700+50")


def open1():
  webbrowser.open("https://www.naver.com/")
  webbrowser.open("https://www.google.co.kr/webhp?hl=ko&tab=ww")
def open2():
  webbrowser.open("https://mail.naver.com/v2/folders/-1")
  webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
def open3():
  webbrowser.open("https://papago.naver.com/")
  webbrowser.open("https://translate.google.com/?hl=ko")
def open4():
  webbrowser.open("https://mlbpark.donga.com/mp/b.php?select=hitView&m=search&b=bullpen&search_select2=hitView&query=1000&x=40&y=19")
def open5():
  webbrowser.open("https://bbongtv.com/")

def open7():
  os.startfile(r"F:\OneDrive - Radiant Vision Systems\01_Miguel.kwon\02_Activity + Weekly_Report\2024Y")
def open8():
  os.startfile(r"F:\OneDrive - Radiant Vision Systems\01_Miguel.kwon\03_Expense\02_Travel\2024Y")

def open9():
 subprocess.Popen('F:\Git\Dove2p0.exe')
 os.startfile("D:\DATABASE\InputIMG")
 os.startfile("C:\Radiant Vision Systems Data\TrueTest\Sequence")
 app=application.Application()
 app.start(r'C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\devenv.exe')
#  subprocess.Popen('F:\Git\TT-DemuraLGDN\TrueTEST-DemuraLGDN')
 
def open10():
 subprocess.Popen('F:\Git\Dove2p0.exe')
 os.startfile("D:\DATABASE\InputIMG")
 os.startfile("C:\Radiant Vision Systems Data\TrueTest\Sequence")
 subprocess.Popen('C:\Program Files\Radiant Vision Systems\TrueTest 1.8\TrueTest.exe')
 

def open11():
 for proc in psutil.process_iter():
        if proc.name() == "TrueTestWatcher.exe" :
            proc.kill()
        if proc.name() == "FTPUploaderVB.exe" :
            proc.kill()
        if proc.name() == "SetSequence.exe" :
            proc.kill()
        if proc.name() == "TrueTest.exe" :
            proc.kill()
        if proc.name() == "Dove2p0.exe" :
            proc.kill()
        if proc.name() == "explorer.exe" :
            proc.kill()

def open12():
   def get_today():
    now = time.localtime()
    s = "%02d%02d%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
    return s

   today=get_today()                          
   backuppath= r'G:\99_Desktop backup'+'/'+today
   b1=backuppath+'/'+'Desktop'
   b2=backuppath+'/'+'Downloads'
   b3=backuppath+'/Documents/KakaoTalk'
   b4=backuppath+'/Documents'



   if not os.path.exists(backuppath):
    os.makedirs(backuppath)
   if not os.path.exists(b1):
    os.makedirs(b1)
   if not os.path.exists(b2):
    os.makedirs(b2)
   if not os.path.exists(b3):
    os.makedirs(b3)
#  backup_dir=backuppath+'/'+ today 
#  if not os.path.exists(backup_dir):
#     os.makedirs(backup_dir)
 

   sourcepath1=r"C:\Users\ssa2p\Desktop"
   sourcepath2=r"C:\Users\ssa2p\Downloads"  
   sourcepath3=r"C:\Users\ssa2p\Documents\KakaoTalk Downloads"
   sourcepath4=r"C:\Users\ssa2p\Documents"
   sourcepath41=r"C:\Users\ssa2p\Documents\*.*"
   
  
   filelist1 = glob.glob(f"{sourcepath1}/")
   filelist2 = glob.glob(f"{sourcepath2}/")
   filelist3 = glob.glob(f"{sourcepath3}/")
   filelist4 = glob.glob(f"{sourcepath4}/*.*")

#  backup_dir=backuppath

   
   shutil.copytree(
        sourcepath1,
        b1,
        dirs_exist_ok=True
    )
   
   
  #  for files in os.listdir(sourcepath1):
  #   path = os.path.join(sourcepath2, files)
  #   try:
  #       shutil.rmtree(path)
  #   except OSError:
  #       os.remove(path)
   
   
   
   shutil.copytree(
        sourcepath2,
        b2,
        dirs_exist_ok=True
    )
   
   
  
   for files in os.listdir(sourcepath2):
    path = os.path.join(sourcepath2, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
   
    
   
   shutil.copytree(
        sourcepath3,
        b3,
        dirs_exist_ok=True
    )
   for files in os.listdir(sourcepath3):
    path = os.path.join(sourcepath3, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)
        
   for src in filelist4:
    f = os.path.basename(src)
    tgt1 = os.path.join(b4, f)    
    shutil.copyfile(src, tgt1)
    
  

   for filelist4 in filelist4:
    try:
        os.remove(filelist4)
    except OSError as e:
        print(f"Error:{ e.strerror}")
    
   
    
  
    
 
    
  
web11btn = tk.Button(window, text='Naver,goole',height=1, width=10, command=open1)
web11btn.place(x=0, y=10)
web12btn = tk.Button(window, text='Mail',height=1, width=10, command=open2)
web12btn.place(x=90, y=10)
web21btn = tk.Button(window, text='Translate',height=1, width=10, command=open3)
web21btn.place(x=0, y=40)
web22btn = tk.Button(window, text='ETC',height=1, width=10, command=open4)
web22btn.place(x=90, y=40)
web31btn = tk.Button(window, text='BBong',height=1, width=10, command=open5)
web31btn.place(x=0, y=70)
# web32btn = tk.Button(window, text='Expense',height=1, width=10, command=openweb6)
# web32btn.place(x=90, y=70)

web41btn = tk.Button(window, text='weekly',height=1, width=10, command=open7)
web41btn.place(x=0, y=100)
web42btn = tk.Button(window, text='Expense',height=1, width=10, command=open8)
web42btn.place(x=90, y=100)
web51btn = tk.Button(window, text='TT',height=1, width=4, command=open9)
web51btn.place(x=0, y=130)
web511btn = tk.Button(window, text='TT',height=1, width=4, command=open10)
web511btn.place(x=45, y=130)
web52btn = tk.Button(window, text='Quit',height=1, width=10, command=open11)
web52btn.place(x=90, y=130)
web61btn = tk.Button(window, text='Backup',height=1, width=10, command=open12)
web61btn.place(x=0, y=160)
 
 
window.mainloop()