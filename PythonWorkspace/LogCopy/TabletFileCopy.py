import shutil
import os
import glob
import time
from datetime import datetime
from os import path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox




window = tk.Tk()
window.title("RADIANT-TABLET-SETUP")
window.geometry('700x100')


label1 = tk.Label(window, text='LogBackup')
label1.place(x=150, y=0)


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

#  if not backuppath:
#   os.mkdir(backuppath)
#   make_folder(backup_dir)


#  source = r"C:\Radiant Vision Systems Data\TrueTest\AppData"
 


#  if __name__ == '__main__':
#     shutil.copyfile(
#         sourcefile,
#         backup_dir,
#         dirs_exist_ok=True
#     )



 sourcepath = r"C:\Radiant Vision Systems Data\TrueTest\Sequence\*.txt"
 filelist=glob.glob(sourcepath)
 destination1 = r"D:\Program\RVS\Log"
#  destination2 = r"C:\Radiant Vision Systems Data\TrueTest\Sequence\Calibration"

 if not destination1:
  os.mkdir(destination1)
  make_folder(backup_dir)

 for src in filelist:
    f = os.path.basename(src)
    tgt1 = os.path.join(destination1, f)
    # tgt2 = os.path.join(destination2, f)
    shutil.copyfile(src, tgt1)
    # shutil.copyfile(src, tgt2)
    

button2 = tk.Button(window, text='click', command=SequenceBackup)
button2.place(x=150, y=30)
















window.mainloop()