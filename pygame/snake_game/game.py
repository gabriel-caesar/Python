import sys, pygame, random
clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.display.set_caption('Snake Game')

class Snake:
  def __init__(self, head):
    self.body = [
      pygame.Rect(50, 50, 4, 4),
      pygame.Rect(50, 53, 4, 4),
      pygame.Rect(50, 56, 4, 4),
    ]
    self.head = head

  def body_collision(self, direction):
    # center point of the current head's direction
    if direction == 'right':
      [contact_x, contact_y] = self.head.midright
    elif direction == 'left':
      [contact_x, contact_y] = self.head.midleft
    elif direction == 'up':
      [contact_x, contact_y] = self.head.midtop
    elif direction == 'down':
      [contact_x, contact_y] = self.head.midbottom

    for p in self.body:
      if p.collidepoint(contact_x, contact_y):
        return True
    return False

  def move(self, movement):
    # move head
    # then every block's position becomes its next block's position
    snake_head = self.head
    storage = [snake_head.x, snake_head.y]
    snake_head.x += movement[0]
    snake_head.y += movement[1]

    # handling wrap-around effect
    if snake_head.x >= 200:
      snake_head.x = 1
    elif snake_head.x <= 0:
      snake_head.x = 199
    elif snake_head.y >= 98:
      snake_head.y = 0
    elif snake_head.y <= 0:
      snake_head.y = 99

    for block in self.body:
      oldx = block.x
      oldy = block.y
      block.x = storage[0]
      block.y = storage[1]
      storage = [oldx, oldy]

  def draw(self, display):
    for piece in self.body:
      pygame.draw.rect(display, (255, 255, 255), piece) # drawing the snake

def ate_food(snake, food):
  if snake.head.colliderect(food):
    food_sound.set_volume(0.2)
    food_sound.play()
    fbody_p = snake.body[0]
    for _ in range(10):
      p = pygame.Rect(fbody_p.x, fbody_p.y, 4, 4)
      snake.body.append(p)
    # change the food's position
    food.x = random.randint(1, 180)
    food.y = random.randint(1, 80)

food_sound = pygame.mixer.Sound('./snake_game/coin1.mp3')
snakeh_image = pygame.image.load('./snake_game/snake_head.png')
snakeh_rect = snakeh_image.get_rect()
snakeh_rect.x = 50
snakeh_rect.y = 59
snake = Snake(snakeh_rect)
food = pygame.Rect(random.randint(1, 180), random.randint(1, 80), 4, 4)

snake_movement = [0, 0]
head_direction = 'down'
right = False
left = False
up = False
down = False

# window values
screen = pygame.display.set_mode((600, 400), 0, 32)
display = pygame.Surface((200, 100))

while True:
  display.fill((0, 0, 0))
  display.blit(snakeh_image, (snakeh_rect.x, snakeh_rect.y)) # blitting the snake image
  snake.draw(display)
  ate_food(snake, food)
  got_bit_body = snake.body_collision(head_direction)

  # ================== SNAKE MOVEMENT ==================
  if not got_bit_body:
    if right:
      snake.move([3, 0])
      display.blit(pygame.transform.rotate(snakeh_image, 90), (snakeh_rect.x, snakeh_rect.y))
    if left:
      snake.move([-3, 0])
      display.blit(pygame.transform.rotate(snakeh_image, -90), (snakeh_rect.x, snakeh_rect.y))
    if up:
      snake.move([0, -3])
      display.blit(pygame.transform.rotate(snakeh_image, 180), (snakeh_rect.x, snakeh_rect.y))
    if down:
      snake.move([0, 3])
      display.blit(pygame.transform.rotate(snakeh_image, 0), (snakeh_rect.x, snakeh_rect.y))
  if got_bit_body:
    for p in snake.body:
      pygame.draw.rect(display, (255, 0, 0), p)
  # ================== SNAKE MOVEMENT ==================

  pygame.draw.rect(display, (255, 0, 0), food) # drawing the food
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == KEYDOWN:
      if event.key == K_q:
        pygame.quit()
        sys.exit()
      if event.key == K_UP:
        if not down and not got_bit_body: # cant go down on the same axis
          head_direction='up'
          up = True
          down = False
          right = False
          left = False
      if event.key == K_DOWN:
        if not up and not got_bit_body: # cant go up on the same axis
          head_direction='down'
          down = True
          up = False
          right = False
          left = False
      if event.key == K_RIGHT:
        if not left and not got_bit_body: # cant go left on the same axis
          head_direction='right'
          right = True  
          down = False
          up = False
          left = False
      if event.key == K_LEFT:
        if not right and not got_bit_body: # cant go right on the same axis
          head_direction='left'
          left = True
          right = False
          down = False
          up = False

  screen.blit(pygame.transform.scale(display, (600, 400)), (0, 0)) # display becomes 2x bigger
  pygame.display.update()
  clock.tick(16)