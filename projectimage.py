import customtkinter as ctk
from tkinter import filedialog
import matplotlib.pyplot as plt
import cv2
import numpy as np
from scipy import stats
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ===== باقي دوال المعالجة كما هي =====

def point_operations(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    add_img = cv2.add(img, 50)
    sub_img = cv2.subtract(img, 50)
    div_img = cv2.divide(img, 2)
    comp_img = cv2.bitwise_not(img)
    show_results(['Original','Addition','Subtraction','Division','Complement'],
                 [img,add_img,sub_img,div_img,comp_img], cmap='gray')


def show_results(titles, images, cmap=None):
    plt.figure(figsize=(15,8))
    for i in range(len(images)):
        plt.subplot(2,(len(images)+1)//2,i+1)
        plt.imshow(images[i], cmap=cmap)
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()


# ===== GUI =====

class ImageProcessingApp:

    def __init__(self):

        self.root = ctk.CTk()
        self.root.title("Image Processing App")
        self.root.geometry("700x500")

        self.img_path = None

        self.create_widgets()

    def create_widgets(self):

        self.path_label = ctk.CTkLabel(self.root,
                                       text="No image loaded")
        self.path_label.pack(pady=10)


        load_btn = ctk.CTkButton(self.root,
                                 text="Load Image",
                                 command=self.load_image)
        load_btn.pack(pady=10)


        btn_frame = ctk.CTkFrame(self.root)
        btn_frame.pack(pady=10)


        tasks = [
            ("Point Ops", point_operations),
        ]


        for i,(name,func) in enumerate(tasks):

            btn = ctk.CTkButton(btn_frame,
                                text=name,
                                command=lambda f=func: self.run_task(f),
                                width=150)

            btn.grid(row=i//3, column=i%3, padx=10, pady=10)


        exit_btn = ctk.CTkButton(self.root,
                                 text="Exit",
                                 fg_color="red",
                                 command=self.root.quit)

        exit_btn.pack(pady=20)


    def load_image(self):

        path = filedialog.askopenfilename(
            filetypes=[("Images","*.jpg *.png *.jpeg *.bmp")]
        )

        if path:
            self.img_path = path
            self.path_label.configure(text=f"Loaded: {path}")


    def run_task(self,func):

        if self.img_path:
            func(self.img_path)
        else:
            self.path_label.configure(text="Load image first")


    def run(self):
        self.root.mainloop()



# ===== Run =====

if __name__ == "__main__":

    app = ImageProcessingApp()
    app.run()