import tkinter as tk
from tkinter import filedialog
import pyttsx3

def read_file(file_path):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 1)  # Volume 0-1
    with open(file_path, 'r') as file:
        text = file.read()
        engine.say(text)
        engine.runAndWait()

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        read_file(file_path)

def main():
    root = tk.Tk()
    root.title("Text-to-Speech Reader")

    label = tk.Label(root, text="Select a text file to read aloud:")
    label.pack(pady=10)

    button = tk.Button(root, text="Select File", command=select_file)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

# This example assumes .txt files for simplicity.
# You can extend it to support other formats or handle exceptions for unsupported files.
# Adjust rate and volume properties in read_file() as per your preference.
# Customize the GUI further to suit your needs (e.g., add more buttons, labels, or functionalities).