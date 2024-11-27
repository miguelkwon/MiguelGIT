import hashlib
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def generate_md5():
    # 파일 경로 선택 창 열기
    filepath = filedialog.askopenfilename(title="Select a file to hash")
    if filepath:
        # 선택한 파일 경로를 해시코드 생성
        hash_object = hashlib.md5(filepath.encode())
        md5_hash_code = hash_object.hexdigest()
        
        # 텍스트박스에 해시코드 표시
        hash_textbox.delete(0, tk.END)
        hash_textbox.insert(0, md5_hash_code)

def copy_to_clipboard():
    # 해시코드를 클립보드에 복사
    root.clipboard_clear()
    root.clipboard_append(hash_textbox.get())
    messagebox.showinfo("복사 완료", "해시코드가 클립보드에 복사되었습니다.")

# GUI 창 생성
root = tk.Tk()
root.title("MD5 해시 생성기")

# '해시 생성' 버튼
generate_button = tk.Button(root, text="해시할 문자열 불러오기", command=generate_md5)
generate_button.grid(row=0, column=0, padx=10, pady=10)

# 해시코드를 표시할 텍스트박스
hash_textbox = tk.Entry(root, width=50)
hash_textbox.grid(row=0, column=1, padx=10, pady=10)

# '복사하기' 버튼
copy_button = tk.Button(root, text="복사하기", command=copy_to_clipboard)
copy_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
