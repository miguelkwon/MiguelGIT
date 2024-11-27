import tkinter as tk
from pandastable import Table
import pandas as pd

# 데이터 준비
data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Value': [10, 20, 30]
})

# Tkinter 초기화
root = tk.Tk()
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

# 테이블 초기화
table = Table(frame, dataframe=data)
table.show()

# 색상 마스크를 적용하는 방법
def apply_row_colors(table):
    row_colors = {}  # 행 색상 정보를 저장
    for i, row in data.iterrows():
        if i % 2 == 0:  # 짝수 행
            row_colors[i] = '#FFCCCC'  # 짝수 행 배경색
        else:
            row_colors[i] = '#CCCCFF'  # 홀수 행 배경색

    # `rowcolors` 속성에 설정
    table.setRowColors(row_colors)
    table.redraw()  # 테이블 갱신

# 색상 적용
apply_row_colors(table)

root.mainloop()
