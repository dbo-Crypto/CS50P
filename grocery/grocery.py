def main():
    grocerylist = grocery_list()
    sorted = {}
    listed_grocerylist = list(grocerylist)
    listed_grocerylist.sort()
    for i in listed_grocerylist:
        sorted[i] = grocerylist[i]

    for i in sorted:
        print(f"{sorted[i]} {i}")

def grocery_list():
    grocerylist = {}
    while True:
        try:
            user_input = input("")
            user_input = user_input.upper()
            if user_input == "":
                return grocerylist
            else:
                if user_input in grocerylist:
                    grocerylist[user_input] = grocerylist[user_input] + 1
                else:
                    grocerylist[user_input] = 1
        except EOFError:
            return grocerylist

main()