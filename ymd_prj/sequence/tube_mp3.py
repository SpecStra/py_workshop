from pytube import YouTube
from moviepy.editor import *


def download_mp3(url):
    hashed_name = url[-11:]
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download()

    audio = AudioFileClip(output_file)
    audio.write_audiofile(f"./src/{hashed_name}/sound.mp3")

    os.remove(output_file)

