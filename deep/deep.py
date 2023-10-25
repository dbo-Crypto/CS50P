user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
user_input = user_input.lower().strip()
match user_input:
    case "42" | "forty two" | "forty-two":
        print("yes")
    case _:
        print("no")