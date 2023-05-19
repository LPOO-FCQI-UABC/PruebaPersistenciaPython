import concurrent.futures
import threading
import time
import random

from MyClass import MyClass

if __name__ == "__main__":

    threads = list()

    for index in range(3):
        print(f"Main    : create and start thread {index}.")
        my_object = MyClass(f"My object {index}")
        x = threading.Thread(target=my_object.run)
        x.start()
        threads.append(x)

    print("Done.")
