import threading

def display():
    for i in range(1, 6):
        print(threading.current_thread().name, "->", i)

t1 = threading.Thread(target=display)
t2 = threading.Thread(target=display)

t1.start()
t2.start()

t1.join()
t2.join()
