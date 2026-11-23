from threading import Thread
from time import sleep
def numbers():
    for i in range(1,6):
        print(i)
        sleep(1)
def alphabets():
    for ch in ['A','B','C','D','E']:
        print(ch)
        sleep(2)
t1 = Thread(target=numbers)
t2 = Thread(target=alphabets)
t1.start()
t2.start()

t1.join()
t2.join()

print("Finished")