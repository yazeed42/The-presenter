## Not completed code, just a prototype for the GUI and not complete

import os
import tkinter as tk
from tkinter import Image, filedialog
from tkinter.tix import IMAGETEXT
# from pptx import Presentation
# from Pylance import ImageTk

# Create the main application window
app = tk.Tk()
app.title("PowerPoint to Video Converter")

# Configure the GUI window size
app.geometry("1600x900")  # Set your desired width and height

# Function to handle file selection and conversion
def convert_ppt_to_video():
    file_path = filedialog.askopenfilename(filetypes=[("PowerPoint Files", "*.pptx")])
    if file_path:
        # Update the file_label to display the selected file name
        file_label.config(text="Selected file: " + os.path.basename(file_path))
        # You can also store the file_path in a global variable for further use
        # global selected_file_path
        # selected_file_path = file_path
        # ...
        # Add code here to parse slides and convert to video
        # Update the UI to display conversion progress or results

# Function to clear the selected file
def clear_file():
    file_label.config(text="No file selected")

# Load custom button images
select_button_image = tk.PhotoImage(file='prototypes/img/select_button.png')
clear_button_image = tk.PhotoImage(file='prototypes/img/clear_button.png')


# Create and configure GUI components using the DarkTheme style
file_label = tk.Label(app, text="No file selected")
select_button = tk.Button(app, image=select_button_image, command=convert_ppt_to_video, borderwidth=0)
clear_button = tk.Button(app, image=clear_button_image, command=clear_file, borderwidth=0)


# Layout GUI components
file_label.pack(pady=10)
select_button.pack()
clear_button.pack()

# Configure the root window background color
app.configure(bg="#1e1e1e")  # Set your desired background color

# Start the GUI application
app.mainloop()
