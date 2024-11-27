
import os
import hashlib

# 폴더 경로 설정
folder1 = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (2)'
folder2 = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (3)'

# 해시 값을 계산하는 함수
def calculate_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# 폴더의 모든 TIFF 파일의 해시 값을 저장하는 함수
def get_tiff_files_hash(folder):
    hash_dict = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.tif') or file.lower().endswith('.tiff'):
                file_path = os.path.join(root, file)
                file_hash = calculate_hash(file_path)
                hash_dict[file] = file_hash
    return hash_dict

# 두 폴더의 TIFF 파일을 비교하는 함수
def compare_folders(folder1, folder2):
    folder1_hashes = get_tiff_files_hash(folder1)
    folder2_hashes = get_tiff_files_hash(folder2)

    all_files = set(folder1_hashes.keys()).union(set(folder2_hashes.keys()))
    for file in all_files:
        hash1 = folder1_hashes.get(file, None)
        hash2 = folder2_hashes.get(file, None)
        
        if hash1 == hash2:
            print(f"{file}: 동일")
        else:
            print(f"{file}: 다름")

# 비교 실행
compare_folders(folder1, folder2)
