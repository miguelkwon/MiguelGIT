import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
from pandastable import Table
import pickle
import os
import subprocess

class LogAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("로그 분석 툴")
        self.root.state('zoomed')  # Maximize the window on startup

        self.search_index1 = 0  # 첫 번째 검색어 위치 초기화
        self.search_index2 = 0  # 두 번째 검색어 위치 초기화



        # Multiple file paths
        self.file_paths = []
        self.df_list = []  # DataFrames for each log file
        self.file_names = []  # 각 파일의 이름을 저장할 리스트
        self.tables = {}  # Dictionary to store table widgets

        # Top Frame for File Selection and Conversion
        top_frame = tk.Frame(root)
        top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Bottom Frame for Log Content and Analysis
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left and Right Frames within the Bottom Frame
        left_frame = tk.Frame(bottom_frame, width=400)
        right_frame = tk.Frame(bottom_frame, width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # File Selection
        tk.Label(top_frame, text="로그 파일 경로:").pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="파일 열기", command=self.load_files).pack(side=tk.LEFT, padx=5)

        # Display loaded file names and paths
        # self.file_list_label = tk.Label(top_frame, text="불러온 파일 목록:\n(파일 경로 및 이름이 표시됩니다.)", justify=tk.LEFT, anchor="w")
        # self.file_list_label.pack(side=tk.LEFT, padx=10)

        # self.file_list_label = tk.Label(
        #     top_frame, 
        #     text="불러온 파일 목록:\n(파일 경로 및 이름이 표시됩니다.)", 
        #     justify=tk.LEFT, 
        #     anchor="w", 
        #     width=150,  # 너비를 40으로 설정
        #     height=8   # 높이를 3으로 설정
        # )
        # self.file_list_label.pack(side=tk.LEFT, padx=10)


        # Tabs for displaying multiple files
        self.tab_control = ttk.Notebook(left_frame)
        self.tab_control.pack(fill=tk.BOTH, expand=True)

        # 첫 번째 검색어 영역
        # search_frame1 = tk.Frame(right_frame)
        # search_frame1.pack(pady=5, anchor="n")  # 상단 정렬
        # tk.Label(search_frame1, text="첫 번째 검색어:").pack(side=tk.LEFT)
        # self.search_text1 = tk.Entry(search_frame1, width=40)
        # self.search_text1.pack(side=tk.LEFT)
        # tk.Button(search_frame1, text="검색", command=lambda: self.search_in_table(1)).pack(side=tk.LEFT)

        # # 두 번째 검색어 영역
        # search_frame2 = tk.Frame(right_frame)
        # search_frame2.pack(pady=5, anchor="n")  # 상단 정렬
        # tk.Label(search_frame2, text="두 번째 검색어:").pack(side=tk.LEFT)
        # self.search_text2 = tk.Entry(search_frame2, width=40)
        # self.search_text2.pack(side=tk.LEFT)
        # tk.Button(search_frame2, text="검색", command=lambda: self.search_in_table(2)).pack(side=tk.LEFT)

        # File Selection 영역 및 첫 번째 검색어, 두 번째 검색어
        tk.Label(
            top_frame, 
            text="불러온 파일 목록:\n(파일 경로 및 이름이 표시됩니다.)", 
            justify=tk.LEFT, 
            anchor="w", 
            width=50, 
            height=8
         ).grid(row=0, column=0, padx=10, pady=5, sticky="nw")

        # 첫 번째 검색어
        tk.Label(top_frame, text="첫 번째 검색어:").grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.search_text1 = tk.Entry(top_frame, width=30)
        self.search_text1.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        tk.Button(top_frame, text="검색", command=lambda: self.search_in_table(1)).grid(row=0, column=3, padx=5, pady=5)

        # 두 번째 검색어
        tk.Label(top_frame, text="두 번째 검색어:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.search_text2 = tk.Entry(top_frame, width=30)
        self.search_text2.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        tk.Button(top_frame, text="검색", command=lambda: self.search_in_table(2)).grid(row=0, column=6, padx=5, pady=5)

        # 열 비율 조정 (필요에 따라)
        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=0)
        top_frame.grid_columnconfigure(2, weight=0)
        top_frame.grid_columnconfigure(3, weight=0)
        top_frame.grid_columnconfigure(4, weight=0)
        top_frame.grid_columnconfigure(5, weight=0)
        top_frame.grid_columnconfigure(6, weight=0)


        

        self.load_last_search_terms()

        # Right Frame 내부에 그리드 레이아웃 사용
        button_frame = tk.Frame(right_frame)
        button_frame.pack(pady=10, anchor="n")  # 버튼 프레임 상단 정렬

        # Sequence Analyze Button
        self.analyze_button = tk.Button(button_frame, text="시퀀스 분석", command=self.analyze_sequences)
        self.analyze_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")  # 같은 열에 배치

        # Result Save Button
        self.save_button = tk.Button(button_frame, text="저장", command=self.save_results)
        self.save_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")  # 같은 열에 배치

        # Copy Results Button
        self.copy_button = tk.Button(button_frame, text="결과 복사", command=self.copy_results)
        self.copy_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")  # 같은 열에 배치

        # Frame for Sequence Results
        self.sequence_result_frame = tk.Frame(right_frame)
        self.sequence_result_frame.pack(fill=tk.BOTH, expand=True)



        # Label for Sequence Results
        self.sequence_result_label = tk.Label(right_frame, text="")
        self.sequence_result_label.pack(pady=10)

        self.previous_highlighted_rows = []
        self.current_sequence_index = 0

        # Save search terms on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Set pandas option to avoid FutureWarning
        pd.set_option('future.no_silent_downcasting', True)
        
    def search_in_table(self, search_number):
        """display_table에서 검색어를 검색하고 순차적으로 이동"""
        if search_number == 1:
            search_text = self.search_text1.get().strip()
            self.search_index1 = self.find_in_table(search_text, self.search_index1)
        elif search_number == 2:
            search_text = self.search_text2.get().strip()
            self.search_index2 = self.find_in_table(search_text, self.search_index2)


    def find_in_table(self, search_text, start_index):
        """display_table의 테이블에서 특정 검색어를 검색하여 순차적으로 이동 및 스크롤"""
        if not search_text:
            messagebox.showerror("오류", "검색어를 입력하세요.")
            return start_index

        # 현재 선택된 탭의 테이블 가져오기
        selected_tab = self.tab_control.select()
        tab_title = self.tab_control.tab(selected_tab, "text")

        if tab_title not in self.tables:
            messagebox.showerror("오류", "테이블을 찾을 수 없습니다.")
            return start_index

        table = self.tables[tab_title]
        df = table.model.df  # 현재 표시된 DataFrame

        # 테이블 행 높이와 전체 높이로 가시 행 수 계산
        row_height = table.rowheight
        table_height = table.parentframe.winfo_height()
        visible_rows = max(1, table_height // row_height)

        # 검색어 탐색
        for idx in range(start_index, len(df)):
            if search_text in df.iloc[idx]["Command"]:
                # 선택된 행 강조 표시
                table.setSelectedRow(idx)
                table.redraw()

                # 검색어가 있는 행으로 스크롤 이동하여 중앙에 위치시키기
                row_count = len(df)
                center_offset = max(0, visible_rows // 2)  # 가시 행 수의 절반
                target_index = max(0, idx - center_offset)  # 검색된 행을 중앙에 위치
                scroll_position = min(1, target_index / max(1, row_count - visible_rows))
                table.yview_moveto(scroll_position)

                # 열로 스크롤 이동하여 Command 열이 가시 영역에 오도록 설정
                command_col_index = df.columns.get_loc("Command")
                total_columns = len(df.columns)
                visible_columns = table.colsDisplayed
                target_col_position = min(1, command_col_index / max(1, total_columns - visible_columns))
                table.xview_moveto(target_col_position)

                return idx + 1  # 다음 탐색을 위한 시작 인덱스

        # 검색어를 찾지 못했을 경우
        messagebox.showinfo("알림", f"'{search_text}'에 대한 추가 결과가 없습니다.")
        return 0  # 검색어를 못 찾으면 인덱스를 초기화



           
    
    def load_files(self):
        self.file_paths = filedialog.askopenfilenames(filetypes=[("Text files", "*.txt")])
        # 기존 탭 제거
        for tab in self.tab_control.tabs():
            self.tab_control.forget(tab)
        if self.file_paths:
            self.file_names = [os.path.basename(path) for path in self.file_paths]

            for idx, file_path in enumerate(self.file_paths):
                self.convert_to_dataframe(file_path, display=(idx == 0))

            # Update the file list label
            self.update_file_list_display()

    def update_file_list_display(self):
        file_list_text = "불러온 파일 목록:\n" + "\n".join(f"{path}" for path in self.file_paths)
        self.file_list_label.config(text=file_list_text)

    def convert_to_dataframe(self, file_path, display=False):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                log_content = file.readlines()
        except Exception as e:
            messagebox.showerror("파일 오류", f"파일을 열 수 없습니다: {e}")
            return

        log_data = []
        for line in log_content[1:]:  # 첫 행 생략
            parts = line.strip().split(maxsplit=3)
            if len(parts) >= 3:
                merged = parts[1] + " " + parts[2] + " " + parts[3] if len(parts) == 4 else parts[1] + " " + parts[2]
                log_data.append([parts[0], merged])
            elif len(parts) == 2:
                log_data.append([parts[0], parts[1]])
            elif len(parts) == 1:
                log_data.append([parts[0], ""])

        df = pd.DataFrame(log_data, columns=["Time", "Command"])
        self.df_list.append(df)

        # Ensure future behavior to avoid FutureWarning
        df = df.infer_objects(copy=False)

        # Display the table in a tab
        self.display_table(df, os.path.basename(file_path))

    def display_table(self, df, title):
        frame = tk.Frame(self.tab_control)
        self.tab_control.add(frame, text=title)
        table = Table(frame, dataframe=df, showtoolbar=False, showstatusbar=False)
        table.columnwidths = {'Command': 1000}
        table.show()
        self.tables[title] = table  # Store the table widget in the dictionary

    # def analyze_sequences(self):
    #     search1 = self.search_text1.get().strip()
    #     search2 = self.search_text2.get().strip()

    #     if not search1 or not search2:
    #         messagebox.showerror("오류", "두 개의 검색어를 모두 입력하세요.")
    #         return

    #     results = []

    #     for file_name, df in zip(self.file_names, self.df_list):
    #         sequences = []
    #         seq_start = None

    #         for idx, row in df.iterrows():
    #             if seq_start is None and search1 in row["Command"]:
                    
    #                 seq_start = idx
    #             elif seq_start is not None and search2 in row["Command"]:
                    
    #                 sequences.append((seq_start, idx))
    #                 seq_start = None

    #         for seq_num, (start, end) in enumerate(sequences, start=1):
    #             start_time = pd.to_datetime(df.iloc[start, 0])
    #             end_time = pd.to_datetime(df.iloc[end, 0])
    #             duration = end_time - start_time
    #             # Format duration as HH:MM:SS.sss
    #             total_seconds = int(duration.total_seconds())
    #             hours = total_seconds // 3600
    #             minutes = (total_seconds % 3600) // 60
    #             seconds = duration.total_seconds() % 60
    #             formatted_duration = f"{hours:02}:{minutes:02}:{seconds:06.3f}"
    #             results.append([file_name, seq_num, start_time, end_time, formatted_duration])

           

    #     if results:
    #         self.sequence_df = pd.DataFrame(results, columns=["File", "Sequence No.", "Start Time", "End Time", "Duration"])
    #         self.display_sequence_results(self.sequence_df)
    #     else:
    #         self.sequence_result_label.config(text="시퀀스를 찾을 수 없습니다.")

    def analyze_sequences(self):
        search1 = self.search_text1.get().strip()
        search2 = self.search_text2.get().strip()

        if not search1 or not search2:
            messagebox.showerror("오류", "두 개의 검색어를 모두 입력하세요.")
            return

        # 새로운 결과를 추가할 리스트
        new_results = []

        # 이미 분석된 파일 이름을 추적 (중복 분석 방지)
        analyzed_files = set(self.sequence_df["File"]) if hasattr(self, "sequence_df") else set()

        for file_name, df in zip(self.file_names, self.df_list):
            if file_name in analyzed_files:
                continue  # 이미 분석된 파일은 건너뜀

            sequences = []  # 각 파일별 시퀀스 저장
            seq_start = None  # 시퀀스 시작 지점

            # 시퀀스 찾기
            for idx, row in df.iterrows():
                if seq_start is None and search1 in row["Command"]:
                    seq_start = idx
                elif seq_start is not None and search2 in row["Command"]:
                    sequences.append((seq_start, idx))
                    seq_start = None

            # 시퀀스 결과를 new_results에 추가
            for seq_num, (start, end) in enumerate(sequences, start=1):
                start_time = pd.to_datetime(df.iloc[start, 0])
                end_time = pd.to_datetime(df.iloc[end, 0])
                duration = end_time - start_time
                total_seconds = int(duration.total_seconds())
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = duration.total_seconds() % 60
                formatted_duration = f"{hours:02}:{minutes:02}:{seconds:06.3f}"
                new_results.append([file_name, seq_num, start_time, end_time, formatted_duration])

        # 기존 결과와 새로운 결과를 병합
        if new_results:
            new_df = pd.DataFrame(new_results, columns=["File", "Sequence No.", search1, search2, "Time"])
            if hasattr(self, "sequence_df"):
                self.sequence_df = pd.concat([self.sequence_df, new_df], ignore_index=True)
            else:
                self.sequence_df = new_df

            self.display_sequence_results(self.sequence_df)
        else:
            messagebox.showinfo("알림", "새로 분석할 시퀀스가 없습니다.")



    
    












    def display_sequence_results(self, df):
        for widget in self.sequence_result_frame.winfo_children():
            widget.destroy()

        table = Table(self.sequence_result_frame, dataframe=df, showtoolbar=False, showstatusbar=False)
        table.show()

    


    def save_results(self):
        try:
            # display_sequence_results에 표시된 데이터를 가져오기
            table_widget = self.sequence_result_frame.winfo_children()[0]  # 표시된 Table 가져오기
            displayed_df = table_widget.model.df  # 현재 표시된 DataFrame 가져오기

            # 다운로드 폴더 경로 설정
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            default_file_name = "sequence_results.csv"
            file_path = os.path.join(downloads_path, default_file_name)

            # DataFrame을 CSV로 저장
            displayed_df.to_csv(file_path, index=False, encoding="utf-8-sig")

            # 성공 메시지
            messagebox.showinfo("성공", f"결과가 CSV 파일로 저장되었습니다:\n{file_path}")

            # 다운로드 폴더 열기
            if os.name == 'nt':  # Windows
                os.startfile(downloads_path)
            elif os.name == 'posix':  # macOS 또는 Linux
                subprocess.Popen(['open', downloads_path] if sys.platform == 'darwin' else ['xdg-open', downloads_path])
        except Exception as e:
            messagebox.showerror("오류", f"결과를 저장하는 중 오류가 발생했습니다: {e}")

    def copy_results(self):
            try:
                # display_sequence_results에 표시된 데이터를 클립보드로 복사
                table_widget = self.sequence_result_frame.winfo_children()[0]  # 표시된 Table 가져오기
                displayed_df = table_widget.model.df  # 현재 표시된 DataFrame 가져오기
                
                # DataFrame을 탭 구분된 텍스트로 변환
                df_string = displayed_df.to_csv(sep='\t', index=False)

                # 클립보드에 복사
                self.root.clipboard_clear()
                self.root.clipboard_append(df_string)
                # messagebox.showinfo("성공", "결과를 클립보드에 복사했습니다.")
            except Exception as e:
                messagebox.showerror("오류", f"결과를 복사하는 중 오류가 발생했습니다: {e}")



    def load_last_search_terms(self):
        try:
            with open("last_search_terms.pkl", "rb") as f:
                terms = pickle.load(f)
                self.search_text1.insert(0, terms.get("search1", ""))
                self.search_text2.insert(0, terms.get("search2", ""))
        except (FileNotFoundError, EOFError):
            pass

    def save_last_search_terms(self):
        terms = {"search1": self.search_text1.get(), "search2": self.search_text2.get()}
        with open("last_search_terms.pkl", "wb") as f:
            pickle.dump(terms, f)

    def on_closing(self):
        self.save_last_search_terms()
        self.root.destroy()


# GUI 실행
root = tk.Tk()
app = LogAnalyzer(root)
root.mainloop()
