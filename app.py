import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog
from pygifsicle import optimize

root = tk.Tk()
root.withdraw()

file = filedialog.askopenfilename()
data = input("Please enter 0.1~1.0: ")
size = float(data)

if(size):
    Clip = VideoFileClip(file).resize(size)
    gif = Clip.write_gif(r"output.gif", fps = 24)


del gif
del Clip

print("轉換完成")