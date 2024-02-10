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
import tkinter.ttk as ttk 
# import paramiko
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import sys
from datetime import datetime
from os import path
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import random
from tqdm.notebook import tqdm
import os, sys
import subprocess
import threading
import time
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel








win = tk.Tk()
win.title("RADIANT-TABLET-SETUP")
win.geometry('900x600')


# progressbar = ttk.Progressbar(win, maximum=100, mode="indeterminate")
# progressbar.pack()



TTZIPCOPYlb = tk.Label(win, text='TrueTest 1.8.zip copy')
TTZIPCOPYlb.place(x=0, y=0)

TTQUITlb = tk.Label(win, text='TrueTest 1.8 Quit')
TTQUITlb.place(x=150, y=0)

RENAMEFOLDERlb = tk.Label(win, text='TT folder change name')
RENAMEFOLDERlb.place(x=300, y=0)

DLLCOPYlb = tk.Label(win, text='DLLCOPY')
DLLCOPYlb.place(x=450, y=0)

RUNTTlb = tk.Label(win, text='Run TrueTest')
RUNTTlb.place(x=600, y=0)


def Test():
  
  copyfolder=r"C:\Program Files\Radiant Vision Systems"
  source = r"F:\Copy"
  shutil.copytree(source,copyfolder,dirs_exist_ok=True)
  messagebox.showinfo("!!!!!!!","복사 완료")
 
  
 

def TTZIP501M():
 
#  copyfolderTEST=r"\\192.168.1.200\e\Program Files\Radiant Vision Systems"
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


 source = r"F:\Copy"
 #  shutil.copytree(source,copyfolderTEST,dirs_exist_ok=True)
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
 
def TTZIP501C():
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

def TTZIP502M():
 copyfolder1=r"\\10.122.51.183\c\Program Files\Radiant Vision Systems"
 copyfolder2=r"\\10.122.51.184\c\Program Files\Radiant Vision Systems"
 copyfolder3=r"\\10.122.51.185\c\Program Files\Radiant Vision Systems"
 copyfolder4=r"\\10.122.51.186\c\Program Files\Radiant Vision Systems"
 copyfolder5=r"\\10.122.51.187\c\Program Files\Radiant Vision Systems"
 copyfolder6=r"\\10.122.51.188\c\Program Files\Radiant Vision Systems"
 copyfolder7=r"\\10.122.51.192\c\Program Files\Radiant Vision Systems"
 copyfolder8=r"\\10.122.51.193\c\Program Files\Radiant Vision Systems"
 copyfolder9=r"\\10.122.51.194\c\Program Files\Radiant Vision Systems"
 copyfolder10=r"\\10.122.51.195\c\Program Files\Radiant Vision Systems"
 copyfolder11=r"\\10.122.51.196\c\Program Files\Radiant Vision Systems"
 copyfolder12=r"\\10.122.51.197\c\Program Files\Radiant Vision Systems"
 copyfolder13=r"\\10.122.51.201\c\Program Files\Radiant Vision Systems"
 copyfolder14=r"\\10.122.51.202\c\Program Files\Radiant Vision Systems"
 copyfolder15=r"\\10.122.51.203\c\Program Files\Radiant Vision Systems"
 copyfolder16=r"\\10.122.51.204\c\Program Files\Radiant Vision Systems"
 copyfolder17=r"\\10.122.51.205\c\Program Files\Radiant Vision Systems"
 copyfolder18=r"\\10.122.51.206\c\Program Files\Radiant Vision Systems"
 copyfolder19=r"\\10.122.51.210\c\Program Files\Radiant Vision Systems"
 copyfolder20=r"\\10.122.51.211\c\Program Files\Radiant Vision Systems"
 copyfolder21=r"\\10.122.51.212\c\Program Files\Radiant Vision Systems"
 copyfolder22=r"\\10.122.51.213\c\Program Files\Radiant Vision Systems"
 copyfolder23=r"\\10.122.51.214\c\Program Files\Radiant Vision Systems"
 copyfolder24=r"\\10.122.51.215\c\Program Files\Radiant Vision Systems"
 
 source = r"F:\Copy"

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
 
def TTZIP502C():
 
 copyfolder25=r"\\10.122.51.219\c\Program Files\Radiant Vision Systems"
 copyfolder26=r"\\10.122.51.220\c\Program Files\Radiant Vision Systems"
 copyfolder27=r"\\10.122.51.221\c\Program Files\Radiant Vision Systems"
 copyfolder28=r"\\10.122.51.222\c\Program Files\Radiant Vision Systems"
 copyfolder29=r"\\10.122.51.223\c\Program Files\Radiant Vision Systems"
 copyfolder30=r"\\10.122.51.224\c\Program Files\Radiant Vision Systems"
 copyfolder31=r"\\10.122.51.228\c\Program Files\Radiant Vision Systems"
 copyfolder32=r"\\10.122.51.229\c\Program Files\Radiant Vision Systems"
 copyfolder33=r"\\10.122.51.230\c\Program Files\Radiant Vision Systems"
 copyfolder34=r"\\10.122.51.231\c\Program Files\Radiant Vision Systems"
 copyfolder35=r"\\10.122.51.232\c\Program Files\Radiant Vision Systems"
 copyfolder36=r"\\10.122.51.233\c\Program Files\Radiant Vision Systems"
 copyfolder37=r"\\10.122.51.237\c\Program Files\Radiant Vision Systems"
 copyfolder38=r"\\10.122.51.238\c\Program Files\Radiant Vision Systems"
 copyfolder39=r"\\10.122.51.239\c\Program Files\Radiant Vision Systems"
 copyfolder40=r"\\10.122.51.240\c\Program Files\Radiant Vision Systems"
 copyfolder41=r"\\10.122.51.241\c\Program Files\Radiant Vision Systems"
 copyfolder42=r"\\10.122.51.242\c\Program Files\Radiant Vision Systems"
 copyfolder43=r"\\10.122.51.246\c\Program Files\Radiant Vision Systems"
 copyfolder44=r"\\10.122.51.247\c\Program Files\Radiant Vision Systems"
 copyfolder45=r"\\10.122.51.248\c\Program Files\Radiant Vision Systems"
 copyfolder46=r"\\10.122.51.249\c\Program Files\Radiant Vision Systems"

 source = r"F:\Copy"
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

def TTZIP503M():
 copyfolder1=r"\\10.122.52.73\c\Program Files\Radiant Vision Systems"
 copyfolder2=r"\\10.122.52.74\c\Program Files\Radiant Vision Systems"
 copyfolder3=r"\\10.122.52.75\c\Program Files\Radiant Vision Systems"
 copyfolder4=r"\\10.122.52.76\c\Program Files\Radiant Vision Systems"
 copyfolder5=r"\\10.122.52.77\c\Program Files\Radiant Vision Systems"
 copyfolder6=r"\\10.122.52.78\c\Program Files\Radiant Vision Systems"
 copyfolder7=r"\\10.122.52.87\c\Program Files\Radiant Vision Systems"
 copyfolder8=r"\\10.122.52.88\c\Program Files\Radiant Vision Systems"
 copyfolder9=r"\\10.122.52.89\c\Program Files\Radiant Vision Systems"
 copyfolder10=r"\\10.122.52.90\c\Program Files\Radiant Vision Systems"
 copyfolder11=r"\\10.122.52.91\c\Program Files\Radiant Vision Systems"
 copyfolder12=r"\\10.122.52.92\c\Program Files\Radiant Vision Systems"
 copyfolder13=r"\\10.122.52.96\c\Program Files\Radiant Vision Systems"
 copyfolder14=r"\\10.122.52.97\c\Program Files\Radiant Vision Systems"
 copyfolder15=r"\\10.122.52.98\c\Program Files\Radiant Vision Systems"
 copyfolder16=r"\\10.122.52.99\c\Program Files\Radiant Vision Systems"
 copyfolder17=r"\\10.122.52.100\c\Program Files\Radiant Vision Systems"
 copyfolder18=r"\\10.122.52.101\c\Program Files\Radiant Vision Systems"
 copyfolder19=r"\\10.122.52.105\c\Program Files\Radiant Vision Systems"
 copyfolder20=r"\\10.122.52.106\c\Program Files\Radiant Vision Systems"
 copyfolder21=r"\\10.122.52.107\c\Program Files\Radiant Vision Systems"
 copyfolder22=r"\\10.122.52.108\c\Program Files\Radiant Vision Systems"
 copyfolder23=r"\\10.122.52.109\c\Program Files\Radiant Vision Systems"
 copyfolder24=r"\\10.122.52.110\c\Program Files\Radiant Vision Systems"
 
 source = r"F:\Copy"

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

def TTZIP503C():
 copyfolder25=r"\\10.122.52.135\c\Program Files\Radiant Vision Systems"
 copyfolder26=r"\\10.122.52.136\c\Program Files\Radiant Vision Systems"
 copyfolder27=r"\\10.122.52.137\c\Program Files\Radiant Vision Systems"
 copyfolder28=r"\\10.122.52.138\c\Program Files\Radiant Vision Systems"
 copyfolder29=r"\\10.122.52.139\c\Program Files\Radiant Vision Systems"
 copyfolder30=r"\\10.122.52.140\c\Program Files\Radiant Vision Systems"
 copyfolder31=r"\\10.122.52.126\c\Program Files\Radiant Vision Systems"
 copyfolder32=r"\\10.122.52.127\c\Program Files\Radiant Vision Systems"
 copyfolder33=r"\\10.122.52.128\c\Program Files\Radiant Vision Systems"
 copyfolder34=r"\\10.122.52.129\c\Program Files\Radiant Vision Systems"
 copyfolder35=r"\\10.122.52.130\c\Program Files\Radiant Vision Systems"
 copyfolder36=r"\\10.122.52.131\c\Program Files\Radiant Vision Systems"
 copyfolder37=r"\\10.122.52.117\c\Program Files\Radiant Vision Systems"
 copyfolder38=r"\\10.122.52.118\c\Program Files\Radiant Vision Systems"
 copyfolder39=r"\\10.122.52.119\c\Program Files\Radiant Vision Systems"
 copyfolder40=r"\\10.122.52.120\c\Program Files\Radiant Vision Systems"
 copyfolder41=r"\\10.122.52.121\c\Program Files\Radiant Vision Systems"
 copyfolder42=r"\\10.122.52.122\c\Program Files\Radiant Vision Systems"
 copyfolder43=r"\\10.122.52.146\c\Program Files\Radiant Vision Systems"
 copyfolder44=r"\\10.122.52.148\c\Program Files\Radiant Vision Systems"
 copyfolder45=r"\\10.122.52.147\c\Program Files\Radiant Vision Systems"
 copyfolder46=r"\\10.122.52.148\c\Program Files\Radiant Vision Systems"

 source = r"F:\Copy"
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

def TTZIP504M():
 copyfolder1=r"\\10.122.50.143\c\Program Files\Radiant Vision Systems"
 copyfolder2=r"\\10.122.50.144\c\Program Files\Radiant Vision Systems"
 copyfolder3=r"\\10.122.50.145\c\Program Files\Radiant Vision Systems"
 copyfolder4=r"\\10.122.50.146\c\Program Files\Radiant Vision Systems"
 copyfolder5=r"\\10.122.50.147\c\Program Files\Radiant Vision Systems"
 copyfolder6=r"\\10.122.50.148\c\Program Files\Radiant Vision Systems"
 copyfolder7=r"\\10.122.50.152\c\Program Files\Radiant Vision Systems"
 copyfolder8=r"\\10.122.50.153\c\Program Files\Radiant Vision Systems"
 copyfolder9=r"\\10.122.50.154\c\Program Files\Radiant Vision Systems"
 copyfolder10=r"\\10.122.50.155\c\Program Files\Radiant Vision Systems"
 copyfolder11=r"\\10.122.50.156\c\Program Files\Radiant Vision Systems"
 copyfolder12=r"\\10.122.50.157\c\Program Files\Radiant Vision Systems"
 copyfolder13=r"\\10.122.50.220\c\Program Files\Radiant Vision Systems"
 copyfolder14=r"\\10.122.50.221\c\Program Files\Radiant Vision Systems"
 copyfolder15=r"\\10.122.50.222\c\Program Files\Radiant Vision Systems"
 copyfolder16=r"\\10.122.50.223\c\Program Files\Radiant Vision Systems"
 copyfolder17=r"\\10.122.50.224\c\Program Files\Radiant Vision Systems"
 copyfolder18=r"\\10.122.50.225\c\Program Files\Radiant Vision Systems"
 copyfolder19=r"\\10.122.50.233\c\Program Files\Radiant Vision Systems"
 copyfolder20=r"\\10.122.50.234\c\Program Files\Radiant Vision Systems"
 copyfolder21=r"\\10.122.50.229\c\Program Files\Radiant Vision Systems"
 copyfolder22=r"\\10.122.50.230\c\Program Files\Radiant Vision Systems"
 copyfolder23=r"\\10.122.50.231\c\Program Files\Radiant Vision Systems"
 copyfolder24=r"\\10.122.50.232\c\Program Files\Radiant Vision Systems"
 
 source = r"F:\Copy"

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

def TTZIP504C():
 copyfolder25=r"\\10.122.50.238\c\Program Files\Radiant Vision Systems"
 copyfolder26=r"\\10.122.50.239\c\Program Files\Radiant Vision Systems"
 copyfolder27=r"\\10.122.51.82\c\Program Files\Radiant Vision Systems"
 copyfolder28=r"\\10.122.51.83\c\Program Files\Radiant Vision Systems"
 copyfolder29=r"\\10.122.50.240\c\Program Files\Radiant Vision Systems"
 copyfolder30=r"\\10.122.50.16\c\Program Files\Radiant Vision Systems"
 copyfolder31=r"\\10.122.51.84\c\Program Files\Radiant Vision Systems"
 copyfolder32=r"\\10.122.51.117\c\Program Files\Radiant Vision Systems"
 copyfolder33=r"\\10.122.51.85\c\Program Files\Radiant Vision Systems"
 copyfolder34=r"\\10.122.51.86\c\Program Files\Radiant Vision Systems"
 copyfolder35=r"\\10.122.51.73\c\Program Files\Radiant Vision Systems"
 copyfolder36=r"\\10.122.51.74\c\Program Files\Radiant Vision Systems"
 copyfolder37=r"\\10.122.51.77\c\Program Files\Radiant Vision Systems"
 copyfolder38=r"\\10.122.51.78\c\Program Files\Radiant Vision Systems"
 copyfolder39=r"\\10.122.51.75\c\Program Files\Radiant Vision Systems"
 copyfolder40=r"\\10.122.51.76\c\Program Files\Radiant Vision Systems"
 copyfolder41=r"\\10.122.51.66\c\Program Files\Radiant Vision Systems"
 copyfolder42=r"\\10.122.51.67\c\Program Files\Radiant Vision Systems"
 copyfolder43=r"\\10.122.51.64\c\Program Files\Radiant Vision Systems"
 copyfolder44=r"\\10.122.51.65\c\Program Files\Radiant Vision Systems"
 copyfolder45=r"\\10.122.51.68\c\Program Files\Radiant Vision Systems"
 copyfolder46=r"\\10.122.51.69\c\Program Files\Radiant Vision Systems"

 source = r"F:\Copy"
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
    
def allkillTT():
 subprocess.call([r'C:\Users\ssa2p\Desktop\Kill\StartKill.bat'])
 
def onekillTT():
 for proc in psutil.process_iter():
        if proc.name() == "TrueTestWatcher.exe" :
            proc.kill()
        if proc.name() == "FTPUploaderVB.exe" :
            proc.kill()
        if proc.name() == "SetSequence.exe" :
            proc.kill()
        if proc.name() == "TrueTest.exe" :
            proc.kill()

def allrename501M():
   os.rename('\\127.0.0.1\c\Program Files\Radiant Vision Systems\TrueTest 1.8','\\127.0.0.1\c\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
  #  os.rename('\\10.122.50.19\c\Program Files\Radiant Vision Systems\TrueTest 1.8','\\10.122.50.19\c\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
  #  os.rename('\\10.122.50.20\c\Program Files\Radiant Vision Systems\TrueTest 1.8','\\10.122.50.20\c\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
  #  os.rename('\\10.122.50.17\c\Program Files\Radiant Vision Systems\TrueTest 1.8','\\10.122.50.17\c\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
  #  os.rename('\\10.122.50.18\c\Program Files\Radiant Vision Systems\TrueTest 1.8','\\10.122.50.18\c\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
   


def onerename():
   os.rename('C:\Program Files\Radiant Vision Systems\TrueTest 1.8','C:\Program Files\Radiant Vision Systems\TrueTest 1.8 old')
   
def alldllcopy():
 copyfolder=r"C:\Program Files\Radiant Vision Systems\TrueTest 1.8" 
 source = r"F:\Copy"
 shutil.copytree(source,copyfolder,dirs_exist_ok=True)
 time.sleep(1)
 subprocess.Popen('C:\Program Files\Radiant Vision Systems\TrueTest 1.8\TrueTest.exe').wait(1)

def onedllcopy():
 copyfolder=r"C:\Program Files\Radiant Vision Systems\TrueTest 1.8" 
 source = r"F:\Copy"
 shutil.copytree(source,copyfolder,dirs_exist_ok=True)
 time.sleep(1)
 subprocess.Popen('C:\Program Files\Radiant Vision Systems\TrueTest 1.8\TrueTest.exe').wait(1)

def DLL501M():
 copyfolder1=r"\\10.122.50.19\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder2=r"\\10.122.50.20\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder3=r"\\10.122.50.17\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder4=r"\\10.122.50.18\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder5=r"\\10.122.50.15\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder6=r"\\10.122.50.241\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder7=r"\\10.122.50.26\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder8=r"\\10.122.50.27\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder9=r"\\10.122.50.28\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder10=r"\\10.122.50.64\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder11=r"\\10.122.50.30\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder12=r"\\10.122.50.38\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder13=r"\\10.122.50.204\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder14=r"\\10.122.50.205\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder15=r"\\10.122.50.206\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder16=r"\\10.122.50.207\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder17=r"\\10.122.50.208\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder18=r"\\10.122.50.209\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder19=r"\\10.122.50.195\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder20=r"\\10.122.50.196\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder21=r"\\10.122.50.197\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder22=r"\\10.122.50.198\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder23=r"\\10.122.50.199\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder24=r"\\10.122.50.200\c\Program Files\Radiant Vision Systems\TrueTest 1.8"


 source = r"F:\Copy"
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
def DLL501C():
 copyfolder25=r"\\10.122.50.213\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder26=r"\\10.122.50.214\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder27=r"\\10.122.51.52\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder28=r"\\10.122.51.53\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder29=r"\\10.122.50.215\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder30=r"\\10.122.50.216\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder31=r"\\10.122.51.54\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder32=r"\\10.122.51.55\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder33=r"\\10.122.51.56\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder34=r"\\10.122.51.57\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder35=r"\\10.122.51.87\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder36=r"\\10.122.51.88\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder37=r"\\10.122.51.91\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder38=r"\\10.122.51.92\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder39=r"\\10.122.51.89\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder40=r"\\10.122.51.90\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder41=r"\\10.122.51.101\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder42=r"\\10.122.51.102\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder43=r"\\10.122.50.99\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder44=r"\\10.122.51.100\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder45=r"\\10.122.51.103\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder46=r"\\10.122.51.104\c\Program Files\Radiant Vision Systems\TrueTest 1.8"

 source = r"F:\Copy"

 
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
def DLL502M():
 copyfolder1=r"\\10.122.51.183\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder2=r"\\10.122.51.184\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder3=r"\\10.122.51.185\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder4=r"\\10.122.51.186\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder5=r"\\10.122.51.187\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder6=r"\\10.122.51.188\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder7=r"\\10.122.51.192\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder8=r"\\10.122.51.193\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder9=r"\\10.122.51.194\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder10=r"\\10.122.51.195\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder11=r"\\10.122.51.196\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder12=r"\\10.122.51.197\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder13=r"\\10.122.51.201\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder14=r"\\10.122.51.202\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder15=r"\\10.122.51.203\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder16=r"\\10.122.51.204\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder17=r"\\10.122.51.205\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder18=r"\\10.122.51.206\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder19=r"\\10.122.51.210\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder20=r"\\10.122.51.211\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder21=r"\\10.122.51.212\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder22=r"\\10.122.51.213\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder23=r"\\10.122.51.214\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder24=r"\\10.122.51.215\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 
 source = r"F:\Copy"

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
def DLL502C():
 copyfolder25=r"\\10.122.51.219\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder26=r"\\10.122.51.220\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder27=r"\\10.122.51.221\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder28=r"\\10.122.51.222\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder29=r"\\10.122.51.223\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder30=r"\\10.122.51.224\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder31=r"\\10.122.51.228\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder32=r"\\10.122.51.229\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder33=r"\\10.122.51.230\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder34=r"\\10.122.51.231\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder35=r"\\10.122.51.232\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder36=r"\\10.122.51.233\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder37=r"\\10.122.51.237\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder38=r"\\10.122.51.238\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder39=r"\\10.122.51.239\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder40=r"\\10.122.51.240\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder41=r"\\10.122.51.241\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder42=r"\\10.122.51.242\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder43=r"\\10.122.51.246\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder44=r"\\10.122.51.247\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder45=r"\\10.122.51.248\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder46=r"\\10.122.51.249\c\Program Files\Radiant Vision Systems\TrueTest 1.8"

 source = r"F:\Copy"
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
def DLL503M():
 copyfolder1=r"\\10.122.52.73\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder2=r"\\10.122.52.74\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder3=r"\\10.122.52.75\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder4=r"\\10.122.52.76\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder5=r"\\10.122.52.77\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder6=r"\\10.122.52.78\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder7=r"\\10.122.52.87\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder8=r"\\10.122.52.88\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder9=r"\\10.122.52.89\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder10=r"\\10.122.52.90\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder11=r"\\10.122.52.91\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder12=r"\\10.122.52.92\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder13=r"\\10.122.52.96\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder14=r"\\10.122.52.97\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder15=r"\\10.122.52.98\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder16=r"\\10.122.52.99\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder17=r"\\10.122.52.100\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder18=r"\\10.122.52.101\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder19=r"\\10.122.52.105\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder20=r"\\10.122.52.106\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder21=r"\\10.122.52.107\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder22=r"\\10.122.52.108\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder23=r"\\10.122.52.109\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder24=r"\\10.122.52.110\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 
 source = r"F:\Copy"

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
def DLL503C():
 copyfolder25=r"\\10.122.52.135\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder26=r"\\10.122.52.136\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder27=r"\\10.122.52.137\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder28=r"\\10.122.52.138\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder29=r"\\10.122.52.139\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder30=r"\\10.122.52.140\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder31=r"\\10.122.52.126\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder32=r"\\10.122.52.127\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder33=r"\\10.122.52.128\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder34=r"\\10.122.52.129\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder35=r"\\10.122.52.130\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder36=r"\\10.122.52.131\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder37=r"\\10.122.52.117\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder38=r"\\10.122.52.118\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder39=r"\\10.122.52.119\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder40=r"\\10.122.52.120\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder41=r"\\10.122.52.121\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder42=r"\\10.122.52.122\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder43=r"\\10.122.52.146\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder44=r"\\10.122.52.148\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder45=r"\\10.122.52.147\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder46=r"\\10.122.52.148\c\Program Files\Radiant Vision Systems\TrueTest 1.8"

 source = r"F:\Copy"
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
def DLL504M():
 copyfolder1=r"\\10.122.50.143\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder2=r"\\10.122.50.144\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder3=r"\\10.122.50.145\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder4=r"\\10.122.50.146\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder5=r"\\10.122.50.147\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder6=r"\\10.122.50.148\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder7=r"\\10.122.50.152\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder8=r"\\10.122.50.153\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder9=r"\\10.122.50.154\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder10=r"\\10.122.50.155\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder11=r"\\10.122.50.156\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder12=r"\\10.122.50.157\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder13=r"\\10.122.50.220\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder14=r"\\10.122.50.221\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder15=r"\\10.122.50.222\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder16=r"\\10.122.50.223\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder17=r"\\10.122.50.224\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder18=r"\\10.122.50.225\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder19=r"\\10.122.50.233\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder20=r"\\10.122.50.234\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder21=r"\\10.122.50.229\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder22=r"\\10.122.50.230\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder23=r"\\10.122.50.231\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder24=r"\\10.122.50.232\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 
 source = r"F:\Copy"

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
def DLL504C():
 copyfolder25=r"\\10.122.50.238\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder26=r"\\10.122.50.239\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder27=r"\\10.122.51.82\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder28=r"\\10.122.51.83\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder29=r"\\10.122.50.240\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder30=r"\\10.122.50.16\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder31=r"\\10.122.51.84\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder32=r"\\10.122.51.117\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder33=r"\\10.122.51.85\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder34=r"\\10.122.51.86\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder35=r"\\10.122.51.73\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder36=r"\\10.122.51.74\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder37=r"\\10.122.51.77\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder38=r"\\10.122.51.78\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder39=r"\\10.122.51.75\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder40=r"\\10.122.51.76\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder41=r"\\10.122.51.66\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder42=r"\\10.122.51.67\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder43=r"\\10.122.51.64\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder44=r"\\10.122.51.65\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder45=r"\\10.122.51.68\c\Program Files\Radiant Vision Systems\TrueTest 1.8"
 copyfolder46=r"\\10.122.51.69\c\Program Files\Radiant Vision Systems\TrueTest 1.8"

 source = r"F:\Copy"
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


Testbtn = tk.Button(win, text='Test',height=1, width=10, command=Test)
Testbtn.place(x=0, y=20)
TTZIP501Mbtn = tk.Button(win, text='501L-1st',height=1, width=10, command=TTZIP501M)
TTZIP501Mbtn.place(x=0, y=45)
TTZIP501Cbtn = tk.Button(win, text='501L-2nd', height=1, width=10,command=TTZIP501C)
TTZIP501Cbtn.place(x=0, y=70)
TTZIP502Mbtn = tk.Button(win, text='502L-1st', height=1, width=10,command=TTZIP502M)
TTZIP502Mbtn.place(x=0, y=95)
TTZIP502Cbtn = tk.Button(win, text='502L-2nd', height=1, width=10,command=TTZIP502C)
TTZIP502Cbtn.place(x=0, y=120)
TTZIP503Mbtn = tk.Button(win, text='503L-1st', height=1, width=10,command=TTZIP503M)
TTZIP503Mbtn.place(x=0, y=145)
TTZIP503Cbtn = tk.Button(win, text='503L-2nd', height=1, width=10,command=TTZIP503C)
TTZIP503Cbtn.place(x=0, y=170)
TTZIP504Mbtn = tk.Button(win, text='504L-1st', height=1, width=10,command=TTZIP504M)
TTZIP504Mbtn.place(x=0, y=195)
TTZIP504Cbtn = tk.Button(win, text='504L-2nd', height=1, width=10,command=TTZIP504C)
TTZIP504Cbtn.place(x=0, y=220)

ALLTTQUITbtn = tk.Button(win, text='ALL',height=1, width=10, command=allkillTT)
ALLTTQUITbtn.place(x=150, y=20)
ONETTQUITbtn = tk.Button(win, text='One',height=1, width=10, command=onekillTT)
ONETTQUITbtn.place(x=150, y=45)

Allrenamebtn = tk.Button(win, text='ALL',height=1, width=10, command=allrename501M)
Allrenamebtn.place(x=300, y=20)
Onerenamebtn = tk.Button(win, text='One',height=1, width=10, command=onerename)
Onerenamebtn.place(x=300, y=45)

ALLDLLCOPYbtn = tk.Button(win, text='ALL',height=1, width=10, command=alldllcopy)
ALLDLLCOPYbtn.place(x=450, y=20)
ONEDLLCOPYbtn = tk.Button(win, text='One',height=1, width=10, command=onedllcopy)
ONEDLLCOPYbtn.place(x=450, y=45)

DLL501Mbtn = tk.Button(win, text='501L-1st',height=1, width=10, command=DLL501M)
DLL501Mbtn.place(x=450, y=70)
DLL501Cbtn = tk.Button(win, text='501L-2nd', height=1, width=10,command=DLL501C)
DLL501Cbtn.place(x=450, y=95)
DLL502Mbtn = tk.Button(win, text='502L-1st', height=1, width=10,command=DLL502M)
DLL502Mbtn.place(x=450, y=120)
DLL502Cbtn = tk.Button(win, text='502L-2nd', height=1, width=10,command=DLL502C)
DLL502Cbtn.place(x=450, y=145)
DLL503Mbtn = tk.Button(win, text='503L-1st', height=1, width=10,command=DLL503M)
DLL503Mbtn.place(x=450, y=170)
DLL503Cbtn = tk.Button(win, text='503L-2nd', height=1, width=10,command=DLL503C)
DLL503Cbtn.place(x=450, y=195)
DLL504Mbtn = tk.Button(win, text='504L-1st', height=1, width=10,command=DLL504M)
DLL504Mbtn.place(x=450, y=220)
DLL504Cbtn = tk.Button(win, text='504L-2nd', height=1, width=10,command=DLL504C)
DLL504Cbtn.place(x=450, y=245)

win.mainloop()