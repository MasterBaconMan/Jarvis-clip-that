# Jarvis-clip-that

## Introduction
This is an OBS and macro tool.

To use this tool, you must have OBS installed. To download OBS, go here: <https://obsproject.com/download> .

To start the program, run the file named "run.bat".

## GUI Navigation:

### This is the GUI:

![alt text](https://github.com/MasterBaconMan/audio-air-fryer/blob/main/images%20for%20README/GUI.PNG)

The "Input Name" is the name you use to excecute commands. By default it is called "Jarvis"

The "WebSocket Server password" is not required but will be explained later.

The "Select Microphone" is a dropdown where you can choose your input microphone device

## Commandands:

### To use commands, say the name that you input (default jarvis) and then the command into your selected audio device
"Clip" - Activates replay buffer or saves replay buffer in OBS (OBS must be running)

"Start Recording" - Starts an OBS recording (OBS must be running)

"Stop Reocording" - Stops an OBS recording (OBS must be running)

"Quit" - Quits the program

"Increase Volume" - Raises system volume (You can specify a number)

"Decrease Volume" - Lowers system volume (You can specify a number)

"Play" - Pauses/Unpauses media last selected

"Pause" - Pauses/Unpauses media last selected

"Skip" - Skips media selected

### Macros:

To use a macro, click on the "Macro add/edit" button.

![alt text](https://github.com/MasterBaconMan/Jarvis-clip-that/blob/main/images%20for%20README/macro.PNG)

This will open up a seperate window where you can add a name to the macro (This is the name you will say out loud to excecute the command for the macro),
and the "..." where you can add the keys to be pressed in the macro. Clicl the "save" button after typing in your desired keys.

![alt text](https://github.com/MasterBaconMan/Jarvis-clip-that/blob/main/images%20for%20README/macro%20example1.PNG)

![alt text](https://github.com/MasterBaconMan/Jarvis-clip-that/blob/main/images%20for%20README/macro%20example2.PNG)

You can press the "run macro" button to test your macro


Currently custom macros do not save between instances, but that is a feature that will be worked on later.


## OBS Setup:
To use the commands with OBS, some settings must be enabled first.

### Step one, navigate to "Tools" and "WebSocket Server Settings".

![alt text](https://github.com/MasterBaconMan/audio-air-fryer/blob/main/images%20for%20README/step%201.PNG "Step 1")

### Step two, check the box for "Enable WebSocket Server". Optionally you can check or uncheck "Enable Authentication" if you want to have a password.

![alt text](https://github.com/MasterBaconMan/audio-air-fryer/blob/main/images%20for%20README/Step%202.PNG "Step 2")

### Step three, in your "Controls" tab, navigate to settings.

![alt text](https://github.com/MasterBaconMan/audio-air-fryer/blob/main/images%20for%20README/Step%203.PNG "Step 3")

### Step four, navigate to the "Output" tab in settings.

![alt text](https://github.com/MasterBaconMan/audio-air-fryer/blob/main/images%20for%20README/step%204.PNG "Step 4")

### Step five, scroll down and check the box that says "Replay Buffer".

![alt text](https://github.com/MasterBaconMan/audio-air-fryer/blob/main/images%20for%20README/Step%206.PNG "Step 5")

Video settings are altered in OBS.

