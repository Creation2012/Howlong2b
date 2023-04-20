import subprocess
import time

def appsList():
    apps = set()
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    proc.stdout.readline()
    proc.stdout.readline()
    proc.stdout.readline()

    for line in proc.stdout:
        if not line.decode()[0].isspace():
            apps.update(line.decode().rstrip())

    return apps

#mainTracking()
while True:
        time.sleep(2-time.time()%2)
        print(appsList()) 
