import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk


class ImageCropGUI:
    def __init__(self, image_path, hashed_name):
        self.original_image = cv2.imread(image_path)
        self.image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
        self.target_image = Image.open(f"./src/{hashed_name}/thumbnail.jpg")
        self.output_path = f"./src/{hashed_name}/cropped_thumb.jpg"
        self.cropped_image = None
        self.crop_rect = None
        self.top_left = None
        self.bottom_right = None

        self.root = Tk()
        self.root.title("Image Crop GUI")

        self.canvas_width = 1280
        self.canvas_height = 720

        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.image_tk = ImageTk.PhotoImage(Image.fromarray(self.image))
        self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.button_crop = Button(self.root, text="Crop Image", command=self.button_clicked)
        self.button_crop.pack(pady=10)

        self.root.mainloop()

    def button_clicked(self):
        if self.top_left and self.bottom_right:
            self.cropped_image = self.target_image.crop((self.top_left[0], self.top_left[1],
                                                         self.bottom_right[0], self.bottom_right[1]))
            self.cropped_image.save(self.output_path)
            # self.crop_image = self.original_image.crop(
            # (self.top_left[0], self.top_left[1], self.bottom_right[0], self.bottom_right[1]))
            # self.crop_image.save("cropped_image.jpg")
            self.root.destroy()

    def on_click(self, event):
        self.top_left = (event.x, event.y)
        self.crop_rect = None
        print("a")

    def on_drag(self, event):
        self.bottom_right = (event.x, event.y)
        self.draw_crop_rect()

    def on_release(self, event):
        self.bottom_right = (event.x, event.y)
        self.draw_crop_rect()

    def draw_crop_rect(self):
        if self.crop_rect:
            self.canvas.delete(self.crop_rect)
        if self.top_left and self.bottom_right:
            self.crop_rect = self.canvas.create_rectangle(self.top_left[0], self.top_left[1], self.bottom_right[0],
                                                          self.bottom_right[1], outline="red")
        # print("setting: ", self.top_left[0], self.top_left[1], self.bottom_right[0], self.bottom_right[1])
