from random import randint

class Board:
    def __init__(self):
        self.data = [' - '] * 9

    def display(self):
        for i in range(1,4):
            print(f" {' '.join(self.data[(i-1)*3:i*3])} ")

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
        self.win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
            [0, 4, 8], [2, 4, 6] # Diagonals
        ]

        player_name = input("Enter name: ")
        player_symbol = input("What symbol would you like to be? (opponent is always X): ")
        print("")
        self.player = Player(player_name, player_symbol)
        self.opponent = Player("Opponent", "X")
        cur = randint(0,1)
        if cur == 0:
            self.current_player = self.player
            print(f"{self.player.name} starts!")
        else:
            self.current_player = self.opponent
            print("Opponent starts!")

    def checkWin(self, player):
        sym = player.symbol
        return any(all(self.board.data[pos] == f" {sym} " for pos in condition) for condition in self.win_conditions)

    def checkDraw(self):
        return all(cell != ' - ' for cell in self.board.data)
    
    def checkStatus(self):
        if self.checkWin(self.current_player):
            self.board.display()
            print(f"Player {self.current_player.symbol} wins!")
            return False

        elif self.checkDraw():
            self.board.display()
            print("The game is a draw!")
            return False
        
        return True
    
    
    

    def playGame(self):
        while True:
            self.board.display()
            
            if self.current_player == self.player:
                try:
                    print(f"{self.player.name}, it's your move!")
                    row = int(input("Column to place piece: "))
                    column = int(input("Row: "))
                    if not self.board.set_cell(row, column, self.player.symbol):
                        print("Cell already taken, try again.")
                        continue
                except ValueError:
                    print("Invalid input, please enter numbers only.")
                    continue
            else:
                #if you can get three in a row; do it
                #if you can stop the opponent from getting three in a row; do it
                #otherwise random move

                # (self.board.data[pos] == f" {sym} " for pos in condition) for condition in self.win_conditions

                # for condition in self.win_conditions:
                #     for pos in condition:
                #         if all()



                row = randint(1,3)
                column = randint(1,3)
                while not self.board.set_cell(row, column, self.opponent.symbol):
                    row = randint(1,3)
                    column = randint(1,3)
                print("\nThe opponent made a move!")

            if not self.checkStatus():
                break
            self.current_player = self.opponent if self.current_player == self.player else self.player


ticTacToe = TicTacToe()
ticTacToe.playGame()

