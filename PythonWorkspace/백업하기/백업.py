import os
import shutil
from datetime import datetime

# 바탕화면, 다운로드, Kakao Download 폴더 경로 설정
desktop_path = os.path.join(os.path.expanduser("~"), r"F:\OneDrive - Radiant Vision Systems\바탕 화면")
downloads_path = os.path.join(os.path.expanduser("~"), r"C:\Users\miguel.kwon\Downloads")
kakao_download_path = os.path.join(os.path.expanduser("~"), r"F:\OneDrive - Radiant Vision Systems\문서\KakaoTalk Downloads")

# 백업할 경로 설정
destination_path = r"F:\Backup"  # 여기에 원하는 경로를 입력하세요

# 오늘 날짜 폴더 생성
today_date = datetime.today().strftime('%Y-%m-%d')
backup_folder = os.path.join(destination_path, today_date)
os.makedirs(backup_folder, exist_ok=True)

# 바탕화면, 다운로드, Kakao Download 폴더를 위한 별도 폴더 생성
desktop_backup_folder = os.path.join(backup_folder, "Desktop")
downloads_backup_folder = os.path.join(backup_folder, "Downloads")
kakao_download_backup_folder = os.path.join(backup_folder, "KakaoDownload")
os.makedirs(desktop_backup_folder, exist_ok=True)
os.makedirs(downloads_backup_folder, exist_ok=True)
os.makedirs(kakao_download_backup_folder, exist_ok=True)

# 파일 백업 함수
def backup_files(source, destination):
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

# 바탕화면, 다운로드, Kakao Download 폴더 백업
backup_files(desktop_path, desktop_backup_folder)
backup_files(downloads_path, downloads_backup_folder)
backup_files(kakao_download_path, kakao_download_backup_folder)

print(f"백업이 성공적으로 완료되었습니다: {backup_folder}")
