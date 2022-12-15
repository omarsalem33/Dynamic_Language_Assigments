import random
def Game():
    while True:
        guess = input('> ')  
        if guess.isdecimal():
            return int(guess)  
        print('Please enter a number between 1 and 100.')
 
print('Guess the Number, by Al Sweigart al@inventwithpython.com')
secretNumber = random.randint(1, 100)  
print('I am thinking of a number between 1 and 100.')
 
for i in range(10):  
    print('You have {} guesses left. Take a guess.'.format(10 - i))
    guess = Game()
    if guess == secretNumber:
        break  
    elif guess < secretNumber:
        print('Your guess is  low.')
    elif guess > secretNumber:
         print('Your guess is high.')
 
if guess == secretNumber:
     print('congrats! You guessed my number!')
else:
     print('Game over. The number I was thinking of was', secretNumber)