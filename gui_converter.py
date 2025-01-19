import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
from overlay_video_with_shape import main

def select_directory():
    # Open a dialog to select a directory
    directory = filedialog.askdirectory()
    if directory:
        directory_label.config(text=directory)  # Update label with selected directory
        global selected_directory
        selected_directory = directory  # Store the selected directory

def select_output_directory():
    # Open a dialog to select an output directory
    output_directory = filedialog.askdirectory()
    if output_directory:
        output_label.config(text=output_directory)  # Update label with selected output directory
        global selected_output_directory
        selected_output_directory = output_directory  # Store the selected output directory

def convert_presentation():
    try:
        if not selected_directory or not selected_output_directory:
            messagebox.showwarning("Warning", "Please select both input and output directories.")
            return
        
        # Set the directories based on the selected directory
        pptx_directory = selected_directory  # Assuming "ppt" folder is under the selected directory
        output_directory = selected_output_directory  # Use the user-defined output directory

        # Call the main function with the selected directories
        main(pptx_directory, output_directory)
        messagebox.showinfo("Success", "Conversion completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("PPT to PDF Converter")

# Label to display the selected directory
directory_label = tk.Label(root, text="No input directory selected", wraplength=300)
directory_label.pack(pady=10)

# Button to select the input directory
select_button = tk.Button(root, text="Select Input Directory", command=select_directory, padx=20, pady=10)
select_button.pack(pady=10)

# Label to display the selected output directory
output_label = tk.Label(root, text="No output directory selected", wraplength=300)
output_label.pack(pady=10)

# Button to select the output directory
output_button = tk.Button(root, text="Select Output Directory", command=select_output_directory, padx=20, pady=10)
output_button.pack(pady=10)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_presentation, padx=20, pady=10)
convert_button.pack(pady=20)

# Variables to store the selected directories
selected_directory = ""
selected_output_directory = ""

# Run the GUI loop
root.mainloop()