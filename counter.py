import main

def on():
	startC = time.time()
	while(True):
		appsList()
		
		time.sleep(1 - time.time()%1)

f = open("tracking.txt","a")