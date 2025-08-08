import subprocess
import clip
import pyautogui


# Function to read from speech to text file
def readfile():
    file = open("PythonCodes\\Speech\\text.txt", "rt")
    return file.readlines()



# Function to read name from settings file

file = open("PythonCodes\\GUI\\Settings.txt")
settings = file.readlines()
name = str(settings[0])
name = name.lower()
print(settings, name)
file.close()

def stop():
    # stop function placeholder
    print("STOP!")


# variable setup
wordlist = []
previous = ""
name = "jarvis"

while(1):
    # Prepares the words from the textfile into a useable format.
    words = str(readfile())
    words = words.replace("]", "")
    words = words.replace("[", "")
    words = words.replace("'", "")
    words.split(" ")
    #print(words)

    #resets the wordlist if more than 10 words are stored
    if len(wordlist) > 10:
        wordlist = []

    # name = nameSetting()
    
    # this if statement runs if jarvis is in words, in the wordlist, and there is a new message
    if ((words.find(name) >= 0) or name in wordlist) and words != previous:
        
        # adds words to the wordlist
        wordlist = wordlist + (words.split(" "))
        

        # Maybe turn on a light on raspberry pi here? Like when jarvs' name is called

        # Testing code
        if "quit" in wordlist:
            print("quit") 
            with open("PythonCodes\\Jarvis\\Status.txt", "wt") as f:
                f.write("quit")
            break

        
        # Code for start and stop recording, runs start and stop recording function in clip file
        try:
            if ("recording") in wordlist:
                if "stop" in wordlist:
                    print("Stop Recording Jarvis file")
                    clip.stop_recording()
                    wordlist = []
                elif "start" in wordlist:
                    print("Start Recording Jarvis file")
                    clip.start_recording()
                    wordlist = []
        except:
            print("Incorrect Password")




        # Runs clipping function in clip python file
        try:
            if "clip" in wordlist:
                print("clip")
                clip.clip()
                wordlist = []
        except:
            print("Incorrect Password")
        

        # Media control functions
        if "play" in wordlist:
            pyautogui.press('playpause')
            wordlist = []

        if "pause" in wordlist:
            pyautogui.press('playpause')
            wordlist = []

        if "skip" in wordlist:
            pyautogui.press('nexttrack')
            wordlist = []

        # Volume control function
        if "volume" in wordlist:
            if "increase" in wordlist:
                loop = 5
                for word in wordlist:
                    if word.isdigit():
                        loop = word
                for i in range(loop):
                    pyautogui.press('volumeup')
                wordlist = []

            if "decrease" in wordlist:
                loop = 5
                for word in wordlist:
                    if word.isdigit():
                        loop = word
                for i in range(loop):
                    pyautogui.press('volumedown')
                wordlist = []


        #for testing
        print(wordlist)
    



    #updates previous message KEEP AT END OF WHILE LOOP!
    previous = words