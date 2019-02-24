import random

board = []
second_board = []
board_height = 0
board_width = 0
mines = 0
mine_location = []


def _print_welcome():
	print('BUSCAMINAS')
	print('*' * 50)
	print('Elije una dificultad:')
	print('[P]incipiante')
	print('[I]ntermedio')
	print('[M]aestro')
   

def locate_mines():
	located_mines = 0
	while(located_mines < mines):
		guess_location = [random.randint(0,board_height - 1),random.randint(0,board_width - 1)]
		if guess_location not in mine_location:
			mine_location.append(guess_location)
			located_mines += 1
			
    
def set_mines():
	global board
	setting_mine = 0
	
	while(setting_mine < mines):
		row = mine_location[setting_mine][0]
		column = mine_location[setting_mine][1]
		board[row][column] = 'X'
		
		setting_mine += 1
		
	
def set_guess():
	for row in range(board_height):
		for column in range(board_width):
			if(board[row][column]!= 'X'):
				if(row == 0):
					starts_row_in = 0
				else:
					starts_row_in = row - 1 
				
				if(column == 0):
					starts_column_in = 0
				else:
					starts_column_in = column - 1
					
				if(row == (board_height - 1)):
					ends_row_in = (board_height - 1)
				else:
					ends_row_in = row + 1
				
				if(column == (board_width - 1)):
					ends_column_in = (board_width - 1)
				else:
					ends_column_in = column + 1			
				
				guess = get_mines(starts_row_in,starts_column_in,ends_row_in,ends_column_in)
				board[row][column] = guess			
			
			
def get_mines(starts_row_in,starts_column_in,ends_row_in,ends_column_in):
	guess = 0
	row = starts_row_in
	while(row <= ends_row_in):
		column = starts_column_in
		while(column <= ends_column_in):
			if (board[row][column] == 'X'):
				guess += 1
			column += 1
		row += 1
	return guess
	
	
def set_board():
	global board
	global second_board
	
	board = [[0 for x in range(board_height)] for y in range(board_width)] 
	second_board = [[False for x in range(board_height)] for y in range(board_width)] 
	set_mines()
	set_guess()
	
	
def _print_board_completed():
	for row in range(board_height):
		for column in range(board_width):
			print(board[row][column], end=" ")
		print()

		
def _print_board_game():
	for row in range(board_height):
		for column in range(board_width):
			if(not second_board[row][column]):
				print('?', end=" ")
			else:
				print(board[row][column], end=" ")
		print()
	
	
def _print_action():
	print("Seleccione la fila: ")
	row = int(input())
	print("Seleccione la columna: ")
	column = int(input())
	return row, column
	
	
def check_cell_content(row, column):
	isAlive = True
	
	if ( board[row][column] == 'X'):
		second_board[row][column] = True
		_print_board_game()
		print("Has encontrado una mina!")
		isAlive = False
	elif ( board[row][column] > 0 ):
		second_board[row][column] = True
	elif ( board[row][column] == 0 ):
		uncover_cells(row, column)
	
	return isAlive


def uncover_cells(row, column):
	second_board[row][column] = True
	
	# UP
	# DOWN
	# LEFT
	# RIGHT
	
	
if __name__ == "__main__":
	_print_welcome()
	
	difficulty = input()
	difficulty = difficulty.upper()
	
	if difficulty == 'P':
		board_height = 9
		board_width = 9
		mines = 10
	elif difficulty == 'I':
		board_height = 16
		board_width = 16
		mines = 40
	elif difficulty == 'M':
		board_height = 16
		board_width = 30
		mines = 99
	else:
		print('Acción no valida')
		exit()

	locate_mines()

	set_board()
	isAlive = True
	
	_print_board_completed()
	print(mine_location)
	
	while(isAlive):
		_print_board_game()
		row, column = _print_action()
		
		isAlive = check_cell_content(row - 1, column - 1)
		
	
	