import os, sys
from tkinter import *
import random
import time
import math


# generate a new rgb value to give to the given UI element
def change_color(root):
    r = str(hex(random.randint(0, 255)))[2:]
    g = str(hex(random.randint(0, 255)))[2:]
    b = str(hex(random.randint(0, 255)))[2:]
    if len(r) == 1:
        r = '0'+r
    if len(g) == 1:
        g = '0'+g
    if len(b) == 1:
        b = '0'+b

    hex_number = '#' + r + g + b
    root.configure(bg=hex_number)

    # call this function again in one second
    root.after(200, change_color, root)


def convert_val_to_color(v):
    pass


base_20_yrold_target_exer_hr = 100
max_20_yrold_target_exer_hr = 170

base_30_yrold_target_exer_hr = 95
max_30_yrold_target_exer_hr = 162

# initialize random
random.seed(time.localtime())

# tkinter UI setup and start
window = Tk()
window.title("")
window.configure(bg="red")
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
change_color(window)
window.mainloop()


