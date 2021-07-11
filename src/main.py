import os

def startGame():
    player1char = input("Player 1, please select X or O: ")

    while(not player1char.lower() == "o" and not player1char.lower() == "x"):
        print(f'"{player1char}" is not O or X.')
        player1char = input("Please select X or O: ")
    player1char = player1char.upper()
    player2char = 'O' if player1char == 'X' else 'X'
    return (player1char, player2char)

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

def printBoard(board):
    clear_output()
    line = '---|---|---'
    boardValueLine = lambda boardLine: f' {boardLine[0]} | {boardLine[1]} | {boardLine[2]} '
    print(boardValueLine(board[0]), line, 
          boardValueLine(board[1]), line,
          boardValueLine(board[2]), sep="\n")
    
def requestPlayerInput(playerNumber, char, board):
    userInput = input(f"Player {playerNumber} (1-9): ")
    while(not userInput.isdigit() or int(userInput) > 9 or int(userInput) < 1 or not getBoardValue(int(userInput), board) == ' '):
        print(f'"{userInput}" is not a valid unoccupied position between 1 and 9.')
        userInput = input(f"Player {playerNumber} (1-9): ")
    position = int(userInput)
    currentValue = getBoardValue(position, board)
    updateBoard(position, char, board)
            
    
def updateBoard(position, char, board):
    index1, index2 = getPositionIndex(position)
    board[index1][index2] = char

def getBoardValue(position, board):
    index1, index2 = getPositionIndex(position)
    return board[index1][index2] 

def getPositionIndex(position):
    index = 2
    if(position in [1, 2, 3]):
        index = 0
    elif(position in [4, 5, 6]):
        index = 1
    index2 = position - (index * 3) - 1
    return (index, index2)

def checkWinner(board):
    hCombos = [set([hLine[0], hLine[1], hLine[2]]) for hLine in board]
    vCombos = []
    for i in range(0, 3):
        vCombos.append(set([board[0][i], board[1][i], board[2][i]]))
    dCombos = [
        set([board[0][0], board[1][1], board[2][2]]),
        set([board[0][2], board[1][1], board[2][0]])
    ]
    
    combos = hCombos + vCombos + dCombos
    
    winner = ' '
    for index, combo in enumerate(combos):
        if(len(combo) == 1 and not list(combo)[0] == ' '):
            winner = list(combo)[0]
            break
    return winner

def displayWinner(board, playerNumber):
    printBoard(board)
    print(f'\nPlayer {playerNumber} wins!')
    
def runGame():
    while(True):
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ',' ',' ']]
        clear_output()
        player1Char, player2Char = startGame()
        winner = False
        player = 2
        while(not winner):
            printBoard(board)
            player = 2 if player == 1 else 1
            requestPlayerInput(player, player1Char if player == 1 else player2Char, board)
            winningChar = checkWinner(board)
            if(not winningChar == ' '):
                displayWinner(board, player);
                break
        
        userInput = input(f"\nPlay again? (Y/N): ")
        if(not userInput.lower() == 'y' and not userInput.lower() == 'yes'):
            break
        
runGame()