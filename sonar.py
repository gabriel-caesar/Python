# pseudo-code:
# gameboard is 10x10
# input a coordinate
# that coordinate will check how far the treasure is
# sonar devices have a range of 4 spaces
import random
import sys
import math
import re

class Gameboard:
  
  # I made it 10x10 because the print is nicer
  def __init__(self, treasures):
    self.x: int = 10
    self.y: int = 10
    self.sonar_devices = 20
    self.dropped_sonar_locations =[]
    self.board: list = []
    self.treasures: int = treasures
  
  # builds the gameboard with the coordinates you choose
  def build_board(self):
    for i in range(self.x):
      self.board.append([])
      for _ in range(self.y):
        self.board[i].append(' ')
      
  # pretty print for the gameboard
  def print_board(self):
    column_nums = '   ' # column number identifiers

    for column in range(len(self.board[0])):
      column_nums += str(column)
      column_nums += '    '

    print(column_nums)

    for row in range(len(self.board)):
      print(row, self.board[row], row, end='\n') # row number identifiers get printed with the rows

    print(column_nums)

  # drop treasures throughout the board
  def drop_treasure(self):

    # placeholder list for coordinate dicts
    coords = []

    # compares the existing coordinates inside coords
    # agains the ones being generate in the current iteration
    def check(existing_coordinates, x, y):
      return existing_coordinates['x'] == x and existing_coordinates['y'] == y

    for _ in range(self.treasures):
      while True:
        x = random.randint(0, self.x - 1)
        y = random.randint(0, self.y - 1)
        
        # duplicate condition checker
        # "dic in coords" is an coordinate dict inside coords in that current interation
        # any() will work something like the Array.some() JS method
        duplicate_condition = any(check(dic, x, y) for dic in coords)

        # if any duplicate was found
        if not duplicate_condition:
          coords.append({'x': x, 'y': y})
          break

        
    # then, treasures becomes a list of dict coordinates of the sunken treasures
    self.treasures = coords

  # drop sonars on the board
  def drop_sonars(self, x, y):

    # checks if a device was already dropped in the desired coordinates
    def check_duplicate_locations(exist, x, y): 
      return exist['x'] == x and exist['y'] == y
    if any(check_duplicate_locations(coord, x, y) for coord in self.dropped_sonar_locations):
      print('\nThere is a sonar device in this location already\n')
      return

    distance_list = []
    for coord in self.treasures:
      # getting the distance
      distance_list.append(self.check_distance(coord, x, y)) 

    # taking the minimum value out of the list of coordinates
    distance = min(distance_list)

    self.sonar_devices -= 1 # subtract from the sonar total amount
    
    if distance == 0:
      self.treasures.remove({'x': x, 'y': y}) # removing the found treasure from the treasures list
      self.board[x][y] = 'F' # updating the found treasure location
      print('\n ------------------ \n')
      self.print_board() # print the board
      print(f"You've found a sunken treasure") # user feedback
    elif distance <= 4:
      self.board[x][y] = str(distance) # drop sonar at the coordinates location
      print('\n ------------------ \n')
      self.print_board() # print the board
      print(f'Treasure detected at a distance of {distance} from the sonar device.')
    else:
      self.board[x][y] = 'O'
      print('\n ------------------ \n')
      self.print_board() # print the board
      print('Sonar did not detect anything. All treasure chests out of range') # nothing found

    self.dropped_sonar_locations.append({'x': x, 'y': y}) # recording the dropped location
    print(f'\nDropped a sonar device at [{x}, {y}] coordinates')
    print(f'\nYou have {self.sonar_devices} sonar devices left\n')


  @staticmethod
  def check_distance(coord, x, y):
      # using the pythagorean theorem to calculate the smallest distance
      # between the sonar device and the sunken treasure
      distance = math.sqrt((coord['x'] - x) * (coord['x'] - x) + (coord['y'] - y) * (coord['y'] - y))
    
      return round(distance)
  

def main():
  while (True):
    unstripped_answer = input('Tell me the coordinates commander (Enter q or quit to exit)!\nOrder: ')
    answer = unstripped_answer.strip()

    # quits the game
    if answer.lower() == 'quit' or answer.lower() == 'q':
      sys.exit()

    # accepts only up to 2 numbers per coordinates between a space
    # strip works like trim()
    if bool(re.search(r'^\d{1,2}\s\d{1,2}$', answer)): 
        
      # creates a list out of the coordinates string
      user_coordinates = list(answer.strip(','))
    
      # coordinates placeholder arrays
      x_array = []
      y_array = []

      # flag for when the for loop passes the space between coordinates
      passed_space = False

      # get the raw x and y coordinates out of the user_coordinates array
      for i in user_coordinates:

        if i == ' ':
          passed_space = True

        if not passed_space and i != ' ':
          x_array.append(i)
        elif passed_space and i != ' ':
          y_array.append(i)    
        

      # x and y filtered coordinates
      x_coordinate = int(''.join(x_array))
      y_coordinate = int(''.join(y_array))

      # checks if the coordinates are within the board
      if x_coordinate > 9 or y_coordinate > 9:

        print('\nCoordinates need to be within the board limit (up to 9 either way)\n')

      else:

        # will drop the sonar device and check the 
        # distance for the closest sunken treasure
        gameboard.drop_sonars(x_coordinate, y_coordinate)

      if len(gameboard.treasures) == 0:
        print('You found all the treasures, congrats!')
        sys.exit()

      if gameboard.sonar_devices == 0:
        print('You ran out of sonar devices, you loose!')
        sys.exit()

    else:
      print('The coordinates needs to be numbers!')
    

gameboard = Gameboard(3)

gameboard.build_board()
gameboard.drop_treasure()
gameboard.print_board()
main()