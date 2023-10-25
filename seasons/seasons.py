from datetime import date, datetime
import re
import inflect
import sys


def get_date():
    user_input = input("Date of Birth: ")
    return user_input


def check_date(date):
    if test_user_input := re.search(r"^(\d{1,4})-(\d{1,2})-(\d{1,2})$", date):
        if (
            0 <= int(test_user_input.group(1)) <= 9999
            and 1 <= int(test_user_input.group(2)) <= 12
            and 1 <= int(test_user_input.group(3)) <= 31
        ):
            return date
        else:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


def main():
    p = inflect.engine()
    current_date = date.today()
    input_date = get_date()
    input_date = check_date(input_date)

    if input_date:
        input_date_object = date.fromisoformat(input_date)
        delta = current_date - input_date_object
        delta = str(delta).split(" ")
        delta = delta[0]
        delta = int(delta) * 24 * 60

        letters = p.number_to_words(delta, andword="")
        print(f"{letters.capitalize()} minutes")


if __name__ == "__main__":
    main()
