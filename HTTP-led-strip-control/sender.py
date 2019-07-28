import requests
from random import randint
import time

dictionary = ['r','g','b','k','o','p','s','y']

def colorize(n):
    res = ''
    for i in range(160):
        index = randint(0, 7)
        res = res+dictionary[index]
    return res
        
while True:
    randomColor = colorize (10)
    try:
        requests.get('http://192.168.0.100/'+randomColor)
    except:
        print('error')
    time.sleep(0.5)
    print (randomColor)