import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption('Physics')
screen = pygame.display.set_mode((500, 500), 0, 32)

player = pygame.Rect(100,100,40,80)

tiles = [
  pygame.Rect(200,350,50,50),
  pygame.Rect(260,320,50,50)
]

def collision_test(rect, tiles): # tests rect collisions against titles
  collisions = []
  for tile in tiles:
    if rect.colliderect(tile): # if rect collided with tile
      collisions.append(tile) # populate the tile to the collisions list
  return collisions
  
# rect: what's moving
# movement: how much is moving
# tiles: what's colliding with  
def move(rect, movement, tiles):
  rect.x += movement[0] # rect move in the x axis
  collisions = collision_test(rect, tiles) # test the collision for this movement
  for tile in collisions: # for all tiles that collided
    if movement[0] > 0: # if the movement was rightwards
      rect.right = tile.left
    if movement[0] < 0: # if the movement was leftwards
      rect.left = tile.right

  rect.y += movement[1] # rect move in the y axis
  collisions = collision_test(rect, tiles)
  for tile in collisions:
    if movement[1] > 0:
      rect.bottom = tile.top
    if movement[1] < 0:
      rect.top = tile.bottom
  return rect

# movement flags
right = False
left = False
up = False
down = False

while True:

  screen.fill((0, 0, 0)) # fills the screen with the color provided

  pygame.draw.rect(screen, (255, 255, 255), player) # draw the player rect onto the screen with a given color
  
  for tile in tiles:
    pygame.draw.rect(screen, (255, 0, 0), tile)

  # player velocity
  movement = [0, 0]
  if right:
    movement[0] += 5
  if left:
    movement[0] -= 5
  if down:
    movement[1] += 5
  if up:
    movement[1] -= 5

  player = move(player, movement, tiles)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == KEYDOWN:
      if event.key == K_UP:
        up = True
      if event.key == K_DOWN:
        down = True
      if event.key == K_RIGHT:
        right = True
      if event.key == K_LEFT:
        left = True

    if event.type == KEYUP:
      if event.key == K_UP:
        up = False
      if event.key == K_DOWN:
        down = False
      if event.key == K_RIGHT:
        right = False
      if event.key == K_LEFT:
        left = False

  pygame.display.update() # updates the screen every iteration
  clock.tick(60) # fps
