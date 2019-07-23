#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys, pygame
import requests
from random import randrange as rand

urlServer = 'http://localhost:3000/'
nodeIP = 'http://192.168.0.100/'
#urlServer = 'http://chameleoncodesoft.com:3000/'
# The configuration
config = {
	'cell_size':	40,
	'cols':		10,
	'rows':		16,
	'delay':	750,
	'maxfps':	30
}

colors = [
(0,   0,   0  ), # Black
(255, 0,   0  ), # Red
(0,   255, 0  ), # Green
(0,   0,   255), # Blue
(255, 120, 0  ), # Orange
(255, 255, 0  ), # Yellow
(180, 0,   255), # Purple
(0,   220, 220)  # Sky
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
			mat1[cy+off_y-1	][cx+off_x] += val
	return mat1

def new_board():
	board = [ [ 0 for x in range(config['cols']) ]
			for y in range(config['rows']) ]
	board += [[ 1 for x in range(config['cols'])]]
	return board

class TetrisApp(object):
	def __init__(self):
		pygame.init()
		pygame.key.set_repeat(250,25)
		self.width = config['cell_size']*config['cols']
		self.height = config['cell_size']*config['rows']

		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.event.set_blocked(pygame.MOUSEMOTION) # We do not need
		                                             # mouse movement
		                                             # events, so we
		                                             # block them.
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
		for i, line in enumerate(msg.splitlines()):
			msg_image =  pygame.font.Font(
				pygame.font.get_default_font(), 12).render(
					line, False, (255,255,255), (0,0,0))

			msgim_center_x, msgim_center_y = msg_image.get_size()
			msgim_center_x //= 2
			msgim_center_y //= 2

			self.screen.blit(msg_image, (
			  self.width // 2-msgim_center_x,
			  self.height // 2-msgim_center_y+i*22))
	def setColors(self,color):
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

	def sendColorsString(self,stringColor):
		try:
			if(len(stringColor)==160):
				requests.get(nodeIP+stringColor)
			else:
				print('string extra!')
		except Exception as error:
			print(error)

	def serializeMatrix(self,matrix):
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
			stripString = stripString+self.setColors(item)
		self.sendColorsString(stripString)

	def sendMatrix(self,matrix):
		newMatrix = []
		counter = 0
		for cy, row in enumerate(matrix):
			if counter < config['rows']:
				newMatrix.append(row)
			counter = counter + 1
		self.serializeMatrix(newMatrix)

	def draw_matrix(self, matrix, offset):
		off_x, off_y  = offset
		for y, row in enumerate(matrix):
			for x, val in enumerate(row):
				if val:
					pygame.draw.rect(
						self.screen,
						colors[val],
						pygame.Rect(
							(off_x+x) *
							  config['cell_size'],
							(off_y+y) *
							  config['cell_size'], 
							config['cell_size'],
							config['cell_size']),0)

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
		pygame.display.update()
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

	def changeStatus(self,data):
		key_actions = {
			'ESCAPE':	self.quit,
			'LEFT':		lambda:self.move(-1),
			'RIGHT':	lambda:self.move(+1),
			'DOWN':		self.drop,
			'UP':		self.rotate_stone,
			'p':		self.toggle_pause,
			'SPACE':	self.start_game
		}
		if data['right'] == 1:
			key_actions['RIGHT']()
		elif data['left'] == 1:
			key_actions['LEFT']()
		elif data['down'] == 1:
			key_actions['DOWN']()
		elif data['move'] == 1:
			key_actions['UP']()
	
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

	def run(self):
		key_actions = {
			'ESCAPE':	self.quit,
			'LEFT':		lambda:self.move(-1),
			'RIGHT':	lambda:self.move(+1),
			'DOWN':		self.drop,
			'UP':		self.rotate_stone,
			'p':		self.toggle_pause,
			'SPACE':	self.start_game
		}

		self.gameover = False
		self.paused = False

		pygame.time.set_timer(pygame.USEREVENT+1, config['delay'])
		dont_burn_my_cpu = pygame.time.Clock()
		while 1:
			self.screen.fill((0,0,0))
			if self.gameover:
				self.center_msg("""Game Over!
Press space to continue""")
			else:
				if self.paused:
					self.center_msg("Paused")
				else:
					self.draw_matrix(self.board, (0,0))
					self.draw_matrix(self.stone,
					                 (self.stone_x,
					                  self.stone_y))
					matrixUnida = self.unirMatrices(self.board, self.stone, self.stone_x, self.stone_y)
					self.sendMatrix(matrixUnida)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.USEREVENT+1:
					self.drop()
				elif event.type == pygame.QUIT:
					self.quit()
				elif event.type == pygame.KEYDOWN:
					for key in key_actions:
						if event.key == eval("pygame.K_"
						+key):
							key_actions[key]()

			dont_burn_my_cpu.tick(config['maxfps'])
			r = requests.get(urlServer)
			data = r.json()
			self.changeStatus(data)

if __name__ == '__main__':
	App = TetrisApp()
	App.run()
