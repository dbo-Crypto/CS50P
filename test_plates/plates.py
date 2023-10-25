def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s.isalnum():
            if s.isalpha():
                return True
            elif s[0].isalpha and s[1].isalpha():
                if s[2].isnumeric() and s[2] == "0":
                    return False
                else:
                    if s[-1].isalpha():
                        return False
                    elif s[-1].isnumeric() and s[-2].isalpha():
                        for i in range(4, len(s)):
                            if s[i].isalpha():
                                return False
                            else:
                                return True
                    else:
                        return True
            else:
                return False














    # e = s
    # s = [*s]
    # if 2 <= len(s) <= 6:
    #     if e.isalpha():
    #         return True
    #     elif e.isalnum() and s[-1].isalpha():
    #         return False
    #     elif e.isalnum() == False:
    #         return False

    #     if s[0].isalpha() and s[1].isalpha():
    #         for i in range(0, len(s)):
    #             d = 0
    #             if s[i].isnumeric():

    #                 c = 0
    #                 if s[i] != "0":
    #                     c = 1
    #                     if s[i].isalnum() and e[:-1].isalpha():
    #                         #print("1")
    #                         return False
    #                     for i in range(6, len(s)):
    #                         d = 1

    #                         #print(s[i]+"  "+s[i-1])
    #                         if s[i].isalpha() and s[i-1].isnumeric() and c == 1 and d == 0:
    #                             #print("3")
    #                             #print(str(s[i]))
    #                             return False
    #                         else:
    #                             return True
    #                     else:
    #                         return True
    #                 elif s[i] =="0" and c == 0:
    #                     #print("2")
    #                     return False

    #     else:
    #         return False

main()