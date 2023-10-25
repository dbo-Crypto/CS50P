import inflect

def main():
    list_names = []
    p = inflect.engine()
    while True:
        try:
            user_input = input()
            if user_input != None:
                list_names.append(user_input)
        except EOFError:
            res = p.join(list_names)
            print(f"Adieu, adieu, to {res}")
            break
main()