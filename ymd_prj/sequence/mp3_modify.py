from mutagen.id3 import ID3, APIC, error, TIT2, TPE1, TALB



def modify_mp3(title: str, singer: str, album: str, hashed_path: str):
    # mp3 파일 경로
    file_path = f"./src/{hashed_path}/sound.mp3"

    # ID3 태그 정보 불러오기
    try:
        tags = ID3(file_path)
    except:
        tags = ID3()

    # 제목 수정
    tags["TIT2"] = TIT2(encoding=3, text=[title])

    # 가수 수정
    tags["TPE1"] = TPE1(encoding=3, text=[singer])

    # 앨범 수정
    tags["TALB"] = TALB(encoding=3, text=[album])

    # 앨범아트 수정
    with open(f"./src/{hashed_path}/cropped_thumb.jpg", "rb") as albumart_file:
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
