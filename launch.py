import subprocess

with open("PythonCodes\\Jarvis\\Status.txt", "wt") as f:
    lines = ["start", "none"]
    f.writelines(lines)

# installs packages if not already installed
install_obs = subprocess.run(["pip","install","obs-websocket-py"])
install_audio = subprocess.run(["pip","install","pyaudio"])
install_pygame = subprocess.run(["pip", "install", "pygame"])
install_pyautogui = subprocess.run(["pip", "install", "pyautogui"])
install_SpeechRecognition = subprocess.run(["pip", "install", "SpeechRecognition"])

p1 = subprocess.Popen(["python",  "PythonCodes/Speech/STT.py"])
p2 = subprocess.Popen(["python", "PythonCodes/Jarvis/Jarvis.py"])
p3 = subprocess.Popen(["python", "PythonCodes/GUI/GUI.py"])


p1.wait()
p2.wait()
p3.wait()