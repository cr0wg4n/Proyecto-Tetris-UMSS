import time
from GTetris import TetrisApp

App = TetrisApp()

FPS = 1
last_time = time.time()
height = 16
width = 10
while True:
    lista = App.run("DOWN")
    matrix = []
    counter = 0
    for cy, row in enumerate(lista):
        if counter < 16:
            matrix.append(row)
        counter = counter + 1
    print(matrix)
    new_time = time.time()
    sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
    if sleep_time > 0:
        time.sleep(sleep_time)
    last_time = new_time