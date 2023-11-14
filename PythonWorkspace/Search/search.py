from tkinter import *
import pandas as pd
from tkinter import filedialog






search = Tk()
search.title('Find parameter' )
search.geometry("1200x300-500+140")





def opseq():
    sequence = filedialog.askopenfilename(
        initialdir='G:/',
        title = "sequence 파일을 선택 해 주세요",
        filetypes= {("txt file","*.*")})
       
    



 



btn1 = Button(search,text='OPEN sequence',bg='white',fg='black',command=opseq).grid(row=0,column=1)






search.mainloop()