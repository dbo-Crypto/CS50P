# while True:
#         user_input = input("Fraction: ")
#         user_input = user_input.split("/")
#         try:
#             x = (int(user_input[0]) / int(user_input[1])) * 100
#             print(x)
#             if x == 0:
#                 res = "E"
#             elif x == 100:
#                 res = "F"
#             else:
#                 res = int(x)+'%'
#         except:
#             pass



def main():

    x = int(fraction())
    if x >= 99:
        print("F")
    elif x <= 1:
        print("E")
    else:
        print(f"{x}%")


def fraction():
    while True:
        try:
            user_input = input("Fraction: ")
            user_input = user_input.split("/")
            x = round((int(user_input[0]) / int(user_input[1])), 2) * 100
            if x >100:
                pass
            else:
                return x
        except (ValueError, ZeroDivisionError):
            pass

main()