
import tkinter as tk
from tkinter import *

class SecondGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Second")
        self.root.geometry("400x300")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.label = tk.Label(self.main_frame, text="Welcome to My App!")
        self.label.grid(row=0, column=0, pady=10)

        self.button = tk.Button(self.main_frame, text="drop down menu", command=self.on_button_click)
        self.button.grid(row=1, column=0, pady=10)

    def on_button_click(self):
        self.label.config(text=)

if __name__ == "__main__":
    root = tk.Tk()
    main = ManinGUI(root)


class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis")
        self.root.geometry("400x300")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.label = tk.Label(self.main_frame, text="Welcome to My App!")
        self.label.grid(row=0, column=0, pady=10)

        self.button = tk.Button(self.main_frame, text="drop down menu", command=self.on_button_click)
        self.button.grid(row=1, column=0, pady=10)

    def on_button_click(self):
        self.label.config(text=)

if __name__ == "__main__":
    root = tk.Tk()
    main = ManinGUI(root)
    root.mainloop()

window.mainloop()