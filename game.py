import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    guesses = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1, {x} '))
        if guess > random_number:
            print("Too high, Try again!")
            guesses = guesses + 1
        elif guess < random_number:
            print("Too low, Try again.")
            guesses = guesses + 1

        if guesses == 1:
            print('You have 4 guesses left!')
        elif guesses == 2:
            print('You have 3 guesses left!')
        elif guesses == 3:
            print('You have 2 guesses left!')
        elif guesses == 4:
            print('You have 1 guess left!')
        else:
            print("You have no guesses left")
            break

    print("You got it!! It only took you " + str(guesses) + " guesses!")
    

guess(x = random.randint(1,1000))
