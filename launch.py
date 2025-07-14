import subprocess


p1 = subprocess.Popen(["python",  "PythonCodes/Speech/STT.py"])
p2 = subprocess.Popen(["python", "PythonCodes/Jarvis/Jarvis.py"])

p1.wait()
p2.wait()