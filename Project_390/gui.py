import tkinter as tk
import sys
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
sublabel1 = tk.Label(root, text="Omar Barakat – 20199519 – 19oksb@queensu.ca\n Ian Desouza – {Insert Student #} – 20iagd@queensu.ca \n Jacob O’Neil – 20221893 – 19jmon1@queensu.ca \n ", font=("Helvetica", 12), fg="#666", bg="#eee")
sublabel1.pack()

def runGUI():
    label = tk.Label(root, text="Using File Path: "+ filepath+"")
    label.pack()
    label = tk.Label(root, text="Predicted Movement Type:")
    label.pack()
    walk_or_run = gui_execute(filepath)
    if (walk_or_run):
        label = tk.Label(root, text="Jumping", font=("Comic Sans", 46))
    else:
        label = tk.Label(root, text="Walking", font=("Comic Sans", 46))
    label.pack()
    button_b.pack(pady=10)
    button_c.pack(pady=10)
    button_d.pack(pady=10)
    button_e.pack(pady=10)
    button_f.pack(pady=10)
    button_g.pack(pady=10)
    button_a.pack_forget()

def die():
    sys.exit
# Function to display an image
def display_image(image_file):

    image = Image.open(image_file)
    image = image.resize((1400, 600))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

# Define the image file names for each button
proc = "grab_img/proc.png"
raw = "grab_img/raw.png"
rpabs = "grab_img/rpabs.png"
rpx = "grab_img/rpx.png"
rpy = "grab_img/rpy.png"
rpz = "grab_img/rpz.png"

# Create five buttons that display different images
button_a = tk.Button(root, text="Begin Analysis", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: runGUI())
button_a.pack(pady=10)

button_b = tk.Button(root, text="Show Processed Graph", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(proc))
button_b.pack_forget()

button_c = tk.Button(root, text="Show Raw Graph", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(raw))
button_c.pack_forget()

button_d = tk.Button(root, text="Show X-Axis Graph", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(rpx))
button_d.pack_forget()

button_e = tk.Button(root, text="Show Y-Axis Graph", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(rpy))
button_e.pack_forget()

button_f = tk.Button(root, text="Show Z-Axis Graph", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(rpz))
button_f.pack_forget()

button_g = tk.Button(root, text="Show Absolute Graph", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: display_image(rpabs))
button_g.pack_forget()

# button_exit = tk.Button(root, text="Show Absolute Graph", font=("Helvetica", 16), fg="#fff", bg="#333", command=lambda: die())
# button_exit.pack(pady=10)
# Run the main event loop
root.mainloop()