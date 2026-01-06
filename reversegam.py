import random
import sys

# gameboard size
WIDTH = 8
HEIGHT = 8

def generate_board():
  board = []

  for i in range(WIDTH):
    board.append([])
    for _ in range(HEIGHT):
      board[i].append(' ')

  return board

def print_board(board):
  column_nums = '    ' # first column numbers spacing
  for i in range(len(board)):
    # building the column numbers
    column_nums += str(i)
    column_nums += '    '

  print(column_nums) # column numbers

  for i, row in enumerate(board):
    print(i, row, i) # row numbers and board tiles

  print(column_nums) # column numbers

def is_valid_move(board, tile, xstart, ystart):

  surrounding_movements = [[0, 1], [1, 1], [1, 0], [1, -1],[0, -1], [-1, -1], [-1, 0], [-1, 1]]
  other_tile = '' # opponent tile placeholder

  if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
    return False

  # assigning the opponent tile a value
  if tile.upper() == 'X':
    other_tile = 'O'
  else:
    other_tile = 'X'

  tilesToFlip = [] # list of tiles to flip
  coord_scores = []
  score = 0 # how many tiles the current move can flip

  for x_dir, y_dir in surrounding_movements:
    x, y = xstart, ystart
    x += x_dir # checking surroundings
    y += y_dir # checking surroundings
    while is_on_board(x, y) and board[x][y] == other_tile: # if the sum ended up in an opponent tile
      x += x_dir
      y += y_dir
      score += 1
      if is_on_board(x, y) and board[x][y] == tile: # valid move
        # start bouncing back
        while True:
          x -= x_dir
          y -= y_dir
          tilesToFlip.append([x, y]) # record tiles to be flipped
          if x == xstart and y == ystart: # when the loop gets back to the origin, break
            coord_scores.append([[xstart, ystart], score]) 
            score = 0 # clear the score variable
            break

  if len(tilesToFlip) == 0: # there are no tiles to flip
    return False
  else: # there are tiles to flip
    return tilesToFlip, coord_scores
  
def get_valid_moves(board, tile):
  valid_moves = [] # placeholder

  # iterating through all gameboard coords to check valid moves
  for x in range(WIDTH): 
    for y in range(HEIGHT):
      if is_valid_move(board, tile, x, y) != False:
        valid_moves.append([x, y])

  return valid_moves

def feed_valid_moves(board, moves_list):
  for move in moves_list: # feeding hints into board
    mx, my = move[0], move[1]
    board[mx][my] = 'H'

def clear_old_valid_moves(board):
  for row in board: # clearing previous hints
    for i, column in enumerate(row):
      if column == 'H' or column == 'B': # checking the value
        row[i] = ' ' # updating the index of that value

def is_on_board(x, y): # is move within the board
  return x < WIDTH and x >= 0 and y >= 0 and y < HEIGHT

def who_goes_first(): # if 0 -> user's turn ; if 1 -> bot's turn
  return random.randint(0, 1)

def is_game_won(board):
  spaces_filled = 0 # how many spaces filled in total
  x_spots = 0 # how many x spots filled
  y_spots = 0 # how many y spots filled

  for row in board: # iterate through every row
    for column in row: # iterate through every column in the row
      if column == 'X': # check if it is taken by X
        spaces_filled += 1
        x_spots += 1

      elif column == 'O': # check if it is taken by O
        spaces_filled += 1
        y_spots += 1

  if spaces_filled == WIDTH * HEIGHT: # if the board is filled
    return x_spots, y_spots # returning a tuple of the spots filled
  
  else:
    return False

def make_move(board, tile, x, y):
  result = is_valid_move(board, tile, x, y)[0] # getting the valid moves
  board[x][y] = tile

  for coord in result:
    x_result, y_result = coord[0], coord[1]
    board[x_result][y_result] = tile
  
def getBestMove(board, tile):
  list_of_score_moves = []
  score_numbers = [] 

  # iterating through all gameboard coords to check valid moves
  for x in range(WIDTH): 
    for y in range(HEIGHT):
      if is_valid_move(board, tile, x, y) != False:
        score_moves = is_valid_move(board, tile, x, y)[1]

        if len(score_moves) > 1:
          for el in score_moves:
            list_of_score_moves.append(el)
        else:
          list_of_score_moves.append(*score_moves) # spreads the score_moves into the list

  for el in list_of_score_moves: # appending all scores to the list of scores_numbers
    score_numbers.append(el[1])

  highest_score = max(score_numbers) # getting the highest score

  # works like the .find() method from js
  # finding the coordinate that matches the highest score
  return next((el for el in list_of_score_moves if el[1] == highest_score), None)[0]
  
def get_points(board):
  x_points = 0
  o_points = 0

  for row in board:
    for column in row:
      if column == 'X':
        x_points += 1

      elif column == 'O':
        o_points += 1

  return x_points, o_points

def play_game():
  # defining variables
  player_tile = None
  bot_tile = None
  hints = False
  turn = None

  # deciding what tile bot will have upon user choice
  while True:
    tile_choice = input('Wants to be X or O?\n')
    if tile_choice.upper() == 'X':
      player_tile = tile_choice.upper()
      bot_tile = 'O'
      break

    elif tile_choice.upper() == 'O':
      player_tile = tile_choice.upper()
      bot_tile = 'X'
      break
    
    else:
      print('Choose only between X or O')
  
  gameboard = generate_board() # generates the gameboard

  # feeding the first values
  gameboard[3][3] = 'X'
  gameboard[3][4] = 'O'
  gameboard[4][3] = 'O'
  gameboard[4][4] = 'X'
  print_board(gameboard) # prints the first image of board

  turn = who_goes_first()

  while True: # main game loop
    x_points, o_points = get_points(gameboard) # get the updated points from both sides
    print(f"Player points: {x_points} | Bot points: {o_points}")

    if turn == 0:
      while True: # player's move while loop
        player_move = input("Enter you coordinates, enter 'quit' to quit or type 'hints' \n") # player move choice
        if player_move.isdigit() and len(player_move) == 2:
          player_x = int(player_move[0])
          player_y = int(player_move[1])

          # if the coordinates entered are already taken and is not a hint
          if gameboard[player_x][player_y] != ' ' and gameboard[player_x][player_y] != 'H'  and gameboard[player_x][player_y] != 'B': 
            print('This coordinate is already taken')

          elif is_on_board(player_x, player_y) and is_valid_move(gameboard, player_tile, player_x, player_y): # if move is valid
            make_move(gameboard, player_tile, player_x, player_y) # calling player main move function

            if hints: # hints are displayed as a capital h (H)
              clear_old_valid_moves(gameboard)
              valid_moves = get_valid_moves(gameboard, player_tile) 
              feed_valid_moves(gameboard, valid_moves) 

            print_board(gameboard)

            if is_game_won(gameboard) != False: # game won check
              print('You won the game, congrats!')
              sys.exit()

            turn += 1 # pass the turn
            break

          else: # out of bounds condition
            print('Out of bounds or invalid move\n')

        elif player_move == 'quit': # quits the game
          sys.exit()

        elif player_move == 'hints': # toggles hints between False and True
          hints = not hints

          if hints: # hints are displayed as a capital h (H)
            clear_old_valid_moves(gameboard)
            valid_moves = get_valid_moves(gameboard, player_tile)
            feed_valid_moves(gameboard, valid_moves) # feed hints
          
          else: # if hints is toggled off
            clear_old_valid_moves(gameboard)

          print_board(gameboard) 

        else: # if the player input is not in the right coordinate format
          print('Your move needs to be 2 numbers from 0 to 8 and no space in between\n')  

    elif turn == 1:
      while True: # bot's move while loop
        press_enter = input('Press enter so the bot makes a move\n')

        if len(press_enter) != 0: # if the wrote something other than only pressing enter
          print('Just press enter, do not enter any values\n')

        else:
          # getting the bot's best move
          bot_move = getBestMove(gameboard, bot_tile)
  
          bx, by = bot_move # unpacking the x and y coordinates from the move
          tiles_to_flip, _ = is_valid_move(gameboard, bot_tile, bx, by) # getting the tiles to flip

          for tx, ty in tiles_to_flip: # flipping
            gameboard[tx][ty] = bot_tile

          gameboard[bx][by] = bot_tile # assigning the tile to the bot's final coordinate decision

          print_board(gameboard)

          if is_game_won(gameboard) != False: # game won check
            print('You loose! Bot won the game.')
            sys.exit()

          turn -= 1 # pass the turn
          break
    
    else:
      print('Something went wrong')
      sys.exit()

play_game()
