from ymd_prj.sequence.tube_req import download_thum
from ymd_prj.sequence.tube_mp3 import download_mp3
from ymd_prj.sequence.gui_load import ImageCropGUI
from ymd_prj.sequence.mp3_modify import modify_mp3
from ymd_prj.sequence.finish import last_check
import os

# 0. User setting
url = "https://www.youtube.com/watch?v=blA7epJJaR4"
hashed_name = url[-11:]
music_title = "Higher"
music_singer = "Tobu"

# 1. thum
download_thum(url)

# 2. mp3
download_mp3(url)

# 3. crop from gui
def gui_on():
    thumb_url = f"./src/{hashed_name}/thumbnail.jpg"
    if os.path.isfile(thumb_url):
        ImageCropGUI(thumb_url, hashed_name)
    else:
        print("썸네일이 없습니다")
        exit()

gui_on()

# 4. resizing?

# 5. mp3 gui load
modify_mp3(title=music_title, singer=music_singer, album=url, hashed_path=hashed_name)

# 6. move to output, check, delete dummy files
last_check(music_title, hashed_name)