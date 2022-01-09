import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog
from pygifsicle import optimize

root = tk.Tk()
root.withdraw()

file = filedialog.askopenfilename()
#file_name = file.split('/')[-1]

Clip = VideoFileClip(file).resize(0.4)

gif = Clip.write_gif(r"output.gif", fps = 24)

del gif
del Clip

print("轉換完成")