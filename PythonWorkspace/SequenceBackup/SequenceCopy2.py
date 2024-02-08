import shutil
import os
import glob
import time
from datetime import datetime

#get today date
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


    

