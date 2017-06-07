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
		#print move

	return int(move)


def makeMove(board, letter, move):

	board[move] = letter


def isWinner(board, letter):

	return ((board[1] == letter and board[2] == letter and board[3] == letter) or

	(board[4] == letter and board[5] == letter and board[6] == letter) or

	(board[7] == letter and board[8] == letter and board[9] == letter) or

	(board[1] == letter and board[4] == letter and board[7] == letter) or

	(board[2] == letter and board[5] == letter and board[8] == letter) or

	(board[3] == letter and board[6] == letter and board[9] == letter) or

	(board[3] == letter and board[5] == letter and board[7] == letter) or

	(board[1] == letter and board[5] == letter and board[9] == letter))


def isBoardFull(board):

	for i in range(1, 10):

		if isSpaceFree(board, i):

			return False

	return True


def getDuplicate(board):

	duplicate = []

	for i in board:

		duplicate.append(i)

	return duplicate



def choose(board, list):

	moves = []

	for i in list:

		if isSpaceFree(board, i):

			#print i
			moves.append(i)



	if len(moves) != 0:
		return random.choice(moves)

	else:

		return None



def getComputerMove(board, computerLetter):


	if computerLetter == 'X':

		playerLetter = 'O'

	else:

		playerLetter = 'X'

	#print playerLetter


	for i in range(1, 10):

		copy = getDuplicate(board)

		if isSpaceFree(copy, i):

			makeMove(copy, computerLetter, i)

			if isWinner(copy, computerLetter):

				#print i
				return i


	for i in range(1, 10):

		copy = getDuplicate(board)

		if isSpaceFree(copy, i):

			makeMove(copy, playerLetter, i)

			if isWinner(copy, playerLetter):

				#print i
				return i


	move = choose(board, [1, 3, 7, 9])

	if move != None:

		return move


	if isSpaceFree(board, 5):

		return 5

	return choose(board, [2, 4, 6, 8])




print('\n Welcome to Tic Tac Toe !!! \n')

board = [' '] * 10
#drawboard(board)

playerLetter, computerLetter = inputLetter()
#print 'You are ' + playerLetter + '\n'
#print 'Computer is ' + computerLetter + '\n'


turn = toss()

print 'The ' + turn + ' will go first.\n'

isPlaying = True

while True:

	while isPlaying:

		if turn == 'player':

			drawBoard(board)
			move = getPlayerMove(board)
			makeMove(board, playerLetter, move)

			if isWinner(board, playerLetter):

				drawBoard(board)
				print('Hooray! You have won the game!')
				isPlaying = False

			else:

				if isBoardFull(board):

					drawBoard(board)
					print('The game is a tie!')
					isPlaying = False

				else:

					turn = 'computer'

		else:

			move = getComputerMove(board, computerLetter)
			makeMove(board, computerLetter, move)


			if isWinner(board, computerLetter):

				drawBoard(board)
				print('You lose! Better luck next time.')
				isPlaying = False

			else:

				if isBoardFull(board):

					drawBoard(board)
					print('The game is a tie!')
					isPlaying = False

				else:

					turn = 'player'
