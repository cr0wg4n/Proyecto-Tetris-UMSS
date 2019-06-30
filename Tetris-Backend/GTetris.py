#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from random import randrange as rand

# The configuration
config = {
    'cell_size':    40,
    'cols':     10,
    'rows':     16,
    'delay':    750,
    'maxfps':   30
}

colors = [
(0,   0,   0  ),
(255, 0,   0  ),
(0,   150, 0  ),
(0,   0,   255),
(255, 120, 0  ),
(255, 255, 0  ),
(180, 0,   255),
(0,   220, 220)
]

# Define the shapes of the single parts
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

def rotate_clockwise(shape):
    return [ [ shape[y][x]
            for y in range(len(shape)) ]
        for x in range(len(shape[0]) - 1, -1, -1) ]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for cy, row in enumerate(shape):
        for cx, cell in enumerate(row):
            try:
                if cell and board[ cy + off_y ][ cx + off_x ]:
                    return True
            except IndexError:
                return True
    return False

def remove_row(board, row):
    del board[row]
    return [[0 for i in range(config['cols'])]] + board

def join_matrixes(mat1, mat2, mat2_off):
    off_x, off_y = mat2_off
    for cy, row in enumerate(mat2):
        for cx, val in enumerate(row):
            mat1[cy+off_y-1 ][cx+off_x] += val
    return mat1

def new_board():
    board = [ [ 0 for x in range(config['cols']) ]
            for y in range(config['rows']) ]
    board += [[ 1 for x in range(config['cols'])]]
    return board

class TetrisApp(object):
    def __init__(self):
        self.width = config['cell_size']*config['cols']
        self.height = config['cell_size']*config['rows']

        self.gameover = False
        self.paused = False
        self.init_game()

    def new_stone(self):
        self.stone = tetris_shapes[rand(len(tetris_shapes))]
        self.stone_x = int(config['cols'] / 2 - len(self.stone[0])/2)
        self.stone_y = 0

        if check_collision(self.board,
                           self.stone,
                           (self.stone_x, self.stone_y)):
            self.gameover = True

    def init_game(self):
        self.board = new_board()
        self.new_stone()

    def center_msg(self, msg):
        print(msg);

    def draw_matrix(self, matrix, offset):
        off_x, off_y  = offset
        for y, row in enumerate(matrix):
            print(row)

    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > config['cols'] - len(self.stone[0]):
                new_x = config['cols'] - len(self.stone[0])
            if not check_collision(self.board,
                                   self.stone,
                                   (new_x, self.stone_y)):
                self.stone_x = new_x

    def quit(self):
        self.center_msg("Exiting...")
        sys.exit()

    def drop(self):
        if not self.gameover and not self.paused:
            self.stone_y += 1
            if check_collision(self.board,
                               self.stone,
                               (self.stone_x, self.stone_y)):
                self.board = join_matrixes(
                  self.board,
                  self.stone,
                  (self.stone_x, self.stone_y))
                self.new_stone()
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(
                              self.board, i)
                            break
                    else:
                        break

    def rotate_stone(self):
        if not self.gameover and not self.paused:
            new_stone = rotate_clockwise(self.stone)
            if not check_collision(self.board,
                                   new_stone,
                                   (self.stone_x, self.stone_y)):
                self.stone = new_stone

    def toggle_pause(self):
        self.paused = not self.paused

    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False

    def run(self, direccion):
        matrixUnida = []
        key_actions = {
            'ESCAPE':   self.quit,
            'LEFT':     lambda:self.move(-1),
            'RIGHT':    lambda:self.move(+1),
            'DOWN':     self.drop,
            'UP':       self.rotate_stone,
            'p':        self.toggle_pause,
            'SPACE':    self.start_game
        }
        if self.gameover:
            self.center_msg("""Game Over! Press space to continue""")
        else:
            if self.paused:
                self.center_msg("Paused")
            else:
                #print(self.stone_x, end=" ")
                #print(self.stone_y)
                #self.draw_matrix(self.board, (0,0))
                #self.draw_matrix(self.stone,
                #                 (self.stone_x,
                #                  self.stone_y))
                matrixUnida = self.unirMatrices(self.board, self.stone, self.stone_x, self.stone_y)
        for key in key_actions:
            if key == direccion:
                key_actions[key]()
        return matrixUnida

    def unirMatrices(self, matrix, figura, posX, posY):        
        respuesta = [ [ 0 for x in range(config['cols']) ]
                for y in range(config['rows']) ]
        respuesta += [[ 1 for x in range(config['cols'])]]
        for cy, row in enumerate(matrix):
            for cx, val in enumerate(row):
                respuesta[cy][cx] = matrix[cy][cx]
        for cy, row in enumerate(figura):
            for cx, val in enumerate(row):
                respuesta[cy+posY-1 ][cx+posX] += val 
        return respuesta

        


