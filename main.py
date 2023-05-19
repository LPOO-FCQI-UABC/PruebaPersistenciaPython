import concurrent.futures
import threading
import time
import random

from MyClass import MyClass


def pepito(name):
    print(f"Thread {name}: starting")
    max = random.randint(1, 10)
    for i in range(0, max):
        print(f"Thread {name}: working {i}/{max}")
        time.sleep(2)
    print(f"Thread {name}: finishing")

if __name__ == "__main__":

    threads = list()

    for index in range(3):
        print(f"Main    : create and start thread {index}.")
        my_object = MyClass(f"My object {index}")
        x = threading.Thread(target=my_object.run)
        x.start()
        threads.append(x)

    print("Done.")
