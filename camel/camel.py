user_input = input("camelCase: ").strip()
user_input = [*user_input]
for i in range (0, len(user_input)):
    if user_input[i].isupper():
        user_input[i] = user_input[i].replace(user_input[i],"_"+user_input[i].lower())
print("".join(user_input))