import random

print ('Hi! Welcome to the "Guess the number" game. Let us start of by telling me your name.')
name = input ()

print ('Nice to meet you, ' + name + '. I am thinking of a number between 1 and 20')
secretNumber = random.randint (1, 20)

for guessesTaken in range (1, 7):
    print ('Take a guess.')
    guess = int (input ())

    if guess < secretNumber:
        print ('Your guess is too low.')
    elif guess > secretNumber:
        print ('Your guess is too high')
    else:
        break
if guess == secretNumber:
    print ('Good job, ' + name + '! You guessed my number in ' + str (guessesTaken) + ' guesses')
else:
    print ('Nope. The number I was thinking was ' + str (secretNumber))
    
    
