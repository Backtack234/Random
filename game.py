import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1, {x} '))
        if guess > random_number:
            print("Too high, Try again.")
        elif guess < random_number:
            print("Too low, Try again.")
    
    print("You got it!!")
guess(x = random.randint(1, 1000))

