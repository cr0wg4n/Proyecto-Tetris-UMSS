import time
from GTetris import TetrisApp

App = TetrisApp()

FPS = 1
last_time = time.time()
while True:
    lista = App.run("DOWN")
    for cy, row in enumerate(lista):
        print(row)
    new_time = time.time()
    sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
    if sleep_time > 0:
        time.sleep(sleep_time)
    last_time = new_time