from random import randint

class Board:
    def __init__(self):
        self.data = [' - '] * 9

    def display(self):
        for i in range(1,4):
            print(f" {'' ''.join(self.data[(i-1)*3:i*3])} ")

    def isPosFree(self, pos):
        return self.data[pos] == ' - '

    def set_cell(self, x, y, marker):
        if self.isPosFree((x-1) + (y-1)*3) :
            self.data[(x-1) + (y-1)*3] = f" {marker} "
            return True
        return False

class Player:
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name

class TicTacToe:
    def __init__(self):
        self.board = Board()

        player_name = input("Enter name: ")
        player_symbol = input("What symbol would you like to be? (opponent is always X): ")
        self.player = Player(player_name, player_symbol)
        self.opponent = Player("Opponent", "X")
        cur = randint(0,1)
        if cur == 0:
            self.current_player = self.player
        else:
            self.current_player = self.opponent

    def checkWin(self):
        sym = self.p.sym
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6] # Diagonals
        ]
        return any(all(self.board[pos] == sym for pos in condition) for condition in win_conditions)

    def checkDraw(self):
        return all(True for i in self.board if i != " - ")
    
    def checkStatus(self, end):
        if self.checkWin(self.current_player):
            self.board.display()
            print(f"Player {self.current_player.symbol} wins!")
            end = True

        elif self.checkDraw():
            self.board.display()
            print("The game is a draw!")
            end = True

    def playGame(self):
        end = False
        while end == False:
            self.board.display()

            
            if self.current_player == self.player:
                row = input("Row to place piece: ")#
                column = input("Column: ")
                if self.board.set_cell(row, column, self.current_player.symbol) == True:
                    self.checkStatus()
                    self.current_player = self.opponent
                else:
                    raise Exception("Cell already taken")
            else:
                row = randint(1,3)
                column = randint(1,3)
                while self.board.set_cell(row, column, self.current_player.symbol) == True:
                    row = randint(1,3)
                    column = randint(1,3)

                    self.checkStatus()
                    self.current_player = self.player


        





ticTacToe = TicTacToe()
ticTacToe.playGame()

