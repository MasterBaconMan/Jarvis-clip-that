import speech_recognition as sr


r = sr.Recognizer()

mytext = "Starting Up"


# Microphoen selection code, default 0. Will need to be a setting in the GUI. This is an example listing all audio related devices. Will need to be refined in the future. Temporary for testing
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")

# This is Jacob's specific number, will be replaced by a variable later
mic_index = 1



with open("PythonCodes\\Speech\\text.txt", "wt") as f:
    f.write("starting up")

# Loop infinitely for user to
# speak


while(1):    
    # quit function
    file = open("PythonCodes\\Jarvis\\Status.txt", "rt")
    quit = file.readlines()
    if "quit" in quit:
        break
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone(device_index=mic_index) as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            mytext = r.recognize_google(audio2)
            mytext = mytext.lower()

            print(mytext)
            
            # writes mytext into the text file to be read by jarvis
            with open("PythonCodes\\Speech\\text.txt", "wt") as f:
                f.write(mytext)



    except sr.RequestError as e:
        print("Could not request results")
        
    except sr.UnknownValueError:
        print("unknown error occurred")    