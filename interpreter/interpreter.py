user_input = input("Expression: ")
user_input = user_input.strip()


if "+" in user_input:
    user_input = user_input.split("+")
    for i in range (0,len(user_input)):
        user_input[i] = float(user_input[i])
    print(user_input[0]+user_input[1])
elif "-" in user_input:
    user_input = user_input.split("-")
    for i in range (0,len(user_input)):
        user_input[i] = float(user_input[i])
    print(user_input[0] - user_input[1])
elif "*" in user_input:
    user_input = user_input.split("*")
    for i in range (0,len(user_input)):
        user_input[i] = float(user_input[i])
    print(user_input[0] * user_input[1])
elif "/" in user_input:
    user_input = user_input.split("/")
    for i in range (0,len(user_input)):
        user_input[i] = float(user_input[i])
    print(user_input[0] / user_input[1])

