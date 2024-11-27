import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime, timedelta

# 스케줄러 프로그램 클래스 정의
class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("일정 관리 스케줄러")
        self.root.geometry("700x750")
        
        # 달력 위젯 생성
        self.cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
        self.cal.grid(row=0, column=0, padx=20, pady=20)
        
        # 스케줄 메모 입력 필드와 버튼
        self.memo_label = tk.Label(root, text="선택한 날짜의 메모:")
        self.memo_label.grid(row=1, column=0)
        
        self.memo_text = tk.Text(root, height=10, width=40)
        self.memo_text.grid(row=2, column=0, padx=20, pady=10)
        
        # 저장 및 조회 버튼
        self.save_button = tk.Button(root, text="스케줄 저장", command=self.save_schedule)
        self.save_button.grid(row=3, column=0, pady=5)
        
        self.view_button = tk.Button(root, text="스케줄 조회", command=self.view_schedule)
        self.view_button.grid(row=4, column=0, pady=5)
        
        # 일주일 일정 표시 버튼
        self.weekly_view_button = tk.Button(root, text="일주일 일정 보기", command=self.view_weekly_schedule)
        self.weekly_view_button.grid(row=5, column=0, pady=5)
        
        # 일주일 달력 형태로 날짜와 스케줄을 표시할 필드
        self.weekly_label = tk.Label(root, text="일주일 일정:")
        self.weekly_label.grid(row=0, column=1, padx=20)
        
        self.weekly_text = tk.Text(root, height=30, width=40)
        self.weekly_text.grid(row=1, column=1, rowspan=5, padx=20, pady=10)
        
        # 스케줄을 저장할 딕셔너리 초기화
        self.schedules = {}
        
        # 스케줄이 있는 날짜 표시를 위한 태그 스타일 설정
        self.cal.tag_config("scheduled", background="lightblue", foreground="black")

    def save_schedule(self):
        # 선택한 날짜와 메모 내용
        date = self.cal.get_date()
        memo = self.memo_text.get("1.0", tk.END).strip()
        
        # 메모를 저장
        if date and memo:
            self.schedules[date] = memo
            
            # 해당 날짜에 태그 추가 (스케줄 표시)
            self.cal.tag_add("scheduled", date)
            
            messagebox.showinfo("저장 완료", f"{date}의 스케줄이 저장되었습니다.")
            self.memo_text.delete("1.0", tk.END)  # 텍스트박스 초기화
        else:
            messagebox.showwarning("입력 오류", "메모를 입력하세요.")
    
    def view_schedule(self):
        # 선택한 날짜의 메모 조회
        date = self.cal.get_date()
        memo = self.schedules.get(date, "")
        
        if memo:
            self.memo_text.delete("1.0", tk.END)
            self.memo_text.insert("1.0", memo)  # 메모 텍스트박스에 출력
            messagebox.showinfo("스케줄 조회", f"{date}의 스케줄을 불러옵니다.")
        else:
            messagebox.showinfo("스케줄 조회", f"{date}에 저장된 스케줄이 없습니다.")

    def view_weekly_schedule(self):
        # 선택한 날짜를 기준으로 일주일 간의 스케줄 조회
        selected_date = self.cal.get_date()
        start_date = datetime.strptime(selected_date, "%Y-%m-%d")
        
        # 일주일 스케줄을 텍스트 박스에 출력
        self.weekly_text.delete("1.0", tk.END)  # 텍스트 박스 초기화
        
        # 선택한 날짜부터 일주일 간 날짜와 메모를 표시
        for i in range(7):  # 선택한 날짜부터 일주일 동안 반복
            current_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
            memo = self.schedules.get(current_date, "일정 없음")
            self.weekly_text.insert(tk.END, f"{current_date}: {memo}\n")

# GUI 프로그램 실행
root = tk.Tk()
app = ScheduleApp(root)
root.mainloop()
