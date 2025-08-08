from obswebsocket import obsws, requests

global HOST
HOST = "localhost"
global PORT
PORT = 4455

def passwordSetting():
    file = open("PythonCodes\\GUI\\Settings.txt")
    settings = file.readlines()
    password = settings[1]
    password = password.replace("\n", "")
    return password

global PASSWORD
# This can be changed by the user
PASSWORD = passwordSetting()


# Cliptime has to be changed in OBS
cliptime = 45


def clip():
    ws = obsws(HOST, PORT, PASSWORD)
    ws.connect()

    # Formats request to see if replay buffer is running
    request = str(ws.call(requests.GetReplayBufferStatus()))
    request = request.replace("})>", "")
    request = request.rsplit(" ")


    # Starts replay buffer if none is running, else records clip
    if "False" in request:
        ws.call(requests.StartReplayBuffer())
        print("No clip saved, starting buffer")
    else:
        ws.call(requests.SaveReplayBuffer())
        print("Saving Clip")
    ws.disconnect()



def start_recording():
    start = obsws(HOST, PORT, PASSWORD)
    start.connect()

    start.call(requests.StartRecord())
    print("recording started")

    start.disconnect()



def stop_recording():
    stop = obsws(HOST, PORT, PASSWORD)
    stop.connect()

    stop.call(requests.StopRecord())
    print("recording stopped")

    stop.disconnect()


