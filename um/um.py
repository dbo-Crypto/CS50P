import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"(^|[^a-zA-Z0-9])um(\W| |$)", s.lower()))


if __name__ == "__main__":
    main()
