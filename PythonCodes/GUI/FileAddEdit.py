import tkinter as tk


def openfileGUI():
    fileswindow = tk.Toplevel(root)
    fileswindow.title("Files")
    fileswindow.geometry("300x200")

root = tk.Tk()
button = tk.Button(root, text="Add/Edit Files", command=openfileGUI)

button.pack()

root.mainloop()
