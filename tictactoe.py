import random

print('Welcome to Tic Tac Toe !!!')

print '\n'

board = [' '] * 10 

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

letter = ''
print("Do you want to be 'X' or 'O' ??")

while not (letter == 'X' or letter == 'O'):
	
	letter = input()

	if letter == 'X':

		playerLetter = 'X'
		computerLetter = 'O'
	
	elif letter == 'O':

		playerLetter = 'O'
		computerLetter = 'X'

	else:

		print 'Please check the character entered !!'
		print "Do you want to be 'X' or 'O' ??"

print 'You are ' + playerLetter + '\n'
print 'Computer is ' + computerLetter + '\n'

toss = random.randint(0, 1)

if toss == 0:

	turn = 'computer'

else:

	turn = 'player'

print 'The ' + turn + ' will go first.\n'
