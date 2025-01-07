from tkinter import *
from fungsi import *
import os


os.system("cls")

base = Tk()
base.config(background="light blue")
base.title("INPUT DATA KE SQLite")

# Get screen width and height
screen_width = base.winfo_screenwidth()
screen_height = base.winfo_screenheight()
 
# Set window dimensions
window_width = 400
window_height = 300
 
# Calculate x and y coordinates to center the window
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window with center position
base.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")



# label 
label_id()
label_nama()
label_gender()
Label_alamat()
Label_telepon()

# Text
text_id()
text_nama()
text_gender()
text_alamat()
text_telepon()

# button
submit()

base.mainloop()
 