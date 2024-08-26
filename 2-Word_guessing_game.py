import random

name = input('Enter name:')

print('Welcome !',name)

words = ['random', 'sharp', 'soft', 'office', 
         'silence', 'method', 'computer' ]

word = random.choice(words)

print('Guess the character')

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:

            print(char, end=" ")

        else:
            print("_")

            failed += 1

    if failed == 0:

        print('\nYou win')

        print(f'The word is {word}')
        break

    print()

    guess = input('Enter the guess char:')

    guesses += guess

    if guess not in word:
        print('wrong')
        
        turns -= 1

        print(f'you left only {turns}')

        if turns == 0:
            print('you lose')


