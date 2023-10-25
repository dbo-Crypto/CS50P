def main():
    user_input = input("Input: ").strip()
    res = shorten(user_input)
    print(res)


def shorten(word):
    letters = ["a","e","i","o","u","A","E","I","O","U"]
    for i in word:
        if i in letters:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()