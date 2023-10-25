import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s
    ):
        if matches.group(3) == "AM" and 0 <= int(matches.group(1)) <= 12:
            if int(matches.group(1)) == 12:
                hour1 = "00"
            elif int(matches.group(1)) < 10:
                hour1 = f"0{matches.group(1)}"
            else:
                hour1 = matches.group(1)
            if matches.group(2) == None:
                minute1 = "00"
            elif matches.group(2) != None and 0 <= int(matches.group(2)) < 60:
                minute1 = matches.group(2)
            else:
                raise ValueError

        elif matches.group(3) == "PM" and 0 <= int(matches.group(1)) <= 12:
            if int(matches.group(1)) == 12:
                hour1 = "12"
            else:
                hour1 = int(matches.group(1)) + 12
            if matches.group(2) == None:
                minute1 = "00"
            elif matches.group(2) != None and 0 <= int(matches.group(2)) < 60:
                minute1 = matches.group(2)
            else:
                raise ValueError

        else:
            raise ValueError

        if matches.group(6) == "AM" and 0 <= int(matches.group(4)) <= 12:
            if int(matches.group(4)) == 12:
                hour2 = "00"
            elif int(matches.group(4)) < 10:
                hour2 = f"0{matches.group(4)}"
            else:
                hour2 = matches.group(4)
            if matches.group(5) == None:
                minute2 = "00"
            elif matches.group(5) != None and 0 <= int(matches.group(5)) < 60:
                minute2 = matches.group(5)
            else:
                raise ValueError

        elif matches.group(6) == "PM" and 0 <= int(matches.group(4)) <= 12:
            if int(matches.group(4)) == 12:
                hour2 = "12"
            else:
                hour2 = int(matches.group(4)) + 12
            if matches.group(5) == None:
                minute2 = "00"
            elif matches.group(5) != None and 0 <= int(matches.group(5)) < 60:
                minute2 = matches.group(5)
            else:
                raise ValueError

        else:
            raise ValueError

        new_time = f"{hour1}:{minute1} to {hour2}:{minute2}"
        return new_time
    else:
        raise ValueError


if __name__ == "__main__":
    main()
