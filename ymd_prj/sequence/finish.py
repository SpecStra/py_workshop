import os
import shutil


def last_check(title: str, hashed_path: str):
    moto_file = f"./src/{hashed_path}/sound.mp3"
    out_file = f"./output/01_{title}.mp3"
    shutil.move(moto_file, out_file)

    # 파일이 mp3 파일인지 확인
    if os.path.isfile(out_file) and out_file.endswith(".mp3"):
        # mp3 파일 실행
        os.system(f"start {out_file}")
    else:
        print("This is not an mp3 file.")

    user_input = input("Press Enter to continue or type 'q' to quit: ")
    if user_input.lower() == "q":
        exit()

    # 삭제할 폴더 경로
    folder_path = f"./src/{hashed_path}"

    # 폴더 내부의 파일 모두 삭제
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    # 폴더 자체 삭제
    try:
        os.rmdir(folder_path)
    except Exception as e:
        print(f"Failed to delete {folder_path}. Reason: {e}")
