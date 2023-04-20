from sys import stdin
import time
import subprocess
from threading import Thread
from datetime import date, datetime

def readTrackingName():
    stock = set()
    f = open("tracking.txt","r")
    for i in f:
        #TODO protect from empty file
        x=(i.split("{")[1]).split("}")[0]
        stock.add(x.rstrip())

    f.close()

    return stock

def appsList():
    apps = set()
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select ProcessName'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    proc.stdout.readline()
    proc.stdout.readline()
    proc.stdout.readline()

    for line in proc.stdout:
        if not line.decode()[0].isspace():
            apps.add(line.decode().rstrip())

    return apps

def stockConstruction():
    stock = set()
    f = open("dump.txt","r")
    for i in f:
        stock.add(i.rstrip())

    stock.update(readTrackingName())

    f.close()

    return stock

def appsTracking(apps, stock):
    f = open("dump.txt","a")
    t = open("tracking.txt","a")
    for i in apps:
        print("Collect info of this app: "+i+"? (Y/y - yes, N/n = no)")
        x = input()
        if x == 'y' or x == 'Y':
            print("How you want to display app? (default is process name)")
            x = input()
            if x:
                t.write(x+" {"+i+"}"+" Added: "+date.today().strftime("%d/%m/%Y")+"\n")
            else:
                t.write("{"+i+"}"+" Added: "+date.today().strftime("%d/%m/%Y")+"\n")
        else:
            f.write(i+"\n")
    f.close()
    t.close()

def mainTracking():
    apps = appsList()
    stock = stockConstruction()
    apps = (apps.difference(stock))
    appsTracking(apps, stock)

def mainCounter():
    dic = {}
    while True:
        apps = appsList()
        processName = readTrackingName()
        x = (apps.intersection(processName))

        if not len(dic):
            for i in x:
                dic.update({i: datetime.now().time()})
        
        if not len(x):
            break

        print(x)

if __name__ == "__main__":
    #mainTracking()
    x = datetime.now().time()
    x = str(x)
    print(x)
    x = datetime.strptime(x,"%H:%M:%S")
    #print(datetime.strptime(datetime.now().itime(),"%H:%M"))
    #print(datetime.now().time()+1)
    #Thread(group=None, target=mainCounter(), name="howlong2b-c").start()
