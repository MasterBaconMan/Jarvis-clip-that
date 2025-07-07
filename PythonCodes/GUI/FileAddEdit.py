import tkinter as tk


def openfileGUI():
    fileswindow = tk.Toplevel(root)
    fileswindow.title("Files")

    clipbutton = tk.Button(fileswindow, text="Clip", command=lambda:openeditor)


def openeditor(title):
    editor_window = tk.Toplevel(root)
    editor_window.title(title)


root = tk.Tk()
button = tk.Button(root, text="Add/Edit Files", command=openfileGUI)

button.pack()

root.mainloop()