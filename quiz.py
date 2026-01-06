print('Welcome to my quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
  quit()

print("Okay! Let's play")

## game starts

points = 0

answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
  points += 1
  print('Correct!')
else:
  if points - 1 >= 0:
    points -= 1
  print('Wrong!')
print(f'Points: {points}')
  
answer = input('What does GPU stand for? ')
if answer.lower() == 'graphic processing unit':
  points += 1
  print('Correct!')
else:
  if points - 1 >= 0:
    points -= 1
  print('Wrong!')
print(f'Points: {points}')

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
  points += 1
  print('Correct!')
else:
  if points - 1 >= 0:
    points -= 1
  print('Wrong!')
print(f'Points: {points}')

answer = input('What does PSU stand for? ')
if answer.lower() == 'power supply':
  points += 1
  print('Correct!')
else:
  if points - 1 >= 0:
    points -= 1
  print('Wrong!')
print(f'Points: {points}')

if points >= 3:
  print('\n You won! \n')
else:
  print('\n You loose, you need at least 3 points to win. \n')