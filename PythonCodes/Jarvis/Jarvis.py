import subprocess
import clip
import pyautogui


# Function to read from speech to text file
def readfile():
    file = open("PythonCodes\\Speech\\text.txt", "rt")
    return file.readlines()

# Converts a string into an integer
def text2int(numword):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if ((numword in units) or (numword in tens)) == False:
        try:
             numword = int(numword)
        except:
            pass
        if (isinstance(numword, int)):
            return numword
    else:
        if numword in tens:
            for ten in enumerate(tens):
                if ten[1] == numword:
                    return int((ten[0]*10))
        if numword in units:
            for ones in enumerate(units):
                if ones[1] == numword:
                    return int((ones[0]))

# Gets the sum of a list
def wordlistAddition(wordlist):
    addList = []
    value = 0
    for word in wordlist:
        if (text2int(word) != None):
            addList.append(text2int(word))

    if len(addList) > 0:
        for num in addList:
            value = value + num
    
    if len(addList) == 0:
        value = 6
    return value


# Function to read name from settings file

file = open("PythonCodes\\GUI\\Settings.txt")
settings = file.readlines()
name = str(settings[0])
name = name.lower()
# print(settings, name)
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
            print("Incorrect Password or OBS not running")




        # Runs clipping function in clip python file
        try:
            if "clip" in wordlist:
                print("clip")
                clip.clip()
                wordlist = []
        except:
            print("Incorrect Password or OBS not running")
        

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
                
                loop = int(wordlistAddition(wordlist)/2)

                print(loop)

                for i in range(loop):
                    pyautogui.press('volumeup')
                print(f"increasing volume by {loop*2}")
                wordlist = []

            if "decrease" in wordlist:
                
                loop = int(wordlistAddition(wordlist)/2)

                for i in range(loop):
                    pyautogui.press('volumedown')
                print(f"decreasing volume by {loop * 2}")
                wordlist = []


        #for testing
        print(wordlist)
    



    #updates previous message KEEP AT END OF WHILE LOOP!
    previous = words