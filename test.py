from ymd_prj.sequence.tube_req import download_thum
from ymd_prj.sequence.tube_mp3 import download_mp3

url = "https://www.youtube.com/watch?v=YGgahso4Zto"
# 1. thum
download_thum(url)
# 2. mp3
download_mp3(url)