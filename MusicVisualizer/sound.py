import pyaudio
import numpy as np
import requests
from random import randint
import time
import signal
nodeIP='http://192.168.0.100/'
try:
    CHUNK = 2**11
    RATE = 44100

    Height = 16
    Width = 10

    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                frames_per_buffer=CHUNK)

    # for i in range(int(10*44100/1024)): #go for a few seconds
    #     data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    #     peak=np.average(np.abs(data))*2
    #     bars="#"*int(50*peak/2**16)*2
    #     print("%04d %05d %s"%(i,peak,bars))
    matrix = []
    for i in range(Height):
        matrix.append(['k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k'])

    colors = ['r','g','b','o','p','s','y']

    def serializeMatrix(matrix):
        w = 10
        h = 16
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
            stripString = stripString+item
        return stripString

    def addToMatrix(listBar):
        matrix.insert(0,listBar)
        if len(matrix) > Height:
            matrix.pop()
            send()
    def send():
        try:
            stringColor = serializeMatrix(matrix)
            if stringColor!="k"*160:
                requests.get(nodeIP+stringColor)
        except:
            print('done')
        
    def convertPeaks(bars):
        listBar = []
        index = randint(0, 6)
        color = colors[index]
        for c in range(Width):
            if c < len(bars):
                listBar.append(color)
            else:
                listBar.append('k')
        addToMatrix(listBar)

    while True:
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        bars="o"*int(50*peak/2**16)
        convertPeaks(bars)
        #print("%05d %s"%(peak,bars))
except KeyboardInterrupt:
    # stream.stop_stream()
    # stream.close()
    # p.terminate()
    print('close')