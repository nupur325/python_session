from threading import Thread
def task(): #don't give parameters
    print("Thread is running")

#create thread
t = Thread(target=task) #if parameter is given the in auto starts execution then whats the use of creating thread

#start thread
t.start()

#waiting for completion
t.join()

print("Main program ends")