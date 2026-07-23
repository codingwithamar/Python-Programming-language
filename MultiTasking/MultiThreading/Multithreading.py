# =============================================================================
# Author  : codingwithamar@gmail.com
# File    : Multithreading.py
# Path    : Python-Programming-Language\MultiTasking\MultiThreading\Multithreading.py
# Subject : MultiThreading
# Description : using start(), join() explain multithreading
# =============================================================================

import threading

def fun():
    print("Hello from\n", threading.current_thread().name)

def main():
    t1 = threading.Thread(target=fun)
    t2 = threading.Thread(target=fun)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

