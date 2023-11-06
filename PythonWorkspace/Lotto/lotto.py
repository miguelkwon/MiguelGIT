from tkinter import *
import openpyxl
import requests
#import pyautogui
import tkinter
#import pandas as pd
import os
from tkinter import filedialog
from openpyxl import load_workbook


tk = Tk()

tk.title('lotto 당첨 조회 ;;       20231104  -  1092회' )
tk.geometry("1200x300-500+140")

# def cklotto():
    # ft2cm = entry1.get()
    # entry2.delete(0,"end")
    # pyautogui.alert('당첨.')
    # entry2.insert(0,round(float(ft2cm)*30.48,4))


# label1 = Label(tk,text='lotto 번호 입력').grid(row=0, column=0)


# entry1 = Entry(tk)
# entry2 = Entry(tk)
# entry3 = Entry(tk)
# entry4 = Entry(tk)
# entry5 = Entry(tk)
# entry6 = Entry(tk)


# entry1.grid(row=0,column=1)
# entry2.grid(row=0,column=2)
# entry3.grid(row=0,column=3)
# entry4.grid(row=0,column=4)
# entry5.grid(row=0,column=5)
# entry6.grid(row=0,column=6)


# btn1 = Button(tk,text='lotto 당첨 조회',bg='black',fg='white',command=cklotto).grid(row=0,column=8)


def oplotto():
    # val_input = entry1.get()
    # entry2.delete(0,"end")
    
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'
    url = url.format(entry1.get())
    req_result = requests.get(url)
    json_result = req_result.json()
    # print(json_result)
    # print(type(json_result))

    val_return_success = json_result.get('returnValue', None)
    val_drw_dt = json_result.get('drwNoDate', None)
    val_no_1 = json_result.get('drwtNo1', None)
    val_no_2 = json_result.get('drwtNo2', None)
    val_no_3 = json_result.get('drwtNo3', None)
    val_no_4 = json_result.get('drwtNo4', None)
    val_no_5 = json_result.get('drwtNo5', None)
    val_no_6 = json_result.get('drwtNo6', None)
    val_bonus_no = json_result.get('bnusNo', None)
    
    
    #pyautogui.alert('당첨.')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    entry4.delete(0,'end')
    entry5.delete(0,'end')
    entry6.delete(0,'end')
    entry7.delete(0,'end')
    entry8.delete(0,'end')
    
    
    
        
    
    entry2.insert(0,val_no_1)
    entry3.insert(0,val_no_2)
    entry4.insert(0,val_no_3)
    entry5.insert(0,val_no_4)
    entry6.insert(0,val_no_5)
    entry7.insert(0,val_no_6)
    entry8.insert(2,val_bonus_no)

def opuserlotto():
    load_userlotto = filedialog.askopenfilename(
        initialdir=f'{os.getcwd()}',
        title = "Exel 파일을 선택 해 주세요",
        filetypes= {("exel file","*.xlsx")})
    
    #load_userlotto = load_lotto("\\Users\\kwanghokwon\\Desktop\\PythonWorkspace\\Lotto\\a.xlsx", data_only=True)
    userexel=openpyxl.load_workbook(load_userlotto)
    load_lotto=userexel.active
    
    #load_lotto=userexel.get_
    #get_cells = load_lotto['A1' : 'F10']
    #load_lotto = pd.read_excel(userexel, sheet_name=0, skiprows=5, usecols="A:F")
    #load_lotto = userexel().active
    get_cells = load_lotto['A1' : 'F10']
    #for row in get_cells:
     #   for cell in row:
      #   print(cell.value)
    
    #사용자 lotto 번호 1
    entry9.insert(0,load_lotto['A1'].value)
    entry10.insert(0,load_lotto['B1'].value)
    entry11.insert(0,load_lotto['C1'].value)
    entry12.insert(0,load_lotto['D1'].value)
    entry13.insert(0,load_lotto['E1'].value)
    entry14.insert(0,load_lotto['F1'].value)
    
    #사용자 lotto 번호 2
    entry15.insert(0,load_lotto['A2'].value)
    entry16.insert(0,load_lotto['B2'].value)
    entry17.insert(0,load_lotto['C2'].value)
    entry18.insert(0,load_lotto['D2'].value)
    entry19.insert(0,load_lotto['E2'].value)
    entry20.insert(0,load_lotto['F2'].value)

    #사용자 lotto 번호 3
    entry21.insert(0,load_lotto['A3'].value)
    entry22.insert(0,load_lotto['B3'].value)
    entry23.insert(0,load_lotto['C3'].value)
    entry24.insert(0,load_lotto['D3'].value)
    entry25.insert(0,load_lotto['E3'].value)
    entry26.insert(0,load_lotto['F3'].value)
    
    #사용자 lotto 번호 4
    entry27.insert(0,load_lotto['A4'].value)
    entry28.insert(0,load_lotto['B4'].value)
    entry29.insert(0,load_lotto['C4'].value)
    entry30.insert(0,load_lotto['D4'].value)
    entry31.insert(0,load_lotto['E4'].value)
    entry32.insert(0,load_lotto['F4'].value)

      #사용자 lotto 번호 5
    entry33.insert(0,load_lotto['A5'].value)
    entry34.insert(0,load_lotto['B5'].value)
    entry35.insert(0,load_lotto['C5'].value)
    entry36.insert(0,load_lotto['D5'].value)
    entry37.insert(0,load_lotto['E5'].value)
    entry38.insert(0,load_lotto['F5'].value)

    #사용자 lotto 번호 6
    entry44.insert(0,load_lotto['A6'].value)
    entry45.insert(0,load_lotto['B6'].value)
    entry46.insert(0,load_lotto['C6'].value)
    entry47.insert(0,load_lotto['D6'].value)
    entry48.insert(0,load_lotto['E6'].value)
    entry49.insert(0,load_lotto['F6'].value)
    
    #사용자 lotto 번호 7
    entry51.insert(0,load_lotto['A7'].value)
    entry52.insert(0,load_lotto['B7'].value)
    entry53.insert(0,load_lotto['C7'].value)
    entry54.insert(0,load_lotto['D7'].value)
    entry55.insert(0,load_lotto['E7'].value)
    entry56.insert(0,load_lotto['F7'].value)

    #사용자 lotto 번호 8
    entry58.insert(0,load_lotto['A8'].value)
    entry59.insert(0,load_lotto['B8'].value)
    entry60.insert(0,load_lotto['C8'].value)
    entry61.insert(0,load_lotto['D8'].value)
    entry62.insert(0,load_lotto['E8'].value)
    entry63.insert(0,load_lotto['F8'].value)
    
    #사용자 lotto 번호 9
    entry64.insert(0,load_lotto['A9'].value)
    entry65.insert(0,load_lotto['B9'].value)
    entry66.insert(0,load_lotto['C9'].value)
    entry67.insert(0,load_lotto['D9'].value)
    entry68.insert(0,load_lotto['E9'].value)
    entry69.insert(0,load_lotto['F9'].value)

      #사용자 lotto 번호 10
    entry71.insert(0,load_lotto['A10'].value)
    entry72.insert(0,load_lotto['B10'].value)
    entry73.insert(0,load_lotto['C10'].value)
    entry74.insert(0,load_lotto['D10'].value)
    entry75.insert(0,load_lotto['E10'].value)
    entry76.insert(0,load_lotto['F10'].value)

     

    
    



        

def checklotto():
    lotto=[entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get()]
    bonuslotto=[entry8.get()]
    
    user1lotto=[entry9.get(),entry10.get(),entry11.get(),entry12.get(),entry13.get(),entry14.get()]
    user2lotto=[entry15.get(),entry16.get(),entry17.get(),entry18.get(),entry19.get(),entry20.get()]
    user3lotto=[entry21.get(),entry22.get(),entry23.get(),entry24.get(),entry25.get(),entry26.get()]
    user4lotto=[entry27.get(),entry28.get(),entry29.get(),entry30.get(),entry31.get(),entry32.get()]
    user5lotto=[entry33.get(),entry34.get(),entry35.get(),entry36.get(),entry37.get(),entry38.get()]
    user6lotto=[entry44.get(),entry45.get(),entry46.get(),entry47.get(),entry48.get(),entry49.get()]
    user7lotto=[entry51.get(),entry52.get(),entry53.get(),entry54.get(),entry55.get(),entry56.get()]
    user8lotto=[entry58.get(),entry59.get(),entry60.get(),entry61.get(),entry62.get(),entry63.get()]
    user9lotto=[entry64.get(),entry65.get(),entry66.get(),entry67.get(),entry68.get(),entry69.get()]
    user10lotto=[entry71.get(),entry72.get(),entry73.get(),entry74.get(),entry75.get(),entry76.get()]
    #pyautogui.alert(lotto)
    





    #내번호가 lotto 당첨번호 리스트에 포함되어 있냐 체크.
    
    
    same1 = 0
    for myN1 in user1lotto:
     if myN1 in lotto:
      same1 +=1
    
    

    same11=0
    for myN11 in user1lotto:
     if myN11 in bonuslotto:
        same11 +=1
    
    entry39.delete(0,'end')

    if same1 ==0 :
        entry39.insert(0,"꽝꽝꽝")        
    elif same1 ==1 :
        entry39.insert(0,"꽝꽝꽝")
    elif same1 ==2 :
        entry39.insert(0,"꽝꽝꽝")
    elif same1 ==3 :
        entry39.config(fg="green")
        entry39.insert(0,"5등")
    elif same1 ==4 :
        entry39.config(fg="green")
        entry39.insert(0,"4등")
    elif (same1 ==5) and (same11==0):
        entry39.config(fg="red")
        entry39.insert(0,"3등")
    elif (same1 ==5) and (same11==1):
        entry39.config(fg="red")
        entry39.insert(0,"2등")
    elif same1 ==6 :
        entry39.config(fg="red")
        entry39.insert(0,"1등")
      
    END

    same2 = 0
    for myN2 in user2lotto:
     if myN2 in lotto:
        same2 +=1

    same22=0
    for myN22 in user2lotto:
     if myN22 in bonuslotto:
        same22 +=1
     
    entry40.delete(0,'end')

    if same2 ==0 :
        entry40.insert(0,"꽝꽝꽝")        
    elif same2 ==1 :
        entry40.insert(0,"꽝꽝꽝")
    elif same2 ==2 :
        entry40.insert(0,"꽝꽝꽝")
    elif same2 ==3 :
        entry40.config(fg="green")
        entry40.insert(0,"5등")
    elif same2 ==4 :
        entry40.config(fg="green")
        entry40.insert(0,"4등")
    elif same2 ==5 and (same22==0):
        entry40.config(fg="red")
        entry40.insert(0,"3등")
    elif same2 ==5 and (same22==1):
        entry40.config(fg="red")
        entry40.insert(0,"2등")
    elif same2 ==6 :
        entry40.config(fg="red")
        entry40.insert(0,"1등")
    END

    same3 = 0
    for myN3 in user3lotto:
     if myN3 in lotto:
        same3 +=1

    same33=0
    for myN33 in user3lotto:
     if myN33 in bonuslotto:
        same33 +=1
    
    entry41.delete(0,'end')

    if same3 ==0 :
        entry41.insert(0,"꽝꽝꽝")        
    elif same3 ==1 :
        entry41.insert(0,"꽝꽝꽝")
    elif same3 ==2 :
        entry41.insert(0,"꽝꽝꽝")
    elif same3 ==3 :
        entry41.config(fg="green")
        entry41.insert(0,"5등")
    elif same3 ==4 :
        entry41.config(fg="green")
        entry41.insert(0,"4등")
    elif same3 ==5 and (same33==0):
        entry41.config(fg="red")
        entry41.insert(0,"3등")
    elif same3 ==5 and (same33==1):
       entry41.config(fg="red")
       entry41.insert(0,"2등")
    elif same3 ==6 :
        entry41.config(fg="red")
        entry41.insert(0,"1등")
    END

    same4 = 0
    for myN4 in user4lotto:
     if myN4 in lotto:
        same4 +=1

    same44=0
    for myN44 in user4lotto:
     if myN44 in bonuslotto:
        same44 +=1

    entry42.delete(0,'end')

    if same4 ==0 :
        entry42.insert(0,"꽝꽝꽝")        
    elif same4 ==1 :
        entry42.insert(0,"꽝꽝꽝")
    elif same4 ==2 :
        entry42.insert(0,"꽝꽝꽝")
    elif same4 ==3 :
        entry42.config(fg="green")
        entry42.insert(0,"5등")
    elif same4 ==4 :
        entry42.config(fg="green")
        entry42.insert(0,"4등")
    elif same4 ==5 and (same44==0):
        entry42.config(fg="red")
        entry42.insert(0,"3등")
    elif same4 ==5 and (same44==1):
       entry42.config(fg="red")
       entry42.insert(0,"2등")
    elif same4 ==6 :
        entry42.config(fg="red")
        entry42.insert(0,"1등")

    END
    
    same5 = 0
    for myN5 in user5lotto:
     if myN5 in lotto:
        same5 +=1

    same55=0
    for myN55 in user5lotto:
     if myN55 in bonuslotto:
        same55 +=1
    
    entry43.delete(0,'end')

    if same5 ==0 :
        entry43.insert(0,"꽝꽝꽝")        
    elif same5 ==1 :
        entry43.insert(0,"꽝꽝꽝")
    elif same5 ==2 :
        entry43.insert(0,"꽝꽝꽝")
    elif same5 ==3 :
        entry43.config(fg="green")
        entry43.insert(0,"5등")
    elif same5 ==4 :
        entry43.config(fg="green")
        entry43.insert(0,"4등")
    elif same5 ==5 and (same55==0):
        entry43.config(fg="red")
        entry43.insert(0,"3등")
    elif same5 ==5 and (same55==1):
       entry43.config(fg="red")
       entry43.insert(0,"2등")
    elif same5 ==6 :
        entry43.config(fg="red")
        entry43.insert(0,"1등")
    
    END

    same6 = 0
    for myN6 in user6lotto:
     if myN6 in lotto:
      same6 +=1
    
    

    same66=0
    for myN66 in user6lotto:
     if myN66 in bonuslotto:
        same66 +=1
    
    entry50.delete(0,'end')

    if same6 ==0 :
        entry50.insert(0,"꽝꽝꽝")        
    elif same6 ==1 :
        entry50.insert(0,"꽝꽝꽝")
    elif same6 ==2 :
        entry50.insert(0,"꽝꽝꽝")
    elif same6 ==3 :
        entry50.config(fg="green")
        entry50.insert(0,"5등")
    elif same6 ==4 :
        entry50.config(fg="green")
        entry50.insert(0,"4등")
    elif (same6 ==5) and (same66==0):
        entry50.config(fg="red")
        entry50.insert(0,"3등")
    elif (same6 ==5) and (same6==1):
        entry50.config(fg="red")
        entry39.insert(0,"2등")
    elif same6 ==6 :
        entry50.config(fg="red")
        entry50.insert(0,"1등")
      
    END

    same7 = 0
    for myN7 in user7lotto:
     if myN7 in lotto:
        same7 +=1

    same77=0
    for myN77 in user7lotto:
     if myN77 in bonuslotto:
        same77 +=1
     
    entry57.delete(0,'end')

    if same7 ==0 :
        entry57.insert(0,"꽝꽝꽝")        
    elif same7 ==1 :
        entry40.insert(0,"꽝꽝꽝")
    elif same7 ==2 :
        entry57.insert(0,"꽝꽝꽝")
    elif same7 ==3 :
        entry57.config(fg="green")
        entry57.insert(0,"5등")
    elif same7 ==4 :
        entry57.config(fg="green")
        entry57.insert(0,"4등")
    elif same7 ==5 and (same77==0):
        entry57.config(fg="red")
        entry57.insert(0,"3등")
    elif same7 ==5 and (same77==1):
        entry57.config(fg="red")
        entry57.insert(0,"2등")
    elif same7 ==6 :
        entry57.config(fg="red")
        entry57.insert(0,"1등")
    END

    same8 = 0
    for myN8 in user8lotto:
     if myN8 in lotto:
        same8 +=1

    same88=0
    for myN88 in user8lotto:
     if myN88 in bonuslotto:
        same88 +=1
    
    entry78.delete(0,'end')

    if same8 ==0 :
        entry78.insert(0,"꽝꽝꽝")        
    elif same8 ==1 :
        entry78.insert(0,"꽝꽝꽝")
    elif same8 ==2 :
        entry78.insert(0,"꽝꽝꽝")
    elif same8 ==3 :
        entry78.config(fg="green")
        entry78.insert(0,"5등")
    elif same8 ==4 :
        entry78.config(fg="green")
        entry78.insert(0,"4등")
    elif same8 ==5 and (same88==0):
        entry78.config(fg="red")
        entry78.insert(0,"3등")
    elif same8 ==5 and (same88==1):
       entry78.config(fg="red")
       entry78.insert(0,"2등")
    elif same8 ==6 :
        entry78.config(fg="red")
        entry78.insert(0,"1등")
    END

    same9 = 0
    for myN9 in user9lotto:
     if myN9 in lotto:
        same9 +=1

    same99=0
    for myN99 in user9lotto:
     if myN99 in bonuslotto:
        same99 +=1

    entry70.delete(0,'end')

    if same9 ==0 :
        entry70.insert(0,"꽝꽝꽝")        
    elif same9 ==1 :
        entry70.insert(0,"꽝꽝꽝")
    elif same9 ==2 :
        entry70.insert(0,"꽝꽝꽝")
    elif same9 ==3 :
        entry70.config(fg="green")
        entry70.insert(0,"5등")
    elif same9 ==4 :
        entry70.config(fg="green")
        entry70.insert(0,"4등")
    elif same9 ==5 and (same99==0):
        entry70.config(fg="red")
        entry70.insert(0,"3등")
    elif same9 ==5 and (same99==1):
       entry70.config(fg="red")
       entry70.insert(0,"2등")
    elif same9 ==6 :
        entry70.config(fg="red")
        entry70.insert(0,"1등")

    END
    
    same10 = 0
    for myN10 in user10lotto:
     if myN10 in lotto:
        same10 +=1

    same1010=0
    for myN1010 in user10lotto:
     if myN1010 in bonuslotto:
        same1010 +=1
    
    entry77.delete(0,'end')

    if same10 ==0 :
        entry77.insert(0,"꽝꽝꽝")        
    elif same10 ==1 :
        entry77.insert(0,"꽝꽝꽝")
    elif same10 ==2 :
        entry77.insert(0,"꽝꽝꽝")
    elif same10 ==3 :
        entry77.config(fg="green")
        entry77.insert(0,"5등")
    elif same10 ==4 :
        entry77.config(fg="green")
        entry77.insert(0,"4등")
    elif same10 ==5 and (same1010==0):
        entry77.config(fg="red")
        entry77.insert(0,"3등")
    elif same10 ==5 and (same1010==1):
       entry77.config(fg="red")
       entry77.insert(0,"2등")
    elif same10 ==6 :
        entry77.config(fg="red")
        entry77.insert(0,"1등")
    
    END
       
    
        

label1 = Label(tk,text='lotto 회자번호 입력').grid(row=0, column=0)
label2 = Label(tk,text='lotto 당첨번호').grid(row=2, column=0)
label3 = Label(tk,text='사용자 lotto번호 1').grid(row=3, column=0)
label4 = Label(tk,text='사용자 lotto번호 2').grid(row=4, column=0)
label12 = Label(tk,text='사용자 lotto번호 3').grid(row=5, column=0)
label13 = Label(tk,text='사용자 lotto번호 4').grid(row=6, column=0)
label14 = Label(tk,text='사용자 lotto번호 5').grid(row=7, column=0)
label3 = Label(tk,text='사용자 lotto번호 6').grid(row=8, column=0)
label4 = Label(tk,text='사용자 lotto번호 7').grid(row=9, column=0)
label12 = Label(tk,text='사용자 lotto번호 8').grid(row=10, column=0)
label13 = Label(tk,text='사용자 lotto번호 9').grid(row=11, column=0)
label14 = Label(tk,text='사용자 lotto번호 10').grid(row=12, column=0)
label5 = Label(tk,text='lotto 번호 1').grid(row=1, column=1)
label6 = Label(tk,text='lotto 번호 2').grid(row=1, column=2)
label7 = Label(tk,text='lotto 번호 3').grid(row=1, column=3)
label8 = Label(tk,text='lotto 번호 4').grid(row=1, column=4)
label9 = Label(tk,text='lotto 번호 5').grid(row=1, column=5)
label10 = Label(tk,text='lotto 번호 6').grid(row=1, column=6)
label11 = Label(tk,text='lotto 보너스 번호').grid(row=1, column=7)






#lotto number
entry1 = Entry(tk)
entry1.grid(row=0,column=1)
entry2 = Entry(tk)
entry2.grid(row=2,column=1)
entry3 = Entry(tk)
entry3.grid(row=2,column=2)
entry4 = Entry(tk)
entry4.grid(row=2,column=3)
entry5 = Entry(tk)
entry5.grid(row=2,column=4)
entry6 = Entry(tk)
entry6.grid(row=2,column=5)
entry7 = Entry(tk)
entry7.grid(row=2,column=6)
entry8 = Entry(tk)
entry8.grid(row=2,column=7)

#사용자 lotto 번호 1
entry9 = Entry(tk)
entry9.grid(row=3,column=1)
entry10 = Entry(tk)
entry10.grid(row=3,column=2)
entry11 = Entry(tk)
entry11.grid(row=3,column=3)
entry12 = Entry(tk)
entry12.grid(row=3,column=4)
entry13 = Entry(tk)
entry13.grid(row=3,column=5)
entry14 = Entry(tk)
entry14.grid(row=3,column=6)

entry39 = Entry(tk)
entry39.grid(row=3,column=8)

#사용자 lotto 번호 2
entry15 = Entry(tk)
entry15.grid(row=4,column=1)
entry16 = Entry(tk)
entry16.grid(row=4,column=2)
entry17 = Entry(tk)
entry17.grid(row=4,column=3)
entry18 = Entry(tk)
entry18.grid(row=4,column=4)
entry19 = Entry(tk)
entry19.grid(row=4,column=5)
entry20 = Entry(tk)
entry20.grid(row=4,column=6)

entry40 = Entry(tk)
entry40.grid(row=4,column=8)

#사용자 lotto 번호 3
entry21 = Entry(tk)
entry21.grid(row=5,column=1)
entry22 = Entry(tk)
entry22.grid(row=5,column=2)
entry23 = Entry(tk)
entry23.grid(row=5,column=3)
entry24 = Entry(tk)
entry24.grid(row=5,column=4)
entry25 = Entry(tk)
entry25.grid(row=5,column=5)
entry26 = Entry(tk)
entry26.grid(row=5,column=6)

entry41 = Entry(tk)
entry41.grid(row=5,column=8)

#사용자 lotto 번호 4
entry27 = Entry(tk)
entry27.grid(row=6,column=1)
entry28 = Entry(tk)
entry28.grid(row=6,column=2)
entry29 = Entry(tk)
entry29.grid(row=6,column=3)
entry30 = Entry(tk)
entry30.grid(row=6,column=4)
entry31 = Entry(tk)
entry31.grid(row=6,column=5)
entry32 = Entry(tk)
entry32.grid(row=6,column=6)

entry42 = Entry(tk)
entry42.grid(row=6,column=8)


#사용자 lotto 번호 5
entry33 = Entry(tk)
entry33.grid(row=7,column=1)
entry34 = Entry(tk)
entry34.grid(row=7,column=2)
entry35 = Entry(tk)
entry35.grid(row=7,column=3)
entry36 = Entry(tk)
entry36.grid(row=7,column=4)
entry37 = Entry(tk)
entry37.grid(row=7,column=5)
entry38 = Entry(tk)
entry38.grid(row=7,column=6)

entry43 = Entry(tk)
entry43.grid(row=7,column=8)


#사용자 lotto 번호 6
entry44 = Entry(tk)
entry44.grid(row=8,column=1)
entry45 = Entry(tk)
entry45.grid(row=8,column=2)
entry46 = Entry(tk)
entry46.grid(row=8,column=3)
entry47 = Entry(tk)
entry47.grid(row=8,column=4)
entry48 = Entry(tk)
entry48.grid(row=8,column=5)
entry49 = Entry(tk)
entry49.grid(row=8,column=6)

entry50 = Entry(tk)
entry50.grid(row=8,column=8)

#사용자 lotto 번호 7
entry51 = Entry(tk)
entry51.grid(row=9,column=1)
entry52 = Entry(tk)
entry52.grid(row=9,column=2)
entry53 = Entry(tk)
entry53.grid(row=9,column=3)
entry54 = Entry(tk)
entry54.grid(row=9,column=4)
entry55 = Entry(tk)
entry55.grid(row=9,column=5)
entry56 = Entry(tk)
entry56.grid(row=9,column=6)

entry57 = Entry(tk)
entry57.grid(row=9,column=8)

#사용자 lotto 번호 8
entry58 = Entry(tk)
entry58.grid(row=10,column=1)
entry59 = Entry(tk)
entry59.grid(row=10,column=2)
entry60 = Entry(tk)
entry60.grid(row=10,column=3)
entry61 = Entry(tk)
entry61.grid(row=10,column=4)
entry62 = Entry(tk)
entry62.grid(row=10,column=5)
entry63 = Entry(tk)
entry63.grid(row=10,column=6)

entry78 = Entry(tk)
entry78.grid(row=10,column=8)

#사용자 lotto 번호 9
entry64 = Entry(tk)
entry64.grid(row=11,column=1)
entry65 = Entry(tk)
entry65.grid(row=11,column=2)
entry66 = Entry(tk)
entry66.grid(row=11,column=3)
entry67 = Entry(tk)
entry67.grid(row=11,column=4)
entry68 = Entry(tk)
entry68.grid(row=11,column=5)
entry69 = Entry(tk)
entry69.grid(row=11,column=6)

entry70 = Entry(tk)
entry70.grid(row=11,column=8)


#사용자 lotto 번호 10
entry71 = Entry(tk)
entry71.grid(row=12,column=1)
entry72 = Entry(tk)
entry72.grid(row=12,column=2)
entry73 = Entry(tk)
entry73.grid(row=12,column=3)
entry74 = Entry(tk)
entry74.grid(row=12,column=4)
entry75 = Entry(tk)
entry75.grid(row=12,column=5)
entry76 = Entry(tk)
entry76.grid(row=12,column=6)

entry77 = Entry(tk)
entry77.grid(row=12,column=8)



btn1 = Button(tk,text='lotto 번호 불러오기',bg='white',fg='black',command=oplotto).grid(row=0,column=2)
btn3 = Button(tk,text='사용자 lotto 번호 불러오기',bg='white',fg='black',command=opuserlotto).grid(row=0,column=4)
btn4 = Button(tk,text='lotto 당첨 조회',bg='white',fg='black',command=checklotto).grid(row=0,column=5)


#listbox = Listbox(tk,width=100, height=1).grid(row=20,column=0)
#listbox.config(borderwidth=3)






# val_input = input('Input round number : ')




# print('Return success flag :', val_return_success)
# print('Draw lottery date :', val_drw_dt)
# print('Number 1 :', val_no_1)
# print('Number 2 :', val_no_2)
# print('Number 3 :', val_no_3)
# print('Number 4 :', val_no_4)
# print('Number 5 :', val_no_5)
# print('Number 6 :', val_no_6)
# print('Bonus Number :', val_bonus_no)


tk.mainloop()