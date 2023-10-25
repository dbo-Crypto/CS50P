import sys

def main():
    user_input = input("Fraction: ")
    res = convert(user_input)
    res = gauge(res)
    print(res)


def convert(fraction):
    fraction = fraction.split("/")
    while True:
        try:
            x = round((int(fraction[0]) / int(fraction[1])), 2) * 100
            if x >100:
                x = input("Fraction: ")
                pass
            else:
                return x
        except (ValueError, ZeroDivisionError):
            x = input("Fraction: ")
            pass


def gauge(percentage):
    percentage = int(percentage)
    if percentage >= 99:
            return "F"
    elif percentage <= 1:
            return "E"
    else:
            return (f"{percentage}%")


if __name__ == "__main__":
    main()