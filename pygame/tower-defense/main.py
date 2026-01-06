import pygame
import sys
from random import choice, randint
from utils import load_image
from player import Player

SCREEN_X = 1200
SCREEN_Y = 640
CHUNK_SIZE = 8 
TILE_SIZE = 32
GROUND_STARTPOINT_Y = 384 // TILE_SIZE

pygame.init()

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption('Tower Defense')
clock = pygame.time.Clock()

def generate_chunks(cx, cy):
  chunk_data = []
  for y in range(CHUNK_SIZE):
    for x in range(CHUNK_SIZE):
      # cx * CHUNK_SIZE → is the top-left corner of the chunk in a tile map
      # adding the x to the equation gets the current tile offset within the chunk we're filling
      tile_x = cx * CHUNK_SIZE + x
      tile_y = cy * CHUNK_SIZE + y

      tile_type = 0
      if tile_y == GROUND_STARTPOINT_Y:
        tile_type = choice([1, 2, 2, 2, 2, 3, 4]) # grass, dirt or stone
      elif tile_y > GROUND_STARTPOINT_Y:
        tile_type = 5 # underground
      elif tile_y == GROUND_STARTPOINT_Y - 1:
        gc = randint(0, 3)
        if gc == 1:
          tile_type = choice([6, 7, 8, 9]) # rocks or plants

      if tile_type != 0:
        chunk_data.append([[tile_x, tile_y], tile_type])

  return chunk_data # return the chunk_data for each chunk that's filled

def draw_map(chunk_data):
  for chunk in chunk_data:
    x_pos = chunk[0][0] * TILE_SIZE
    y_pos = chunk[0][1] * TILE_SIZE
    if chunk[1] == 1:
      screen.blit(grass_1, (x_pos, y_pos))
    elif chunk[1] == 2:
      screen.blit(grass_2, (x_pos, y_pos))
    elif chunk[1] == 3:
      screen.blit(dirt_1, (x_pos, y_pos))
    elif chunk[1] == 4:
      screen.blit(stone_1, (x_pos, y_pos))
    elif chunk[1] == 6:
      screen.blit(rock_1, (x_pos, y_pos))
    elif chunk[1] == 7:
      screen.blit(rock_2, (x_pos, y_pos))
    elif chunk[1] == 8:
      screen.blit(flowers_1, (x_pos, y_pos))
    elif chunk[1] == 9:
      screen.blit(flowers_2, (x_pos, y_pos))
    elif chunk[1] == 5:
      screen.blit(underground, (x_pos, y_pos))

def generate_map():
  chunks_horizontal = round(SCREEN_X // (CHUNK_SIZE * TILE_SIZE)) + 1
  chunks_vertical = round(SCREEN_Y // (CHUNK_SIZE * TILE_SIZE)) + 1
  chunk_data = []
  for cy in range(chunks_vertical):
    for cx in range(chunks_horizontal):
      chunk_data += generate_chunks(cx, cy)

  return chunk_data

# Generating map
chunk_data = generate_map()

# Importing the world images
gun_subpath = ['assets', 'graphics', 'field_gun']
world_subpath = ['assets', 'graphics', 'world']
field_gun_image = load_image('fieldgun_idle.png', gun_subpath)
grass_1 = load_image('grass_1.png', world_subpath)
grass_2 = load_image('grass_2.png', world_subpath)
dirt_1 = load_image('dirt_1.png', world_subpath)
stone_1 = load_image('stone_1.png', world_subpath)
flowers_1 = load_image('flowers_1.png', world_subpath)
flowers_2 = load_image('flowers_2.png', world_subpath)
rock_2 = load_image('rock_2.png', world_subpath)
rock_1 = load_image('rock_1.png', world_subpath)
underground = load_image('underground.png', world_subpath)

# Instantiating a new player
player = Player(200, 384)

player_sprite_group = pygame.sprite.GroupSingle()
player_sprite_group.add(player)
while True:
  screen.fill("#63bbd1")  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.set_direction('left')
      if event.key == pygame.K_RIGHT:
        player.set_direction('right')

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT:
        player.set_direction('')
      if event.key == pygame.K_RIGHT:
        player.set_direction('')

  # Map drawing
  draw_map(chunk_data)

  player_sprite_group.draw(screen)
  player.update()

  pygame.display.update()
  clock.tick(60)