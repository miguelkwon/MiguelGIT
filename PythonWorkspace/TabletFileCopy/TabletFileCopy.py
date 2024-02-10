import shutil
import os
import glob
import time
import subprocess
import psutil
import zipfile
from zipfile import ZipFile
import pefile
import pywintypes
import win32api
import ftplib
# import paramiko
from win32api import GetFileVersionInfo, LOWORD, HIWORD


import sys
from datetime import datetime
from os import path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


cmd = ['powershell.exe', 'Start-Process', 'notepad', '${env:ProgramFiles(x86)}\test\setting.ini','-Verb','runAs']
subprocess.run(cmd ,shell=True)







TabletSetup = tk.Tk()
TabletSetup.title("RADIANT-TABLET-SETUP")
TabletSetup.geometry('600x300')

label1 = tk.Label(TabletSetup, text='TT Folder Change Name')
label1.place(x=0, y=0)

# TTlabel= tk.Label(TabletSetup, text='TrueTest1.8')
# TTlabel.place(x=0, y=20)


def change_text():
	    
	# TTlabel['text'] = 'TrueTest1.8 old' 
    # TTlabel.place(x=0, y=20)
#  print(os.system('tasklist'))
	# os.system('taskkill /f /im TrueTestWatcher.exe') #프로세스명을 사용한 프로세스 종료
 for proc in psutil.process_iter():
        if proc.name() == "TrueTestWatcher.exe" :
            proc.kill()
        if proc.name() == "FTPUploaderVB.exe" :
            proc.kill()
        if proc.name() == "SetSequence.exe" :
            proc.kill()
 time.sleep(1)

#  def get_version_number (filename):
#   info = GetFileVersionInfo (filename, "C:\Program Files\Radiant Vision Systems\TrueTest 1.8','C:\Program Files\Radiant Vision Systems\TrueTest 1.8 old")
#   ms = info['FileVersionMS']
#   ls = info['FileVersionLS']
#   print(ms,ls)
#   return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)

#  TTlabel['text'] = 'TrueTest1.8 old' 

#  os.rename('C:\Program Files\Radiant Vision Systems\TrueTest 1.8','C:\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
    # print(label1['text'])

# button1 = tk.Button(TabletSetup, text='click', command=change_text)
#  copyfolder=r"C:\Program Files\Radiant Vision Systems"
#  source = r"F:\Copy"
#  shutil.copytree(source,copyfolder,dirs_exist_ok=True) 

 copyfolder=r"C:\Program Files\Radiant Vision Systems\TrueTest 1.8" 
 source = r"F:\Copy"
 shutil.copytree(source,copyfolder,dirs_exist_ok=True) 

#  time.sleep(3)

#  zip_ref = zipfile.ZipFile('C:\Program Files\Radiant Vision Systems\TrueTest 1.8.zip')
#  zip_ref.extractall('C:\Program Files\Radiant Vision Systems\TrueTest 1.8')
#  zip_ref.close()

#  time.sleep(10)


 
#  subprocess.Popen('C:\Program Files\Radiant Vision Systems\TrueTest 1.8\TrueTest.exe').wait(1)


button1=tk.Button(TabletSetup, text="Run", height=1, width=3, command=change_text)
button1.place(x=0, y=30)





label2 = tk.Label(TabletSetup, text='Sequence Backup')
label2.place(x=150, y=0)



def SequenceBackup():
 def get_today():
    now = time.localtime()
    s = "%02d%02d%02d%02d%02d%02d" % (now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
    return s

 def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

 backuppath=r"D:\Radiant Vision Systems Data\TrueTest\Sequence"
 today=get_today()
 backup_dir=backuppath +"/"+ today

 if not backuppath:
  os.mkdir(backuppath)
  make_folder(backup_dir)


 source = r"C:\Radiant Vision Systems Data\TrueTest\Sequence"



 if __name__ == '__main__':
    shutil.copytree(
        source,
        backup_dir,
        dirs_exist_ok=True
    )



 sourcepath = r"C:\Radiant Vision Systems Data\TrueTest\Sequence\*.seqxc"
 filelist=glob.glob(sourcepath)
 destination1 = r"C:\Radiant Vision Systems Data\TrueTest\Sequence\Master"
 destination2 = r"C:\Radiant Vision Systems Data\TrueTest\Sequence\Calibration"


 for src in filelist:
    f = os.path.basename(src)
    tgt1 = os.path.join(destination1, f)
    tgt2 = os.path.join(destination2, f)
    shutil.copyfile(src, tgt1)
    shutil.copyfile(src, tgt2)
    

button2 = tk.Button(TabletSetup, text='click', command=SequenceBackup)
button2.place(x=150, y=30)







label3 = tk.Label(TabletSetup, text='TrueTest 1.8.zip copy')
label3.place(x=300, y=0)

def FileCopy():
	copyfolder=r"C:\Program Files\Radiant Vision Systems"
	dir_path = filedialog.askdirectory(initialdir="/",\
					title = "폴더를 선택 해 주세요")
	#folder 변수에 선택 폴더 경로 넣기

	if dir_path == '':
		messagebox.showwarning("경고", "폴더를 선택 하세요")    #폴더 선택 안했을 때 메세지 출력
	else:
		res = os.listdir(dir_path) # 폴더에 있는 파일 리스트 넣기

		print(res)    #folder내 파일 목록 값 출력

		if len(res) == 0:
			messagebox.showwarning("경고", "폴더내 파일이 없습니다.")
		else:
			for file in res:	           
				# if __name__ == '__main__':
                           shutil.copytree(dir_path,copyfolder,dirs_exist_ok=True)  
    # backup_dir=backuppath

    # if not copyfolder:
    #   os.mkdir(copyfolder)
    #   make_folder(copyfolder)


    # source = r"F:\Copy"



    

		
				# print(dir_path + "/" + file) # 파일/폴더 목록 하나씩 출력하기
# def FileCopy():
#     # def make_folder(folder_name):
#     #  if not os.path.isdir(folder_name):
#     #     os.mkdir(folder_name)

#     copyfolder=r"C:\Program Files\Radiant Vision Systems"
#     # backup_dir=backuppath

#     # if not copyfolder:
#     #   os.mkdir(copyfolder)
#     #   make_folder(copyfolder)


#     # source = r"F:\Copy"



#     if __name__ == '__main__':
#      shutil.copytree(
#         res,
#         copyfolder,
#         dirs_exist_ok=True
#      )  

# button3 = tk.Button(TabletSetup, text='Open', command=FolderOpen)
# button3.place(x=300, y=30)


button3 = tk.Button(TabletSetup, text='Copy', command=FileCopy)
button3.place(x=350, y=30)









# label4 = tk.Label(TabletSetup, text='Test')
# label4.place(x=500, y=0)

# def Test():
 
# 	dir_path = filedialog.askdirectory(initialdir="/",\
# 					title = "폴더를 선택 해 주세요")
# 	#folder 변수에 선택 폴더 경로 넣기

# 	if dir_path == '':
# 		messagebox.showwarning("경고", "폴더를 선택 하세요")    #폴더 선택 안했을 때 메세지 출력
# 	else:
# 		res = os.listdir(dir_path) # 폴더에 있는 파일 리스트 넣기

# 		print(res)    #folder내 파일 목록 값 출력

# 		if len(res) == 0:
# 			messagebox.showwarning("경고", "폴더내 파일이 없습니다.")
# 		else:
# 			for file in res:
# 				print(dir_path + "/" + file) # 파일/폴더 목록 하나씩 출력하기

# button4 = tk.Button(TabletSetup, text='click', command=Test)
# button4.place(x=500, y=30)





label5 = tk.Label(TabletSetup, text='Quit TrueTest1.8')
label5.place(x=0, y=100)

# TTlabel= tk.Label(TabletSetup, text='TrueTest1.8')
# TTlabel.place(x=0, y=20)


def Quit_tt():
	    
	# TTlabel['text'] = 'TrueTest1.8 old' 
    # TTlabel.place(x=0, y=20)
#  print(os.system('tasklist'))
	# os.system('taskkill /f /im TrueTestWatcher.exe') #프로세스명을 사용한 프로세스 종료
 for proc in psutil.process_iter():
        if proc.name() == "TrueTestWatcher.exe" :
            proc.kill()
        if proc.name() == "FTPUploaderVB.exe" :
            proc.kill()
        if proc.name() == "SetSequence.exe" :
            proc.kill()
        if proc.name() == "TrueTest.exe" :
            proc.kill()
 time.sleep(0)

#  def get_version_number (filename):
#   info = GetFileVersionInfo (filename, "C:\Program Files\Radiant Vision Systems\TrueTest 1.8','C:\Program Files\Radiant Vision Systems\TrueTest 1.8 old")
#   ms = info['FileVersionMS']
#   ls = info['FileVersionLS']
#   print(ms,ls)
#   return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)

#  TTlabel['text'] = 'TrueTest1.8 old' 

#  os.rename('C:\Program Files\Radiant Vision Systems\TrueTest 1.8','C:\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
    # print(label1['text'])

# button1 = tk.Button(TabletSetup, text='click', command=change_text)
#  copyfolder=r"C:\Program Files\Radiant Vision Systems"
#  source = r"F:\Copy"
#  shutil.copytree(source,copyfolder,dirs_exist_ok=True) 

 copyfolder=r"C:\Program Files\Radiant Vision Systems\TrueTest 1.8" 
 source = r"c\Program Files\Radiant Vision Systems"
 shutil.copytree(source,copyfolder,dirs_exist_ok=True) 

#  time.sleep(3)

#  zip_ref = zipfile.ZipFile('C:\Program Files\Radiant Vision Systems\TrueTest 1.8.zip')
#  zip_ref.extractall('C:\Program Files\Radiant Vision Systems\TrueTest 1.8')
#  zip_ref.close()

#  time.sleep(10)


 
#  subprocess.Popen('C:\Program Files\Radiant Vision Systems\TrueTest 1.8\TrueTest.exe').wait(1)


button5=tk.Button(TabletSetup, text="Run", height=1, width=3, command=Quit_tt)
button5.place(x=0, y=120)


def QuitAll():	  
   
	
 for proc in psutil.process_iter():
        if proc.name() == "TrueTestWatcher.exe" :
            proc.kill()
        if proc.name() == "FTPUploaderVB.exe" :
            proc.kill()
        if proc.name() == "SetSequence.exe" :
            proc.kill()
        if proc.name() == "TrueTest.exe" :
            proc.kill()
#  time.sleep(0)

QuitAll=tk.Button(TabletSetup, text="All", height=1, width=3, command=QuitAll)
QuitAll.place(x=30, y=120)








label6 = tk.Label(TabletSetup, text='Dll copy')
label6.place(x=300, y=100)
label8 = tk.Label(TabletSetup, text='D:\program\RVS\copy')
label8.place(x=300, y=120)

def FileCopy():
	# copyfolder=r"C:\Program Files\Radiant Vision Systems\TrueTest 1.8"
	# dir_path = filedialog.askdirectory(initialdir="/",\
	# 				title = "폴더를 선택 해 주세요")
	# #folder 변수에 선택 폴더 경로 넣기

	# if dir_path == '':
	# 	messagebox.showwarning("경고", "폴더를 선택 하세요")    #폴더 선택 안했을 때 메세지 출력
	# else:
	# 	res = os.listdir(dir_path) # 폴더에 있는 파일 리스트 넣기

	# 	print(res)    #folder내 파일 목록 값 출력

	# 	if len(res) == 0:
	# 		messagebox.showwarning("경고", "폴더내 파일이 없습니다.")
	# 	else:
	# 		for file in res:	           
	# 			# if __name__ == '__main__':
    #                        shutil.copytree(dir_path,copyfolder,dirs_exist_ok=True)  
    # backup_dir=backuppath

    # if not copyfolder:
    #   os.mkdir(copyfolder)
    #   make_folder(copyfolder)


    # source = r"F:\Copy"

 copyfolder=r"C:\Program Files\Radiant Vision Systems\TrueTest 1.8" 
 source = r"F:\Copy"
 shutil.copytree(source,copyfolder,dirs_exist_ok=True)

 time.sleep(1)

 subprocess.Popen('C:\Program Files\Radiant Vision Systems\TrueTest 1.8\TrueTest.exe').wait(1)

    

		
				# print(dir_path + "/" + file) # 파일/폴더 목록 하나씩 출력하기
# def FileCopy():
#     # def make_folder(folder_name):
#     #  if not os.path.isdir(folder_name):
#     #     os.mkdir(folder_name)

#     copyfolder=r"C:\Program Files\Radiant Vision Systems"
#     # backup_dir=backuppath

#     # if not copyfolder:
#     #   os.mkdir(copyfolder)
#     #   make_folder(copyfolder)


#     # source = r"F:\Copy"



#     if __name__ == '__main__':
#      shutil.copytree(
#         res,
#         copyfolder,
#         dirs_exist_ok=True
#      )  

# button3 = tk.Button(TabletSetup, text='Open', command=FolderOpen)
# button3.place(x=300, y=30)


button3 = tk.Button(TabletSetup, text='Copy', command=FileCopy)
button3.place(x=300, y=150)







label7 = tk.Label(TabletSetup, text='Dll copy to all pc')
label7.place(x=450, y=100)

def FileCopy():
 
#   local_path='F:/Copy/'
#   file=r'/Dove2p0_PG.dll'
#   network_path=r"//192.168.1.200"
#   network_internal_path=r"//192.168.1.200/E:/Program/RVS"

#   os.chdir(network_path)
#   shutil.copy(local_path+file,network_internal_path+file)
  


#  copyfolder1=r"\\10.122.50.19\D:\program\RVS\copy"
#  copyfolder2=r"\\10.122.50.20\D:\program\RVS\copy"
#  copyfolder3=r"\\10.122.50.17\D:\program\RVS\copy"
#  copyfolder4=r"\\10.122.50.18\D:\program\RVS\copy"
#  copyfolder5=r"\\10.122.50.15\D:\program\RVS\copy"
#  copyfolder6=r"\\10.122.50.241\D:\program\RVS\copy"
#  copyfolder7=r"\\10.122.50.26\D:\program\RVS\copy"
#  copyfolder8=r"\\10.122.50.27\D:\program\RVS\copy"
#  copyfolder9=r"\\10.122.50.28\D:\program\RVS\copy"
#  copyfolder10=r"\\10.122.50.64\D:\program\RVS\copy"
#  copyfolder11=r"\\10.122.50.30\D:\program\RVS\copy"
#  copyfolder12=r"\\10.122.50.38\D:\program\RVS\copy"
#  copyfolder13=r"\\10.122.50.204\D:\program\RVS\copy"
#  copyfolder14=r"\\10.122.50.205\D:\program\RVS\copy"
#  copyfolder15=r"\\10.122.50.206\D:\program\RVS\copy"
#  copyfolder16=r"\\10.122.50.207\D:\program\RVS\copy"
#  copyfolder17=r"\\10.122.50.208\D:\program\RVS\copy"
#  copyfolder18=r"\\10.122.50.209\D:\program\RVS\copy"
#  copyfolder19=r"\\10.122.50.195\D:\program\RVS\copy"
#  copyfolder20=r"\\10.122.50.196\D:\program\RVS\copy"
#  copyfolder21=r"\\10.122.50.197\D:\program\RVS\copy"
#  copyfolder22=r"\\10.122.50.198\D:\program\RVS\copy"
#  copyfolder23=r"\\10.122.50.199\D:\program\RVS\copy"
#  copyfolder24=r"\\10.122.50.200\D:\program\RVS\copy"
#  copyfolder25=r"\\10.122.50.213\D:\program\RVS\copy"
#  copyfolder26=r"\\10.122.50.214\D:\program\RVS\copy"
#  copyfolder27=r"\\10.122.51.52\D:\program\RVS\copy"
#  copyfolder28=r"\\10.122.51.53\D:\program\RVS\copy"
#  copyfolder29=r"\\10.122.50.215\D:\program\RVS\copy"
#  copyfolder30=r"\\10.122.50.216\D:\program\RVS\copy"
#  copyfolder31=r"\\10.122.51.54\D:\program\RVS\copy"
#  copyfolder32=r"\\10.122.51.55\D:\program\RVS\copy"
#  copyfolder33=r"\\10.122.51.56\D:\program\RVS\copy"
#  copyfolder34=r"\\10.122.51.57\D:\program\RVS\copy"
#  copyfolder35=r"\\10.122.51.87\D:\program\RVS\copy"
#  copyfolder36=r"\\10.122.51.88\D:\program\RVS\copy"
#  copyfolder37=r"\\10.122.51.91\D:\program\RVS\copy"
#  copyfolder38=r"\\10.122.51.92\D:\program\RVS\copy"
#  copyfolder39=r"\\10.122.51.89\D:\program\RVS\copy"
#  copyfolder40=r"\\10.122.51.90\D:\program\RVS\copy"
#  copyfolder41=r"\\10.122.51.101\D:\program\RVS\copy"
#  copyfolder42=r"\\10.122.51.102\D:\program\RVS\copy"
#  copyfolder43=r"\\10.122.50.99\D:\program\RVS\copy"
#  copyfolder44=r"\\10.122.51.100\D:\program\RVS\copy"
#  copyfolder45=r"\\10.122.51.103\D:\program\RVS\copy"
#  copyfolder46=r"\\10.122.51.104\D:\program\RVS\copy"
 copyfolderTEST=r"\\192.168.1.200\e\Program\RVS\Copy"
 def make_folder(copyfolderTEST):
    if not os.path.isdir(copyfolderTEST):
        os.mkdir(copyfolderTEST)
 source = r"F:\Copy"
 shutil.copytree(source,copyfolderTEST,dirs_exist_ok=True)
 
 
#  shutil.copytree(source,copyfolder1,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder2,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder3,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder4,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder5,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder6,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder7,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder8,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder9,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder10,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder11,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder12,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder13,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder14,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder15,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder16,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder17,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder18,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder19,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder20,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder21,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder22,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder23,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder24,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder25,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder26,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder27,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder28,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder29,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder30,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder31,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder32,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder33,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder34,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder35,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder36,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder37,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder38,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder39,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder40,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder41,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder42,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder43,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder44,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder45,dirs_exist_ok=True)
#  shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
   

    

		


button6 = tk.Button(TabletSetup, text='Copy', command=FileCopy)
button6.place(x=450, y=150)





TTZIPlb = tk.Label(TabletSetup, text='TrueTest 1.8.zip copy')
TTZIPlb.place(x=500, y=100)

def TTZIP():
 
 copyfolderTEST=r"\\192.168.1.200\e\Program Files\Radiant Vision Systems"
 copyfolder1=r"\\10.122.50.19\c\Program Files\Radiant Vision Systems"
 copyfolder2=r"\\10.122.50.20\c\Program Files\Radiant Vision Systems"
 copyfolder3=r"\\10.122.50.17\c\Program Files\Radiant Vision Systems"
 copyfolder4=r"\\10.122.50.18\c\Program Files\Radiant Vision Systems"
 copyfolder5=r"\\10.122.50.15\c\Program Files\Radiant Vision Systems"
 copyfolder6=r"\\10.122.50.241\c\Program Files\Radiant Vision Systems"
 copyfolder7=r"\\10.122.50.26\c\Program Files\Radiant Vision Systems"
 copyfolder8=r"\\10.122.50.27\c\Program Files\Radiant Vision Systems"
 copyfolder9=r"\\10.122.50.28\c\Program Files\Radiant Vision Systems"
 copyfolder10=r"\\10.122.50.64\c\Program Files\Radiant Vision Systems"
 copyfolder11=r"\\10.122.50.30\c\Program Files\Radiant Vision Systems"
 copyfolder12=r"\\10.122.50.38\c\Program Files\Radiant Vision Systems"
 copyfolder13=r"\\10.122.50.204\c\Program Files\Radiant Vision Systems"
 copyfolder14=r"\\10.122.50.205\c\Program Files\Radiant Vision Systems"
 copyfolder15=r"\\10.122.50.206\c\Program Files\Radiant Vision Systems"
 copyfolder16=r"\\10.122.50.207\c\Program Files\Radiant Vision Systems"
 copyfolder17=r"\\10.122.50.208\c\Program Files\Radiant Vision Systems"
 copyfolder18=r"\\10.122.50.209\c\Program Files\Radiant Vision Systems"
 copyfolder19=r"\\10.122.50.195\c\Program Files\Radiant Vision Systems"
 copyfolder20=r"\\10.122.50.196\c\Program Files\Radiant Vision Systems"
 copyfolder21=r"\\10.122.50.197\c\Program Files\Radiant Vision Systems"
 copyfolder22=r"\\10.122.50.198\c\Program Files\Radiant Vision Systems"
 copyfolder23=r"\\10.122.50.199\c\Program Files\Radiant Vision Systems"
 copyfolder24=r"\\10.122.50.200\c\Program Files\Radiant Vision Systems"
 copyfolder25=r"\\10.122.50.213\c\Program Files\Radiant Vision Systems"
 copyfolder26=r"\\10.122.50.214\c\Program Files\Radiant Vision Systems"
 copyfolder27=r"\\10.122.51.52\c\Program Files\Radiant Vision Systems"
 copyfolder28=r"\\10.122.51.53\c\Program Files\Radiant Vision Systems"
 copyfolder29=r"\\10.122.50.215\c\Program Files\Radiant Vision Systems"
 copyfolder30=r"\\10.122.50.216\c\Program Files\Radiant Vision Systems"
 copyfolder31=r"\\10.122.51.54\c\Program Files\Radiant Vision Systems"
 copyfolder32=r"\\10.122.51.55\c\Program Files\Radiant Vision Systems"
 copyfolder33=r"\\10.122.51.56\c\Program Files\Radiant Vision Systems"
 copyfolder34=r"\\10.122.51.57\c\Program Files\Radiant Vision Systems"
 copyfolder35=r"\\10.122.51.87\c\Program Files\Radiant Vision Systems"
 copyfolder36=r"\\10.122.51.88\c\Program Files\Radiant Vision Systems"
 copyfolder37=r"\\10.122.51.91\c\Program Files\Radiant Vision Systems"
 copyfolder38=r"\\10.122.51.92\c\Program Files\Radiant Vision Systems"
 copyfolder39=r"\\10.122.51.89\c\Program Files\Radiant Vision Systems"
 copyfolder40=r"\\10.122.51.90\c\Program Files\Radiant Vision Systems"
 copyfolder41=r"\\10.122.51.101\c\Program Files\Radiant Vision Systems"
 copyfolder42=r"\\10.122.51.102\c\Program Files\Radiant Vision Systems"
 copyfolder43=r"\\10.122.50.99\c\Program Files\Radiant Vision Systems"
 copyfolder44=r"\\10.122.51.100\c\Program Files\Radiant Vision Systems"
 copyfolder45=r"\\10.122.51.103\c\Program Files\Radiant Vision Systems"
 copyfolder46=r"\\10.122.51.104\c\Program Files\Radiant Vision Systems"

 

 source = r"F:\Copy"


 shutil.copytree(source,copyfolderTEST,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder1,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder2,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder3,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder4,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder5,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder6,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder7,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder8,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder9,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder10,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder11,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder12,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder13,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder14,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder15,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder16,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder17,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder18,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder19,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder20,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder21,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder22,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder23,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder24,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder25,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder26,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder27,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder28,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder29,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder30,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder31,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder32,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder33,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder34,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder35,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder36,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder37,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder38,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder39,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder40,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder41,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder42,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder43,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder44,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder45,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder46,dirs_exist_ok=True)


TTZIPbtn = tk.Button(TabletSetup, text='501L-1st', command=TTZIP)
TTZIPbtn.place(x=600, y=150)

def TTZIP501M():
 
 copyfolderTEST=r"\\192.168.1.200\e\Program Files\Radiant Vision Systems"
 copyfolder1=r"\\10.122.50.19\c\Program Files\Radiant Vision Systems"
 copyfolder2=r"\\10.122.50.20\c\Program Files\Radiant Vision Systems"
 copyfolder3=r"\\10.122.50.17\c\Program Files\Radiant Vision Systems"
 copyfolder4=r"\\10.122.50.18\c\Program Files\Radiant Vision Systems"
 copyfolder5=r"\\10.122.50.15\c\Program Files\Radiant Vision Systems"
 copyfolder6=r"\\10.122.50.241\c\Program Files\Radiant Vision Systems"
 copyfolder7=r"\\10.122.50.26\c\Program Files\Radiant Vision Systems"
 copyfolder8=r"\\10.122.50.27\c\Program Files\Radiant Vision Systems"
 copyfolder9=r"\\10.122.50.28\c\Program Files\Radiant Vision Systems"
 copyfolder10=r"\\10.122.50.64\c\Program Files\Radiant Vision Systems"
 copyfolder11=r"\\10.122.50.30\c\Program Files\Radiant Vision Systems"
 copyfolder12=r"\\10.122.50.38\c\Program Files\Radiant Vision Systems"
 copyfolder13=r"\\10.122.50.204\c\Program Files\Radiant Vision Systems"
 copyfolder14=r"\\10.122.50.205\c\Program Files\Radiant Vision Systems"
 copyfolder15=r"\\10.122.50.206\c\Program Files\Radiant Vision Systems"
 copyfolder16=r"\\10.122.50.207\c\Program Files\Radiant Vision Systems"
 copyfolder17=r"\\10.122.50.208\c\Program Files\Radiant Vision Systems"
 copyfolder18=r"\\10.122.50.209\c\Program Files\Radiant Vision Systems"
 copyfolder19=r"\\10.122.50.195\c\Program Files\Radiant Vision Systems"
 copyfolder20=r"\\10.122.50.196\c\Program Files\Radiant Vision Systems"
 copyfolder21=r"\\10.122.50.197\c\Program Files\Radiant Vision Systems"
 copyfolder22=r"\\10.122.50.198\c\Program Files\Radiant Vision Systems"
 copyfolder23=r"\\10.122.50.199\c\Program Files\Radiant Vision Systems"
 copyfolder24=r"\\10.122.50.200\c\Program Files\Radiant Vision Systems"
 copyfolder25=r"\\10.122.50.213\c\Program Files\Radiant Vision Systems"
 copyfolder26=r"\\10.122.50.214\c\Program Files\Radiant Vision Systems"
 copyfolder27=r"\\10.122.51.52\c\Program Files\Radiant Vision Systems"
 copyfolder28=r"\\10.122.51.53\c\Program Files\Radiant Vision Systems"
 copyfolder29=r"\\10.122.50.215\c\Program Files\Radiant Vision Systems"
 copyfolder30=r"\\10.122.50.216\c\Program Files\Radiant Vision Systems"
 copyfolder31=r"\\10.122.51.54\c\Program Files\Radiant Vision Systems"
 copyfolder32=r"\\10.122.51.55\c\Program Files\Radiant Vision Systems"
 copyfolder33=r"\\10.122.51.56\c\Program Files\Radiant Vision Systems"
 copyfolder34=r"\\10.122.51.57\c\Program Files\Radiant Vision Systems"
 copyfolder35=r"\\10.122.51.87\c\Program Files\Radiant Vision Systems"
 copyfolder36=r"\\10.122.51.88\c\Program Files\Radiant Vision Systems"
 copyfolder37=r"\\10.122.51.91\c\Program Files\Radiant Vision Systems"
 copyfolder38=r"\\10.122.51.92\c\Program Files\Radiant Vision Systems"
 copyfolder39=r"\\10.122.51.89\c\Program Files\Radiant Vision Systems"
 copyfolder40=r"\\10.122.51.90\c\Program Files\Radiant Vision Systems"
 copyfolder41=r"\\10.122.51.101\c\Program Files\Radiant Vision Systems"
 copyfolder42=r"\\10.122.51.102\c\Program Files\Radiant Vision Systems"
 copyfolder43=r"\\10.122.50.99\c\Program Files\Radiant Vision Systems"
 copyfolder44=r"\\10.122.51.100\c\Program Files\Radiant Vision Systems"
 copyfolder45=r"\\10.122.51.103\c\Program Files\Radiant Vision Systems"
 copyfolder46=r"\\10.122.51.104\c\Program Files\Radiant Vision Systems"

 

 source = r"F:\Copy"


 shutil.copytree(source,copyfolderTEST,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder1,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder2,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder3,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder4,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder5,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder6,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder7,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder8,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder9,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder10,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder11,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder12,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder13,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder14,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder15,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder16,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder17,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder18,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder19,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder20,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder21,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder22,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder23,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder24,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder25,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder26,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder27,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder28,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder29,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder30,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder31,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder32,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder33,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder34,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder35,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder36,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder37,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder38,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder39,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder40,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder41,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder42,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder43,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder44,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder45,dirs_exist_ok=True)
 shutil.copytree(source,copyfolder46,dirs_exist_ok=True)

def TTZIP501C():
    shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
def TTZIP502M():
    shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
def TTZIP502C():
    shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
def TTZIP503M():
    shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
def TTZIP503C():
    shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
def TTZIP504M():
    shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
def TTZIP504C():
    shutil.copytree(source,copyfolder46,dirs_exist_ok=True)
    
TTZIP501Mbtn = tk.Button(TabletSetup, text='501L-1st', command=TTZIP501M)
TTZIP501Mbtn.place(x=600, y=150)
TTZIP501Cbtn = tk.Button(TabletSetup, text='501L-2nd', command=TTZIP501C)
TTZIP501Cbtn.place(x=600, y=175)
TTZIP502Mbtn = tk.Button(TabletSetup, text='502L-1st', command=TTZIP502M)
TTZIP502Mbtn.place(x=600, y=200)
TTZIP502Cbtn = tk.Button(TabletSetup, text='502L-2nd', command=TTZIP502C)
TTZIP502Cbtn.place(x=600, y=225)
TTZIP503Mbtn = tk.Button(TabletSetup, text='503L-1st', command=TTZIP503M)
TTZIP503Mbtn.place(x=600, y=250)
TTZIP503Cbtn = tk.Button(TabletSetup, text='503L-2nd', command=TTZIP503C)
TTZIP503Cbtn.place(x=600, y=275)
TTZIP504Mbtn = tk.Button(TabletSetup, text='504L-1st', command=TTZIP504M)
TTZIP504Mbtn.place(x=600, y=300)
TTZIP504Cbtn = tk.Button(TabletSetup, text='504L-2nd', command=TTZIP504C)
TTZIP504Cbtn.place(x=600, y=325)



TabletSetup.mainloop()