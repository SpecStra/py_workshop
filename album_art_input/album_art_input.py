import os
from mutagen.id3 import ID3, APIC, TALB

src_path = "./src"

if not os.path.exists(src_path):
    os.makedirs(src_path)
    print(f"{src_path} directory created.")
else:
    print(f"{src_path} directory already exists.")


def modify_mp3(mp3_path: str, img_path: str, album: str):
    # mp3 파일 경로
    file_path = f"{mp3_path}"

    # ID3 태그 정보 불러오기
    try:
        tags = ID3(file_path)
    except:
        tags = ID3()

    # 앨범 수정
    tags["TALB"] = TALB(encoding=3, text=[album])

    # 앨범아트 수정
    with open(f"{img_path}", "rb") as albumart_file:
        albumart_data = albumart_file.read()
        tags["APIC"] = APIC(
            encoding=3,
            mime="image/jpeg",
            type=3,
            desc=u"Cover",
            data=albumart_data
        )

    # 태그 정보 저장
    tags.save(file_path)


img_name = ""

# src 폴더 내의 각 폴더에 접근하여 파일 목록 출력
for folder in os.listdir(src_path):
    folder_path = os.path.join(src_path, folder)
    if os.path.isdir(folder_path):
        print(f"Files in {folder}:")
        img_solate = list(filter(lambda x: ".png" in x or ".jpg" in x, os.listdir(folder_path)))
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                print(file)
            if os.path.isfile(file_path):
                if ".mp3" in file:
                    modify_mp3(
                        mp3_path=f"./src/{folder}/{file}",
                        img_path=f"./src/{folder}/{img_solate[0]}",
                        album=folder
                    )
