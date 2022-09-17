def RedaktSl(board,letter,move):
    board[move] = letter
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
displayBoard(board)   
redakt = input('Введите число от 1 до 9')
redakt = 5


def ProverkaWin(board,):
    print(ProverkaWin(board,'X'))
board[4] = 'X'
board[5] = 'X'
board[6] = 'X'
displayBoard(board)
print(ProverkaWin(board,'X',True))
