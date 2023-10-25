import validators

def main():
    email = input("What's yoiur email address? ")
    print(validate(email))

def validate(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

main()