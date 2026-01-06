# Game Setup

## First Steps
- Import `pygame` and `sys`.
- Instantiate a clock variable from `pygame.time.Clock()` for the frame rates. Its `.tick()` method basically caps the fps at a stable speed so it doesn't run as fast as the CPU allows.
- Get all the event/key/window constants into the current scope of the game with `from pygame.locals import *`.
- Initialize pygame modules with `pygame.init()`.
- Write a title for your game window with `pygame.display.set_caption('Title')`.
- Create a main display surface with `pygame.display.set_mode((x_size, y_size), 0, 32)`.

## Main Loop
- Create a `while True:` loop to be your main game loop.
- Write a for loop to watch for events like quit, keyboard or mouse events:
  ```py
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  ```
- And then for the arrow keys for example you can write:
  ```py
  if event.type == KEYDOWN:
    if event.key == K_UP:
      # some logic...

  if event.type == KEYUP:
    if event.key == K_UP:
      # some logic...  
  ```
- Also make sure you fill (repaint) the screen with a background color every frame update with `screen.fill((0, 0, 0))`. This will prevent moving object trails and wipe old drawings out the screen.
- Write `pygame.display.update()` so all objects of your game are drawn onto the `screen` surface.
- Lastly write `clock.tick(60)` for your frame rates cap.