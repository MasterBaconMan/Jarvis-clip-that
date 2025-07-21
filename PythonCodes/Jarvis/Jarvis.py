


# Function to read from speech to text file
def readfile():
    file = open("PythonCodes\\Speech\\text.txt", "rt")
    return file.readlines()


def stop():
    # stop function placeholder
    print("STOP!")


# variable setup
wordlist = []
previous = ""


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

    # this if statement runs if jarvis is in words, in the wordlist, and there is a new message
    if ((words.find("jarvis") >= 0) or "jarvis" in wordlist) and words != previous:
        
        # adds words to the wordlist
        wordlist = wordlist + (words.split(" "))
        

        # Maybe turn on a light on raspberry pi here? Like when jarvs' name is called

        # Testing code
        if "quit" in wordlist:
            print("quit") 
            with open("PythonCodes\\Jarvis\\Status.txt", "wt") as f:
                f.write("quit")
            break


        #for testing
        print(wordlist)
    



    #updates previous message KEEP AT END OF WHILE LOOP!
    previous = words