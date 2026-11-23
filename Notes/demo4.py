import threading
import time
def square(num):
    print(f"Sqaure: {num*num}")
    time.sleep(1)
def cube(num):
     print(f"Cube: {num*num*num}")
     time.sleep(2)
t1 = threading.Thread(target=square,args=(4,)) #write "4," so it takes arg as tuple 
t2 = threading.Thread(target=cube,args=(4,))

t1.start()
t2.start()
t1.join()
t2.join()
print("Done")

# when number of arguments are not known use args