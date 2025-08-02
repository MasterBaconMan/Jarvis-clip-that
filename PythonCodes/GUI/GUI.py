# import nesesarry librairies 
from tkinter import *
from tkinter import ttk

# set up GUI window
home = Tk()
home.title("Jarvis Home")
home.geometry("600x400")

# placeholder for dropdown options, will be able to select 
drop_down_options = ["", "Mic 1", "Mic 2", "Mic 3", "Mic 4"]

#Every label is defined here
labelName = Label(home, text = "Input Name:", font=("Arial", 10))
labelName.grid(row=1, column=0, pady=0, padx=0)

currentName = Label(home, text = "Current Name: Jarvis", font=("Arial", 10))
currentName.grid(row=1, column=4, pady=0, padx=0)

inputTime = Label(home, text = "Input Clip Time:", font=("Arial", 10))
inputTime.grid(row=2, column=0, pady=5, padx=0)

currentTime = Label(home, text = "Current Time: 0.00", font=("Arial", 10))
currentTime.grid(row=2, column=4, pady=5, padx=0)

labelMic = Label(home, text = "Select Microphone", font=("Arial", 10))
labelMic.grid(row=3, column=0, pady=0, padx=0)

currentMic = Label(home, text = "Current Microphone:", font=("Arial", 10))
currentMic.grid(row=3, column=4, pady=0, padx=0)

#Every entry is defined here
timeEntry = Entry(home, width=30)
timeEntry.grid(row=2, column=2, pady=5, padx=0)

entry = Entry(home, width=30)
entry.grid(row=1, column=2, pady=0, padx=0)

#defining the dropdown menu
selected_option = StringVar()
selected_option.set(drop_down_options[0])

dropdown = ttk.Combobox(home, textvariable=selected_option, values=drop_down_options, state="readonly")
dropdown.grid(row=3, column=2, pady=10)

#every current function that each button does
def confirmMic():
    user_input = selected_option.get()
    currentMic.config(text=f"Current Microphone: {user_input}")
    with open("settings.txt", "a") as file:
      file.write(user_input + "\n")
    

def confirmName():
  user_input = entry.get()
  currentName.config(text=f"Current Name: {user_input}")
  with open("settings.txt", "a") as file:
    file.write(user_input + "\n")

def confirmTime():
  user_input = timeEntry.get()
  currentTime.config(text=f"Current Time: {user_input}")
  with open("settings.txt", "a") as file:
    file.write(user_input + "\n")

#every button is defined here
nameButton = Button(home, text="Confirm", command=confirmName)
nameButton.grid(row=1, column=3, pady=0, padx=0)

micButton = Button(home, text="Confirm", command=confirmMic)
micButton.grid(row=3, column=3, pady=10)

timeButton = Button(home, text="Confirm", command=confirmTime)
timeButton.grid(row=2, column=3, pady=0, padx=0)


home.mainloop()