"""
Level 1:
Task 2:
Write a python program that randomly generates a number between 1 and 100.The user has to guess the number,
and the program will give feedback if the guess is too high or too low.
"""

import random
num = random.randint(1, 100)
max_attempts = 5
attempts = 0

print('Guess the number between 1 to 100')
while attempts < max_attempts:
    guess = int(input(f'Attempt {attempts+1}: Enter your guess: '))
    attempts += 1

    if guess == num:
        print('Congratulations!! You guessed it right.')
        break
    elif guess < num:
        print('Too Low!')
    else:
        print('Too High!')

if attempts == max_attempts and guess != num:
    print('You have used all your attempts!!')
    print(f'Sorry!, The correct number was {num}.')
