#Skeleton Program for the AQA COMP1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA COMP1 Programmer Team
#developed in a Python 3.4 programming environment

import random

def SetUpGameBoard(Board, Boardsize):
  """
    Initializes the game board for the game. The board is a square grid 
    of size 'BoardSize' x 'BoardSize'. Initially, four pieces are set in the center of 
    the board in a diagonal layout - two 'C's and two 'H's, alternating.
  """
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if (Row == (BoardSize + 1) // 2 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2 + 1):
        Board[Row][Column] = "C"
      elif (Row == (BoardSize + 1) // 2 + 1 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2):
        Board[Row][Column] = "H"
      else:
        Board[Row][Column] = " "

def ChangeBoardSize():
  """
    Prompts the user to specify a new size for the game board. The valid range for board size is between 4 and 9. 
    The function ensures that the user input falls within this range, repeatedly prompting for input until a valid size is entered. 
  """
  BoardSize = int(input("Enter a board size (between 4 and 9): "))
  while not(BoardSize >= 4 and BoardSize <= 9):
    BoardSize = int(input("Enter a board size (between 4 and 9): "))
  return BoardSize

def GetHumanPlayerMove(PlayerName):
  """
    Requests input from the human player to determine their next move. The coordinates are provided as a single integer, 
    representing a row and column.
  """
  print("Enter the coodinates of the square where you want to place your piece: ")

  while True:
    Row = input("Row number: ")
    Column = input("Column number: ")
    try:
      Row = int(Row)
      Column = int(Column)
      break
    except ValueError:
      print("Invalid input; please only enter numbers for the coordinates")

  return int(f"{Row}{Column}")

def GetComputerPlayerMove(BoardSize):
  """
    Determines the move for the computer player. It randomly selects a position on the game board for the computer's move. 
    The selection is made within the bounds of the current board size, ensuring the move is within the playable area.
  """
  return random.randint(1, BoardSize) * 10 + random.randint(1, BoardSize)

def GameOver(Board, BoardSize):
  """
    Evaluates whether the game has reached its end. The game is considered over when there are no more empty spaces 
    (' ') on the board, implying that all possible moves have been made.
  """
  for Row in range(1 , BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == " ":
        return False
  return True

def GetPlayersName():
  """
    Asks the user to enter their name, which will be used in the game. The player's name is used for personalizing 
    the game experience, such as addressing the player during their turn or announcing the winner of the game.
  """
  PlayerName = input("What is your name? ")
  return PlayerName

def CheckIfMoveIsValid(Board, Move, BoardSize):
  """
    Checks the validity of a proposed move. A move is considered valid if the targeted square on the board is currently empty. 
  """
  Row = Move % 10
  Column = Move // 10
  MoveIsValid = False
  if Row > BoardSize or Row < 0:
    return False
  elif Column > BoardSize or Column < 0:
    return False
  elif Board[Row][Column] == " ":
    MoveIsValid = True
  return MoveIsValid

def GetPlayerScore(Board, BoardSize, Piece):
  """
    Calculates and returns the score of a player. The score is the total number of pieces belonging to the player on the board. 
  """
  Score = 0
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == Piece:
        Score = Score + 1
  return Score

def CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  """
    Determines whether there are opponent pieces in a line from a starting point that can be flipped following a player's move. 
    This is a key element of gameplay, where capturing opponent pieces by enclosing them in a line is a primary mechanism.
  """
  RowCount = StartRow + RowDirection
  ColumnCount = StartColumn + ColumnDirection
  FlipStillPossible = True
  FlipFound = False
  OpponentPieceFound = False
  while RowCount <= BoardSize and RowCount >= 1 and ColumnCount >= 1 and ColumnCount <= BoardSize and FlipStillPossible and not FlipFound:
    if Board[RowCount][ColumnCount] == " ":
      FlipStillPossible = False
    elif Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      OpponentPieceFound = True
    elif Board[RowCount][ColumnCount] == Board[StartRow][StartColumn] and not OpponentPieceFound:
      FlipStillPossible = False
    else:
      FlipFound = True
    RowCount = RowCount + RowDirection
    ColumnCount = ColumnCount + ColumnDirection
  return FlipFound

def FlipOpponentPiecesInOneDirection(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  """
    Flips the opponent's pieces in a specified direction starting from a given point. This function is executed after a valid move 
    is made.
  """
  FlipFound = CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection)
  if FlipFound:
    RowCount = StartRow + RowDirection
    ColumnCount = StartColumn + ColumnDirection
    while Board[RowCount][ColumnCount] != " " and Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      if Board[RowCount][ColumnCount] == "H":
        Board[RowCount][ColumnCount] = "C"
      else:
        Board[RowCount][ColumnCount] = "H"
      RowCount = RowCount + RowDirection
      ColumnCount = ColumnCount + ColumnDirection

def MakeMove(Board, BoardSize, Move, HumanPlayersTurn):
  """
    Executes a move on the board. This includes placing a piece at the designated spot and flipping any opponent pieces 
    as dictated by the rules of the game.
  """
  Row = Move % 10
  Column = Move // 10
  if HumanPlayersTurn:
    Board[Row][Column] = "H"
  else:
    Board[Row][Column] = "C"
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, -1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, 1)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, -1)


def PrintLine(BoardSize):
  """
    Prints a horizontal line as part of the game board display. This line is used to visually separate rows of the board. 
    The length of the line is proportional to the size of the board. This function is a helper function for 'DisplayGameBoard',
    contributing to the board's visual representation in the console.
  """
  print("   ", end="")
  for Count in range(1, BoardSize * 2):
    print("_", end="")
  print()

def DisplayGameBoard(Board, BoardSize):
  """
    Renders the game board in the console. This function presents the current state of the board, including the positions of all 
    pieces ('H' for human, 'C' for computer, and ' ' for empty spaces). It displays row and column numbers around the board for easy 
    reference and uses horizontal and vertical lines to create a grid-like appearance.
  """
  print()
  print("  ", end="")
  for Column in range(1, BoardSize + 1):
    print(" ", end="")
    print(Column, end="")
  print()
  PrintLine(BoardSize)
  for Row in range(1, BoardSize + 1):
    print(Row, end="")
    print(" ", end="")
    for Column in range(1, BoardSize + 1):
      print("|", end="")
      print(Board[Row][Column], end="")
    print("|")
    PrintLine(BoardSize)
    print()

def DisplayMenu():
  """
    Displays the main menu of the game to the console. The menu provides options to the player, including starting a new game, 
    entering their name, changing the board size, and quitting the game. This function facilitates the primary user interaction 
    with the game outside of the gameplay itself, allowing players to navigate through different actions and settings.
  """
  print("(p)lay game")
  print("(e)nter name")
  print("(c)hange board size")
  print("(q)uit")
  print()

def GetMenuChoice(PlayerName):
  """
    Prompts the player to choose an option from the main menu. The player's input is expected to be a single letter corresponding 
    to one of the menu options. This function is a key part of the game's navigation, enabling the player to select what they want 
    to do next in the game interface.
  """
  print(PlayerName, "enter the letter of your chosen option: ", end="")
  Choice = input()
  return Choice

def CreateBoard():
  """
    Creates and initializes the game board as a two-dimensional list (a list of lists). This function sets up an empty board based 
    on the current board size, with each cell initialized to an empty string. The board is used to store the positions of all pieces 
    throughout the game. This function is usually called at the start of a new game to reset the board to its initial state.
  """
  Board = []
  for Count in range(BoardSize + 1):
    Board.append([])
    for Count2 in range(BoardSize + 1):
      Board[Count].append("")
  return Board

def PlayGame(PlayerName, BoardSize):
  """
    Manages the entire game process, from start to finish. This function sets up the board, manages turns between the human and 
    computer players, checks for the validity of moves, and updates the board accordingly. It also determines when the game is over 
    and announces the winner based on the scores. This function is the core of the game, where the main gameplay loop occurs.
  """
  Board = CreateBoard()
  SetUpGameBoard(Board, BoardSize)
  HumanPlayersTurn = False
  while not GameOver(Board, BoardSize):
    HumanPlayersTurn = not HumanPlayersTurn
    DisplayGameBoard(Board, BoardSize)
    MoveIsValid = False
    while not MoveIsValid:
      if HumanPlayersTurn:
        Move = GetHumanPlayerMove(PlayerName)
      else:
        Move = GetComputerPlayerMove(BoardSize)
      MoveIsValid = CheckIfMoveIsValid(Board, Move, BoardSize)
    if not HumanPlayersTurn:
      print("Press the Enter key and the computer will make its move")
      input()
    MakeMove(Board, BoardSize, Move, HumanPlayersTurn)
  DisplayGameBoard(Board, BoardSize)
  HumanPlayerScore = GetPlayerScore(Board, BoardSize, "H")
  ComputerPlayerScore = GetPlayerScore(Board, BoardSize, "C")
  if HumanPlayerScore > ComputerPlayerScore:
    print("Well done", PlayerName, ", you have won the game!")
  elif HumanPlayerScore == ComputerPlayerScore:
    print("That was a draw!")
  else:
    print("The computer has won the game!")
  print()


random.seed()
BoardSize = 6
PlayerName = ""
Choice = ""
while Choice != "q":
  DisplayMenu()
  Choice = GetMenuChoice(PlayerName)
  if Choice == "p":
    PlayGame(PlayerName, BoardSize)
  elif Choice == "e":
    PlayerName = GetPlayersName()
  elif Choice == "c":
    BoardSize = ChangeBoardSize()
