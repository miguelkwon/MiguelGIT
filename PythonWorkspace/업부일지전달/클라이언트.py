import pandas as pd
from tkinter import Tk, Label, Button, filedialog, Listbox, Scrollbar, Frame, END, MULTIPLE

def read_excel(file_path):
    df = pd.read_excel(file_path, header=None, skiprows=7, usecols="A:L", nrows=35, parse_dates=[0])
    df.columns = ['Date'] + [f'Column_{i}' for i in range(1, 12)]
    df['Date'] = df['Date'].fillna(pd.Timestamp('1900-01-01'))  # NaT 값을 기본 날짜로 대체
    return df

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        df = read_excel(file_path)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # 날짜 파싱 실패 시 NaT로 변환
        dates = df['Date'].dropna().drop_duplicates().tolist()  # NaT 값 제거
        listbox.delete(0, END)
        for date in dates:
            listbox.insert(END, date.strftime("%Y-%m-%d"))  # 날짜를 문자열 형식으로 변환하여 추가
        global selected_df
        selected_df = df

def show_selected_date_data():
    selected_dates = listbox.curselection()
    selected_date_strs = [listbox.get(i) for i in selected_dates]
    selected_data = selected_df[selected_df['Date'].dt.strftime("%Y-%m-%d").isin(selected_date_strs)]
    data_listbox.delete(0, END)
    for _, row in selected_data.iterrows():
        row_data = ' | '.join(map(str, row[1:].values))  # 'Date' 열을 제외한 나머지 데이터 추가
        data_listbox.insert(END, row_data)
    return selected_data

def save_selected_data():
    selected_data = show_selected_date_data()
    if not selected_data.empty:
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            selected_data.to_excel(file_path, index=False)
            print(f'Data saved to {file_path}')

def gui_client():
    global listbox, data_listbox, root
    root = Tk()
    root.title("Excel Data Viewer")

    label = Label(root, text="Select an Excel file to load")
    label.pack()

    select_button = Button(root, text="Select File", command=select_file)
    select_button.pack()

    listbox = Listbox(root, width=50, height=10, selectmode=MULTIPLE)
    listbox.pack()

    show_data_button = Button(root, text="Show Selected Date Data", command=show_selected_date_data)
    show_data_button.pack()

    save_data_button = Button(root, text="Save Selected Data", command=save_selected_data)
    save_data_button.pack()

    data_frame = Frame(root)
    data_frame.pack()

    scrollbar = Scrollbar(data_frame)
    scrollbar.pack(side="right", fill="y")

    data_listbox = Listbox(data_frame, width=100, height=10, yscrollcommand=scrollbar.set)
    data_listbox.pack(side="left", fill="both")

    scrollbar.config(command=data_listbox.yview)

    root.mainloop()

if __name__ == "__main__":
    selected_df = None
    gui_client()
