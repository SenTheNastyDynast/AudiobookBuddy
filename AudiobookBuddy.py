import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Function to handle radio button selection
def toggle_input_mode():
    if input_mode.get() == "Text":
        text_input_field.pack(fill=tk.X, padx=5, pady=5)
        file_input_frame.pack_forget()
    else:
        text_input_field.pack_forget()
        file_input_frame.pack(fill=tk.X, padx=5, pady=5)

# Function to search for a file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_input_field.delete(0, tk.END)
        file_input_field.insert(0, file_path)

# Function to list available voices
def list_voices():
    cmd = "edge-tts --list-voices"
    subprocess.Popen(cmd, shell=True)

# Function to open the output folder
def open_output_folder():
    folder_path = r"A:\Audiobook Buddy"
    os.startfile(folder_path)

# Function to generate the final command and run it in CMD
def generate_command():
    voice = voice_input.get()
    if not voice:
        messagebox.showerror("Error", "Voice field cannot be empty!")
        return

    # Collect the relevant user inputs
    if input_mode.get() == "Text":
        text = text_input_field.get("1.0", tk.END).strip()
        cmd = f'edge-playback --text "{text}" --voice {voice}'
    else:
        file_path = file_input_field.get()
        cmd = f'edge-playback --file "{file_path}" --voice {voice}'

    # Add optional parameters
    rate_value = rate_slider.get()
    if rate_value != 0:
        cmd += f" --rate={rate_value:+d}%"

    volume_value = volume_slider.get()
    if volume_value != 0:
        cmd += f" --volume={volume_value:+d}%"

    pitch_value = pitch_slider.get()
    if pitch_value != 0:
        cmd += f" --pitch={pitch_value:+d}Hz"

    filename = filename_input.get().strip()
    if filename:
        cmd += f" --write-media {filename}"

    # Run the command in a new CMD window
    subprocess.Popen(cmd, shell=True)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Audiobook Buddy")
root.geometry("500x600")

# Input mode: Text or File
input_mode = tk.StringVar(value="Text")
radio_frame = tk.Frame(root)
radio_frame.pack(fill=tk.X, padx=5, pady=5)

tk.Radiobutton(radio_frame, text="Text", variable=input_mode, value="Text", command=toggle_input_mode).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(radio_frame, text="File", variable=input_mode, value="File", command=toggle_input_mode).pack(side=tk.LEFT, padx=5)

# Text input field (default)
text_input_field = tk.Text(root, height=5)
text_input_field.insert(tk.END, "Hello, world! This is just a test to verify the accuracy and quality of the voice model. So, what do you think? Pretty cool, huh?")
text_input_field.pack(fill=tk.X, padx=5, pady=5)

# File input field (hidden by default)
file_input_frame = tk.Frame(root)
file_input_field = tk.Entry(file_input_frame)
file_input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
file_browse_button = tk.Button(file_input_frame, text="Search", command=browse_file)
file_browse_button.pack(side=tk.LEFT, padx=5)

# Voice input
voice_input_frame = tk.Frame(root)
voice_input_frame.pack(fill=tk.X, padx=5, pady=5)
tk.Button(voice_input_frame, text="List Voices", command=list_voices).pack(side=tk.LEFT)
voice_input = tk.Entry(voice_input_frame)
voice_input.insert(0, "en-US-Aria")
voice_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

# Sliders: Rate, Volume, and Pitch
rate_slider = tk.Scale(root, from_=-100, to=100, label="Rate:", orient=tk.HORIZONTAL)
rate_slider.set(0)
rate_slider.pack(fill=tk.X, padx=5, pady=5)

volume_slider = tk.Scale(root, from_=-100, to=100, label="Volume:", orient=tk.HORIZONTAL)
volume_slider.set(0)
volume_slider.pack(fill=tk.X, padx=5, pady=5)

pitch_slider = tk.Scale(root, from_=-500, to=500, label="Pitch:", orient=tk.HORIZONTAL)
pitch_slider.set(0)
pitch_slider.pack(fill=tk.X, padx=5, pady=5)

# Filename input
filename_frame = tk.Frame(root)
filename_frame.pack(fill=tk.X, padx=5, pady=5)

filename_label = tk.Label(filename_frame, text="Filename:")
filename_label.pack(side=tk.LEFT, padx=5)

filename_input = tk.Entry(filename_frame)
filename_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

# Buttons for opening output folder and generating command
buttons_frame = tk.Frame(root)
buttons_frame.pack(fill=tk.X, padx=5, pady=5)

open_folder_button = tk.Button(buttons_frame, text="Open Output Folder", command=open_output_folder)
open_folder_button.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(buttons_frame, text="Generate", command=generate_command)
generate_button.pack(side=tk.LEFT, padx=5)

# Start the application
toggle_input_mode()  # Set initial view
root.mainloop()
