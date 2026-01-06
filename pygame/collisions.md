# Game Collisions

## Getting Started
The most simple example is to demonstrate this physics through a group of rectangles which by convenience **Pygame** provides.

- Create a player rectangle: `player = pygame.Rect(top, left, width, height)`. Understand `top` and `left` as the very first pixel coordinates in the left top corner of the rect.
- Create two rectangle tiles and store in a variable: `tiles = [pygame.Rect(200, 350, 50, 50),pygame.Rect(260, 320, 50, 50)]`.

## Collision Test
This function returns a group of tiles that your rect collided with.

- This function will contain two main arguments: **the rect being tested for collision** and **the tiles which the rect collides with**.
- We will use `colliderect()` method from the `Rect` class that checks if one rect overlapped the other.

```py
def collision_test(rect, tiles):
  collisions = []
  for tile in tiles:
    if rect.colliderect(tile):
      collisions.append(tile)
  return collisions
```

## Movement
This is the main movement function in which you'd use for your main character.

- Takes three arguments: **the player rect**, **the movement tuple** and **a group of tiles**.
- `Rect` objects provide attributes like `left`, `right`, `top`, `bottom` to check or set the rectangle's edges. Changing these attributes moves the rectangle without directly changing its width or height.
- Create four flags for the four directions the rect will be able to move:
  ```py
  # movement flags
  right = False
  left = False
  up = False
  down = False
  ```
- Then for each `event.key` you toggle these flags on and off based on `KEYDOWN` or `KEYUP`.
- Create 4 conditions for the four movement directions:
  ```py
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
  ```
- Create the move function:
  ```py
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
  ```
- Lastly, call the `move()` function and assign it to your `player` variable so within the loop it will be always updated towards the direction you move, forever watching for collisions:
  ```py
  player = move(player, movement, tiles)
  ```
