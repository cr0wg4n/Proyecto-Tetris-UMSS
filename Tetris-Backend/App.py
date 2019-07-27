import time
from GTetris import TetrisApp
import requests
from multiprocessing import Process

App = TetrisApp()
FPS = 1
last_time = time.time()
height = 16
width = 10
urlServer = 'http://localhost:3000/'
nodeIP = 'http://192.168.0.100/'
#urlServer = 'http://chameleoncodesoft.com:3000/'

def setColors(color):
    if color == 0:
        return 'k'
    elif color == 1:
        return 'r'            
    elif color == 2:
        return 'g'      
    elif color == 3:
        return 'b'
    elif color == 4:
        return 'o'
    elif color == 5:
        return 'y'
    elif color == 6:
        return 'p'    
    elif color == 7:
        return 's'

def sendColorsString(stringColor):
    try:
        requests.get(nodeIP+stringColor)
    except:
        print('done!')

def serializeMatrix(matrix):
    print(matrix)
    w = width
    h = height
    invertFlag = False
    strip = []
    i = w-1
    while i>=0:
        j = h-1
        while j>=0:
            if invertFlag == False:
                strip.append(matrix[j][i])
            else:
                strip.append(matrix[h-1-j][i])
            j = j-1
        invertFlag = not invertFlag
        i = i-1
    stripString = ''
    for item in strip:
        stripString = stripString+setColors(item)
    #print(stripString)
    sendColorsString(stripString)

def changeStatus():
    r = requests.get(urlServer)
    data = r.json()
    res = []
    if data['right'] == 1:
        res = App.run('RIGHT')
    elif data['left'] == 1:
        res = App.run('LEFT')
    elif data['down'] == 1:
        res = App.run('DOWN')
        res = App.run('DOWN')        
    elif data['move'] == 1:
        res = App.run('UP')
    else:
        res = App.run('DOWN')
    return res

while True:
    lista = changeStatus()
    matrix = []
    counter = 0
    for cy, row in enumerate(lista):
        if counter < height:
            matrix.append(row)
        counter = counter + 1
    serializeMatrix(matrix)
    # new_time = time.time()
    # sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
    # if sleep_time > 0:
    #     time.sleep(sleep_time)
    # last_time = new_time
    time.sleep(0.30)
    