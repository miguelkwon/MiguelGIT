import os
import filecmp

# 폴더 내의 파일 목록을 가져오는 함수
def get_file_list(folder):
    file_list = []
    for root, _, files in os.walk(folder):
        for file in files:
            # 폴더 내 상대 경로로 저장
            relative_path = os.path.relpath(os.path.join(root, file), folder)
            file_list.append(relative_path)
    return sorted(file_list)

# 두 폴더의 파일 목록을 비교하여 차이점 출력
def compare_folders(folder1, folder2):
    files_in_folder1 = get_file_list(folder1)
    files_in_folder2 = get_file_list(folder2)

    print(f"폴더 1 ({folder1})의 파일 목록:")
    for file in files_in_folder1:
        print(file)

    print(f"\n폴더 2 ({folder2})의 파일 목록:")
    for file in files_in_folder2:
        print(file)

    # 파일 목록 차이 비교
    only_in_folder1 = set(files_in_folder1) - set(files_in_folder2)
    only_in_folder2 = set(files_in_folder2) - set(files_in_folder1)

    if only_in_folder1:
        print("\n폴더 1에만 있는 파일들:")
        for file in only_in_folder1:
            print(file)

    if only_in_folder2:
        print("\n폴더 2에만 있는 파일들:")
        for file in only_in_folder2:
            print(file)

    # 두 폴더에 공통으로 있는 파일들의 내용 비교
    common_files = set(files_in_folder1).intersection(set(files_in_folder2))
    different_files = []
    
    for file in common_files:
        file1 = os.path.join(folder1, file)
        file2 = os.path.join(folder2, file)
        # 파일 내용을 비교
        if not filecmp.cmp(file1, file2, shallow=False):
            different_files.append(file)

    if different_files:
        print("\n다음 파일들의 내용이 다릅니다:")
        for file in different_files:
            print(file)
    else:
        print("\n공통된 파일들의 내용이 모두 동일합니다.")

# 폴더 경로 설정
folder1_path = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (2)'
folder2_path = 'F:\OneDrive - Radiant Vision Systems\바탕 화면\새 폴더 (3)'

# 폴더 비교 실행
compare_folders(folder1_path, folder2_path)
