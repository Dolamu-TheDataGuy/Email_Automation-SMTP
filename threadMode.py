import threading
import time
import os

print("Start of Program!")


def take_nap():
    time.sleep(5)
    print("Wake Up!")


thread_obj = threading.Thread(target=take_nap)
thread_obj.start()

print("End of Program")
