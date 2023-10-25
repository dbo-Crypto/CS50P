import random


def main():
    level = get_level()
    score = 0
    while True:

        for i in range(0,10):
            x = generate_integer(level)
            y = generate_integer(level)
            res = x + y
            error_count = 0
            while True:
                answer = input(f"{x} + {y} = ")
                if answer.isnumeric() and int(answer) == res:
                    score += 1
                    break
                elif res != int(answer) and error_count < 2:
                        error_count += 1
                        #answer = input(f"{x} + {y} = ")
                        print("EEE")
                        pass
                else:
                    print("EEE")
                    print(f"{x} + {y} = {res}")
                    break
        print(f"Score: {score}")
        break







def get_level():
    while True:
        user_input = input("Level: ")
        try:
            if user_input in ["1", "2", "3"]:
               return int(user_input)
            else:
                print("Level is not 1, 2 or 3")
                pass
        except EOFError:
            break


def generate_integer(level):
    if level == 1:
        start = 0
        end = (10**level)-1
        return random.randint(start, end)
    else:
        start = 10**(level-1)
        end = (10**level)-1
        return random.randint(start, end)


if __name__ == "__main__":
    main()