
import random

def create_gameboard(n): # n represents the number of cols and rows
  board = [] # gameboard

  # since I am not using the variable of the for loop, I swap it to an underline char
  for _ in range(n):
    row = [] # empty row
    for _ in range(n):
      row.append(' ') # fills row with 3 blank strings
    board.append(row) # appends the filled row to board

  return board

def bot_coordinates(gameboard): # gets (x, y) coordinates from bot

  while (True): # checking for valid input
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if gameboard[x][y] != ' ':
      continue
    else:
      break

  return [int(x), int(y)]

def player_coordinates(gameboard): # gets (x, y) coordinates from player
  while (True): # checking for valid input

    x = input('What row? ')

    if x.isdigit() and int(x) <= 2 and int(x) >= 0:
      y = input('What column? ')
      if y.isdigit() and int(y) <= 2 and int(y) >= 0:
        if gameboard[int(x)][int(y)] == ' ':
          break
        else:
          print('This spot is already filled!')

  return [int(x), int(y)]

def symbol_choice(): # gets the player's symbol choice
  while (True): # checking for valid input
    s = input('What symbol you want to be? X or O? ')
    if s == 'X' or s == 'O':
      break
    if s != 'X' or s != 'O':
      s = input('Please select either X or O. ')
  
  return s

def win_check(gameboard, s):
  # winning conditions
  if gameboard[0][0] == s and gameboard[1][1] == s and gameboard[2][2] == s \
    or gameboard[0][2] == s and gameboard[1][1] == s and gameboard[2][0] == s \
    or gameboard[0][0] == s and gameboard[1][0] == s and gameboard[2][0] == s \
    or gameboard[0][1] == s and gameboard[1][1] == s and gameboard[2][1] == s \
    or gameboard[0][2] == s and gameboard[1][2] == s and gameboard[2][2] == s \
    or gameboard[0][0] == s and gameboard[0][1] == s and gameboard[0][2] == s \
    or gameboard[1][0] == s and gameboard[1][1] == s and gameboard[1][2] == s \
    or gameboard[2][0] == s and gameboard[2][1] == s and gameboard[2][2] == s:
    return True
  else:
    return False
  
def tie_check(gameboard): # checking if the game tied
  counter = 0
  for i in range(len(gameboard)):
    for j in range(len(gameboard[i])):
      if gameboard[i][j] != ' ': # if a coordinate is filled
        counter =+ 1 # increment the counter

  if counter == 9: # if all coordinates are filled return true
    return True
  return False
  
def main():
  turn = 1
  gameboard = create_gameboard(3)
  
  player_symbol = symbol_choice()
  bot_symbol = None

  if player_symbol == 'X':
    bot_symbol = 'O'
  else:
    bot_symbol = 'X'

  while (True):

    # player's turn ---------------------------------------
    coordinates_1 = player_coordinates(gameboard)
    x_player = coordinates_1[0]
    y_player = coordinates_1[1]

    gameboard[x_player][y_player] = player_symbol

    if tie_check(gameboard): # break if tie
      print(f'The game tied on turn: {turn}!')
      break

    # feedback being print on terminal --------------------
    print(f"\nPlayer's turn: {turn}")
    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2], '\n')
    turn += 1

    if win_check(gameboard, player_symbol):
      print('Player won the game!')
      break

    # bot's turn ------------------------------------------
    coordinates_2 = bot_coordinates(gameboard)
    x_bot = coordinates_2[0]
    y_bot = coordinates_2[1]

    gameboard[x_bot][y_bot] = bot_symbol

    if tie_check(gameboard): # break if tie
      print(f'The game tied on turn: {turn}!')
      break

    # feedback being print on terminal --------------------
    print(f"\nBot's turn: {turn}")
    print(gameboard[0])
    print(gameboard[1])
    print(gameboard[2], '\n')
    turn += 1

    if win_check(gameboard, bot_symbol):
      print('Bot won the game!')
      break
    
# run the game
main()
  