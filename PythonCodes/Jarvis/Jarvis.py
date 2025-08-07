import subprocess
import clip


# Function to read from speech to text file
def readfile():
    file = open("PythonCodes\\Speech\\text.txt", "rt")
    return file.readlines()



# Function to read name from settings file
def nameSetting():
    file = open("PythonCodes\\GUI\\Settings.txt")
    settings = file.readlines()
    name = settings[0]
    name = name.lower()
    return name

def stop():
    # stop function placeholder
    print("STOP!")


# variable setup
wordlist = []
previous = ""
name = ""

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

    # Changes the name in the loop if name is updated
    name = nameSetting()
    
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
        if ("recording") in wordlist:
            if "stop" in wordlist:
                print("Stop Recording Jarvis file")
                clip.stop_recording()
                wordlist = []
            elif "start" in wordlist:
                print("Start Recording Jarvis file")
                clip.start_recording()
                wordlist = []




        # Runs clipping function in clip python file
        if "clip" in wordlist:
            print("clip")
            clip.clip()
            wordlist = []
        



        #for testing
        print(wordlist)
    



    #updates previous message KEEP AT END OF WHILE LOOP!
    previous = words