# import nesesarry librairies \
import subprocess
import speech_recognition as sr
from tkinter import *
from tkinter import ttk

miclist = {}
drop_down_options = []

for index, name in enumerate(sr.Microphone.list_microphone_names()):
  miclist.update({index:name})

temp = []
res = dict()

for key, val in miclist.items():
  if val not in temp:
    temp.append(val)
    res[key] = val

search_word = "Microphone"
filter_out_word = "Speakers"

filtered_mics = {key: value for key, value in res.items() if (search_word in value) and (filter_out_word not in value)}

print(str(filtered_mics))

# Function to read from speech to text file

#def readfile():
#    file = open("PythonCodes\\Speech\\text.txt", "rt")
#    return file.readlines()

# set up GUI window
home = Tk()
home.title("Jarvis Home")
home.geometry("600x400")

# placeholder for dropdown options, will be able to select 
for key,item in filtered_mics.items():
  drop_down_options.append(f"{key} : {item}")


# drop_down_options = ["", "Mic 1", "Mic 2", "Mic 3", "Mic 4"]

#Every label is defined here
labelName = Label(home, text = "Input Name:", font=("Arial", 10))
labelName.grid(row=1, column=0, pady=0, padx=0)

currentName = Label(home, text = "", font=("Arial", 10))
currentName.grid(row=1, column=4, pady=0, padx=0)

inputTime = Label(home, text = "Input WebSocket Server password:", font=("Arial", 10))
inputTime.grid(row=2, column=0, pady=5, padx=0)

currentTime = Label(home, text = "", font=("Arial", 10))
currentTime.grid(row=2, column=4, pady=5, padx=0)

labelMic = Label(home, text = "Select Microphone", font=("Arial", 10))
labelMic.grid(row=3, column=0, pady=0, padx=0)

currentMic = Label(home, text = "", font=("Arial", 10))
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
  currentMic.config(text="Saved!")
  with open("PythonCodes\\GUI\\Settings.txt", "r") as file:
    lines = file.readlines()
    file.close()
  lineToPrint = 2
  lines[lineToPrint] = user_input + "\n"
  with open("PythonCodes\\GUI\\Settings.txt", "w") as file:
    file.writelines(lines)
    file.close()
    

def confirmName():
  user_input = entry.get()
  currentName.config(text="Saved!")
  with open("PythonCodes\\GUI\\Settings.txt", "r") as file:
    lines = file.readlines()
    file.close()
  lineToPrint = 0
  lines[lineToPrint] = user_input + "\n"
  with open("PythonCodes\\GUI\\Settings.txt", "w") as file:
    file.writelines(lines)
    file.close()

def confirmTime():
  user_input = timeEntry.get()
  currentTime.config(text="Saved!")
  with open("PythonCodes\\GUI\\Settings.txt", "r") as file:
    lines = file.readlines()
    file.close()
  lineToPrint = 1
  lines[lineToPrint] = user_input + "\n"
  with open("PythonCodes\\GUI\\Settings.txt", "w") as file:
    file.writelines(lines)
    file.close()

#every button is defined here
nameButton = Button(home, text="Confirm", command=confirmName)
nameButton.grid(row=1, column=3, pady=0, padx=0)

micButton = Button(home, text="Confirm", command=confirmMic)
micButton.grid(row=3, column=3, pady=10)

timeButton = Button(home, text="Confirm", command=confirmTime)
timeButton.grid(row=2, column=3, pady=0, padx=0)

# Quits if jarvis quit function is called
file = open("PythonCodes\\Jarvis\\Status.txt", "rt")
quit = file.readlines()
if "quit" in quit:
  home.destroy()


# subprocess and button needed to open macro gui
# p4 = subprocess.Popen(["python", "PythonCodes/GUI/FileAddEdit.py"])
# p4.wait()

home.mainloop()