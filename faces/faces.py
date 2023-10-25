user_input = input()
user_input = user_input.split()
for i in range (0, len(user_input)):
    if user_input[i] == ':)':
        user_input[i] = "\U0001F642"
    elif user_input[i] == ':(':
        user_input[i] = "\U0001F641"
user_input = ' '.join(user_input)
print(user_input)