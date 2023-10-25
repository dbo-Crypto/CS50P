def main():
    menu = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
    total = 0
    while True:
        try:
            user_input = input("Item: ")
            user_input = user_input.title()
            if user_input in menu:
                total = total + menu[user_input]
                print(f"${'%.2f' % total}")
            elif user_input == "":
                break
        except EOFError:
            break

main()