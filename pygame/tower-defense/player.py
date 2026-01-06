import pygame
from utils import load_image

player_subpath = ['assets', 'graphics', 'player']
player_idle_1 = load_image('player_idle_1.png', player_subpath)
player_idle_2 = load_image('player_idle_2.png', player_subpath)
player_walk_1 = load_image('player_walk_1.png', player_subpath)
player_walk_2 = load_image('player_walk_2.png', player_subpath)
player_walk_3 = load_image('player_walk_3.png', player_subpath)
player_walk_4 = load_image('player_walk_4.png', player_subpath)

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.player_frames = [player_idle_1, player_idle_2]
    self.player_index = 0
    self.image = self.player_frames[self.player_index]
    self.rect = self.image.get_rect()
    self.rect.midbottom = (x, y)
    self.state = 'idle'
    self.move_dir_x = 0
    self.move_dir_y = 0
    self.flip = False

  def set_direction(self, dir):
    if dir == 'left':
      self.move_dir_x -= 3
      self.state = 'run'
      if self.flip != False: 
        self.flip = False

    elif dir == 'right':
      self.move_dir_x += 3
      self.state = 'run'
      if self.flip != True:
        self.flip = True

    else: 
      self.move_dir_x = 0
      self.player_index = 0 # prevents list index out of range error
      self.state = 'idle'

  def animation(self):
    if self.state == 'idle':
      self.player_frames = [player_idle_1, player_idle_2]
    else:
      self.player_frames = [
        player_walk_1,
        player_walk_2,
        player_walk_3,
        player_walk_4
      ]

    self.player_index += 0.1
    if int(self.player_index) == len(self.player_frames): 
      self.player_index = 0   

    self.image = pygame.transform.flip(self.player_frames[int(self.player_index)], self.flip, False)

  def update(self):
    self.animation()
    x, y = self.rect.midbottom
    x += self.move_dir_x
    y += self.move_dir_y
    self.rect.midbottom = (x, y)