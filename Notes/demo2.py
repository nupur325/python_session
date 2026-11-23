from threading import Thread
from time import sleep
def task(): #don't give parameters
    for i in range(5):
        print(i)
        sleep(i)

#create thread
t = Thread(target=task)

#start thread
t.start()

#waiting for completion
t.join()