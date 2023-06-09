import os
import shutil
import requests as req
from bs4 import BeautifulSoup


def download_thum(url):
    hashed_name = url[-11:]
    response = req.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    thumbnail_meta = soup.find_all("meta", property="og:image")

    thumbnail_url = None
    for meta in thumbnail_meta:
        content = meta.get("content")
        if "maxresdefault.jpg" in content:
            thumbnail_url = content
            break
        elif "hqdefault.jpg" in content:
            thumbnail_url = content

    if not os.path.isdir(f"./src/{hashed_name}"):
        os.makedirs(f"./src/{hashed_name}")

    if thumbnail_url:
        # 이미지 다운로드
        thumbnail_data = req.get(thumbnail_url).content
        with open(f"./src/{hashed_name}/thumbnail.jpg", "wb") as f:
            f.write(thumbnail_data)
    else:
        print("해상도 높은 썸네일을 찾을 수 없습니다.")
