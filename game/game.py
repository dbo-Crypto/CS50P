import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            result = random.randint(1, int(level))
            break
        else:
            pass
    except:
        pass
while True:
    try:
        guess = input("Guess: ")
        if guess.isnumeric():
            if int(guess) == result:
                print("Just right!")
                break
            elif int(guess) < result:
                print("Too small!")
            elif int(guess) > result:
                print("Too large!")
        else:
            pass
    except EOFError:
        pass
