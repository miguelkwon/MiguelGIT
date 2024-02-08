import shutil
import os
import glob
import time
from datetime import datetime
from os import path
import tkinter as tk









window = tk.Tk()
window.title("RADIANT-TABLET-SETUP")
window.geometry('500x100')

label1 = tk.Label(window, text='TrueTest1.8 -> 1.8. xxxx')
label1.place(x=0, y=0)

def change_text():
    label1['text'] = 'New Text'
    os.rename('C:\Program Files\Radiant Vision Systems\TrueTest 1.8','C:\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
    # print(label1['text'])

button1 = tk.Button(window, text='click', command=change_text)
button1.place(x=10, y=30)





label2 = tk.Label(window, text='Sequence Backup')
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
    

button2 = tk.Button(window, text='click', command=SequenceBackup)
button2.place(x=150, y=30)







label3 = tk.Label(window, text='File Copy')
label3.place(x=300, y=0)

def FileCopy():
    # def make_folder(folder_name):
    #  if not os.path.isdir(folder_name):
    #     os.mkdir(folder_name)

    copyfolder=r"C:\Program Files\Radiant Vision Systems"
    # backup_dir=backuppath

    # if not copyfolder:
    #   os.mkdir(copyfolder)
    #   make_folder(copyfolder)


    source = r"F:\Copy"



    if __name__ == '__main__':
     shutil.copytree(
        source,
        copyfolder,
        dirs_exist_ok=True
    )  

button3 = tk.Button(window, text='click', command=FileCopy)
button3.place(x=300, y=30)



label3 = tk.Label(window, text='File Copy')
label3.place(x=300, y=0)
































window.mainloop()