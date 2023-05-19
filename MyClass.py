import time
import random

class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass: {self.name}"

    def run(self):
        print(f"Thread {self.name}: starting")
        max = random.randint(1, 10)
        for i in range(0, max):
            print(f"Thread {self.name}: working {i}/{max}")
            time.sleep(1)
        print(f"Thread {self.name}: finishing")
