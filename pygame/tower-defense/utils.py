from os import path
import pygame

def load_image(img_name, subpath):
  dir = path.dirname(__file__) # gets the file's directory absolute path
  img_path = path.join(dir, *subpath, img_name) # creates the image path
  return pygame.image.load(img_path) # returns the image surface