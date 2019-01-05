from pypresence import Presence, Activity
import time, os, re


def getpid(process_name):
    return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]

while True:

    pid = re.compile(r"[^a-zA-Z0-9-]").sub("", str(getpid('ForzaHorizon4.exe')))

    if pid != '':

        client_id = "530434490909327360"
        RPC = Presence(client_id)
        RPC.connect()

        ac = Activity(RPC, pid=int(pid), large_image="main")

        ac.start = int(time.time())
        print("Sucessfully Launched the RPC :)")

        while pid != '':
            pid = re.compile(r"[^a-zA-Z0-9-]").sub("", str(getpid('ForzaHorizon4.exe')))
            
            time.sleep(15)
        RPC.close()

    else:
        print("Forza Horizon 4 isn't running...")
    
    time.sleep(15)

    