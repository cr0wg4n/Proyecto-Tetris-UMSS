import requests
from random import randint
import time

dictionary = ['r','g','b','k']

def colorize(n):
    res = ''
    for i in range(160):
        index = randint(0, 3)
        res = res+dictionary[index]
    return res
        
while True:
    randomColor = colorize (10)
    try:
        requests.get('http://192.168.1.5/'+randomColor)
    except:
        print('error')
    time.sleep(0.5)
    print (randomColor)