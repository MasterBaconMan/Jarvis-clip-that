import time
def readfile():
    file = open("PythonCodes\\Speech\\text.txt", "rt")
    return file.readlines()

print(readfile())

while(1):
    print(readfile())