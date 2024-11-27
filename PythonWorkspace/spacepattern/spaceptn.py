import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image
import numpy as np
import os
import platform

# 문자열을 RGB 튜플로 변환하는 함수
def parse_rgb_string(rgb_string):
    return tuple(map(int, rgb_string.strip("()").split(',')))

# 체크보드 생성 함수
def create_checkerboard(width, height, gap, color1, color2, full_ptn):
    board = np.zeros((height, width, 3), dtype=np.uint8)  # 빈 보드 생성 (검정 바탕)

    if full_ptn:  # 전체를 하나의 색으로 채움
        board[:, :] = color1
    else:
        for i in range(height):
            for j in range(width):
                # 첫 번째 색상을 (1,1)에서 시작하고 gap 간격마다 배치
                if ((i + 1) % gap == 1) and ((j + 1) % gap == 1):
                    board[i, j] = color1  # 첫 번째 색상
                else:
                    board[i, j] = color2  # 두 번째 색상
    return board

# 폴더 열기 함수
def open_folder(filepath):
    folder_path = os.path.dirname(filepath)
    if platform.system() == "Windows":
        os.startfile(folder_path)
    elif platform.system() == "Darwin":
        os.system(f'open "{folder_path}"')
    else:
        os.system(f'xdg-open "{folder_path}"')

# 체크보드 이미지를 저장하는 함수
def save_image():
    if current_board is None:
        status_label.config(text="⚠️ 저장할 이미지가 없습니다.")
        return
    filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG 파일", "*.png")])
    if filepath:
        Image.fromarray(current_board).save(filepath)
        status_label.config(text=f"이미지 저장 완료: {filepath}")
        open_folder(filepath)

# 체크보드 생성 및 표시 함수
def generate_board():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        gap = int(pixel_size_entry.get())

        color1 = parse_rgb_string(selected_color1.get())
        color2 = parse_rgb_string(selected_color2.get())
        full_ptn = full_ptn_var.get()  # FULL PTN 선택 여부 확인
        if full_ptn:
            color2 = color1  # 두 번째 색상 = 첫 번째 색상
    except ValueError:
        status_label.config(text="⚠️ 유효한 숫자를 입력하세요.")
        return

    global current_board
    current_board = create_checkerboard(width, height, gap, color1, color2, full_ptn)
    status_label.config(text="생성 완료!")

# FULL PTN 선택 시 두 번째 색상 버튼 숨기기/보이기 함수
def toggle_color2_buttons():
    if full_ptn_var.get():  # FULL PTN이 체크된 경우 숨김
        for button in color2_buttons:
            button.grid_remove()
    else:  # 체크 해제된 경우 다시 보이기
        for button in color2_buttons:
            button.grid()

# Tkinter UI 구성
root = tk.Tk()
root.title("SPACE PTN 생성기")

current_board = None

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(main_frame, text="WIDTH:").grid(row=0, column=0, padx=5, pady=5)
width_entry = ttk.Entry(main_frame, width=10)
width_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="HEIGHT:").grid(row=1, column=0, padx=5, pady=5)
height_entry = ttk.Entry(main_frame, width=10)
height_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="픽셀간격 :").grid(row=2, column=0, padx=5, pady=5)
pixel_size_entry = ttk.Entry(main_frame, width=10)
pixel_size_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(main_frame, text="첫 번째 색상 선택:").grid(row=3, column=0, padx=5, pady=5)
selected_color1 = tk.StringVar(value="(255, 0, 0)")

red_button1 = ttk.Radiobutton(main_frame, text="Red (255,0,0)", variable=selected_color1, value="(255, 0, 0)")
green_button1 = ttk.Radiobutton(main_frame, text="Green (0,255,0)", variable=selected_color1, value="(0, 255, 0)")
blue_button1 = ttk.Radiobutton(main_frame, text="Blue (0,0,255)", variable=selected_color1, value="(0, 0, 255)")

red_button1.grid(row=4, column=0, padx=5, pady=2, sticky=tk.W)
green_button1.grid(row=5, column=0, padx=5, pady=2, sticky=tk.W)
blue_button1.grid(row=6, column=0, padx=5, pady=2, sticky=tk.W)

# 두 번째 색상 선택 버튼 생성
selected_color2 = tk.StringVar(value="(0, 0, 0)")

red_button2 = ttk.Radiobutton(main_frame, text="Red (255,0,0)", variable=selected_color2, value="(255, 0, 0)")
green_button2 = ttk.Radiobutton(main_frame, text="Green (0,255,0)", variable=selected_color2, value="(0, 255, 0)")
blue_button2 = ttk.Radiobutton(main_frame, text="Blue (0,0,255)", variable=selected_color2, value="(0, 0, 255)")
black_button2 = ttk.Radiobutton(main_frame, text="Black (0,0,0)", variable=selected_color2, value="(0, 0, 0)")

color2_buttons = [red_button2, green_button2, blue_button2, black_button2]

# 초기에는 두 번째 색상 버튼 숨기기
for i, button in enumerate(color2_buttons):
    button.grid(row=8 + i, column=0, padx=5, pady=2, sticky=tk.W)
    button.grid_remove()  # 숨기기

# FULL PTN 체크버튼
full_ptn_var = tk.BooleanVar(value=False)
full_ptn_button = ttk.Checkbutton(main_frame, text="FULL PTN", variable=full_ptn_var, command=toggle_color2_buttons)
full_ptn_button.grid(row=12, column=0, columnspan=2, pady=5)

generate_button = ttk.Button(main_frame, text="생성", command=generate_board)
generate_button.grid(row=13, column=0, columnspan=2, pady=10)

save_button = ttk.Button(main_frame, text="이미지 저장", command=save_image)
save_button.grid(row=14, column=0, columnspan=2, pady=5)

status_label = ttk.Label(main_frame, text="")
status_label.grid(row=15, column=0, columnspan=2)

root.mainloop()
