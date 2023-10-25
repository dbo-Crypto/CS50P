user_input = input("Input: ").strip()
letters = ["a","e","i","o","u","A","E","I","O","U"]
for i in user_input:
    if i in letters:
        user_input = user_input.replace(i, "")
print(user_input)