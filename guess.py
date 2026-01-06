import random

# inputs always return strings, even though you've wrote a number
number_cap = input('Type a number: ')

# while the number cap is not a number or smaller than or equal to 0
while (number_cap.isdigit() == False or int(number_cap) <= 0):
  # ask for a number again
  number_cap = input('Please type a number bigger than 0. No words expected: ')
  
# store the random number
r = random.randint(0, int(number_cap))

print(r)

while True:
  answer = input(f'\nGuess a number between 0 and {r}\n')

  if not answer.isdigit():
     print('\nThat was not a number')
     continue

  if int(answer) == r:
    print('\nYou win!\n')
    break
  else:
    print('\nWRONG!!!\n')
    continue