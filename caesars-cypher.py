import sys

def encrypt(key):
  
  sentence = input('Enter your message:\n')

  # make the sentence a list of characters
  sentence_list = list(''.join(sentence.strip()))

  encrypted_sentence = []

  # move the sentence letters "key" times foward
  for letter in sentence_list:
    if letter.isalnum():
      unicode_value = ord(letter)
      encrypted_value = ((unicode_value - 97 + key) % 26) + 97 # modular arithmetic
      encrypted_sentence.append(chr(encrypted_value))
    else:
      encrypted_sentence.append(letter)

  print(f'Your translated text is:\n{''.join(encrypted_sentence)}\n')
  

def decrypt(key):
  sentence = input('Enter your message:\n')

  # make the sentence a list of characters
  sentence_list = list(''.join(sentence.strip()))

  decrypted_sentence = []

  # move the sentence letters "key" times foward
  for letter in sentence_list:
    if letter.isalnum():
      unicode_value = ord(letter)
      encrypted_value = ((unicode_value - 97 - key) % 26) + 97 # modular arithmetic
      decrypted_sentence.append(chr(encrypted_value))
    else:
      decrypted_sentence.append(letter)

  print(f'Your translated text is:\n{''.join(decrypted_sentence)}\n')
  

def main():

  MAX_KEY_SIZE = 52

  while True:
    answer = input('Do you wish to encrypt or decrypt a message?\n')

    if answer.lower() == 'encrypt':
      while True:
        key = input('Enter the key number (1-52)\n')

        if not key.isdigit(): # key needs to be a digit
          print('Not a valid key number, it needs to be (1-52)\n')

        elif int(key) <= 0 or int(key) > MAX_KEY_SIZE: # key can't be negative or zero
          print('No negatives or zero values, it needs to be (1-52)\n')

        else: # if every other condition passed, call the function
          encrypt(int(key))
          break

    elif answer.lower() == 'decrypt':
      while True:
        key = input('Enter the key number (1-52)\n')

        if not key.isdigit(): # key needs to be a digit
          print('Not a valid key number, it needs to be (1-52)\n')

        elif int(key) <= 0 or int(key) > MAX_KEY_SIZE: # key can't be negative or zero
          print('No negatives, big or zero values, it needs to be (1-52)\n')

        else: # if every other condition passed, call the function
          decrypt(int(key))
          break

    # quit the game
    elif answer.lower() == 'quit' or answer.lower() == 'q' or answer.lower() == 'no':
      sys.exit()

    else:
      print("Enter either 'decrypt or 'encrypt'!\n")


# running main program
main()