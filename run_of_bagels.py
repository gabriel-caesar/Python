import random

def main():
    counter = 1 # counter of how many guesses
    number = str(random.randint(100, 999)) # converting to str
    state = '' # Fermi, Pico or Bagels

    print('I am thinking of a 3-digit number. Try to guess what it is. You have 10 guesses to get it.')

    while(True):
        print(state)
        # reset the state
        state = '' 
        print(f'Guess #{counter}')
        answer = input()
        # checking if user input is digit and 3 numbers long
        if len(list(answer)) == 3 and answer.isdigit():

            # limiting the user to 10 guesses
            if counter == 10:
                print("You didn't get it before 10 guesses.")
                break

            # base case
            if answer == number:
                print('You got it!')
                response = input('Do you want to play again? (yes or no)')
                if response == 'yes':
                    main()
                elif response == 'no':
                    break
                else:
                    print('yes or no?')
             
            
            for i in range(len(list(number))):
                if answer[i] == number[i]:
                    state = f'Fermi on {answer[i]}'
                elif answer[i] in number and answer[i] != number[i]:
                    # because I think Fermi is more important
                    if state != 'Fermi':
                        state = f'Pico on {answer[i]}'
                else:
                    if state == '':
                        state = 'Bagels'
                
        
            # increment counter if any of the conditions were met
            counter += 1    
        else:
            print('Three digits number, please')
           

main()
