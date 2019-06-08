import numpy as np
from ListShapes import ListShapes

class Tetris:
    
  def __init__(self, _rows, _cols, _scale):
    self.rows = _rows
    self.cols = _cols
    self.shape = []
    self.xShape = 0
    self.yShape = 0
    self.initGame()

  def initGame(self):
    self.listShapes = ListShapes("List")
    self.matrix = np.zeros((self.rows, self.cols))
    self.key_actions = {
        'LEFT':     lambda:self.moveColumns(-1),
        'RIGHT':    lambda:self.moveColumns(+1),
        'DOWN':     lambda:self.moveShape()
    }

  def drawMatrix(self):
    board = np.zeros((self.rows, self.cols))
    for y, row in enumerate(self.matrix):
        for x, val in enumerate(row):
            board[y][x] = val
    for y, row in enumerate(self.shape):
        for x, val in enumerate(row):
            board[y][x] = val
    return board

  def newShape(self):
    self.shape = self.listShapes.getRandomShape()
    self.xShape = int(self.cols / 2 - len(self.shape[0])/2)
    self.yShape = 0

  def play(self, direction):
    for key in self.key_actions:
        if direction == key:
            self.key_actions[key]()

  def moveShape(self):
    self.yShape = self.yShape + 1;

  def moveColumns(self, col):
    print("col ", col)