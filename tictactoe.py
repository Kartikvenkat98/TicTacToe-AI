import random

def drawBoard(board):

	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

	print('-----------')

	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')

	print('-----------')

	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')

	print '\n'

	
def inputLetter():

	letter = ''
	print("Do you want to be 'X' or 'O' ??")

	while not (letter == 'X' or letter == 'O'):
		
		letter = input()

		if letter == 'X':

			return ['X', 'O']
		
		elif letter == 'O':

			return ['O', 'X']

		else:

			print 'Please check the character entered !!'
			print "Do you want to be 'X' or 'O' ??"



def toss():

	if random.randint(0, 1) == 0:

		return 'computer'

	else:

		return 'player'
		

def isSpaceFree(board, move):

	return board[move] == ' '


def getPlayerMove(board):

	move = ' '

	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

		print('What is your next move? (1-9)')
		move = str(input())

	return int(move)


def makeMove(board, letter, move):

	board[move] = letter



print('\n Welcome to Tic Tac Toe !!! \n')

board = [' '] * 10 
#drawboard(board)

playerLetter, computerLetter = inputLetter()
#print 'You are ' + playerLetter + '\n'
#print 'Computer is ' + computerLetter + '\n'


turn = toss()

print 'The ' + turn + ' will go first.\n'

while True:

	if turn == 'player':

		drawBoard(board)
		move = getPlayerMove(board)
		makeMove(board, playerLetter, move)
		turn = 'computer'

	else:

		drawBoard(board)
		turn = 'player'
