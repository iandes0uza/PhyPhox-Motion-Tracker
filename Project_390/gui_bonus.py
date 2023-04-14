import tkinter as tk
import pandas as pd
import os
from PIL import Image, ImageTk
from tkinter import filedialog
from gui_backend import gui_execute

# Create the main window
root = tk.Tk()
filepath = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
root.title("My GUI")
root.geometry("1700x1900")  # Set window size

# Create a label widget
label = tk.Label(root, text="ELEC 390 Final Project Results", font=("Helvetica", 24), fg="#333", bg="#eee")
label.pack(pady=20)

# Create a sublabel widget
sublabel = tk.Label(root, text="Group 47", font=("Helvetica", 18), fg="#666", bg="#eee")
sublabel.pack()
# Create a sublabel widget
sublabel1 = tk.Label(root, text="Omar Barakat – 20199519 – 19oksb@queensu.ca\n Ian Desouza – 20232372 – 20iagd@queensu.ca \n Jacob O’Neil – 20221893 – 19jmon1@queensu.ca \n ", font=("Helvetica", 12), fg="#666", bg="#eee")
sublabel1.pack()

raw = pd.read_csv('accelerations.csv')
walk_jump = gui_execute(raw)
if (walk_jump): print("YEAS")
else: print("NO")
os.system('python Bonus.py')

root.mainloop()