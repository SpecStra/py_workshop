import cv2
import numpy as np
import pytesseract
import pyperclip
import time
from PIL import ImageGrab
import requests as req

# 좌표 범위
x, y, w, h = 420, 870, 1415, 1030

last_copied_text = ''  # 이전에 클립보드에 복사한 텍스트

while True:
    # 화면 캡처
    img = np.array(ImageGrab.grab(bbox=(x, y, x+w, y+h)))

    # 이미지 전처리
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # OCR 수행
    text = pytesseract.image_to_string(gray, lang='jpn')

    if text != last_copied_text:
        last_copied_text = text
        print(text)

    # 추출된 텍스트를 클립 보드에 저장
    pyperclip.copy(text)

    # 0.1초 대기
    time.sleep(1)
