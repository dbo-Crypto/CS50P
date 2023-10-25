user_input = input("Greeting: ")
user_input = user_input.lower().strip().split()

if user_input[0] == "hello" or user_input[0] == "hello,":
    print("$0")
elif user_input[0][0] == "h":
    print("$20")
else:
    print("$100")