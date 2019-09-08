import random

def drawBoard(board):

	"""

	This function prints out the board

	"board" is a list of 10 strings representing the board (ignore index 0)


			|		|			
		1	|	2	|	3	
			|		|
	    ------------------------------------------
			|		|		
		4	|	5	|	6
			|		|
	    ------------------------------------------
			|		|
		7	|	8	|	9
			|		|


	"""

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

	# Lets the player select which letter they want to be.

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

	# Randomly choose who goes first

	if random.randint(0, 1) == 0:

		return 'computer'

	else:

		return 'player'


def isSpaceFree(board, move):

	# Return true if the passed move is free on the passed board.

	return board[move] == ' '


def getPlayerMove(board):

	# Let the player type in their move.

	move = ' '

	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

		print('What is your next move? (1-9)')
		move = str(input())
		#print move

	return int(move)


def makeMove(board, letter, move):

	board[move] = letter


def isWinner(board, letter):

	return ((board[1] == letter and board[2] == letter and board[3] == letter) or # across the top

	(board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle

	(board[7] == letter and board[8] == letter and board[9] == letter) or # across the bottom

	(board[1] == letter and board[4] == letter and board[7] == letter) or # down the left side

	(board[2] == letter and board[5] == letter and board[8] == letter) or # down the middle

	(board[3] == letter and board[6] == letter and board[9] == letter) or # down the right side

	(board[3] == letter and board[5] == letter and board[7] == letter) or # diagonal

	(board[1] == letter and board[5] == letter and board[9] == letter)) # diagonal


def isBoardFull(board):

	# Return True if every space on the board has been taken. Otherwise return False.

	for i in range(1, 10):

		if isSpaceFree(board, i):

			return False

	return True


def getDuplicate(board):

	# Make a duplicate of the board list and return it the duplicate.

	duplicate = []

	for i in board:

		duplicate.append(i)

	return duplicate



def choose(board, list):

	# Returns a valid move from the passed list on the passed board.

	# Returns None if there is no valid move.

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

	# Given a board and the computer's letter, determine where to move and return that move.

	if computerLetter == 'X':

		playerLetter = 'O'

	else:

		playerLetter = 'X'

	#print playerLetter


	# First, check if it can win in the next move

	for i in range(1, 10):

		copy = getDuplicate(board)

		if isSpaceFree(copy, i):

			makeMove(copy, computerLetter, i)

			if isWinner(copy, computerLetter):

				#print i
				return i


	# Check if the player could win on their next move, and block them.

	for i in range(1, 10):

		copy = getDuplicate(board)

		if isSpaceFree(copy, i):

			makeMove(copy, playerLetter, i)

			if isWinner(copy, playerLetter):

				#print i
				return i


	# Try to take one of the corners, if they are free.

	move = choose(board, [1, 3, 7, 9])

	if move != None:

		return move


	# Try to take the center, if it is free.

	if isSpaceFree(board, 5):

		return 5


	# Move on one of the sides.

	return choose(board, [2, 4, 6, 8])


def playAgain():

	# Returns True if the player wants to play again, otherwise it returns False.

	print("Do you want to play again? ('yes' or 'no')")
	return input().lower().startswith('y')




print('\n Welcome to Tic Tac Toe !!! \n')

while True:

	board = [' '] * 10
	#drawboard(board)

	playerLetter, computerLetter = inputLetter()
	#print 'You are ' + playerLetter + '\n'
	#print 'Computer is ' + computerLetter + '\n'

	turn = toss()

	print 'The ' + turn + ' will go first.\n'

	isPlaying = True


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


	if not playAgain():

		break
