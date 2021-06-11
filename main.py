from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import *
import tkinter
import os

from scripts.image_ob import *
from scripts.video_ob import *
from scripts.web_cam import *

y_spacing_no = 120
y_spacing_y = 270

current_path = os.path.dirname(__file__)
output_loc = os.path.join(current_path, 'outputs/')


def op_loc():
    os.startfile(output_loc)


def search_image_t():
    image1 = filedialog.askopenfilename()
    if image1:
        img_obj_dection(image1, True)


def search_vid_t():
    image1 = filedialog.askopenfilename()
    if image1:
        vid_obj_dection(image1, True)


def search_image_f():
    image1 = filedialog.askopenfilename()
    if image1:
        img_obj_dection(image1, False)


def search_vid_f():
    image1 = filedialog.askopenfilename()
    if image1:
        vid_obj_dection(image1, False)


root = tk.Tk()
root.geometry('600x600-100-100')
root.resizable(False, False)
root.configure(background='#212121')
root.title('yv3_351 -Lucii')


title = tk.Label(
    root, text="Project Yolo_v3_obj [3.5.1]", font="Arial 24", bg='white', width=400).pack()

q_disp = tk.Label(
    root, text=" * Hit 'Q' to exit any operation", font="Arial 18", bg='#212121', fg='#ffffff').place(x=140, y=60)

image_T = tkinter.Button(
    root, text="Image", font="Arial 18", bg='#414141', fg='#ffffff', width=10, command=search_image_f).place(x=20, y=y_spacing_no)

video_T = tkinter.Button(
    root, text="Video", font="Arial 18", bg='#414141', fg='#ffffff', width=10, command=search_vid_f).place(x=220, y=y_spacing_no)

Cam_button_T = tkinter.Button(
    root, text="Web Cam", font="Arial 18", bg='#414141', fg='#ffffff', width=10, command=web_cam_f).place(x=420,  y=y_spacing_no)

op_text = tk.Label(
    root, text=" * To generate output files", font="Arial 18", bg='#212121', fg='#ffffff').place(x=140, y=200)

image_F = tkinter.Button(
    root, text="Image", font="Arial 18", bg='#414141', fg='#ffffff', width=10, command=search_image_t).place(x=20,  y=y_spacing_y)

video_F = tkinter.Button(
    root, text="Video ", font="Arial 18", bg='#414141', fg='#ffffff', width=10, command=search_vid_t).place(x=220, y=y_spacing_y)

Cam_button_F = tkinter.Button(
    root, text="Web Cam", font="Arial 18", bg='#414141', fg='#ffffff', width=10, command=web_cam_t).place(x=420, y=y_spacing_y)

disp = tk.Label(root, text=" Web cam takes time to load\n  \nEvery image and video \n processed will be saved into outputs folder  ",
                font="Arial 18", bg='#212121', fg='#ffffff').place(x=30, y=350)

file_open = tkinter.Button(
    root, text="Output Folder", font="Arial 18", bg='#414141', fg='#ffffff', command=op_loc).place(x=200, y=510)

auther = tk.Label(
    root, text="- Lucii -", font="Arial 18", bg='#212121', fg='#ffffff').place(x=480, y=550)

root.mainloop()
